---
name: compound-engineering
category: operating
maturity: core
---

# Compound engineering

## Intent

Make each solved problem reduce the cost and risk of solving the next similar problem.

## Use when

- a pattern repeats;
- the same review comment occurs more than once;
- an agent repeatedly needs the same instructions;
- a manual recovery procedure stabilizes;
- a one-off script becomes operationally important.

## Core rule

> Do not repeatedly pay for the same lesson; crystallize it into reusable capability.

## Procedure

1. Finish the immediate problem first.
2. Identify what was general versus incident-specific.
3. Choose the lightest durable form:
   - helper;
   - test;
   - validator;
   - skill;
   - template;
   - hook;
   - runbook;
   - canonical service;
   - registry/config.
4. Give the reusable artifact one clear responsibility.
5. Wire it into the normal path so use does not depend on memory.
6. Add evidence/acceptance criteria.
7. Retire or merge the artifact if later evidence shows duplication.

## Non-negotiables

- Do not create abstractions before a real pattern exists.
- Reuse canonical infrastructure instead of creating a second framework for the reusable form.
- A "skill" must be executable enough to change behaviour.

## Verification

The next similar task should require less bespoke reasoning, fewer repeated instructions, or a smaller failure surface.

## Anti-patterns

- permanent one-off scripts with no owner;
- copied prompts in many repos;
- runbook that is never wired into startup/normal workflow;
- hundreds of overlapping skills with no canonical route.

## Evidence

- `zennith-os/skills/` and AGENTS pipeline — repeated operations crystallized into executable skills and hooks.
- `alamakfarm/skills/` — production gates and generation procedures captured as skills.
- `piggybankos/workflows/` and `routines/` — recurring work materialized as artifacts.
- `altechcamera/docs/agent-workspace/` — tool references/workflow recipes packaged for repeated agent operation.
