# AGENTS.md — ShoStack

ShoStack records **evidence-backed engineering skills**. Treat it as an operating manual, not a marketing page and not a source-code mirror.

## Read order

1. `README.md`
2. `docs/DISCLOSURE-POLICY.md`
3. `docs/EVIDENCE.md`
4. the relevant `skills/<name>/SKILL.md`
5. the newest relevant file under `docs/working/`

## Working rule

Any substantial change to the skill model starts with a dated working record:

`docs/working/YYYY-MM-DD-<slug>.md`

Record scope, evidence inspected, interpretation, changes made and verification. Update it while the work evolves. Preserve refuted assumptions and plan changes rather than reconstructing a clean story at the end.

## Private evidence → public skill rule

Source repositories may contain proprietary implementation. Inspect them to establish evidence, but publish only the transferable engineering behaviour.

Never copy into ShoStack:

- proprietary algorithms, scoring logic or business thresholds;
- internal endpoint/tool inventories or infrastructure topology;
- customer-, brand- or product-specific schemas;
- source code or distinctive implementation snippets;
- private prompts, internal workflow recipes or operational secrets;
- identifiers, credentials, private URLs or account data.

Public evidence should describe the **class of evidence**, not reproduce the implementation.

Before writing, ask:

> If an outsider read this, would they learn the engineering principle — or could they reconstruct how the source product works?

If the latter, abstract further.

## Evidence rule

Do not promote a personal skill from intuition alone.

For every skill:

- separate **observed fact** from **generalized principle**;
- do not infer proficiency merely because a dependency exists;
- prefer behaviour repeated across independent systems;
- use tests and failure handling as stronger evidence than documentation alone;
- keep detailed source paths and implementation facts out of the public skill artifact.

### Maturity

- `candidate`: one convincing implementation;
- `repeated`: two independent systems;
- `core`: three or more materially different systems, or an explicit cross-project invariant with implementation evidence.

A skill may be demoted, split or retired when new evidence shows the abstraction is too broad.

## Skill contract

Every `SKILL.md` should contain:

1. intent;
2. trigger / when to use;
3. core rule;
4. procedure;
5. non-negotiables;
6. verification;
7. anti-patterns;
8. evidence basis (abstracted, disclosure-safe).

Prefer tool-agnostic behaviour. Put framework-specific mechanics only in implementation skills.

## Git discipline

- `main` is reviewed truth.
- Reuse the long-lived `dev` branch for normal ShoStack development.
- Do not force-update `main`.
- Compare `dev` with current `main` before merge.
- Keep commits coherent; documentation and the skill it describes should land together.

## Claim discipline

A package manifest proves a technology is present. It does not, by itself, prove mastery.

Implemented behaviour + tests + operational repetition across projects is stronger evidence.

Write the strongest claim the evidence supports — no stronger.
