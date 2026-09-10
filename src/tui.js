(() => {
  "use strict";

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;

    const selector = ".tui-window[data-tui-escape-close], .tui-dialog[data-tui-escape-close]";
    const activeSurface = document.activeElement?.closest?.(selector)
      ?? document.querySelector(selector);

    if (!activeSurface) return;

    activeSurface.dispatchEvent(new CustomEvent("tui:escape", {
      bubbles: true,
      detail: { sourceEvent: event }
    }));
  });
})();
