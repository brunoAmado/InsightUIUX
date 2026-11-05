# InsightUIUX™ (`:4023 /api/uiux`)

> **Tagline**: Dedicated 2D UI/UX Design System, Open-Source Penpot W3C Tokens/SVG (`Figma` Replacement), Sovereign Mobbin Pattern Library & UX Engine 2.8
> **Foundation Tier**: `insightCoreIO + insightCoreAI` ([`InsightCore™`](file:///C:/Users/bruno/PycharmProjects/InsightCore))
> **Deployment Modes**: Standalone Microservice (`:4023`) or Mountable FastAPI Router (`/api/uiux`) inside `ChronicleRAG` (`:8765`).

## 1. Core Capabilities (2D UI/UX, Open-Source Penpot & Sovereign Mobbin Patterns)
- `ux_engine_2_8_anti_ai_slop_dom_and_css_linter`: Rejects `#000000` terminal black backgrounds (enforcing `#090d16` -> `#0f172a` -> `#172033` tinted dark slate), eliminates decorative purple-to-blue AI gradients, and enforces 1 Hero KPI + 3 compact secondary cards.
- `open_source_penpot_w3c_design_tokens_and_svg_exporter` (`GET /api/uiux/penpot-tokens`): 100% open-source replacement for **Figma** using **Penpot (MPL-2.0)** native SVG + W3C Design Tokens Community Group (`$value`, `$type`) format and **Storybook**.
- `sovereign_mobbin_reference_pattern_library` (`GET /api/uiux/patterns`): 100% free replacement for **Mobbin** providing reference-grounded HTML/CSS blueprints distilled from `ChronicleRAG`'s 111-chapter Master UI/UX Book (*Linear Command Palette & Issue Table*, *Stripe Checkout & `onBlur` Form*, *Raycast Hero KPI & 4-State Dashboard*, *CitySocket `375px` Mobile NFC Tap*).
- `typography_7_decision_125_modular_scale_and_tabular_nums`: Enforces 5 modular font sizes (`1.25` ratio), 2 weights (`400`/`600`), `68ch` reading measure, and `font-variant-numeric: tabular-nums`.
- `concentric_border_radius_and_tinted_dark_slate_tokens`: Enforces $R_{\text{outer}} = R_{\text{inner}} + \text{padding}$ and serves canonical design tokens (`/api/uiux/tokens`).

## 2. 4-Layer Hybrid Polyglot Layout
- `rust_core/`: Memory-safe Rust kernel (`insight_uiux_rs`) with Concentric Border Radius math and Trojan-Source Unicode stripping (`CVE-2021-42574`).
- `insight_uiux/`: Python FastAPI Engine (`engine.py`), Mountable Router (`router.py`), and Standalone Server (`server.py`).
- `node_sdk/index.js`: Universal JavaScript / Node.js SDK (`InsightUIUXClient`).
- `ui_component/insight-uiux.ts`: Standards-based TypeScript Web Component (`<insight-uiux>`).
- `tests/test_insight_uiux.py`: Unit, Unhappy-Path & Regression Test Suite.
