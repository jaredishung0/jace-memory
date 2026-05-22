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

## NOW

- [ ] Commit all changes (skills + plan + character updates)
- [ ] Create remote git repository + push
- [ ] Build pre-commit hook (YAML frontmatter validation)
- [ ] Build post-commit hook (REPO_MAP.txt regeneration)

## NEXT

- [ ] Create skills/seed-profile/ (ingest Jared profile)
- [ ] Create skills/memory-link/ (wiki-link maintenance)
- [ ] Create skills/litellm-query/ (curl wrapper)
- [ ] Test Agent Skills pattern with session summary

## PHASE 2 (LiteLLM proxy)

- [ ] Test LiteLLM memory K/V via curl
- [ ] Configure LiteLLM with memory-bank model
- [ ] Test A2A agent registration
- [ ] Test MCP tool access

## PHASE 3 (Postgres + Docker)

- [ ] Dockerize Postgres with restart: always
- [ ] Configure LiteLLM + Postgres connection
- [ ] Test memory K/V persistence
- [ ] Implement DB shadow protocol