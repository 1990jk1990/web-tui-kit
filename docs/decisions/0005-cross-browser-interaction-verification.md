# ADR-0005: Cross-browser interaction verification with Playwright

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `openspec/changes/browser-interaction-verification/`
- Related issue: #17
- Supersedes: none
- Superseded by: none

## Context

`web-tui-kit` already protects canonical visual output with Playwright/Chromium screenshot regression and inexpensive source-level tests. Important keyboard and custom-event contracts, however, can only be proven end-to-end by executing the real runtime in a browser engine. Firefox is also a stated compatibility target where the required standards are supported, but the project previously had no automated Firefox browser evidence.

Interaction verification must strengthen evidence without turning browser automation into a runtime dependency, without duplicating the visual baseline matrix, and without presenting mobile emulation as physical Android certification.

## Decision

Use the existing pinned Python Playwright dependency for browser-driven interaction verification.

Run the desktop interaction contract in both the Playwright-pinned Chromium and Firefox engines. The suite exercises the canonical `src/` runtime through a purpose-built semantic HTML fixture and verifies:

- bubbling `tui:escape` dispatch from opted-in surfaces,
- `data-tui-list` ArrowUp/ArrowDown/Home/End focus movement and wrapping,
- disabled, inert, hidden, and `aria-disabled` item skipping,
- no synthetic checkbox activation during focus navigation,
- preservation of native radio-group arrow behavior,
- preservation of text-entry arrow/caret behavior.

Also run a narrow touch-capable Chromium context that verifies mobile viewport/touch/coarse-pointer conditions and native tap interaction. This is representative browser evidence only; it does not certify Android OS, WebView, on-screen-keyboard, or physical-device behavior.

Keep Chromium/Linux as the sole canonical pixel-baseline environment defined by ADR-0002. Firefox is added for behavioral compatibility evidence, not as a second screenshot-baseline authority.

Browser automation remains development/CI-only. `src/` keeps no Playwright, browser-driver, Node.js, framework, or package-manager dependency.

## Considered alternatives

- Continue relying on source-level assertions for interaction behavior.
- Add Firefox screenshot baselines in addition to Chromium baselines.
- Introduce a Node-based browser test project and package-manager lockfile.
- Use Selenium/WebDriver as a second browser-automation stack.
- Treat touch-capable Chromium emulation as sufficient evidence for physical Android support.

## Consequences

### Positive

- Verifies actual keyboard/event behavior in two browser engines instead of inferring it from source text.
- Reuses the already pinned Playwright toolchain instead of creating another test stack.
- Exercises Firefox without creating a second visual baseline authority.
- Adds behavioral evidence for the same touch/coarse-pointer environment already used by mobile visual regression.
- Keeps the browser-native runtime and direct-vendoring distribution model unchanged.

### Negative / trade-offs

- CI becomes slower because Firefox must also be installed for the interaction job.
- Browser-engine behavior can change when the pinned Playwright version is deliberately upgraded, requiring review of interaction evidence.
- Automated touch emulation still cannot prove physical Android, vendor WebView, software-keyboard, or accessibility-service behavior.
- A purpose-built fixture adds test maintenance, although it avoids coupling interaction assertions to demo copy/layout.

## Evidence / notes

The interaction fixture must consume `src/tokens.css`, `src/tui.css`, and `src/tui.js` directly and must not duplicate reusable component styling or runtime behavior. Compatibility documentation owns the distinction between automated browser evidence, manual device evidence, and unverified gaps.
