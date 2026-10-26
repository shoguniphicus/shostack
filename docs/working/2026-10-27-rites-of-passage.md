# 2026-10-27 — Rites of Passage: progressive idea-to-SaaS discovery

## Why this is being built
ShoStack presently starts most visibly at repository reality and engineering execution. A new user may have an idea but lack the vocabulary or facts to specify a product to a coding agent. The requested capability is an **agent-led product discovery harness** that helps such users discover and steer the product through small, earned transitions rather than pretending to "one-shot" a sophisticated SaaS.

## Source evidence inspected
- Current ShoStack `main` and `dev` initially aligned at `0229b987d744c41349d2db94cd38d287f089ab7d`.
- Existing ShoStack skills: reality-first repo reading, working-doc-driven development, contract-first boundaries, evidence-gated verification, bounded/reversible change, SaaS delivery discipline.
- Existing `starter/` is execution-oriented; no upstream nontechnical discovery pack is present.
- Across prior product-shaping discussions the observed steering pattern is incremental: state what is known or believed, challenge architecture/assumptions, revise technical ownership, select mock-first verification, and promote decisions into written contracts. A rejected integration approach or excessive abstraction may require returning to earlier questions.
- These patterns are **methodological observations**, not proof of measured uplift or an independently validated packaged interviewing product.

## Design requirements
1. Begin with a messy, unstructured idea; never require software vocabulary.
2. Respect **I know / I think I know / I don't know**, plus explicit decisions and observed evidence. Do not silently turn hypotheses into truth.
3. Ask **one highest-value question per turn by default**. Exhaustive means eventually covering material risk, not an exhaustive upfront questionnaire.
4. Maintain durable product truth, open uncertainty and decision provenance; summarize and allow `I disagree` as first-class steering.
5. Define meaningful rites of passage with entry/exit criteria; permit loops/backtracking without suggesting everything is complete.
6. Distinguish market hypothesis, technical preference, user requirement, authority and security/privacy issues.
7. Allow **reversible mock/concierge proof before full specification**, and don't claim release-readiness from an impressive document.
8. Produce an easy-to-install text pack usable by humans and coding agents with no proprietary dependencies or secrets.
9. Scope: ShoStack repository docs, skill, starter, deterministic non-destructive initialization and tests; no client-source disclosures or sales claims.

## Proposed structure
- `docs/RITES-OF-PASSAGE.md` — canonical product-discovery method, transitions and truthful readiness.
- `skills/idea-to-saas-discovery/SKILL.md` — agent protocol that activates the method.
- `starter/idea-to-saas/` — clear entrypoint, instructions, question coverage, synthetic example and compact templates.
- `starter/idea-to-saas/bootstrap.py` — opt-in safe initializer (will not overwrite workspace state).
- `starter/idea-to-saas/tests/` — deterministic initializer checks.
- Cross-links from ShoStack README, skill index and starter index.

## Test scenarios
- Vague idea with no tech vocabulary starts in exploration, not stack selection.
- Confidence and hypothesis classifications remain distinguishable.
- User corrections supersede earlier decisions with a reason; no silent drift.
- "I don't know" is recorded and answered with options, not invented certainty.
- "Build it all" yields an explicit bounded proof and blocker list, not a production guarantee.
- Bootstrap does not overwrite existing product records; repeat invocation is safe.
- New relative Markdown links resolve, policy prevents leaking proprietary client material.

## Truthful gates
- A staged `Product Brief` does not prove market desirability.
- A user-decided technical direction does not prove system implementation.
- Passing a deterministic initializer test does not prove LLM interviewing quality.
- Public source changes are distinct from merge, install, live rollout and independent usability evaluation.

## Execution status
Planning and evidence recorded before creating the method/pack. Record exact checks, changed files, release SHA and remaining gaps after implementation.
