# AGENTS.md — ShoStack

ShoStack records **evidence-backed engineering skills**. Treat it as an operating manual, not a marketing page.

## Read order

1. `README.md`
2. `docs/EVIDENCE.md`
3. the relevant `skills/<name>/SKILL.md`
4. the newest relevant file under `docs/working/`

## Working rule

Any substantial change to the skill model starts with a dated working record:

`docs/working/YYYY-MM-DD-<slug>.md`

Record scope, evidence inspected, interpretation, changes made, and verification. Update it while the work evolves; do not reconstruct a perfect story at the end.

## Evidence rule

Do not promote a personal skill from intuition alone.

For every skill:

- cite representative repository paths;
- separate **observed fact** from **generalized principle**;
- do not infer proficiency merely because a dependency exists;
- prefer behaviour repeated across independent projects;
- keep repo-specific policies in the evidence section unless they generalize cleanly.

### Maturity

- `candidate`: one convincing repo / implementation;
- `repeated`: two independent projects;
- `core`: three or more materially different systems, or an explicit cross-project convention with implementation evidence.

A skill may be demoted or split when new evidence shows the abstraction is too broad.

## Skill contract

Every `SKILL.md` should contain:

1. intent;
2. trigger / when to use;
3. core rule;
4. procedure;
5. non-negotiables;
6. verification;
7. anti-patterns;
8. evidence.

Prefer tool-agnostic behaviour. Put framework-specific mechanics in implementation skills.

## Git discipline

- `main` is reviewed truth.
- Reuse the long-lived `dev` branch for normal ShoStack development.
- Do not force-update `main`.
- Compare `dev` with current `main` before merge.
- Keep commits coherent; documentation and the skill it describes should land together.

## Claim discipline

A package manifest proves a technology is present. It does not, by itself, prove mastery.

A working record + architecture + tests + repeated implementation across projects is stronger evidence.

Write the strongest claim the evidence supports — no stronger.
