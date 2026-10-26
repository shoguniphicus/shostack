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

## Implementation completed on dev
- Added the canonical `docs/RITES-OF-PASSAGE.md` with nine revisitable rites (R0–R8), epistemic classification, agent question cadence and evidence-based readiness gates.
- Added `docs/FOUNDER-STEERING-PATTERNS.md` documenting the moves: partial idea, knowledge/belief/unknown, rejection, simplify, mock-first, architecture/authority steering, audit, durable planning and release verification.
- Added `skills/idea-to-saas-discovery/SKILL.md` as a **candidate** interviewer capability.
- Added `starter/idea-to-saas/`: user guide, self-contained agent instructions, a conditional 29-area question coverage map, PRODUCT/DECISIONS/NEXT templates, synthetic scenarios, non-destructive initializer and its tests.
- Linked discovery from ShoStack README, starter and skills index, agent read order and the downstream SaaS delivery guide.

## Checks actually performed
1. **Deterministic initializer:** recreated the committed script and test module locally; used stand-in Markdown template contents (including the expected interviewer keyword) to isolate file-creation behavior. `python3 -m unittest discover -s tests -v` on Python **3.13.5**: **5 tests passed** (creation, no overwrite, dry-run, missing workspace, symlink guard).
2. `python3 -m py_compile bootstrap.py tests/test_bootstrap.py`: **passed** on the local mirror.
3. On the GitHub `dev` tree, checked **16 Markdown files** against existing repository paths: **0 broken relative links**.
4. Verified no literal escaped-newline formatting regressions in those documents; all nine rite markers present; 29 areas in the conditional question map; all five bootstrap input templates exist and the initializer uses exclusive file-creation mode.
5. Basic content-level pattern scan of new/revised Markdown found **no private product-repository addresses, access-token shaped values or obvious account credentials**.

## Limits not hidden
- The deterministic tests ran on a script copy with **synthetic stand-in templates**, not a checkout of the exact repository payload, because the execution container had no GitHub network access. They establish the initializer logic only.
- A full LLM conversational evaluation with actual novice founders **has not been run**. The eight synthetic cases define how to perform it; this package is still candidate maturity.
- No live product, website deployment, market validation or paid offering is claimed from documentation + initializer tests.
- Branch merge and any source link publication must be recorded separately when confirmed.

## Next evaluation
Pilot the pack with both a novice and a technically opinionated founder. Evaluate how well it asks high-impact questions, captures corrected assumptions, avoids false certainty and resumes from files. Add measured cases and revise the prompts only in response to observed errors.
