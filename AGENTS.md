# AGENTS.md

This project follows **AI-DOC-1 v1.3**.

Standard source: `https://github.com/1990jk1990/AI-DOC-1`

This repository is also the canonical UI reference for applications that use **web-tui-kit**.

## Role

Act as the project's knowledge steward. The human user is not required to know where project information belongs.

You must:

- determine and maintain the correct canonical artifact automatically,
- inspect repository evidence before asking questions,
- ask only for material user-owned information that cannot be safely inferred,
- reconcile affected requirements, architecture, decisions, developer docs, tests, implementation, and release identity before completion,
- never preserve project knowledge only in chat history.

Do not ask the human whether to use OpenSpec, arc42, an ADR, or another documentation mechanism.

## Mandatory onboarding

Before non-trivial changes:

1. Read `ai-doc-1.yaml`.
2. Read `README.md` and `CONTRIBUTING.md`.
3. Read the relevant current specification under `openspec/specs/`.
4. Read relevant architecture and ADRs under `docs/`.
5. For UI work, read `DESIGN_SYSTEM.md`, `src/tokens.css`, `src/tui.css`, and `demo/index.html`.
6. For framework/template integration work, read `docs/project/framework-integration.md`, `examples/README.md`, the relevant recipe under `examples/`, ADR-0001, and ADR-0004.
7. For browser verification/compatibility work, read `docs/project/testing.md`, `docs/project/compatibility.md`, `openspec/specs/browser-verification/spec.md`, ADR-0002, and ADR-0005.
8. For accessibility-semantic verification work, read `docs/project/testing.md`, `docs/project/compatibility.md`, `openspec/specs/accessibility-verification/spec.md`, ADR-0006, and the canonical demo markup being asserted.
9. For release/version/distribution work, read `VERSION`, `RELEASING.md`, the release/distribution specification, and relevant release ADRs.
10. Inspect relevant tests, visual baselines when UI output may change, and GitHub work state.

## Canonical sources

- Expected behavior → `openspec/specs/`.
- Active non-trivial behavioral changes → `openspec/changes/`.
- Current architecture → `docs/architecture/`.
- Important rationale → `docs/decisions/`.
- Exact design-token values → `src/tokens.css`.
- Implementation → `src/`.
- Executable structural behavior evidence → `tests/test_repository.py`.
- Framework/template integration evidence → `tests/test_framework_recipes.py`.
- Browser interaction verification infrastructure evidence → `tests/test_interaction_regression.py`.
- Browser interaction fixture → `tests/browser/interaction.html`.
- Browser interaction runner → `scripts/interaction_regression.py`.
- Accessibility semantic verification infrastructure evidence → `tests/test_accessibility_regression.py`.
- Accessibility semantic runner → `scripts/accessibility_regression.py`.
- Canonical semantic demo evidence → `demo/index.html` and `demo/dialogs.html`.
- Release/version/archive evidence → `tests/test_release.py`.
- Reviewed visual regression baselines → `tests/visual/baselines/`.
- Primary visual reference → `demo/index.html`.
- Broader component examples → `demo/components.html` and `demo/dialogs.html`.
- Framework/template consumption recipes → `examples/`.
- Framework integration guidance → `docs/project/framework-integration.md`.
- Compatibility evidence → `docs/project/compatibility.md`.
- Physical Android evidence procedure/results → `docs/project/android-device-check.md`.
- Open work → GitHub Issues/Projects.
- Plain release version → `VERSION`.
- Published release identity → immutable Git tags/GitHub Releases.
- Maintainer release procedure → `RELEASING.md`.
- Secrets → external secret store; never this repository.

`DESIGN_SYSTEM.md` is a practical consumption guide. It may summarize canonical behavior but must point to OpenSpec and implementation rather than becoming a conflicting source of truth.

## Project-specific UI rules

Follow the current OpenSpec specification first. In particular, preserve these established design constraints unless the specification is deliberately changed:

- no rounded corners, gradients, blur, glass effects, soft shadows, or modern card-style visual language,
- monospace typography for core application chrome,
- hard light/dark borders for raised and recessed surfaces,
- canonical blue desktop background, grey surfaces, red title/help accents, and blue selections,
- package-style dialogs use the canonical composition shown in `demo/index.html`,
- native semantic HTML wherever practical,
- keyboard reachability for interactive controls,
- touch usability on Android without replacing the visual language with a separate mobile design,
- no hover-only operation,
- horizontal scrolling for tables that do not fit narrow viewports rather than silently dropping important columns.

Keep the baseline framework-independent. A consuming application may use a framework, but this library must not require one unless a future accepted decision changes that constraint.

## Framework/template integration rules

- Treat React, Vue, server-rendered templates, and other frameworks as consumers of the canonical browser-native contract, not as alternate design-system runtimes.
- Reuse canonical `tui-*` classes, native semantic controls, CSS custom properties, and `tui:escape`/`data-tui-list` behavior instead of copying CSS into framework-specific style systems.
- Framework state may control native input values/checked state, but do not replace semantic inputs/buttons with generic clickable containers merely for state management.
- `tui:escape` remains an application signal; framework code decides whether to close, cancel, navigate, or do nothing.
- Do not add competing ArrowUp/ArrowDown/Home/End handlers to a `data-tui-list` that already uses canonical `src/tui.js` enhancement unless intentionally replacing the contract.
- Keep framework dependencies out of `src/` and repository runtime requirements.
- Prefer copy-ready recipes over maintained adapter packages until a concrete capability gap justifies a new architectural decision.

## Browser verification rules

