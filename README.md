# web-tui-kit

A reusable, framework-independent browser UI design system inspired by Debian debconf, `dialog`, and `whiptail`.

The project is the canonical UI reference for browser-based applications that should share the same text-oriented visual language on Linux desktops and Android devices.

**Version:** `0.4.0` (pre-1.0). The canonical version is stored in `VERSION`; released versions use immutable `vMAJOR.MINOR.PATCH` Git tags.

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
- `http://localhost:8000/demo/components.html` for the broader component gallery.

No application build step and no JavaScript framework are required.

## Distribution and use in another project

For reproducible downstream use, pin an immutable release tag instead of copying from the moving `main` branch. For the first release line:

```bash
git clone --branch v0.4.0 --depth 1 https://github.com/1990jk1990/web-tui-kit.git
```

Copy or vendor the files from `src/` and include them in the consuming application:

```html
<link rel="stylesheet" href="/ui/tokens.css">
<link rel="stylesheet" href="/ui/tui.css">
<script src="/ui/tui.js" defer></script>
```

`src/tui.js` is optional when the consuming application does not need the small progressive keyboard enhancements. The exact CSS token values are defined in `src/tokens.css`; reusable component implementation lives in `src/tui.css` and `src/tui.js`.

Tagged GitHub prereleases also provide a focused `web-tui-kit-MAJOR.MINOR.PATCH.zip` and matching SHA-256 checksum containing the runtime, executable demos, version marker, changelog, security guidance, and practical design-system/AI-agent references. `v0.4.0` does not require or publish an npm package; direct tagged vendoring is the primary distribution model.

For the closest match to the original Debian/Ubuntu package-configuration look, start from `.tui-screen`, `.tui-dialog`, `.tui-dialog-title`, `.tui-checklist`, `.tui-check-row`, `.tui-actions`, and `.tui-button` as demonstrated in `demo/index.html`.

For common dialog compositions, use `demo/dialogs.html` and `DESIGN_SYSTEM.md` rather than inventing per-application variants. Containers marked with `data-tui-list` gain optional ArrowUp/ArrowDown/Home/End focus navigation while normal Tab reachability and native control activation remain intact.

See `RELEASING.md` for the versioning/release procedure and `docs/project/compatibility.md` for current compatibility evidence and its limits.

## Project memory and canonical sources

This repository follows **AI-DOC-1 v1.3**. The repository itself is durable project memory; chat history is not required to continue development.

- AI working rules: `AGENTS.md`
- release identity: `VERSION` + immutable Git tags/GitHub Releases
- release procedure: `RELEASING.md`
- project purpose and scope: `docs/project/overview.md`
- compatibility evidence: `docs/project/compatibility.md`
- accepted UI/release behavior: `openspec/specs/`
- current architecture: `docs/architecture/`
- durable decision rationale: `docs/decisions/`
- practical design-system usage guide: `DESIGN_SYSTEM.md`
- exact design-token values: `src/tokens.css`
- implementation: `src/`
- primary executable visual reference: `demo/index.html`
- core dialog gallery: `demo/dialogs.html`
- broader component gallery: `demo/components.html`
- structural regression evidence: `tests/`
- reviewed visual baselines: `tests/visual/baselines/`

See `docs/index.md` for the documentation entry point.

## Prompt for ChatGPT / coding assistants

For a stable released reference, a consuming project can use:

> Use `https://github.com/1990jk1990/web-tui-kit/tree/v0.4.0` as the canonical UI design system. Read `AGENTS.md`, `VERSION`, the current OpenSpec specifications, `DESIGN_SYSTEM.md`, and `demo/index.html` before implementing UI. Treat `demo/index.html` as the primary visual target, `demo/dialogs.html` as the core dialog catalog, and `demo/components.html` as the broader component catalog. Reuse the existing tokens, CSS classes, and interaction patterns instead of inventing a new visual language. The application must remain usable in Linux desktop browsers and Android browsers.

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
