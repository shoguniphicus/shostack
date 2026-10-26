# ShoStack

> **How you do anything is how you do everything.**

ShoStack is a public, evidence-backed record of **how Sho builds**: repeatable engineering methods that remain useful across stacks, products and AI coding environments.

It is deliberately **not** a mirror of source repositories. Private or proprietary implementation may be inspected to prove a skill exists, then abstracted away. ShoStack publishes the method, not the product recipe.

See [the disclosure policy](docs/DISCLOSURE-POLICY.md).

## Start before coding: the Rites of Passage

**Have an idea but cannot yet explain the whole product?** Start with the [Idea-to-SaaS discovery pack](starter/idea-to-saas/README.md), not a giant one-shot specification. The agent asks progressive, context-aware questions, distinguishes what you know / think / do not know, records changed decisions, and helps earn the right to build.

- [**The Rites of Passage**](docs/RITES-OF-PASSAGE.md) — nine revisitable stages from rough idea through evidence-backed delivery.
- [**How a founder steers AI**](docs/FOUNDER-STEERING-PATTERNS.md) — real-world conversational moves: challenge, simplify, disagree, audit, mock, record and verify.
- [**Idea-to-SaaS starter**](starter/idea-to-saas/README.md) — safe bootstrap, private product/decision/next records, reusable interviewing instructions and scenario checks.

This is a **candidate** discovery package; not a magic app generator or a proven business-outcome guarantee.

## The working system behind real SaaS builds

ShoStack records the engineering discipline I use in day-to-day product work — **not a prompt pack assembled for resale**. It connects business intent, architecture, coding-agent instructions, system contracts, verification and accountable handoff.

- [**How I take a SaaS change from problem to verified delivery**](docs/SAAS-DELIVERY-SYSTEM.md)
- [**Copy and adapt the public starter**](starter/README.md) — agent instructions, working records, boundary contracts and release evidence
- [**Products in practice**](docs/PROJECTS-IN-PRACTICE.md) — public product context, without copying client implementation

These are public methods and editable templates, **not** a finished commercial installer or independently benchmarked harness.


## The ShoStack loop

The second deep dive sharpened the recurring loop into:

1. **Inspect reality** — current tree, runtime, tests, incidents and local instructions.
2. **Name authoritative truth** — separate canonical state from caches, projections and replicas.
3. **Frame contract + authority** — identity, states, permissions, versions, retries and ownership.
4. **Create a working record** — capture scope, evidence, changed assumptions and decisions.
5. **Build through chokepoints** — one authoritative mutation path per responsibility.
6. **Make change safe under repetition** — atomic writes, idempotency, deduplication and race resistance.
7. **Verify adversarially** — happy path plus failure, corruption, concurrency and bypass cases.
8. **Degrade honestly** — keep safe partial service where possible without pretending coverage is complete.
9. **Promote deliberately** — source → working → reviewed → approved → released are distinct states.
10. **Compound the lesson** — recurring incidents become tests, skills, guards, wrappers, runbooks or canonical helpers.

## Operating skills

