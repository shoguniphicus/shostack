# Coding agent operating contract (template)

Adapt these rules to your repository. Existing project instructions, data owners and approval rules take precedence.

## First read
- Read repository/nested `AGENTS.md`, `CLAUDE.md`, applicable rules, working records and authoritative contracts.
- Inspect current branch, SHA, source, tests and reachable runtime. Separate observed from planned.
- Identify what the current request authorizes; do not assume deployment or destructive-action permission.

## Required work loop
1. **Outcome:** state the business/user-visible change and what stays unchanged.
2. **Reality:** record the implemented baseline, evidence and unknowns.
3. **Authority:** identify canonical data, owners, access boundaries and approvals.
4. **Contract:** record schema, error, version, state, retry and concurrency semantics where services meet.
5. **Plan and implement:** keep a dated working record; make the smallest reversible change.
6. **Verify:** execute the relevant path and an important failure case; log command and result.
7. **Handoff:** report exact commit, merge, deployed state if actually checked, and remaining risks.

## Truth labels
"Implemented" ≠ "Tested" ≠ "Merged" ≠ "Deployed". Do not report predictions as results, nor a passing unit test as a passed target-runtime smoke test.

## Security and disclosure
Never expose credentials, internal topology, private customer material, privileged URLs, proprietary algorithms or internal prompts in public documentation. Stop for missing authorization, broken protection checks or uncertain destructive actions.

## Required records
- `docs/working/YYYY-MM-DD-task.md`
- An owner-controlled contract record for changed boundaries
- A release-evidence record when making a release claim

Do not invent framework-specific commands in this template.
