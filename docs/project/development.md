# Development

## Repository structure

```text
src/                 runtime design tokens, CSS, and JavaScript
demo/                executable visual reference
openspec/specs/      canonical accepted behavior
openspec/changes/    active non-trivial behavior changes
docs/architecture/   current architecture
docs/decisions/      durable decision rationale
docs/project/        developer-facing project information
tests/               executable regression evidence
scripts/             documentation and AI-DOC-1 validation tooling
.github/workflows/   continuous integration
```

## Development workflow

1. Read `AGENTS.md` and the relevant canonical sources.
2. Classify the change by impact; behavioral changes require OpenSpec maintenance.
3. Implement the smallest coherent change using existing tokens and patterns where possible.
4. Update the demo for new or changed reusable visual patterns.
5. Add or update tests.
6. Reconcile architecture, ADRs, developer docs, and security material when affected.
7. Run the verification commands from `docs/project/testing.md`.
8. Review the complete diff before merge.

## Component additions

Do not introduce one-off styling when an existing token or pattern serves the same purpose. If a genuinely reusable token or component is added, keep its implementation, specification, demo coverage, and practical design-system guidance aligned.

## Generated documentation

`docs/generated/` is created from canonical OpenSpec Markdown by `scripts/sync_openspec_docs.py`. Do not edit generated files manually.
