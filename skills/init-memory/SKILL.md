---
name: init-memory
description: Scaffold a new memory system project directory with root maps, memories/ structure, and Obsidian config.
---

# Init Memory Skill

Creates a new memory-system style project.

## Structure Created

```
project-name/
├── SELF.md      (scaffold - edit personal identity)
├── HOMIE.md     (scaffold - edit partner profile)  
├── MEMORY.md    (empty - milestones go here)
├── PLAN.md      (empty - strategic plan)
├── TODO.md      (empty - task tracker)
├── AGENTS.md    (empty - directory index)
├── .obsidian/
│   ├── app.json
│   └── core-plugins.json
├── memories/
│   ├── people/.gitkeep
│   ├── projects/.gitkeep
│   ├── decisions/.gitkeep
│   ├── concepts/.gitkeep
│   └── sessions/.gitkeep
└── .gitignore   (standard patterns)
```

## Initialization

```bash
mkdir -p project-name/memories/{people,projects,decisions,concepts,sessions}
touch project-name/memories/*/..gitkeep
```

## Post-scaffold

1. Initialize git repo if needed
2. Create initial commit
3. Generate REPO_MAP.txt
4. Ready for customization