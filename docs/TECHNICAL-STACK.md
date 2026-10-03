# Implementation environments

This file records broad coding environments in which the ShoStack methods have been demonstrated. It intentionally avoids mirroring dependency manifests or proprietary architecture.

Technology presence is **not** a proficiency score.

## PHP application systems

Demonstrated environment:

- PHP 8+
- Laravel 12
- October CMS 4
- relational models and migrations
- modular plugin/domain architecture
- PHPUnit-style testing
- API middleware and authorization
- container-aware development

Repeated methods include domain services, transactions, explicit lifecycle state, versioned business records and thin transport layers.

## Python operational / agent systems

Demonstrated environment:

- Python 3
- FastAPI
- Pydantic
- pytest
- CLI + HTTP + MCP surfaces
- file/record processing
- relational/derived indexes
- background jobs and health surfaces

Repeated methods include typed boundaries, canonical shared cores, atomic persistence, idempotency, fault-aware recovery and privacy-aware auditing.

## Frontend / operator systems

Demonstrated environment:

- Next.js / React / TypeScript
- Vue / JavaScript
- responsive component systems
- operational charts/tables
- client caching and live refresh

Observed methods include independent data surfaces, stale-request cancellation, cache versioning and visible health/freshness states.

## Agent interoperability

Demonstrated environment:

- MCP servers and tools
- permission-scoped agent APIs
- machine-readable contracts
- agent work queues / handoffs
- human approval boundaries
- audited actions

The skill claim is not "uses MCP." It is the design of safe, bounded agent capability over existing domain truth.

## Delivery and operations

Demonstrated environment:

- Git/GitHub review workflows
- Docker-aware runtime execution
- local hooks and local CI
- automated validators and smoke tests
- branch/revision discipline
- object/file-backed artifact workflows

## Data / knowledge modelling

Demonstrated patterns include:

- stable identities and explicit state transitions;
- revision/provenance records;
- canonical records with rebuildable indexes/caches;
- typed references;
- append/reconciliation ledgers;
- manifests and registries.

Specific source schemas, business logic and storage topology are intentionally excluded. See [the disclosure policy](DISCLOSURE-POLICY.md).
