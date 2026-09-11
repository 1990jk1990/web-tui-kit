# Project overview

## Purpose

`web-tui-kit` is a reusable browser UI design system for applications that should present a consistent text-oriented interface inspired by Debian debconf, `dialog`, and `whiptail`.

Its primary use case is to let independent browser applications share one UI language and to give humans and coding assistants a durable reference that can be reused instead of recreating the style from screenshots or chat history.

## Users

- developers building browser-based tools,
- AI coding agents implementing those tools,
- end users operating the resulting interfaces on Linux desktops and Android devices.

## Scope

The repository provides design tokens, CSS component styles, small progressive-enhancement JavaScript, executable visual/semantic references, requirements, architecture documentation, development guidance, structural regression tests, browser-driven Chromium visual regression baselines for canonical demos, cross-browser interaction verification in Chromium/Firefox, browser accessibility-semantic verification in Chromium/Firefox, representative narrow touch-browser evidence, deterministic tagged release artifacts for direct vendoring, and framework/template integration recipes that reuse the canonical browser-native contract.

The canonical visual/semantic reference is `demo/index.html`: a centered package-style dialog with a blue desktop background, grey beveled surface, red title accent, recessed scrollable checklist, blue focused row, text-style checkbox markers, contextual help accents, and angle-bracket actions. Its native labels/groups/headings are also exercised by browser semantic regression.

`demo/dialogs.html` is the executable catalog for common dialog compositions: message, yes/no confirmation, input, action menu, radiolist, checklist, and progress/gauge. It also supplies canonical semantic evidence for labels, groups, native state, and progress. `demo/components.html` provides broader general component coverage.

`examples/react/`, `examples/vue/`, and `examples/server-rendered/` show how different application stacks consume the same semantic markup/class/event contract. They are consumption recipes rather than separate framework runtimes.

The accepted behavioral, verification, release/distribution, and framework-integration contracts are canonical in `openspec/specs/`.

## Non-goals

`web-tui-kit` is not a terminal emulator, ncurses binding, application backend, routing framework, or full application framework. Consuming applications remain responsible for their domain logic, data access, authentication, routing, and application-specific behavior. Development-only browser/accessibility verification and release tooling is not part of the runtime contract consumed by applications.

The project does not maintain React/Vue adapter runtimes or require framework dependencies in `src/`. A future adapter requires a demonstrated integration gap and a deliberate architecture/specification change. Tagged direct vendoring remains the baseline distribution model.

Automated touch-capable Chromium evidence is not physical Android/Android WebView certification. Browser role/name/state automation is not a WCAG conformance statement and is not screen-reader/assistive-technology certification. Physical-device and real assistive-technology evidence are recorded separately only after actual runs.

## Maturity

The project is pre-1.0. Version `0.6.0` is the current published prerelease and packages the established visual foundation, core dialog patterns, accessibility/keyboard refinement, canonical Chromium visual regression, deterministic release/distribution workflow, React/Vue/server-rendered consumption recipes, and browser-driven Chromium/Firefox interaction verification with representative narrow touch behavior. The active v0.7 milestone adds browser accessibility-semantic regression for canonical roles, names, labels, native states, and progress semantics while preserving Linux Chromium as the sole screenshot authority and keeping assistive-technology/device claims evidence-bound. Public component contracts may still evolve through minor releases before 1.0.
