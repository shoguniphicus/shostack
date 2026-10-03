---
name: python-fastapi-pydantic-agent-systems
category: implementation
maturity: repeated
---

# Python FastAPI / Pydantic agent systems

## Intent

Build Python operational and agent systems around one reusable domain core, with typed boundaries exposed through APIs, CLIs, MCP or background routines.

## Use when

- building a local/remote sidecar;
- exposing structured workflows to agents;
- creating an operator API over file-backed or service-backed state;
- sharing one capability between CLI and network callers.

## Core rule

> Keep domain functions reusable and typed; make FastAPI, CLI and MCP thin surfaces over the same core.

## Procedure

1. Define stable Python models/contracts for external inputs and outputs.
2. Put canonical reads/writes and invariants in ordinary domain modules, not inside route handlers.
3. Make FastAPI routers validate, authorize and translate; call the shared domain core.
4. Let CLI/MCP surfaces call the same core or skill registry.
5. Treat caches/indexes as derived and rebuildable when the durable source lives elsewhere.
6. Use startup/lifespan hooks for health checks, cache warmup or watchers only when ownership is clear.
7. Decide which startup failures are fatal and which should degrade visibly but allow useful operation.
8. Use atomic writes/idempotent receipts for durable operational artifacts.
9. Add SSE or other push mechanisms when polling would create poor operator semantics.
10. Test domain logic and boundary validation separately.

## Non-negotiables

- Do not let every route reimplement storage rules.
- A derived SQLite/search index must not silently become the only durable truth.
- Validation belongs at the boundary and at canonical mutation chokepoints where necessary.
- Graceful degradation must not silently bypass a safety invariant.
- Shared code should not depend on being called from one transport.

## Verification

The same domain action can be reasoned about independently of whether it arrived through HTTP, MCP, CLI or a routine, and its durable state remains reconstructable.

## Anti-patterns

- business logic embedded entirely in FastAPI route functions;
- separate MCP/CLI implementations of the same action;
- caches with no invalidation/rebuild contract;
- startup doing irreversible work merely because the server booted;
- free-form dictionaries everywhere when a contract is stable enough for models.

## Deep-dive heuristics

- Persist important files atomically: a failed write should leave either the old valid state or the new valid state, never a torn hybrid.
- Expose liveness separately from basic HTTP reachability when workers/background execution can stall while the server still answers.
- Degraded replicas/caches may be skipped only if the response surfaces that coverage loss and authoritative local truth remains sound.

## Evidence basis

- Observed across independent Python operational systems where APIs, CLIs and agent surfaces share a typed domain core.
- Reinforced by atomic persistence, derived-cache rebuildability, health/liveness surfaces and boundary validation.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
