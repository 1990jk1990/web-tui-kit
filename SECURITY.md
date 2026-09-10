# Security

## Current security scope

`web-tui-kit` is currently a static client-side UI library and demo. It has no backend service, authentication system, database, or required secret configuration in this repository.

## Reporting a vulnerability

Report sensitive security findings privately through the repository's GitHub security reporting features when available. Do not place credentials, exploit details that would unnecessarily expose users, or other secrets in a public issue.

## Development rules

- Never commit secrets or real production data.
- Preserve semantic browser controls and safe DOM handling when extending JavaScript.
- Treat content from consuming applications as untrusted unless the application establishes otherwise.
- Security-relevant behavior changes require tests and appropriate AI-DOC-1 Class 3 documentation.

## Supported versions

No stable release has been published yet. Security fixes currently target the active development line. Once releases are published, supported-version policy must be updated here.
