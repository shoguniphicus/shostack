---
name: agent-native-system-design
category: operating
maturity: core
---

# Agent-native system design

## Intent

Build systems that AI agents can operate without receiving excessive authority or relying on fragile conversational context.

## Use when

- exposing business operations to agents;
- creating MCP tools;
- building autonomous/recurrent workflows;
- designing agent workspaces;
- separating human approval from machine execution.

## Core rule

> Give the agent a small, explicit, machine-readable capability surface backed by domain truth.

## Procedure

1. Define the agent's job in user-intent terms.
2. Expose only the capabilities required for that job.
3. Use stable schemas, enums, IDs and bounded result sizes.
4. Keep domain policy in services/config, not in prompt prose alone.
5. Make permissions and scopes explicit.
6. Provide reference docs/examples/error semantics.
7. Make retries idempotent where actions can repeat.
8. Log consequential actions and skipped/blocked decisions.
9. Separate machine workspace/memory from canonical domain truth.

## Non-negotiables

- Do not expose admin tools to public/anonymous agents because scopes might hide them.
- Do not rely on an LLM to invent facts already represented by domain data.
- Do not require the agent to infer hidden lifecycle state.
- High-impact writes need explicit authority/guardrails.

## Verification

A fresh agent can use the surface correctly from its docs/schema without privileged tribal knowledge, and cannot reach unrelated capabilities.

## Anti-patterns

- giant generic tool;
- prompt-only policy;
- raw database access;
- ambiguous free-form error text;
- an agent session becoming the only memory of a decision.

## Evidence

- `altechcamera/AGENTS.md` — MCP tools, scopes, agent workspaces and references.
- `altechcamera` public MCP audit — separate public server, intent-oriented tools, sanitized projections.
- `agencyos/AGENTS.md` — agent role, job claim/submit lifecycle and permission matrix.
- `zennith-os/AGENTS.md` — executable skills, memory separation and agent navigation map.
- `piggybankos/AGENTS.md` — message/proposal channels and logged autonomous decisions.
