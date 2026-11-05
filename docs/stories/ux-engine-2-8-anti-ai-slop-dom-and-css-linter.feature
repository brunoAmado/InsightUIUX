Feature: UX Engine 2.8 Anti-AI-Slop DOM & CSS Linter (`/api/uiux/execute`) (InsightUIUX)
  As a frontend architect and UI engineer
  I want to reject pure #000000 terminal black backgrounds (enforcing tinted dark slate #090d16 -> #0f172a -> #172033), eliminate decorative purple-to-blue gradients, and verify persistent <label for='...'> above inputs
  So that every SetMiddle and Família Insights™ interface maintains a high-craft, zero-slop visual hierarchy

  @positive @happy_path @chroniclerag
  Scenario: Happy path - UX Engine 2.8 Anti-AI-Slop DOM & CSS Linter (`/api/uiux/execute`) succeeds with verified parameters
    Given the "InsightUIUX" subsystem and epic "insightuiux-2d-design-system-and-ux-engine-2-8" are initialized
    And ChronicleRAG provenance from "Book_Lit_Master_UI_UX_Engineering.md" is active
    When the frontend architect and UI engineer triggers "ux-engine-2-8-anti-ai-slop-dom-and-css-linter" with valid parameters
    Then the operation succeeds with deterministic output and appends an EU AI Act Art. 12 SHA-256 receipt

  @negative @unhappy_path @validation
  Scenario: Negative edge case - UX Engine 2.8 Anti-AI-Slop DOM & CSS Linter (`/api/uiux/execute`) rejects malformed or out-of-bounds input
    Given the "InsightUIUX" subsystem and epic "insightuiux-2d-design-system-and-ux-engine-2-8" are initialized
    When the frontend architect and UI engineer triggers "ux-engine-2-8-anti-ai-slop-dom-and-css-linter" with empty or malformed parameters
    Then the system returns a 400 validation error without mutating state

  @security @pt_eu_compliance @rule_11
  Scenario: Security boundary - UX Engine 2.8 Anti-AI-Slop DOM & CSS Linter (`/api/uiux/execute`) enforces CNPD/GDPR PII scrubbing and blocks injection payloads
    Given the SecurityAuditAgent, InsightAudit (:4009), and Blue-Team guards are active
    When an untrusted caller submits path traversal, prompt injection, or raw PT NIF/IBAN PII to "ux-engine-2-8-anti-ai-slop-dom-and-css-linter"
    Then sensitive tokens are scrubbed or blocked and a security audit event is recorded
