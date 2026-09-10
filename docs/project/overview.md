# Project overview

## Purpose

`web-tui-kit` is a reusable browser UI design system for applications that should present a consistent text-oriented interface inspired by Debian debconf, `dialog`, and `whiptail`.

Its primary use case is to let independent browser applications share one UI language and to give humans and coding assistants a durable reference that can be reused instead of recreating the style from screenshots or chat history.

## Users

- developers building browser-based tools,
- AI coding agents implementing those tools,
- end users operating the resulting interfaces on Linux desktops and Android devices.

## Scope

The repository provides design tokens, CSS component styles, small progressive-enhancement JavaScript, executable visual references, requirements, architecture documentation, development guidance, structural regression tests, browser-driven Chromium visual regression baselines for canonical demos, cross-browser interaction verification in Chromium/Firefox, representative narrow touch-browser evidence, deterministic tagged release artifacts for direct vendoring, and framework/template integration recipes that reuse the canonical browser-native contract.

The canonical visual reference is `demo/index.html`: a centered package-style dialog with a blue desktop background, grey beveled surface, red title accent, recessed scrollable checklist, blue focused row, text-style checkbox markers, contextual help accents, and angle-bracket actions.

`demo/dialogs.html` is the executable catalog for common dialog compositions: message, yes/no confirmation, input, action menu, radiolist, checklist, and progress/gauge. `demo/components.html` provides broader general component coverage.

`examples/react/`, `examples/vue/`, and `examples/server-rendered/` show how different application stacks consume the same semantic markup/class/event contract. They are consumption recipes rather than separate framework runtimes.

The accepted behavioral, verification, release/distribution, and framework-integration contracts are canonical in `openspec/specs/`.

## Non-goals

`web-tui-kit` is not a terminal emulator, ncurses binding, application backend, routing framework, or full application framework. Consuming applications remain responsible for their domain logic, data access, authentication, routing, and application-specific behavior. Development-only browser verification and release tooling is not part of the runtime contract consumed by applications.

The project does not maintain React/Vue adapter runtimes or require framework dependencies in `src/`. A future adapter requires a demonstrated integration gap and a deliberate architecture/specification change. Tagged direct vendoring remains the baseline distribution model.

Automated touch-capable Chromium evidence is not physical Android/Android WebView certification. Physical device evidence is recorded separately only after an actual device run.

## Maturity

The project is pre-1.0. Version `0.5.0` is the current published prerelease and packages the established visual foundation, core dialog patterns, accessibility/keyboard refinement, visual regression gates, release/distribution workflow, and copy-ready React/Vue/server-rendered integration recipes without changing the browser-native runtime baseline. The active v0.6 milestone strengthens runtime evidence with browser-driven Chromium/Firefox interaction checks and representative narrow touch behavior while keeping Chromium/Linux as the canonical screenshot environment. Public component contracts may still evolve through minor releases before 1.0.
