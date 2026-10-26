---
name: saas-delivery-discipline
category: operating
maturity: candidate
---

# SaaS product-delivery discipline

## Intent

Turn an AI coding session into a bounded, contract-aware, verifiable product change that another engineer or agent can resume.

## Use when

Extending a SaaS, coordinating frontend/backend work, maintaining an application with real users, or handing work between coding-agent sessions.

## Core rule

> Generated code is not delivered product. Define authority and contracts, verify what actually runs, and report the precise state of the release.

## Procedure

1. State the business outcome, acceptance condition and non-goals.
2. Inspect the actual source tree, branch/SHA, rules, runtime and tests.
3. Identify canonical data, authority, trust boundaries and service ownership.
4. Document interfaces, states, versions, errors, permissions and retry semantics.
5. Start a dated working record and plan a small reversible change.
6. Implement without silently adding a competing source of truth.
7. Run the relevant legitimate and negative/regression checks; record outputs.
8. Reconcile concurrent changes, commit/merge deliberately, and report deployed versus merely merged status.
9. Distil repeated failure classes into checks or skills.

## Non-negotiables

- Never copy private source, customer data, internal topology or proprietary prompts into public material.
- Do not turn planned capability into an implementation claim.
- Do not claim tests, runtime smoke or deployment without actual evidence.
- Require authorization for release, destructive operations or privilege changes.
- Keep effort proportional to the change's risk.

## Verification

A reviewer can find the baseline SHA, contract owner, acceptance check, commands and results, failing-before/passing-after regression where relevant, final ref, and any unverified gates. The relevant boundary contract detects drift between callers and implementers.

## Anti-patterns

Prompt-only magic fixes; duplicated API specifications with no single owner; successful typecheck called an integration test; PR called deployed; invented reliability statistics; private client recipes published as examples.

## Evidence basis

This is a newly packaged synthesis of existing ShoStack operating skills and observed project-level agent instructions. The **starter package has not been independently benchmarked**, so its maturity is deliberately `candidate`. See [SaaS delivery](../../docs/SAAS-DELIVERY-SYSTEM.md) and [disclosure](../../docs/DISCLOSURE-POLICY.md).