- Keep Linux Chromium as the canonical screenshot-baseline environment unless an accepted decision deliberately changes it.
- Use browser-driven interaction verification for externally relevant JavaScript keyboard/custom-event behavior; do not treat source-text assertions as equivalent end-to-end evidence.
- Exercise the desktop interaction contract in pinned Chromium and Firefox and keep the narrow touch-capable Chromium case representative rather than calling it physical Android certification.
- Keep `tests/browser/interaction.html` a test fixture over canonical `src/` assets; do not duplicate reusable CSS or runtime logic there.
- Browser verification dependencies remain development/CI-only and must not enter `src/` or the downstream runtime contract.
- Never record a physical Android result unless exact device, OS/browser version, date, and observed results come from an actual device run.

## Accessibility semantic verification rules

- Prefer native HTML semantics. Do not introduce ARIA roles/states solely to satisfy a test when an equivalent native element already provides the semantics.
- Treat `.tui-dialog` as presentation-only unless the application deliberately supplies native `<dialog>` or equivalent application-level semantics; do not infer modal semantics from a CSS class name.
- Use browser role/name/native-state queries against canonical demos for semantic evidence. Source-text assertions may protect structure but are not equivalent browser evidence.
- Presentation-only visual annotations embedded in labels/controls must not accidentally pollute accessible names. If a helper becomes operation-critical, expose it deliberately as a description rather than relying on accidental text concatenation.
- Exercise the semantic contract in pinned Chromium and Firefox plus the representative narrow touch-capable Chromium case while keeping Linux Chromium as the sole pixel-baseline authority.
- Browser-computed semantics are evidence, not proof of WCAG conformance, screen-reader output, assistive-technology interoperability, or physical Android accessibility-service behavior.
- Accessibility verification tooling remains development/CI-only and must not enter `src/` or downstream runtime requirements.

## Adding or changing reusable components

For non-trivial component behavior changes:

1. update or create the relevant OpenSpec change/specification,
2. implement from existing tokens before adding one-off values,
3. update `demo/index.html` when the canonical composition changes and the broader demo pages when reusable component coverage changes,
4. add or update structural tests,
5. run the visual-regression suite when canonical UI output can change and explicitly review any baseline update,
6. run the browser-interaction suite when keyboard/custom-event/list-navigation behavior can change,
7. run the accessibility semantic suite when roles, names, labels, state, progress semantics, or canonical control markup can change,
8. update architecture or an ADR only when the change affects current structure or durable rationale,
9. reconcile `DESIGN_SYSTEM.md` if its practical usage guidance is affected.

Normal CI visual verification is read-only. Do not make CI automatically accept new screenshots. For an intentional visual change, use the documented `python scripts/visual_regression.py --update` workflow and review the PNG changes together with the implementation. The Linux GitHub Actions Chromium environment is the canonical baseline-rendering environment.

## Release and distribution rules

- Use the Semantic Version in `VERSION`; release tags are the same value with a `v` prefix.
- Treat published tags as immutable. Fix forward with a new version rather than moving an existing release tag.
- Keep direct vendoring from an immutable tag as the primary pre-1.0 distribution path unless an accepted follow-up decision changes that model.
- Do not introduce npm/package-registry publication without a concrete consumer need and deliberate architecture/specification update.
- Run `python scripts/build_release.py --version "v$(cat VERSION)" --check` for release preparation.
- Tag-triggered publication must verify tag/version identity, main-branch ancestry, structural/documentation checks, visual regression, cross-browser interaction regression, accessibility semantic regression, and deterministic release artifacts before creating a GitHub Release.
- Compatibility statements must reflect actual evidence. Mobile Chromium emulation is not physical Android device certification, and browser semantic automation is not screen-reader/WCAG certification.

## Change classes

- Class 0 — trivial/internal: usually implementation/tests only.
- Class 1 — behavioral: OpenSpec + implementation/tests.
- Class 2 — architectural: relevant Class 1 artifacts + arc42 documentation + ADR when rationale is durable.
- Class 3 — operational/security/data/breaking: relevant lower-class artifacts + explicit safety, migration, deployment, or rollback material.

## Human interaction and safety

Ask only when intended behavior or scope remains materially ambiguous, a genuine user preference must choose among valid alternatives, security intent is unknown, destructive action needs authorization, or conflicting project rules cannot be resolved from repository evidence.

Never commit secrets or real production data. Explain destructive/high-impact actions and recovery implications before execution.

## Completion check

A UI change is complete only when affected canonical documentation is reconciled, structural tests pass, applicable visual baselines pass or are deliberately reviewed/updated, applicable browser-interaction checks pass, applicable accessibility semantic checks pass, the result is visually consistent, keyboard and touch use remain viable, narrow-screen behavior remains intentional, and reusable patterns are represented in the appropriate demo pages.

A framework/template integration change is complete only when recipes reuse canonical runtime contracts, no parallel styling/runtime dependency is introduced, relevant OpenSpec/architecture/ADR/docs are reconciled, and structural tests prove the integration boundary.

A browser-verification/compatibility change is complete only when the fixture/runner/workflows and structural safeguards agree, browser evidence is accurately documented, physical-device claims are not inferred from emulation, and existing visual/structural/docs checks remain green.

An accessibility-semantic verification change is complete only when canonical demo semantics, runner/workflow/release gate, structural safeguards, OpenSpec/architecture/ADR/docs, and evidence boundaries agree; browser semantic evidence must not be overstated as assistive-technology or WCAG certification.

A release-preparation change is complete only when version identity, changelog, release specification/architecture, compatibility evidence, deterministic artifact checks, and tag workflow safeguards are reconciled and PR CI is green. Publication is complete only after the immutable tag and matching GitHub Release artifacts have been verified.
