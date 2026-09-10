# Getting started

## Prerequisites

A modern browser is sufficient to use the library. Python 3 is convenient for serving the demo locally and is used by repository validation tooling.

## Run the demo

```bash
git clone https://github.com/1990jk1990/web-tui-kit.git
cd web-tui-kit
python3 -m http.server 8000
```

Open `http://localhost:8000/demo/`.

## Integrate into another application

Vendor or copy the files under `src/`, then load them in this order:

```html
<link rel="stylesheet" href="/ui/tokens.css">
<link rel="stylesheet" href="/ui/tui.css">
<script src="/ui/tui.js" defer></script>
```

The CSS classes and usage patterns are described in `DESIGN_SYSTEM.md`. Accepted behavior is canonical in `openspec/specs/`.

## No build requirement

The current baseline is directly consumable by browsers. A consuming application may have its own build system or framework; `web-tui-kit` itself does not require one for runtime use.
