---
name: canonical-chokepoints
category: operating
maturity: core
---

# Canonical chokepoints

## Intent

Prevent drift by routing important mutations and policy decisions through one authoritative path.

## Use when

- multiple services can write the same concept;
- adding a new workflow/adapter/integration;
- introducing agent tools;
- storing files or records;
- extending validation.

## Core rule

> Reuse or extend the canonical writer/service; do not create a parallel truth path for convenience.

## Procedure

1. Name the authoritative source and write path for the responsibility.
2. List derived/read-only views separately.
3. Route new behaviour through the canonical service.
4. If the canonical path cannot express the requirement, extend it first.
5. Keep indexes, projections and caches rebuildable where possible.
6. Ensure downstream adapters do not silently become new policy owners.

## Non-negotiables

- One responsibility should not have two independent authorities.
- Transport layers should not invent domain truth.
- Derived indexes must not become unrecoverable hidden state.
- Agent convenience is not a reason to bypass business invariants.

## Verification

- The new path reaches the same central validator/writer as existing paths.
- Deleting/rebuilding a derived view does not destroy canonical truth.
- Responsibility ownership is documented.

## Anti-patterns

- direct filesystem/database writes beside a canonical service;
- a public API reusing an admin transport and leaking its internals;
- duplicated validation in client and server that can drift;
- raw SDK calls when a policy wrapper already exists.

## Deep-dive heuristics

- Periodically audit for bypass writers/callers; a canonical path is not canonical if old shortcuts remain live.
- When porting callers onto the chokepoint, preserve externally relied-on contracts while removing the bypass underneath.
- Put the invariant at the lowest shared mutation point that every legitimate path can inherit.

## Evidence basis

- Observed across multiple systems that centralize writes, validation or side effects and regression-test historical bypasses.
- Reinforced by migrations that preserve external behaviour while moving callers onto one authoritative path.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
