---
name: failure-oriented-testing
category: operating
maturity: core
---

# Failure-oriented testing

## Intent

Test the invariant by deliberately recreating the ways it can fail, not merely by proving the happy path once.

## Use when

- fixing a production incident;
- adding authorization or guardrails;
- changing persistence;
- handling concurrency, caching or retries;
- repairing an architectural bypass.

## Core rule

> A regression test should kill the old bug or the refuted design.

## Procedure

1. State the property under test in plain language.
2. Identify the exact pre-fix behaviour that violated it.
3. Build a test that would fail on that behaviour.
4. Inject failure at a neutral/shared seam where possible.
5. Add adversarial cases: duplicate, corrupt, stale, concurrent, unauthorized, partial.
6. Add preservation controls proving legitimate behaviour still works.
7. Prefer end-to-end coverage when the bug crossed layers.
8. Keep the test after the incident; it is now executable institutional memory.
9. When a bug class had multiple bypasses, add a class-level regression sweep.

## Non-negotiables

- A test passing on both buggy and fixed code is not proof of the fix.
- Do not mock away the layer where the bug actually lived.
- Security tests should try the bypass, not only the expected authorized request.
- Fault tests must leave the test environment isolated/hermetic.

## Verification

A good fix can answer:

- What old behaviour does this test fail on?
- What legitimate control still passes?
- Which failure classes are covered?
- Does an integration/E2E test cover the cross-layer path if needed?

## Anti-patterns

- adding only a happy-path test after a failure incident;
- asserting implementation details instead of the property;
- using a fault injector that only the new code calls;
- removing regression tests because the implementation was refactored;
- calling a mocked unit test "end-to-end."

## Evidence basis

- Repeated across security, persistence, workflow, agent and content-production systems.
- Observed techniques include corruption fixtures, mid-write fault injection, concurrency races, mutation/bypass tests and real-path integration tests.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
