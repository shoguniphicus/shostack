# Disclosure policy — distill the skill, not the product

ShoStack is public-facing by design. Source repositories may contain implementation that is commercially sensitive, operationally sensitive, or simply unnecessary to disclose.

The rule is:

> **Private evidence may prove a skill. Public ShoStack should teach the method without teaching the proprietary implementation.**

## Do not publish

Do not copy or closely paraphrase:

- proprietary algorithms, scoring systems, ranking logic or business thresholds;
- internal data models, field inventories or entity relationship details unique to a product;
- endpoint names, tool inventories, private routes or internal service topology;
- customer, brand, campaign, trading, product or operational data;
- source code, distinctive scripts or implementation snippets;
- private prompts, generation recipes or domain-specific agent instructions;
- credentials, secrets, account identifiers, private URLs, IPs or filesystem coordinates;
- incident details that expose an exploitable internal weakness.

## Safe abstraction levels

Prefer the property or method:

| Too specific | ShoStack-safe abstraction |
|---|---|
| exact internal route/tool inventory | capability surface is deliberately bounded |
| business scoring formula and thresholds | policy is explicit, configurable and tested |
| proprietary workflow/entity names | lifecycle is represented by explicit states |
| source-code implementation of a guard | mutating surfaces fail closed at a trusted boundary |
| exact database/storage topology | canonical state is separated from derived/cache state |
| internal retry recipe | retries are idempotent, bounded and reconciled |
| copied prompt or model recipe | generation inputs are provenance-bound and auditable |

## Evidence can remain private

ShoStack does not need a public breadcrumb to every internal file.

A maturity claim may be based on private repository review as long as the public skill:

1. states only the generalized behaviour;
2. does not require the proprietary detail to be useful;
3. is conservative about maturity;
4. can be re-audited from the source repositories when needed.

## Redaction checklist

Before committing a skill or evidence note:

1. **Reconstruction test:** could this help an outsider reconstruct a source product's architecture or business logic?
2. **Uniqueness test:** is this detail specific to one product instead of the reusable engineering method?
3. **Minimum-detail test:** can the same skill be taught with less implementation detail?
4. **Secret/privacy test:** does it expose payloads, identifiers, internal names or operational coordinates?
5. **Career-value test:** does the remaining abstraction still demonstrate a meaningful engineering capability?

If 1–4 are yes, abstract or remove. The goal is not vagueness; it is **precise engineering language at the right abstraction layer**.
