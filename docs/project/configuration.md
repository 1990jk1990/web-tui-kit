# Configuration

`web-tui-kit` currently requires no environment variables, credentials, backend configuration, or runtime configuration files.

## Design tokens

Exact theme and sizing values are CSS custom properties in `src/tokens.css`. Consuming applications may override tokens deliberately, but the repository defaults remain the canonical baseline implementation.

## Runtime behavior

`src/tui.js` uses DOM conventions rather than external configuration. In particular, a window opts into Escape-event dispatch with the `data-tui-escape-close` attribute.

## Secrets

No secret belongs in this repository. Consuming applications must manage their own credentials through an appropriate external secret mechanism.
