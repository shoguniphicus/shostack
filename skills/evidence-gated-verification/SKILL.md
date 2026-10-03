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

## Evidence

- `zennith-os/skills/git-discipline/SKILL.md` — hook reachability tested by execution.
- `zennith-os/skills/zen-ci/SKILL.md` — executable local CI and audited bypass.
- `agencyos/docs/working/2026-08-21-p0-headless-hardening-final-audit.md` — explicitly refuses to claim green CI before a run.
- `alamakfarm/docs/WORKFLOW.md` — visual/publishing gates require actual source pixels and explicit pass.
