(() => {
  "use strict";

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;

    const activeWindow = document.activeElement?.closest?.(".tui-window[data-tui-escape-close]")
      ?? document.querySelector(".tui-window[data-tui-escape-close]");

    if (!activeWindow) return;

    activeWindow.dispatchEvent(new CustomEvent("tui:escape", {
      bubbles: true,
      detail: { sourceEvent: event }
    }));
  });
})();
