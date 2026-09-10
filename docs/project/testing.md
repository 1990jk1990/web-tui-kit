# Testing

## Project tests

Run the current automated regression checks with:

```bash
python -m unittest discover -s tests -v
```

The initial test suite checks repository-level contracts such as demo asset references, required design tokens and component selectors, the Escape event contract, native-control presence, mobile viewport metadata, and absence of selected forbidden visual effects.

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

The repository does not yet contain automated cross-browser interaction tests, accessibility audits, screenshot/visual-regression tests, or device-matrix tests. Until those are added, `demo/index.html` remains the executable visual reference and browser/device review is manual evidence rather than automated proof.

When behavior becomes important enough that regression would be costly, add executable coverage rather than relying only on prose or visual inspection.
