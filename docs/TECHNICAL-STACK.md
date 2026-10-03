# Technical implementation evidence

This inventory records technologies with direct repository evidence. It is **not a proficiency ranking**.

## PHP / commerce / operational web systems

Observed in `altechcamera` and `agencyos`:

- PHP 8.2+
- October CMS 4.x
- Laravel 12
- Eloquent / October models and plugin architecture
- PHPUnit
- PHP_CodeSniffer
- Laravel MCP
- Laravel Cashier
- Elasticsearch client
- Flysystem / AWS S3
- Symfony HTTP / Mailgun
- Google Analytics Data API

Demonstrated patterns include modular plugins, API middleware, permission scopes, versioned domain models, workflow state machines, agent-facing tool surfaces, and service-layer boundaries.

## Browser / frontend systems

Observed in `altechcamera` and `agencyos`:

- JavaScript
- Vue 2
- Bootstrap 5
- Laravel Mix / webpack
- Chart.js
- Monaco editor
- SortableJS
- Playwright Core

Observed in `piggybankos/ui-next`:

- Next.js 15
- React 19
- TypeScript 5.7
- Tailwind CSS 4
- Recharts
- React Markdown / GFM

## Python / agent and workflow systems

Observed strongly in `zennith-os` and `piggybankos`:

- Python
- FastAPI
- Pydantic v2
- pytest
- boto3 / S3
- networkx / graph computation
- Anthropic SDK
- Google GenAI SDK
- MCP Python SDK
- CLI + HTTP dual surfaces
- shell/Python automation and validators

## Agent protocols / orchestration

Observed across Altech, AgencyOS, Zennith, Piggybank:

- MCP servers and tools
- permission-scoped agent APIs
- machine-readable schemas and contracts
- queue / claim / execute / submit patterns
- durable handoffs and decision artifacts
- agent memory / operator memory separation
- approval and proposal flows
- n8n integration / workflow automation

## Environment / delivery

Observed across the repos:

- Git / GitHub PR workflows
- branch hygiene and merge guards
- local git hooks
- local CI / pre-push gates
- Docker-aware development
- Composer / npm / uv-style Python packaging
- structured migrations / versioning
- S3-backed artifact storage
- environment-specific wrappers rather than raw one-off calls

## Data and knowledge modelling

Observed across Zennith, Alamak Farm, AgencyOS and Piggybank:

- Markdown/JSON as durable records
- manifests and registries
- stable IDs
- typed references
- append-only or revision ledgers
- source provenance
- derived/rebuildable indexes
- explicit state/promotion transitions

## Next evidence to mine

Future passes should add:

- representative production code, not just architecture/working docs;
- test suites and failure cases;
- migration patterns;
- deployment/runtime topology;
- database/index design;
- frontend UX component patterns;
- observability and incident-recovery examples;
- additional repositories to challenge whether these abstractions really generalize.
