---
name: contract-first-boundaries
category: operating
maturity: core
---

# Contract-first boundaries

## Intent

Make system behaviour explicit enough that humans, services and agents can coordinate without hidden assumptions.

## Use when

- defining APIs or MCP tools;
- designing workflow state;
- integrating services;
- handing work between agents;
- introducing permissioned actions.

## Core rule

> Define identity, ownership, states, inputs, outputs, permissions and failure semantics before scaling automation.

## Procedure

1. Identify the bounded responsibility and its owner.
2. Define stable identities and versioning rules.
3. Define allowed states and transitions.
4. Define input/output schema and error semantics.
5. Define permissions/capabilities separately from implementation convenience.
6. Define idempotency/dedup behaviour for repeat calls.
7. Freeze contract fixtures or tests at integration boundaries.
8. Let each side own only its responsibility.

## Non-negotiables

- No ambiguous "current" item without stable identity/version.
- No important `WAIT` state without owner/trigger/expiry when it blocks work.
- Read-only does not automatically mean public-safe.
- Capability exposure should be intentional, not "registered then hidden."

## Verification

A caller can determine:

- what it may do;
- what state it is in;
- which result is authoritative;
- how to retry safely;
- what an error means.

## Anti-patterns

- hidden policy constants inside prompts;
- free-form statuses with no transition contract;
- public surfaces that expose internal fields because they already exist;
- two services both claiming schema authority.

## Evidence

- `agencyos/AGENTS.md` — explicit entities, states, versions, roles and queue lifecycle.
- `piggybankos/memory/ACTION-DECISION-CONTRACT.md` — shared machine contract, exact recommendations, blocker schema, idempotent dispatch.
- `altechcamera/AGENTS.md` and public MCP audit — scopes, tool contracts, public/admin separation.
