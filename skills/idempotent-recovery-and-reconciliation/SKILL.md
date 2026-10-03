---
name: idempotent-recovery-and-reconciliation
category: operating
maturity: core
---

# Idempotent recovery & reconciliation

## Intent

Make retries, restarts and uncertain external effects converge on one correct state instead of duplicating work or re-interpreting authority.

## Use when

- webhooks/events may be delivered more than once;
- jobs can retry after timeout/crash;
- an external side effect may have succeeded even when the caller did not receive confirmation;
- workers restart with in-flight work;
- state must be reconciled against an external system.

## Core rule

> A repeated request should either return the same logical result or fail explicitly because its meaning conflicts — never silently create a second effect.

## Procedure

1. Give the logical action a stable identity or idempotency key.
2. Separate **intent recorded** from **effect observed**.
3. On retry, look up prior intent/effect before creating anything new.
4. Treat same key + different meaning as a conflict, not a duplicate.
5. Reconcile uncertain effects from authoritative external state where possible.
6. Make recovery transitions explicit and bounded.
7. Record duplicate prevention, reconciliation and recovery as observable events.
8. Consume or supersede one-time authority after the effect it authorized is final.
9. Test restart, duplicate delivery, timeout-after-success and partial-progress cases.

## Non-negotiables

- Idempotency cannot be based only on timing.
- Retry must not reopen a settled decision.
- Reconciliation discovers state; it does not invent new authority.
- Duplicate prevention must survive process restarts when the side effect matters.
- A conflict on the same key must fail loudly.

## Verification

Prove:

- duplicate requests do not duplicate effects;
- same key with changed semantics is rejected;
- uncertain submissions can be reconciled;
- restart preserves enough identity to resume safely;
- final state remains stable under repeated reconciliation.

## Anti-patterns

- "retry and hope";
- generating a fresh ID for every attempt;
- treating timeout as proof nothing happened;
- using an in-memory dedup set for durable side effects;
- recovery that silently changes the original decision.

## Evidence basis

- Repeated across workflow ingestion, external-effect execution and multi-agent systems with stable source identity, durable idempotency and reconciliation.
- Reinforced by duplicate-delivery, restart and conflicting-idempotency tests.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
