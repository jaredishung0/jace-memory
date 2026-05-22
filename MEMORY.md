---
id: memory_index
type: root_map
tags: [#core, #index]
synopsis: "High-level conceptual log for the memory system project."
links: [[SELF.md]], [[HOMIE.md]], [[TODO.md]]
---

# MEMORY: Project Milestones & Context

## 2026-05-21

- **Over-engineered architecture doc** reviewed and scrapped.
- **New direction:** dead-simple file-based memory system. Git-backed. LiteLLM gateway. Obsidian-visible.
- Pi's identity formalized in `SELF.md`. Jared's profile in `HOMIE.md`.
- Memory server (FastAPI) handles CRUD + recall through LiteLLM.
- Memories stored as flat markdown files with YAML frontmatter.
