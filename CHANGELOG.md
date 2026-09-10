# Changelog

All notable user-visible changes will be recorded here once release versioning begins.

## Unreleased

- Initial framework-independent web TUI design-system scaffold.
- AI-DOC-1 v1.3 project memory, architecture, requirements, validation, tests, and CI.
- Added a canonical package-configuration dialog reference modeled on the Debian/Ubuntu `dialog`/`whiptail` visual language.
- Added reusable `.tui-dialog`, scrollable checklist, help-label, access-key, and centered-screen patterns plus a separate component gallery.
- Added reusable message, yes/no, input, menu, radiolist, checklist, and native progress/gauge patterns.
- Added optional `data-tui-list` keyboard navigation with ArrowUp, ArrowDown, Home, and End while preserving native Tab and activation behavior.
- Added `demo/dialogs.html` as the executable gallery for core dialog patterns.
- Refined optional list navigation so native radio-group and text-entry arrow behavior is never intercepted; disabled, hidden, inert, and unavailable choices are skipped.
- Added disabled choice-row presentation and `forced-colors` system-color overrides for high-contrast environments.
- Established a motion-free core interaction contract: no required decorative animation, transitions, or smooth scrolling.
- Added pinned Playwright/Chromium visual regression coverage with reviewed desktop/mobile baselines for the canonical package and core-dialog demos plus CI failure artifacts.
