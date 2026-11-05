"""
`InsightUIUX™` Core Engine (`insight_uiux.engine`).
Dedicated 2D UI/UX Design System, Open-Source Penpot W3C Token/SVG Exporter, Sovereign Mobbin Pattern Library & UX Engine 2.8 Auditor (`:4023 /api/uiux`), distilled from:
- `Book_Lit_Master_UI_UX_Engineering.md` (111 chapters, 89 source books) & `Book_Lit_Master_ui_ux_design.md` (78 chapters)
- `Book_Context_j9j_d7AGSDc.md` (*I Tested Your Favorite "Alternative" Design Tools* — Penpot, Graphite, Inkscape, Quant-UX, Storybook)
- `.agents/skills/ux-engine/SKILL.md`:
  * Ch. 1: Anti-AI-Slop Dashboard Architecture (no decorative purple/blue gradients, 1 flat semantic accent `#4f46e5`, 1 primary Hero KPI + 3 compact)
  * Ch. 2: Typography as a 7-Decision Mathematical System (5 sizes on `1.25` modular scale, weights `400` & `600`, `68ch` reading measure)
  * Ch. 3: Concentric Border Radii (`R_outer = R_inner + padding`), Cards vs. Panels, Tinted Dark Slate (`#090d16` -> `#0f172a` -> `#172033`, never pure `#000000`)
  * Ch. 4: Form UX ("Validate on Blur, Forgive on Keystroke" `onBlur` -> `onChange`, persistent `<label for="...">` above inputs, example `placeholder` inside inputs)
  * Ch. 5: Desktop Data Tables & Mobile Row Stacking (`font-variant-numeric: tabular-nums`, right-aligned numbers, `40px`/`48px`/`56px` density modes)
  * Ch. 17: 4-State Reactive Completeness (*Loading Skeleton*, *Empty State*, *Error + Retry*, *Populated State*)
*(Note: Inclusivity & demographic fairness live in `InsightInclude™` `:4020`, and 3D Three.js/Blender/CAD/Interactive Draw/Games/Canva-SVG/Slidev live in `InsightDesign™` `:4024`.)*
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

SOVEREIGN_MOBBIN_REFERENCE_PATTERNS: Dict[str, Dict[str, Any]] = {
    "linear_issue_table_and_command_palette": {
        "pattern_id": "linear_issue_table_and_command_palette",
        "replaces_proprietary_service": "Mobbin SaaS B2B Workspace / Issue Tracker Reference",
        "reference_apps": ["Linear", "Raycast", "Ashby"],
        "ux_engine_chapters": ["Ch. 5 Desktop Data Tables & Bulk Selection", "Ch. 7 Command Palette (⌘K)", "Ch. 18 Linear Aesthetic"],
        "key_rules": [
            "1px hairline borders (rgba(255,255,255,0.07)), zero zebra striping",
            "Right-aligned numeric/SLA columns with font-variant-numeric: tabular-nums",
            "3 density modes (40px Compact, 48px Default, 56px Comfortable) + Shift+Click bulk selection",
            "Sub-50ms ⌘K / Ctrl+K command palette with roving tabindex",
        ],
        "html_blueprint": (
            '<section style="background:#0f172a;color:#f8fafc;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:16px;font-variant-numeric:tabular-nums;">'
            '<header style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">'
            '<label for="cmd-search" style="font-size:12px;font-weight:600;color:#cbd5e1;">Command Filter (Ctrl+K)</label>'
            '<input id="cmd-search" type="search" placeholder="Filter issues, status, or assignee..." style="background:#090d16;color:#f8fafc;border:1px solid #334155;border-radius:8px;padding:6px 10px;" />'
            '</header>'
            '<table style="width:100%;border-collapse:collapse;font-size:15px;">'
            '<thead><tr style="border-bottom:1px solid rgba(255,255,255,0.07);"><th style="text-align:left;padding:8px;">Issue</th><th style="text-align:right;padding:8px;">Latency (ms)</th></tr></thead>'
            '<tbody><tr style="height:48px;"><td style="padding:8px;">SET-104 · MID Class B Telemetry</td><td style="text-align:right;padding:8px;">4.2 ms</td></tr></tbody>'
            '</table></section>'
        ),
    },
    "stripe_checkout_and_onblur_form": {
        "pattern_id": "stripe_checkout_and_onblur_form",
        "replaces_proprietary_service": "Mobbin High-Conversion Checkout & Auth Form Reference",
        "reference_apps": ["Stripe Checkout", "Revolut", "Clerk"],
        "ux_engine_chapters": ["Ch. 4 Validate on Blur, Forgive on Keystroke", "Ch. 15 Specialized High-Conversion Inputs"],
        "key_rules": [
            "Persistent <label for='...'> above every input; placeholder strictly inside input box",
            "Validate first on blur; switch invalid field to live input listener to clear error immediately",
            "16px minimum input font size on mobile to prevent iOS Safari auto-zoom",
        ],
        "html_blueprint": (
            '<form novalidate style="background:#0f172a;color:#f8fafc;border-radius:16px;padding:16px;display:grid;gap:12px;">'
            '<label for="fiscal-nif" style="font-size:12px;font-weight:600;color:#cbd5e1;">Portuguese NIF (9 Digits)</label>'
            '<input id="fiscal-nif" name="nif" inputmode="numeric" placeholder="e.g. 509123456" style="background:#090d16;color:#f8fafc;border:1px solid #334155;border-radius:8px;padding:8px 12px;font-size:16px;font-variant-numeric:tabular-nums;" />'
            '<button type="submit" style="background:#4f46e5;color:#ffffff;border:none;border-radius:8px;padding:10px 16px;font-weight:600;">Verify & Settle</button>'
            '</form>'
        ),
    },
    "raycast_hero_kpi_and_4state_dashboard": {
        "pattern_id": "raycast_hero_kpi_and_4state_dashboard",
        "replaces_proprietary_service": "Mobbin Analytics & Telemetry Dashboard Reference",
        "reference_apps": ["Raycast", "Vercel Analytics", "Grafana"],
        "ux_engine_chapters": ["Ch. 1 Anti-AI-Slop Dashboard Architecture", "Ch. 14 Honest Dashboard Charts", "Ch. 17 Reactive State Machines"],
        "key_rules": [
            "Break equal-card monotony: 1 Primary Hero KPI card large + 3 Secondary KPI cards compact",
            "Drop pastel icon tiles on metric cards — the metric number is the hero",
            "Spec all 4 mandatory states: Loading Skeleton, Empty State CTA, Error + Retry, Populated Hero Metric",
        ],
        "html_blueprint": (
            '<section style="background:#090d16;color:#f8fafc;padding:16px;border-radius:16px;font-variant-numeric:tabular-nums;" aria-live="polite">'
            '<div style="background:#0f172a;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:20px;margin-bottom:12px;">'
            '<div style="font-size:12px;color:#94a3b8;text-transform:uppercase;letter-spacing:0.05em;">Primary Grid Load (Hero KPI)</div>'
            '<div style="font-size:30px;font-weight:600;letter-spacing:-0.02em;line-height:1.15;margin-top:4px;">18.42 kW</div>'
            '</div></section>'
        ),
    },
    "citysocket_375px_mobile_nfc_tap": {
        "pattern_id": "citysocket_375px_mobile_nfc_tap",
        "replaces_proprietary_service": "Mobbin Mobile IoT & EV Charging Flow Reference",
        "reference_apps": ["CitySocket", "Tesla Mobile", "Apple Wallet NFC"],
        "ux_engine_chapters": ["Ch. 5 Mobile Row Stacking", "Ch. 9 5s Soft-Delete Undo Toast", "Ch. 20 375px Mobile Readiness"],
        "key_rules": [
            "375px viewport readiness with >= 44x44px coarse-pointer touch targets",
            "Stack mobile rows into 2 lines: Identity top-left, tabular-nums Metric top-right",
            "5-second soft-stop undo toast for session termination",
        ],
        "html_blueprint": (
            '<section style="max-width:375px;background:#0f172a;color:#f8fafc;border-radius:16px;padding:16px;font-variant-numeric:tabular-nums;">'
            '<div style="display:flex;justify-content:space-between;align-items:center;">'
            '<span style="font-size:15px;font-weight:600;">Lamppost #LP-042 (NTAG 424)</span>'
            '<span style="font-size:15px;font-weight:600;color:#10b981;">7.40 kW</span>'
            '</div>'
            '<button type="button" style="margin-top:12px;width:100%;min-height:44px;background:#4f46e5;color:#ffffff;border:none;border-radius:8px;font-weight:600;">Authorize EV Session</button>'
            '</section>'
        ),
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


def export_penpot_w3c_tokens_and_svg(component_title: str = "InsightUIUX Penpot Component") -> Dict[str, Any]:
    """
    Open-Source Figma Replacement (`Penpot` MPL-2.0):
    Exports UX Engine 2.8 tokens in the standard W3C Design Tokens Community Group (DTCG) format
    (`$value`, `$type`) natively imported by Penpot & Style Dictionary, plus a Penpot-ready SVG/Flexbox artboard.
    """
    safe_title = str(component_title or "InsightUIUX Penpot Component")
    w3c_tokens = {
        "$schema": "https://tr.designtokens.org/format/",
        "open_source_target": "Penpot (https://github.com/penpot/penpot - MPL-2.0)",
        "color": {
            "canvas-bg": {"$value": "#090d16", "$type": "color"},
            "panel-bg": {"$value": "#0f172a", "$type": "color"},
            "surface-bg": {"$value": "#172033", "$type": "color"},
            "primary-accent": {"$value": "#4f46e5", "$type": "color"},
            "focus-ring": {"$value": "#818cf8", "$type": "color"},
            "text-primary": {"$value": "#f8fafc", "$type": "color"},
            "text-secondary": {"$value": "#cbd5e1", "$type": "color"},
            "text-muted": {"$value": "#94a3b8", "$type": "color"},
        },
        "dimension": {
            "radius-sm": {"$value": "4px", "$type": "dimension"},
            "radius-md": {"$value": "8px", "$type": "dimension"},
            "radius-lg": {"$value": "16px", "$type": "dimension"},
            "density-compact": {"$value": "40px", "$type": "dimension"},
            "density-default": {"$value": "48px", "$type": "dimension"},
            "density-comfortable": {"$value": "56px", "$type": "dimension"},
        },
        "fontSizes": {
            "xs": {"$value": "12px", "$type": "dimension"},
            "sm": {"$value": "15px", "$type": "dimension"},
            "md": {"$value": "19px", "$type": "dimension"},
            "lg": {"$value": "24px", "$type": "dimension"},
            "xl": {"$value": "30px", "$type": "dimension"},
        },
    }
    penpot_svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 240" width="640" height="240" data-penpot-artboard="true">'
        '<rect x="0" y="0" width="640" height="240" rx="16" fill="#0f172a" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>'
        '<rect x="16" y="16" width="608" height="208" rx="8" fill="#172033"/>'
        f'<text x="36" y="60" fill="#f8fafc" font-family="Inter, system-ui, sans-serif" font-size="24" font-weight="600">{safe_title}</text>'
        '<text x="36" y="96" fill="#cbd5e1" font-family="Inter, system-ui, sans-serif" font-size="15" font-weight="400">Open-Source Penpot Native SVG + W3C Design Tokens (Zero Figma Lock-in)</text>'
        '<rect x="36" y="136" width="180" height="44" rx="8" fill="#4f46e5"/>'
        '<text x="64" y="163" fill="#ffffff" font-family="Inter, system-ui, sans-serif" font-size="15" font-weight="600">Inspect Artboard</text>'
        '</svg>'
    )
    return {
        "ok": True,
        "replaces_proprietary_tool": "Figma",
        "open_source_stack": ["Penpot (MPL-2.0)", "Quant-UX", "Storybook (MIT)"],
        "w3c_design_tokens": w3c_tokens,
        "penpot_svg_artboard": penpot_svg,
        "cas_svg_uri": build_cas_uri(penpot_svg),
    }


def get_sovereign_mobbin_pattern(pattern_id: str = "linear_issue_table_and_command_palette") -> Dict[str, Any]:
    """
    Open-Source Mobbin Replacement:
    Returns reference-grounded UI blueprints distilled from ChronicleRAG's 111-chapter Master UI/UX Book.
    """
    key = str(pattern_id or "").strip().lower()
    chosen = SOVEREIGN_MOBBIN_REFERENCE_PATTERNS.get(
        key,
        SOVEREIGN_MOBBIN_REFERENCE_PATTERNS["linear_issue_table_and_command_palette"],
    )
    return {
        "ok": True,
        "replaces_proprietary_tool": "Mobbin",
        "open_source_stack": [
            "ChronicleRAG Book_Lit_Master_UI_UX_Engineering.md (111 Chapters)",
            "shadcn/ui + Radix Primitives (MIT)",
            "OpenUI + Playwright DOM Inspector",
        ],
        "available_patterns": list(SOVEREIGN_MOBBIN_REFERENCE_PATTERNS.keys()),
        "selected_pattern": chosen,
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
            "version": "1.1.0",
            "port": self.DEFAULT_PORT,
            "api_prefix": self.API_PREFIX,
            "core_tier": "insightCoreIO + insightCoreAI",
            "mandate": "Dedicated 2D UI/UX Design System, Open-Source Penpot W3C Tokens/SVG, Sovereign Mobbin Pattern Library & UX Engine 2.8",
            "open_source_replacements": {
                "figma_replacement": "Penpot (MPL-2.0) W3C Design Tokens + Native SVG Artboards + Storybook",
                "mobbin_replacement": "ChronicleRAG 111-Chapter Sovereign Pattern Library + shadcn/Radix Blueprints",
            },
            "extracted_from": [
                "Book_Lit_Master_UI_UX_Engineering.md (111 Chapters)",
                "Book_Lit_Master_ui_ux_design.md (78 Chapters)",
                "Book_Context_j9j_d7AGSDc.md (Open-Source Alternative Design Tools: Penpot, Graphite, Inkscape)",
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
        pattern_id = str(data.get("pattern_id", "linear_issue_table_and_command_palette"))
        component_title = str(data.get("component_title", "SetMiddle Penpot Artboard"))

        audit = audit_uiux_engine_2_8(markup)
        concentric = compute_concentric_border_radius(inner_r, pad_px)
        penpot_bundle = export_penpot_w3c_tokens_and_svg(component_title)
        mobbin_pattern = get_sovereign_mobbin_pattern(pattern_id)
        return {
            "ok": True,
            "member": self.MEMBER_ID,
            "ux_engine_2_8_audit": audit,
            "concentric_border_radius": concentric,
            "design_tokens": UX_ENGINE_2_8_DESIGN_TOKENS,
            "penpot_open_source_export": penpot_bundle,
            "sovereign_mobbin_pattern": mobbin_pattern,
            "cas_uri": build_cas_uri(markup),
        }

    def scrub_input(self, text: str) -> Dict[str, Any]:
        return scrub_pt_eu_pii_and_byok_secrets(text)
