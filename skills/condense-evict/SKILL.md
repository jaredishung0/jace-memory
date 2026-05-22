---
name: condense-evict
description: Condense context and evict unnecessary information when >20% threshold reached
---

# Condense-Evict Skill

## Trigger
When context window >20% occupancy.

## Actions
1. Summarize current work to session file
2. Index new files to SQLite
3. Git commit summary
4. Clear non-essential context

## Script
```bash
#!/bin/bash
echo "Context eviction triggered..."
# Write summary to memories/sessions/
# Index to SQLite
# Git commit
# Output: evict complete
echo "Context condensed. Ready for next task."
```