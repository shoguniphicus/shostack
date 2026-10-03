# Second deep-dive skill distillation — Progress Log (2026-10-03)

## Scope

- Re-audit the supplied source repositories at implementation/test/operations depth.
- Enrich ShoStack skills from recurring engineering behaviour, not proprietary product mechanics.
- Redact the first-pass public evidence where it exposes internal architecture more specifically than needed.
- Add a durable disclosure rule so future skill mining keeps private implementation details private.

## Public-distillation rule

Private source material may be inspected as evidence, but ShoStack should publish only the transferable method.

Do **not** copy into ShoStack:

- internal endpoint inventories, tool counts, route names or credentials;
- proprietary algorithms, scoring formulas or business thresholds;
- customer/product-specific data models or workflow names;
- private storage layouts, internal service names or operational topology unless genericized;
- source code or distinctive implementation snippets;
- secrets, identifiers, account details, private URLs or infrastructure coordinates.

Prefer statements like:

- "explicit state machines constrain workflow transitions";
- "agent capability surfaces are permission-bounded";
- "derived indexes are rebuildable from canonical records";
- "retry/recovery is idempotent and bounded";

instead of reproducing how a specific product implements those ideas.

## Questions for this pass

1. Which skills are still too shallow or generic?
2. Which repeated skills are missing entirely?
3. Which first-pass evidence should be abstracted/redacted?
4. Which practices appear in code/tests/operations rather than only in documentation?
5. What would another senior engineer or coding agent need to reproduce the method?

## Status

Deep implementation review in progress.
