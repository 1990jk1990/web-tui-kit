# ADR-0008: Declare a browser-native public contract stability boundary

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `openspec/changes/public-contract-readiness/`
- Related issue: #28
- Supersedes: none
- Superseded by: none

## Context

By `v0.8.0`, `web-tui-kit` has a functioning framework-independent runtime, canonical visual/browser/accessibility regression evidence, executable framework/template consumer recipes, deterministic tagged distribution, and an established direct-vendoring workflow.

However, consumers could infer stability from several different artifacts without one explicit boundary saying which names and markup relationships are intentionally supported. The repository exposes many CSS custom properties and reusable CSS classes, plus progressive JavaScript data attributes and a custom event. It also contains demos, tests, scripts, workflow details, framework verification fixtures, and pinned development dependencies that are visible but are not intended to become downstream APIs.

A 1.0 release would turn this ambiguity into long-term compatibility debt. The project therefore needs an explicit distinction between supported browser-native consumer surface and implementation/evidence details before making a normal Semantic Versioning stability commitment.

The audit also found a concrete inconsistency: `--tui-help` was declared as a public help-accent token, including a forced-colors `LinkText` mapping, but `.tui-help` consumed `--tui-title` instead. Normal colors happened to match, masking the mismatch.

## Decision

The public runtime contract is the browser-native surface documented in `openspec/specs/public-contract/spec.md` and `docs/project/public-contract.md`:

- the three runtime files under `src/`,
- every canonical `--tui-*` custom property name and its documented semantic purpose,
- every canonical reusable `tui-*` CSS class currently implemented in `src/tui.css`,
- the scoped `.is-active` and `.is-selected` state hooks only where combined with documented TUI component selectors,
- documented native semantic element/child relationships required by those component patterns,
- `data-tui-escape-close`, `data-tui-list`, `data-tui-list-item`, and the bubbling `tui:escape` event contract,
- framework/template recipes as consumption guidance over that browser-native contract rather than as separately supported adapter APIs.

Repository demos remain normative visual/semantic examples for documented patterns, but incidental demo IDs, text, ordering, and page wiring are not public APIs. Tests, scripts, generated files, CI implementation, pinned evidence-tool versions, selector/declaration ordering, pseudo-element technique, and JavaScript helper names are non-public unless a future accepted requirement promotes a specific item.

Structural tests will protect the declared inventory and fail when a public runtime name disappears silently or when a new `tui-*` class/token is introduced without being classified/documented.

Before 1.0, intentional breaking public-contract changes use a MINOR version and explicit migration notes. Starting with 1.0, normal Semantic Versioning applies: compatible fixes in PATCH, additive/deprecation changes in MINOR, and incompatible public-contract changes in MAJOR. Planned removals should be deprecated with migration guidance before later major removal unless an urgent security/legal/standards issue requires faster action.

The `--tui-help` implementation is corrected to consume `--tui-help`; this fixes the semantic-token mismatch without renaming any consumer surface.

## Considered alternatives

- Treat all files/selectors/details in the release archive as public. Rejected because it would freeze incidental implementation and verification details, making maintenance disproportionately expensive.
- Treat only a small curated subset of CSS classes/tokens as public and reserve the rest as internal. Rejected for the current runtime because the existing `src/` stylesheet has been intentionally presented as a reusable class/token system and downstream consumers can reasonably use the documented component breadth.
- Introduce a framework component API as the 1.0 contract instead of stabilizing HTML/CSS/DOM behavior. Rejected because the established architecture is framework-independent and current React/Vue/template consumers already interoperate through semantic markup/classes/events.
- Delay defining compatibility until the 1.0 release itself. Rejected because cleanup and migration decisions are safer while the project is explicitly pre-1.0.

## Consequences

### Positive

- Consumers and coding agents can distinguish supported interfaces from visible repository internals.
- 1.0 compatibility expectations have a concrete scope rather than an implicit one.
- New public classes/tokens cannot accidentally appear without classification.
- Future maintainers can refactor CSS/JavaScript/test implementation details without treating every internal change as a consumer migration.
- Framework integrations remain portable because the stable contract is browser-native rather than tied to adapter package versions.
- The help token now behaves consistently with its documented purpose, including forced-colors mode.

### Negative / trade-offs

- The current public class/token inventory is deliberately broad, so post-1.0 incompatible naming cleanup will require major-version discipline.
- Maintainers must update OpenSpec, the practical inventory, structural tests, changelog/migration guidance, and versioning classification together when public surface changes.
- Some visual default changes can remain compatible even though they are user-visible; review must distinguish stable token purpose from literal default value.

## Evidence / notes

`v0.8.0` provides the evidence baseline immediately before this decision: immutable tagged distribution, deterministic ZIP/checksum, canonical Chromium screenshot regression, Chromium/Firefox interaction regression, browser accessibility-semantic regression, and representative executable React/Vue/server-rendered recipe verification.

Physical Android-device testing, real screen-reader/assistive-technology sessions, WCAG conformance evaluation, npm publication, maintained framework adapters, and a broad framework-version matrix remain separate evidence/product domains. They are not promoted into 1.0 prerequisites by this decision unless a later accepted requirement does so deliberately.
