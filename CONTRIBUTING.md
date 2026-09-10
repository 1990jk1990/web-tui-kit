# Contributing

`web-tui-kit` follows AI-DOC-1 v1.3 and treats the repository as durable project memory.

## Before changing the project

Read `AGENTS.md` first. For UI changes, also read the relevant current specification under `openspec/specs/`, `DESIGN_SYSTEM.md`, the affected files under `src/`, and `demo/index.html`.

## Workflow

Use a focused branch and pull request for non-trivial changes. Keep unrelated functional changes separate so review and rollback remain straightforward.

Behavioral changes must update the relevant OpenSpec artifacts. Architectural changes must update the relevant files under `docs/architecture/`; create an ADR under `docs/decisions/` only when the rationale is durable and useful later.

When adding a reusable component, prefer existing tokens and patterns, update the demo, and add regression evidence in `tests/`.

## Verification

Before requesting review, run the fast repository/documentation checks:

```bash
python -m unittest discover -s tests -v
python scripts/validate_ai_doc_1.py
pip install -r requirements-docs.txt
python scripts/sync_openspec_docs.py
mkdocs build --strict
```

For UI or visual changes, also run the pinned browser screenshot suite:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium
python scripts/visual_regression.py
```

If an intended visual change makes the suite fail, do not weaken the threshold or allow CI to overwrite the baseline. Regenerate deliberately with `python scripts/visual_regression.py --update`, review the resulting PNG changes, then rerun the normal comparison. The Linux GitHub Actions environment is the canonical rendering environment; see `docs/project/testing.md` for details.

Document pre-existing failures separately from failures introduced by a change.

## Documentation

Do not create chat logs, AI context dumps, or parallel `new`/`v2`/`final` documentation. Update the canonical source for the information being changed. Do not edit `docs/generated/` manually.

## Security

Never commit credentials, access tokens, private keys, production secrets, or real production data. See `SECURITY.md`.
