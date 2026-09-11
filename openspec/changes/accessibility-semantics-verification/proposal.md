# Accessibility semantics verification

Status: Active
Related issue: #20
Change class: Class 2 — verification architecture / accessibility evidence

## Motivation

`web-tui-kit` v0.6.0 has structural tests, canonical Chromium screenshot regression, and browser-driven Chromium/Firefox interaction evidence. The remaining verification gap documented by the project is automated evidence for the browser-exposed accessibility semantics of the canonical UI patterns.

The next milestone should verify roles, accessible names, native state, label associations, and progress semantics in real browser engines without replacing native HTML with ARIA-heavy replicas and without presenting browser automation as screen-reader certification or proof of WCAG conformance.

## Proposed behavior

- Add browser-driven accessibility-semantic verification for the canonical package-configuration and dialog demo pages.
- Verify named regions/surfaces, group and radiogroup names, native control names, checked/disabled state, text-input label association, action-button names, and native progressbar semantics.
- Keep `.tui-dialog` presentation-only: canonical `<section>` examples are expected to expose their existing named-region semantics and MUST NOT be reclassified as modal dialogs merely for the test suite.
- Exclude purely visual helper annotations such as repeated `<Help>` hints from control accessible names when they do not convey operation-critical meaning.
- Run the desktop semantic contract in the Playwright-pinned Chromium and Firefox engines and add a narrow touch-capable Chromium semantic case.
- Reuse the existing pinned Python Playwright dependency and canonical demo/runtime assets; add no runtime or framework dependency.
- Add a read-only accessibility-semantics CI matrix and retain a screenshot artifact only on failure for diagnosis.
- If the suite proves stable, make future tag-triggered releases run it before deterministic artifact creation/publication.
- Reconcile OpenSpec, architecture/ADR material, compatibility/testing guidance, contributor/agent rules, structural safeguards, and changelog.

## Evidence boundary

The automated suite proves only the browser-computed semantic contract exercised by the pinned browser builds. It does not by itself establish WCAG conformance, screen-reader behavior, assistive-technology interoperability, physical Android accessibility-service behavior, or usability by every disability/access method.

Manual assistive-technology and physical-device evidence remains separate and must be recorded only when actually performed.

## Boundaries

This change does not redesign the UI, introduce a new runtime component model, add a framework adapter, add npm/package-registry publication, replace native controls with generic ARIA widgets, create Firefox screenshot baselines, or claim physical-device/assistive-technology certification.

No screenshot baseline is intentionally changed. Semantic markup may be refined where canonical demo helper text currently pollutes an otherwise clear control name, provided the visible output remains unchanged and visual regression confirms that.

## Acceptance criteria

- A deterministic browser semantic runner exists and fails when canonical roles/names/native states regress.
- Chromium and Firefox desktop verify the canonical package/dialog semantic contract.
- A narrow touch-capable Chromium case proves the core semantic contract remains exposed in the representative mobile/touch context.
- Canonical visual helper annotations do not accidentally become part of native control accessible names where they are presentation-only.
- CI runs the semantic suite read-only on pull requests and `main`, with development-only dependencies.
- Structural tests protect the runner/workflow/release-gate contract.
- Compatibility/testing documentation distinguishes browser semantic evidence from screen-reader, WCAG, and physical-device claims.
- Architecture and durable rationale are reconciled without changing runtime dependency direction.
- Existing structural, documentation, visual, interaction, and deterministic release checks remain green.
