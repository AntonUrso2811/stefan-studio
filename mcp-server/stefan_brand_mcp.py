#!/usr/bin/env python3
"""
stefan-brand-mcp — Local MCP server exposing Urso & Co canonical brand content.

Runs on Anton's Mac as a launchd agent. Exposes tools to any Claude surface
(Claude Code, Cowork sessions) that registers this MCP server. Reads content
directly from the filesystem — data never leaves the machine.

Architecture:
    GitHub (AntonUrso2811/stefan-studio, private)
        │ launchd pulls every 10 min
        ▼
    ~/projects/stefan-studio/  (canonical clone)
        │ this MCP server reads files here
        ▼
    Any Claude surface that registers this MCP server
        gets tools like get_foundation_brief, get_copy_bank,
        get_voice_system, invoke_copy_urso.

Transferability: to spin this up for a new client (e.g. Stefan),
copy this file, change REPO_ROOT and SERVER_NAME, point launchd at
the new script. Each client gets its own MCP server process.
"""

from __future__ import annotations

import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# ─── Configuration ────────────────────────────────────────────────────────────

SERVER_NAME = "stefan-brand"

# Resolve repo root. Prefer env var override, fallback to default Mac location.
REPO_ROOT = Path(os.environ.get(
    "URSO_STUDIO_PATH",
    str(Path.home() / "projects" / "stefan-studio"),
)).expanduser().resolve()

# ─── Server ───────────────────────────────────────────────────────────────────

mcp = FastMCP(
    SERVER_NAME,
    # Disable MCP's built-in DNS rebinding protection — Cloudflare Tunnel
    # is our access control boundary and the default allowed-hosts list
    # ["127.0.0.1:*", "localhost:*", "[::1]:*"] rejects tunnel requests.
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    ),
)


def _read(rel_path: str) -> str:
    """Read a repo-relative file. Raises with a clear message if missing."""
    full = REPO_ROOT / rel_path
    if not full.exists():
        raise FileNotFoundError(
            f"{SERVER_NAME}: {rel_path} not found at {full}. "
            f"Check that {REPO_ROOT} is a valid clone of stefan-studio."
        )
    return full.read_text(encoding="utf-8")


# ─── Tools — canonical brand content ──────────────────────────────────────────

@mcp.tool()
def get_project_rules() -> str:
    """Return project-rules.md — the machine-readable hard rules: locked
    hero tagline, refused vocabulary (10 words), banned CTAs (5),
    language conventions (UK English), visual hard rules, copy rules,
    session-start ritual. Read this FIRST in any fresh session.
    """
    return _read("project-rules.md")


@mcp.tool()
def get_brand_index() -> str:
    """Return brand-kit/INDEX.md — per-document jurisdiction and
    tiebreak order for the three brand documents (foundation-brief,
    component-copy-bank, voice-system-v1). Resolves any doc-on-doc
    disagreement.
    """
    return _read("brand-kit/INDEX.md")


@mcp.tool()
def get_foundation_brief() -> str:
    """Return brand-kit/01-docs/foundation-brief.md — positioning,
    archetype, audience, commercial model, offer ladder, canonical
    refused-vocabulary list. Status: READY. Version: v1.5.
    """
    return _read("brand-kit/01-docs/foundation-brief.md")


@mcp.tool()
def get_copy_bank() -> str:
    """Return brand-kit/01-docs/component-copy-bank.md — every on-voice
    string that ships (CTAs, section headers, pricing, microcopy) plus
    the banned-CTA list. Canonical home of the hero tagline.
    """
    return _read("brand-kit/01-docs/component-copy-bank.md")


@mcp.tool()
def get_voice_system() -> str:
    """Return brand-kit/01-docs/voice-system-v1.md — the seven voice
    principles and method IP. INTERNAL ONLY: use as quality constraint,
    never surface the framework mechanics (step numbers, Fingerprint,
    calibration cadences, failure-mode taxonomy) in user-facing output.
    """
    return _read("brand-kit/01-docs/voice-system-v1.md")


# ─── Tools — skills ───────────────────────────────────────────────────────────

@mcp.tool()
def get_copy_skill() -> str:
    """Return skills/copy/SKILL.md — the universal craft skill that
    /copy-urso wraps. Four-stage pipeline: Copywriter → Copy Chief →
    QC (8.5+ gate) → Humanizer.
    """
    return _read("skills/copy/SKILL.md")


@mcp.tool()
def get_copy_urso_skill() -> str:
    """Return skills/copy-urso/SKILL.md — the Urso brand-overlay skill.
    Wraps /copy with the brand foundation, Copy Bank, and Voice System
    quality checks. Invoked for any string that will ship under the
    Urso & Co name.
    """
    return _read("skills/copy-urso/SKILL.md")


# ─── Tools — operational ──────────────────────────────────────────────────────

@mcp.tool()
def get_operations_plan() -> str:
    """Return OPERATIONS-PLAN.md — the single source of truth for how
    the studio operates across Claude Design, Claude Code, and Cowork.
    Includes the five rules of ongoing operation and the session-start
    ritual.
    """
    return _read("OPERATIONS-PLAN.md")


@mcp.tool()
def list_brand_files() -> str:
    """Return a tree of brand-kit/ contents — useful when exploring
    what's available beyond the three canonical docs.
    """
    import subprocess
    result = subprocess.run(
        ["find", "brand-kit", "-type", "f", "-not", "-path", "*/.git/*"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


@mcp.tool()
def get_freshness() -> str:
    """Return the canonical clone's current HEAD commit and how recent
    it is. Use this at session start to confirm the MCP server is
    reading fresh content. If HEAD is older than expected, check
    launchd agent 'co.ursoandco.stefan-studio-pull'.
    """
    import subprocess
    result = subprocess.run(
        ["git", "log", "-1", "--format=%h %cr %s"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return f"stefan-studio HEAD: {result.stdout.strip()}\nRepo path: {REPO_ROOT}"


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Transport selection via env var or CLI flag.
    # Default: stdio (for Claude Code local invocation).
    # Set URSO_MCP_TRANSPORT=http or pass --http to expose over HTTP for remote clients (Cowork).
    import sys
    transport = os.environ.get("URSO_MCP_TRANSPORT", "stdio")
    if "--http" in sys.argv or transport == "http":
        # Streamable-HTTP transport — the standard for remote MCP clients
        # (Claude.ai custom connectors). Binds to 0.0.0.0:8765 by default so
        # it's reachable via Cloudflare Tunnel / ngrok from Cowork.
        # Endpoint path: /mcp/ (with trailing slash).
        port = int(os.environ.get("URSO_MCP_PORT", "8765"))
        host = os.environ.get("URSO_MCP_HOST", "0.0.0.0")
        mcp.settings.host = host
        mcp.settings.port = port
        mcp.settings.stateless_http = True  # simpler semantics for remote clients
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")
