# web-tui-kit documentation

This is the human-readable documentation entry point for `web-tui-kit`.

## Start here

- [Project overview](project/overview.md)
- [Getting started](project/getting-started.md)
- [Development](project/development.md)
- [Technology stack](project/technology-stack.md)
- [Testing](project/testing.md)
- [Compatibility evidence](project/compatibility.md)
- [Configuration](project/configuration.md)
- [Architecture introduction and goals](architecture/01-introduction-and-goals.md)
- [Solution strategy](architecture/04-solution-strategy.md)
- [Building-block view](architecture/05-building-block-view.md)
- [Architecture decisions](architecture/09-architecture-decisions.md)

Repository-root `RELEASING.md` defines versioning, release preparation, tagging, and GitHub Release publication.

## Requirements

OpenSpec under `openspec/` is canonical for accepted behavior and non-trivial behavioral changes. During the documentation build, current Markdown specs are mirrored into `docs/generated/requirements/` for browsing. Generated pages are not canonical and must not be edited manually.

## Design-system reference

`DESIGN_SYSTEM.md` is the practical consumption guide. Exact CSS values are owned by `src/tokens.css`, while reusable implementation is owned by `src/`.

## Release identity

`VERSION` contains the canonical plain Semantic Version. Immutable `vMAJOR.MINOR.PATCH` Git tags and matching GitHub Releases identify published pre-1.0 versions. Direct vendoring from a release tag is the primary distribution model.

## AI-DOC-1

The repository follows AI-DOC-1 v1.3. `ai-doc-1.yaml` records the adopted version and canonical source mapping; `AGENTS.md` contains working rules for AI coding agents.
