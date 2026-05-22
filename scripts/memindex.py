#!/usr/bin/env python3
"""Simple SQLite memory indexer for markdown files."""

import sqlite3
import hashlib
import os
import sys
from pathlib import Path

DB_PATH = ".memory.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY,
        path TEXT UNIQUE,
        title TEXT,
        content TEXT,
        tags TEXT,
        hash TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.execute("""CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts 
        USING fts5(title, content, tags, content='memories', content_row=True)""")
    conn.commit()
    return conn

def index_file(path):
    with open(path, 'r') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    title = Path(path).stem
    tags = ""
    
    if content.startswith('---'):
        lines = content.split('\n')
        if '---' in lines[1:]:
            end_idx = lines[1:].index('---') + 1
            yaml_block = '\n'.join(lines[1:end_idx])
            for line in yaml_block.split('\n'):
                if line.startswith('tags:'):
                    tags = line.split(':', 1)[1].strip()
                elif line.startswith('synopsis:'):
                    title = line.split(':', 1)[1].strip()
    
    # Remove frontmatter and extract title
    if content.startswith('---'):
        content = '\n'.join(content.split('\n')[end_idx+2:])
    
    content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
    
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("INSERT OR REPLACE INTO memories (path, title, content, tags, hash) VALUES (?, ?, ?, ?, ?)",
                     (str(path), title, content[:10000], tags, content_hash))
        conn.commit()
        print(f"✓ Indexed: {path}")
    except Exception as e:
        print(f"✗ Error: {path} - {e}")
    finally:
        conn.close()

def search(query, limit=10):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute(f"""SELECT path, title FROM memories WHERE title LIKE '%{query}%' OR content LIKE '%{query}%' LIMIT ?""", 
                       (limit,))
    results = cur.fetchall()
    for row in results:
        print(f"{row[0]}: {row[1]}")
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: memindex.py <index|search> [paths...]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "init":
        init_db()
        print(f"Initialized {DB_PATH}")
    elif cmd == "index":
        init_db()
        for path in sys.argv[2:]:
            if os.path.isdir(path):
                for root, dirs, files in os.walk(path):
                    for f in files:
                        if f.endswith('.md'):
                            index_file(os.path.join(root, f))
            elif os.path.isfile(path):
                index_file(path)
    elif cmd == "search":
        search(' '.join(sys.argv[2:]))