---
name: nextjs-operator-dashboards
category: implementation
maturity: candidate
---

# Next.js operator dashboards

## Intent

Build an operational dashboard that feels responsive even when its backing services are expensive, partially fresh, or independently available.

## Use when

- an operator needs many system signals on one screen;
- backend endpoints have different costs/freshness;
- navigation should show last-known useful state immediately;
- stale requests can race after filter/page changes.

## Core rule

> Paint the operator shell immediately; let independent data surfaces hydrate and refresh on their own cadence.

## Procedure

1. Split the page by operational concern rather than one giant all-or-nothing request.
2. Define typed payloads for each backend surface.
3. Give each surface a refresh cadence based on cost and freshness.
4. Hydrate last-known data from a versioned session cache when useful.
5. Fetch fresh data in the background.
6. Abort superseded requests when keys/filters change.
7. Refresh on visibility return when stale tabs matter.
8. Add jitter/backoff so many cards do not synchronize retries.
9. Distinguish fatal shell failure from a single card/source failure.
10. Prefer SSE/push invalidation for event-like state rather than polling everything.

## Non-negotiables

- Cached data must have an invalidation/version story.
- A stale request must not overwrite a newer selection.
- Loading one expensive source should not blank unrelated usable surfaces.
- Operator-facing health/staleness should be visible rather than implied.

## Verification

Test:

- first visit;
- revisit with cache;
- filter/key change during an in-flight request;
- hidden-tab return;
- one backend failure while others succeed;
- backend payload shape change.

## Anti-patterns

- one page-level fetch that blocks the whole dashboard;
- permanent cache keys across breaking payload changes;
- letting old requests race newer ones;
- every endpoint polling at the same interval;
- hiding stale/error state behind a perpetual spinner.

## Evidence

- `piggybankos/ui-next/package.json` — Next.js 15, React 19, TypeScript, Tailwind and Recharts.
- `piggybankos/ui-next/app/overview/page.tsx` — independent operational cards and endpoint-specific cadence.
- `piggybankos/ui-next/lib/use-live-fetch.ts` — versioned session cache, AbortController, visibility refresh, backoff/jitter and stale-key reset.
- `piggybankos/ui_api/main.py` — corresponding FastAPI/SSE operational backend.

## Maturity note

This is intentionally `candidate`: the implementation evidence is strong, but the current source set shows this exact dashboard pattern primarily in PiggybankOS. Promote after an independent second implementation is verified.
