# Development

## Repository structure

```text
src/                 runtime design tokens, CSS, and JavaScript
demo/                executable visual references
openspec/specs/      canonical accepted behavior
openspec/changes/    active non-trivial behavior changes
docs/architecture/   current architecture
docs/decisions/      durable decision rationale
docs/project/        developer-facing project information
tests/               executable structural/release/visual regression evidence
scripts/             validation, visual-regression, and release tooling
.github/workflows/   continuous integration and tag release automation
VERSION              canonical plain Semantic Version
RELEASING.md         maintainer release procedure
```

## Development workflow

1. Read `AGENTS.md` and the relevant canonical sources.
2. Classify the change by impact; behavioral changes require OpenSpec maintenance.
3. Implement the smallest coherent change using existing tokens and patterns where possible.
4. Update the demo for new or changed reusable visual patterns.
5. Add or update tests.
6. Reconcile architecture, ADRs, developer docs, compatibility evidence, and security material when affected.
7. Run the verification commands from `docs/project/testing.md`.
8. Review the complete diff before merge.

## Component additions

Do not introduce one-off styling when an existing token or pattern serves the same purpose. If a genuinely reusable token or component is added, keep its implementation, specification, demo coverage, practical design-system guidance, and visual baselines aligned.

## Release preparation

Release/version changes are not routine development metadata. Follow `RELEASING.md`; update `VERSION` and `CHANGELOG.md` together, validate the deterministic distribution archive, and keep published tags immutable. Direct tagged vendoring is the current distribution baseline.

## Generated output

`docs/generated/` is created from canonical OpenSpec Markdown by `scripts/sync_openspec_docs.py`. `site/`, `dist/`, and `test-results/` are generated local/CI output. Do not edit generated documentation manually or commit generated build/release/failure directories.
