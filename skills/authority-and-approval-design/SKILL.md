---
name: authority-and-approval-design
category: operating
maturity: core
---

# Authority & approval design

## Intent

Make it explicit who or what may decide, approve, execute, revise or publish — and bind that authority to the exact artifact/state it applies to.

## Use when

- agents can take consequential actions;
- workflows have review/approval;
- human and machine roles overlap;
- execution is separated from decision-making;
- an approved artifact can later change.

## Core rule

> Presence of data is not authority. Authority is an explicit, current contract over an exact identity/version/action.

## Procedure

1. Separate stages such as proposal, review, approval, execution and publication.
2. Define who may move each boundary.
3. Bind approval to the reviewed version/reference, not only a mutable name.
4. Define whether authority is one-time, reusable, expiring or revocable.
5. Let executors re-check safety/runtime constraints without re-litigating the approved decision.
6. Invalidate or supersede stale authority explicitly when the underlying artifact changes materially.
7. Keep unresolved/unapproved components from riding along with approved ones.
8. Audit who authorized what and what effect consumed the authority.
9. Test unauthorized, stale-version and partial-approval cases.

## Non-negotiables

- A reviewer role alone does not imply every approval is valid.
- Approval of version A does not approve mutated version B.
- An executor must not invent missing authority.
- A later non-authoritative note must not silently reverse an already-finalized effect.
- Publication/release may require a separate authority from internal approval.

## Verification

You can answer:

- Who authorized this?
- Exactly what version/action was authorized?
- Is that authority still current?
- Has it already been consumed?
- Which safety/runtime checks may still block execution?

## Anti-patterns

- boolean `approved=true` on a mutable object with no version binding;
- "manager can do anything" as the only permission model;
- worker re-evaluating business intent after approval;
- partial approval treated as whole-object approval;
- merge automatically implying publish.

## Evidence basis

- Observed across workflow systems, agent execution systems and production/publishing pipelines with explicit human/machine review boundaries.
- Reinforced by invalid-transition, partial-approval, stale-authority and role/capability tests.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
