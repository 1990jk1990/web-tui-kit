# web-tui-kit documentation

This is the human-readable documentation entry point for `web-tui-kit`.

## Start here

- [Project overview](project/overview.md)
- [Getting started](project/getting-started.md)
- [Public consumer contract](project/public-contract.md)
- [Framework integration](project/framework-integration.md)
- [Development](project/development.md)
- [Technology stack](project/technology-stack.md)
- [Testing](project/testing.md)
- [Compatibility evidence](project/compatibility.md)
- [Physical Android device check](project/android-device-check.md)
- [Configuration](project/configuration.md)
- [Architecture introduction and goals](architecture/01-introduction-and-goals.md)
- [Solution strategy](architecture/04-solution-strategy.md)
- [Building-block view](architecture/05-building-block-view.md)
- [Architecture decisions](architecture/09-architecture-decisions.md)

Repository-root `RELEASING.md` defines versioning, release preparation, tagging, compatibility classification, and GitHub Release publication.

## Requirements

OpenSpec under `openspec/` is canonical for accepted behavior and non-trivial behavioral changes. During the documentation build, current Markdown specs are mirrored into `docs/generated/requirements/` for browsing. Generated pages are not canonical and must not be edited manually.

The accepted public-contract specification defines the supported downstream token/class/state/semantic-markup/data-attribute/event boundary and the pre/post-1.0 compatibility rules. `project/public-contract.md` is its practical inventory.

The accepted verification contracts include separate browser-interaction and accessibility-semantic specifications. Browser semantic automation records roles/names/native states exposed by the exercised engines; it must not be interpreted as screen-reader certification or a WCAG conformance statement.

## Design-system reference

`DESIGN_SYSTEM.md` is the practical consumption guide. Exact CSS values are owned by `src/tokens.css`, while reusable implementation is owned by `src/`. Public stability protects declared token/class names and semantic purposes/relationships rather than incidental implementation technique.

Framework/template consumers should also read `project/framework-integration.md` and the matching source recipe under `examples/`. Those recipes consume the canonical runtime; they are not framework-specific replacements for it.

## Compatibility evidence

`project/compatibility.md` records what automated/manual environments have actually been exercised. `project/android-device-check.md` defines the physical Android procedure and must not be marked verified without a real device result. Automated accessibility-semantic checks are browser evidence only; real assistive-technology/device results remain separate evidence.

## Release identity

`VERSION` contains the canonical plain Semantic Version. Immutable `vMAJOR.MINOR.PATCH` Git tags and matching GitHub Releases identify published versions. Direct vendoring from a release tag is the primary pre-1.0 distribution model, and focused archives include the public-contract guide alongside the runtime.

## AI-DOC-1

The repository follows AI-DOC-1 v1.3. `ai-doc-1.yaml` records the adopted version and canonical source mapping; `AGENTS.md` contains working rules for AI coding agents.
