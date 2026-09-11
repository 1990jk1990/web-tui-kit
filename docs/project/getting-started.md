# Getting started

## Prerequisites

A modern browser is sufficient to use the library. Python 3 is convenient for serving the demo locally and is used by repository validation tooling.

## Choose a version

For a consuming application, pin an immutable release tag rather than depending on the moving `main` branch. For the current stable release:

```bash
git clone --branch v1.0.0 --depth 1 https://github.com/1990jk1990/web-tui-kit.git
cd web-tui-kit
```

Maintainers working on the design system itself should clone the normal development branch instead.

## Run the demo

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/demo/`.

The server-rendered integration recipe is also directly browser-openable at `http://localhost:8000/examples/server-rendered/package-configuration.html`.

## Integrate into another application

Vendor or copy the files under `src/`, then load them in this order:

```html
<link rel="stylesheet" href="/ui/tokens.css">
<link rel="stylesheet" href="/ui/tui.css">
<script src="/ui/tui.js" defer></script>
```

`src/tui.js` is optional if the consuming application does not need the progressive Escape/list-navigation helpers. Record the source release tag next to a vendored copy so future updates are deliberate and traceable.

Tagged GitHub Releases include a focused `web-tui-kit-MAJOR.MINOR.PATCH.zip` plus SHA-256 checksum. That archive contains the runtime, executable demos, framework/template integration recipes, `docs/project/public-contract.md`, version/changelog/security information, and practical design-system/AI-agent guidance without requiring the full development repository. Pre-1.0 `v0.*` tags are prereleases; stable-line tags starting with `v1.0.0` are normal GitHub Releases.

The supported downstream token/class/state/data-attribute/event and semantic-markup surface is inventoried in `docs/project/public-contract.md`. Starting with 1.0, normal Semantic Versioning applies to that declared public contract. The CSS usage patterns are described in `DESIGN_SYSTEM.md`; accepted behavior is canonical in `openspec/specs/`.

## React, Vue, and templates

Applications that already use React, Vue, or server-side templates still consume the same browser-native runtime. Start with `docs/project/framework-integration.md` and the matching source under `examples/`.

The framework owns application state/lifecycle; `web-tui-kit` owns the declared visual classes, native-control patterns, CSS custom properties, and small progressive JavaScript contract. Do not create a parallel framework-specific theme or copy component CSS into scoped/CSS-in-JS styles.

## No build or package-manager requirement

The runtime baseline is directly consumable by browsers. A consuming application may have its own build system or framework; `web-tui-kit` itself does not require Node.js, npm, a bundler, or another package registry for runtime use.
