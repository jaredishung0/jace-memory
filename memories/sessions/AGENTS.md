---
id: sessions_dir_agent
type: directory_agent
tags: [#log, #sessions]
synopsis: "Session summaries — written every session for cross-session continuity."
links: [[MEMORY.md]]
---

# AGENTS: memories/sessions/

Session continuity. Every time I (the agent) run a session with Jared, I write a summary here. This is how we survive context resets — future sessions read the latest summaries to know where we are.

## Active

- [[2026-05-22_memory-system-build]] — initial build + persona rewrite
- [[2026-05-22_memory-system-kickoff]] — first memory written

## Rules

- File naming: `YYYY-MM-DD_topic.md`
- Include: what was accomplished, key decisions, project state, what's next
- Link to related project files
- Write this LAST, before session ends
- future sessions: read the latest 2-3 summaries + MEMORY.md for orientation
