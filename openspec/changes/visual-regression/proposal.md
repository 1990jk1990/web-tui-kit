# Visual regression coverage

Status: Active
Related issue: #5
Change class: Class 2 — verification architecture

## Motivation

The project now has a stable enough core dialog/component surface and an accessibility/keyboard baseline that visual changes should be detected automatically before merge. Manual demo inspection remains useful, but it does not provide reproducible evidence that desktop and narrow/mobile compositions stayed unchanged.

## Proposed behavior

- Add browser-driven screenshot regression checks for canonical demo views.
- Capture at least the canonical package-configuration demo and the core dialog gallery at fixed desktop and narrow/mobile viewports.
- Use a pinned Playwright/Chromium toolchain so CI rendering is repeatable.
- Store reviewed baseline screenshots in the repository and compare future renders against them.
- Produce actual/diff artifacts when a visual comparison fails so maintainers can inspect the change.
- Keep visual-test dependencies outside the runtime contract; consuming applications still need only the static assets under `src/`.
- Document an explicit baseline-update procedure for intentional visual changes.

## Compatibility and boundaries

The browser-native runtime remains unchanged and framework-independent. The new dependencies are development/CI verification dependencies only. The visual suite does not replace structural unit tests, accessibility review, or manual device checks.

The authoritative visual baseline is generated on the repository's pinned Linux CI environment. Local runs on other operating systems may differ in font rasterization; maintainers should regenerate accepted baselines through the documented canonical environment rather than silently weakening thresholds.

## Acceptance criteria

- A reproducible browser-driven visual-regression command exists.
- Desktop and narrow/mobile baseline screenshots exist for `demo/index.html` and `demo/dialogs.html`.
- CI runs the visual checks on pull requests and pushes to `main`.
- Visual failures retain useful actual/diff artifacts.
- Intentional baseline updates are documented and reviewable.
- Architecture/testing documentation and an ADR explain the verification-tooling decision.
- Existing runtime and structural tests continue to pass.
