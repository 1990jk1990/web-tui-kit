# Security

## Current security scope

`web-tui-kit` is a static client-side UI library and demo. It has no backend service, authentication system, database, or required secret configuration in this repository.

## Reporting a vulnerability

Report sensitive security findings privately through the repository's GitHub security reporting features when available. Do not place credentials, exploit details that would unnecessarily expose users, or other secrets in a public issue.

## Development rules

- Never commit secrets or real production data.
- Preserve semantic browser controls and safe DOM handling when extending JavaScript.
- Treat content from consuming applications as untrusted unless the application establishes otherwise.
- Security-relevant behavior changes require tests and appropriate AI-DOC-1 Class 3 documentation.
- Release publication must use the repository's verified tag workflow rather than ad-hoc artifact uploads.

## Release integrity

Tagged pre-1.0 releases publish a focused ZIP plus a SHA-256 checksum. Consumers that download the focused archive should verify the checksum before vendoring it. Git tags are treated as immutable; a security fix is published as a new version rather than by moving an existing tag.

## Supported versions

Until `v0.4.0` is published, security fixes target the active `main` development line. After tagged pre-1.0 releases begin, only the latest published pre-1.0 release and the active development line are expected to receive security fixes. Older pre-1.0 tags are retained for auditability but are not maintained as long-term support branches.

This policy will be revisited when the project reaches `1.0.0` or if a downstream consumer creates a concrete need for longer support windows.
