---
name: memory-link
description: Maintain wiki-links across markdown files for Obsidian graph connectivity
---

# Memory Link Skill

## Purpose
Ensure all markdown files have proper wiki-links for Obsidian graph visualization.

## Wiki-Link Format
```
[[file-name]]           # Links to file-name.md
[[folder/file-name]]    # Links to folder/file-name.md
[[file#heading]]        # Links to heading in file
```

## Usage

```bash
# Check for broken links
./skills/memory-link/check-links.sh

# Add missing backlinks
./skills/memory-link/backlink.sh
```

## Link Patterns

### System Files (global)
- `[[PERSONA]]` → Jace character
- `[[USER]]` → Jared profile  
- `[[SYSTEM]]` → Operational instructions

### Memory Files (project)
- `[[memories/People/Jared]]` → Jared profile
- `[[memories/Skills/memory-create]]` → Memory creation skill

## Obsidian Compatibility

All links use double-bracket wiki-link syntax. Headings are underlined with `---`. 

Example:
```markdown
---
tags: [#project, #memory]
---

# Project Name

See also: [[REPO_MAP]], [[TODO]], [[SYSTEM]]
```