# Second deep-dive skill distillation — Progress Log (2026-10-03)

## Scope

- Re-audit the source systems at implementation, test and operations depth.
- Enrich ShoStack from recurring engineering behaviour, not proprietary product mechanics.
- Redact first-pass public evidence that exposed more internal architecture than necessary.
- Add a durable disclosure rule for future skill mining.

## Disclosure decision

Private implementation may be inspected as evidence, but public ShoStack records only the transferable property.

Excluded from public skill artifacts:

- internal endpoint or tool inventories;
- proprietary algorithms, scores and business thresholds;
- product-specific data models and workflow names;
- private storage/runtime topology;
- source snippets and private prompts;
- secrets, identifiers and operational coordinates.

## Deep-dive findings

The first pass captured process well but compressed several distinct system skills into generic "safety" or "verification."

The second pass found repeated implementation/test evidence for:

1. **Idempotent recovery & reconciliation** — repeated work converges instead of duplicating effects.
2. **Atomicity & race resistance** — writes and concurrent work protect against torn state and stale ownership.
3. **Failure-oriented testing** — tests target bug classes, bypasses, corruption and concurrency rather than only happy paths.
4. **Authority & approval design** — proposal, approval, execution and publication are separate authorities bound to exact state/version.
5. **Honest degradation** — optional replicas/caches may degrade; authoritative truth or permission failures block.
6. **Derived-state & cache discipline** — caches/indexes are disposable and visibly stale, not shadow truth.
7. **Privacy-aware observability** — audits preserve diagnostic value while redacting secrets/private payloads.

## Existing skills enriched

The deeper pass also strengthened:

- evidence-gated verification with counterfactual and fault-injection thinking;
- guardrails-as-code with deny-unknown mutation boundaries;
- canonical chokepoints with bypass audits and class-level migrations;
- contracts with replay, concurrency and authority semantics;
- bounded reversible change with staged execution modes;
- agent-native design with explicit authority independent of apparent locality;
- provenance with digest/version binding;
- compound engineering with class-level regression nets;
- environment fidelity with real-runtime integration checks.

## Public cleanup

The first-pass path-by-path evidence map and source-specific evidence sections were replaced by:

- an evidence methodology;
- abstract evidence-basis sections;
- a disclosure policy;
- broad implementation-environment descriptions.

The intent is to prove the skill without publishing the source products' internal recipes.

## Disclosure audit

The final `main…dev` added-line audit checked for source-project names, internal code-path markers, internal operator/brand identifiers and distinctive product-specific identifiers.

**Result: PASS.** None of those markers appear in the newly added public lines.

This is deliberately stricter than checking only for secrets: the goal is to avoid leaking reconstructable proprietary architecture even when the underlying source repositories are available to the auditor.

## Validation

- New skill files are procedural, bounded and usable without source-project knowledge.
- Maturity remains conservative: derived-state/cache discipline is `repeated`, and the existing operator-dashboard skill remains `candidate`.
- Existing skill evidence sections no longer publish internal repository paths.
- The disclosure policy is now part of the mandatory ShoStack read order.
- The branch is ready for final `main…dev` comparison and reviewed merge.
