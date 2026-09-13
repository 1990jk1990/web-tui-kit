# Browser verification specification

## Purpose

This specification defines the accepted automated browser-verification and compatibility-evidence contract for `web-tui-kit`. Runtime component behavior remains canonical in the relevant UI specifications; this document defines how browser evidence is produced and interpreted.

## Requirements

### Requirement: Browser-driven interaction verification

The repository MUST provide browser-driven verification for the progressive interaction contracts implemented by `src/tui.js` rather than relying only on source-text assertions.

The interaction suite MUST execute the canonical runtime assets through semantic HTML controls and MUST verify `tui:escape`, optional `data-tui-list` navigation, skipped unavailable items, native radio behavior, and text-entry arrow-key preservation.

#### Scenario: Runtime interaction regression

- **GIVEN** a change alters `src/tui.js` or related interaction markup
- **WHEN** the browser interaction suite runs
- **THEN** a regression in the documented Escape/list/native-control contracts MUST cause the suite to fail

### Requirement: Chromium and Firefox desktop evidence

The desktop interaction contract MUST be exercised in the Chromium and Firefox browser engines supplied by the pinned Playwright release.

Firefox interaction evidence MUST NOT establish a second canonical screenshot baseline; Linux Chromium remains the canonical pixel-regression environment unless a future accepted decision changes that model.

#### Scenario: Firefox compatibility evidence

- **GIVEN** the repository claims the standards-based baseline should remain usable in current Firefox
- **WHEN** CI runs the browser interaction suite
- **THEN** the documented keyboard/custom-event contracts MUST be exercised in the pinned Firefox engine

### Requirement: Touch-capable narrow Chromium evidence

The interaction suite MUST include a narrow Chromium context with mobile/touch emulation enabled and MUST verify that the context exposes touch/coarse-pointer behavior and that a native interactive control remains operable by tap.

#### Scenario: Touch interaction evidence

- **GIVEN** a 390×844 Chromium context with mobile/touch flags enabled
- **WHEN** the touch interaction case runs
- **THEN** the coarse-pointer media query and touch capability MUST be active and a native checkbox MUST be activatable by tap

### Requirement: Physical Android claims require physical evidence

Automated mobile/touch Chromium emulation MUST NOT be described as physical Android Chrome, Android WebView, software-keyboard, or device certification.

The repository MUST provide a manual physical-Android evidence procedure and MUST record a dated run from an actual Android device against an exact repository commit/tag, identify the exercised browser family, and record the observed checklist outcomes before upgrading compatibility documentation to claim a physical-device result.

Device manufacturer/model and exact Android/Chrome version numbers MAY be recorded when material to a defect or compatibility investigation, but they are not required for the baseline physical-device claim and MUST NOT be inferred or fabricated when the tester chooses not to retain them.

A physical Chrome for Android result MUST NOT be generalized to Android WebView, multiple vendors, a browser-version matrix, accessibility-service/screen-reader behavior, WCAG conformance, latency, or performance.

#### Scenario: No physical device run exists

- **GIVEN** only Playwright touch/mobile emulation has been executed
- **WHEN** compatibility evidence is documented
- **THEN** physical Android verification MUST remain explicitly unverified

#### Scenario: Physical Android Chrome baseline is recorded

- **GIVEN** an actual Android device runs the canonical checklist against an exact repository commit/tag in Chrome for Android
- **WHEN** the date, browser family, and observed PASS/FAIL outcomes are recorded
- **THEN** compatibility documentation MAY state that a physical Android Chrome baseline exists while keeping Android WebView and broader device/version claims explicitly unverified

### Requirement: Browser verification is development-only

Playwright, Chromium, Firefox, browser drivers, and interaction fixtures MUST remain development/CI concerns and MUST NOT become dependencies of the runtime consumed from `src/`.

#### Scenario: Plain downstream consumer

- **GIVEN** a consuming application vendors the released `src/` assets
- **WHEN** it uses `web-tui-kit`
- **THEN** it MUST NOT need Playwright, Chromium, Firefox, Python, Node.js, or the repository browser-test fixture

### Requirement: Future release publication includes interaction gate

Tag-triggered release publication MUST run the browser interaction suite before deterministic artifact creation/publication, alongside the existing structural, documentation, and visual checks.

#### Scenario: Browser interaction regression on a release tag

- **GIVEN** a matching release tag on `main`
- **WHEN** browser interaction verification fails
- **THEN** the GitHub prerelease MUST NOT be published
