# Accessibility verification specification

## Purpose

This specification defines the accepted automated browser evidence for the accessibility semantics exposed by canonical `web-tui-kit` patterns. Runtime UI behavior remains canonical in the relevant UI specifications; this document defines what semantic evidence is produced and how it may be interpreted.

## Requirements

### Requirement: Browser-driven semantic verification

The repository MUST provide browser-driven checks for the canonical package-configuration and core-dialog patterns using the actual canonical demo/runtime assets.

The checks MUST use browser-computed role/name/native-state queries rather than treating source-text assertions alone as sufficient accessibility evidence.

#### Scenario: Canonical semantic regression

- **GIVEN** a canonical demo or runtime change alters browser-exposed semantics
- **WHEN** the accessibility semantic suite runs
- **THEN** a regression in the accepted roles, accessible names, label associations, or native states MUST cause the suite to fail

### Requirement: Native semantics remain primary

Canonical examples MUST use native buttons, inputs, labels, radio controls, checkboxes, and progress elements where those native elements already provide the required semantics.

ARIA MUST NOT be introduced solely to replace equivalent native semantics. Presentation-only visual annotations inside a control or label MUST NOT accidentally become part of the control accessible name when they do not add operation-critical meaning.

#### Scenario: Checklist helper annotation

- **GIVEN** a native checkbox row displays a repeated visual `<Help>` annotation
- **WHEN** the browser computes the checkbox accessible name
- **THEN** the service label MUST remain the control name and the presentation-only helper annotation MUST NOT be appended accidentally

### Requirement: Presentation-only dialog class does not imply modal semantics

`.tui-dialog` is a visual class and MUST NOT by itself imply ARIA `dialog`, `alertdialog`, or modal semantics.

Canonical section-based examples with an accessible heading MUST retain their browser-native named-region semantics unless the application deliberately uses a native `<dialog>` or otherwise provides application-level dialog semantics.

#### Scenario: Canonical package surface

- **GIVEN** `demo/index.html` renders its named `<section class="tui-dialog">`
- **WHEN** browser semantic verification runs
- **THEN** the surface MUST expose its existing named-region/heading semantics and MUST NOT be asserted as a modal dialog solely because of the CSS class name

### Requirement: Canonical control semantics

The semantic suite MUST verify representative canonical controls and state:

- the package checklist group name and checkbox names/checked state,
- core action-button names,
- input label association for the hostname field,
- action-menu group/button names and disabled state,
- radiogroup name plus radio names/checked/disabled state,
- checklist disabled state,
- native progressbar accessible name and numeric value/max semantics.

#### Scenario: Native progress gauge

- **GIVEN** the canonical gauge uses `<progress>` labelled `Installing packages`
- **WHEN** semantic verification runs
- **THEN** the browser MUST expose a progressbar named `Installing packages` whose underlying native value/max are `65` and `100`

### Requirement: Chromium and Firefox desktop semantic evidence

The canonical desktop semantic contract MUST be exercised in the Chromium and Firefox engines supplied by the pinned Playwright release.

Firefox semantic evidence MUST NOT establish a second screenshot-baseline authority; Linux Chromium remains the canonical pixel-regression environment.

#### Scenario: Firefox semantic compatibility

- **GIVEN** the canonical demo markup uses standards-based native semantics
- **WHEN** the semantic suite runs in pinned Firefox
- **THEN** the documented roles, names, labels, and native states MUST remain discoverable through browser semantic queries

### Requirement: Narrow touch-capable Chromium semantic evidence

The semantic suite MUST include a narrow Chromium context with mobile/touch emulation enabled and MUST verify that the core package surface, checklist, native checkbox, and action control remain semantically discoverable.

#### Scenario: Representative mobile semantic context

- **GIVEN** the canonical package demo at a 390×844 touch-capable Chromium context
- **WHEN** semantic verification runs
- **THEN** its named region, checklist group, representative checkbox, and `Ok` action MUST retain the same semantic identities as the desktop pattern

### Requirement: Accessibility automation evidence is bounded

Passing browser semantic checks MUST NOT be described as screen-reader certification, assistive-technology interoperability certification, physical Android accessibility-service verification, or proof of WCAG conformance.

Documentation MUST distinguish browser-computed semantic evidence from manual assistive-technology and physical-device evidence.

#### Scenario: Automated suite passes

- **GIVEN** all pinned-browser semantic checks pass
- **WHEN** compatibility evidence is documented
- **THEN** the project MAY claim automated browser semantic evidence but MUST NOT upgrade unperformed assistive-technology or device checks to verified status

### Requirement: Accessibility verification is development-only

Playwright, browser engines, semantic test runners, and failure artifacts MUST remain development/CI concerns and MUST NOT become dependencies of the released `src/` runtime.

#### Scenario: Plain downstream consumer

- **GIVEN** a consuming application vendors the released runtime assets
- **WHEN** it uses `web-tui-kit`
- **THEN** it MUST NOT need Playwright, Python, Chromium, Firefox, or accessibility test tooling

### Requirement: Future release publication includes semantic gate

Once accepted by this milestone, tag-triggered release publication MUST run the accessibility semantic suite before deterministic artifact creation/publication, alongside structural, documentation, visual, and interaction verification.

#### Scenario: Semantic regression on a release tag

- **GIVEN** a matching release tag on `main`
- **WHEN** accessibility semantic verification fails
- **THEN** the GitHub prerelease MUST NOT be published
