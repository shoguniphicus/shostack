# Initial ShoStack skill distillation — Progress Log (2026-10-03)

## Scope & objectives

- Inspect the first five source repositories supplied by Sho.
- Distill repeated engineering behaviour rather than produce a technology résumé.
- Seed `shostack` with portable, evidence-backed skill contracts.
- Keep technology inventory separate from behavioural skill claims.

## Repositories inspected

- `shoguniphicus/altechcamera`
- `shoguniphicus/piggybankos`
- `shoguniphicus/agencyos`
- `shoguniphicus/zennith-os`
- `shoguniphicus/alamakfarm`

## Evidence inspected

Representative surfaces included:

- repo roots and recent commits;
- `AGENTS.md` / README operating instructions;
- `docs/working/` structures and selected audits;
- Altech public MCP audit;
- Agency P0 final hardening audit;
- Piggybank action-decision contract;
- Zennith builder / git-discipline / zen-ci patterns;
- Alamak Farm workflow and branching rules;
- Composer, npm and Python package manifests.

See `docs/EVIDENCE.md` for path-level details.

## Interpretation

The strongest repeated pattern is not one framework. It is a process:

`inspect → establish truth → contract → working record → canonical implementation → verify → promote → compound`.

This appears in commerce, agency workflow, investing/quant automation, creative production, and a large AI marketing OS.

## Initial core skills

1. reality-first repo reading;
2. working-doc-driven development;
3. canonical chokepoints;
4. contract-first boundaries;
5. bounded reversible change;
6. evidence-gated verification;
7. agent-native system design;
8. guardrails as code;
9. provenance and promotion;
10. compound engineering.

## Code-level validation pass

The first abstraction pass was checked against implementation, not just architecture notes:

- **Altech** — `GaiaServer.php` registers the actual MCP tool surface; `AiAgentSecurityMiddleware.php` enforces authentication, declared scopes, IP/rate limits and audit; `GaiaToolTrait.php` reuses existing API controllers while propagating security context; `ContextualRecommendationGraphService.php` explicitly refuses to invent recommendation candidates.
- **AgencyOS** — the real `plugins/gaia/*` bounded contexts exist; `JobStatusMachine.php` encodes legal lifecycle transitions and cancellation authority; `JobService.php` wraps creation/versioning/status changes in domain services and transactions.
- **PiggybankOS** — `config/action-policy.yaml` is a real policy kernel; `scripts/quant_funnel.py` records lifecycle receipts and writes scorecards atomically; `ui_api/main.py` is a FastAPI operational sidecar; the Next.js dashboard uses reusable live-fetch/cache/cancellation mechanics.
- **Zennith OS** — `sidecar/records.py` is genuinely a canonical write chokepoint with brand/reference/invariant enforcement; `sidecar/mcp_server.py` validates inputs and routes MCP calls through the same registered skill/domain surfaces rather than creating a second truth store.

This pass strengthened the claim that the operating patterns are implemented behaviour, not merely preferred documentation style.

## Implementation skill layer

The first concrete environment skills are:

1. October CMS / Laravel plugin systems — **repeated**;
2. MCP tool-server design — **core**;
3. Python FastAPI / Pydantic agent systems — **repeated**;
4. Next.js operator dashboards — **candidate**;
5. environment fidelity & local automation — **core**.

The lower maturity on Next.js is deliberate: Piggybank provides strong production evidence, but the current audit does not yet show the same pattern independently in another supplied repository.

## Important restraint

A dependency in `composer.json`, `package.json`, or `pyproject.toml` proves presence/use in a project. It does not alone justify a mastery claim. Framework evidence is promoted into a skill only when production code shows how it is actually used.

## Validation

- Every operating skill has evidence from at least two repositories.
- Core abstractions were preferred only where the behaviour repeats across materially different domains.
- Implementation skills were checked against actual services, middleware, state machines, APIs, hooks or UI code.
- Repo-specific rules remain cited as evidence rather than being copied blindly into universal procedure.
- Work is developed on reusable `dev`, compared with current `main`, and intended to reach `main` through a reviewed PR rather than a direct write.