| Skill | What it captures |
|---|---|
| [Reality-first repo reading](skills/reality-first-repo-reading/SKILL.md) | Establish executable reality before design or claims |
| [Working-doc-driven development](skills/working-doc-driven-development/SKILL.md) | Plan, evidence, execution and handoff as one evolving record |
| [Canonical chokepoints](skills/canonical-chokepoints/SKILL.md) | One authoritative mutation/service path per responsibility |
| [Contract-first boundaries](skills/contract-first-boundaries/SKILL.md) | Explicit identity, state, permissions, versions and retry semantics |
| [Bounded reversible change](skills/bounded-reversible-change/SKILL.md) | Reduce blast radius before increasing commitment |
| [Evidence-gated verification](skills/evidence-gated-verification/SKILL.md) | Prove the real claim on the real execution path |
| [Failure-oriented testing](skills/failure-oriented-testing/SKILL.md) | Design tests to kill real bug classes and bypasses |
| [Agent-native system design](skills/agent-native-system-design/SKILL.md) | Safe machine-readable capability surfaces for AI agents |
| [Authority & approval design](skills/authority-and-approval-design/SKILL.md) | Separate proposal, approval, execution and publication authority |
| [Guardrails as code](skills/guardrails-as-code/SKILL.md) | Turn recurring failure classes into executable walls |
| [Atomicity & race resistance](skills/atomicity-and-race-resistance/SKILL.md) | Prevent torn state, duplicate effects and stale-writer races |
| [Idempotent recovery & reconciliation](skills/idempotent-recovery-and-reconciliation/SKILL.md) | Make retries/restarts converge instead of duplicate or reinterpret |
| [Honest degradation](skills/honest-degradation/SKILL.md) | Degrade optional dependencies while protecting authoritative truth |
| [Derived-state & cache discipline](skills/derived-state-and-cache-discipline/SKILL.md) | Keep caches/indexes disposable, versioned and visibly stale |
| [Privacy-aware observability](skills/privacy-aware-observability/SKILL.md) | Diagnose and audit without copying secrets/private payloads |
| [Provenance & promotion](skills/provenance-and-promotion/SKILL.md) | Preserve source identity and promote state explicitly |
| [Compound engineering](skills/compound-engineering/SKILL.md) | Convert repeated lessons into reusable system capability |
| [Idea-to-SaaS discovery](skills/idea-to-saas-discovery/SKILL.md) | Progressive founder-led product discovery and meaningful rites of passage; **candidate** |\n| [SaaS delivery discipline](skills/saas-delivery-discipline/SKILL.md) | Product-to-verified-change workflow; new **candidate** synthesis |

## Implementation skills

| Skill | Maturity | What it captures |
|---|---|---|
| [October CMS / Laravel plugin systems](skills/octobercms-laravel-plugin-systems/SKILL.md) | repeated | Domain plugins, services, transactions, versions and state machines |
| [MCP tool-server design](skills/mcp-tool-server-design/SKILL.md) | core | Permission-bounded AI capability surfaces over domain truth |
| [Python FastAPI / Pydantic agent systems](skills/python-fastapi-pydantic-agent-systems/SKILL.md) | repeated | Typed shared cores exposed through API, CLI and agent surfaces |
| [Next.js operator dashboards](skills/nextjs-operator-dashboards/SKILL.md) | candidate | Responsive operational UI over expensive or partially fresh data |
| [Environment fidelity & local automation](skills/environment-fidelity-local-automation/SKILL.md) | core | Run, test and guard work where it actually executes |

See [Implementation environments](docs/TECHNICAL-STACK.md) for a deliberately broad technology inventory.

## Evidence without disclosure

The skills were distilled from multiple materially different production and operational systems spanning web applications, workflow automation, AI-agent operations, decision automation and creative production.

ShoStack does **not** publish internal algorithms, data models, endpoint inventories, business thresholds, proprietary prompts, source snippets or infrastructure topology. The public evidence model is described in [docs/EVIDENCE.md](docs/EVIDENCE.md).

## What makes a ShoStack skill

A skill must be:

- **observable** — supported by implemented behaviour, tests, operational records or repeated code patterns;
- **portable** — still useful after product names and domain logic are removed;
- **procedural** — another engineer or coding agent can execute it;
- **bounded** — it says when not to apply itself;
- **testable** — it names evidence that proves the method was followed;
- **disclosure-safe** — it teaches the engineering principle without exposing proprietary implementation.

## Maturity

- **candidate** — one convincing implementation;
- **repeated** — independently observed in at least two systems;
- **core** — repeated across three or more materially different systems, or encoded as a cross-project invariant with implementation evidence.

Maturity is about **evidence of repeated behaviour**, not seniority adjectives.

## Why this exists

ShoStack can serve as:

1. a personal engineering operating manual;
2. a portable instruction source for coding agents;
3. evidence for career, consulting and training narratives;
4. a place to crystallize new practices after real work proves they deserve to become skills.
