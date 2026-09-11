# 4. Solution strategy

## Browser-native baseline

The design system is delivered as static browser assets. `src/tokens.css` owns exact design constants, `src/tui.css` implements reusable visual component classes, and `src/tui.js` adds only behavior that cannot be expressed by semantic HTML/CSS alone.

This keeps the library usable by plain HTML applications and by applications that use React, Vue, server-rendered templates, or other frameworks, provided they preserve the relevant markup and class contracts.

## Public contract strategy

The browser-native runtime is also the stability boundary. `openspec/specs/public-contract/spec.md` defines compatibility behavior and `docs/project/public-contract.md` inventories the supported consumer surface: canonical `--tui-*` custom-property names and purposes, reusable `tui-*` classes, scoped state hooks, required semantic markup relationships, and the documented `data-tui-*` / `tui:escape` progressive JavaScript contract.

Visible repository details are not automatically APIs. Demo IDs/text/order, test fixtures, verification scripts, generated output, CI implementation, pinned evidence-tool versions, CSS declaration/selector ordering, pseudo-element technique, and JavaScript helper/local names remain non-public unless an accepted requirement explicitly promotes one.

Structural tests compare the implemented token/class surface with the declared inventory so a public name cannot silently disappear and a new `tui-*` token/class cannot accidentally become unclassified public surface. ADR-0008 records this boundary and the pre/post-1.0 compatibility policy.

Before 1.0, an intentional incompatible public-contract change is a MINOR release with explicit migration guidance. Starting with 1.0, normal Semantic Versioning applies to the declared public contract; compatible additions/deprecations may occur in MINOR releases, while incompatible removal/rename/semantic contract breaks require a MAJOR release.

## Framework integration strategy

Frameworks are consumers of the browser-native contract, not alternate design-system runtimes. `examples/react/`, `examples/vue/`, and `examples/server-rendered/` provide copy-ready integration recipes that demonstrate framework-owned state/lifecycle behavior while reusing canonical classes, native controls, CSS assets, and custom events.

No maintained framework adapter layer is introduced while semantic markup, canonical CSS classes/custom properties, and the existing progressive JavaScript contract are sufficient. This avoids duplicated styling/API surfaces and framework-version maintenance in the core repository. A future adapter requires a concrete capability gap and a deliberate follow-up architecture/specification decision. ADR-0004 records the rationale.

Representative executable verification strengthens this strategy without changing the runtime boundary. A private toolchain under `tests/framework/` compiles the canonical React and Vue recipe files and runs them, plus the server-rendered recipe, in pinned Chromium against canonical `src/` assets. These Node/framework/compiler dependencies are verification-only and never become requirements of `src/` or downstream applications. ADR-0007 records this verification boundary.

## Progressive enhancement

Native HTML controls provide their normal semantics and keyboard behavior. JavaScript is intentionally small and additive; the current enhancements dispatch a custom Escape event for opted-in windows/dialogs and provide narrowly scoped optional list focus navigation without replacing native activation or selection behavior.

The public progressive behavior is exposed through `data-tui-escape-close`, `data-tui-list`, `data-tui-list-item`, and the bubbling `tui:escape` event. Implementation-local functions/selectors are deliberately outside the public API.

## Responsive strategy

The same visual language is retained across desktop and narrow touch screens. Responsive CSS changes spacing, wrapping, control hit areas, checklist help placement, and table overflow rather than replacing the interface with a separate mobile design system.

## Visual strategy

The implementation centralizes palette, typography, spacing, borders, scrollbar sizing, and control sizing in tokens. Component CSS composes those tokens into hard-edged raised and recessed surfaces.

The primary visual composition is the package-style dialog: a centered grey beveled surface over the blue desktop, with an overlapping red title, recessed selection area, blue row focus, text-style checkbox markers, short red help accents, and angle-bracket actions. `demo/index.html` is the canonical executable reference for that composition; `demo/components.html` provides wider component coverage and `demo/dialogs.html` provides the common dialog compositions.

Exact values belong to the token file rather than architecture prose. Public token compatibility protects the custom-property name and semantic purpose, not an immutable literal value. `.tui-help` consumes the dedicated `--tui-help` token so normal and forced-colors implementations agree with that semantic purpose.

## Verification strategy

Fast Python unit tests enforce repository contracts such as required tokens, selectors, canonical demo structure, small JavaScript behavior invariants, the declared public token/class/data-attribute/event inventory, framework-recipe reuse/boundaries, executable framework-verification infrastructure, browser/accessibility-verification infrastructure, version/release archive rules, and release-workflow safeguards. AI-DOC-1 validation and a strict MkDocs build verify repository/documentation structure.

`tests/test_public_contract.py` is the inexpensive executable guard for the stability boundary. It fails if canonical `--tui-*` tokens or `tui-*` component classes drift from the declared inventory, protects scoped state hooks and progressive JavaScript names, checks the help-token mapping, and confirms the public-contract guide remains a focused-release input.

