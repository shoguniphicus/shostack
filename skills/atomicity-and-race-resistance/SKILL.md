---
name: atomicity-and-race-resistance
category: operating
maturity: core
---

# Atomicity & race resistance

## Intent

Prevent partial writes, duplicate effects and stale actors from corrupting authoritative state.

## Use when

- replacing durable files;
- updating multiple related records;
- multiple workers can process the same logical item;
- UI requests can overlap;
- branches/versions can move while a change is being prepared.

## Core rule

> Authoritative state should move from one valid state to another; concurrent or failed work must not leave a torn in-between state.

## Procedure

1. Identify the atomic unit the user/system cares about.
2. Use datastore transactions for multi-record mutations when available.
3. For file replacement, write a temporary complete artifact then atomically replace the target.
4. Use stable reservations/locks/idempotency where two workers could claim the same logical action.
5. Coalesce concurrent identical reads/work when fan-out is expensive.
6. Cancel or discard stale asynchronous results that no longer match current input/version.
7. Use expected version/SHA when replacing shared state.
8. Preserve the previous valid state when a write fails.
9. Test concurrency and injected mid-write failure.

## Non-negotiables

- Never truncate the authoritative target before the replacement is known-good.
- Do not let stale work overwrite a newer user/system choice.
- Locking should match the logical resource, not merely the process.
- "Eventually consistent" is not permission to expose impossible intermediate state.

## Verification

Test at least:

- failure halfway through persistence;
- two actors attempting the same claim/effect;
- old response arriving after a new request;
- expected-version mismatch;
- concurrent cache miss / producer fan-out.

## Anti-patterns

- direct overwrite of a critical file;
- read-modify-write without version/locking on shared state;
- multiple workers creating separate "same" actions;
- async UI responses accepted regardless of current selection;
- assuming branch head did not move.

## Evidence basis

- Observed across database-backed workflows, file-backed canonical records, operator UIs and safe Git/revision workflows.
- Reinforced by transaction, fault-injection, concurrency and stale-write regression tests.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
