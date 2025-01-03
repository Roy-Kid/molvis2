import { defineConfig } from "vite";
import anywidget from "@anywidget/vite";

export default defineConfig({
	build: {
		outDir: "src/static",
		lib: {
			entry: ["src/index.ts"],
			formats: ["es"],
		},
		rollupOptions:{
			"output": {
				"inlineDynamicImports": true,
				"entryFileNames": "molvis.js"
			}
		}
	},
	optimizeDeps: {
		include: ["@anywidget/core"]
	},
    plugins: [anywidget()],
});