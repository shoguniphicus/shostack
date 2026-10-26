# Founder steering patterns — how the product emerges through conversation

> This is the part of ShoStack that a one-shot app prompt cannot reproduce: **the founder's growing understanding and the agent's ability to preserve, challenge and respond to that understanding**.

This document distils the public, transferable **conversation pattern** used when shaping real software and services. It does not reproduce private client prompts, repositories, system designs or customer data. It complements [the Rites of Passage](RITES-OF-PASSAGE.md).

## Two kinds of steering

**Founder steering:** I know this operational constraint; I believe this user behaviour; I don't know if the business model works; I reject this complexity; this feature is not the product; I choose this first step.

**Agent steering:** Here are the assumptions behind your idea; this question will change our design most; here are two simpler explanations; this decision contradicts an earlier one; this is safe to mock but not safe to release; this evidence is still missing.

Both should be visible. A capable agent must neither obey every uncertain guess as truth nor override a clear owner decision with its own preferred architecture.

## The observed conversational moves — made reusable

| Founder's move | What it communicates | What the agent should do | What to record |
| --- | --- | --- | --- |
| **"I want to build something like..."** | Outcome/reference, not a requirement to copy source or behavior. | Ask which job and experience matters; distinguish inspiration from literal replication. | Raw intent and open scope. |
| **"What does the user actually send/do?"** | Missing real-world journey. | Walk input → ownership → decisions → output → recovery in concrete terms. | Journey and assumptions. |
| **"I think the flow works this way."** | Provisional theory. | Label THINK, look for contradiction and cheap falsifier. | Hypothesis, impact if wrong, test. |
| **"I don't know how that works."** | Legitimate knowledge gap. | Explain options in plain language without silently choosing one. | UNKNOWN, owner, next learning step. |
| **"Why is this so complicated? Keep it simple."** | Complexity is exceeding demonstrated need. | Name what can be removed and what risk that removal creates; retain essential boundaries. | Rejected abstraction, replacement and cost. |
| **"Is this a feature or a product?"** | Commercial viability challenge. | Test who pays, existing alternatives, input friction, repeat usage and switching costs. | Revised proposition or the decision not to build. |
| **"Audit. What did we miss? What else?"** | Request for adversarial review, not praise. | Identify ambiguity, contradictory assumptions, hidden operational work and missing proof. | Issues and rank by consequence. |
| **"Use mock data first."** | Want experience/contract learning before expensive integration. | Separate mock UX, validated contracts and real provider/payment/storage work; state what a mock cannot prove. | Explicit maturity boundary. |
| **"Architecture and services matter more than screens."** | Priority correction. | Reorder plan around authoritative state, workflows and interfaces before polishing UI. | Revised dependency order. |
| **"Record the plan with details."** | Conversation needs durability beyond this chat. | Maintain product and decision records; don't reconstruct fake decisions later. | Dated decision and next checkpoint. |
| **"Do it, one huge step at a time."** | Wants meaningful progress with bounded control. | Ship one coherent thin vertical with tests, not scattered branches and speculative features. | Scope, acceptance and handoff. |
| **"I disagree / don't do it that way."** | Clear rejection/supersession. | Stop defending the old plan; reconcile affected decisions and the new truth. | Original option marked superseded with why. |
| **"Merge and verify."** | Distinguish proposed work from real delivery. | Check ref, tests and runtime separately; avoid asserting live success from source alone. | Evidence and actual released status. |

A founder may alternate among these moves multiple times in a single product. **Discovery is spiral, not linear.** Each pass should reduce consequential uncertainty or make a reversible test possible.

## What the agent must learn about the founder, not just the product

- **What they know first-hand:** work processes, relationships, constraints and observed failures.
- **What they believe might be true:** market demand, technical feasibility, pricing and user habits.
- **What they don't yet know:** hidden handoffs, payment willingness, legal permissions, operational costs or edge cases.
- **What is non-negotiable:** their authorized product direction, preferred simplicity, capability boundaries and acceptable costs.
- **What changes their mind:** counterexamples, evidence, working prototypes, operator pain or a clearer way to solve the same problem.

Do not turn someone else's opinions into a fabricated founder decision. Do not make the founder answer architecture questions merely because an agent likes system design.

## An illustrative evolution (synthetic, not from client files)

1. "I want an app that helps people sign up for community classes." **Raw idea**, not specification.
2. "I know teachers currently chase confirmations in messages." **KNOW / reported**; request a concrete example.
3. "I think parents will pay monthly." **THINK**; explore buying alternatives and adoption friction.
4. "Actually parents won't make accounts; teachers need a simple record." **REJECTED** account-heavy approach; record the new actor/journey.
5. "I don't know if this can stand alone from existing class software." **UNKNOWN**; test feature versus product rather than invent a differentiator.
6. "Let's mock one booking/confirmation flow." **DECIDED** reversible scope; retain market uncertainty.
7. "The mock was usable but didn't prove demand." **OBSERVED** only if actual tested evidence exists, otherwise record as a proposed evaluation.
8. "Now design the backend so confirmations have one owner." An architecture question is earned after a known journey; contract verification becomes the next gate.

No single message contained the final SaaS. The value was in preserving each correction until the smaller product became clear.

## Four checkpoints that prevent false certainty

**After the first idea:** Can we repeat the user's actual problem without inventing features?

**After a challenge:** Can the founder see which claims are knowledge, hypotheses or unknowns, and why one counterexample matters?

**Before implementation:** Can an independent engineer reconstruct one actor's end-to-end journey, boundaries, first slice and acceptance — with explicit unknowns?

**After a delivered slice:** Is there observed test or user evidence, a recorded change decision and a safe continuation plan?

If not, return to the appropriate rite. A decision to stop or radically simplify is a successful discovery outcome.

## Why "one shot" does not work for complex SaaS

A prompt can generate screens, scaffolding and plausible defaults, but it cannot magically know how an organization operates, what its users will adopt, who may perform consequential actions, what data can be used, whether somebody pays, or what will fail in production.

ShoStack's answer is not to ban fast prototypes. It is to **label them honestly and convert what they teach into the next decision**. A prototype may be one-shot; the discovery and operation of a serious product are not.

The related starter is in [Idea-to-SaaS](../starter/idea-to-saas/README.md), and the engineering continuation is [SaaS delivery discipline](SAAS-DELIVERY-SYSTEM.md).
