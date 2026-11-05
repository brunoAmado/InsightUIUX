"""
`InsightUIUX™` (`insight_uiux`) — Dedicated 2D UI/UX Design System, Open-Source Penpot W3C Tokens, Sovereign Mobbin Patterns & UX Engine 2.8 (`:4023 /api/uiux`).
"""

from insight_uiux.engine import (
    SOVEREIGN_MOBBIN_REFERENCE_PATTERNS,
    UX_ENGINE_2_8_DESIGN_TOKENS,
    InsightUIUXEngine,
    audit_uiux_engine_2_8,
    compute_concentric_border_radius,
    export_penpot_w3c_tokens_and_svg,
    get_sovereign_mobbin_pattern,
)

__version__ = "1.1.0"

__all__ = [
    "InsightUIUXEngine",
    "SOVEREIGN_MOBBIN_REFERENCE_PATTERNS",
    "UX_ENGINE_2_8_DESIGN_TOKENS",
    "__version__",
    "audit_uiux_engine_2_8",
    "compute_concentric_border_radius",
    "export_penpot_w3c_tokens_and_svg",
    "get_sovereign_mobbin_pattern",
]
