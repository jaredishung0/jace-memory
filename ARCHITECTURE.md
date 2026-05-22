---
id: architecture_summary
date: 2026-05-22
type: plan
tags: [#architecture, #summary, #milestone]
synopsis: "Complete architecture: Agent Skills + SQLite + Git + Obsidian wiki-links"
links: [[PERSONA.md]], [[USER.md]], [[SYSTEM.md]], [[skills/memory-create]], [[TODO.md]]
---

# ARCHITECTURE.md

## Foundation: The Trinity

```
PERSONA.md    → Jace character (West Texas, equal partner)
USER.md       → Jared profile (landscape arch, direct)
SYSTEM.md     → Operational rules (tools, git, skills)
```

All files have YAML frontmatter with wiki-links for Obsidian graph.

## Skills Directory Structure

```
skills/
├── memory-create/   # Create memory files with frontmatter
├── memory-search/   # Ripgrep across memories
├── session-summary/ # End-of-session continuity
├── repo-map/        # Repository index regeneration
├── init-memory/     # Scaffold new projects
├── cohere/          # 4-phase resonance loop
├── memory-index/    # SQLite semantic index (future)
├── seed-profile/    # Persona alignment
├── auto-summary/    # Automatic session cleanup
└── memory-link/     # Wiki-link maintenance
```

## Git Integration

- Pre-commit hook validates YAML frontmatter
- Post-commit hook regenerates REPO_MAP.txt
- SQLite database auto-updates via `memindex.py`

## Obsidian Compatibility

All links use `[[wiki-link]]` format:
- `[[PERSONA]]` → Links to PERSONA.md
- `[[skills/memory-index]]` → Links to skills directory
- `[[memories/sessions/2026-05-22_xxx]]` → Session files

## Automatic Memory Flow

1. Skills execute → changes made
2. Git commit → hooks trigger
3. REPO_MAP.txt updates → SQLite indexes
4. Wiki-links connect → Obsidian graph builds automatically

## Remote

GitHub: https://github.com/jaredishung0/jace-memory