# ShoStack skills

A ShoStack skill is a **reusable engineering procedure backed by real implementation evidence**.

The public skill must remain useful after proprietary product details are removed.

Read [the disclosure policy](../docs/DISCLOSURE-POLICY.md) before adding or expanding a skill.

## Format

Each skill should answer:

- **Intent** — what capability this represents.
- **Use when** — triggers.
- **Core rule** — the shortest invariant.
- **Procedure** — how to execute it.
- **Non-negotiables** — what must remain true.
- **Verification** — what proves it was done.
- **Anti-patterns** — common tempting failures.
- **Evidence basis** — abstracted classes of implementation evidence, never a proprietary recipe.

## Promotion rules

Do not create a `core` skill because a phrase sounds good.

Promote only when either:

- the behaviour appears in three or more materially different systems; or
- it is an explicit cross-project invariant with executable implementation evidence.

Technology-specific capability may be valuable with one strong implementation; mark it `candidate` or `repeated` rather than inflating it.

## Deep-dive preference

Tests and failure handling often reveal more about engineering style than happy-path architecture.

When mining a source repo, look especially for:

- duplicate/retry behaviour;
- crash/torn-write behaviour;
- invalid transitions;
- permission bypass tests;
- stale/cache behaviour;
- concurrency races;
- degraded dependencies;
- redaction/audit behaviour;
- recovery and reconciliation;
- version/approval binding.

## Design goal

A coding agent that knows nothing about Sho should be able to read one `SKILL.md` and reproduce the engineering behaviour without learning how any proprietary source product is internally built.
