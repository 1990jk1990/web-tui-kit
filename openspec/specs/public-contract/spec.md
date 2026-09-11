# Public consumer contract specification

## Purpose

This specification defines the supported consumer-facing surface of `web-tui-kit` and the compatibility rules that apply to that surface. It separates intentionally supported interfaces from repository implementation, demo, test, and generated details before the project makes a 1.0 stability commitment.

## Requirements

### Requirement: Public runtime files

The public browser runtime MUST remain the three canonical files under `src/`:

- `src/tokens.css` — public CSS custom properties and default theme values,
- `src/tui.css` — public reusable component/layout/state classes,
- `src/tui.js` — optional progressive behavior for the documented data attributes and custom event.

Consumers MUST be able to load `tokens.css` before `tui.css` without a framework, package manager, bundler, or application build step. `tui.js` MUST remain optional for consumers that do not use its documented progressive behaviors.

#### Scenario: Plain consumer uses only presentation

- **GIVEN** a consumer serves static browser assets
- **WHEN** it loads `src/tokens.css` followed by `src/tui.css`
- **THEN** documented component presentation MUST work without loading `src/tui.js`

### Requirement: Public token names and semantics

Every CSS custom property declared by the canonical `:root` blocks in `src/tokens.css` with a `--tui-` prefix is part of the public theming contract.

The public contract protects each token's name and documented purpose. Exact default values MAY evolve in a compatible release when the token keeps the same meaning and applicable visual/compatibility evidence is updated. Repurposing an existing token to a materially different meaning is a public-contract change.

Forced-colors overrides MAY replace normal default values with CSS system colors while preserving the token's semantic purpose.

#### Scenario: Consumer overrides a public token

- **GIVEN** a consumer overrides `--tui-selection-bg`
- **WHEN** canonical components render selection states
- **THEN** those components MUST continue to consume that token for the documented selection-background purpose

### Requirement: Public CSS component and state hooks

Reusable classes implemented in `src/tui.css` with the `tui-` prefix are public consumer hooks unless this specification deliberately classifies a future name as internal before release.

The current public class inventory is documented in `docs/project/public-contract.md` and MUST be protected by structural regression evidence. The scoped state hooks `.is-active` and `.is-selected` are also public only when combined with the documented `tui-*` component selectors that implement them; those generic class names are not global styling contracts on unrelated elements.

Consumers MUST NOT need to depend on selector ordering, declaration ordering, pseudo-element implementation technique, private descendant selectors, or exact generated marker/bracket mechanism beyond the documented rendered behavior and semantic markup requirements.

#### Scenario: Public class is silently renamed

- **GIVEN** a documented public `tui-*` class exists in a released contract
- **WHEN** a maintainer removes or renames it without an intentional compatibility change
- **THEN** structural regression checks MUST fail before release

### Requirement: Semantic markup remains part of component contracts

CSS class names do not replace native semantics. Where a documented pattern requires a native button, input, label, link, table, or progress element, consumers MUST preserve that semantic element or provide an equivalent application-level contract explicitly allowed by the component documentation.

In particular:

- `.tui-button` and `.tui-menu-row` are intended for native buttons,
- `.tui-input`, `.tui-select`, and `.tui-textarea` are intended for their corresponding native form controls,
- `.tui-check` / `.tui-radio` and `.tui-check-row` / `.tui-radio-row` retain native checkbox/radio inputs,
- `.tui-progress` is intended for a native `<progress>` element,
- `.tui-table` is intended for semantic table markup,
- `.tui-dialog` remains presentation-only and MUST NOT imply modal semantics by itself.

Required child/sibling relationships used by the documented checkbox/radio marker patterns are public markup expectations because the canonical CSS depends on them.

#### Scenario: Framework renders a checklist row

- **GIVEN** a React, Vue, or template consumer renders `.tui-check-row`
- **WHEN** it follows the public contract
- **THEN** the rendered row MUST retain a native checkbox and the documented `.tui-mark` marker relationship instead of replacing the input with a generic clickable element

### Requirement: Public progressive JavaScript contract

When `src/tui.js` is loaded, the following names are public behavior contracts:

- `data-tui-escape-close` on `.tui-window` or `.tui-dialog`,
- bubbling custom event `tui:escape`, including `detail.sourceEvent` containing the originating keyboard event,
- `data-tui-list` on an opted-in list container,
- `data-tui-list-item` on an explicitly opted-in custom focusable list item.

The accepted keyboard behavior for those attributes remains defined by the main `web-tui-kit` specification. Internal function names, query construction, listener placement, and implementation technique are not public APIs.

#### Scenario: Consumer handles Escape

- **GIVEN** a consumer loads `src/tui.js` and marks a TUI surface with `data-tui-escape-close`
- **WHEN** Escape is pressed for the applicable surface
- **THEN** the consumer MUST continue to receive a bubbling `tui:escape` event with the originating keyboard event available as `detail.sourceEvent`

