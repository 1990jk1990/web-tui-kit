# Public contract and 1.0 readiness audit

Status: Active
Related issue: #28
Change class: Class 3 — public compatibility / potential breaking cleanup

## Motivation

`web-tui-kit` has now published `v0.8.0` with a deterministic tagged-vendoring release path, canonical visual regression, Chromium/Firefox interaction verification, browser accessibility-semantic verification, and executable representative framework/template recipe checks. The remaining strategic question is no longer whether the existing runtime can be exercised, but which parts of that runtime and its documentation are intentionally supported as the public consumer contract before the project considers a normal 1.0 compatibility commitment.

The project currently documents many reusable classes, tokens, native-control patterns, data attributes, and custom-event behaviors, but it does not yet define one explicit stability boundary separating supported consumer surface from demo/test/internal implementation detail or a durable deprecation/migration policy for that surface.

## Proposed change

- Inventory the intentionally public runtime surface across `src/`, OpenSpec, `DESIGN_SYSTEM.md`, integration guidance, demos, and release contents.
- Define which CSS custom properties, reusable `tui-*` classes, semantic markup expectations, JavaScript custom events, data attributes, and integration patterns are public contracts.
- Explicitly classify demo-only, test-only, generated, and internal implementation details as non-public.
- Reconcile names and contracts while the project is still pre-1.0; any intentional cleanup must be documented as a migration and verified through the applicable regression gates.
- Define compatibility, deprecation, migration, and removal rules for public surface changes before and after 1.0.
- Add structural regression safeguards for the declared public contract so silent removal/rename is caught by CI.
- Define concrete evidence-based exit criteria for a later 1.0 decision.

## Boundaries

This audit does not by itself introduce npm/registry publication, a framework adapter runtime, a visual redesign, physical Android certification, screen-reader/assistive-technology certification, or a WCAG conformance claim.

The framework-independent browser runtime, immutable tagged-vendoring distribution model, Linux Chromium screenshot authority, and existing evidence boundaries remain the baseline unless the audit finds a concrete contradiction requiring a separate accepted decision.

## Verification plan

- Reconcile accepted OpenSpec with the public-surface inventory and stability policy.
- Add/update structural tests for public tokens/classes/events/data attributes and documented integration points.
- Run the normal project/AI-DOC/docs checks.
- If runtime markup/style/behavior changes are required, run applicable visual, interaction, accessibility-semantic, and framework-recipe gates and review any intentional migration impact.
- Review the complete diff and compatibility guidance before archival and merge.

## Expected outcome

At completion, downstream consumers and coding agents should be able to tell which `web-tui-kit` interfaces are intentionally stable, which details they must not depend on, how future breaking changes are communicated, and what still has to be true before the project can deliberately choose a `1.0.0` release.