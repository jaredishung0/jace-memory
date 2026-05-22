---
name: auto-summary
description: Generate session summary and index to memory automatically at session end
---

# Auto Summary Skill

## Purpose
End-of-session continuity: summarize key changes, index new files, evict context.

## Usage

```bash
# Run at session end
./skills/auto-summary/run.sh
```

## Actions

1. **Generate summary** → `memories/sessions/YYYY-MM-DD_slug.md`
2. **Index new files** → `python3 scripts/memindex.py index memories/sessions/*.md`
3. **Git commit** → Auto-commit summary + indexed files
4. **Context eviction** → Summary exits active context

## Integration

Add to session termination:
```bash
# Evict context
python3 scripts/memindex.py index memories/sessions/$(date +%Y-%m-%d)_*.md
git add -A && git commit -m "session: $(date +%Y-%m-%d) summary"
```