### Requirement: Integration patterns are public guidance, not adapter APIs

The React, Vue, and server-rendered recipes and `docs/project/framework-integration.md` define supported ways to consume the browser-native public contract. They MUST reuse the canonical runtime surface and native semantics.

Example component names, local variable names, fixture IDs, test harness APIs, pinned representative framework/tool versions, and generated verification output are NOT public runtime APIs.

#### Scenario: Framework verification tool changes

- **GIVEN** the repository changes its internal recipe build harness without changing the rendered canonical contract
- **WHEN** consumers upgrade
- **THEN** the harness change MUST NOT require a consumer-side runtime migration

### Requirement: Non-public repository details

The following categories are explicitly outside the consumer compatibility contract unless a future accepted specification promotes a particular item:

- `demo/` document IDs, copy text, ordering, and page-specific wiring beyond the documented reusable patterns,
- `tests/`, `test-results/`, browser fixtures, visual baseline file names, and verification helper APIs,
- `scripts/`, GitHub Actions implementation details, MkDocs/generated documentation output, and release-tool implementation internals,
- internal CSS declaration order, selector grouping, media-query organization, pseudo-element technique, and JavaScript helper/local names,
- exact pinned development-tool/framework/browser versions, which are evidence anchors rather than downstream API requirements.

Canonical demos remain normative visual/semantic examples for the documented patterns, but consumers MUST NOT treat incidental page IDs/text/order as stable API.

### Requirement: Pre-1.0 compatibility policy

Before `1.0.0`, compatible fixes SHOULD increment PATCH. New public capability and intentional incompatible public-contract changes MUST increment MINOR, be called out in `CHANGELOG.md`, and include migration guidance when an existing documented consumer pattern changes.

A pre-1.0 MINOR release MAY remove or rename public surface, but MUST NOT do so silently.

#### Scenario: Pre-1.0 class rename

- **GIVEN** a public class must be renamed before 1.0
- **WHEN** the change is released
- **THEN** the project MUST use a new MINOR version and document the old name, new name, and required consumer migration

### Requirement: Post-1.0 compatibility and deprecation policy

Starting with `1.0.0`, normal Semantic Versioning compatibility expectations apply to the declared public contract:

- PATCH releases MUST preserve the public contract while delivering compatible fixes,
- MINOR releases MAY add compatible public surface and MAY deprecate existing surface,
- incompatible removal, rename, required semantic-markup change, token repurposing, or documented event/data-attribute contract break MUST require a new MAJOR release.

After 1.0, planned removal of public surface SHOULD first be marked deprecated in documentation and changelog in at least one prior MINOR release, with a migration path, before removal in a MAJOR release. An urgent security, legal, or standards-compliance issue MAY require faster removal, but the break and migration MUST still be documented explicitly.

#### Scenario: Post-1.0 deprecated token

- **GIVEN** a public token is no longer preferred after 1.0
- **WHEN** maintainers plan to remove it
- **THEN** a compatible MINOR release SHOULD first mark it deprecated with replacement guidance and the actual removal MUST wait for a MAJOR release unless an urgent exception applies

### Requirement: Public contract is distributed with releases

The focused tagged release archive MUST include `docs/project/public-contract.md` alongside the runtime and existing consumer guidance so a downstream consumer can identify the supported surface without cloning the development repository.

#### Scenario: Consumer inspects focused ZIP

- **GIVEN** a tagged release ZIP
- **WHEN** a consumer reviews its documentation
- **THEN** the archive MUST contain the public-contract guide describing supported runtime names, semantic expectations, and stability rules

### Requirement: 1.0 readiness is evidence-based

A `1.0.0` release MUST NOT be selected merely because the version sequence reached `0.9.x`. Before 1.0 preparation begins:

- the supported public surface and stability/deprecation policy MUST be accepted and structurally protected,
- any known intentional pre-1.0 public naming/semantic cleanup selected by the audit MUST be complete,
- the candidate public contract MUST pass the existing structural/docs, canonical visual, cross-browser interaction, accessibility-semantic, representative framework-recipe, and deterministic release-archive gates,
- release and consumer documentation MUST describe the 1.0 compatibility commitment consistently,
- unsupported evidence domains MUST remain accurately bounded rather than being converted into certification claims.

Physical Android-device certification, screen-reader/assistive-technology certification, WCAG conformance certification, registry publication, maintained framework adapters, and an exhaustive framework-version matrix are NOT prerequisites for 1.0 unless a separate accepted requirement later makes one of them mandatory.

#### Scenario: Automated gates pass without physical Android evidence

- **GIVEN** the declared public contract and all required repository release gates pass
- **AND** physical Android evidence remains explicitly documented as unverified rather than certified
- **WHEN** maintainers evaluate 1.0 readiness
- **THEN** the absence of physical-device certification alone MUST NOT block the 1.0 decision
