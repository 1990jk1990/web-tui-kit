# Compatibility evidence

This page records what the project has actually exercised. It is intentionally more conservative than the compatibility targets in OpenSpec.

Compatibility evidence and public API stability are separate concerns. `docs/project/public-contract.md` defines which runtime names/semantic relationships consumers may rely on; this page records environments in which those contracts have actually been exercised.

## Release target

The runtime prioritizes current Chromium-based browsers on Linux desktop and Android and should remain usable in current Firefox where the required standards are supported. The UI is browser-native HTML/CSS/JavaScript and does not require an operating-system-specific client.

## Current automated evidence

The repository pins Playwright `1.62.0`. In the canonical GitHub Actions Linux environment used for browser verification, that Playwright release installs Chrome for Testing `151.0.7922.34` (Chromium build v1234) and Firefox `153.0` (Playwright Firefox build v1538). Browser-build numbers are evidence for these repository verification runs, not a promise that downstream users must run those exact browser versions.

Framework recipe verification additionally pins representative direct development dependencies under `tests/framework/`: React `19.0.0`, React DOM `19.0.0`, Vue `3.5.13`, `@vue/compiler-sfc` `3.5.13`, and esbuild `0.24.2`. These versions are evidence anchors for the checked-in recipes, not an exhaustive supported-version range.

| Environment | Evidence | Current status |
| --- | --- | --- |
| Linux desktop, Chromium | GitHub Actions on Ubuntu 24.04 installs the Chromium build pinned by Playwright 1.62.0. Canonical package/dialog demos are compared with reviewed desktop screenshots. The interaction fixture verifies `tui:escape`, list focus behavior, unavailable-item skipping, native radio behavior, and native text-entry caret movement. The accessibility suite additionally verifies canonical browser-computed roles, accessible names, label associations, checked/disabled states, named groups/regions, and native progress semantics. | Automated canonical visual + behavioral + semantic evidence |
| Linux desktop, Firefox | GitHub Actions installs Firefox 153.0 from the same pinned Playwright release and runs the desktop interaction and accessibility-semantic contracts against canonical runtime/demo assets. Firefox is not used as a second screenshot-baseline authority. | Automated behavioral + semantic compatibility evidence |
| Android-like Chromium, narrow touch context | Pinned Chromium runs at fixed 390×844 viewport/screen dimensions with `is_mobile` and `has_touch`. Canonical demos have reviewed mobile screenshots; interaction verification confirms touch/coarse-pointer context and native tap operation; the semantic suite verifies the core package region, checklist, representative native checkbox, and action remain discoverable with the same semantic identities. | Automated representative mobile/touch browser evidence |
| React recipe, representative toolchain | The canonical `examples/react/PackageConfiguration.jsx` source is bundled with React/React DOM 19.0.0 and rendered in pinned Linux Chromium against canonical `src/` assets. The smoke run verifies native checkbox state, list focus enhancement, Escape-to-cancel handling, and accepted service payloads. | Automated representative recipe compile + runtime evidence |
| Vue recipe, representative toolchain | The canonical `examples/vue/PackageConfiguration.vue` SFC is compiled with Vue/compiler-sfc 3.5.13, bundled with esbuild 0.24.2, and rendered in pinned Linux Chromium against canonical `src/` assets. The same native state/focus/Escape/accept contracts are exercised. | Automated representative recipe compile + runtime evidence |
| Server-rendered recipe | The browser-openable canonical template recipe is loaded with canonical assets in the framework-recipe smoke run; native form state, list focus enhancement, and Escape handling are verified. | Automated representative template-consumption evidence |
| Physical Android Chrome / Android WebView | No physical Android device result is recorded yet. `android-device-check.md` defines the exact manual evidence procedure and record format. | Not independently verified |
| Screen reader / other assistive technology | No real screen-reader or other assistive-technology session is recorded. Browser role/name/state queries exercise browser accessibility mappings but are not an AT session. | Not independently verified |

## What the Chromium mobile/touch evidence proves

The mobile visual cases prove that the canonical demos render consistently in a Chromium mobile/touch browsing context, that the narrow viewport composition is stable, and that `@media (pointer: coarse)` rules participate in the reference rendering.

The interaction case independently confirms that the browser context exposes a coarse pointer and touch points, that the visible checklist-style touch row can activate its nested native checkbox, and that the Escape custom-event contract remains operable in the same narrow touch context. The accessibility semantic case confirms that the canonical named package surface, group, representative checkbox, and action retain their browser-computed semantic identities in that representative context.

These automated checks do **not** prove Android operating-system integration, vendor-specific Android WebView behavior, on-screen keyboard behavior, physical accessibility-service behavior, screen-reader output, physical touch latency, device-specific viewport chrome, orientation handling on real hardware, or performance on a physical device. Those require separate evidence.