Visual output is verified separately with a pinned Python Playwright release and its matching Chromium build. `scripts/visual_regression.py` serves the repository locally, renders fixed desktop and touch-capable narrow/mobile cases for `demo/index.html` and `demo/dialogs.html`, and compares those renders with reviewed PNG baselines under `tests/visual/baselines/`. The Linux GitHub Actions environment is the canonical screenshot environment. Failed comparisons retain actual/diff images as workflow artifacts.

Behavioral browser verification uses the same pinned Playwright dependency but a separate purpose-built fixture and runner. `scripts/interaction_regression.py` executes the canonical runtime in Chromium and Firefox desktop contexts to prove `tui:escape`, optional `data-tui-list` focus navigation/disabled-item skipping, native radio behavior, and text-entry arrow-key preservation. A narrow touch-capable Chromium case additionally verifies coarse-pointer/touch context and native tap operation. `.github/workflows/interaction-regression.yml` runs these checks on pull requests and `main`.

Accessibility-semantic browser verification also reuses the pinned Playwright toolchain but runs directly against the canonical package and dialog demos. `scripts/accessibility_regression.py` checks browser-computed roles, accessible names, native checked/disabled state, label associations, named groups/regions, and native progress semantics in Chromium and Firefox desktop contexts plus a narrow touch-capable Chromium package case. Presentation-only `.tui-dialog` styling is deliberately not treated as modal semantics, and presentation-only helper hints are excluded from control names. `.github/workflows/accessibility-regression.yml` owns the read-only CI matrix. ADR-0006 records the rationale and evidence boundary.

Framework/template recipe verification is a separate consumer-integration smoke boundary. `tests/framework/build-fixtures.mjs` compiles the canonical React JSX and Vue SFC source recipes with exact representative direct development versions, while `scripts/framework_recipe_regression.py` renders those generated fixtures and the canonical server-rendered example in Linux Chromium. It verifies native checkbox state, list focus enhancement, Escape-to-application handling, and accept/form payload behavior. `.github/workflows/framework-recipe-regression.yml` is read-only. This evidence is representative rather than an exhaustive framework-version matrix.

Chromium/Linux remains the only canonical pixel-baseline authority. Firefox is behavioral and semantic compatibility evidence rather than a second screenshot baseline. Touch-capable Chromium emulation is representative browser evidence and is not treated as physical Android, WebView, software-keyboard, accessibility-service, or assistive-technology certification. ADR-0005 records the separation and cross-browser interaction strategy.

Visual, interaction, accessibility-semantic, and framework-recipe verification dependencies remain development/CI-only and do not enter the browser runtime contract. Intentional visual changes update baselines explicitly; normal CI never rewrites them automatically. ADR-0002 records the visual-regression tooling rationale.

The automated suites complement rather than replace accessibility review, WCAG evaluation, screen-reader/assistive-technology testing, physical-device checks, and consumer-specific framework/version verification. Passing a pinned representative framework recipe case means the checked-in recipe interoperates with that exact verification toolchain; it is not a broad framework support declaration.

## 1.0 readiness strategy

Version 1.0 is a deliberate compatibility commitment, not an automatic successor to 0.9. The public contract must be accepted, structurally protected, and free of selected pre-1.0 cleanup debt; all existing release gates must pass on the candidate; release/consumer documentation must consistently state the stability commitment; and the focused archive must carry the public-contract guide.

The current evidence gaps remain accurately described rather than being converted into unsupported certification claims. Physical Android certification, real assistive-technology/screen-reader certification, WCAG certification, npm publication, maintained framework adapters, and a broad framework-version matrix are not current 1.0 prerequisites unless a future accepted requirement makes one mandatory.

## Release and distribution strategy

`VERSION` owns the plain Semantic Version. Immutable `vMAJOR.MINOR.PATCH` Git tags and GitHub Releases identify published versions. Before 1.0, tagged direct vendoring is the primary consumer path: downstream projects pin a tag and copy the browser assets they need from `src/`.

`scripts/build_release.py` creates a focused deterministic ZIP and SHA-256 checksum from an explicit allowlist of runtime/reference files, including `docs/project/public-contract.md` so downstream users can inspect the supported stability boundary with the packaged runtime. `.github/workflows/release.yml` runs only for matching version tags; it verifies tag/version identity, requires the tag commit to be contained in `main`, runs structural/documentation/visual/interaction/accessibility-semantic/framework-recipe checks, builds the deterministic archive, and only then publishes a GitHub prerelease.

No npm/package-registry publishing is part of the current pre-1.0 baseline. The npm-based framework verification toolchain is development-only and does not change distribution. ADR-0003 records the release rationale; `RELEASING.md` defines the maintainer procedure and `docs/project/compatibility.md` records compatibility evidence separately from compatibility targets.
