# Technology stack

## Runtime

`web-tui-kit` uses browser-native technologies:

- HTML for semantic structure in consuming applications and the demo,
- CSS custom properties and CSS layout for tokens and presentation,
- plain JavaScript for small progressive enhancements.

There is no required JavaScript framework, package manager, bundler, backend runtime, network service, browser-test library, or accessibility-test runtime in the library runtime.

## Framework/template recipes

`examples/react/` and `examples/vue/` contain source recipes for applications that already use those frameworks. `examples/server-rendered/` demonstrates template-oriented/server-rendered HTML. These examples do not make React, Vue, Node.js, npm, or a template engine repository/runtime dependencies.

The canonical integration contract remains semantic browser markup plus `src/tokens.css`, `src/tui.css`, and optional `src/tui.js`.

## Repository tooling

- Python standard library for structural tests, validation scripts, and deterministic release ZIP/checksum generation,
- MkDocs for human-readable documentation builds,
- Python Playwright plus its pinned Chromium build for canonical visual regression,
- the same pinned Playwright release with Chromium and Firefox browser builds for browser-driven interaction and browser accessibility-semantic verification,
- Pillow for screenshot comparison/diff generation,
- GitHub Actions for structural/docs, visual, browser-interaction, accessibility-semantic, and tag-triggered release verification/publication,
- GitHub CLI in the tag workflow for creating the GitHub prerelease after all gates pass.

Exact structural/documentation CI configuration is canonical in `.github/workflows/ai-doc-1.yml`. Visual CI is canonical in `.github/workflows/visual-regression.yml`; browser interaction CI is canonical in `.github/workflows/interaction-regression.yml`; accessibility semantic CI is canonical in `.github/workflows/accessibility-regression.yml`; tag publication is canonical in `.github/workflows/release.yml`. Dependency constraints are canonical in `requirements-docs.txt` and `requirements-visual.txt`.

The accessibility semantic suite uses browser role/name/native-state queries against canonical demos. No separate Node/axe package-manager stack is introduced at this stage, and passing browser semantic checks is not treated as real screen-reader/assistive-technology or WCAG-conformance certification.

None of the repository tooling above is required by applications consuming `src/`.

## Browser target

The behavioral compatibility requirement is canonical in `openspec/specs/web-tui-kit/spec.md`; implementation should prefer standards-based browser features so consuming applications are not tied to a framework-specific runtime. Exercised compatibility evidence is recorded separately in `docs/project/compatibility.md`.
