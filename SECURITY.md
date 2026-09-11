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

Tagged releases publish a focused ZIP plus a SHA-256 checksum. Consumers that download the focused archive should verify the checksum before vendoring it. Git tags are treated as immutable; a security fix is published as a new version rather than by moving an existing tag.

The focused archive includes `docs/project/public-contract.md`, which identifies the intentionally supported browser-native surface. Starting with 1.0, security fixes that require an incompatible public-contract change must be documented and versioned as a new MAJOR release under the public compatibility policy. Urgent security/legal/standards cases may use the documented exception to normal deprecation lead time, but the break and migration impact must remain explicit.

## Supported versions

After `v1.0.0` is published, the maintained release line is the latest 1.x release plus active development on `main`. Security fixes are expected to target that maintained stable line and current development rather than older pre-1.0 tags.

`v0.9.0` and older pre-1.0 tags remain available for auditability but are not long-term support branches. Additional parallel/LTS support lines are not promised; introduce them only if a concrete downstream support need justifies that maintenance cost.
