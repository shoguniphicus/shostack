# ShoStack / Idea-to-SaaS — Rites of Passage

**For anyone who has an idea, but cannot yet explain all the realities an AI coding agent needs to build a useful product.** The goal is not to fill in a thirty-page questionnaire. It's a guided conversation that progressively discovers the product while respecting what you know, think you know and don't yet know.

The method comes from [Rites of Passage](../../docs/RITES-OF-PASSAGE.md) and the [agent discovery skill](../../skills/idea-to-saas-discovery/SKILL.md). This pack gives you an actual drop-in private workspace.

## Quick start — with a coding agent or ChatGPT that has file access

Clone ShoStack or otherwise obtain this public repo, then from the ShoStack folder run:

```sh
python3 starter/idea-to-saas/bootstrap.py /path/to/your-existing-product-workspace
```

The initializer **never overwrites files**. It creates (when missing):

- `discovery/PRODUCT.md` — what you're building, in your original words; reality ledger, current workflow and tentative scope.
- `discovery/DECISIONS.md` — choices made, options rejected, reasons and reopening triggers.
- `discovery/NEXT.md` — current rite, single next question and unresolved blockers.
- `discovery/INTERVIEWER.md` — self-contained instructions for the discovery agent.
- `discovery/QUESTION-COVERAGE.md` — hidden breadth map to prevent forgotten realities.

You can preview changes without writing anything:

```sh
python3 starter/idea-to-saas/bootstrap.py --dry-run /path/to/your-existing-product-workspace
```

No plugin, API key, billing account or running application is required. Python 3.9+ is sufficient for initialization (the pack's Markdown itself has no Python runtime requirement).

### Start the first conversation

Open your AI coding agent in the product workspace and say:

> Read discovery/INTERVIEWER.md, discovery/PRODUCT.md, discovery/DECISIONS.md and discovery/NEXT.md. I have a rough idea, not a complete software specification. Interview me using the ShoStack Rites of Passage. Record my words as known, believed or unknown, challenge contradictions and update the files as we go. Ask **one most useful question** first. Do not jump straight to architecture or code.

You can start with no more than:

> I want to build something that helps people with [a messy situation].

You do not need to have a framework, roles, database, business model or pricing ready. If the agent can read files but cannot write, ask it to supply the exact revised Markdown rather than claiming files were updated.

### In a chat without repository access

Give the assistant this [public interviewer instruction](AGENTS.addendum.md) and describe the idea. Ask for a copy-ready running PRODUCT / DECISIONS / NEXT summary after major decisions. Chat sessions without filesystem access cannot promise durable local file updates.

## What the agent should feel like

It should talk with you like a product partner: identify the question that most changes the design, explore alternatives, use examples instead of unexplained jargon, and adapt when you say "No, that's not it". A smart refusal to overbuild is often more valuable than another feature suggestion.

There are **nine revisitable rites (R0–R8)** from a raw idea to tested slices. They are not a checkbox waterfall. The agent can propose a cheap mock to answer one unknown long before an entire architecture is defined. For real payments, private user data or production releases, additional proofs are mandatory.

## What this product is not

- It is not a one-shot "app generator".
- It will not invent user interviews, revenue, competitors, legal permissions or customer behavior.
- It is not a production security, compliance or deployment guarantee.
- Passing its initializer tests does not establish interviewing quality or SaaS market success.

The public pack is an early **candidate** methodology and starter, not an independently benchmarked paid installer.

## How to evaluate it

See the [synthetic scenarios](SCENARIOS.md): vague founder idea, unknown payer, rejected feature, technical premature certainty, request to skip discovery and the resume-after-interruption test. Judge agent behavior and the actual updated artifacts, not wordiness or a polished mock PRD.

The future paid offering could add tailored question logic, deep example projects, evaluation fixtures, maintained adapters and tested workflow tooling — but should be licensed and differentiated honestly from the open Apache-2.0 methodology.
