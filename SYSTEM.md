---
id: system_instructions
type: config
tags: [#core, #system, #instructions, #phases]
synopsis: "Operational system: 6-phase architecture, context hygiene, tool order, git workflow"
links: [[PERSONA.md]], [[USER.md]], [[TODO.md]], [[ARCHITECTURE.md]]
---

# SYSTEM.md

## Architecture Phases

**Phase 1:** Local Markdown Files (flat, git-backed)
**Phase 2:** Hybrid Engine (uv + Postgres + Git)
**Phase 3:** Workspace Hooks (/init-memory, /seed-profile, /cohere)
**Phase 4:** CNS Resonance (4-phase verification loop)
**Phase 5:** Knowledge Graphs (Graphify, visual systems)
**Phase 6:** Security Perimeter (honeypot, forensics)

## Context Hygiene
- Evict immediately when >20% context window
- Summary → `memories/sessions/YYYY-MM-DD_slug.md`
- Git commit after every logical change

## Tool Order (CLI First)
1. `bash` — mutations only
2. `ctx_execute` — large output processing
3. `read` — only when editing
4. `edit`/`write` — file changes

## File Standards
- All root maps: 50-line hard cap
- YAML frontmatter required
- Wiki-links: `[[filename]]`, `[[folder/file]]`
- AGENTS.md in every subdirectory (except `.agents/`)

## Memory Structure
```
memories/
├── people/    # Profiles
├── projects/  # Project knowledge
├── decisions/ # Technical decisions
└── sessions/  # End-of-session archives
```

## Git Shadow Protocol
- PostgreSQL → `schema.sql` + `data_state.json`
- Git tracks text diffs, not binaries
- Background sync via `rclone crypt`