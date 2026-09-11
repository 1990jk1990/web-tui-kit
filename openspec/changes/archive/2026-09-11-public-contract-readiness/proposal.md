# Public contract and 1.0 readiness audit

Status: Completed
Related issue: #28
Change class: Class 3 — public compatibility / potential breaking cleanup

## Motivation

`web-tui-kit` published `v0.8.0` with a deterministic tagged-vendoring release path, canonical visual regression, Chromium/Firefox interaction verification, browser accessibility-semantic verification, and executable representative framework/template recipe checks. The remaining strategic question was which parts of that runtime and its documentation are intentionally supported as the public consumer contract before the project considers a normal 1.0 compatibility commitment.

The project documented many reusable classes, tokens, native-control patterns, data attributes, and custom-event behaviors, but did not yet define one explicit stability boundary separating supported consumer surface from demo/test/internal implementation detail or a durable deprecation/migration policy for that surface.

## Completed change

- Inventoried the intentionally public runtime surface across `src/`, OpenSpec, `DESIGN_SYSTEM.md`, integration guidance, demos, and release contents.
- Defined all canonical `--tui-*` custom properties, reusable `tui-*` classes, scoped state hooks, native semantic markup expectations, JavaScript custom events/data attributes, and integration patterns that form the public browser-native contract.
- Explicitly classified demo-only, test-only, generated, CI, pinned evidence-tool, and implementation details as non-public.
- Added `openspec/specs/public-contract/spec.md` and practical `docs/project/public-contract.md` inventory.
- Defined compatibility, deprecation, migration, and removal rules before and after 1.0 plus concrete evidence-based 1.0 exit criteria.
- Added `tests/test_public_contract.py` to fail when declared public token/class/state/data-attribute/event surface drifts silently.
- Added the public-contract guide to the deterministic focused release archive.
- Added ADR-0008 and reconciled architecture, framework integration, compatibility, release, contribution, README, design-system, and AI-agent guidance.
- Corrected `.tui-help` to consume the existing `--tui-help` token. Normal default pixels remain unchanged because the normal title/help values are equal; forced-colors help now follows the token's `LinkText` mapping.

## Boundaries

This audit does not introduce npm/registry publication, a framework adapter runtime, a visual redesign, physical Android certification, screen-reader/assistive-technology certification, or a WCAG conformance claim.

The framework-independent browser runtime, immutable tagged-vendoring distribution model, Linux Chromium screenshot authority, and existing evidence boundaries remain the baseline.

No other current class, token, event, or `data-tui-*` name was selected for pre-1.0 rename/removal by the audit.

## Verification evidence

PR #29 head `e400aa05f6f65ed7d75fdfcc6659e453aaf3ff78` passed the complete pull-request verification set before archival:

- AI-DOC-1 validation / project tests / strict documentation checks: workflow `34552434775`
- Browser interaction regression: workflow `34552434778`
- Accessibility semantics regression: workflow `34552434780`
- Visual regression: workflow `34552434832`
- Framework recipe regression: workflow `34552434821`

The complete PR diff was inspected before archival. The only runtime CSS change is the intentional `.tui-help` token mapping described above; visual regression remained green without baseline changes.

## Outcome

Downstream consumers and coding agents can now distinguish intentionally supported `web-tui-kit` interfaces from visible repository internals, understand how future breaking changes are communicated, and evaluate explicit 1.0 exit criteria. Version 1.0 remains a deliberate follow-up decision/release step rather than an automatic consequence of reaching v0.9.
