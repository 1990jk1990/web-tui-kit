(() => {
  "use strict";

  const listNavigationKeys = new Set(["ArrowUp", "ArrowDown", "Home", "End"]);
  const listItemSelector = [
    'input[type="checkbox"]:not(:disabled):not([aria-disabled="true"])',
    'button:not(:disabled):not([aria-disabled="true"])',
    'a[href]:not([aria-disabled="true"])',
    '[data-tui-list-item][tabindex]:not([tabindex="-1"]):not([aria-disabled="true"]):not([disabled])'
  ].join(", ");

  const getEnabledListItems = (list) => Array.from(
    list.querySelectorAll(listItemSelector)
  ).filter((element) => (
    !element.hidden
    && !element.closest("[inert]")
    && element.getAttribute("aria-hidden") !== "true"
    && element.getClientRects().length > 0
  ));

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      const selector = ".tui-window[data-tui-escape-close], .tui-dialog[data-tui-escape-close]";
      const activeSurface = document.activeElement?.closest?.(selector)
        ?? document.querySelector(selector);

      if (activeSurface) {
        activeSurface.dispatchEvent(new CustomEvent("tui:escape", {
          bubbles: true,
          detail: { sourceEvent: event }
        }));
      }
      return;
    }

    if (!listNavigationKeys.has(event.key) || event.altKey || event.ctrlKey || event.metaKey) {
      return;
    }

    const activeElement = document.activeElement;
    const list = activeElement?.closest?.("[data-tui-list]");
    if (!list) return;

    const items = getEnabledListItems(list);
    const currentIndex = items.indexOf(activeElement);

    // Radio groups and text-entry controls intentionally fall through to
    // their native browser keyboard behavior because they are not list items.
    if (currentIndex < 0 || items.length < 2) return;

    let nextIndex = currentIndex;

    if (event.key === "Home") nextIndex = 0;
    if (event.key === "End") nextIndex = items.length - 1;
    if (event.key === "ArrowUp") nextIndex = (currentIndex - 1 + items.length) % items.length;
    if (event.key === "ArrowDown") nextIndex = (currentIndex + 1) % items.length;

    event.preventDefault();
    items[nextIndex].focus();
  });
})();
