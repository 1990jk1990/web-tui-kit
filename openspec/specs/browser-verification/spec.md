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

### Requirement: Browser-native dialog presentation compatibility

The browser verification suite MUST exercise the public `.tui-dialog` presentation on a native `<dialog>` element because native user-agent dialog styles can differ from ordinary section/container elements.

The exercised case MUST verify that the canonical outer `.tui-dialog` computes to visible overflow and that `.tui-dialog-title` geometrically protrudes above the dialog's top border. This evidence MUST run in the configured Chromium and Firefox desktop cases and in the representative narrow touch-capable Chromium case.

This check verifies the accepted presentation contract only; native `<dialog>` modal lifecycle, focus policy, dismissal, and backdrop behavior remain application-owned unless a separate accepted requirement changes that boundary.

#### Scenario: Native dialog user-agent styling would clip the title

- **GIVEN** `.tui-dialog` and `.tui-dialog-title` are applied to a native `<dialog>`
- **WHEN** the browser interaction fixture shows that dialog
- **THEN** computed outer overflow MUST be `visible` and the title rectangle MUST extend above the dialog rectangle so a user-agent scrolling overflow default cannot silently clip the canonical border title

### Requirement: Chromium and Firefox desktop evidence

The desktop interaction contract MUST be exercised in the Chromium and Firefox browser engines supplied by the pinned Playwright release.

Firefox interaction evidence MUST NOT establish a second canonical screenshot baseline; Linux Chromium remains the canonical pixel-regression environment unless a future accepted decision changes that model.

#### Scenario: Firefox compatibility evidence

- **GIVEN** the repository claims the standards-based baseline should remain usable in current Firefox
- **WHEN** CI runs the browser interaction suite
- **THEN** the documented keyboard/custom-event and focused native-dialog presentation contracts MUST be exercised in the pinned Firefox engine

### Requirement: Touch-capable narrow Chromium evidence

The interaction suite MUST include a narrow Chromium context with mobile/touch emulation enabled and MUST verify that the context exposes touch/coarse-pointer behavior and that a native interactive control remains operable by tap.

Focused browser-native presentation checks that are part of the interaction fixture, including the native `<dialog>` title-overflow regression, MUST also run in this representative narrow context when they do not depend on desktop-only input behavior.

#### Scenario: Touch interaction evidence

- **GIVEN** a 390×844 Chromium context with mobile/touch flags enabled
- **WHEN** the touch interaction case runs
- **THEN** the coarse-pointer media query and touch capability MUST be active, a native checkbox MUST be activatable by tap, and the native-dialog border-title presentation check MUST remain valid

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
- **THEN** the GitHub release MUST NOT be published