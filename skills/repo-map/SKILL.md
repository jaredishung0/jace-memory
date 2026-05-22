---
name: repo-map
description: Regenerate REPO_MAP.txt showing directory structure with file type annotations.
---

# Repo Map Skill

Aider-inspired index generator at `.agents/brain/REPO_MAP.txt`.

## Command

```bash
git ls-files | sort | awk '
BEGIN { print "memory-system/" }
{
  depth = gsub(/\//, "/")
  indent = ""
  for (i = 1; i < depth; i++) indent = indent "  "
  if (/\.md$/) print indent "├── " $0 "  [doc]"
  else if (/\.py$/) print indent "├── " $0 "  [code]"
  else if (/\.yaml|\.yml$/) print indent "├── " $0 "  [config]"
  else print indent "├── " $0
}' > .agents/brain/REPO_MAP.txt
```

## Format

```
memory-system/
├── SELF.md  [identity] Agent persona
├── HOMIE.md  [identity] Jared's profile
├── skills/  [tool] Agent skills
│   └── memory-create/  [dir] Create memory skill
└── memories/  [store] Long-term memory
```

## Post-action

Add and commit the regenerated map: `git add .agents/brain/REPO_MAP.txt && git commit --amend --no-edit`