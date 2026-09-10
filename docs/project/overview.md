# Project overview

## Purpose

`web-tui-kit` is a reusable browser UI design system for applications that should present a consistent text-oriented interface inspired by Debian debconf, `dialog`, and `whiptail`.

Its primary use case is to let independent browser applications share one UI language and to give humans and coding assistants a durable reference that can be reused instead of recreating the style from screenshots or chat history.

## Users

- developers building browser-based tools,
- AI coding agents implementing those tools,
- end users operating the resulting interfaces on Linux desktops and Android devices.

## Scope

The repository provides design tokens, CSS component styles, small progressive-enhancement JavaScript, executable visual references, requirements, architecture documentation, development guidance, structural regression tests, browser-driven visual regression baselines for canonical demos, and deterministic tagged release artifacts for direct vendoring.

The canonical visual reference is `demo/index.html`: a centered package-style dialog with a blue desktop background, grey beveled surface, red title accent, recessed scrollable checklist, blue focused row, text-style checkbox markers, contextual help accents, and angle-bracket actions.

`demo/dialogs.html` is the executable catalog for common dialog compositions: message, yes/no confirmation, input, action menu, radiolist, checklist, and progress/gauge. `demo/components.html` provides broader general component coverage.

The accepted behavioral, verification, and release/distribution contracts are canonical in `openspec/specs/`.

## Non-goals

`web-tui-kit` is not a terminal emulator, ncurses binding, application backend, routing framework, or full application framework. Consuming applications remain responsible for their domain logic, data access, authentication, routing, and application-specific behavior. Development-only browser verification and release tooling is not part of the runtime contract consumed by applications.

The v0.4 release line does not provide npm/package-registry distribution or framework adapters. Tagged direct vendoring remains the baseline.

## Maturity

The project is pre-1.0. Version `0.4.0` establishes the first tagged release baseline after the visual foundation, core dialog patterns, accessibility/keyboard refinement, and visual regression milestones. Canonical package/dialog rendering is guarded by reviewed desktop and touch-capable mobile screenshot baselines in CI. Public component contracts may still evolve through minor releases before 1.0.
