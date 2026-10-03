---
name: working-doc-driven-development
category: operating
maturity: core
---

# Working-doc-driven development

## Intent

Keep the problem statement, decisions, implementation reality and verification in one evolving artifact.

## Use when

Work is substantial enough to change architecture, behaviour, data, workflows, runtime operations, or future understanding.

## Core rule

> The working record starts before the code and changes while the work changes.

## Procedure

1. Create/open a dated working record.
2. Write scope, constraints, success criteria and initial approach.
3. Record evidence and decisions at meaningful checkpoints.
4. Update the plan when reality invalidates it; do not preserve a fake original plan.
5. Link code, tests, PRs, proposals, receipts or artifacts.
6. Finish with what actually changed, what was verified, what remains unresolved, and what should be promoted into durable docs.

## Non-negotiables

- Do not reconstruct all reasoning after implementation.
- Do not call work complete while the working record still describes an obsolete plan.
- Separate unresolved steering from completed history.

## Verification

The doc should let a new agent resume without replaying the whole conversation and should explain why the resulting code differs from obvious alternatives.

## Anti-patterns

- "code first, docs later";
- giant undated scratchpad;
- completion record with no test/result evidence;
- keeping already-resolved TODOs as if they were future work.

## Evidence

- `altechcamera/AGENTS.md` — mandatory dated working docs.
- `piggybankos/AGENTS.md` — explicit work tracking protocol and template.
- `agencyos/docs/working/` — phase plans, audits, handoffs and completions.
- `zennith-os/docs/working/` — extensive implementation and recovery records.
