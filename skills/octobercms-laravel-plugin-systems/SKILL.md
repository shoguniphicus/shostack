---
name: octobercms-laravel-plugin-systems
category: implementation
maturity: repeated
---

# October CMS / Laravel plugin systems

## Intent

Build operational web systems as explicit domain plugins on October CMS / Laravel rather than accumulating business behaviour in controllers, themes or one giant application layer.

## Use when

- modelling a new bounded business capability in October CMS;
- adding workflow/stateful backend behaviour;
- extending an existing plugin ecosystem;
- exposing a domain through web, API or agent interfaces.

## Core rule

> Put domain lifecycle and invariants in plugin services/models/state machines; keep transport layers thin.

## Procedure

1. Name the bounded context and its dependencies before creating files.
2. Follow the plugin anatomy: registration, routes, models, enums, services, migrations/versions, tests, then UI/controllers.
3. Put multi-step writes in a domain service and transaction where consistency matters.
4. Encode lifecycle transitions explicitly instead of accepting arbitrary status mutation.
5. Create a new version when semantic instructions/content change; do not version trivial status-only changes.
6. Enforce workspace/tenant, entitlement and permission boundaries before mutation.
7. Emit domain events only after the authoritative state change succeeds.
8. Test the service/state-machine behaviour independently of presentation.
9. Let controllers/components translate requests and responses; do not make them the only place business rules exist.

## Non-negotiables

- A workflow status is not a free-form column when legal transitions matter.
- Do not duplicate domain validation in every controller/tool.
- Migrations and plugin version history move together.
- Cross-plugin dependencies must be deliberate and visible.
- Business behaviour belongs in the backend domain even when the first caller is an AI agent.

## Verification

For a domain operation, you can point to:

- the owning plugin;
- the service method that performs it;
- the state/enum rules that constrain it;
- the transaction/version semantics;
- tests around legal and illegal paths.

## Anti-patterns

- controller-as-domain-service;
- arbitrary `model->status = ...`;
- one plugin reaching directly into several others' internals;
- theme JavaScript carrying authoritative business rules;
- duplicating a service because a new transport wants slightly different output.

## Evidence

- `agencyos/plugins/gaia/job/services/JobStatusMachine.php` — explicit transition graph and role-aware cancellation.
- `agencyos/plugins/gaia/job/services/JobService.php` — entitlement check, transactions, version creation, state transition and domain events.
- `agencyos/plugins/gaia/{workspace,brief,job,deliverable,feedback,correspondence,decision,...}` — real bounded plugin layout.
- `altechcamera/AGENTS.md` — plugin dependency map and service ownership across security, MCP, customer, market, transaction and stocktake domains.
- Both repositories use October CMS 4 / Laravel 12 / PHP 8.2+.
