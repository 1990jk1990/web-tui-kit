# Development

## Repository structure

```text
src/                 runtime design tokens, CSS, and JavaScript
demo/                executable visual references
examples/            React/Vue/server-rendered consumption recipes
openspec/specs/      canonical accepted behavior
openspec/changes/    active non-trivial behavior changes
docs/architecture/   current architecture
docs/decisions/      durable decision rationale
docs/project/        developer-facing project information
tests/               structural/release/visual/browser interaction evidence
scripts/             validation, visual/interaction regression, and release tooling
.github/workflows/   continuous integration and tag release automation
VERSION              canonical plain Semantic Version
RELEASING.md         maintainer release procedure
```

## Development workflow

1. Read `AGENTS.md` and the relevant canonical sources.
2. Classify the change by impact; behavioral changes require OpenSpec maintenance.
3. Implement the smallest coherent change using existing tokens and patterns where possible.
4. Update the demo for new or changed reusable visual patterns; update `examples/` when consumption guidance changes.
5. Add or update structural and browser-driven evidence appropriate to the behavior being changed.
6. Reconcile architecture, ADRs, developer docs, compatibility evidence, and security material when affected.
7. Run the verification commands from `docs/project/testing.md`.
8. Review the complete diff before merge.

## Component additions

Do not introduce one-off styling when an existing token or pattern serves the same purpose. If a genuinely reusable token or component is added, keep its implementation, specification, demo coverage, practical design-system guidance, visual baselines, and applicable interaction evidence aligned.

## Framework/template integration

`examples/` demonstrates consumption; it does not own a second implementation. A recipe must reuse native controls and canonical `tui-*` classes/events rather than copying reusable CSS into framework-specific style systems.

Framework dependencies belong to the consuming application. Do not add React, Vue, or template-engine dependencies to `src/` or repository runtime requirements merely to make examples executable here. Structural recipe tests should protect that boundary.

If a consumer reports a real behavior that cannot be expressed through the current semantic/class/custom-event contract, open a focused OpenSpec/architecture change before introducing a maintained adapter runtime.

## Browser verification

Source-level tests are useful for inexpensive repository invariants, but externally relevant keyboard/custom-event behavior should also be exercised through `scripts/interaction_regression.py`. The runner uses the purpose-built `tests/browser/interaction.html` fixture over the canonical `src/` assets.

Chromium remains the canonical screenshot baseline environment. Interaction compatibility evidence additionally exercises Firefox desktop and a narrow touch-capable Chromium context. Keep Playwright/browser dependencies out of `src/`; they are development and release-gate tooling only.

Compatibility claims belong in `docs/project/compatibility.md`. Physical Android results must come from an actual run recorded through `docs/project/android-device-check.md`, not from browser emulation.

## Release preparation

Release/version changes are not routine development metadata. Follow `RELEASING.md`; update `VERSION` and `CHANGELOG.md` together, run structural/docs/visual/interaction release gates, validate the deterministic distribution archive, and keep published tags immutable. Direct tagged vendoring is the current distribution baseline.

## Generated output

`docs/generated/` is created from canonical OpenSpec Markdown by `scripts/sync_openspec_docs.py`. `site/`, `dist/`, and `test-results/` are generated local/CI output. Do not edit generated documentation manually or commit generated build/release/failure directories.
