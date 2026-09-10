# Project overview

## Purpose

`web-tui-kit` is a reusable browser UI design system for applications that should present a consistent text-oriented interface inspired by Debian debconf, `dialog`, and `whiptail`.

Its primary use case is to let independent browser applications share one UI language and to give humans and coding assistants a durable reference that can be reused instead of recreating the style from screenshots or chat history.

## Users

- developers building browser-based tools,
- AI coding agents implementing those tools,
- end users operating the resulting interfaces on Linux desktops and Android devices.

## Scope

The repository provides design tokens, CSS component styles, small progressive-enhancement JavaScript, executable visual references, requirements, architecture documentation, and development guidance.

The canonical visual reference is `demo/index.html`: a centered package-style dialog with a blue desktop background, grey beveled surface, red title accent, recessed scrollable checklist, blue focused row, text-style checkbox markers, contextual help accents, and angle-bracket actions.

`demo/dialogs.html` is the executable catalog for common dialog compositions: message, yes/no confirmation, input, action menu, radiolist, checklist, and progress/gauge. `demo/components.html` provides broader general component coverage.

The accepted behavioral contract is canonical in `openspec/specs/`.

## Non-goals

`web-tui-kit` is not a terminal emulator, ncurses binding, application backend, routing framework, or full application framework. Consuming applications remain responsible for their domain logic, data access, authentication, routing, and application-specific behavior.

## Maturity

The project is in early development. The current implementation establishes the visual foundation, common package-dialog compositions, native form controls, selectable list patterns, optional keyboard list navigation, menus, progress/gauges, tables, buttons, and status patterns. No stable release has been published yet.
