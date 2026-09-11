import { useEffect, useRef, useState } from "react";

const DEFAULT_SERVICES = [
  { id: "accounts-daemon.service", enabled: true },
  { id: "apache2.service", enabled: false },
  { id: "cron.service", enabled: true },
  { id: "ssh.service", enabled: true },
];

/**
 * Consumption recipe only.
 *
 * The host React application must load vendored web-tui-kit/tokens.css,
 * web-tui-kit/tui.css, and (for tui:escape/data-tui-list enhancement)
 * web-tui-kit/tui.js once at application level.
 */
export function PackageConfiguration({
  services = DEFAULT_SERVICES,
  onAccept,
  onCancel,
}) {
  const dialogRef = useRef(null);
  const [selected, setSelected] = useState(
    () => new Set(services.filter((service) => service.enabled).map((service) => service.id)),
  );

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return undefined;

    const handleEscape = () => onCancel?.();
    dialog.addEventListener("tui:escape", handleEscape);
    return () => dialog.removeEventListener("tui:escape", handleEscape);
  }, [onCancel]);

  function toggleService(serviceId, checked) {
    setSelected((current) => {
      const next = new Set(current);
      if (checked) next.add(serviceId);
      else next.delete(serviceId);
      return next;
    });
  }

  function accept() {
    onAccept?.(services.filter((service) => selected.has(service.id)).map((service) => service.id));
  }

  return (
    <main className="tui-screen">
      <section
        ref={dialogRef}
        className="tui-dialog"
        data-tui-escape-close
        aria-labelledby="package-title"
      >
        <h1 className="tui-dialog-title" id="package-title">
          Package configuration
        </h1>

        <p className="tui-dialog-copy">Daemons using outdated libraries</p>
        <p className="tui-dialog-copy">Which services should be restarted?</p>

        <div
          className="tui-checklist"
          data-tui-list
          role="group"
          aria-label="Services to restart"
        >
          {services.map((service, index) => (
            <label className="tui-check-row" key={service.id}>
              <input
                type="checkbox"
                checked={selected.has(service.id)}
                onChange={(event) => toggleService(service.id, event.target.checked)}
                autoFocus={index === 0}
              />
              <span className="tui-mark" aria-hidden="true" />
              <span>{service.id}</span>
              <span className="tui-help" aria-hidden="true">&lt;Help&gt;</span>
            </label>
          ))}
        </div>

        <div className="tui-actions">
          <button className="tui-button" type="button" accessKey="o" onClick={accept}>
            <span className="tui-hotkey">O</span>k
          </button>
        </div>
      </section>
    </main>
  );
}
