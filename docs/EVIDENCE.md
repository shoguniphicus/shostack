# Evidence map

This file records the evidence used for the first ShoStack distillation. It is intentionally path-based: future audits should be able to reopen the source and challenge the abstraction.

## 1. altechcamera

Representative evidence:

- `AGENTS.md`
  - dated working doc required before code;
  - October CMS / Laravel plugin dependency map;
  - explicit source-of-truth ordering for MCP tools;
  - runtime commands must execute inside Docker;
  - validator/apply-path contracts;
  - agent security scopes and error-envelope rules.
- `docs/working/2026-10-03/public-mcp-discovery-matchmaking-audit.md`
  - read-only is not treated as automatically public-safe;
  - public MCP gets a separate capability boundary;
  - existing domain truth is reused through sanitized projections;
  - compatibility fails closed;
  - initial tool surface is intentionally small and intent-oriented.
- `composer.json`
  - PHP 8.2+, October CMS 4, Laravel 12, Laravel MCP, Elasticsearch, S3/Flysystem, GA4.
- `package.json`
  - Laravel Mix, Vue 2, Bootstrap, Chart.js, Monaco, Playwright Core.

Signals:
- canonical boundaries;
- agent-native interfaces;
- least-capability design;
- environment fidelity;
- evidence-backed architecture reuse.

## 2. agencyos

Representative evidence:

- `AGENTS.md`
  - workspace/brief/job/deliverable/feedback/correspondence/decision are explicit domain concepts;
  - versioned entities and state machines;
  - plugin-level bounded contexts;
  - role/permission matrix;
  - job claim → execute → submit → review lifecycle;
  - correspondence is linked before confirmed decisions become clean records.
- `docs/working/`
  - repeated plan, phase, audit, handoff, regression, and completion records.
- `docs/working/2026-08-21-p0-headless-hardening-final-audit.md`
  - clear responsibility boundary between Agency and Headless;
  - explicit P1 deferrals instead of uncontrolled P0 expansion;
  - no green claim without executable CI evidence;
  - duplicated validators are rejected in favour of one schema authority.
- `composer.json`
  - October CMS 4.2, Laravel 12, Laravel MCP, Cashier, PHPUnit, PHPCS.

Signals:
- contract-first modelling;
- explicit ownership;
- phase-bounded delivery;
- audit before promotion;
- versioned workflow state.

## 3. piggybankos

Representative evidence:

- `AGENTS.md`
  - substantial work requires a dated working record;
  - every executed and skipped decision is logged;
  - missing safety-critical evidence is a named blocker;
  - uncertainty normally reduces size/reversibility rather than causing unbounded waiting;
  - one canonical wrapper is required for broker operations;
  - missed routines are recovered in a bounded way instead of chaining stale work.
- `memory/ACTION-DECISION-CONTRACT.md`
  - shared machine-readable output contract;
  - deterministic thresholds live in config, not hidden agent intuition;
  - exactly one current decision controls a setup;
  - idempotent dispatch keys prevent duplicate work;
  - `MONITOR` requires owner, expiry, trigger, cost of waiting, and fallback.
- `workflows/`, `routines/`, `scripts/`, `memory/`
  - workflows are explicit artifacts rather than implicit conversational behaviour.
- `ui-next/package.json`
  - Next.js 15, React 19, TypeScript 5.7, Tailwind 4, Recharts.

Signals:
- reversible action under uncertainty;
- explicit machine contracts;
- observability for both actions and omissions;
- idempotency;
- bounded recovery.

## 4. zennith-os

Representative evidence:

- `AGENTS.md`
  - process-first read order;
  - stale-tree verification before repo claims;
  - separate agent/operator/vault memory;
  - skills are executable specs;
  - hooks enforce repeat failure walls;
  - git-level guards are distinguished from agent-session hooks;
  - canonical build pipeline G0→G9 plus compounding.
- `docs/builders-guide.md`
  - one canonical writer;
  - one binary chokepoint;
  - derived indexes are rebuildable;
  - user intent is mapped to existing architecture before coding;
  - new requirements extend canonical primitives rather than bypassing them.
- `skills/git-discipline/SKILL.md`
  - commit/push guards;
  - tree-collapse protection;
  - reachability is tested by execution rather than grep/presence;
  - pull-triggered self-healing hook installation.
- `skills/zen-ci/SKILL.md`
  - local CI;
  - one config plan is the source of truth;
  - state checks are path-scoped to avoid blaming unrelated changes;
  - bypasses emit audit records.
- `pyproject.toml`
  - Python, FastAPI, Pydantic, boto3, networkx, Anthropic, Google GenAI, MCP, pytest.

Signals:
- compound engineering;
- guardrails as code;
- executable verification;
- canonical chokepoints;
- agent-operable systems.

## 5. alamakfarm

Representative evidence:

- `README.md`
  - folders organize files; manifests organize meaning; Git stores history;
  - creative truth and public publishing are different states;
  - story IP is format-independent and adaptations derive from it.
- `docs/WORKFLOW.md`
  - raw material preserved before derivation;
  - explicit intake modes;
  - generation/review gates;
  - approved vs publish-ready vs downstream published are distinct promotions;
  - publishing manifests pin source Git commit SHA;
  - rejected derivatives never become the next source parent.
- `docs/BRANCHING.md`
  - short-lived coherent branches;
  - safe merge sequence for automated edits;
  - re-read before replace;
  - compare before merge;
  - no force update to main;
  - branches are temporary workspaces, not taxonomy.
- `skills/`
  - repeated creative processes are crystallized as executable skill specs.

Signals:
- provenance;
- promotion gates;
- branch safety;
- canonical source packets;
- reusable skills from repeated production work.

## Cross-repo patterns

The strongest cross-project patterns are:

1. **Reality before abstraction.**
2. **Working records before / during implementation.**
3. **One canonical truth or write path per responsibility.**
4. **Contracts and states before uncontrolled automation.**
5. **Small, reversible action under uncertainty.**
6. **Verification that tests the real execution path.**
7. **Agent surfaces with explicit permissions and machine-readable semantics.**
8. **Guardrails encoded in tooling instead of remembered as advice.**
9. **Raw → reviewed → approved → published is a promotion chain, not a single state.**
10. **Repeated solutions are compounded into skills, hooks, scripts, templates and runbooks.**
