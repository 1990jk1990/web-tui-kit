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

Tagged pre-1.0 releases are active. Security fixes are expected to target the latest published pre-1.0 release and the active development line. After `v0.8.0` is published, it becomes the maintained pre-1.0 release line; `v0.7.0` and older tags remain available for auditability but are not long-term support branches.

Older pre-1.0 tags are retained for auditability rather than maintained in parallel. This policy will be revisited when the project reaches `1.0.0` or if a downstream consumer creates a concrete need for longer support windows.
