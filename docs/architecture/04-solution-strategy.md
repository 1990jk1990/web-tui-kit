# 4. Solution strategy

## Browser-native baseline

The design system is delivered as static browser assets. `src/tokens.css` owns exact design constants, `src/tui.css` implements reusable visual component classes, and `src/tui.js` adds only behavior that cannot be expressed by semantic HTML/CSS alone.

This keeps the library usable by plain HTML applications and by applications that use React, Vue, server-rendered templates, or other frameworks, provided they preserve the relevant markup and class contracts.

## Framework integration strategy

Frameworks are consumers of the browser-native contract, not alternate design-system runtimes. `examples/react/`, `examples/vue/`, and `examples/server-rendered/` provide copy-ready integration recipes that demonstrate framework-owned state/lifecycle behavior while reusing canonical classes, native controls, CSS assets, and custom events.

No maintained framework adapter layer is introduced while semantic markup, canonical CSS classes/custom properties, and the existing progressive JavaScript contract are sufficient. This avoids duplicated styling/API surfaces and framework-version maintenance in the core repository. A future adapter requires a concrete capability gap and a deliberate follow-up architecture/specification decision. ADR-0004 records the rationale.

## Progressive enhancement

Native HTML controls provide their normal semantics and keyboard behavior. JavaScript is intentionally small and additive; the current enhancements dispatch a custom Escape event for opted-in windows/dialogs and provide narrowly scoped optional list focus navigation without replacing native activation or selection behavior.

## Responsive strategy

The same visual language is retained across desktop and narrow touch screens. Responsive CSS changes spacing, wrapping, control hit areas, checklist help placement, and table overflow rather than replacing the interface with a separate mobile design system.

## Visual strategy

The implementation centralizes palette, typography, spacing, borders, scrollbar sizing, and control sizing in tokens. Component CSS composes those tokens into hard-edged raised and recessed surfaces.

The primary visual composition is the package-style dialog: a centered grey beveled surface over the blue desktop, with an overlapping red title, recessed selection area, blue row focus, text-style checkbox markers, short red help accents, and angle-bracket actions. `demo/index.html` is the canonical executable reference for that composition; `demo/components.html` provides wider component coverage and `demo/dialogs.html` provides the common dialog compositions.

Exact values belong to the token file rather than architecture prose.

## Verification strategy

Fast Python unit tests enforce repository contracts such as required tokens, selectors, canonical demo structure, small JavaScript behavior invariants, framework-recipe reuse/boundaries, browser/accessibility-verification infrastructure, version/release archive rules, and release-workflow safeguards. AI-DOC-1 validation and a strict MkDocs build verify repository/documentation structure.

Visual output is verified separately with a pinned Python Playwright release and its matching Chromium build. `scripts/visual_regression.py` serves the repository locally, renders fixed desktop and touch-capable narrow/mobile cases for `demo/index.html` and `demo/dialogs.html`, and compares those renders with reviewed PNG baselines under `tests/visual/baselines/`. The Linux GitHub Actions environment is the canonical screenshot environment. Failed comparisons retain actual/diff images as workflow artifacts.

Behavioral browser verification uses the same pinned Playwright dependency but a separate purpose-built fixture and runner. `scripts/interaction_regression.py` executes the canonical runtime in Chromium and Firefox desktop contexts to prove `tui:escape`, optional `data-tui-list` focus navigation/disabled-item skipping, native radio behavior, and text-entry arrow-key preservation. A narrow touch-capable Chromium case additionally verifies coarse-pointer/touch context and native tap operation. `.github/workflows/interaction-regression.yml` runs these checks on pull requests and `main`.

Accessibility-semantic browser verification also reuses the pinned Playwright toolchain but runs directly against the canonical package and dialog demos. `scripts/accessibility_regression.py` checks browser-computed roles, accessible names, native checked/disabled state, label associations, named groups/regions, and native progress semantics in Chromium and Firefox desktop contexts plus a narrow touch-capable Chromium package case. Presentation-only `.tui-dialog` styling is deliberately not treated as modal semantics, and presentation-only helper hints are excluded from control names. `.github/workflows/accessibility-regression.yml` owns the read-only CI matrix. ADR-0006 records the rationale and evidence boundary.

Chromium/Linux remains the only canonical pixel-baseline authority. Firefox is behavioral and semantic compatibility evidence rather than a second screenshot baseline. Touch-capable Chromium emulation is representative browser evidence and is not treated as physical Android, WebView, software-keyboard, accessibility-service, or assistive-technology certification. ADR-0005 records the separation and cross-browser interaction strategy.

Visual, interaction, and accessibility-semantic verification dependencies remain development/CI-only and do not enter the browser runtime contract. Intentional visual changes update baselines explicitly; normal CI never rewrites them automatically. ADR-0002 records the visual-regression tooling rationale.

The automated suites complement rather than replace accessibility review, WCAG evaluation, screen-reader/assistive-technology testing, and manual physical-device checks. Passing browser semantic checks means the exercised browser accessibility mappings expose the accepted roles/names/state; it is not a conformance or AT certification claim.

## Release and distribution strategy

`VERSION` owns the plain Semantic Version. Immutable `vMAJOR.MINOR.PATCH` Git tags and GitHub Releases identify published versions. Before 1.0, tagged direct vendoring is the primary consumer path: downstream projects pin a tag and copy the browser assets they need from `src/`.

`scripts/build_release.py` creates a focused deterministic ZIP and SHA-256 checksum from an explicit allowlist of runtime/reference files. `.github/workflows/release.yml` runs only for matching version tags; it verifies tag/version identity, requires the tag commit to be contained in `main`, runs structural/documentation/visual/interaction/accessibility-semantic checks, builds the deterministic archive, and only then publishes a GitHub prerelease.

No npm/package-registry publishing is part of the current pre-1.0 baseline. That keeps release infrastructure aligned with the package-manager-free runtime baseline. ADR-0003 records the rationale; `RELEASING.md` defines the maintainer procedure and `docs/project/compatibility.md` records compatibility evidence separately from compatibility targets.
