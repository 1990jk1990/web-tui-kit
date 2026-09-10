# ADR-0003: Tagged vendoring and GitHub release archives as the baseline distribution model

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `openspec/changes/release-distribution/`
- Related issue: #3
- Supersedes: none
- Superseded by: none

## Context

`web-tui-kit` is deliberately usable as static browser assets without a JavaScript framework, package manager, bundler, or runtime build step. The first release needs an immutable version reference and a convenient way to copy the runtime into unrelated applications, including projects driven by coding assistants.

Publishing to npm or another package registry would add release credentials, registry metadata, package-manager expectations, and a second distribution identity before there is evidence that those costs improve the main consumption path.

## Decision

Use immutable Git tags and GitHub Releases as the canonical distribution identity for pre-1.0 releases.

The primary consumption path is direct vendoring from a specific tag. Consumers copy the versioned runtime files under `src/` and may also use the tagged demos and design-system guidance as implementation references.

Each release publishes a deterministic `web-tui-kit-MAJOR.MINOR.PATCH.zip` containing the runtime, demos, version marker, changelog, security guidance, and practical design-system/AI-agent references. A matching SHA-256 checksum file is published beside the ZIP.

Do not publish an npm package for `v0.4.0`. Revisit registry distribution only when a concrete consumer need justifies package-manager installation, dependency metadata, or automated upgrade tooling.

## Considered alternatives

- Publish npm immediately and make it the primary installation path.
- Publish both npm and GitHub archives from the first release.
- Distribute only by copying files from the moving `main` branch.
- Publish only GitHub's automatic source archive without a focused runtime distribution ZIP.

## Consequences

### Positive

- The distribution model matches the framework-independent runtime architecture.
- A tag gives humans and coding agents an immutable visual/behavioral reference.
- Consumers can vendor only the files they need without adding Node.js or a package manager.
- The focused ZIP and checksum provide a simple auditable artifact.
- Release credentials remain limited to the repository's GitHub Actions token.

### Negative / trade-offs

- Consumers do not get automatic dependency updates or package-manager lockfile integration.
- Vendored copies must record which tag they came from and update deliberately.
- A future npm package would add another supported distribution surface and require an explicit follow-up decision.

## Evidence / notes

The current project consists of static CSS/JavaScript assets and executable HTML references. No existing runtime feature requires package-manager resolution. The release build and tag workflow therefore remain development tooling rather than runtime dependencies.
