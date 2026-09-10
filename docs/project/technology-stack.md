# Technology stack

## Runtime

`web-tui-kit` uses browser-native technologies:

- HTML for semantic structure in consuming applications and the demo,
- CSS custom properties and CSS layout for tokens and presentation,
- plain JavaScript for small progressive enhancements.

There is no required JavaScript framework, package manager, bundler, backend runtime, or network service in the library runtime.

## Repository tooling

- Python standard library for structural tests, validation scripts, and deterministic release ZIP/checksum generation,
- MkDocs for human-readable documentation builds,
- Python Playwright plus its pinned Chromium build for visual regression,
- Pillow for screenshot comparison/diff generation,
- GitHub Actions for CI and tag-triggered release verification/publication,
- GitHub CLI in the tag workflow for creating the GitHub prerelease after all gates pass.

Exact structural/documentation CI configuration is canonical in `.github/workflows/ai-doc-1.yml`. Visual CI is canonical in `.github/workflows/visual-regression.yml`; tag publication is canonical in `.github/workflows/release.yml`. Dependency constraints are canonical in `requirements-docs.txt` and `requirements-visual.txt`.

None of the repository tooling above is required by applications consuming `src/`.

## Browser target

The behavioral compatibility requirement is canonical in `openspec/specs/web-tui-kit/spec.md`; implementation should prefer standards-based browser features so consuming applications are not tied to a framework-specific runtime. Exercised compatibility evidence is recorded separately in `docs/project/compatibility.md`.
