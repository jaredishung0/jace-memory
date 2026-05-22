---
name: seed-profile
description: Ingest and index user profile for automatic persona alignment
---

# Seed Profile Skill

## Purpose
Create USER.md and index it for automatic persona matching in all interactions.

## Usage

```bash
# Interactive profile creation
./skills/seed-profile/run.sh

# This creates:
# - USER.md (this file)
# - Index in memory.db
# - Preferences in LiteLLM K/V
```

## Profile Template

```yaml
---
name: user-profile
type: identity
tags: [#profile, #preferences, #communication]
synopsis: "User identity, preferences, and communication patterns"
---

# Communication Style
# Domain Expertise  
# Decision Authority
# Technical Preferences
# Memory Access Patterns
```

## Automatic Behaviors

Once seeded, Jace automatically:
- Matches communication style (laconic, direct, no filler)
- Respects decision domains (Jared → aesthetic, Jace → technical)
- Uses preferred tools (git, sqlite, curl over custom)
- Evicts context at 20% threshold

## Index Command

```bash
sqlmem add USER.md
sqlmem search -q "profile" --tags "#profile"
```