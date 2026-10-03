---
name: provenance-and-promotion
category: operating
maturity: core
---

# Provenance and promotion

## Intent

Preserve where information/artifacts came from and prevent drafts/derivatives from silently becoming canonical truth.

## Use when

- ingesting external evidence;
- generating assets/content;
- curating knowledge;
- publishing;
- syncing between repositories/services;
- maintaining versions.

## Core rule

> Preserve source; derive separately; promote explicitly.

## Procedure

1. Capture raw/source material without destructive normalization where practical.
2. Assign stable identity and provenance.
3. Produce derived working artifacts separately.
4. Run the relevant validation/review gates.
5. Promote to approved/canonical state only after passing.
6. Keep publish/release as a distinct state when distribution has different requirements.
7. Pin exact revision/commit/hash for handoff when reproducibility matters.
8. Revise by new version/revision, not by erasing history.

## Non-negotiables

- A rejected derivative never becomes the next source parent.
- Approved truth and public publishing may be different states.
- Downstream projections do not overwrite provenance.
- Derived summaries should not replace the raw source.

## Verification

You can answer:

- Where did this come from?
- Which exact revision was approved?
- Which gate promoted it?
- What downstream release used it?

## Anti-patterns

- copying a draft over the source;
- treating "merged" as automatically "published";
- losing source SHA/hash on handoff;
- uncontrolled duplicate canon across formats.

## Evidence

- `alamakfarm/README.md` and `docs/WORKFLOW.md` — preserve → derive → approve → publish-ready → handoff.
- `agencyos/AGENTS.md` — correspondence linked before confirmed decision/version changes.
- `piggybankos` — decision and lifecycle receipts preserve evidence state.
- `zennith-os` — md-first canonical records with derived indexes.
