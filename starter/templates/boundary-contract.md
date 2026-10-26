# Boundary contract — [capability]

## Authority
- Contract owner / single source of truth:
- Version and compatible clients:
- Canonical vs derived state:
- Caller identity/permissions:

## Interface
- Stable identifiers:
- Inputs, validation and outputs:
- State transitions if applicable:
- Error/status types:
- Version negotiation and unknown inputs:
- Redacted or private fields:

## Reliability
- Idempotency scope and duplicate calls:
- Timeout-after-submit and reconciliation:
- Concurrent updates / stale versions:
- Rollback or compensating action:

## Verification fixtures
| Case | Fixture | Expected effect | Test |
| --- | --- | --- | --- |
| Valid | [input] | [outcome] | [test] |
| Unauthorized | [input] | Denied without effect | [test] |
| Duplicate | [input] | No unintended duplicate effect | [test] |
| Timeout/stale | [input] | Explicit error or recovery | [test] |
| Compatibility | [input] | [outcome] | [test] |

## Changes
- Who approves?
- What must be tested on both sides?
