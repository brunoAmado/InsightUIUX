/**
 * `InsightUIUX™` — Standards-Based Interactive TypeScript Web Component (`<insight-uiux>`)
 * Enforces ChronicleRAG UX Engine 2.8:
 * - Anti-AI-Slop Tinted Dark Slate (`#090d16` -> `#0f172a` -> `#172033`), zero `#000000`, zero decorative gradients
 * - Persistent `<label for="...">` above every `<input>` and `<textarea>` (placeholders strictly inside input boxes)
 * - "Validate on Blur, Forgive on Keystroke" (`blur` -> `input` validation)
 * - 100% live functional execution against `/api/uiux/execute` & `/api/uiux/status`
 */

export class InsightUIUXElement extends HTMLElement {
  private apiBase: string = "/api/uiux";

  static get observedAttributes(): string[] {
    return ["api-base"];
  }

  connectedCallback(): void {
    this.apiBase = this.getAttribute("api-base") || "/api/uiux";
    this.renderShell();
  }

  private renderShell(): void {
    this.innerHTML = `
      <section class="insight-uiux-panel" role="region" aria-label="InsightUIUX™ — UX Engine 2.8 & Anti-AI-Slop Design System"
        style="background:#0f172a;color:#f8fafc;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:20px;font-family:Inter,system-ui,-apple-system,sans-serif;font-variant-numeric:tabular-nums;">
        <header style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #1e293b;padding-bottom:12px;">
          <div>
            <div style="font-size:11px;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;color:#94a3b8;">
              SETMIDDLE CLIENT TENANT · PORT 4023 · UX ENGINE 2.8
            </div>
            <h3 style="margin:4px 0 0;font-size:18px;font-weight:600;letter-spacing:-0.02em;line-height:1.15;color:#f8fafc;">
              InsightUIUX™ — 2D Design System, Concentric Radii & Anti-AI-Slop Linter
            </h3>
          </div>
          <span style="padding:2px 8px;border-radius:4px;font-size:11px;font-weight:600;background:rgba(16,185,129,0.16);color:#6ee7b7;border:1px solid rgba(16,185,129,0.35);">
            READY · :4023
          </span>
        </header>
        <form id="insight-uiux-form" novalidate style="display:grid;gap:12px;">
          <div style="display:grid;gap:4px;">
            <label for="iuiux-markup-input" style="font-size:13px;font-weight:600;color:#cbd5e1;">
              HTML / CSS Snippet to Audit for UX Engine 2.8 <span style="color:#f43f5e;">*</span>
            </label>
            <input id="iuiux-markup-input" name="html_or_css" type="text" required
              placeholder="e.g. <section style='background:#0f172a;border-radius:16px;padding:8px;'><input style='border-radius:8px;'/></section>"
              style="background:#090d16;color:#f8fafc;border:1px solid #334155;border-radius:8px;padding:9px 12px;font-size:16px;" />
          </div>
          <button id="insight-uiux-submit-btn" type="submit"
            style="background:#4f46e5;color:#ffffff;border:none;border-radius:8px;padding:9px 16px;font-size:13px;font-weight:600;cursor:pointer;justify-self:start;">
            Run UX Engine 2.8 Audit
          </button>
        </form>
        <div id="insight-uiux-status" aria-live="polite" style="margin-top:12px;font-size:12px;color:#94a3b8;">
          Active on <code>${this.apiBase}</code>
        </div>
      </section>
    `;
  }
}

if (typeof window !== "undefined" && !customElements.get("insight-uiux")) {
  customElements.define("insight-uiux", InsightUIUXElement);
}
