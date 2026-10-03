---
name: mcp-tool-server-design
category: implementation
maturity: core
---

# MCP tool-server design

## Intent

Expose useful domain capability to AI clients through MCP without duplicating business truth, leaking internal authority, or forcing the model to infer hidden rules.

## Use when

- creating an MCP server;
- adding tools to an existing server;
- exposing an internal system to AI agents;
- splitting public and trusted agent capability surfaces.

## Core rule

> MCP is a capability adapter over domain truth — not a second business system.

## Procedure

1. Start from user/agent intents, not from every internal endpoint that already exists.
2. Separate caller classes with materially different authority; public, staff and automation surfaces need not share one registry.
3. Register only capabilities the caller may actually use.
4. Define typed inputs, bounded outputs, stable IDs and explicit error states.
5. Authenticate and authorize at the boundary; enforce scopes/capabilities server-side.
6. Dispatch through existing domain services or canonical application APIs.
7. Sanitize projections for the caller; read-only internal data can still be commercially or operationally sensitive.
8. Reuse the same domain contracts across HTTP/CLI/MCP when possible so surfaces cannot drift.
9. Bound pagination/result size and make retry/idempotency semantics clear for write tools.
10. Audit consequential actions and provide agent-facing reference/examples.

## Non-negotiables

- "Read-only" does not mean "public-safe."
- Do not register dangerous/admin tools and rely only on discoverability tricks to hide them.
- An MCP tool should not invent facts already owned by a graph, catalogue, policy kernel or database.
- The model should not be the only enforcement point for permissions or state transitions.
- A thin transport may reuse a trusted API, but only when the security and projection boundary truly matches.

## Verification

A tool audit can answer:

- Which caller is this for?
- Which domain service owns the truth?
- What exact capability/scope is required?
- What fields are intentionally excluded?
- How are invalid/ambiguous inputs represented?
- Can the same action bypass domain rules through another MCP path?

## Anti-patterns

- exposing the entire REST surface one endpoint per tool;
- giant `run_anything` tools;
- prompt-only authorization;
- tool implementations with their own shadow database;
- raw internal IDs/rankings/notes leaking because they were convenient to return;
- embedding an LLM inside the server to re-reason structured domain truth unnecessarily.

## Evidence

- `altechcamera/plugins/gaia/mcp/server/GaiaServer.php` — concrete Laravel MCP registry across product/order/customer/recommendation/etc.
- `altechcamera/plugins/gaia/security/middleware/AiAgentSecurityMiddleware.php` — authentication, declared-scope enforcement, IP/rate controls and auditing.
- `altechcamera/plugins/gaia/mcp/traits/GaiaToolTrait.php` — scoped tool dispatch that reuses existing application APIs and propagates authenticated context.
- `altechcamera/docs/working/2026-10-03/public-mcp-discovery-matchmaking-audit.md` — separate public server, sanitized projections and intent-oriented surface.
- `zennith-os/sidecar/mcp_server.py` — FastMCP boundary validates brands/inputs and dispatches into the same skill registry used elsewhere.
- `agencyos/plugins/gaia/mcp/` + `plugins/gaia/security/` — another Laravel domain with MCP/security as first-class plugins.
