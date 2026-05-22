---
name: sync-memory
description: Sync local memory system to remote GitHub repository
---

# Sync Memory Slash Command

## Usage
```bash
/sync-memory
```

## Actions
1. `git add -A` all changes
2. `git commit -m "sync: $(date)"`
3. `git push origin master`
4. Index new files to SQLite

## Script
```bash
#!/bin/bash
cd "$(git rev-parse --show-toplevel)"
echo "Syncing to remote..."
git status --short
git add -A
git commit -m "sync: $(date +%Y-%m-%d\ %H:%M)" || echo "No changes"
git push origin master
echo "Synced."
```