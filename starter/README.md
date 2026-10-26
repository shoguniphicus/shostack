# ShoStack starter — reusable specifications for a coding agent

This is the *open, editable specification layer* of the harness, not a one-command automation product or a set of validated integrations.

## Have an idea, but not yet a product specification?

Start upstream with [ShoStack / Idea-to-SaaS](idea-to-saas/README.md): a guided discovery interviewer, persistent KNOW / THINK / UNKNOWN records, decision history, progressive question coverage, and a safe workspace initializer. Only move to the general coding starter below when there is a bounded task worth implementing.

## Install into an existing project

1. Read existing agent instructions and project-specific ownership rules. Do **not** overwrite them blindly.
2. Merge the appropriate instructions from [AGENTS.template.md](AGENTS.template.md) into the target repository.
3. Create a dated `docs/working/` record using [working-record.md](templates/working-record.md).
4. When changing an integration, create the owner-approved contract using [boundary-contract.md](templates/boundary-contract.md).
5. Before claiming completion, fill in [release-evidence.md](templates/release-evidence.md) with **actual** commands and outcomes.

Keep source-specific commands and private architecture in the target project, not this public repository.

## Starter request to a coding agent

```text
Read the local AGENTS.md and newest relevant docs/working record. Inspect the
actual repository branch/SHA, code, tests and runtime before changing anything.
State acceptance and contract ownership; implement one bounded reversible slice.
Run the real tests and relevant negative case; record exact outputs, missed
checks and remaining risks. Separate code changed, tests passed, merged and
deployed. Never claim an unobserved state.
```

## Prove usefulness before adding complexity

Test the starter against a disposable app with one broken API contract and one repeat-call problem. Record what the agent catches, what it misses and the actual test results. Add executable checks only after concrete failure modes justify them.

Read [the delivery loop](../docs/SAAS-DELIVERY-SYSTEM.md) and [disclosure policy](../docs/DISCLOSURE-POLICY.md).
