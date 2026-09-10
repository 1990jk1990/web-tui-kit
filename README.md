# web-tui-kit

A reusable, framework-independent browser UI design system inspired by Debian debconf, `dialog`, and `whiptail`.

The project is the canonical UI reference for browser-based applications that should share the same text-oriented visual language on Linux desktops and Android devices.

**Version:** `0.5.0` (pre-1.0). The canonical version is stored in `VERSION`; released versions use immutable `vMAJOR.MINOR.PATCH` Git tags.

## Quick start

Clone the repository and serve it with any static web server:

```bash
git clone https://github.com/1990jk1990/web-tui-kit.git
cd web-tui-kit
python3 -m http.server 8000
```

Open:

- `http://localhost:8000/demo/` for the canonical package-configuration reference,
- `http://localhost:8000/demo/dialogs.html` for message, confirmation, input, menu, radiolist, checklist, and gauge patterns,
- `http://localhost:8000/demo/components.html` for the broader component gallery,
- `http://localhost:8000/examples/server-rendered/package-configuration.html` for the browser-openable template/server-rendered integration recipe.

No application build step and no JavaScript framework are required.

## Distribution and use in another project

For reproducible downstream use, pin an immutable release tag instead of copying from the moving `main` branch. For the current release line:

```bash
git clone --branch v0.5.0 --depth 1 https://github.com/1990jk1990/web-tui-kit.git
```

Copy or vendor the files from `src/` and include them in the consuming application:

```html
<link rel="stylesheet" href="/ui/tokens.css">
<link rel="stylesheet" href="/ui/tui.css">
<script src="/ui/tui.js" defer></script>
```

`src/tui.js` is optional when the consuming application does not need the small progressive keyboard enhancements. The exact CSS token values are defined in `src/tokens.css`; reusable component implementation lives in `src/tui.css` and `src/tui.js`.

Tagged GitHub prereleases provide a focused `web-tui-kit-MAJOR.MINOR.PATCH.zip` and matching SHA-256 checksum containing the runtime, executable demos, framework/template integration recipes, version marker, changelog, security guidance, and practical design-system/AI-agent references. Pre-1.0 releases do not require or publish an npm package; direct tagged vendoring is the primary distribution model.

For the closest match to the original Debian/Ubuntu package-configuration look, start from `.tui-screen`, `.tui-dialog`, `.tui-dialog-title`, `.tui-checklist`, `.tui-check-row`, `.tui-actions`, and `.tui-button` as demonstrated in `demo/index.html`.

For common dialog compositions, use `demo/dialogs.html` and `DESIGN_SYSTEM.md` rather than inventing per-application variants. Containers marked with `data-tui-list` gain optional ArrowUp/ArrowDown/Home/End focus navigation while normal Tab reachability and native control activation remain intact.

## Framework and template consumers

React, Vue, and server-rendered applications should generate the same semantic markup/classes instead of using a separate adapter runtime. Copy-ready recipes live under `examples/`, with detailed guidance in `docs/project/framework-integration.md`.

The React/Vue examples demonstrate framework-owned state and lifecycle handling while keeping native form controls. The server-rendered recipe demonstrates ordinary form submission. All three reuse the canonical `src/` assets and treat `tui:escape` as an application-owned signal.

Do not copy the design tokens/component CSS into CSS-in-JS, scoped component styles, or a private theme implementation. If a reusable visual change is needed, make it in the canonical design system.

See `RELEASING.md` for the versioning/release procedure and `docs/project/compatibility.md` for current compatibility evidence and its limits.

## Project memory and canonical sources

This repository follows **AI-DOC-1 v1.3**. The repository itself is durable project memory; chat history is not required to continue development.

- AI working rules: `AGENTS.md`
- release identity: `VERSION` + immutable Git tags/GitHub Releases
- release procedure: `RELEASING.md`
- project purpose and scope: `docs/project/overview.md`
- compatibility evidence: `docs/project/compatibility.md`
- framework integration guidance: `docs/project/framework-integration.md`
- accepted UI/release/integration behavior: `openspec/specs/`
- current architecture: `docs/architecture/`
- durable decision rationale: `docs/decisions/`
- practical design-system usage guide: `DESIGN_SYSTEM.md`
- exact design-token values: `src/tokens.css`
- implementation: `src/`
- primary executable visual reference: `demo/index.html`
- core dialog gallery: `demo/dialogs.html`
- broader component gallery: `demo/components.html`
- framework/template consumption recipes: `examples/`
- structural regression evidence: `tests/`
- reviewed visual baselines: `tests/visual/baselines/`

See `docs/index.md` for the documentation entry point.

## Prompt for ChatGPT / coding assistants

For a stable released reference, a consuming project can use:

> Use `https://github.com/1990jk1990/web-tui-kit/tree/v0.5.0` as the canonical UI design system. Read `AGENTS.md`, `VERSION`, the current OpenSpec specifications, `DESIGN_SYSTEM.md`, and `demo/index.html` before implementing UI. If the target app uses React, Vue, or server-rendered templates, also read `docs/project/framework-integration.md` and the matching example under `examples/`. Treat `demo/index.html` as the primary visual target, `demo/dialogs.html` as the core dialog catalog, and `demo/components.html` as the broader component catalog. Reuse the existing tokens, CSS classes, semantic controls, and interaction patterns instead of inventing a new visual language or framework-specific styling layer. The application must remain usable in Linux desktop browsers and Android browsers.

Using an immutable release tag is preferable to pointing an automated consumer at `main`, because the visual and behavioral reference cannot change underneath that consumer.

## Verification

Run the fast repository/documentation checks with:

```bash
python -m unittest discover -s tests -v
python scripts/validate_ai_doc_1.py
pip install -r requirements-docs.txt
python scripts/sync_openspec_docs.py
mkdocs build --strict
```

Run the browser-driven screenshot regression suite with:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium
python scripts/visual_regression.py
```

Build and verify the focused release archive with:

```bash
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

The visual suite compares the canonical package and dialog demos against reviewed desktop/touch-mobile PNG baselines. See `docs/project/testing.md` for the visual baseline procedure and canonical CI environment.

Contribution details are in `CONTRIBUTING.md`; release-maintainer steps are in `RELEASING.md`.
