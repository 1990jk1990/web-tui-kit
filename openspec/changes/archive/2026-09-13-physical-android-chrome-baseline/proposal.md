# Physical Android Chrome baseline evidence

Status: Completed
Related issue: #34
Change class: Class 1 — compatibility-evidence policy/documentation

## Motivation

`web-tui-kit` 1.0 already had automated touch-capable Chromium evidence but no real-device Android browser result. A physical Android run against immutable `v1.0.0` completed the canonical manual checklist successfully.

The prior evidence procedure also required device manufacturer/model and exact Android/Chrome version numbers for every physical result. For the project baseline, that level of device metadata is not required: the maintained claim only needs to establish that the exact release was exercised on a real Android device in Chrome for Android, on a known date, with explicit observed outcomes. Exact model/version details remain useful when diagnosing a device-specific defect but are optional otherwise.

## Accepted behavior

- Physical Android claims still require an actual device run; Playwright touch/mobile emulation is not a substitute.
- A baseline record requires the exact repository commit/tag, test date, browser family, and observed PASS/FAIL outcomes from the canonical checklist.
- Device manufacturer/model and exact Android/Chrome version numbers are optional evidence metadata rather than mandatory baseline fields.
- Optional device/version details must never be inferred or fabricated when they were not retained by the tester.
- A physical Chrome for Android result does not imply Android WebView compatibility, multi-vendor/device coverage, a browser-version matrix, accessibility-service or screen-reader behavior, WCAG conformance, latency, or performance certification.
- The 2026-09-13 physical Chrome for Android run against immutable `v1.0.0` passed portrait layout, checklist touch/scroll, buttons/touch targets, Android software keyboard/input, radiolist behavior, and orientation change.
- No runtime source, public contract, screenshot baseline, release version, or release artifact changes are required for this evidence-only milestone.

## Verification

- The physical run was performed on an actual Android device using Chrome for Android against the served immutable `v1.0.0` repository state.
- Both canonical pages used by the procedure were exercised.
- All required manual checklist categories were reported PASS with no observed functional/layout defect.
- Canonical browser-verification specification, agent rules, testing guidance, compatibility evidence, and the Android evidence record were reconciled to the accepted metadata policy.

## Boundaries

This change does not establish Android WebView support, an Android device/version support matrix, screen-reader or other assistive-technology interoperability, WCAG conformance, performance guarantees, or physical-device CI. Linux Chromium remains the canonical screenshot-baseline authority and the existing automated release gates remain unchanged.

## Outcome

Issue #34 can be completed once the reconciled documentation change is merged. No patch/minor release is created solely for recording the evidence because the browser-native runtime and declared public contract are unchanged.
