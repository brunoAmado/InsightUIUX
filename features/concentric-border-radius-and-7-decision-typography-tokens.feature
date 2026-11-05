Feature: Concentric Border Radius Calculator (R_outer = R_inner + padding) & 7-Decision 1.25 Modular Typography Tokens (`/api/uiux/tokens`) (InsightUIUX)
  As a design system consumer across all 35 repositories
  I want to compute exact concentric outer border radii in Rust/Python and serve canonical 1.25 modular typography and tabular-nums tokens
  So that eliminates nested corner bulging and arbitrary pixel font sizes across all Web Components

  @positive @happy_path @chroniclerag
  Scenario: Happy path - Concentric Border Radius Calculator (R_outer = R_inner + padding) & 7-Decision 1.25 Modular Typography Tokens (`/api/uiux/tokens`) succeeds with verified parameters
    Given the "InsightUIUX" subsystem and epic "insightuiux-2d-design-system-and-ux-engine-2-8" are initialized
    And ChronicleRAG provenance from "Book_Lit_Master_UI_UX_Engineering.md" is active
    When the design system consumer across all 35 repositories triggers "concentric-border-radius-and-7-decision-typography-tokens" with valid parameters
    Then the operation succeeds with deterministic output and appends an EU AI Act Art. 12 SHA-256 receipt

  @negative @unhappy_path @validation
  Scenario: Negative edge case - Concentric Border Radius Calculator (R_outer = R_inner + padding) & 7-Decision 1.25 Modular Typography Tokens (`/api/uiux/tokens`) rejects malformed or out-of-bounds input
    Given the "InsightUIUX" subsystem and epic "insightuiux-2d-design-system-and-ux-engine-2-8" are initialized
    When the design system consumer across all 35 repositories triggers "concentric-border-radius-and-7-decision-typography-tokens" with empty or malformed parameters
    Then the system returns a 400 validation error without mutating state

  @security @pt_eu_compliance @rule_11
  Scenario: Security boundary - Concentric Border Radius Calculator (R_outer = R_inner + padding) & 7-Decision 1.25 Modular Typography Tokens (`/api/uiux/tokens`) enforces CNPD/GDPR PII scrubbing and blocks injection payloads
    Given the SecurityAuditAgent, InsightAudit (:4009), and Blue-Team guards are active
    When an untrusted caller submits path traversal, prompt injection, or raw PT NIF/IBAN PII to "concentric-border-radius-and-7-decision-typography-tokens"
    Then sensitive tokens are scrubbed or blocked and a security audit event is recorded
