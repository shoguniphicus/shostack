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

## Deep-dive heuristics

- When exact content matters, bind execution or approval to a digest/revision so later mutation is detectable.
- Approval belongs to the specific version/reference that was reviewed, not merely to its human-readable label.
- Auditing may store hashes, sizes and source identity while redacting sensitive payload bytes.

## Evidence basis

- Observed across knowledge, workflow and creative systems where source, derived work, approval and release are separate states.
- Reinforced by revision identity, digests or receipts and gates that prevent rejected or stale derivatives becoming canonical.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
