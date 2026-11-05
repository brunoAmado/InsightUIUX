Feature: 4-State Reactive Machine & Validate-on-Blur Web Component (`<insight-uiux>`) (InsightUIUX)
  As a product engineer and QA verifier
  I want to verify Loading Skeleton, Empty State CTA, Error + Retry, Populated Hero KPI, and Validate-on-Blur/Forgive-on-Keystroke in `<insight-uiux>`
  So that consistent, zero-layout-shift interactive forms and dashboards

  @positive @happy_path @chroniclerag
  Scenario: Happy path - 4-State Reactive Machine & Validate-on-Blur Web Component (`<insight-uiux>`) succeeds with verified parameters
    Given the "InsightUIUX" subsystem and epic "insightuiux-2d-design-system-and-ux-engine-2-8" are initialized
    And ChronicleRAG provenance from "Book_Lit_Master_UI_UX_Engineering.md" is active
    When the product engineer and QA verifier triggers "reactive-4-state-and-validate-on-blur-web-component" with valid parameters
    Then the operation succeeds with deterministic output and appends an EU AI Act Art. 12 SHA-256 receipt

  @negative @unhappy_path @validation
  Scenario: Negative edge case - 4-State Reactive Machine & Validate-on-Blur Web Component (`<insight-uiux>`) rejects malformed or out-of-bounds input
    Given the "InsightUIUX" subsystem and epic "insightuiux-2d-design-system-and-ux-engine-2-8" are initialized
    When the product engineer and QA verifier triggers "reactive-4-state-and-validate-on-blur-web-component" with empty or malformed parameters
    Then the system returns a 400 validation error without mutating state

  @security @pt_eu_compliance @rule_11
  Scenario: Security boundary - 4-State Reactive Machine & Validate-on-Blur Web Component (`<insight-uiux>`) enforces CNPD/GDPR PII scrubbing and blocks injection payloads
    Given the SecurityAuditAgent, InsightAudit (:4009), and Blue-Team guards are active
    When an untrusted caller submits path traversal, prompt injection, or raw PT NIF/IBAN PII to "reactive-4-state-and-validate-on-blur-web-component"
    Then sensitive tokens are scrubbed or blocked and a security audit event is recorded
