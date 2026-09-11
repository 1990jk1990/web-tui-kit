import { readFile, mkdir, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { compileScript, parse } from "@vue/compiler-sfc";
import { build } from "esbuild";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "../..");
const output = path.join(root, "test-results", "framework");
const nodePaths = [path.join(here, "node_modules")];

await mkdir(output, { recursive: true });

const pageTemplate = (bundleName) => `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>web-tui-kit framework recipe verification</title>
  <link rel="stylesheet" href="/src/tokens.css">
  <link rel="stylesheet" href="/src/tui.css">
  <script src="/src/tui.js" defer></script>
</head>
<body class="tui-desktop">
  <div id="app"></div>
  <script>window.__frameworkEvents = [];</script>
  <script type="module" src="./${bundleName}"></script>
</body>
</html>
`;

await build({
  stdin: {
    contents: `
      import { createRoot } from "react-dom/client";
      import { PackageConfiguration } from "./examples/react/PackageConfiguration.jsx";

      const root = createRoot(document.querySelector("#app"));
      root.render(
        <PackageConfiguration
          onAccept={(services) => window.__frameworkEvents.push({ type: "accept", services })}
          onCancel={() => window.__frameworkEvents.push({ type: "cancel" })}
        />,
      );
    `,
    loader: "jsx",
    resolveDir: root,
    sourcefile: "framework-react-entry.jsx",
  },
  bundle: true,
  format: "esm",
  platform: "browser",
  target: "es2022",
  jsx: "automatic",
  nodePaths,
  outfile: path.join(output, "react.js"),
  logLevel: "warning",
});
await writeFile(path.join(output, "react.html"), pageTemplate("react.js"), "utf8");

const vueRecipeRelativePath = "examples/vue/PackageConfiguration.vue";
const vueRecipePath = path.join(root, ...vueRecipeRelativePath.split("/"));
const vueSource = await readFile(vueRecipePath, "utf8");
const parsed = parse(vueSource, { filename: vueRecipePath });
if (parsed.errors.length) {
  throw new Error(`Vue SFC parse failed: ${parsed.errors.join("; ")}`);
}

const compiled = compileScript(parsed.descriptor, {
  id: "web-tui-kit-package-configuration",
  inlineTemplate: true,
});
const vueComponentPath = path.join(output, "vue-component.mjs");
await writeFile(vueComponentPath, compiled.content, "utf8");

await build({
  stdin: {
    contents: `
      import { createApp } from "vue";
      import PackageConfiguration from "./vue-component.mjs";

      createApp(PackageConfiguration, {
        onAccept: (services) => window.__frameworkEvents.push({ type: "accept", services }),
        onCancel: () => window.__frameworkEvents.push({ type: "cancel" }),
      }).mount("#app");
    `,
    loader: "js",
    resolveDir: output,
    sourcefile: "framework-vue-entry.js",
  },
  bundle: true,
  format: "esm",
  platform: "browser",
  target: "es2022",
  nodePaths,
  outfile: path.join(output, "vue.js"),
  logLevel: "warning",
});
await rm(vueComponentPath, { force: true });
await writeFile(path.join(output, "vue.html"), pageTemplate("vue.js"), "utf8");

console.log(`Built framework verification fixtures in ${path.relative(root, output)}`);
