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

## Deep-dive heuristics

- Model trust at the MCP boundary itself; never rely on apparent network origin supplied by a proxy or local UI.
- Separate safe read capabilities from mutating capabilities so observability can remain available during enforcement failures.
- Audit tool calls without storing secrets or unnecessarily copying user payloads.
- Test that an unauthorized caller cannot reach a write through an alternate generic tool.

## Evidence basis

- Observed across independent MCP implementations that keep domain truth outside the protocol adapter and enforce capability boundaries server-side.
- Reinforced by authentication, input validation, safe projections, bounded capabilities and transport-parity tests.
- Source implementation details are intentionally omitted under [the disclosure policy](../../docs/DISCLOSURE-POLICY.md).
