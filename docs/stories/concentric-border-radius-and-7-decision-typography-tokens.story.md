---
slug: concentric-border-radius-and-7-decision-typography-tokens
epic: insightuiux-2d-design-system-and-ux-engine-2-8
project: InsightUIUX
chronicle_book: Book_Lit_Master_UI_UX_Engineering.md
labels:
- bdd
- three-amigos
- concentric-radius
- typography
- tabular-nums
---

# Concentric Border Radius Calculator (R_outer = R_inner + padding) & 7-Decision 1.25 Modular Typography Tokens (`/api/uiux/tokens`)

### Narrative
As a **design system consumer across all 35 repositories**, I want to **compute exact concentric outer border radii in Rust/Python and serve canonical 1.25 modular typography and tabular-nums tokens** so that **eliminates nested corner bulging and arbitrary pixel font sizes across all Web Components**.

### ChronicleRAG & Conversation Provenance
- **5-Tier Project Book**: `Book_Lit_Master_UI_UX_Engineering.md`
- **Primary AST Modules**: `insight_uiux/router.py`, `node_sdk/index.js`
- ChronicleRAG Master Playbooks: `Book_Lit_Master_UI_UX_Engineering.md` (111 chapters, 89 source books) & `Book_Lit_Master_ui_ux_design.md` (78 chapters)
- Antigravity IDE: Tri-Pillar separation of Inclusivity (`InsightInclude` :4020), 2D UI/UX (`InsightUIUX` :4023), and 3D/CAD/Blender/Interactive Draw/Games (`InsightDesign` :4024)

### Acceptance Criteria

1. **Happy Path Execution**: `concentric-border-radius-and-7-decision-typography-tokens` executes across `insight_uiux/router.py`, `node_sdk/index.js` and returns a deterministic, schema-validated response.
2. **Unhappy Path & Input Validation**: Malformed, out-of-range, or unauthorized payloads are rejected with explicit `400`/`403` validation errors and zero side effects.
3. **PT/EU Statutory & Security Gate (`RULE-11`)**: `SecurityAuditAgent` and `InsightAudit (:4009)` confirm zero CWE/OWASP-LLM findings, CNPD/GDPR PII scrubbing (`Lei n.º 58/2019`), and `SHA-256` hash-chained audit receipt logging (`EU AI Act Art. 12`).

### Tasks
- [x] Mine architectural requirements from ChronicleRAG (`Book_Lit_Master_UI_UX_Engineering.md`) and conversation timeline
- [x] Generate Three-Amigos `docs/stories/concentric-border-radius-and-7-decision-typography-tokens.story.md` and Gherkin `concentric-border-radius-and-7-decision-typography-tokens.feature`
- [x] Verify metadata and Gherkin scenarios via `BusinessAnalystAgent.validate_story_metadata()`

---
🔗 Epic: [insightuiux-2d-design-system-and-ux-engine-2-8](../epics/insightuiux-2d-design-system-and-ux-engine-2-8.epic.md)  
🔗 Feature: [concentric-border-radius-and-7-decision-typography-tokens.feature](concentric-border-radius-and-7-decision-typography-tokens.feature)
