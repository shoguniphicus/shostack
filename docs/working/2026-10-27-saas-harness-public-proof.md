# 2026-10-27 — Saas harness public methodology and product context

## Intent
Turn the existing 22 ShoStack skills into a more useful product-delivery entry point with an editable public starter and disclosure-safe context from four named products. No private product implementation is in scope.

## Baseline
- `main` and `dev` observed at `dd6920425130261f536edc28f6354388d0bde1ea`.
- README and AGENTS currently focus on portable operating skills and conservative evidence claims.
- ShoStack existing evidence/disclosure policy is authoritative.
- Higgsocean repository agent instructions explicitly reference ShoStack; Alamak and Language Gym have working-record, verification and repo-specific agent instructions.
- 9order currently links directly to GitHub rather than explaining ShoStack as the product-building system.

## Decisions
- Add SaaS delivery protocol, an original starter specification and candidate synthesis skill.
- Describe public business/product domains without reproducing client architecture, source, tools or prompts.
- Distinguish HiggsOcean active alpha from production products.
- Do not advertise an unbuilt commercial edition or claim measured reliability improvement.

## Work introduced
- `docs/SAAS-DELIVERY-SYSTEM.md` and `docs/PROJECTS-IN-PRACTICE.md`.
- `starter/` operating instructions plus working, contract and release templates.
- `skills/saas-delivery-discipline/SKILL.md` (candidate).
- README, skills index and claim-policy alignment.

## Verification and limits
- Validate Markdown template presence, disclosure-safe content, and links before writing.
- Verify resulting Git ref/PR separately from any runtime status.
- No agent runtime benchmark, production smoke test, or paid product is claimed.

## Next
Exercise the starter on a deliberately faulty, synthetic UI/API sample and publish exact before/after checks.
