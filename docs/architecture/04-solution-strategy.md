# 4. Solution strategy

## Browser-native baseline

The design system is delivered as static browser assets. `src/tokens.css` owns exact design constants, `src/tui.css` implements reusable visual component classes, and `src/tui.js` adds only behavior that cannot be expressed by semantic HTML/CSS alone.

This keeps the library usable by plain HTML applications and by applications that use React, Vue, server-rendered templates, or other frameworks, provided they preserve the relevant markup and class contracts.

## Progressive enhancement

Native HTML controls provide their normal semantics and keyboard behavior. JavaScript is intentionally small and additive; the current enhancement dispatches a custom Escape event for opted-in windows rather than owning application navigation or close logic.

## Responsive strategy

The same visual language is retained across desktop and narrow touch screens. Responsive CSS changes spacing, wrapping, control hit areas, and table overflow rather than replacing the interface with a separate mobile design system.

## Visual strategy

The implementation centralizes palette, typography, spacing, borders, and control sizing in tokens. Component CSS composes those tokens into hard-edged raised and recessed surfaces. Exact values belong to the token file rather than architecture prose.

## Verification strategy

Repository tests enforce inexpensive structural contracts. `demo/index.html` provides executable visual coverage. Broader browser, accessibility, and screenshot regression automation is a known future improvement rather than current evidence.
