# 🏛️ Architecture & Deep-Dive Explanation (`InsightUIUX`)

> **Project**: `InsightUIUX` | **Default Port**: `:4023` | **API Prefix**: `/api/uiux`
> **Stack**: 4-Layer Hybrid Polyglot (Rust Core + Python FastAPI + Node.js SDK + TypeScript Web Component)

---

## 1. Why `InsightUIUX` Exists & How It Fits in the Ecosystem

**`InsightUIUX`** — *Dedicated 2D UI/UX Design System, Anti-AI-Slop DOM/CSS Linter, Concentric Radii, Open-Source Penpot W3C Tokens/SVG & Sovereign Mobbin Pattern Library (UX Engine 2.8)* — is designed around a **Modular Hybrid Polyglot Architecture**. Rather than trapping domain logic inside a single monolithic codebase, `InsightUIUX` exposes its capabilities across four clean layers so every project in the ecosystem can consume it with zero duplication:

```mermaid
flowchart TB
    subgraph L4["Layer 4: Interactive UI & Design System (UX Engine 2.8)"]
        WC["<insight-uiux> Web Component\n(InsightUIUX :4023 + InsightInclude :4020 Certified)"]
    end
    subgraph L3["Layer 3: Universal Client & Orchestration"]
        SDK["node_sdk / Python Editable Package (insight_family_members.pth)"]
        CA["context-assistant (:8080) & InsightChat (:4012)"]
    end
    subgraph L2["Layer 2: Service & Plugin Router (:4023 /api/uiux)"]
        API["FastAPI / Spring Boot Router + 4-Tier Zero-Paid-Token AI Failover (insightCoreAI)"]
    end
    subgraph L1["Layer 1: Deterministic Kernel & Storage Guard"]
        RUST["rust_core/ (FNV-1a, SimHash, Safety Interlocks, CVE-2021-42574)"]
        IO["insightCoreIO (CAS sha256 Vault, PostgreSQL/pgvector, Apache AGE, CNPD Scrubber)"]
    end
    L4 --> L3 --> L2 --> L1
```

---

## 2. Integration with the Tri-Pillar Design & Inclusivity Suite
- **[`InsightInclude™ (:4020)`](https://github.com/brunoAmado/InsightInclude)**: Audits `InsightUIUX` for EU AI Act Art. 10 demographic fairness (`DIR >= 0.80`), `INPI PPP #4` Romance gender neutralization, `Leitura Fácil`, and Portugal `DL n.º 82/2022` (WCAG 2.2 AA/AAA) assistive-tech compliance.
- **[`InsightUIUX™ (:4023)`](https://github.com/brunoAmado/InsightUIUX)**: Audits `InsightUIUX`'s 2D interfaces for *UX Engine 2.8* Anti-AI-Slop rules, concentric border radii ($R_{\text{outer}} = R_{\text{inner}} + \text{padding}$), 7-decision `1.25` typography, **Open-Source Penpot W3C Design Tokens**, and **Sovereign Mobbin Reference Patterns**.
- **[`InsightDesign™ (:4024)`](https://github.com/brunoAmado/InsightDesign)**: Provides 3D Three.js digital-twin scenes, Blender `bpy` scripts, watertight `.STL` parametric CAD enclosures, interactive vector drawing canvases, playable WASD 3D simulations, and **Open-Source Canva SVG / Slidev presentation decks**.

---

## 3. Sovereign AST Knowledge Graph (`InsightCode™ :4013`) & Three-Amigos BDD
- **AST Cartography**: `InsightUIUX` is continuously indexed by **`InsightCode™ (:4013)`** (which replaced legacy `Graphify`) and stored in `context-assistant`'s **Apache AGE (`GraphService`)** call graph.
- **Three-Amigos BDD Suite**: Living Epics (`docs/epics/*.epic.md`), User Stories (`docs/stories/*.story.md`), and executable Gherkin scenarios (`features/*.feature`) are synchronized from **ChronicleRAG (`:8765`)** via `BusinessAnalystAgent`.
