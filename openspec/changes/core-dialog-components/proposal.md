# Core dialog components

Status: Active
Related issue: #2
Change class: Class 1 — behavioral

## Motivation

The initial design system establishes the visual language and a canonical checklist-style package configuration reference, but consuming applications still need to assemble several common `dialog`/`whiptail` interaction patterns themselves.

## Proposed behavior

`web-tui-kit` will provide documented, reusable patterns for:

- message dialogs with a single acknowledgement action,
- yes/no confirmation dialogs,
- input dialogs using native form controls,
- menu/action lists,
- radio-selection lists,
- checklist lists,
- progress/gauge presentation.

List-like controls will optionally support ArrowUp, ArrowDown, Home, and End navigation through `data-tui-list` without removing normal Tab reachability. Space/Enter behavior remains owned by the underlying native controls.

The new patterns must preserve the established hard-edged Debian debconf / `dialog` / `whiptail` visual language and remain usable on narrow touch viewports.

## Compatibility and boundaries

The implementation remains framework-independent plain HTML/CSS/JavaScript. No package manager, bundler, framework runtime, backend, or application routing behavior is introduced.

## Acceptance criteria

- All listed dialog patterns are represented in an executable demo page.
- Reusable styling is implemented in `src/tui.css` and exact shared values stay tokenized in `src/tokens.css` where appropriate.
- Optional list keyboard navigation is implemented as progressive enhancement in `src/tui.js`.
- New behavior has repository-level regression coverage.
- `DESIGN_SYSTEM.md` documents the public classes and data attributes.
- Existing canonical package-configuration demo remains valid.
