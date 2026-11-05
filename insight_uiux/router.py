"""
FastAPI `APIRouter` Plugin for `InsightUIUX™` (`insight_uiux.router`).
Can be mounted standalone (`:4023`) or inside `ChronicleRAG` (`:8765`).
"""

from typing import Any, Dict
from fastapi import APIRouter, Body, FastAPI, Query
from fastapi.responses import Response

from insight_uiux.engine import (
    InsightUIUXEngine,
    UX_ENGINE_2_8_DESIGN_TOKENS,
    export_penpot_w3c_tokens_and_svg,
    get_sovereign_mobbin_pattern,
)


def create_insight_uiux_router() -> APIRouter:
    engine = InsightUIUXEngine()
    router = APIRouter(tags=["InsightUIUX"])

    @router.get("/status")
    def get_status() -> Dict[str, Any]:
        return engine.get_status()

    @router.get("/tokens")
    def get_design_tokens() -> Dict[str, Any]:
        return {"ok": True, "ux_engine_version": "2.8", "tokens": UX_ENGINE_2_8_DESIGN_TOKENS}

    @router.get("/penpot-tokens")
    def get_penpot_tokens(title: str = Query(default="InsightUIUX Penpot Component")) -> Dict[str, Any]:
        return export_penpot_w3c_tokens_and_svg(title)

    @router.get("/patterns")
    def get_mobbin_patterns(pattern_id: str = Query(default="linear_issue_table_and_command_palette")) -> Dict[str, Any]:
        return get_sovereign_mobbin_pattern(pattern_id)

    @router.post("/execute")
    def execute_action(payload: Dict[str, Any] = Body(default={})) -> Dict[str, Any]:
        return engine.execute(payload)

    @router.post("/scrub")
    def scrub_text(payload: Dict[str, Any] = Body(default={})) -> Dict[str, Any]:
        return engine.scrub_input(str(payload.get("text", "")))

    @router.get("/widget.js")
    def get_web_component_js() -> Response:
        js = """
(function() {
  if (typeof window === 'undefined' || customElements.get('insight-uiux')) return;
  class InsightUIUXElement extends HTMLElement {
    connectedCallback() {
      const apiBase = this.getAttribute('api-base') || '/api/uiux';
      this.innerHTML = `<section role="region" aria-label="InsightUIUX Widget" style="background:#0f172a;color:#f8fafc;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:16px;font-family:Inter,system-ui,sans-serif;"><h3 style="margin:0;font-size:15px;font-weight:600;">InsightUIUX™ (UX Engine 2.8 · Penpot · Sovereign Patterns)</h3><div aria-live="polite" style="font-size:12px;color:#94a3b8;margin-top:6px;font-variant-numeric:tabular-nums;">Active on ${apiBase}</div></section>`;
    }
  }
  customElements.define('insight-uiux', InsightUIUXElement);
})();
""".strip()
        return Response(content=js, media_type="application/javascript")

    return router


def mount_insight_uiux_plugin(app: FastAPI, prefix: str = "/api/uiux") -> bool:
    app.include_router(create_insight_uiux_router(), prefix=prefix)
    return True