## Accessibility semantic interpretation

The accessibility regression suite queries the browser's computed role/name mappings and checks native state/value for canonical controls. It is useful regression evidence for lost labels, accidental accessible-name pollution, incorrect native state, or semantic markup regressions that screenshots and keyboard tests can miss.

The canonical `.tui-dialog` CSS class remains presentation-only. Section-based demos are intentionally expected to expose named-region/heading semantics rather than being promoted to modal-dialog semantics solely for testing. Purely visual helper annotations are hidden from accessible names when they do not carry operation-critical meaning.

A passing semantic suite is **not** a WCAG conformance statement and is **not** screen-reader or assistive-technology certification. Real AT/browser combinations can add behavior beyond browser role/name computation and require separate manual/specialized evidence.

## Framework recipe interpretation

The framework recipe regression closes the prior gap where React/Vue examples were source-structure checked but never compiled or executed. It deliberately tests the canonical checked-in recipe files rather than test-only rewrites and renders them with the same `src/` runtime assets consumed by plain browser applications.

A pass means those exact recipe files compile and interoperate with the exact pinned representative direct framework/tool versions in the exercised Linux Chromium run. It does **not** establish an automated React/Vue version matrix, compatibility with older/newer framework releases, SSR/hydration guarantees, framework-specific routing behavior, or support for arbitrary consumer bundler configurations. Add a focused version/capability case when a concrete downstream need makes it material.

## Firefox interpretation

Firefox has automated behavioral and accessibility-semantic evidence for the standards-based browser-native contract. This strengthens the statement that the library should remain usable in current Firefox, but it is not equivalent to full Firefox visual certification: the project deliberately keeps Linux Chromium as the canonical pixel-regression environment so rasterization differences do not create competing screenshot authorities.

If a Firefox-specific visual or semantic defect is reported, add focused evidence for that defect instead of silently assuming the Chromium pixel baseline proves Firefox rendering.

## Physical Android procedure

`docs/project/android-device-check.md` defines the current manual physical-device checklist and an evidence record template. A real result must include the tested repository commit/tag, device model, Android version, Chrome version, date, and observed outcomes. Until such a record exists, physical Android Chrome and WebView remain unverified regardless of the mobile/touch Chromium CI result.

## Public contract and 1.0 interpretation

The v0.9 public-contract audit turned the exercised browser-native surface into an explicit compatibility inventory. Structural public-contract tests protect declared `--tui-*` token names, `tui-*` classes, scoped state hooks, progressive data attributes/events, and release inclusion from silent drift. Browser visual/interaction/accessibility suites validate behavior without replacing that inventory.

Published `v0.9.0` then passed every established release gate, including unchanged canonical Chromium pixels, Chromium/Firefox interaction and semantic verification, representative framework-recipe execution, and deterministic archive validation. That evidence, together with completion of the selected pre-1.0 cleanup and the absence of another focused open product/technical gap, supports the deliberate `1.0.0` stability transition.

Starting with 1.0, normal Semantic Versioning applies to the declared public contract. This stability commitment does **not** convert current evidence gaps into unsupported certification claims. In particular, no physical Android, real assistive-technology, WCAG certification, registry publication, maintained framework adapter, or exhaustive framework-version matrix is implied by 1.0. Those domains remain documented gaps or future product decisions unless accepted requirements change.

## Release interpretation

Stable 1.x releases retain the same automated browser release gates used to establish the 1.0 baseline: canonical Chromium screenshots, Chromium/Firefox interaction and accessibility-semantic verification, representative touch-capable Chromium evidence, representative framework/template recipe verification, structural/public-contract tests, documentation validation, and deterministic archive validation.

Tag-triggered publication runs those gates before release artifact creation/publication. `v0.*` tags remain GitHub prereleases, while `v1.0.0` and later stable-line tags publish normal GitHub Releases. The deterministic focused archive carries `docs/project/public-contract.md`, allowing downstream users to see the supported stability boundary together with the runtime.

Representative touch-capable Chromium evidence supports the Android browser design target but must continue to be described as emulation/browser evidence rather than physical-device certification.

## Known verification gaps

The current suite does not automate Firefox pixel rendering, real screen-reader/assistive-technology sessions, full WCAG evaluation, physical Android devices, Android WebView/browser-version matrices, software-keyboard behavior, real-device orientation changes, physical touch latency, physical Android accessibility services, or a broad React/Vue/framework-tooling version matrix beyond the pinned representative recipe cases.

These are verification gaps, not known runtime failures. Add targeted evidence when a downstream consumer, release risk, or observed defect makes a gap material.
