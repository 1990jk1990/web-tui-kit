# Testing

## Project tests

Run the current automated regression checks with:

```bash
python -m unittest discover -s tests -v
```

The test suite checks repository-level contracts such as demo asset references, required design tokens and component selectors, Escape-event behavior for opted-in windows and dialogs, optional `data-tui-list` keyboard-navigation behavior, the canonical package-configuration dialog/checklist primitives, core dialog-gallery coverage, general component-gallery coverage, mobile viewport metadata, and absence of selected forbidden modern visual effects.

## AI-DOC-1 structure

```bash
python scripts/validate_ai_doc_1.py
```

## Documentation build

```bash
pip install -r requirements-docs.txt
python scripts/sync_openspec_docs.py
mkdocs build --strict
```

## Current coverage limits

The repository does not yet contain automated cross-browser interaction tests, accessibility audits, screenshot/visual-regression tests, or device-matrix tests. Until those are added, `demo/index.html` remains the canonical executable visual reference, `demo/components.html` provides broader component coverage, `demo/dialogs.html` provides executable core-dialog coverage, and browser/device review is manual evidence rather than automated proof.

The next planned verification work is tracked separately in the project backlog so visual-regression and accessibility evidence can be added without mixing it into the core component implementation.
