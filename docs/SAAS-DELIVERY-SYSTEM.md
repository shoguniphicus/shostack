# ShoStack — the working system behind commercial SaaS builds

> ShoStack is the engineering method Sho uses in real product work. It is not a prompt collection written solely to sell, a copy of client source code, or an independently benchmarked product.

Building software with AI involves more than asking for code. Existing systems have users, owners, contracts, state, regressions, integrations and releases. ShoStack provides a **repeatable way to direct the work and demand evidence**.

## The product-to-verification loop

| Step | Question | Minimum evidence |
| --- | --- | --- |
| 1. Frame | Who needs what outcome? What must not change? | Acceptance condition, scope, risk owner |
| 2. Inspect | What is real in this repository and runtime now? | Branch/SHA, code, tests, unknowns |
| 3. Locate authority | Which source owns state, identity, permissions and policy? | Named owner and trusted boundary |
| 4. Contract | How do UI, APIs, agents and services interact and fail? | Inputs, outputs, versions, errors, replay rules |
| 5. Plan | What is the smallest reversible slice? | Working record, dependencies, rollback idea |
| 6. Execute | Does the implementation follow the accepted contract? | Cohesive change and updated decisions |
| 7. Verify | What would prove the old failure is gone? | Tests, negative cases and actual run output |
| 8. Deliver | What was merged, deployed and still unverified? | Exact source ref, runtime evidence if available, handoff |
| 9. Compound | Which repeated problem should become a reusable check? | A skill, guard, fixture or documented invariant |

A small copy change should not inherit the same ceremony as a destructive migration. Increase the verification and approval depth as authority and blast radius increase.

## A coding-agent task request

1. Read the repo-specific agent instructions and newest relevant working records.
2. Inspect the real source ref, executable paths and tests before editing.
3. State the user-visible acceptance criterion and any system-boundary contract.
4. Edit one bounded slice, revising the working record when facts change.
5. Test the legitimate path and an appropriate failure/duplicate/unauthorized case.
6. Reconcile concurrent changes; report exact commit, merge and deployment status separately.
7. Record what remains blocked or unverified; never replace evidence with confidence.

## The completion vocabulary

- **Implemented, unverified** — source exists, necessary tests have not run.
- **Test-verified** — named commands passed at a known ref/environment.
- **Merged** — the commit is reachable from the intended default branch.
- **Deployed** — target runtime publication was actually confirmed.
- **Blocked/partial** — a relevant authority, dependency or proof is missing.

A typecheck is not a network smoke test. A passing mock is not production proof. A pull request is not a merge.

## Get a reusable starting point

[The public starter](../starter/README.md) contains an adaptable agent operating contract, working-record template, boundary-contract template and release-evidence template. These files are specifications, **not a finished executable harness**. Add project-specific checks when real incidents or requirements justify them.

For public product context, read [Products in practice](PROJECTS-IN-PRACTICE.md). For the underlying skills, see [Skills](../skills/README.md). The [evidence standard](EVIDENCE.md) and [disclosure policy](DISCLOSURE-POLICY.md) apply throughout.

## Public methodology and future products

ShoStack's existing Apache-2.0 material stays open. Any future paid packaging, automated compatibility tests, maintained reference implementation or support is a distinct offering, to be evidenced and licensed transparently. No paid installer or measured performance improvement is claimed here.
