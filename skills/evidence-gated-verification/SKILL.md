---
name: evidence-gated-verification
category: operating
maturity: core
---

# Evidence-gated verification

## Intent

Make completion claims only when the relevant execution path has actually been checked.

## Use when

- merging;
- declaring a migration complete;
- changing a validator, contract or security boundary;
- debugging guardrails;
- reporting "green", "fixed", "safe", or "not present."

## Core rule

> Verify the thing that runs, not merely the thing that looks correct.

## Procedure

1. Identify the claim to prove.
2. Identify the real execution path behind that claim.
3. Choose the smallest check that exercises that path directly.
4. Test important negative/failure cases.
5. Record limits: what was not executed or cannot yet be claimed.
6. Keep evidence with the working record, test, receipt or audit.
7. Do not upgrade conditional evidence into a definitive claim.

## Non-negotiables

- Presence is not reachability.
- A static check is not runtime evidence when runtime behaviour matters.
- No green CI claim without a run.
- Failure gates should distinguish "absent" from "broken" where availability matters.

## Verification

The evidence is reproducible and names:

- command/test;
- relevant input/ref;
- observed output;
- limitation or remaining conditional gate.

## Anti-patterns

- grep says hook exists → declaring guard active;
- docs say tool exists → declaring MCP callable;
- code compiles → declaring integration validated;
- "should work" presented as passed verification.

## Deep-dive heuristics

- Prefer a test that would have failed on the old bug; a test passing on both versions is usually only a preservation control.
- Inject failure at a seam shared by old and new implementations when possible, so the test is not biased toward the fix.
- Test corruption, duplication, stale state, concurrency and authorization bypasses in addition to happy paths.
- Keep controls that prove legitimate behaviour still works after the guard or fix is added.
- Surface partial coverage honestly; "some sources healthy" is not the same claim as "complete."

## Evidence basis

- Observed across systems that test runtime reachability, real integration paths, fault injection and negative cases before making completion claims.
- Reinforced by tests explicitly designed to fail on the pre-fix behaviour and pass only after the invariant is restored.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
