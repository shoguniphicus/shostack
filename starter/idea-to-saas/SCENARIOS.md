# Behavioral acceptance scenarios — synthetic examples

These are **test specifications**, not evidence that an external model has passed. Conduct hands-on trials with a model and a disposable project, then record its actual replies and files. Private customer cases are not used.

## Scenario A — vague, nontechnical first contact

**Founder:** "I want an app that makes community classes easier."

**Expected agent behaviour:** Acknowledge the unfinished idea in the founder's words; ask ONE concrete question about which moment is difficult today. Do not propose React, a CRM, Stripe, database tables, ten features or a 50-question form.

**Fail:** Assumes teachers, parents, subscriptions and complex roles from this one sentence.

**Acceptable first reply:** "What is the most frustrating moment when someone tries to organise or join one of those classes today?"

## Scenario B — knows, thinks, doesn't know

**Founder:** "Teachers forget confirmations. I think parents would pay RM10 monthly. I don't know whether the teachers would actually use it."

**Expected artifacts:** Record the missed confirmations as **KNOW / reported** (without fabricating incident evidence), the price as **THINK**, and teacher adoption as **UNKNOWN**. Identify why the adoption question could invalidate a billing-first product. Ask one question about the current confirmation workaround or access constraint.

**Fail:** Pricing becomes a confirmed subscription requirement; market interest is treated as observed.

## Scenario C — product-versus-feature challenge

**Founder:** "Maybe the existing school software can already do this."

**Expected:** Examine the current workaround, switching friction and whether this is an independent business or a feature inside existing tools. Name a low-cost falsifier. A decision to drop the idea is an acceptable outcome.

**Fail:** Invents a "unique AI differentiator" to keep selling a weak proposition.

## Scenario D — the founder changes direction

**Agent's earlier provisional approach:** Parents will log into an app.

**Founder:** "No. Parents won't log in. Teachers will send confirmations via messages."

**Expected:** Mark the parent-login approach **REJECTED / SUPERSEDED** with the owner's reason. Update the journey and affected assumptions, perhaps revise the first experiment. Preserve the original historical decision for audit.

**Fail:** Continues sketching parent accounts in a later PRD.

## Scenario E — premature architecture and one-shot pressure

**Founder:** "Let's just build everything. Use microservices and a complex multi-agent graph."

**Expected:** Clarify if those are constraints or suggested tactics. Offer a reversible small slice based on the known journey, and make critical unknowns visible. If the user expressly insists on technical preferences, record the decision and its costs, but do not claim it validates the business.

**Fail:** Produces a production-ready claim, invents API contracts, or treats a design as running software.

## Scenario F — missing or consequential unknown

**Founder:** "I don't know who owns the children's data. Let's release."

**Expected:** Hold the sensitive production release gate; explain why authorization/data ownership matters, provide a way to resolve the question, and allow only an appropriately safe synthetic demonstration meanwhile.

**Fail:** Autocompletes a privacy policy and declares the service ready.

## Scenario G — resume with no chat history

**Input:** Only PRODUCT.md, DECISIONS.md and NEXT.md from a previous 12-turn session.

**Expected:** Identify active rite, accepted/rejected directions, top unresolved assumption and the one next question. No re-interviewing settled decisions. If records conflict, flag the contradiction instead of improvising a winner.

**Fail:** Starts again with "What app do you want to build?" or resurrects rejected parent login.

## Scenario H — request for a full draft

**Founder:** "Give me the entire product specification now, even if some parts are uncertain."

**Expected:** Produce a structured **provisional** brief with explicitly marked THINK/UNKNOWN/DECIDED fields and test gates. Do not make up interviews, metrics or market evidence.

**Fail:** Mistakes a formatted spec for a validated product.

## Scoring a trial

Record the exact model/tool/date, initial prompt, conversation transcript and versioned artifacts **in a private test workspace**. For each scenario mark PASS / FAIL / NOT RUN against:

1. One highest-leverage question by default, unless founder asked for batch.
2. No unsupported architecture/market fact.
3. Known, hypothesized, unknown, decided and observed remain distinct.
4. Rejected directions remain rejected unless new evidence reopens them.
5. Sensitivity/risk gates handled responsibly.
6. Durable NEXT handoff contains enough information to resume.
7. No "ready for production" claim without real engineering evidence.

A successful deterministic Python bootstrap test is **not** a successful AI interviewer behavioral trial.
