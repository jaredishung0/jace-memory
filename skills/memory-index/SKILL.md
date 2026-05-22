---
name: memory-index
description: Index markdown files into SQLite for semantic search and automatic tracking
---

# Memory Index Skill

## Purpose
Git-friendly, semantic-searchable memory using SQLite. Automatically indexes all markdown files.

## Install

```bash
# Build sqlmem CLI
cd /home/jared/Desktop/sqlite-md-memory/sqlite-memory/cli
make build

# Init project
./sqlmem init --model /home/jared/.models/nomic-embed-text-v1.5.Q8_0.gguf
```

## Usage

### Initial Indexing
```bash
# Index all memories
./sqlmem add /home/jared/Desktop/memory-system/memories/

# Index specific folder
./sqlmem add /home/jared/Desktop/memory-system/HOMIE.md
```

### Search
```bash
# Semantic search
./sqlmem search -q "landscape architecture" --limit 10

# JSON output for processing
./sqlmem search -q "jared preferences" --json
```

### Watch Mode (Automatic)
```bash
# Auto-reindex on file changes
./sqlmem watch --path /home/jared/Desktop/memory-system/
```

## Database Location
- Default: `./memory.db` in project root
- Per-project: Copy `sqlmem watch` to project startup

## Natural Integration

Add to AGENTS.md startup phase:
```bash
sqlmem watch --path $PWD &
```

## Query from Skills

```bash
# Get recent sessions
sqlmem search -q "session summary" --since "7 days ago"

# Find project context
sqlmem search -q "project landscape" --limit 5
```