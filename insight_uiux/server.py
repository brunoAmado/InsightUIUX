"""
Standalone FastAPI Server for `InsightUIUX™` (`python -m insight_uiux.server`).
Runs on port 4023 by default.
"""

import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from insight_uiux.router import mount_insight_uiux_plugin

app = FastAPI(
    title="InsightUIUX™ — 2D UI/UX Design System, Anti-AI-Slop Linter, Concentric Radii & UX Engine 2.8",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

mount_insight_uiux_plugin(app, prefix="/api/uiux")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "InsightUIUX",
        "port": 4023,
        "api_prefix": "/api/uiux",
        "version": "1.0.0",
    }


def main() -> None:
    port = int(os.environ.get("INSIGHT_UIUX_PORT", "4023"))
    uvicorn.run(app, host="127.0.0.1", port=port)


if __name__ == "__main__":
    main()
