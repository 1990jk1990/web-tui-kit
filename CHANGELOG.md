# Changelog

All notable user-visible changes are recorded here.

## Unreleased

- Fixed `.tui-dialog` on native `<dialog>` elements so the canonical `.tui-dialog-title` can protrude across the top bevel without being clipped by user-agent overflow; scrollable dialog content should remain on inner regions rather than the outer dialog surface.
- Added Chromium, Firefox, and representative narrow touch-capable Chromium regression coverage for the native-dialog title/overflow contract discovered through downstream `lighting-service` UI testing.

## 1.0.0 - 2026-09-11

Stable public-contract release.

- Declared the audited browser-native public contract stable under normal Semantic Versioning: PATCH preserves the contract, MINOR may add compatible surface/deprecations, and incompatible public-contract changes require a new MAJOR release.
- Kept the v0.9 public token/class/state/semantic-markup/data-attribute/event inventory unchanged for the 1.0 transition; no visual redesign or new runtime component behavior is introduced solely by the version change.
- Reconciled release automation so `v0.*` tags remain GitHub prereleases while `v1.0.0` and later stable-line tags publish normal GitHub Releases after the same verification gates.
- Retained immutable tagged vendoring and the deterministic focused ZIP/SHA-256 archive as the primary distribution model; 1.0 does not add an npm/package-registry runtime requirement.
- Preserved explicit evidence boundaries: automated Chromium/Firefox/touch/framework checks remain regression evidence rather than physical Android, assistive-technology/WCAG, or exhaustive framework-version certification.
- Added ADR-0009 documenting stable 1.0+ GitHub Release publication while retaining the tagged-vendoring distribution model.

## 0.9.0 - 2026-09-11

Public contract and 1.0 readiness release.

- Added an explicit public consumer-contract inventory covering runtime files, all canonical `--tui-*` tokens, reusable `tui-*` classes, scoped state hooks, semantic markup expectations, `data-tui-*` attributes, and the `tui:escape` event contract.
- Added pre-1.0 and post-1.0 compatibility/deprecation/migration rules plus evidence-based 1.0 exit criteria.
- Added structural regression coverage that fails when declared public runtime names are silently removed/renamed or when a new `tui-*` class/token appears without classification.
- Added the public-contract guide to the deterministic focused release archive.
- Corrected `.tui-help` to consume the existing public `--tui-help` token; normal default pixels are unchanged while forced-colors help accents now follow the documented `LinkText` mapping.
- Added ADR-0008 documenting the browser-native public stability boundary without introducing framework adapters, registry distribution, or unsupported certification claims.

## 0.8.0 - 2026-09-11

Executable framework recipe verification release.

- Added development/CI-only executable verification for the canonical React, Vue, and server-rendered integration recipes.
- Added exact representative React/Vue/compiler/bundler verification versions and compile the canonical JSX/SFC sources directly instead of maintaining test-only recipe copies.
- Added Chromium smoke checks for native checkbox state, canonical `data-tui-list` focus navigation, `tui:escape` application handling, accept payloads, and server-rendered form semantics.
- Added a dedicated read-only framework recipe CI workflow and made future tagged releases fail before artifact creation/publication when representative recipe verification fails.
- Added ADR-0007 and expanded framework-integration/compatibility evidence boundaries without introducing framework dependencies into `src/`, adapter packages, or npm distribution.

## 0.7.0 - 2026-09-11

Accessibility semantics verification release.

- Added browser-driven accessibility-semantic regression coverage over the canonical package and dialog demos in pinned Chromium and Firefox.
- Added a narrow touch-capable Chromium semantic case while keeping browser semantic automation distinct from physical Android and assistive-technology certification.
- Kept presentation-only `.tui-dialog` surfaces semantically honest as named regions and excluded purely visual helper hints from native control accessible names.
- Added a dedicated read-only accessibility CI matrix and made future tag-triggered releases fail before publication when semantic verification fails.
- Added ADR-0006 and a canonical accessibility-verification OpenSpec contract with explicit WCAG/screen-reader evidence boundaries.

## 0.6.0 - 2026-09-11

Browser interaction and compatibility-verification release.

- Added browser-driven interaction regression coverage for `tui:escape`, optional list navigation/disabled-item skipping, native radio behavior, and text-entry arrow-key preservation.
- Added pinned Chromium and Firefox desktop interaction evidence plus a narrow touch-capable Chromium interaction case without changing the canonical Chromium screenshot baseline.
- Added a dedicated interaction CI matrix and made future tag-triggered releases fail before publication when browser interaction verification fails.
- Added explicit compatibility-evidence boundaries and a manual physical-Android Chrome check procedure; mobile/touch emulation remains representative evidence rather than device certification.
- Added ADR-0005 and a canonical browser-verification OpenSpec contract while keeping all browser automation development/CI-only.

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