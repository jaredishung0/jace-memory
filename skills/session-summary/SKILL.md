---
name: session-summary
description: Write a session summary to memories/sessions/ with accomplishments, decisions, and next steps.
---

# Session Summary Skill

End-of-session ritual that writes continuity to `memories/sessions/`.

## File Format

`memories/sessions/YYYY-MM-DD_topic.md`

## Content Template

```markdown
---
id: sess_{slug}
type: sessions
tags: [#session, #summary]
synopsis: "Session summary: {brief summary}"
links: [[SELF.md]], [[HOMIE.md]], [[PLAN.md]]
---
# Session: {Title}

## What Happened
{brief narrative}

## Key Decisions
- Decision 1 with rationale
- Decision 2 with rationale

## State of Projects
- Project: current status

## What's Next
1. Next task
2. Next task
```

## Post-write Actions

1. `git add -A && git commit -m "session: {topic}"`
2. Update TODO.md with next steps
3. Update MEMORY.md if milestone achieved