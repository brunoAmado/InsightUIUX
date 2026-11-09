"""
Unit, Unhappy-Path & Regression Tests for `InsightUIUX™` (`insight_uiux`).
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi.testclient import TestClient
from insight_uiux.engine import (
    InsightUIUXEngine,
    audit_uiux_engine_2_8,
    compute_concentric_border_radius,
    export_penpot_w3c_tokens_and_svg,
    get_sovereign_mobbin_pattern,
)
from insight_uiux.server import app


class TestInsightUIUX(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = InsightUIUXEngine()
        self.client = TestClient(app)

    def test_01_health_status_and_design_tokens(self) -> None:
        r_health = self.client.get("/health")
        self.assertEqual(r_health.status_code, 200)
        self.assertEqual(r_health.json()["service"], "InsightUIUX")
        self.assertEqual(r_health.json()["port"], 4023)

        r_status = self.client.get("/api/uiux/status")
        self.assertEqual(r_status.status_code, 200)
        self.assertTrue(r_status.json()["ok"])

        r_tokens = self.client.get("/api/uiux/tokens")
        self.assertEqual(r_tokens.status_code, 200)
        self.assertEqual(r_tokens.json()["ux_engine_version"], "2.8")

    def test_02_open_source_penpot_and_sovereign_mobbin_patterns(self) -> None:
        r_penpot = self.client.get("/api/uiux/penpot-tokens?title=CitySocket+Card")
        self.assertEqual(r_penpot.status_code, 200)
        penpot = r_penpot.json()
        self.assertTrue(penpot["ok"])
        self.assertEqual(penpot["replaces_proprietary_tool"], "Figma")
        self.assertIn("data-penpot-artboard", penpot["penpot_svg_artboard"])
        self.assertEqual(penpot["w3c_design_tokens"]["color"]["panel-bg"]["$value"], "#0f172a")

        r_pat = self.client.get("/api/uiux/patterns?pattern_id=stripe_checkout_and_onblur_form")
        self.assertEqual(r_pat.status_code, 200)
        pat_body = r_pat.json()
        self.assertTrue(pat_body["ok"])
        self.assertEqual(pat_body["replaces_proprietary_tool"], "Mobbin")
        self.assertEqual(pat_body["selected_pattern"]["pattern_id"], "stripe_checkout_and_onblur_form")

        # Unhappy path pattern fallback
        fallback_pat = get_sovereign_mobbin_pattern("unknown_pattern_xyz")
        self.assertEqual(
            fallback_pat["selected_pattern"]["pattern_id"],
            "linear_issue_table_and_command_palette",
        )

    def test_03_execute_happy_path_and_concentric_radius(self) -> None:
        r_exec = self.client.post("/api/uiux/execute", json={"inner_radius_px": 8, "padding_px": 8})
        self.assertEqual(r_exec.status_code, 200)
        res = r_exec.json()
        self.assertTrue(res["ok"])
        self.assertEqual(res["member"], "InsightUIUX")
        self.assertTrue(res["ux_engine_2_8_audit"]["anti_ai_slop_pass"])
        self.assertEqual(res["concentric_border_radius"]["outer_radius_px"], 16)
        self.assertIn("penpot_open_source_export", res)
        self.assertIn("sovereign_mobbin_pattern", res)

        r_widget = self.client.get("/api/uiux/widget.js")
        self.assertEqual(r_widget.status_code, 200)
        self.assertIn("customElements.define('insight-uiux'", r_widget.text)

    def test_04_unhappy_path_ai_slop_pure_black_and_missing_label_detected(self) -> None:
        slop_html = '<div style="background:#000000;background-image:linear-gradient(purple, blue);"><input placeholder="No label" /></div>'
        audit = audit_uiux_engine_2_8(slop_html)
        self.assertFalse(audit["anti_ai_slop_pass"])
        self.assertGreaterEqual(audit["violations_count"], 2)
        self.assertLess(audit["craft_score_10"], 8.0)

        concentric = compute_concentric_border_radius(12, 8)
        self.assertEqual(concentric["outer_radius_px"], 20)

    def test_05_unhappy_path_binary_blob_rejected_and_pii_scrubbed(self) -> None:
        bad_res = self.engine.execute({"raw_blob": "data:image/png;base64," + ("A" * 600)})
        self.assertFalse(bad_res["ok"])
        self.assertEqual(bad_res["error"], "BINARY_BLOB_REJECTED_USE_CAS_URI")

        r_scrub = self.client.post(
            "/api/uiux/scrub",
            json={"text": "NIF 123456789 e key sk-proj1234567890abcdef\u200b"},
        )
        self.assertEqual(r_scrub.status_code, 200)
        scrub_body = r_scrub.json()
        self.assertTrue(scrub_body["cnpd_gdpr_compliant"])
        self.assertNotIn("123456789", scrub_body["scrubbed_text"])

    def test_06_inline_mic_adornment_dedicated_wrapper_and_concentric_bounds(self) -> None:
        # Unhappy path: inline mic button appended directly to shared parent containing <label> or '+ Set' button
        bad_mic_markup = (
            '<div style="background:#0f172a;font-variant-numeric:tabular-nums;">'
            '<label for="new-partition-input">Folder</label>'
            '<input id="new-partition-input" type="text" />'
            '<button onclick="applyCustomNewFolder()">+ Set</button>'
            '<button class="chronicle-inline-mic-btn">🎙️</button>'
            "</div>"
        )
        bad_audit = audit_uiux_engine_2_8(bad_mic_markup)
        self.assertFalse(bad_audit["anti_ai_slop_pass"])
        rules = [v["rule"] for v in bad_audit["slop_violations"]]
        self.assertIn("CH4_INLINE_ADORNMENT_DEDICATED_WRAPPER", rules)
        self.assertIn("CH4_INLINE_ADORNMENT_CONCENTRIC_BOUNDS", rules)

        # Happy path: dedicated `.chronicle-input-mic-wrap` with concentric bounds (`max-height:calc(100% - 6px)`)
        good_mic_markup = (
            '<div style="background:#0f172a;font-variant-numeric:tabular-nums;">'
            '<label for="ingest-custom-tags-input">4. Custom Tags:</label>'
            '<div class="chronicle-input-mic-wrap relative flex items-center w-full">'
            '<input id="ingest-custom-tags-input" type="text" style="box-sizing:border-box;padding-right:29px;" />'
            '<button class="chronicle-inline-mic-btn" style="position:absolute;right:5px;top:50%;transform:translateY(-50%);width:20px;height:20px;max-height:calc(100% - 6px);box-sizing:border-box;">🎙️</button>'
            "</div></div>"
        )
        good_audit = audit_uiux_engine_2_8(good_mic_markup)
        self.assertTrue(good_audit["anti_ai_slop_pass"])
        self.assertTrue(good_audit["checks"]["inline_adornment_dedicated_wrapper_valid"])
        self.assertTrue(good_audit["checks"]["inline_adornment_concentric_bounds_valid"])


if __name__ == "__main__":
    unittest.main()
