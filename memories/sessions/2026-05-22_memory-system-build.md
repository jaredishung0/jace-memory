---
id: sess_first_build
type: sessions
title: Memory System Initial Build
created: 2026-05-22T02:15:00Z
updated: 2026-05-22T02:15:00Z
tags:
  - build
  - setup
  - architecture
links:
  - [[SELF.md]]
  - [[HOMIE.md]]
  - [[MEMORY.md]]
  - [[TODO.md]]
---
# Memory System Initial Build

## Summary

Scaffolded the file-based memory system from scratch. Jared and I agreed the original architecture doc was way over-engineered. Stripped it down to:

- Flat markdown files with YAML frontmatter
- Git-backed with auto-commit on writes
- LiteLLM proxy routing `memory-bank` model to the server
- Obsidian vault config for graph visibility
- Root maps: SELF.md, HOMIE.md, MEMORY.md, TODO.md

## Decisions

- **No Postgres.** SQLite for LiteLLM (default), flat files for memories.
- **No Docker.** Memory server runs bare-metal via uv.
- **Retrieval first, infra later.** rg-based full-text search for MVP. Semantic recall later.
- **OpenAI-compatible endpoint** on memory server so LiteLLM can route to it natively.

## Memory Store

All memories go in `memories/{type}/YYYY-MM-DD_slug.md`. Types: people, projects, decisions, concepts, sessions.
