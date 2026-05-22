---
id: task_ledger
type: root_map
tags: [#core, #tasks]
synopsis: "Active task ledger. Skills drive everything."
links: [[JACE_PLAN.md]], [[MEMORY.md]]
---

# TODO

## DONE

- [x] Create JACE_PLAN.md v3 with Agent Skills foundation
- [x] Update SELF.md with Jace character + lock
- [x] Update HOMIE.md with explicit complementarity table
- [x] Create skills/ directory with 6 core SKILL.md files
- [x] Add Conversation with Gemini.txt to repo
- [x] Create PERSONA.md, USER.md, SYSTEM.md (foundation trinity)
- [x] Create skills/seed-profile, skills/memory-index
- [x] Push to GitHub: jaredishung0/jace-memory

## NOW

- [ ] Build pre-commit hook (YAML frontmatter validation)
- [ ] Build post-commit hook (REPO_MAP.txt regeneration)
- [ ] Install sqlmem CLI, init memory.db
- [ ] Run initial indexing of all memories

## NEXT

- [ ] Create skills/memory-link/ (wiki-link maintenance)
- [ ] Create skills/litellm-query/ (curl wrapper)
- [ ] Test Agent Skills pattern with session summary
- [ ] Add USER.md to memory index

## PHASE 2 (SQLite Memory)

- [ ] Configure sqlmem with local embedding model
- [ ] Run `sqlmem watch` for automatic reindexing
- [ ] Test semantic search across memories
- [ ] MCP integration for tool access

## PHASE 3 (LiteLLM Proxy - optional)

- [ ] SQLite backend for K/V memory
- [ ] Redis cache for cost reduction
- [ ] Teams = landscape/freelance/research contexts
- [ ] A2A/MCP gateway via LiteLLM