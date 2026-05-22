---
name: init-memory
description: Initialize memory-system in new project folder with fractal AGENTS.md
---

# Init Memory Slash Command

## Usage
```bash
/init-memory
```

## Actions
1. Create `.agents/` directory with SELF.md, HOMIE.md, SYSTEM.md
2. Sprout AGENTS.md in all subdirectories
3. Initialize git repo with hooks
4. Generate base memory structure

## Script
```bash
#!/bin/bash
echo "Initializing memory-system..."
mkdir -p .agents memories/{people,projects,decisions,concepts,sessions}
# Copy template files from skills/init-memory/
cp -r ~/.pi/agent/skills/memory-system/AGENTS.md .agents/
git init
echo "Done."
```