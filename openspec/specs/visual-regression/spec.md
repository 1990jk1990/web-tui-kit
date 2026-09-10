# Visual regression verification specification

## Purpose

This specification defines the accepted repository-level visual-regression contract. It verifies the canonical demos without changing the browser-native runtime contract defined by the main `web-tui-kit` specification.

## Requirements

### Requirement: Canonical screenshot baselines

The repository MUST maintain reviewed screenshot baselines for the canonical package-configuration demo and the core dialog gallery at fixed desktop and narrow/mobile viewports.

The baselines MUST be generated with the pinned Playwright/Chromium verification toolchain and stored under `tests/visual/baselines/`.

#### Scenario: Canonical visual coverage

- **GIVEN** the repository contains the accepted UI demos
- **WHEN** the visual-regression runner enumerates its canonical cases
- **THEN** it MUST cover desktop and narrow/mobile renders of both `demo/index.html` and `demo/dialogs.html`

### Requirement: Deterministic browser capture

The visual runner MUST serve the repository locally, use fixed viewport dimensions and device scale, use the pinned Chromium build associated with the pinned Playwright version, and suppress optional motion/caret effects that could create avoidable screenshot noise.

The Linux CI environment is the canonical rendering environment for accepted baselines.

#### Scenario: Repeatable CI render

- **GIVEN** unchanged repository content and the pinned verification dependencies
- **WHEN** the visual suite runs in the canonical Linux CI environment
- **THEN** the captured images MUST remain within the configured pixel-difference tolerance of the reviewed baselines

### Requirement: Visual drift detection

A visual comparison MUST fail when the proportion of materially changed pixels exceeds the configured tolerance. Missing baselines or image-size mismatches MUST also fail verification.

The default comparison MUST ignore only small per-channel rasterization noise and MUST keep the aggregate changed-pixel allowance narrow enough to detect layout, spacing, border, typography, and responsive-composition regressions.

#### Scenario: Unintended visual change

- **GIVEN** a canonical demo render differs materially from its reviewed baseline
- **WHEN** the visual-regression command runs
- **THEN** verification MUST fail and identify the affected visual case

### Requirement: Failure artifacts

When a visual comparison fails, the runner MUST preserve an actual screenshot and SHOULD preserve a useful diff image. CI MUST upload the visual failure output as a retained workflow artifact when available.

#### Scenario: Failed CI comparison

- **GIVEN** a visual-regression case fails in CI
- **WHEN** the workflow completes
- **THEN** maintainers MUST be able to retrieve the generated visual failure output without reproducing the run locally

### Requirement: Explicit baseline updates

Intentional visual changes MUST update baselines through an explicit update command and the resulting baseline changes MUST be reviewed together with the implementation that caused them.

Normal CI verification MUST NOT regenerate or overwrite baselines automatically.

#### Scenario: Ordinary pull-request verification

- **GIVEN** a pull request runs the normal visual workflow
- **WHEN** the screenshot output differs from a baseline
- **THEN** CI MUST report a failure rather than silently accepting the new image as the baseline

### Requirement: Verification-only dependencies

Playwright, Chromium, Pillow, and any future visual-comparison dependencies MUST remain development/CI verification dependencies only. They MUST NOT become required by consumers of `src/` or alter the framework-independent runtime baseline.

#### Scenario: Consumer integration remains unchanged

- **GIVEN** a consuming application uses `src/tokens.css`, `src/tui.css`, and optionally `src/tui.js`
- **WHEN** visual-regression tooling exists in the repository
- **THEN** the consuming application MUST NOT need Playwright, Python packages, Chromium, or a build step to use the UI kit
