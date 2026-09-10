# Browser interaction and compatibility verification

Status: Completed
Related issue: #17
Change class: Class 2 — verification architecture / compatibility evidence

## Motivation

`web-tui-kit` v0.5.0 had structural regression tests and canonical Chromium screenshot baselines, but several externally relevant interaction contracts were verified only by source-level assertions. This change proves those behaviors in real browser engines and strengthens compatibility evidence without changing the browser-native runtime or adding framework-specific surfaces.

## Accepted behavior

- Browser-driven interaction verification covers `tui:escape`, `data-tui-list` ArrowUp/ArrowDown/Home/End focus navigation, unavailable-item skipping, native radio-group arrow behavior, and native text-entry arrow/caret behavior.
- The desktop interaction suite runs in the Chromium and Firefox browser engines pinned by Playwright 1.62.0.
- A narrow 390×844 touch-capable Chromium case verifies coarse-pointer/touch context, native row tap activation, and Escape dispatch.
- Linux Chromium remains the sole canonical pixel-baseline environment; Firefox provides behavioral compatibility evidence rather than a second screenshot authority.
- `tests/browser/interaction.html` is a purpose-built semantic fixture that consumes the canonical `src/` assets without duplicating reusable styles or runtime behavior.
- `.github/workflows/interaction-regression.yml` runs a read-only Chromium/Firefox matrix on pull requests and `main` and uploads failure screenshots when needed.
- Future tag-triggered release publication runs browser interaction verification before deterministic artifact creation/publication.
- Browser-test tooling remains development/CI-only and the package-manager-free runtime contract is unchanged.
- Compatibility documentation distinguishes automated desktop Chromium/Firefox evidence, touch-emulated Chromium evidence, and physical Android/device evidence.
- `docs/project/android-device-check.md` defines the manual physical-Android Chrome checklist and exact evidence record format. No physical-device result is claimed without an actual run.

## Boundaries

This change does not redesign the UI, change component semantics, add React/Vue adapter runtimes, publish to npm, add framework dependencies to `src/`, or claim physical Android verification from emulation.

No screenshot baseline changed as part of this milestone.

## Verification

- Fast repository tests and AI-DOC-1 structural validation passed on the reconciled feature branch.
- Strict MkDocs documentation build passed.
- Existing Chromium visual-regression baselines passed unchanged.
- Chromium desktop interaction verification passed.
- Narrow touch-capable Chromium interaction verification passed after correcting the test to tap the visible label row rather than the intentionally visually-hidden native checkbox input.
- Firefox desktop interaction verification passed.
- The complete feature diff was reviewed before archival.

## Architectural outcome

ADR-0005 records the durable strategy: reuse the pinned Playwright toolchain for Chromium/Firefox interaction evidence while keeping Chromium/Linux as the canonical screenshot authority and keeping physical Android claims separate from emulation.

## Follow-up

The accumulated verification capability is a new supported project behavior and will be prepared as a focused `0.6.0` release after this feature change is merged. Physical Android evidence remains an independent follow-up that can be added only after a real device run.
