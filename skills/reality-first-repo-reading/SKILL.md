---
name: reality-first-repo-reading
category: operating
maturity: core
---

# Reality-first repo reading

## Intent

Build from the system that actually exists, not from stale memory, generic framework assumptions, or a previous architectural snapshot.

## Use when

- starting work in an existing repository;
- auditing architecture;
- debugging a mismatch between docs and runtime;
- taking over work from another agent or human;
- answering "what is built now?"

## Core rule

> Prove the current referent before changing or describing it.

## Procedure

1. Identify the repository, branch and current head.
2. Read local instruction files before generic habits.
3. Read the most recent working/handoff records relevant to the task.
4. Inspect the actual files, services, schemas, tests and runtime boundary implicated by the request.
5. Search for an existing capability before proposing a new one.
6. Name contradictions between docs and code instead of silently choosing one.
7. Only then frame the change.

## Non-negotiables

- Do not assert current repo state from memory alone.
- Do not assume a conventional file/path exists; inspect it.
- Do not use README-level architecture as a substitute for the code path when correctness depends on implementation.
- Runtime location matters: host, container, service and remote worker are different referents.

## Verification

A good working record can answer:

- Which commit/tree was inspected?
- Which local instructions governed the work?
- Which implementation path was read?
- Which existing capability was reused or rejected, and why?

## Anti-patterns

- designing a new service before searching for the existing one;
- running host commands for a container-only application;
- claiming "not implemented" because one expected path was absent;
- using a stale branch as architectural evidence.

## Evidence

- `zennith-os/AGENTS.md` — process-first read order and stale-tree check.
- `altechcamera/AGENTS.md` — project-specific architecture and Docker runtime rules.
- `agencyos/AGENTS.md` — "check the real structure before assuming files exist."
- `alamakfarm/README.md` — explicit human/GPT read order.
