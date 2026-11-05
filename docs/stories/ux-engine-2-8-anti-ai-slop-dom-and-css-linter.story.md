---
slug: ux-engine-2-8-anti-ai-slop-dom-and-css-linter
epic: insightuiux-2d-design-system-and-ux-engine-2-8
project: InsightUIUX
chronicle_book: Book_Lit_Master_UI_UX_Engineering.md
labels:
- bdd
- three-amigos
- insightuiux
- ux-engine-2-8
- anti-ai-slop
---

# UX Engine 2.8 Anti-AI-Slop DOM & CSS Linter (`/api/uiux/execute`)

### Narrative
As a **frontend architect and UI engineer**, I want to **reject pure #000000 terminal black backgrounds (enforcing tinted dark slate #090d16 -> #0f172a -> #172033), eliminate decorative purple-to-blue gradients, and verify persistent <label for='...'> above inputs** so that **every SetMiddle and Família Insights™ interface maintains a high-craft, zero-slop visual hierarchy**.

### ChronicleRAG & Conversation Provenance
- **5-Tier Project Book**: `Book_Lit_Master_UI_UX_Engineering.md`
- **Primary AST Modules**: `insight_uiux/engine.py`, `rust_core/src/main.rs`
- ChronicleRAG Master Playbooks: `Book_Lit_Master_UI_UX_Engineering.md` (111 chapters, 89 source books) & `Book_Lit_Master_ui_ux_design.md` (78 chapters)
- Antigravity IDE: Tri-Pillar separation of Inclusivity (`InsightInclude` :4020), 2D UI/UX (`InsightUIUX` :4023), and 3D/CAD/Blender/Interactive Draw/Games (`InsightDesign` :4024)

### Acceptance Criteria

1. **Happy Path Execution**: `ux-engine-2-8-anti-ai-slop-dom-and-css-linter` executes across `insight_uiux/engine.py`, `rust_core/src/main.rs` and returns a deterministic, schema-validated response.
2. **Unhappy Path & Input Validation**: Malformed, out-of-range, or unauthorized payloads are rejected with explicit `400`/`403` validation errors and zero side effects.
3. **PT/EU Statutory & Security Gate (`RULE-11`)**: `SecurityAuditAgent` and `InsightAudit (:4009)` confirm zero CWE/OWASP-LLM findings, CNPD/GDPR PII scrubbing (`Lei n.º 58/2019`), and `SHA-256` hash-chained audit receipt logging (`EU AI Act Art. 12`).

### Tasks
- [x] Mine architectural requirements from ChronicleRAG (`Book_Lit_Master_UI_UX_Engineering.md`) and conversation timeline
- [x] Generate Three-Amigos `docs/stories/ux-engine-2-8-anti-ai-slop-dom-and-css-linter.story.md` and Gherkin `ux-engine-2-8-anti-ai-slop-dom-and-css-linter.feature`
- [x] Verify metadata and Gherkin scenarios via `BusinessAnalystAgent.validate_story_metadata()`

---
🔗 Epic: [insightuiux-2d-design-system-and-ux-engine-2-8](../epics/insightuiux-2d-design-system-and-ux-engine-2-8.epic.md)  
🔗 Feature: [ux-engine-2-8-anti-ai-slop-dom-and-css-linter.feature](ux-engine-2-8-anti-ai-slop-dom-and-css-linter.feature)
