# 4. Solution strategy

## Browser-native baseline

The design system is delivered as static browser assets. `src/tokens.css` owns exact design constants, `src/tui.css` implements reusable visual component classes, and `src/tui.js` adds only behavior that cannot be expressed by semantic HTML/CSS alone.

This keeps the library usable by plain HTML applications and by applications that use React, Vue, server-rendered templates, or other frameworks, provided they preserve the relevant markup and class contracts.

## Progressive enhancement

Native HTML controls provide their normal semantics and keyboard behavior. JavaScript is intentionally small and additive; the current enhancements dispatch a custom Escape event for opted-in windows/dialogs and provide narrowly scoped optional list focus navigation without replacing native activation or selection behavior.

## Responsive strategy

The same visual language is retained across desktop and narrow touch screens. Responsive CSS changes spacing, wrapping, control hit areas, checklist help placement, and table overflow rather than replacing the interface with a separate mobile design system.

## Visual strategy

The implementation centralizes palette, typography, spacing, borders, scrollbar sizing, and control sizing in tokens. Component CSS composes those tokens into hard-edged raised and recessed surfaces.

The primary visual composition is the package-style dialog: a centered grey beveled surface over the blue desktop, with an overlapping red title, recessed selection area, blue row focus, text-style checkbox markers, short red help accents, and angle-bracket actions. `demo/index.html` is the canonical executable reference for that composition; `demo/components.html` provides wider component coverage and `demo/dialogs.html` provides the common dialog compositions.

Exact values belong to the token file rather than architecture prose.

## Verification strategy

Fast Python unit tests enforce repository contracts such as required tokens, selectors, canonical demo structure, small JavaScript behavior invariants, version/release archive rules, and release-workflow safeguards. AI-DOC-1 validation and a strict MkDocs build verify repository/documentation structure.

Visual output is verified separately with a pinned Python Playwright release and its matching Chromium build. `scripts/visual_regression.py` serves the repository locally, renders fixed desktop and touch-capable narrow/mobile cases for `demo/index.html` and `demo/dialogs.html`, and compares those renders with reviewed PNG baselines under `tests/visual/baselines/`. The Linux GitHub Actions environment is the canonical screenshot environment. Failed comparisons retain actual/diff images as workflow artifacts.

Visual verification dependencies remain development/CI-only and do not enter the browser runtime contract. Intentional visual changes update baselines explicitly; normal CI never rewrites them automatically. ADR-0002 records the durable tooling rationale.

The visual suite complements rather than replaces structural tests, accessibility review, browser-driven interaction testing, assistive-technology testing, and manual device checks.

## Release and distribution strategy

`VERSION` owns the plain Semantic Version. Immutable `vMAJOR.MINOR.PATCH` Git tags and GitHub Releases identify published versions. Before 1.0, tagged direct vendoring is the primary consumer path: downstream projects pin a tag and copy the browser assets they need from `src/`.

`scripts/build_release.py` creates a focused deterministic ZIP and SHA-256 checksum from an explicit allowlist of runtime/reference files. `.github/workflows/release.yml` runs only for matching version tags; it verifies tag/version identity, requires the tag commit to be contained in `main`, runs structural/documentation/visual checks, builds the deterministic archive, and only then publishes a GitHub prerelease.

No npm/package-registry publishing is part of v0.4.0. That keeps release infrastructure aligned with the package-manager-free runtime baseline. ADR-0003 records the rationale; `RELEASING.md` defines the maintainer procedure and `docs/project/compatibility.md` records compatibility evidence separately from compatibility targets.
