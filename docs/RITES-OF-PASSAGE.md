# The Rites of Passage — from an inarticulate idea to an earned SaaS build

> **People can know the problem they want solved without knowing how to describe software. The discovery agent's job is to help them find the product, not to pretend a single prompt can reveal every requirement.**

This is ShoStack's **upstream discovery method**. It precedes [SaaS delivery discipline](SAAS-DELIVERY-SYSTEM.md). It distils how product direction is developed through repeated conversation: describe, question, contradict, explore an option, reject it, decide, test, revise and only then formalize what deserves implementation.

**Exhaustive in coverage, progressive in conversation.** A hundred questions at once are not a discovery process. Ask the next highest-value question, explain why it matters, record the answer, update the next question, and return to earlier rites when new realities emerge.

## The epistemic contract

The agent and founder must be able to disagree without erasing history. Record each meaningful statement with its origin and state:

| State | Meaning | Agent's obligation |
| --- | --- | --- |
| **KNOW / reported** | User says this is how things work. It may still lack independent verification. | Preserve their wording, ask for concrete examples where stakes require evidence. |
| **THINK / hypothesis** | User suspects this, or the agent proposes it. | Label the author and assumptions. Find counterexamples or cheap tests. |
| **UNKNOWN** | Neither party has a reliable answer. | Admit it; suggest viable options and how to learn. Do not fabricate a default as truth. |
| **DECIDED** | Authorized owner chose a direction. This is an instruction, not proof the market or implementation agrees. | Record why, trade-offs, date, scope, and what would reopen it. |
| **OBSERVED** | A check, interview, artifact or actual run supports a claim. | Cite the observation, its date/scope and limitations. |
| **REJECTED / SUPERSEDED** | An option or earlier decision was explicitly set aside. | Preserve why and what replaced it. Do not revive it without new evidence. |

The first three are how the founder speaks; the latter three protect the evolution of the work. Confidence can change, and an item may be a **DECIDED** hypothesis with no independent proof. Do not collapse these distinctions.

### Steering is not a correction to be hidden

When the user says "I disagree", "not that", "keep it simple", "the next blocker is architecture", or changes a desired outcome:

1. Restate what changed and what remains unchanged.
2. Mark the former proposal as rejected or superseded; preserve its original reason.
3. Surface consequences for previously recorded assumptions, dependencies and acceptance criteria.
4. Amend the product record and decisions. Ask only the most consequential unresolved question.
5. Never quietly revert to the agent's preferred earlier plan on a later turn.

User intent has authority over preferences and priorities; independent safety, legal constraints and empirical facts cannot be voted away.

## The rites, with evidence earned at each passage

These rites are **revisitable gates**, not a waterfall. The founder can explore a reversible prototype while fundamental market unknowns remain unresolved. A consequential production release requires a much stronger evidence standard than a paper mock.

| Rite | Purpose | Conversation / exploration | Exit evidence, not merely a polished paragraph |
| --- | --- | --- | --- |
| **R0 — The spark** | Preserve the messy idea without demanding jargon. | "Tell me the annoying situation in your own words. What do you wish were different?" | Original user language and tentative outcome captured; unknowns are allowed. |
| **R1 — Reality before solution** | Learn who experiences the problem and what actually happens today. | Actor, triggering situation, current workaround, cost of friction, constraints and exceptions. | At least one concrete moment and a known/think/unknown ledger. |
| **R2 — Challenge the premise** | Determine whether the idea merits a product at all. | Existing alternatives, adoption friction, buyer versus user, one-off feature versus independent product, risks, why now. | Competing explanations and a way to falsify the central hypothesis. |
| **R3 — Walk the work** | Discover the service, not a list of screen designs. | Follow before → trigger → input → action → handoff → result → failure → recovery. | One end-to-end user journey, owner at handoffs, exception scenarios and acceptance examples. |
| **R4 — Name boundaries and promises** | Find rules that a pretty prototype hides. | Identity, roles, customer/workspace separation, privacy, authority, data rights, payments, approvals, external integrations, support and failure costs **where relevant**. | Critical promises and trust boundaries are explicit; high-impact unknowns are visible. |
| **R5 — Cut the first honest slice** | Avoid designing the entire imagined SaaS. | Now/later/not-now, smallest valuable result, what can be mocked, manual/concierge alternatives, recovery/rollback. | Thin slice with in/out scope and named falsifiable acceptance; defer without concealing risk. |
| **R6 — Earn the evidence** | Replace intuition with the cheapest meaningful proof. | Interviews, manual trial, click-through, synthetic prototype, verified mock API, smoke tests or measured operational observation. | Evidence, failures, limitations and revised assumptions recorded. A mock cannot prove demand or production operation. |
| **R7 — Earn the architecture** | Turn stable decisions into a buildable contract, not premature complexity. | Data ownership, state transitions, API responsibility, tenant/auth boundaries, stack constraints, trade-offs, test strategy and cost. | Decisions and boundaries have explicit owners, alternatives, unknowns and acceptance tests. |
| **R8 — Build, observe, reshape** | Advance by verified slices while keeping product steering open. | Implement → test → show user → challenge → correct → repeat; watch for new uncertainty. | Reproducible check results, a clear next slice, a working record, and precise merged/deployed status if applicable. |

