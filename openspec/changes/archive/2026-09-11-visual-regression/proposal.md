# Visual regression coverage

Status: Completed
Related issue: #5
Related pull request: #13
Change class: Class 2 — verification architecture

## Motivation

After the core dialog/component surface and accessibility/keyboard baseline were established, visual changes needed automated regression evidence. Manual demo inspection remains useful, but it cannot reproducibly detect unintended drift in desktop or mobile composition.

## Delivered behavior

- Added pinned Python Playwright and Pillow development dependencies with Playwright's matching Chromium build as the canonical renderer.
- Added `scripts/visual_regression.py`, which serves the repository locally, captures fixed canonical cases, and compares them with reviewed PNG baselines.
- Added desktop and touch-capable mobile baselines for `demo/index.html` and `demo/dialogs.html` under `tests/visual/baselines/`.
- Mobile cases explicitly enable mobile/touch emulation so coarse-pointer CSS participates in the captured reference output.
- Added narrow image-comparison tolerance, missing/size mismatch failures, and actual/diff output for failed comparisons.
- Added a read-only GitHub Actions visual-regression workflow for pull requests and `main`, with failure artifacts retained for inspection.
- Documented explicit baseline updates; normal CI never silently accepts or rewrites screenshots.
- Added ADR-0002 and architecture/project documentation for the verification-tooling boundary.
- Kept Playwright, Chromium, and Pillow entirely outside the framework-independent runtime contract.

## Compatibility and boundaries

The browser-native runtime remains unchanged. Visual verification is a development/CI concern and does not require consuming applications to install Python, Playwright, Chromium, Pillow, a package manager, or a build step.

The Linux GitHub Actions environment is the canonical screenshot environment. Local rendering on other operating systems may differ because of font and graphics rasterization. The visual suite complements rather than replaces structural tests, accessibility review, browser interaction tests, or physical-device checks.

## Verification

- The initial baselines were generated and visually reviewed from the pinned Linux CI environment.
- Touch-aware mobile baselines were regenerated after enabling `is_mobile` and `has_touch` so the mobile reference actually exercises coarse-pointer behavior.
- AI-DOC-1 validation run `34536251962` completed successfully.
- Read-only visual-regression run `34536251918` completed successfully against the committed touch-aware baselines.
- The complete branch diff was inspected before archival.
