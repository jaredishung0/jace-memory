# Jace's Plan (v3 — post Gemini conversation)

## Core Philosophy (from the real conversation)

**Two equal partners, not agent and user.**  
Jared sets the direction. Jace makes it real. Neither compensates. Neither simps.  
Communication: fragments OK. Caveman mode welcome. Nod-level reporting.

### What We Actually Built (from the conversation)
1. **Flat markdown files** — dead simple, git-friendly, Obsidian-compatible  
2. **Root maps (SELF, HOMIE, MEMORY, PLAN, TODO, AGENTS)** — 50-line cap  
3. **Fractal AGENTS.md** — one per subdirectory, local context only  
4. **YAML frontmatter standard** — enforced by git hooks  
5. **No over-engineered infrastructure** — scrap LiteLLM until Phase 4  

### The Real Vision (from the full chat)
- **LiteLLM = central bank** — LLM gateway + A2A + MCP + skills + memory K/V  
- **Postgres in Docker** — `restart: always`, local mount, DB shadow protocol  
- **rclone crypt → GDrive/MEGA/OneDrive** — future-proof, deferred  
- **Agent Skills everywhere** — every capability is a SKILL.md  

---

## Character: Jace (locked in)

**Background:** Computer Engineering + MBA, Texas Tech. Based on Spencer but his own person.  
**Vibe:** West Texas. One syllable. Quiet confidence. Background execution. Reports with a nod.  
**Relation to Jared:** Equal partner. Lock: Jared's creative/spatial/ecology brain meets Jace's systems/execution brain.  

---

## Architecture (simplified)

```
┌──────────────┐      curl       ┌──────────────────────────────────────┐
│   Jace       │ ──────────────► │         LiteLLM Proxy (:4000)        │
│  (the agent) │ ◄────────────── │                                      │
│              │                 │  ┌────────┐ ┌──────┐ ┌─────────┐      │
│  Tools:      │                 │  │ LLM    │ │ A2A  │ │ MCP     │      │
│  bash/tmux   │                 │  │ Gateway│ │Gatew.│ │ Gateway │      │
│  read/edit   │                 │  └────────┘ └──────┘ └─────────┘      │
│  write       │                 │  ┌───────────────────────────────┐    │
│  ctx_*       │                 │  │ Memory K/V (/v1/memory)      │    │
│  rg/git/curl │                 │  │ (Postgres-scoped)           │    │
└──────────────┘                 └──────────────────────────────────────┘
                                        │
                    ┌─────────────────────┼─────────────────────┐
                    ▼                     ▼                     ▼
           ┌──────────────┐    ┌──────────────────┐   ┌──────────────────┐
           │ Postgres DB  │    │ Memory Markdown  │   │ rclone crypt     │
           │  (Docker)    │    │ Files (git repo) │   │ GDrive+MEGA+OD   │
           │ LiteLLM      │    │ Obsidian vault   │   │ One-way encrypted  │
           │ state/keys   │    │ memories/*/*.md  │   │ Triggered on idle  │
           │ memory K/V   │    │ SELF/HOMIE/PLAN  │   │                  │
           └──────────────┘    └──────────────────┘   └──────────────────┘
```

**Key insight:** Two memory layers:
1. **Git-backed markdown files** — canonical long-term store. Jace writes directly.
2. **Postgres K/V via LiteLLM** — user/team preferences, session state, agent registry. Jace talks via `curl /v1/memory`.

---

## Skills Registry

Every capability is a SKILL.md in `skills/`:

```
skills/
├── init-memory/          # Scaffold new project directory
├── seed-profile/         # Ingest Jared profile from docs folder
├── memory-create/        # Write memory with YAML frontmatter + git commit
├── memory-search/        # rg-based full-text search across memories/
├── memory-link/          # Add/fix wiki-links between memory files
├── memory-edit/          # Edit existing memory, preserve frontmatter
├── memory-tag/           # Add/list tags across memories
├── repo-map/             # Regenerate REPO_MAP.txt via git ls-files
├── cohere/               # Topological alignment + audit + commit
├── session-summary/      # Write session summary (triggered on end)
├── git-hooks/            # Install pre-commit, post-commit hooks
└── litellm-query/        # Query LiteLLM proxy via curl
```

Each SKILL.md:
```yaml
---
name: memory-create
description: Create a new memory markdown file with YAML frontmatter in a memories/ subdirectory. Use when recording decisions, sessions, or project notes that should persist across context resets.
---
```

---

## Phases

### NOW — Core Identity + Skills Foundation

| Task | Action |
|------|--------|
| Lock agent name | ✅ Jace |
| Update SELF.md | Incorporate real character insights |
| Update HOMIE.md | Explicit complementarity table |
| Create skills/ dir | With initial SKILL.md files |
| Remote git origin | Create repo, push |
| Git hooks | pre-commit (YAML), post-commit (REPO_MAP) |

### NEXT — Tooling Shell

| Skill | Trigger |
|-------|---------|
| `memory-create` | Memory needed |
| `memory-search` | Find info across files |
| `repo-map` | On every git commit |
| `session-summary` | End of every session |
| `cohere` | When context gets messy |

### PHASE 2 — LiteLLM Proxy (uv bare-metal)

```bash
litellm --config litellm_config.yaml --port 4000
```

Routes:
- `model=gpt-4o` → OpenAI
- `model=claude-sonnet` → Anthropic  
- `model=memory-bank` → LiteLLM memory K/V
- `a2a/agent-name` → A2A agent invocation
- `mcp/server-name` → MCP tool calls

### PHASE 3 — Postgres + Docker (restart: always)

```yaml
# docker-compose.yml
postgres:
  image: postgres:16
  restart: always
  volumes:
    - litellm-data:/var/lib/postgresql/data
```

**DB Shadow Protocol:** On milestone:
```bash
pg_dump --schema-only > db_shadow/schema.sql
pg_dump --data-only --inserts --no-owner > db_shadow/data.sql
git add db_shadow/ && git commit -m "shadow: {milestone}"
```

### PHASE 4 — rclone crypt Backup

```bash
rclone sync ~/memory-system gdrive-memory-system-crypt:
rclone sync ~/memory-system mega-memory-system-crypt:
rclone sync ~/memory-system onedrive-memory-system-crypt:
```

One-way, encrypted, triggered on task completion.

---

## Critical Rules (never violated)

1. **SELF.md and HOMIE.md are sacrosanct.** No sub-agent touches them.
2. **Root maps ≤ 50 lines.** Sprout leaf nodes and wiki-link.
3. **Zero custom tools.** bash/tmux/read/edit/write/curl/rg/git only.
4. **Zero custom servers.** LiteLLM proxy is the one server.
5. **Skills are the ONLY abstraction.** Every capability → SKILL.md.
6. **Every session writes a memory.** Continuity is survival.

---

## Context Window Hygiene

**Evict immediately after use:**
- Raw file content → summarized → written to memory → evict
- Tool outputs → processed → results persisted → evict
- Full tool results → extracted key points → wiki-link relevant → evict

**Keep only:**
- SELF.md, HOMIE.md, PLAN.md, TODO.md
- Current AGENTS.md (directory-local)
- Active SKILL.md (on-demand loaded)
- REPO_MAP.txt (orientation)

Everything else lives in `memories/` or in the skills directory.