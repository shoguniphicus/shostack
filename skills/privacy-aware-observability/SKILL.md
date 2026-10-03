---
name: privacy-aware-observability
category: operating
maturity: core
---

# Privacy-aware observability

## Intent

Keep enough telemetry to explain what happened without turning logs or audits into a second leak of secrets or private payloads.

## Use when

- recording agent/API calls;
- logging workflow inputs;
- auditing authentication/authorization;
- storing execution receipts;
- debugging sensitive or proprietary inputs.

## Core rule

> Preserve diagnostic structure and identity; redact sensitive content at the audit boundary.

## Procedure

1. Define which fields/payload paths are sensitive.
2. Redact before persistence, not only at display time.
3. Preserve safe metadata useful for diagnosis: hash, length, type, timestamp, actor, action, status.
4. Never store raw credentials/tokens when a one-way representation is sufficient.
5. Keep redaction separate from the live in-memory request/state so observability does not mutate execution.
6. Redact nested structures recursively where needed.
7. Ensure error/denial responses do not leak secret values or secret-storage locations.
8. Audit both successful and failed consequential actions.
9. Test that sensitive strings are absent from persisted and returned audit material.

## Non-negotiables

- Secrets in URLs/query strings are especially risky.
- "Internal log" is not a reason to store raw credentials.
- Redaction must happen before durable write.
- Hashes/lengths may aid correlation but must not become reversible substitutes for secret storage.
- Auditing should not alter the action being audited.

## Verification

Use sentinel secrets and assert they do not appear in:

- audit records;
- event logs;
- error responses;
- exported diagnostics.

Also verify non-sensitive fields remain available for debugging.

## Anti-patterns

- logging the whole request and "cleaning it later";
- hiding sensitive fields only in the UI;
- storing raw token plus a hash;
- removing so much context that the audit cannot explain the event;
- redaction logic that mutates live state.

## Evidence basis

- Observed across authenticated agent surfaces and workflow/execution audit systems.
- Reinforced by recursive-redaction, raw-token-absence and denial-no-leak tests.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
