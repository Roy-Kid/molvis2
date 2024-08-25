import {Molvis} from './src/app';

const canvas = document.createElement('canvas');
document.body.appendChild(canvas);

const molvis = new Molvis(canvas);
molvis.render();


const atom1 = molvis.add_atom(0, 0, 0, new Map());
const atom2 = molvis.add_atom(2, 0, 0, new Map());
molvis.add_bond(atom1, atom2);