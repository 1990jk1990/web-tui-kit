# ADR-0006: Browser accessibility semantics verification with Playwright

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `openspec/changes/accessibility-semantics-verification/`
- Related issue: #20
- Supersedes: none
- Superseded by: none

## Context

`web-tui-kit` already verifies visual output in pinned Chromium and interaction behavior in pinned Chromium/Firefox. The remaining documented verification gap is browser-exposed accessibility semantics: a control can still render correctly and respond to input while losing an accessible name, label relationship, native state, or useful landmark/group semantics.

The project deliberately prefers native HTML and must avoid turning accessibility testing into a parallel ARIA implementation. It also needs an evidence boundary: browser semantic automation can detect important regressions, but it cannot establish how every screen reader or assistive technology announces the interface and cannot by itself prove WCAG conformance.

## Decision

Reuse the existing pinned Python Playwright toolchain for a separate accessibility-semantics regression suite.

The suite runs the canonical `demo/index.html` and `demo/dialogs.html` pages rather than a second accessibility-only component implementation. It uses browser role/name queries plus native state/value checks to verify representative package/dialog semantics in the Playwright-pinned Chromium and Firefox engines. A narrow touch-capable Chromium case verifies that the core semantic identities remain available in the representative mobile/touch context.

Keep `.tui-dialog` semantics honest: the CSS class is presentation-only, so the canonical section-based examples are verified as named regions/headings rather than being assigned or asserted as modal dialogs. Applications that need true modal behavior continue to own native `<dialog>` or equivalent application-level semantics/lifecycle.

Purely visual helper annotations embedded in canonical controls/labels are marked `aria-hidden="true"` when they do not add operation-critical meaning. This keeps the visible whiptail-style hints without accidentally appending repeated helper text to native control accessible names.

Run the accessibility suite as its own read-only CI matrix on pull requests and `main`. After proving stable in the feature branch, run it in the tag-triggered release workflow before deterministic artifact creation/publication.

Browser automation remains development/CI-only. No Playwright, browser engine, Python, ARIA widget framework, or accessibility-test runtime becomes a dependency of `src/` or downstream applications.

## Evidence boundary

A passing suite means the exercised browser engines expose the accepted roles, names, labels, and native states for the tested canonical patterns. It does not mean:

- every screen reader announces the UI identically,
- assistive technologies on Linux/Android have been certified,
- physical Android accessibility services have been tested,
- all WCAG success criteria have been evaluated,
- usability for every disability/access method has been established.

Those claims require separate manual or specialized evidence and must only be recorded when actually performed.

## Considered alternatives

- Continue relying on source-level semantic assertions only.
- Add a second accessibility-only fixture that duplicates all canonical demo patterns.
- Introduce axe-core/Node.js and a package-manager project immediately.
- Replace native controls with custom ARIA widgets to make role assertions explicit.
- Treat successful browser semantic queries as screen-reader or WCAG certification.

## Consequences

### Positive

- Detects regressions that visual and interaction suites can miss, including lost names/labels/native states.
- Reuses the already pinned browser toolchain and avoids a new package manager/test stack.
- Verifies the actual canonical demo markup that downstream developers and coding agents are expected to copy.
- Preserves native HTML as the primary accessibility mechanism.
- Makes the evidence boundary explicit and reviewable.

### Negative / trade-offs

- CI installs/runs another browser verification suite and therefore takes longer.
- Browser role/name computation is evidence from browser accessibility mappings, not an end-to-end assistive-technology session.
- Directly testing canonical demos couples semantic checks to accepted demo composition; intentional semantic changes require deliberate test/spec updates.
- Hiding visual helper hints from names means any helper that later becomes operation-critical must be exposed deliberately as an accessible description rather than relying on accidental label text.

## Evidence / notes

Linux Chromium remains the only canonical screenshot-baseline authority under ADR-0002. Firefox remains compatibility evidence. ADR-0005 continues to own interaction verification and the physical-Android/emulation distinction. This decision adds semantic evidence without changing either of those authorities or the browser-native runtime dependency direction.