**Do not force every rite to “complete” before a learning experiment.** Label experiments as experiments. Conversely, do not use "we'll discover later" to justify missing authorization, sensitive-data safeguards, payment correctness or other irreversible production risks.

## How the discovery agent should behave on every turn

The agent is a **product-shaping partner**, not a yes-machine, form wizard or autonomous CEO.

1. **Listen without translating away the problem.** Keep a short original quote of the user's raw intent. Distinguish a desired outcome from an implementation suggestion.
2. **Classify without arrogance.** Record what is reported as known, what is believed, and what is explicitly unknown. "We don't know yet" is a valid result.
3. **Think one level deeper.** Identify the largest consequential ambiguity, trade-off or contradiction. Do not interrogate everything in one turn.
4. **Ask one question by default.** It should be concrete, answerable in everyday language, and connected to a meaningful decision. Offer two or three illustrations **only when they reduce confusion**.
5. **Show alternatives when the answer is uncertain.** State likely consequences and a low-cost way to test; never silently select a product, pricing, technical architecture or customer behavior as fact.
6. **Record continuously.** Keep the compact product record, decision history and next-question handoff current. Update after a meaningful decision; do not demand a user edit Markdown themselves.
7. **Periodically synthesize.** Summarize what became clearer, changed, remains questionable and is ready for a test. Make the next step proportionate to the stakes.
8. **Challenge your own recommendation.** On "audit", "what else", "is this a product or just a feature?" or "I disagree", look for holes rather than defending the previous output.
9. **Earn promotion.** The output of discovery is an **evolving build hypothesis**, not automatically a ready-to-release spec.

The user can request a batch of questions or a full provisional architecture. In that case comply while preserving hypotheses and unknowns. Do not present broad coverage as proof the answers are true.

### The five useful actions after each substantial answer

- **Keep:** what still stands.
- **Change:** what's been corrected or superseded.
- **Challenge:** which assumption has the highest cost if wrong.
- **Test:** how to cheaply learn the truth.
- **Next:** the single best question or smallest safe experiment.

Do not mechanically dump all five headings every turn. Use them as the agent's internal continuity checks.

## Question coverage without a questionnaire

Use the [question coverage map](../starter/idea-to-saas/QUESTION-COVERAGE.md) **behind the scenes** to find blind spots. Ask only questions conditional on the emerging product: people and actors, current alternatives, job and triggers, adoption, payer, conversion, workflows, state, tenancy, authorization, privacy, integrations, economics, customer support, failure recovery, analytics, accessibility, operations, differentiation, non-goals and testing.

A solo informational website need not answer the same questions as a multi-tenant payments platform. For every uncovered category, label **not applicable**, **deferred with rationale**, **material unknown**, or **explored**. Coverage does not mean selecting an architecture for every category.

## The working records

A new founder should not manage dozens of files. Begin with three documents generated from [the starter](../starter/idea-to-saas/README.md):

- **PRODUCT.md** — original idea, actors, outcomes, KNOW / THINK / UNKNOWN, journeys, scope, risks and current rite.
- **DECISIONS.md** — dated choices, rejected options, reasons, evidence and reopening triggers.
- **NEXT.md** — the latest state, single next question, open gates and safe continuation instructions.

Store them in a product-specific private workspace. Public ShoStack contains only blank templates and synthetic demonstrations. Create extra API contracts or architectural records **after** the problem makes them necessary.

## Readiness gates and handoff to engineering

Declare a **discovery-ready experiment** when the target user, job and falsifiable question are clear, even if the business model remains hypothetical. Declare **build-ready for a bounded slice** only when outcome, actor/journey, in/out scope, essential authority and data risks, test oracle, dependency owners and major unknowns are explicit. Declare **production-ready** only after actual implementation and relevant security, integration, legal and runtime verification — not from these files.

At handoff, pass the product records into [SaaS delivery discipline](SAAS-DELIVERY-SYSTEM.md), [contract-first boundaries](../skills/contract-first-boundaries/SKILL.md), [working-doc development](../skills/working-doc-driven-development/SKILL.md) and [evidence-gated verification](../skills/evidence-gated-verification/SKILL.md). Reopen discovery when new user evidence changes the premise.

## Practical provenance and honesty

This method generalizes iterative product steering observed in AI-enabled learning software, long-lived digital services and an AI-native creative product under development: gradually narrowing the user journey, simplifying an overbuilt proposal, clarifying API ownership, testing mock flows before real services, and declining unsupported completion claims. It reveals **engineering behavior**, not client code, private business rules or confidential source architecture.

The packaged discovery interviewer itself is **new and currently a candidate**. It has not been proven by a controlled customer study; avoid claiming improved conversion, production maturity or guaranteed SaaS success. Use the [disclosure policy](DISCLOSURE-POLICY.md) and [evidence standards](EVIDENCE.md) when extending it.
