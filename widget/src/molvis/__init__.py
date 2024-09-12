import pathlib
import anywidget
import traitlets
import logging

import molpy as mp

logger = logging.getLogger("molvis-widget-py")

_DEV = True

if _DEV:
    # from `npx vite`
    ESM = "http://localhost:5173/src/index.ts?anywidget"
    CSS = ""
else:
    # from `npx vite build`
    bundled_assets_dir = pathlib.Path(__file__).parent.parent / "static"
    ESM_path = bundled_assets_dir / "molvis.js"
    assert ESM_path.exists(), f"{ESM_path} not found"
    ESM = ESM_path.read_text()
    CSS = (bundled_assets_dir / "style.css").read_text()


class Molvis(anywidget.AnyWidget):

    _esm = ESM
    _css = CSS

    width = traitlets.Int(800).tag(sync=True)
    height = traitlets.Int(600).tag(sync=True)
    ready = traitlets.Bool(False).tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send_cmd(self, method: str, params:dict, buffers: list):
        jsonrpc = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
        }
        self.send(jsonrpc, buffers=buffers)

    def add_atom(self, atom: mp.Atom):

        atom_dict = atom.to_dict()
        if 'xyz' in atom_dict:
            xyz = atom_dict.pop('xyz')
            atom_dict['x'], atom_dict['y'], atom_dict['z'] = xyz
        self.send_cmd("add_atom", atom_dict, [])
        return self
    
    def add_bond(self, bond: mp.Bond):
        self.send_cmd("add_bond", bond.to_dict(), [])
        return self
    
    
    def add_struct(self, struct: mp.Struct):
        for atom in struct.atoms:
            self.add_atom(atom)
        for bond in struct.bonds:
            self.add_bond(bond)
        return self