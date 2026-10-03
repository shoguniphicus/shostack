---
name: environment-fidelity-local-automation
category: implementation
maturity: core
---

# Environment fidelity & local automation

## Intent

Treat the actual execution environment as part of correctness, and move repeatable local checks into wrappers, hooks and auditable automation.

## Use when

- applications run in Docker or sidecars rather than directly on the host;
- multiple machines/agents execute the same repo;
- cloud CI is absent, slow or insufficient;
- commands have safety/policy wrappers;
- debugging differs between source checkout and runtime.

## Core rule

> Run the check where the software really runs, through the canonical local path.

## Procedure

1. Identify the execution boundary: host, container, sidecar, worker, browser, broker wrapper, remote service.
2. Identify the canonical command/wrapper for that boundary.
3. Reproduce the problem/check there, not in a convenient adjacent environment.
4. Encode repeated setup/checks in idempotent scripts.
5. Put critical fast-fail checks at the earliest reliable local hook.
6. Audit that hooks/wrappers are installed and reachable.
7. Keep break-glass bypasses narrow and auditable.
8. Distinguish local preflight evidence from remote/integration evidence.
9. Document environment-specific paths and commands close to the project.
10. Prefer self-healing installation where repeated multi-machine drift is known.

## Non-negotiables

- A host PHP binary does not validate a container-only application.
- A hook file existing does not prove Git executes it.
- Do not bypass a canonical wrapper with raw network calls just because it is faster to type.
- Local automation must not silently claim authority it cannot have remotely.
- Environment fallbacks must not weaken safety-critical invariants.

## Verification

A new machine/agent can determine:

- where the app really runs;
- which command is canonical;
- whether required hooks/checks are active;
- what evidence is local-only versus integration-level.

## Anti-patterns

- testing in the wrong runtime and declaring production fixed;
- hand-running a remembered sequence instead of using the repo wrapper;
- hooks installed below unreachable control flow;
- global local checks that fail contributors for unrelated tree state;
- undocumented per-machine magic.

## Deep-dive heuristics

- Use a real datastore/runtime in end-to-end tests when substitute environments change semantics that matter.
- Hermetic unit tests and real-path integration tests serve different purposes; keep both rather than pretending one replaces the other.
- Installation checks should prove the hook/wrapper actually runs, not only that files were copied.

## Evidence basis

- Observed across containerized applications, Python sidecars and multi-machine repositories where runtime location changes correctness.
- Reinforced by local hooks, wrapper commands and end-to-end checks against the actual execution environment.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
