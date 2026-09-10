# Technology stack

## Runtime

`web-tui-kit` uses browser-native technologies:

- HTML for semantic structure in consuming applications and the demo,
- CSS custom properties and CSS layout for tokens and presentation,
- plain JavaScript for small progressive enhancements.

There is no required JavaScript framework, package manager, bundler, backend runtime, or network service in the library runtime.

## Repository tooling

- Python standard library for project tests and validation scripts,
- MkDocs for human-readable documentation builds,
- GitHub Actions for CI.

Exact CI runtime configuration is canonical in `.github/workflows/ai-doc-1.yml`. Documentation dependency constraints are canonical in `requirements-docs.txt`.

## Browser target

The behavioral compatibility requirement is canonical in `openspec/specs/web-tui-kit/spec.md`; implementation should prefer standards-based browser features so consuming applications are not tied to a framework-specific runtime.
