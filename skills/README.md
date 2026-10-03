# ShoStack skills

A ShoStack skill is a **reusable engineering procedure backed by repository evidence**.

## Format

Each skill should answer:

- **Intent** — what capability this represents.
- **Use when** — triggers.
- **Core rule** — the shortest invariant.
- **Procedure** — how to execute it.
- **Non-negotiables** — what must remain true.
- **Verification** — what proves it was done.
- **Anti-patterns** — common tempting failures.
- **Evidence** — representative repository paths.
- **Maturity** — candidate / repeated / core.

## Promotion rules

Do not create a `core` skill because a phrase sounds good.

Promote only when either:

- the behaviour appears in three or more materially different systems; or
- it is an explicit cross-project operating convention with implementation evidence.

Technology-specific capability may be valuable with one strong implementation; mark it `candidate` or `repeated` rather than inflating it.

## Design goal

A coding agent that knows nothing about Sho should be able to read one `SKILL.md` and reproduce the behaviour without needing the original conversation that created it.
