---
name: honest-degradation
category: operating
maturity: core
---

# Honest degradation

## Intent

Keep useful service available when non-authoritative dependencies fail, while refusing to corrupt or overstate authoritative truth.

## Use when

- replicas/caches can be unhealthy;
- background workers can stall;
- optional providers are unavailable;
- a dashboard combines independent data sources;
- read availability and write safety have different requirements.

## Core rule

> Degrade where the missing component is optional; block where truth, authority or irreversible safety is uncertain — and always disclose the degraded coverage.

## Procedure

1. Classify dependencies as authoritative, required-for-write, or optional/derived.
2. Define fail-closed behaviour for authority/truth/safety boundaries.
3. Define fail-open/partial behaviour for safe reads or optional replicas.
4. Surface exactly what was skipped, stale or unavailable.
5. Keep health/diagnostic surfaces reachable where safe.
6. Persist degradation state long enough for operators/watchdogs to notice.
7. Clear degradation state when the dependency demonstrably recovers.
8. Prevent partial data from being mislabeled as complete.
9. Test multiple simultaneous failures and the authoritative-failure case separately.

## Non-negotiables

- Do not fabricate missing data to preserve a green status.
- Do not use a degraded replica to overwrite authoritative state.
- "HTTP server alive" and "worker healthy" may need separate signals.
- A safe read fallback does not authorize a write.
- Recovery must clear stale degraded markers.

## Verification

Test:

- one optional dependency fails;
- several optional dependencies fail;
- authoritative source fails;
- health/status exposes coverage loss;
- recovered dependency rejoins cleanly.

## Anti-patterns

- all-or-nothing outage for a non-critical replica;
- silently skipping broken inputs;
- green health check while critical worker is dead;
- continuing writes because reads still work;
- stale "degraded" state that never clears.

## Evidence basis

- Repeated across replicated reads, operator dashboards, background workers and permissioned agent systems.
- Reinforced by tests for partial availability, explicit degraded metadata and fail-closed authoritative paths.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
