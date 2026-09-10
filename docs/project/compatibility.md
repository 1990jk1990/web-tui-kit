# Compatibility evidence

This page records what the project has actually exercised. It is intentionally more conservative than the compatibility targets in OpenSpec.

## Release target

The runtime prioritizes current Chromium-based browsers on Linux desktop and Android and should remain usable in current Firefox where the required standards are supported. The UI is browser-native HTML/CSS/JavaScript and does not require an operating-system-specific client.

## Current automated evidence

The repository pins Playwright `1.62.0`. In the canonical GitHub Actions Linux environment used for the v0.6 verification work, that Playwright release installed Chrome for Testing `151.0.7922.34` (Chromium build v1234) and Firefox `153.0` (Playwright Firefox build v1538). Browser-build numbers are evidence for this verification run, not a promise that downstream users must run those exact browser versions.

| Environment | Evidence | Current status |
| --- | --- | --- |
| Linux desktop, Chromium | GitHub Actions on Ubuntu 24.04 installs the Chromium build pinned by Playwright 1.62.0. Canonical package/dialog demos are compared with reviewed desktop screenshots. The interaction fixture also verifies bubbling `tui:escape`, ArrowUp/ArrowDown/Home/End `data-tui-list` focus behavior and wrapping, unavailable-item skipping, no checkbox activation from focus movement, native radio arrow behavior, and native text-entry caret movement. | Automated canonical visual + behavioral evidence |
| Linux desktop, Firefox | GitHub Actions installs Firefox 153.0 from the same pinned Playwright release and runs the desktop interaction contract against the canonical runtime assets. Firefox is not used as a second screenshot-baseline authority. | Automated behavioral compatibility evidence |
| Android-like Chromium, narrow touch context | Pinned Chromium runs at fixed 390×844 viewport/screen dimensions with `is_mobile` and `has_touch`. Canonical demos have reviewed mobile screenshots; the interaction suite additionally verifies touch capability, `(pointer: coarse)`, native tap activation through the visible checkbox row, and `tui:escape`. | Automated representative mobile/touch browser evidence |
| Physical Android Chrome / Android WebView | No physical Android device result is recorded yet. `android-device-check.md` defines the exact manual evidence procedure and record format. | Not independently verified |

## What the Chromium mobile/touch evidence proves

The mobile visual cases prove that the canonical demos render consistently in a Chromium mobile/touch browsing context, that the narrow viewport composition is stable, and that `@media (pointer: coarse)` rules participate in the reference rendering.

The interaction case independently confirms that the browser context exposes a coarse pointer and touch points, that the visible checklist-style touch row can activate its nested native checkbox, and that the Escape custom-event contract remains operable in the same narrow touch context.

These automated checks do **not** prove Android operating-system integration, vendor-specific Android WebView behavior, on-screen keyboard behavior, accessibility-service behavior, physical touch latency, device-specific viewport chrome, orientation handling on real hardware, or performance on a physical device. Those require separate evidence.

## Firefox interpretation

Firefox now has automated behavioral evidence for the standards-based progressive JavaScript contract. This materially strengthens the statement that the library should remain usable in current Firefox, but it is not equivalent to full Firefox visual certification: the project deliberately keeps Linux Chromium as the canonical pixel-regression environment so rasterization differences do not create competing screenshot authorities.

If a Firefox-specific visual defect is reported, add focused evidence for that defect instead of silently assuming the Chromium pixel baseline proves Firefox rendering.

## Physical Android procedure

`docs/project/android-device-check.md` defines the current manual physical-device checklist and an evidence record template. A real result must include the tested repository commit/tag, device model, Android version, Chrome version, date, and observed outcomes. Until such a record exists, physical Android Chrome and WebView remain unverified regardless of the mobile/touch Chromium CI result.

## Release interpretation

For pre-1.0 releases, automated canonical Chromium screenshots plus Chromium/Firefox interaction verification provide the normal browser release gates. Representative touch-capable Chromium evidence supports the Android browser design target but must continue to be described as emulation/browser evidence rather than physical-device certification.

Tag-triggered publication runs the browser interaction suite before release artifact creation/publication, so a regression in the exercised Chromium/Firefox interaction contract blocks a future release.

## Known verification gaps

The current suite does not automate Firefox pixel rendering, accessibility-tree/assistive-technology behavior, physical Android devices, Android WebView/browser-version matrices, software-keyboard behavior, real-device orientation changes, physical touch latency, or an automated React/Vue version matrix for the source recipes.

These are verification gaps, not known runtime failures. Add targeted evidence when a downstream consumer, release risk, or observed defect makes a gap material.
