# Changelog

All notable user-visible changes are recorded here.

## Unreleased

## 0.5.0 - 2026-09-11

Framework/template integration release.

- Added copy-ready React, Vue, and server-rendered integration recipes that reuse the canonical browser-native runtime contract.
- Added framework integration guidance covering immutable release pinning, native form state, `tui:escape`, `data-tui-list`, and styling boundaries.
- Added OpenSpec framework-integration requirements and ADR-0004, which prefers recipes over maintained framework adapters until a concrete capability gap is demonstrated.
- Added structural tests that keep framework dependencies and parallel styling out of `src/`.
- Expanded the deterministic focused release archive to include framework/template integration guidance and recipes.
- Made release tests version-agnostic so subsequent pre-1.0 release preparation does not require rewriting version-specific test assertions.

## 0.4.0 - 2026-09-11

First tagged pre-1.0 release.

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
- Added pinned Playwright/Chromium visual regression coverage with reviewed desktop and touch-capable mobile baselines for the canonical package and core-dialog demos plus CI failure artifacts.
- Added Semantic Versioning, immutable tagged distribution, deterministic focused release ZIP/checksum generation, and verified tag-triggered GitHub prerelease publication.
- Kept direct tagged vendoring as the primary distribution model; no npm/package-registry dependency is introduced for v0.4.0.
