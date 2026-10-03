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

## Deep-dive heuristics

- A robust contract includes replay semantics: what happens if the same request arrives twice?
- Bind authority to an exact identity/version/state; approval of one artifact must not silently authorize a later mutation.
- Specify concurrency ownership where two workers could act on the same logical item.
- Treat unknown enum/state/action values as errors rather than improvising a close-enough interpretation.

## Evidence basis

- Observed across workflow-heavy and agent-facing systems with explicit schemas, state transitions, permissions and retry semantics.
- Reinforced by tests for illegal transitions, duplicate requests, stale authority and boundary failures.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
