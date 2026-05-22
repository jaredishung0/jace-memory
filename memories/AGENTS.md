---
id: memories_dir_agent
type: directory_agent
tags: [#store, #memory]
synopsis: "Memory store directory. Contains all long-term memories organized by domain."
links: [[SELF.md]], [[HOMIE.md]], [[PLAN.md]]
---

# AGENTS: memories/

## Structure

```
memories/
├── AGENTS.md      [map] This file
├── people/        [store] People profiles, interactions, relationships
├── projects/      [store] Project-specific memories, specs, decisions
├── decisions/     [store] Design/architectural decisions
├── concepts/      [store] Learned patterns, techniques, frameworks
└── sessions/      [log] Session summaries (written every session)
```

## Rules

- Every memory is a markdown file with YAML frontmatter.
- File naming: `YYYY-MM-DD_slug-of-title.md`
- Wiki-links connect related memories. If it's related, link it.
- Tags in frontmatter for cross-cutting concerns.
- Session summaries are written every session. This is how we survive context resets.

## Active Sub-directories

- `sessions/` — latest: [[2026-05-22_memory-system-build]] — initial build + persona rewrite
- `people/` — empty (seed later via /seed-profile)
- `projects/` — empty
- `decisions/` — empty
- `concepts/` — empty
