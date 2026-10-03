---
name: guardrails-as-code
category: operating
maturity: core
---

# Guardrails as code

## Intent

Turn a recurring costly failure into an executable prevention or detection mechanism.

## Use when

- the same mistake has happened more than once;
- a rule is important enough that "remember this" is inadequate;
- agent concurrency increases accidental-risk surface;
- merge/deploy correctness depends on an invariant.

## Core rule

> If a rule matters repeatedly, move it from prose toward an executable wall.

## Procedure

1. Describe the failure class, not just the latest incident.
2. Choose the earliest reliable interception point.
3. Encode a narrow guard that blocks the dangerous case without wedging legitimate work.
4. Add a smoke/adversarial test.
5. Install/wire the guard at the actual execution point.
6. Verify reachability, not just file presence.
7. Provide a deliberate audited escape for legitimate exceptional work where appropriate.
8. Add recovery/detection when no preventive wall can be absolute.

## Non-negotiables

- Guard the invariant, not a filename coincidence.
- Fail-open vs fail-closed must be deliberate and documented.
- A bypass should not silently erase auditability.
- A hook that exists but never executes is not a guard.

## Verification

- the bad case is reproducibly blocked/detected;
- the normal case still works;
- installation/reachability is tested;
- bypass/recovery semantics are known.

## Anti-patterns

- adding another warning paragraph after each incident;
- broad checks that fail unrelated contributors;
- brittle grep-based "installed" checks;
- guard logic duplicated in many places.

## Evidence

- `zennith-os/skills/git-discipline/SKILL.md` — branch, push, tree-collapse, ontology and sentinel walls.
- `zennith-os/skills/zen-ci/SKILL.md` — pre-push local CI and path-scoped state checks.
- `altechcamera/AGENTS.md` — validator/apply-path contract and normalized agent errors.
- `alamakfarm/docs/WORKFLOW.md` — mandatory visual-fidelity and source-lock gates.
