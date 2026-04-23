# stefan-brand-mcp

Local MCP server exposing Urso & Co canonical brand content to any Claude surface (Claude Code, Cowork). Content stays on your Mac — data never leaves the machine.

## What this gives you

Every Claude surface that registers this MCP server gets these tools **automatically on every session**, with zero per-session friction:

| Tool | Returns |
|---|---|
| `get_project_rules` | `project-rules.md` — machine-readable hard rules |
| `get_brand_index` | `brand-kit/INDEX.md` — per-doc jurisdiction + tiebreak |
| `get_foundation_brief` | Brand foundation v1.5 |
| `get_copy_bank` | Component Copy Bank — on-voice strings + banned CTAs |
| `get_voice_system` | Voice System v1 (internal IP — use as constraint) |
| `get_copy_skill` | Universal `/copy` skill source |
| `get_copy_urso_skill` | Urso brand-overlay `/copy-urso` skill source |
| `get_operations_plan` | OPERATIONS-PLAN.md |
| `list_brand_files` | Tree of `brand-kit/` |
| `get_freshness` | HEAD commit + how recent (for session-start freshness check) |

The server reads directly from `~/projects/stefan-studio/` — which launchd keeps fresh via `git pull` every 10 minutes, plus the Claude Code SessionStart hook pulls on every new session.

## Install (one-time, on this Mac)

```bash
cd ~/projects/stefan-studio/mcp-server
uv sync
```

This creates a virtualenv with the MCP SDK.

## Register in Claude Code

Add to `~/.claude/settings.json` under a top-level `mcpServers` key:

```json
{
  "mcpServers": {
    "stefan-brand": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/antonurso/projects/stefan-studio/mcp-server",
        "run",
        "python",
        "stefan_brand_mcp.py"
      ]
    }
  }
}
```

Restart Claude Code. Tools appear under the `mcp__stefan-brand__*` prefix.

## Register in Cowork

Cowork's MCP registration lives in its settings UI — look for "MCP Servers" or "Custom tools" in Cowork's preferences panel. Point it at the same command above. Cowork handles the subprocess lifecycle.

If Cowork only supports remote MCP servers, wrap this one behind an SSH tunnel or use Anthropic's hosted MCP proxy (roadmap item).

## Verify

From any Claude surface after registration:

> Call `mcp__stefan-brand__get_freshness` to confirm the server is live and reading the latest commit.

Expected: `stefan-studio HEAD: <short-sha> <relative-time> <subject>`.

## Configuration — override repo path

The server reads from `~/projects/stefan-studio` by default. Override with:

```bash
export URSO_STUDIO_PATH=/path/to/your/clone
```

This is what makes the pattern transferable. For a new client, copy this folder, update the env var (or hardcode `REPO_ROOT`), run on the same machine. Each client gets its own MCP server process, its own canonical repo, its own tools.

## Transferability — spin up for a new client

To create `stefan-brand-mcp`:

```bash
cp -r ~/projects/stefan-studio/mcp-server ~/projects/stefan-studio/mcp-server
cd ~/projects/stefan-studio/mcp-server
# Edit stefan_brand_mcp.py: change SERVER_NAME from "stefan-brand" to "stefan-brand"
# Rename stefan_brand_mcp.py to stefan_brand_mcp.py (optional — server name is the canonical identifier)
uv sync
```

Register in Claude Code / Cowork as a separate MCP server. Tools namespace under `mcp__stefan-brand__*`. Both servers can run simultaneously — no conflict.

## Architecture (why this is the right pattern)

- **Single write path.** Only Claude Code commits to `stefan-studio`. Every surface reads the same commit.
- **Launchd keeps the clone fresh.** `co.ursoandco.stefan-studio-pull` pulls every 10 min.
- **MCP reads live files.** No caching, no staleness. Every tool call reads the current disk state.
- **Content never leaves your Mac.** Voice System IP stays on the machine; the MCP server only serves Claude surfaces that registered it.
- **Transferable.** Template this directory for any future client. One MCP process per client. Isolated, per-brand.
