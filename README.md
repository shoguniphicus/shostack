# ShoStack

> **How you do anything is how you do everything.**

ShoStack is an evidence-backed record of how Sho builds software with humans and AI agents.

This is **not** a list of technologies copied from package manifests. It is a library of repeatable engineering behaviours distilled from real repositories, plus implementation skills that have concrete repository evidence behind them.

## The ShoStack loop

Across very different systems, the same loop keeps appearing:

1. **Inspect reality** — read the current tree, local instructions, recent working records, and the real runtime before making claims.
2. **Name the source of truth** — decide which record, service, schema, file, or boundary is authoritative.
3. **Frame the contract** — define states, inputs, outputs, permissions, failure semantics, and ownership before expanding implementation.
4. **Create a working record** — plan before code; update it while the work changes.
5. **Build through chokepoints** — extend canonical services and writers instead of creating one-off bypasses.
6. **Verify the real path** — test the layer that actually runs, not a convenient approximation.
7. **Promote deliberately** — move working material into approved/canonical/published state only after its gates pass.
8. **Compound the lesson** — recurring fixes become skills, helpers, tests, hooks, templates, or runbooks.

The individual skills under [`skills/`](skills/) make this loop executable.

## Skill families

### Operating skills

| Skill | What it captures |
|---|---|
| [Reality-first repo reading](skills/reality-first-repo-reading/SKILL.md) | Inspect the actual current system before proposing or changing it |
| [Working-doc-driven development](skills/working-doc-driven-development/SKILL.md) | Plan → execute → document as one continuous artifact |
| [Canonical chokepoints](skills/canonical-chokepoints/SKILL.md) | One authoritative write path / service / truth boundary |
| [Contract-first boundaries](skills/contract-first-boundaries/SKILL.md) | Explicit schemas, states, permissions and responsibility boundaries |
| [Bounded reversible change](skills/bounded-reversible-change/SKILL.md) | Reduce scope and blast radius under uncertainty instead of freezing |
| [Evidence-gated verification](skills/evidence-gated-verification/SKILL.md) | Claims require tests or evidence from the path that matters |
| [Agent-native system design](skills/agent-native-system-design/SKILL.md) | Build interfaces AI agents can use safely and predictably |
| [Guardrails as code](skills/guardrails-as-code/SKILL.md) | Turn recurring failure modes into executable walls |
| [Provenance and promotion](skills/provenance-and-promotion/SKILL.md) | Preserve raw truth; promote derived state deliberately |
| [Compound engineering](skills/compound-engineering/SKILL.md) | Convert repeated work into reusable institutional capability |

### Implementation skills

| Skill | Maturity | What it captures |
|---|---|---|
| [October CMS / Laravel plugin systems](skills/octobercms-laravel-plugin-systems/SKILL.md) | repeated | Domain plugins, service layers, transactions, versions and state machines |
| [MCP tool-server design](skills/mcp-tool-server-design/SKILL.md) | core | Safe AI capability surfaces backed by existing domain truth |
| [Python FastAPI / Pydantic agent systems](skills/python-fastapi-pydantic-agent-systems/SKILL.md) | repeated | Shared Python core exposed through API, CLI and agent surfaces |
| [Next.js operator dashboards](skills/nextjs-operator-dashboards/SKILL.md) | candidate | Responsive operational UIs over expensive and partially fresh data |
| [Environment fidelity & local automation](skills/environment-fidelity-local-automation/SKILL.md) | core | Run and guard work in the environment that actually executes it |

See [`docs/TECHNICAL-STACK.md`](docs/TECHNICAL-STACK.md) for the wider observed stack. Technology is recorded separately from skill so the repo does not confuse "dependency exists" with "demonstrated engineering behaviour."

## Evidence base

The first pass is distilled from:

- `shoguniphicus/altechcamera`
- `shoguniphicus/piggybankos`
- `shoguniphicus/agencyos`
- `shoguniphicus/zennith-os`
- `shoguniphicus/alamakfarm`

See [`docs/EVIDENCE.md`](docs/EVIDENCE.md) for representative paths and the reasoning behind each skill.

## What makes a ShoStack skill

A skill must be:

- **observable** — grounded in shipped repository behaviour or repeated working records;
- **portable** — useful beyond the repo where it was discovered;
- **procedural** — another developer or coding agent can actually execute it;
- **bounded** — it says when not to apply itself;
- **testable** — it names evidence that indicates the skill was followed.

## Maturity

ShoStack does not use inflated labels such as "expert" by default.

- **candidate** — one clear implementation or one repo;
- **repeated** — observed independently in at least two projects;
- **core** — repeated across three or more materially different systems, or encoded as an explicit cross-project rule.

The current skills are intentionally conservative. New evidence may split, merge, strengthen, demote, or retire them.

## Why this exists

ShoStack can serve four purposes at once:

1. a personal engineering operating manual;
2. a portable instruction source for coding agents;
3. evidence for career / consulting / training narratives;
4. a place to crystallize new practices when repeated work proves they deserve to become skills.
