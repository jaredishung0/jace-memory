"""
memory-server: file-based memory backend for agentic systems.

Stores memories as markdown files with YAML frontmatter.
Git-commits every write. Exposes OpenAI-compatible endpoint for LiteLLM routing.
"""

from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
import uuid
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ── paths ──────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
MEMORIES = ROOT / "memories"
SUBDIRS = ["people", "projects", "decisions", "concepts", "sessions"]

for d in SUBDIRS:
    (MEMORIES / d).mkdir(parents=True, exist_ok=True)

# ── app ────────────────────────────────────────────────────────────
app = FastAPI(title="Memory Server", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── models ─────────────────────────────────────────────────────────
class MemoryCreate(BaseModel):
    type: str = "sessions"       # subdirectory name
    title: str = ""
    content: str = ""
    tags: list[str] = []
    links: list[str] = []        # wiki-links [[Target]]

class MemorySearch(BaseModel):
    query: str = ""
    types: list[str] = []        # filter by subdirectory
    limit: int = 10
    tags: list[str] = []

class MemoryRecall(BaseModel):
    query: str = ""
    limit: int = 10

class MemoryOut(BaseModel):
    id: str
    type: str
    title: str
    content: str
    tags: list[str]
    links: list[str]
    created: str
    updated: str
    filepath: str

# ── helpers ────────────────────────────────────────────────────────
def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def _slug(text: str) -> str:
    s = text.lower().strip().replace(" ", "-")
    s = re.sub(r"[^a-z0-9\-]", "", s)
    return s[:60] or "untitled"

def _generate_id() -> str:
    return uuid.uuid4().hex[:10]

def _filepath(mtype: str, title: str) -> Path:
    date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    return MEMORIES / mtype / f"{date}_{_slug(title)}.md"

def _to_markdown(id: str, mtype: str, title: str, content: str,
                 tags: list[str], links: list[str], created: str, updated: str) -> str:
    tags_yaml = "\n".join(f"  - {t}" for t in tags) if tags else "  []"
    links_yaml = "\n".join(f"  - [[{l}]]" for l in links) if links else "  []"
    # Escape triple backticks in content for safe embedding
    safe_content = content.replace("```", "`\u200b``")
    return f"""---
id: {id}
type: {mtype}
title: {title}
created: {created}
updated: {updated}
tags:
{tags_yaml}
links:
{links_yaml}
---
# {title}

{safe_content}
"""

def _parse_markdown(text: str, filepath: str) -> MemoryOut | None:
    """Parse YAML frontmatter + markdown body."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not m:
        return None
    front_raw = m.group(1)
    body = m.group(2).strip()

    # Simple YAML key: value parser (no pyyaml dep)
    front: dict = {}
    current_key = None
    current_list = []
    in_list = False
    for line in front_raw.split("\n"):
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            if in_list and current_key:
                front[current_key] = current_list
                current_list = []
                in_list = False
            key, _, val = line.partition(":")
            k = key.strip()
            v = val.strip()
            if v == "" or v == "[]":
                current_key = k
                in_list = True
                current_list = []
            else:
                front[k] = v
                current_key = None
        elif line.strip().startswith("- ") and in_list:
            current_list.append(line.strip()[2:])
    if in_list and current_key:
        front[current_key] = current_list

    title = body.split("\n")[0].lstrip("#").strip() if body else front.get("title", "")

    return MemoryOut(
        id=front.get("id", ""),
        type=front.get("type", ""),
        title=title or front.get("title", ""),
        content=body,
        tags=front.get("tags", []) if isinstance(front.get("tags"), list) else [],
        links=front.get("links", []) if isinstance(front.get("links"), list) else [],
        created=front.get("created", ""),
        updated=front.get("updated", ""),
        filepath=filepath,
    )

def _git_commit(filepath: Path, message: str):
    """Auto-commit a file change. Best-effort — never raise."""
    try:
        subprocess.run(
            ["git", "add", str(filepath.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, timeout=10,
        )
        subprocess.run(
            ["git", "commit", "-m", f"memory: {message[:80]}"],
            cwd=ROOT, capture_output=True, timeout=10,
        )
    except Exception:
        pass  # not in a git repo yet, or git not available

# ── endpoints ──────────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {"status": "ok", "memories": len(list(MEMORIES.rglob("*.md")))}


@app.post("/memories", response_model=MemoryOut)
async def create_memory(m: MemoryCreate):
    if m.type not in SUBDIRS:
        raise HTTPException(400, f"type must be one of: {SUBDIRS}")
    if not m.title:
        raise HTTPException(400, "title is required")

    mem_id = _generate_id()
    now = _now()
    fp = _filepath(m.type, m.title)

    md = _to_markdown(mem_id, m.type, m.title, m.content, m.tags, m.links, now, now)
    fp.write_text(md, encoding="utf-8")

    _git_commit(fp, m.title)

    return MemoryOut(
        id=mem_id, type=m.type, title=m.title,
        content=m.content, tags=m.tags, links=m.links,
        created=now, updated=now, filepath=str(fp.relative_to(ROOT)),
    )


@app.get("/memories/search")
async def search_memories(
    q: str = Query("", description="search query"),
    types: str = Query("", description="comma-separated type filter"),
    tags: str = Query("", description="comma-separated tag filter"),
    limit: int = Query(10, ge=1, le=100),
):
    """Full-text search via ripgrep (rg). Falls back to grep."""
    type_filter = [t.strip() for t in types.split(",") if t.strip()] if types else []
    tag_filter = [t.strip() for t in tags.split(",") if t.strip()] if tags else []

    if not q:
        # No query — list recent
        files = sorted(MEMORIES.rglob("*.md"), reverse=True)[:limit]
    else:
        # Find files matching query
        try:
            result = subprocess.run(
                ["rg", "-l", "-i", q, "--", str(MEMORIES)],
                capture_output=True, text=True, timeout=15,
            )
            matched = [Path(p) for p in result.stdout.strip().split("\n") if p.strip()]
        except (FileNotFoundError, subprocess.TimeoutExpired):
            # Fallback: Python grep
            matched = []
            for fp in MEMORIES.rglob("*.md"):
                try:
                    if q.lower() in fp.read_text(encoding="utf-8").lower():
                        matched.append(fp)
                except Exception:
                    pass
        files = sorted(matched, reverse=True)[:limit]

    results = []
    for fp in files:
        m = _parse_markdown(fp.read_text(encoding="utf-8"), str(fp))
        if not m:
            continue
        if type_filter and m.type not in type_filter:
            continue
        if tag_filter and not any(t in m.tags for t in tag_filter):
            continue
        results.append(m)

    return {"results": results, "count": len(results)}


@app.post("/memories/recall")
async def recall_memories(r: MemoryRecall):
    """Semantic-adjacent recall. For now uses full-text search.
    Future: embed query via LiteLLM, cosine similarity."""
    if not r.query.strip():
        return {"results": [], "count": 0}

    try:
        result = subprocess.run(
            ["rg", "-l", "-i", r.query, "--", str(MEMORIES)],
            capture_output=True, text=True, timeout=15,
        )
        matched = [Path(p) for p in result.stdout.strip().split("\n") if p.strip()]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        matched = []
        for fp in MEMORIES.rglob("*.md"):
            try:
                if r.query.lower() in fp.read_text(encoding="utf-8").lower():
                    matched.append(fp)
            except Exception:
                pass

    files = sorted(matched, reverse=True)[:r.limit]
    results = []
    for fp in files:
        m = _parse_markdown(fp.read_text(encoding="utf-8"), str(fp))
        if m:
            results.append(m)

    return {"results": results, "count": len(results)}


@app.get("/memories")
async def list_memories(
    type: str = Query("", description="filter by type"),
    limit: int = Query(20, ge=1, le=200),
):
    """List recent memories, optionally filtered by type."""
    files = sorted(MEMORIES.rglob("*.md"), reverse=True)
    results = []
    for fp in files:
        if type and type not in str(fp):
            continue
        m = _parse_markdown(fp.read_text(encoding="utf-8"), str(fp))
        if m:
            results.append(m)
            if len(results) >= limit:
                break
    return {"results": results, "count": len(results)}


@app.get("/memories/{mem_id}")
async def get_memory(mem_id: str):
    """Find a memory by ID (scans all *.md)."""
    for fp in MEMORIES.rglob("*.md"):
        m = _parse_markdown(fp.read_text(encoding="utf-8"), str(fp))
        if m and m.id == mem_id:
            return m
    raise HTTPException(404, f"memory '{mem_id}' not found")


# ── OpenAI-compatible endpoint (for LiteLLM routing) ──────────────

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str = "memory-bank"
    messages: list[ChatMessage] = []
    max_tokens: int = 1024
    temperature: float = 0.0

class ChatChoice(BaseModel):
    index: int = 0
    message: ChatMessage
    finish_reason: str = "stop"

class ChatUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

class ChatResponse(BaseModel):
    id: str = "mem-" + uuid.uuid4().hex[:8]
    object: str = "chat.completion"
    created: int = 0
    model: str = "memory-bank"
    choices: list[ChatChoice] = []
    usage: ChatUsage = ChatUsage()

@app.post("/v1/chat/completions")
async def chat_completions(req: ChatRequest):
    """
    OpenAI-compatible endpoint. Extracts the query from the last user message,
    searches memories, returns results as JSON in the response content.

    LiteLLM routes 'memory-bank' model to this endpoint.
    """
    # Extract query from messages
    query_parts = []
    for msg in req.messages:
        if msg.role in ("user", "system") and msg.content:
            query_parts.append(msg.content)

    query = " ".join(query_parts) if query_parts else ""

    if not query.strip():
        results = []
    else:
        try:
            result = subprocess.run(
                ["rg", "-l", "-i", query, "--", str(MEMORIES)],
                capture_output=True, text=True, timeout=15,
            )
            matched = [Path(p) for p in result.stdout.strip().split("\n") if p.strip()]
        except (FileNotFoundError, subprocess.TimeoutExpired):
            matched = []
            for fp in MEMORIES.rglob("*.md"):
                try:
                    if query.lower() in fp.read_text(encoding="utf-8").lower():
                        matched.append(fp)
                except Exception:
                    pass

        results = []
        for fp in sorted(matched, reverse=True)[:10]:
            m = _parse_markdown(fp.read_text(encoding="utf-8"), str(fp))
            if m:
                results.append(m.model_dump())

    now_ts = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
    content = json.dumps({"results": results, "count": len(results)}, indent=2)

    return ChatResponse(
        created=now_ts,
        choices=[ChatChoice(
            message=ChatMessage(role="assistant", content=content)
        )],
    )


# ── main ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
