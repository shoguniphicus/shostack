---
name: derived-state-and-cache-discipline
category: operating
maturity: repeated
---

# Derived-state & cache discipline

## Intent

Gain speed and searchability from caches/indexes without allowing them to become an accidental second source of truth.

## Use when

- building a search/index database over canonical records;
- caching expensive API/sidecar reads;
- rendering operator dashboards;
- maintaining materialized summaries or manifests.

## Core rule

> Derived state may be stale or disposable; canonical truth must remain reconstructable without it.

## Procedure

1. Name the canonical source explicitly.
2. Make the derived representation rebuildable.
3. Define invalidation/update strategy.
4. Version caches when payload/schema changes can make old bytes unsafe.
5. Store freshness/staleness metadata when operators need to reason about age.
6. Coalesce concurrent cache misses for expensive producers.
7. On corruption, repair/rebuild the derived state rather than editing canonical truth to fit it.
8. Keep degraded cache/index state visible.
9. Test cold start, warm start, invalidation, stale shape and concurrent miss.

## Non-negotiables

- A cache hit is not proof of current truth.
- A derived index must not become the only place a record exists.
- Breaking payload changes require cache invalidation/versioning.
- Rebuild must not mutate the canonical source merely to make indexing easier.

## Verification

Prove:

- deleting the derived state does not destroy truth;
- rebuild restores equivalent query capability;
- old incompatible cache versions are ignored;
- two concurrent misses do not multiply expensive work;
- staleness is detectable.

## Anti-patterns

- hidden cache/index becoming canonical because it is faster;
- permanent browser cache across incompatible payload versions;
- cache with no owner/invalidation story;
- "rebuild" that rewrites source data;
- unbounded polling of expensive sources.

## Evidence basis

- Repeated across file-backed knowledge systems and operator dashboards with rebuildable indexes and versioned caches.
- Reinforced by warm/cold start, concurrent cache-miss and stale-shape tests.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
