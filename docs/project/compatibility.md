# Compatibility evidence

This page records what the project has actually exercised. It is intentionally more conservative than the compatibility targets in OpenSpec.

## Release target

The runtime prioritizes current Chromium-based browsers on Linux desktop and Android and should remain usable in current Firefox where the required standards are supported. The UI is browser-native HTML/CSS/JavaScript and does not require an operating-system-specific client.

## Current automated evidence

| Environment | Evidence | Current status |
| --- | --- | --- |
| Linux desktop, Chromium | GitHub Actions on `ubuntu-latest` installs the Chromium build pinned by Playwright 1.62.0, opens the canonical demos, and compares reviewed desktop screenshots. Structural tests also run on the same Linux CI family. | Automated release-gate evidence |
| Android-like Chromium, narrow touch context | The same pinned Chromium is launched with fixed 390×844 viewport/screen dimensions plus `is_mobile` and `has_touch`. This activates mobile viewport behavior and coarse-pointer CSS and compares reviewed mobile screenshots. | Automated representative browser-layout evidence |
| Firefox desktop | Core code intentionally uses standards-based HTML/CSS/JS and avoids a framework runtime. | Compatibility target; no automated browser run yet |
| Physical Android device / Android WebView | No physical-device or emulator job is currently part of CI. | Not yet independently verified |

## What the mobile visual test proves

The mobile visual cases prove that the canonical demos render consistently in a Chromium mobile/touch browsing context, that the narrow viewport composition is stable, and that `@media (pointer: coarse)` rules participate in the reference rendering.

They do **not** prove Android operating-system integration, vendor-specific WebView behavior, on-screen keyboard behavior, accessibility-service behavior, or performance on a physical device. Those require separate device/emulator evidence.

## Release interpretation

For pre-1.0 releases, automated Linux Chromium plus touch-capable mobile Chromium emulation is sufficient to guard the canonical browser UI baseline. Any release notes or README language must describe the Android result as a supported design target backed by representative mobile-Chromium rendering, not as physical-device certification.

When a real Android device/emulator matrix is added, record the tested browser/WebView versions, device/API level, test date, and what was exercised rather than replacing this evidence page with a generic “Android supported” statement.

## Known verification gaps

The current suite does not yet automate Firefox rendering, browser interaction flows beyond the repository's small JavaScript contracts, accessibility-tree/assistive-technology testing, soft-keyboard behavior, physical touch latency, orientation changes, or a matrix of Android browser/WebView versions.

These are verification gaps, not known runtime failures. Add targeted evidence when a downstream consumer or observed defect makes a gap material.
