# web-tui-kit

A reusable, framework-independent browser UI design system inspired by Debian debconf, `dialog`, and `whiptail`.

The project is the canonical UI reference for browser-based applications that should share the same text-oriented visual language on Linux desktops and Android devices.

**Status:** early development. No stable release has been published yet.

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

## Use in another project

Copy or vendor the files from `src/` and include them in the consuming application:

```html
<link rel="stylesheet" href="/ui/tokens.css">
<link rel="stylesheet" href="/ui/tui.css">
<script src="/ui/tui.js" defer></script>
```

The exact CSS token values are defined in `src/tokens.css`; reusable component implementation lives in `src/tui.css` and `src/tui.js`.

For the closest match to the original Debian/Ubuntu package-configuration look, start from `.tui-screen`, `.tui-dialog`, `.tui-dialog-title`, `.tui-checklist`, `.tui-check-row`, `.tui-actions`, and `.tui-button` as demonstrated in `demo/index.html`.

For common dialog compositions, use `demo/dialogs.html` and `DESIGN_SYSTEM.md` rather than inventing per-application variants. Containers marked with `data-tui-list` gain optional ArrowUp/ArrowDown/Home/End focus navigation while normal Tab reachability and native control activation remain intact.

## Project memory and canonical sources

This repository follows **AI-DOC-1 v1.3**. The repository itself is durable project memory; chat history is not required to continue development.

- AI working rules: `AGENTS.md`
- project purpose and scope: `docs/project/overview.md`
- accepted UI behavior: `openspec/specs/`
- current architecture: `docs/architecture/`
- durable decision rationale: `docs/decisions/`
- practical design-system usage guide: `DESIGN_SYSTEM.md`
- exact design-token values: `src/tokens.css`
- implementation: `src/`
- primary executable visual reference: `demo/index.html`
- core dialog gallery: `demo/dialogs.html`
- broader component gallery: `demo/components.html`
- executable regression evidence: `tests/`

See `docs/index.md` for the documentation entry point.

## Prompt for ChatGPT / coding assistants

A consuming project can use the following instruction:

> Use `https://github.com/1990jk1990/web-tui-kit` as the canonical UI design system. Read `AGENTS.md`, `ai-doc-1.yaml`, the current OpenSpec specification, `DESIGN_SYSTEM.md`, and `demo/index.html` before implementing UI. Treat `demo/index.html` as the primary visual target, `demo/dialogs.html` as the core dialog catalog, and `demo/components.html` as the broader component catalog. Reuse the existing tokens, CSS classes, and interaction patterns instead of inventing a new visual language. The application must remain usable in Linux desktop browsers and Android browsers.

## Verification

Run the project checks with:

```bash
python -m unittest discover -s tests -v
python scripts/validate_ai_doc_1.py
pip install -r requirements-docs.txt
python scripts/sync_openspec_docs.py
mkdocs build --strict
```

Contribution and documentation workflow details are in `CONTRIBUTING.md`.
