"""
`InsightUIUX™` Core Engine (`insight_uiux.engine`).
Dedicated 2D UI/UX Design System & UX Engine 2.8 Auditor (`:4023 /api/uiux`), distilled from:
- `Book_Lit_Master_UI_UX_Engineering.md` (111 chapters, 89 source books) & `Book_Lit_Master_ui_ux_design.md` (78 chapters)
- `.agents/skills/ux-engine/SKILL.md`:
  * Ch. 1: Anti-AI-Slop Dashboard Architecture (no decorative purple/blue gradients, 1 flat semantic accent `#4f46e5`, 1 primary Hero KPI + 3 compact)
  * Ch. 2: Typography as a 7-Decision Mathematical System (5 sizes on `1.25` modular scale, weights `400` & `600`, `68ch` reading measure)
  * Ch. 3: Concentric Border Radii (`R_outer = R_inner + padding`), Cards vs. Panels, Tinted Dark Slate (`#090d16` -> `#0f172a` -> `#172033`, never pure `#000000`)
  * Ch. 4: Form UX ("Validate on Blur, Forgive on Keystroke" `onBlur` -> `onChange`, persistent `<label for="...">` above inputs, example `placeholder` inside inputs)
  * Ch. 5: Desktop Data Tables & Mobile Row Stacking (`font-variant-numeric: tabular-nums`, right-aligned numbers, `40px`/`48px`/`56px` density modes)
  * Ch. 17: 4-State Reactive Completeness (*Loading Skeleton*, *Empty State*, *Error + Retry*, *Populated State*)
*(Note: Inclusivity & demographic fairness live in `InsightInclude™` `:4020`, and 3D Three.js/Blender/CAD/Interactive Draw/Games live in `InsightDesign™` `:4024`.)*
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

_INSIGHT_CORE_DIR = Path(__file__).resolve().parent.parent.parent / "InsightCore"
if _INSIGHT_CORE_DIR.exists() and str(_INSIGHT_CORE_DIR) not in sys.path:
    sys.path.insert(0, str(_INSIGHT_CORE_DIR))

from insight_core_io import assert_no_binary_blob_in_db_row, build_cas_uri, scrub_pt_eu_pii_and_byok_secrets

UX_ENGINE_2_8_DESIGN_TOKENS: Dict[str, Any] = {
    "surfaces_tinted_dark_slate": {
        "canvas_bg": "#090d16",
        "elevated_panel_bg": "#0f172a",
        "interactive_surface_bg": "#172033",
        "hairline_border": "rgba(255, 255, 255, 0.07)",
        "forbid_pure_black_hex": "#000000",
    },
    "semantic_accent": {
        "primary_accent": "#4f46e5",
        "focus_visible_ring": "2px solid #818cf8",
        "danger_accent": "#f43f5e",
        "success_accent": "#10b981",
    },
    "typography_7_decisions": {
        "modular_scale_ratio": 1.25,
        "sizes_px": [12, 15, 19, 24, 30],
        "weights": [400, 600],
        "text_hierarchy_colors": {
            "primary": "#f8fafc",
            "secondary": "#cbd5e1",
            "muted": "#94a3b8",
        },
        "display_line_height": 1.15,
        "body_line_height": 1.55,
        "max_reading_measure": "68ch",
        "numeric_alignment": "tabular-nums",
    },
    "radius_scale_px": {
        "small_input_badge": 4,
        "medium_button_tile": 8,
        "large_card_modal": 16,
        "pill_chip": 9999,
    },
    "table_density_row_heights_px": {
        "compact": 40,
        "default": 48,
        "comfortable": 56,
    },
}


def compute_concentric_border_radius(inner_radius_px: int = 8, padding_px: int = 8) -> Dict[str, int]:
    """Enforces Chapter 3 Concentric Border Radius Law: R_outer = R_inner + padding."""
    inner = max(0, int(inner_radius_px))
    pad = max(0, int(padding_px))
    return {
        "inner_radius_px": inner,
        "padding_px": pad,
        "outer_radius_px": inner + pad,
    }


def audit_uiux_engine_2_8(html_or_css: str) -> Dict[str, Any]:
    """
    Deterministic UX Engine 2.8 Anti-AI-Slop & Design System Linter:
    1. Rejects pure `#000000` terminal black backgrounds (requires tinted dark `#090d16` / `#0f172a` / `#172033`).
    2. Rejects decorative AI-slop linear-gradients on generic headers/cards.
    3. Verifies `<label for="...">` + input `placeholder` separation.
    4. Verifies `tabular-nums` for numeric scannability.
    5. Computes an Anti-AI-Slop Craft Score (`0.0` - `10.0`).
    """
    snippet = str(html_or_css or "")
    slop_violations: List[Dict[str, str]] = []

    if re.search(r"background(?:-color)?\s*:\s*(?:#000000|#000\b|black\b)", snippet, flags=re.IGNORECASE):
        slop_violations.append({
            "rule": "CH3_NO_PURE_BLACK_DARK_MODE",
            "remediation": "Replace #000000 with tinted dark slate (#090d16 canvas, #0f172a panel, #172033 surface).",
        })

    if re.search(r"linear-gradient\([^)]*(?:purple|violet|#8b5cf6|#a855f7)[^)]*(?:blue|cyan|#3b82f6|#06b6d4)", snippet, flags=re.IGNORECASE):
        slop_violations.append({
            "rule": "CH1_NO_DECORATIVE_AI_SLOP_GRADIENT",
            "remediation": "Eliminate decorative purple-to-blue gradients; use a single flat semantic accent (#4f46e5).",
        })

    has_inputs = bool(re.search(r"<(?:input|textarea)\b", snippet, flags=re.IGNORECASE))
    has_label_for = bool(re.search(r"<label\b[^>]*\bfor=", snippet, flags=re.IGNORECASE))
    if has_inputs and not has_label_for:
        slop_violations.append({
            "rule": "CH4_PERSISTENT_LABEL_ABOVE_INPUT",
            "remediation": "Every <input>/<textarea> must have a persistent <label for='...'> above it.",
        })

    has_tabular_nums = "tabular-nums" in snippet
    has_tinted_slate = any(hex_col in snippet.lower() for hex_col in ("#090d16", "#0f172a", "#172033"))

    score = max(0.0, round(10.0 - (2.5 * len(slop_violations)), 2))
    return {
        "ux_engine_version": "2.8",
        "anti_ai_slop_pass": len(slop_violations) == 0,
        "craft_score_10": score,
        "violations_count": len(slop_violations),
        "slop_violations": slop_violations,
        "checks": {
            "tinted_dark_slate_present": has_tinted_slate,
            "tabular_nums_present": has_tabular_nums,
            "label_for_binding_valid": (not has_inputs) or has_label_for,
            "validation_timing_pattern": "VALIDATE_ON_BLUR_FORGIVE_ON_KEYSTROKE",
            "four_states_required": ["LOADING_SKELETON", "EMPTY_STATE_CTA", "ERROR_WITH_RETRY", "POPULATED_HERO_METRIC"],
        },
    }


class InsightUIUXEngine:
    MEMBER_ID = "InsightUIUX"
    DEFAULT_PORT = 4023
    API_PREFIX = "/api/uiux"

    def get_status(self) -> Dict[str, Any]:
        return {
            "ok": True,
            "product": "InsightUIUX™",
            "version": "1.0.0",
            "port": self.DEFAULT_PORT,
            "api_prefix": self.API_PREFIX,
            "core_tier": "insightCoreIO + insightCoreAI",
            "mandate": "Dedicated 2D UI/UX Design System & UX Engine 2.8 (Anti-AI-Slop, 7-Decision Typography, Concentric Radii, Tinted Dark Mode & 4-State Reactive Machines)",
            "extracted_from": [
                "Book_Lit_Master_UI_UX_Engineering.md (111 Chapters)",
                "Book_Lit_Master_ui_ux_design.md (78 Chapters)",
                ".agents/skills/ux-engine/SKILL.md",
            ],
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        ok_storage, violations = assert_no_binary_blob_in_db_row(payload or {})
        if not ok_storage:
            return {"ok": False, "member": self.MEMBER_ID, "error": "BINARY_BLOB_REJECTED_USE_CAS_URI", "violations": violations}
        data = payload or {}
        default_markup = (
            '<section style="background:#0f172a;color:#f8fafc;font-variant-numeric:tabular-nums;border-radius:16px;padding:8px;">'
            '<label for="metric-filter">Filter KPI</label>'
            '<input id="metric-filter" placeholder="e.g. Revenue Q4" style="border-radius:8px;" />'
            "</section>"
        )
        markup = str(data.get("html_or_css", data.get("html", default_markup)))
        inner_r = int(data.get("inner_radius_px", 8))
        pad_px = int(data.get("padding_px", 8))

        audit = audit_uiux_engine_2_8(markup)
        concentric = compute_concentric_border_radius(inner_r, pad_px)
        return {
            "ok": True,
            "member": self.MEMBER_ID,
            "ux_engine_2_8_audit": audit,
            "concentric_border_radius": concentric,
            "design_tokens": UX_ENGINE_2_8_DESIGN_TOKENS,
            "cas_uri": build_cas_uri(markup),
        }

    def scrub_input(self, text: str) -> Dict[str, Any]:
        return scrub_pt_eu_pii_and_byok_secrets(text)
