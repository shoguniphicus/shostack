---
name: idea-to-saas-discovery
category: operating
maturity: candidate
description: Progressive founder interview and idea-to-SaaS specification, preserving what is known, believed, unknown, decided and observed. Use before architecture or coding when the user has a vague or changing software idea.
---

# Idea-to-SaaS discovery — the Rites of Passage

## Intent

Help a nontechnical or technically experienced founder shape an initially unclear product through progressive, evidence-aware dialogue. Turn an evolving conversation into durable, revisable product intent **without claiming a one-shot prompt can specify a complex SaaS**.

## Use when

- "I have an idea for an app / SaaS but don't know how to explain it."
- The user is feeding in partial knowledge or frequently steering the product's direction.
- The agent needs to interview stakeholders before architecture/design/code.
- The user says "audit", "what else?", "I disagree", "this is overcomplicated" or "is this a product or just a feature?" during discovery.

Do not use this interviewer as a reason to delay straightforward, already scoped implementation tasks.

## Core rule

> Ask one consequential question at a time; never promote a belief into a fact, a preference into an architectural requirement, a decision into verified evidence, or a plan into running software.

Read [Rites of Passage](../../docs/RITES-OF-PASSAGE.md) before leading the interview. Consult the [question coverage map](../../starter/idea-to-saas/QUESTION-COVERAGE.md) silently and adapt it; it is not a questionnaire to present in full.

## Procedure

1. **Start from their raw idea.** Ask for a moment they wish worked differently, not for a technology stack or a ready PRD. Capture their own words before paraphrasing.
2. **Map epistemic state.** Explicitly distinguish KNOW (reported), THINK (hypothesis), UNKNOWN, DECIDED, OBSERVED and REJECTED/SUPERSEDED; do not invent source evidence.
3. **Identify the current rite (R0–R8).** Note the weakest consequential unknown; choose one useful question or a reversible experiment. Jump forward/back as reality demands.
4. **Interrogate the work and viability.** Find actor, trigger, current workaround, desired outcome, payer/adoption hypothesis, end-to-end journey, handoffs, failure and recovery. Scale question depth to consequence.
5. **Challenge constructively.** Offer alternatives, feature-vs-product tests, conflicting goals or cheap falsifiers; preserve the option the user rejected and why.
6. **Update durable records.** Use PRODUCT.md, DECISIONS.md and NEXT.md. The agent writes and maintains them when file access exists; in chat-only mode, show copy-ready updated text or a concise running summary instead of claiming local files were edited.
7. **Earn a boundary-limited build brief.** State in/out scope, authority/data constraints, at least one demonstrable acceptance path, blocker/deferred decisions and how evidence will be collected.
8. **Handoff, don't abandon.** Link to [SaaS delivery discipline](../saas-delivery-discipline/SKILL.md) for implementation and [working-doc driven development](../working-doc-driven-development/SKILL.md) for auditable execution. Re-enter discovery when new feedback contradicts assumptions.

## Turn-by-turn interaction contract

- **Default:** one clear, high-leverage question per turn, in ordinary language, with a sentence explaining why this question matters when needed.
- **When the user knows:** accept as reported context; seek an example or evidence if the downside of being wrong is high.
- **When the user thinks they know:** name the hypothesis, offer a counterexample or practical test.
- **When the user doesn't know:** offer plausible choices and implications, mark UNKNOWN and avoid forced selection.
- **When the user steers or rejects:** explicitly retain/revise affected choices and record the rejected alternative.
- **When the user wants a huge plan:** give the requested provisional structure with confidence/unknown annotations, not a fake definitive architecture.
- **When the user says build:** determine whether the safe next step is a mock/prototype, contract, or actual implementation; do not silently create production systems or assume permission.
- **When the user asks "what else?":** audit missing domains and prior contradictions instead of starting irrelevant new features.
- **At the end of a discovery session:** state what was clarified, unresolved critical risks, which rite is active and the next question/action. Do not claim all requirements are finished.

## Non-negotiables

- Never bombard a beginner with the whole question bank, unless they expressly ask to see it.
- Do not demand final pricing, UI style, framework or database choices before understanding user/job and present workflow.
- Do not hide unknown users, payment responsibilities, authorization, data ownership or privacy risks behind attractive mockups.
- Do not manufacture user interviews, willingness-to-pay, client metrics, regulatory conclusions or market validation.
- Preserve user decisions and supersession reasons; the agent must not silently override them.
- Do not quote or mirror private client code, internal prompts, confidential architectures or business secrets into public training material.
- An unknown can be responsibly deferred for a reversible test, not for an irreversible release or security-sensitive integration.

## Verification

In a synthetic trial, check that the agent (a) starts with a raw idea rather than a stack, (b) asks a single relevant question, (c) preserves KNOW/THINK/UNKNOWN distinctions, (d) records corrections and supersessions, (e) does not claim demand or production readiness on a mock, and (f) writes a reconstructible next-turn handoff. See [scenario tests](../../starter/idea-to-saas/SCENARIOS.md).

These are **behavioral acceptance criteria**, not a claim that this newly packaged skill has already passed an independent LLM evaluation.

## Anti-patterns

- A thirty-page PRD generated from one sentence with invented users, pricing and architecture.
- Asking 60 unrelated questions in the first response.
- Treating the founder's uncertain guess as a confirmed requirement.
- Over-defending an elegant feature rather than determining if anyone will use or pay for it.
- Returning to a previously rejected choice without noticing it was rejected.
- Declaring all rites completed just because documents have headings.
- Jumping to microservices/agent graphs/queues while the service journey is still unknown.

## Evidence basis

The working discipline is distilled from iterative product-shaping, architecture audits and repeated founder-led course correction across distinct types of software work. The synthesized discovery pack is new, marked **candidate**, and not yet independently benchmarked. Public evidence follows the [disclosure policy](../../docs/DISCLOSURE-POLICY.md).
