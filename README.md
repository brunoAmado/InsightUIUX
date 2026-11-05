# InsightUIUX™ (`:4023 /api/uiux`)

> **Tagline**: Dedicated 2D UI/UX Design System, Anti-AI-Slop DOM/CSS Linter, 7-Decision Mathematical Typography, Concentric Border Radii & UX Engine 2.8
> **Foundation Tier**: `insightCoreIO + insightCoreAI` ([`InsightCore™`](file:///C:/Users/bruno/PycharmProjects/InsightCore))
> **Deployment Modes**: Standalone Microservice (`:4023`) or Mountable FastAPI Router (`/api/uiux`) inside `ChronicleRAG` (`:8765`).

## 1. Core Capabilities (2D UI/UX & UX Engine 2.8)
- `ux_engine_2_8_anti_ai_slop_dom_and_css_linter`: Rejects `#000000` terminal black backgrounds (enforcing `#090d16` -> `#0f172a` -> `#172033` tinted dark slate), eliminates decorative purple-to-blue AI gradients, and enforces 1 Hero KPI + 3 compact secondary cards.
- `typography_7_decision_125_modular_scale_and_tabular_nums`: Enforces 5 modular font sizes (`1.25` ratio), 2 weights (`400`/`600`), `68ch` reading measure, and `font-variant-numeric: tabular-nums`.
- `concentric_border_radius_and_tinted_dark_slate_tokens`: Enforces $R_{\text{outer}} = R_{\text{inner}} + \text{padding}$ and serves canonical design tokens (`/api/uiux/tokens`).
- `reactive_4_state_and_on_blur_form_ux_verifier`: Verifies *Loading Skeleton*, *Empty State*, *Error + Retry*, *Populated State*, persistent `<label for="...">` above inputs, and `"Validate on Blur, Forgive on Keystroke"`.
- *(Note: Inclusivity & demographic fairness live in [`InsightInclude™`](file:///C:/Users/bruno/PycharmProjects/InsightInclude) on `:4020`, and 3D Three.js/Blender/CAD/Interactive Draw/Games live in [`InsightDesign™`](file:///C:/Users/bruno/PycharmProjects/InsightDesign) on `:4024`.)*

## 2. 4-Layer Hybrid Polyglot Layout
- `rust_core/`: Memory-safe Rust kernel (`insight_uiux_rs`) with Concentric Border Radius math and Trojan-Source Unicode stripping (`CVE-2021-42574`).
- `insight_uiux/`: Python FastAPI Engine (`engine.py`), Mountable Router (`router.py`), and Standalone Server (`server.py`).
- `node_sdk/index.js`: Universal JavaScript / Node.js SDK (`InsightUIUXClient`).
- `ui_component/insight-uiux.ts`: Standards-based TypeScript Web Component (`<insight-uiux>`).
- `tests/test_insight_uiux.py`: Unit, Unhappy-Path & Regression Test Suite.
