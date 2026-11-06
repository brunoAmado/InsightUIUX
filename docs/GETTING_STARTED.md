# 🚀 Getting Started with `InsightUIUX`

> **Service Port**: `:4023` | **API Prefix**: `/api/uiux`
> **Technology Stack**: 4-Layer Hybrid Polyglot (Rust Core + Python FastAPI + Node.js SDK + TypeScript Web Component)
> **Tagline**: Dedicated 2D UI/UX Design System, Anti-AI-Slop DOM/CSS Linter, Concentric Radii, Open-Source Penpot W3C Tokens/SVG & Sovereign Mobbin Pattern Library (UX Engine 2.8)

---

## 1. Prerequisites

Depending on the layers of `InsightUIUX` you are working with, ensure the following tools are available on your machine:
- **Python 3.11+**: Shared virtual environment at `C:\Users\bruno\PycharmProjects\chronicle-rag\.venv` (with `insight_family_members.pth` linking all 27 `Insight*` / `SetMiddle` packages in editable `LATEST-HEAD` mode).
- **Rust Toolchain (`cargo` / `rustc` 2021 edition)**: For compiling `rust_core/` memory-safe kernels.
- **Node.js 20+ & TypeScript**: For `node_sdk/` universal clients and `ui_component/` Web Components (`<insight-uiux>`).
- **Java 21 & Maven (`mvnw`)** *(for `context-assistant` and `Indexer`)*: OpenJDK 21 with Vector API / Virtual Threads.

---

## 2. Quickstart: Running `InsightUIUX` Locally

### Step 1 — Clone or Navigate to the Workspace
```powershell
# Primary JetBrains / Development Workspace:
cd "C:\Users\bruno\PycharmProjects\InsightUIUX"

# Or Context-Assistant Managed DEV Mirror:
cd "C:\Users\bruno\IdeaProjects\context-assistant\projects\InsightUIUX"
```

### Step 2 — Run the Automated Test Suite (Mandatory Pre-Flight Gate)
```powershell
python -m unittest discover -s tests -v
```

### Step 3 — Start the Service on Port `:4023`
```powershell
python -m insight_uiux.server
```

### Step 4 — Verify Health & Status Endpoints
```powershell
curl http://127.0.0.1:4023/health
curl http://127.0.0.1:4023/api/uiux/status
```

---

## 3. Multi-Environment Architecture (`DEV` -> `DEMO_SHARED` -> `CLIENT_PROD`)

`InsightUIUX` participates in the 3-stage SetMiddle & Família Insights™ promotion pipeline managed by `context-assistant (:8080)`:
1. **`DEV` (`branch: dev`)**: Resolves shared modules directly from live `HEAD` via `insight_family_members.pth`.
2. **`DEMO_SHARED` (`branch: demo`)**: Pre-production integration environment across JetBrains workspaces.
3. **`CLIENT_PROD` (`branch: main`)**: Tagged production release with strict tenant isolation (`SETMIDDLE` vs. `INSIGHTCV_ECOSYSTEM`).

---

## 4. Next Steps
- 📖 Read **[How-To Guides & Recipes](./HOW_TO_GUIDES.md)** for step-by-step code examples.
- 🏛️ Read **[Architecture & Ecosystem Explanation](./ARCHITECTURE_AND_EXPLANATION.md)** for internal data flow and polyglot layer design.
- 🛡️ Read **[Security & PT/EU Statutory Compliance](./SECURITY_AND_COMPLIANCE.md)** for `RULE-11` privacy, accessibility, and SAST rules.
