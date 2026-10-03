# Initial ShoStack skill distillation — Progress Log (2026-10-03)

## Scope & objectives

- Inspect the first five source repositories supplied by Sho.
- Distill repeated engineering behaviour rather than produce a technology résumé.
- Seed `shostack` with portable, evidence-backed skill contracts.
- Keep technology inventory separate from behavioural skill claims.

## Repositories inspected

- `shoguniphicus/altechcamera`
- `shoguniphicus/piggybankos`
- `shoguniphicus/agencyos`
- `shoguniphicus/zennith-os`
- `shoguniphicus/alamakfarm`

## Evidence inspected

Representative surfaces included:

- repo roots and recent commits;
- `AGENTS.md` / README operating instructions;
- `docs/working/` structures and selected audits;
- Altech public MCP audit;
- Agency P0 final hardening audit;
- Piggybank action-decision contract;
- Zennith builder / git-discipline / zen-ci patterns;
- Alamak Farm workflow and branching rules;
- Composer, npm and Python package manifests.

See `docs/EVIDENCE.md` for path-level details.

## Interpretation

The strongest repeated pattern is not one framework. It is a process:

`inspect → establish truth → contract → working record → canonical implementation → verify → promote → compound`.

This appears in commerce, agency workflow, investing/quant automation, creative production, and a large AI marketing OS.

## Initial core skills

1. reality-first repo reading;
2. working-doc-driven development;
3. canonical chokepoints;
4. contract-first boundaries;
5. bounded reversible change;
6. evidence-gated verification;
7. agent-native system design;
8. guardrails as code;
9. provenance and promotion;
10. compound engineering.

## Important restraint

A dependency in `composer.json`, `package.json`, or `pyproject.toml` proves presence/use in a project. It does not alone justify a mastery claim. Framework evidence is recorded separately and will be strengthened with production-code/test examples in later passes.

## Validation

- Every initial skill has evidence from at least two repositories.
- Core abstractions were preferred only where the behaviour repeats across materially different domains.
- Repo-specific rules remain cited as evidence rather than being copied blindly into universal procedure.
- `main` remains untouched while this first pass is developed on reusable `dev`.
