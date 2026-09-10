# Browser interaction and compatibility verification

Status: Active
Related issue: #17
Change class: Class 2 — verification architecture / compatibility evidence

## Motivation

`web-tui-kit` v0.5.0 has structural regression tests and canonical Chromium screenshot baselines, but several externally relevant interaction contracts are still verified only by source-level assertions. The next milestone should prove those behaviors in real browser engines and strengthen compatibility evidence without changing the browser-native runtime or adding framework-specific surfaces.

## Proposed behavior

- Add browser-driven interaction verification for `tui:escape`, `data-tui-list` ArrowUp/ArrowDown/Home/End focus navigation, disabled-item skipping, and preservation of native radio/text-entry keyboard behavior.
- Run the standards-based desktop interaction suite in the Playwright-pinned Chromium and Firefox engines.
- Add a narrow touch-capable Chromium interaction case so the responsive/coarse-pointer environment is exercised behaviorally in addition to screenshot comparison.
- Keep Linux Chromium as the canonical pixel-baseline environment; Firefox is interaction/compatibility evidence rather than a second screenshot baseline.
- Use a purpose-built test fixture that consumes the canonical `src/` assets and semantic controls rather than embedding alternate runtime behavior.
- Keep browser-test tooling development/CI-only and preserve the package-manager-free browser runtime contract.
- Update compatibility documentation to distinguish automated desktop Chromium/Firefox interaction evidence, touch-emulated Chromium evidence, and physical Android/device evidence.
- Define a small manual physical-Android Chrome checklist. Do not record physical-device support as verified until an actual device/browser result is supplied.

## Boundaries

This change does not redesign the UI, change component semantics, add React/Vue adapter runtimes, publish to npm, add framework dependencies to `src/`, or claim physical Android verification from emulation.

No screenshot baseline is intentionally changed by this milestone. If browser-driven tests reveal a real runtime defect, fix the defect through the normal OpenSpec/implementation/test workflow rather than weakening the verification.

## Acceptance criteria

- A deterministic browser interaction runner exists and fails on contract violations.
- Chromium desktop and Firefox desktop exercise Escape dispatch, list focus navigation, disabled-item skipping, native radio behavior, and text-entry arrow-key preservation.
- A narrow touch-capable Chromium case proves touch/mobile context and core interaction viability.
- CI installs the pinned Playwright browser builds needed by the interaction suite and runs the suite read-only on pull requests and `main`.
- Structural tests protect the interaction-runner/workflow contract.
- Compatibility evidence clearly separates automated browser evidence from physical-device evidence.
- Verification architecture and durable rationale are reconciled without changing the runtime dependency direction.
- Existing structural, documentation, visual-regression, and release checks remain green.
