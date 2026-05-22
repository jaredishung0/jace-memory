---
id: root_agent_map
type: directory_agent
tags: [#core, #map, #index]
synopsis: "Root directory index. Entry point for all subdirectory navigation."
links: [[SELF.md]], [[HOMIE.md]], [[MEMORY.md]], [[PLAN.md]], [[TODO.md]], [[memories/AGENTS.md]]
---

# AGENTS: Root Directory Map

```
memory-system/
├── SELF.md        [identity] Agent persona — who I am
├── HOMIE.md       [identity] Jared's profile — who he is
├── MEMORY.md      [index] High-level milestones
├── PLAN.md        [plan] Implementation roadmap — read on session start
├── TODO.md        [tasks] Active task ledger
├── AGENTS.md      [map] This file — directory index
├── .obsidian/     [config] Obsidian vault settings
├── memories/      [store] Long-term memory (see memories/AGENTS.md)
├── server/        [tool] Optional FastAPI server for cross-agent access
├── .agents/       [engine] Internal system directory (no AGENTS.md here)
├── litellm_config.yaml [deferred] LiteLLM proxy config
└── .gitignore
```

**Navigation:** All root maps are 50-line capped. If you need deep context, follow the [[wiki-link]] to the leaf node. When in `memories/`, read `memories/AGENTS.md` instead of this file.
