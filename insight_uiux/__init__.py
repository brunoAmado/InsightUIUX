"""
`InsightUIUX™` (`insight_uiux`) — Dedicated 2D UI/UX Design System & UX Engine 2.8 (`:4023 /api/uiux`).
"""

from insight_uiux.engine import (
    UX_ENGINE_2_8_DESIGN_TOKENS,
    InsightUIUXEngine,
    audit_uiux_engine_2_8,
    compute_concentric_border_radius,
)

__version__ = "1.0.0"

__all__ = [
    "InsightUIUXEngine",
    "UX_ENGINE_2_8_DESIGN_TOKENS",
    "__version__",
    "audit_uiux_engine_2_8",
    "compute_concentric_border_radius",
]
