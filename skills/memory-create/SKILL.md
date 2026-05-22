---
name: memory-create
description: Create a new memory markdown file with YAML frontmatter in the memories/ directory. Use when recording decisions, sessions, or project notes that should persist across context resets.
links:
  - [[SYSTEM.md]]
  - [[TODO.md]]
  - [[memories/]]
---

# Memory Create Skill

Creates a memory file in `memories/{type}/YYYY-MM-DD_slug.md` with proper YAML frontmatter.

## Steps

1. Determine memory type from content: people, projects, decisions, concepts, sessions
2. Create slug from title (lowercase, hyphens)
3. Use `write` tool to create file with YAML frontmatter:
   - id: unique_snake_case
   - type: memory
   - tags: array of relevant tags
   - synopsis: single-sentence summary
   - links: wiki-links to related memories
4. Run `git add -A && git commit -m "memory: {title}"`

## Example

```
memories/projects/2026-05-22_jace-plan-v3.md
```

Frontmatter:
```yaml
---
id: jace-plan-v3
type: memory
tags: [#plan, #jace]
synopsis: "Jace's implementation plan v3 after Gemini conversation."
links: [[SELF.md]], [[HOMIE.md]]
---
```