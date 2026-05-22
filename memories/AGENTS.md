---
id: memories_dir_agent
type: directory_agent
tags: [#store, #memory]
synopsis: "Memory store directory. Contains all long-term memories organized by domain."
links: [[PERSONA.md]], [[USER.md]], [[SYSTEM.md]], [[ARCHITECTURE.md]]
---

# AGENTS: memories/

```
memories/
├── AGENTS.md      [map] This file
├── people/        [store] People profiles
├── projects/      [store] Project memories
├── decisions/   [store] Technical decisions
├── concepts/    [store] Learned patterns
└── sessions/    [log] Session summaries
```

All memory files use YAML frontmatter + wiki-links. Session summaries exit active context.

See: [[TODO.md]] for file structure work.