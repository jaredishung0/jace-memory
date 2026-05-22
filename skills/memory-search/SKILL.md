---
name: memory-search
description: Search across all memory files using ripgrep. Returns matching files with context snippets.
links: [[memory-create]], [[SYSTEM.md]]
---

# Memory Search Skill

Uses `rg` to search across `memories/` directory for relevant content.

## Usage

```bash
rg -i "search terms" memories/ --type md -C 2
```

## Post-processing

1. Extract file paths and matching lines
2. Group by memory type (people, projects, decisions, concepts, sessions)
3. Summarize findings with wiki-links to source files
4. If match is in frontmatter, highlight the key fields

## Output Format

```
## Search Results for "{query}"

### memories/sessions/2026-05-22_jace-plan-v3.md
- Line 12: "Jace's implementation plan v3..."
- Related: [[SELF.md]], [[HOMIE.md]]
```