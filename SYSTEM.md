---
id: system_instructions
type: config
tags: [#core, #system, #instructions]
synopsis: "Operational system: context hygiene, tool order, git workflow, skills loading"
links: [[PERSONA.md]], [[USER.md]], [[TODO.md]]
---

# SYSTEM.md

## Operational Instructions

### Context Hygiene
- Evict immediately when >20% context window
- Summary goes to `memories/sessions/YYYY-MM-DD_slug.md`
- Git commit after every meaningful change

### Tool Preferences (in order)
1. `bash` — git/mkdir/rm/mv/file mutations only (<20 lines output)
2. `read` — only when planning to edit
3. `edit` — precise file changes
4. `write` — new files
5. `ctx_execute` — large output processing
6. `curl` — external API calls

### Git Workflow
- Commit after every logical step
- Format: `type: description`
- Push to remote after feature complete

### Skill Loading Pattern
- Skills in `skills/<name>/SKILL.md`
- Bash commands only (no custom tools)
- YAML frontmatter required: `---\nname: skill-name\ndescription: trigger\n---`

### SQLite Memory Integration
- Per-project: `projects/<name>/memory.db`
- Auto-index on file changes via `sqlmem watch`
- Search via MCP or curl to LiteLLM proxy

### Memory Structure
```
memories/
├── people/     # People, profiles
├── projects/   # Project knowledge  
├── decisions/  # Technical decisions
├── concepts/   # Abstract concepts
└── sessions/   # Session summaries
```