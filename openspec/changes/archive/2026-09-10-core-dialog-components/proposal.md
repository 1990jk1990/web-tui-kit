# Core dialog components

Status: Completed
Related issue: #2
Related pull request: #11
Change class: Class 1 — behavioral

## Motivation

The initial design system established the visual language and a canonical checklist-style package configuration reference, but consuming applications still needed to assemble several common `dialog`/`whiptail` interaction patterns themselves.

## Delivered behavior

`web-tui-kit` now provides documented, reusable patterns for:

- message dialogs with a single acknowledgement action,
- yes/no confirmation dialogs,
- input dialogs using native form controls,
- menu/action lists,
- radio-selection lists,
- checklist lists,
- progress/gauge presentation.

List-like controls can opt in to ArrowUp, ArrowDown, Home, and End navigation through `data-tui-list` without removing normal Tab reachability. Space/Enter behavior remains owned by the underlying native controls.

The patterns preserve the established hard-edged Debian debconf / `dialog` / `whiptail` visual language and remain responsive for narrow touch viewports.

## Compatibility and boundaries

The implementation remains framework-independent plain HTML/CSS/JavaScript. No package manager, bundler, framework runtime, backend, or application routing behavior was introduced.

## Verification

- All core dialog patterns are represented in `demo/dialogs.html`.
- Reusable styling lives in `src/tui.css`; shared exact sizing remains tokenized in `src/tokens.css`.
- Optional list keyboard navigation lives in `src/tui.js`.
- Repository regression tests cover the selectors, demo coverage, and keyboard contract.
- `DESIGN_SYSTEM.md`, architecture, testing docs, README, changelog, and current OpenSpec were reconciled.
- GitHub Actions run `34533768810` completed successfully before archival.
