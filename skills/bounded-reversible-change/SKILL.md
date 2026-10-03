---
name: bounded-reversible-change
category: operating
maturity: core
---

# Bounded reversible change

## Intent

Keep moving under uncertainty without taking an unnecessarily large or irreversible bet.

## Use when

- requirements are incomplete;
- architecture has risk;
- a production fix is urgent;
- an agent must act with partial evidence;
- a project risks scope explosion.

## Core rule

> Uncertainty should usually shrink the action or its blast radius before it stops action entirely.

## Procedure

1. Identify hard blockers separately from ordinary uncertainty.
2. Choose the smallest coherent change that can produce useful evidence.
3. Keep it reversible: branch, version, feature boundary, small phase, guarded rollout, or explicit fallback.
4. Name what is deliberately deferred.
5. Re-evaluate after evidence arrives.
6. Escalate size only when prior gates pass.

## Non-negotiables

- Safety-critical missing information can block.
- Ordinary uncertainty is not a license for endless analysis.
- A "small" change must still be coherent; do not scatter unrelated patches.
- Filled/committed state is not silently undone merely to make paperwork consistent.

## Verification

The working record states:

- the bounded scope;
- hard blockers;
- fallback/reversal path;
- explicit deferrals;
- evidence required for the next expansion.

## Anti-patterns

- all-or-nothing redesign;
- "monitor" with no trigger or expiry;
- widening P0 because adjacent improvements are tempting;
- destructive cleanup when a narrower correction suffices.

## Evidence

- `piggybankos/memory/ACTION-DECISION-CONTRACT.md` — smaller reversible action under uncertainty.
- `agencyos/docs/working/2026-08-21-p0-headless-hardening-final-audit.md` — explicit P1 deferrals and narrow correction.
- `altechcamera/docs/working/2026-10-03/public-mcp-discovery-matchmaking-audit.md` — deliberately small Phase 1 public surface.
- `alamakfarm/docs/BRANCHING.md` — coherent temporary branches and safe merge.
