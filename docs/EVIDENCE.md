# Evidence methodology

ShoStack skills are grounded in real implementation, but this public repository intentionally keeps the underlying proprietary implementation out of the evidence record.

## Evidence strength

From weaker to stronger:

1. **Dependency presence** — proves a technology appears in a project.
2. **Documentation/architecture** — proves an intended method or rule exists.
3. **Production implementation** — proves the method is encoded in executable code.
4. **Tests and negative cases** — prove important invariants and failure behaviour.
5. **Operational repetition** — proves the method survived use, incidents, recovery and later changes.
6. **Independent repetition** — proves the behaviour generalizes across materially different systems.

Skill maturity is based primarily on levels 3–6.

## Source diversity

The initial evidence base spans multiple materially different kinds of systems, including:

- long-lived web/business applications;
- agent-facing operational systems;
- workflow and decision automation;
- operator dashboards and sidecars;
- creative/content production pipelines.

The public repo does not reproduce the source projects' algorithms, schemas, routes, prompts or operational topology.

## What the second deep dive added

The deeper code/test review revealed several recurring behaviours that were underrepresented in the first pass:

- explicit idempotency and duplicate-effect prevention;
- reconciliation after uncertain or partial external effects;
- atomic persistence and stale-writer/race prevention;
- derived caches/indexes treated as disposable rather than canonical;
- failure injection and regression tests aimed at the old bug class;
- authority bound to exact state/version rather than vague role assumptions;
- deliberate fail-open vs fail-closed choices based on whether truth/authority is at risk;
- audit trails that redact sensitive payloads while preserving diagnostic value;
- partial/degraded results surfaced honestly rather than reported as complete.

These behaviours became new skills instead of being buried as implementation trivia.

## Public evidence basis

Each skill ends with an **Evidence basis** section that describes the classes of systems and checks in which the behaviour was observed.

Exact repository paths and implementation details are intentionally omitted under [the disclosure policy](DISCLOSURE-POLICY.md).

## Maturity interpretation

- **candidate** — strong evidence in one implementation;
- **repeated** — independent evidence in at least two systems;
- **core** — evidence across three or more materially different systems, or a cross-project invariant with executable enforcement.

This is deliberately conservative. A sophisticated one-off implementation is still a candidate until repetition proves it is a stable personal engineering habit.
