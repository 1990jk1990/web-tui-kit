# web-tui-kit

A reusable web UI design system inspired by Debian debconf, `dialog`, and `whiptail`.

The project exists as a **canonical UI reference** for browser-based applications that should look and behave consistently on Linux desktops and Android devices.

## Goals

- reproduce the classic blue/grey dialog-style visual language in the browser
- stay usable with mouse, touch, and keyboard
- avoid framework lock-in
- keep the design system small enough that coding assistants can understand and reuse it quickly
- provide one source of truth for colors, spacing, borders, components, and interaction rules

## Start here

Coding assistants should read these files in this order:

1. `AGENTS.md`
2. `DESIGN_SYSTEM.md`
3. `src/tokens.css`
4. `src/tui.css`
5. `demo/index.html`

## Quick start

Clone the repository and serve it with any static web server:

```bash
git clone https://github.com/1990jk1990/web-tui-kit.git
cd web-tui-kit
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/demo/
```

No build step and no JavaScript framework are required.

## Use in another project

Copy or vendor the files from `src/` and include them in the application:

```html
<link rel="stylesheet" href="/ui/tokens.css">
<link rel="stylesheet" href="/ui/tui.css">
<script src="/ui/tui.js" defer></script>
```

Example markup:

```html
<section class="tui-window" aria-labelledby="settings-title">
  <h1 class="tui-title" id="settings-title">Configuration</h1>
  <p>Select an option:</p>

  <label class="tui-check">
    <input type="checkbox" checked>
    <span>Enable service</span>
  </label>

  <div class="tui-actions">
    <button class="tui-button" type="button">OK</button>
    <button class="tui-button" type="button">Cancel</button>
  </div>
</section>
```

## Prompt for ChatGPT / coding assistants

A practical prompt for another project is:

> Use `https://github.com/1990jk1990/web-tui-kit` as the canonical UI design system. Read `AGENTS.md` and `DESIGN_SYSTEM.md` first. Reuse the existing CSS classes and interaction patterns instead of inventing a new visual language. The application must work in modern Linux desktop browsers and Android browsers.

## Project status

Early development. The first milestone is a stable visual foundation plus common form, dialog, table, navigation, and status components.
