#!/usr/bin/env python3
"""
brain.command - BRAIN Management Suite
═══════════════════════════════════════════════════════════
Unified CLI for managing the BRAIN personal knowledge system.
Double-click in Finder to open the interactive menu, or run
directly from Terminal and pass a command name.

Commands:
  search    🔎  Full-text search, ripgrep-accelerated (pure-Python fallback)
  load      📥  Ranked, token-budgeted file set for a task
  remember  🧠  Write the engine-owned Memory/Log.md: note, --loop, close, route (never hand-edited)
  new       🆕  Scaffold a new project or venture from its .template/
  health    🩺  Run lint + links + stale + index + gitkeep + error-log review in one pass
  selftest  🧪  Regression smoke test of brain.command itself (startup/cascade/lint/links)
  manifest  📋  Rebuild the incremental, content-hashed index (manifest.json)
  backup    💾  Copy a file to System/.backups/ with Section 10.1 naming (pre-edit step)
  tokens    🪙  Estimate token cost by file, folder, and total
  memory    🧠  Memory layer: tiered pipeline (list/status/cascade) + collections (add person/organization/place/decision/event/insight, sync)
  skill     📦  List/validate/package skill sources in Skills/.unpackaged/ (.skill zips at the Skills/ root)
  startup   🚀  Print the full Section 9 session-init bundle in one call (--json for paths/tokens)
  read      📖  Surgical reads: one section, --toc outline with token costs, --fm frontmatter only
  links     🔗  Wikilink graph integrity: check (broken/ambiguous), orphans, stats
  inbox     📨  Inbox status - files awaiting the sorting protocol (exit 1 when pending)
  index     🗂  Verify Projects/, Ventures/, and Memory collections agree with their registries
  summary   🗒  Scaffold a session summary (canonical format) + run the cascade; latest; status
  consolidate 🧹  Read-only ADD/UPDATE/SUPERSEDE/NOOP worksheet for the Memory Consolidation Loop
  changelog 🧾  Append a correctly versioned changelog entry: changelog add patch "description"
  git       🌿  Vault versioning: status / init (iCloud-safe separate-git-dir) / snapshot "msg"
  rename    ✏️  Backlink-safe rename: rewrites every [[wikilink]] pointing at the file
  gitkeep   📌  Empty-folder preservation: add .gitkeep to empty folders, drop it when files arrive
  trash     🗑   Two-level deletion: soft-remove to .trash, restore, or hard-remove from .trash only
  lint      🔍  Validate frontmatter schema across all .md files
  stale     ⏰  Flag outdated memory, stale Library content, and lifetime-hygiene issues
  diff      📊  Show what changed since the index was built (hash-based)
  sync      🔄  Push tags → Finder metadata, incremental (changed tags only)

Usage:
  python3 brain.command                            # interactive menu
  python3 brain.command sync                       # run a command directly
  python3 brain.command sync all                   # force a full re-sync
  python3 brain.command search "query"             # full-text search
  python3 brain.command search "query" folder=library type=reference
  python3 brain.command skill package develop          # zip one skill to Skills/develop.skill
  python3 brain.command skill package all --yes        # package every valid skill
  python3 brain.command startup --json                 # session-init bundle (paths + token costs)
  python3 brain.command read Instructions.md "9. Session Initialization Checklist"
  python3 brain.command changelog add patch "Fixed X in Y" files="System/brain.command"
  python3 brain.command load "task desc"           # token budget: load "task" 30000
  python3 brain.command load "task" --json         # machine-readable file list
  python3 brain.command new project "Site" --yes   # non-interactive scaffold
  python3 brain.command memory add person "Jane Doe"   # scaffold a person profile
  python3 brain.command memory add decision "Switched to LLC"   # scaffold a decision record
  python3 brain.command memory add date recurring "Jan 1 (yearly)" "Annual review"   # engine writes the row
  python3 brain.command remember "What to log"     # append a Log note (newest first)
  python3 brain.command remember "Follow up with X" --loop   # open loop (auto-listed)
  python3 brain.command remember close "follow up" # resolve a matching open loop
  python3 brain.command backup Memory/Log.md       # pre-edit snapshot, auto-named
  python3 brain.command backup list                # review snapshots (Section 10.3)
  python3 brain.command backup clear --yes         # lint-gated cleanup, keeps .gitkeep
  python3 brain.command sync tag "Library/X/book.pdf" library reference timeless
  python3 brain.command manifest full              # from-scratch index rebuild
  python3 brain.command folder profile             # the Profile (self) bundle in one call
  python3 brain.command folder ventures Acme-Corp  # one venture, deep

Agent notes:
  --yes anywhere on the command line auto-confirms prompts (new).
  Prompts never hang in non-interactive shells; unanswered confirms abort safely.
  diff exits 1 when drift is found (branch on $?); lint/stale exit 1 on findings.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import plistlib
import re
import shutil
import sqlite3
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.request
import zlib
from datetime import datetime, timezone
from pathlib import Path

# ══════════════════════════════════════════════════════════
#  Self-locating paths - portable, no hardcoded absolutes
# ══════════════════════════════════════════════════════════

SYSTEM_DIR   = Path(os.path.abspath(__file__)).parent   # System/
BRAIN_DIR    = SYSTEM_DIR.parent                         # BRAIN/  (anywhere on disk)

DATA_DIR          = SYSTEM_DIR / "Data"
LOG_FILE          = DATA_DIR / "errors.log"
REPORTS_FILE      = DATA_DIR / "reports.log"      # activity log: one line per state-changing command
REPORTS_MAX_LINES = 1000                          # reports.log auto-trims to the most recent N entries
MANIFEST_FILE     = DATA_DIR / "manifest.json"    # scale-ready file index (schema v2)
SYNC_STATE_FILE   = DATA_DIR / "sync-state.json"  # last-synced tags per file (incremental sync)
LEDGER_FILE       = DATA_DIR / "session-ledger.json"  # tokens served to the AI this session
FRICTION_FILE     = DATA_DIR / "friction.jsonl"   # operating-friction signal the reflection loop reads
AGENT_CATALOG_FILE = DATA_DIR / "agent-catalog.json"  # derived agent/team roll-up, refreshed in lockstep with the manifest

REQUIRED_FIELDS   = ["title", "description", "status", "tags", "aliases",
                     "keywords", "created", "updated", "type", "folder",
                     "layer", "policy", "author", "path", "id"]
# Canonical field order is two bands (Instructions 8.1): a human-facing band
# (title -> updated) shown in Obsidian, then a system band (type -> id) hidden
# by the .obsidian/snippets/brain-hide-system.css snippet. `version` (core/
# contract files only) sits between `policy` and `author`. Order is for human/
# Obsidian readability; the parser and lint are order-independent.
# `version` is required only on core/contract files (see _is_core_file); it is
# validated conditionally in lint, not listed in the always-required set above.
VALID_STATUS      = {"draft", "active", "deprecated", "archived"}
# Which files carry a per-file `version` (MAJOR.MINOR.PATCH, two-digit
# zero-padded to match changelog.md) is decided by LOCATION, not type, in
# _is_core_file() - see Instructions 8.6. Type alone cannot distinguish a
# governance folder doc from a Library content-area doc (both are
# `information`), so the test mirrors the changelog's core-files definition:
# root governance + System/ + .template/ + Layer-1 folder docs.
ID_RE             = re.compile(r"^[a-z]{2}-[a-z0-9-]+$")
VERSION_RE        = re.compile(r"^\d{2}\.\d{2}\.\d{2}$")
# Two-letter id prefix per folder (stable-slug namespacing + collision guard).
ID_PREFIX         = {"root": "ro", "library": "li", "profile": "id",
                     "memory": "me", "projects": "pr", "ventures": "ve",
                     "system": "sy", "inbox": "in"}
VALID_FILE_TYPES  = {"guide", "constitution", "information", "template",
                     "log", "record", "self", "reference", "script", "agent"}
VALID_FOLDERS     = {"root", "library", "profile", "memory", "ventures",
                     "projects", "system", "inbox"}
# Tag vocabulary per Constitution Article VII (five dimensions: Folder, File
# Role, AI Signal, Sensitivity, Freshness). Folder + File Role tags reuse
# VALID_FOLDERS and VALID_FILE_TYPES above. Retention was retired in 05.00.00 -
# it is now the boolean `policy` frontmatter field, not a tag. The Content and
# Life-Stage dimensions were removed in 04.00.00.
VALID_AI_SIGNAL_TAGS    = {"startup"}
VALID_SENSITIVITY_TAGS  = {"sensitive"}
VALID_FRESHNESS_TAGS    = {"timeless", "enduring", "current"}

# Approximate tokens per character for rough estimation (Gemini/Claude avg)
CHARS_PER_TOKEN   = 4

# Index + retrieval tuning (scale-readiness layer)
# v3: entries carry `importance` (capture-time 1-5 rating parsed from the
# body); load_index rejects other versions so a stale-shape manifest is
# rebuilt clean rather than consumed.
INDEX_SCHEMA_VERSION = 3
LOAD_TOKEN_BUDGET    = 50000     # default token ceiling for `load` (override: load "task" <budget>)
# Lifetime-hygiene thresholds (surfaced by `stale`; advisory, never auto-acted on)
MEMORY_SHARD_WARN_TOKENS = 25000  # permanent Memory file larger than this → suggest sharding
LOG_UNPROMOTED_WARN      = 10    # more Log.md entries than this → suggest consolidation loop
BACKUP_PILE_WARN         = 1000  # advisory ceiling - rotation keeps real counts far below this
# Directories never indexed, searched, linted, or synced (snapshots, app config, trash, vcs, build cache)
SKIP_DIRS            = {"Backups", ".obsidian", ".trash", ".git", "__pycache__"}
# Junk/sidecar files never indexed
SKIP_FILES           = {".DS_Store", ".gitkeep", ".localized", ".metadata_never_index",
                        "LICENSE"}  # root GitHub license file: repo infra, not BRAIN content
# In-progress downloads and temp writes (browser/aria2 partials, the atomic
# writer's own .tmp~ files): never indexed, hashed, or tagged.
TRANSIENT_SUFFIXES   = (".part", ".tmp", ".aria2", ".tmp~")
EXEC_SUFFIXES        = {".command", ".py", ".sh", ".zsh", ".rb"}   # binaries tagged `script` by sync
# Em dash, built from its code point so this file never contains the literal
# character that Constitution Article 9.1 bans vault-wide (lint would flag it).
EM_DASH              = chr(0x2014)

# Script metadata
VERSION           = "v17+ (changelog unreadable - investigate)"  # fallback only; banner reads the live version
AUTHOR            = "Tanner Golden"
WEBSITE           = "https://www.tannergolden.com"
CREATED           = "May 18th, 2026"

# ══════════════════════════════════════════════════════════
#  Logging
# ══════════════════════════════════════════════════════════

try:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    _log_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
except OSError:
    _log_handler = logging.NullHandler()

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s  [brain.command / %(name)s]  %(levelname)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[_log_handler]
)


# ══════════════════════════════════════════════════════════
#  Activity log (reports.log) - the success-side companion to errors.log
# ══════════════════════════════════════════════════════════
#  errors.log records failures; reports.log records the state-changing
#  commands that ran (sync, manifest, cascade, backup, trash, rename, new,
#  changelog, gitkeep, skill package, git init/snapshot). Read-only commands
#  and read-only subcommands (sync verify, backup list, memory status,
#  gitkeep check, git status, ...) never write here. The write is centralized
#  in _finish_ledger and gated by _is_mutating, so it stays in one place.

# Subcommand that flips an otherwise-mutating command into read-only.
_READONLY_CMDS = {
    "search", "load", "read", "lint", "links", "tokens",
    "folder", "startup", "diff", "index", "inbox",
    "consolidate", "selftest", "help", "-h", "--help", "?",
}

def _is_mutating(cmd: str, argv: list) -> tuple:
    """Return (writes_state, label) for a CLI invocation. label is the full
    command line, logged verbatim (trimmed). Subcommand-aware so read-only
    subcommands of a mutating command stay silent."""
    if not cmd or cmd in _READONLY_CMDS:
        return (False, "")
    sub = argv[1].lower() if len(argv) > 1 else ""
    label = " ".join(argv)
    rules = {
        "sync":      sub != "verify",                 # verify is a read-back check
        "memory":    sub in ("cascade", "add", "sync", "rm", "supersede"),  # list/status read-only
        # "coverage" is deliberately absent from the profile set: it is a
        # read-only report (writes nothing, ever) and is never logged here.
        "profile":   sub in ("add", "rm", "sync"),     # entry-bearing Profile facets
        "backup":    sub != "list",                   # bare backup + clear mutate
        "trash":     sub not in ("", "list"),          # bare trash = list view; path/restore/empty mutate
        "skill":     sub == "package",                # list is read-only
        "agents":    sub == "catalog",                # catalog writes the derived catalog file
        "health":    True,                            # refreshes index, writes catalog, gitkeep fixes
        "git":       sub in ("init", "snapshot"),     # status is read-only
        "summary":   sub == "new",                    # latest/bare are read-only
        "changelog": sub == "add",                    # bare prints the version
        "bump":      True,                            # always writes version + updated
        "gitkeep":   sub != "check",                  # check is a dry run
        "logs":      sub == "clear",                   # bare logs/status is read-only
        "manifest":  True,
        "db":        sub in ("build", "rebuild", "rollup", "all", "refresh"),  # search/status read-only
        "kb":        sub in ("refresh", "setup", "add", "remove", "rm", "relink"),  # search/list read-only
        "new":       True,
        "remember":  True,                            # always writes Memory/Log.md
        "friction":  sub != "list",                   # list is a read-only review
        "rename":    True,
    }
    return (rules.get(cmd, False), label)

def _report(label: str, rc: int) -> None:
    """Append one line to reports.log for a state-changing command, then trim to
    the most recent REPORTS_MAX_LINES. Never raises - a logging failure must not
    crash the command that succeeded."""
    try:
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "OK" if rc == 0 else f"EXIT {rc}"
        line = f"{stamp}  [brain.command]  {status}  {label[:200]}\n"
        REPORTS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(REPORTS_FILE, "a", encoding="utf-8") as fh:
            fh.write(line)
        # Trim to the most recent REPORTS_MAX_LINES (cheap; the file is small).
        with open(REPORTS_FILE, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        if len(lines) > REPORTS_MAX_LINES:
            with open(REPORTS_FILE, "w", encoding="utf-8") as fh:
                fh.writelines(lines[-REPORTS_MAX_LINES:])
    except Exception:
        try:
            logging.getLogger("reports").error("reports.log write failed", exc_info=True)
        except Exception:
            pass

# Captured by main() before dispatch so the centralized _finish_ledger hook can
# log the invocation without every command knowing its own name.
_INVOKED = ("", [])


# ══════════════════════════════════════════════════════════
#  Shared helpers
# ══════════════════════════════════════════════════════════

def run(args: list, timeout: int = 15) -> subprocess.CompletedProcess:
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout)

# Set by main() when --yes appears anywhere on the command line. Lets agents and
# scripts run confirming commands (new) without stdin interaction.
AUTO_CONFIRM = False

def confirm(prompt: str = "Proceed? (yes/no): ") -> bool:
    if AUTO_CONFIRM:
        print(f"\n{prompt}yes  (--yes)")
        return True
    try:
        return input(f"\n{prompt}").strip().lower() in ("yes", "y")
    except EOFError:
        return False

def divider(char: str = "-", width: int = 58) -> str:
    # ASCII separators: box-drawing chars cost 3-10x more tokens in common tokenizers.
    return char * width

def header(title: str, emoji: str = "") -> None:
    print()
    print(divider("="))
    print(f"  {emoji}  {title}" if emoji else f"  {title}")
    print(divider("="))
    print()

def step(n: int, total: int, label: str) -> None:
    print(f"\n  [{n}/{total}] {label}")

def ok(msg: str)   -> None: print(f"    ✅  {msg}")
def warn(msg: str) -> None: print(f"    ⚠️   {msg}")
def fail(msg: str) -> None: print(f"    ❌  {msg}")

def iter_md_files():
    """Yield all .md file Paths in the BRAIN, skipping hidden dirs and
    System/.backups/."""
    try:
        for root, dirs, files in os.walk(BRAIN_DIR):
            # Skip hidden dirs and Backups (snapshots). .template is hidden from
            # Obsidian but engine-managed (lint, sync, scaffolding) - the one
            # hidden dir we walk.
            dirs[:] = sorted(d for d in dirs if (not d.startswith(".") or d == ".template")
                             and d != "Backups")
            for f in sorted(files):
                if f.endswith(".md"):
                    yield Path(root) / f
    except PermissionError as e:
        logging.getLogger("iter").error("Permission denied walking BRAIN: %s", e)

def rel(path: Path) -> str:
    """Return path relative to BRAIN_DIR. Falls back to absolute path on error."""
    try:
        return str(path.relative_to(BRAIN_DIR))
    except ValueError:
        return str(path)

def parse_frontmatter(path: Path) -> dict | None:
    """Parse YAML frontmatter from a .md file. Returns dict or None."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    return _parse_frontmatter_text(content)

def _parse_frontmatter_text(content: str) -> dict | None:
    """Parse YAML frontmatter from already-read file text (the single-read
    path: lint reads each file once and reuses the text). Returns dict or None."""
    if not content.startswith("---"):
        return None
    mend = re.search(r"\n---[ \t]*\r?\n", content[3:])
    if mend is None:
        return None
    block = content[3:3 + mend.start() + 1]
    fm = {}
    for line in block.splitlines():
        m = re.match(r'^(\w[\w_-]*):\s*(.*)', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            val = val.strip('"\'')
            fm[key] = val
    # List-valued fields (tags, aliases, keywords). Two YAML shapes are supported
    # per field: inline flow array  key: ["a", "b"]  and block list
    #   key:
    #     - a
    # The col-0 line loop above leaves an inline array as a raw string and a
    # block list as an empty string, so normalise each into a real list here. An
    # explicit empty array (key: []) normalises to [] so "present but empty" is
    # preserved (aliases/keywords are required-present but may be empty).
    for lf in ("tags", "aliases", "keywords"):
        inline = re.search(rf'^{lf}:\s*\[(.*?)\]', block, re.MULTILINE)
        if inline is not None:
            fm[lf] = [t.strip().strip("\"'") for t in inline.group(1).split(",") if t.strip()]
            continue
        if re.search(rf'^{lf}:\s*$', block, re.MULTILINE):
            # Block-style list: collect the consecutive "  - item" lines.
            items, in_field = [], False
            for line in block.splitlines():
                if re.match(rf'^{lf}:\s*$', line):
                    in_field = True
                    continue
                if in_field:
                    item = re.match(r'^\s*-\s+(.*)', line)
                    if item:
                        items.append(item.group(1).strip().strip("\"'"))
                    elif line.strip() == "":
                        continue
                    else:
                        break  # next key reached; stop collecting
            fm[lf] = items
    return fm

def count_tokens(path: Path) -> int:
    """Rough token estimate for a file."""
    try:
        return max(1, len(_read_text(path)) // CHARS_PER_TOKEN)
    except OSError:
        return 0

def _ordinal(n: int) -> str:
    """Return integer with ordinal suffix: 1st, 2nd, 3rd, 4th…"""
    if 11 <= (n % 100) <= 13:
        return f"{n}th"
    last = n % 10
    if last == 1: return f"{n}st"
    if last == 2: return f"{n}nd"
    if last == 3: return f"{n}rd"
    return f"{n}th"

def _fmt_date(dt: datetime) -> str:
    """Format datetime as 'May 18th, 2026'."""
    return dt.strftime(f"%B {_ordinal(dt.day)}, %Y")


# ══════════════════════════════════════════════════════════
#  Session context ledger - the AI cannot read its own context meter, so the
#  engine keeps one for everything it serves (the MemGPT/harness pattern: the
#  tool measures, the model receives the number as text). `startup` resets it;
#  a 4-hour gap also resets it. Thresholds are deliberately early - engine-served
#  tokens are a LOWER bound on real context use, and research says summarize
#  well before pressure, never at the 95% auto-point.
# ══════════════════════════════════════════════════════════

# Context windows per model family (researched 2026-06; consumer-session sizes).
# Engine-served tokens are a LOWER bound on real usage, so thresholds fire as
# percentages of the window well before genuine pressure: 20% note, 30%
# recommend, 45% urgent. Default is Claude's 200k - the smallest, safest floor.
CONTEXT_WINDOWS = {
    "claude":    200_000,   # Claude standard (all current models)
    "claude-1m": 1_000_000, # Claude 1M beta (usage tier 4 / API)
    "gemini":    1_000_000, # Gemini Pro line
    "gemini-2m": 2_000_000, # Gemini Pro 2M tier
    "gpt":       1_000_000, # GPT-5.x line
}
DEFAULT_WINDOW = ("claude", 200_000)
LEDGER_PCT = (0.20, 0.30, 0.45)  # note, recommend, urgent
LEDGER_RESET_AFTER = 4 * 3600  # seconds of inactivity = new session

def _ledger_reset(initial: int = 0, model: str = "") -> None:
    """Start a fresh session ledger. `model` picks the context window:
    a CONTEXT_WINDOWS key, or a raw token count. Defaults to Claude 200k."""
    label, window = DEFAULT_WINDOW
    m = model.strip().lower()
    if m in CONTEXT_WINDOWS:
        label, window = m, CONTEXT_WINDOWS[m]
    elif m.isdigit() and int(m) >= 50_000:
        label, window = f"{int(m)//1000}k custom", int(m)
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        LEDGER_FILE.write_text(json.dumps(
            {"started": datetime.now(timezone.utc).isoformat(),
             "updated": time.time(), "tokens": initial,
             "window": window, "model": label}))
    except OSError as e:
        logging.getLogger("ledger").error("reset failed: %s", e)

def _ledger_add(n: int) -> dict:
    """Add n served tokens; returns the ledger dict (the caller reads it for the footer). Stale ledgers reset."""
    data = _read_json(LEDGER_FILE)
    if not data or time.time() - data.get("updated", 0) > LEDGER_RESET_AFTER:
        data = {"started": datetime.now(timezone.utc).isoformat(), "tokens": 0,
                "window": DEFAULT_WINDOW[1], "model": DEFAULT_WINDOW[0]}
    data["tokens"] = int(data.get("tokens", 0)) + n
    data["updated"] = time.time()
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        LEDGER_FILE.write_text(json.dumps(data))
    except OSError as e:
        logging.getLogger("ledger").error("write failed: %s", e)
    return data

def _ledger_footer(data: dict) -> str:
    """One status line after every CLI command - the AI's context fuel gauge,
    scaled to the session's declared model window (startup <model> sets it)."""
    total = data.get("tokens", 0)
    window = data.get("window", DEFAULT_WINDOW[1]) or DEFAULT_WINDOW[1]
    model = data.get("model", DEFAULT_WINDOW[0])
    pct = total / window
    gauge = f"~{total:,} served · ~{pct:.0%} of {model} {window//1000}k window (lower bound)"
    if pct >= LEDGER_PCT[2]:
        return (f"[CONTEXT {gauge} - WRITE THE SESSION SUMMARY NOW (summary new), run memory "
                f"cascade, and show the user the handoff notice (Memory/Memory.md).]")
    if pct >= LEDGER_PCT[1]:
        return f"[CONTEXT {gauge} - update the running session summary at the next task boundary (Section 14).]"
    if pct >= LEDGER_PCT[0]:
        return f"[CONTEXT {gauge} - checkpoint at task boundaries (Section 14).]"
    return f"[ctx {gauge}]"


class _CountingWriter:
    """stdout proxy that counts characters, so the ledger reflects exactly what
    the engine put into the AI's context."""
    def __init__(self, stream):
        self.stream, self.chars = stream, 0
    def write(self, text):
        self.chars += len(text)
        try:
            return self.stream.write(text)
        except BrokenPipeError:
            # A downstream reader (head, a closed pager, an agent pipe) went away
            # mid-stream. That is not an engine fault; swallow it so it never lands
            # in errors.log as noise. Report the chars as written and move on.
            return len(text)
    def flush(self):
        try:
            return self.stream.flush()
        except BrokenPipeError:
            return None
    def isatty(self):
        return self.stream.isatty()


# ══════════════════════════════════════════════════════════
#  Index core - incremental, content-hashed file index
# ══════════════════════════════════════════════════════════
#
# manifest.json is the BRAIN's scale-ready index. It is a plain JSON file so any
# AI or pipeline can read it directly - no database, no driver, no SQL - the same
# portability premise as the rest of the BRAIN. Every read-heavy command consults
# the index instead of re-walking and re-parsing the whole vault.
#
# Change detection is two-tier. (mtime, size) is the cheap "maybe changed" signal
# that lets the build skip re-reading unchanged files. The SHA-256 content hash is
# the authoritative "actually changed" identity, and it is portable: it survives an
# iCloud sync or a git clone, where mtimes reset, so `diff` never reports false
# changes after the vault moves machines.

def _is_skipped_dir(name: str) -> bool:
    """Dirs we never descend into: hidden, snapshots, app config, trash, vcs.
    Exception: .template/ is hidden only from Obsidian - the engine manages it."""
    if name == ".template":
        return False
    return name.startswith(".") or name in SKIP_DIRS

def iter_all_files(markdown_only: bool = False):
    """Yield file Paths in the BRAIN, skipping snapshot/config/trash dirs and junk files.
    markdown_only=True restricts to .md (the scope the linter and tag-sync use)."""
    try:
        for root, dirs, files in os.walk(BRAIN_DIR):
            # Prune skipped dirs and the generated-artifacts dir (manifest,
            # logs, sync-state) so the index never indexes itself or churns on
            # its own output.
            dirs[:] = sorted(d for d in dirs
                             if not _is_skipped_dir(d))
            for f in sorted(files):
                if f in SKIP_FILES or f.startswith("."):
                    continue
                if f.endswith(TRANSIENT_SUFFIXES):
                    continue  # in-progress download / temp write: never indexed
                if Path(root) == DATA_DIR and not f.endswith(".md"):
                    continue  # generated artifacts: never indexed (the index
                              # would churn on its own output); Data.md is real
                if markdown_only and not f.endswith(".md"):
                    continue
                yield Path(root) / f
    except PermissionError as e:
        logging.getLogger("index").error("Permission denied walking BRAIN: %s", e)

def _sha256(path: Path) -> str:
    """SHA-256 of file contents, streamed so large binaries never load fully into memory."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
    except OSError as e:
        logging.getLogger("index").error("hash failed for %s: %s", path, e)
        return ""
    return h.hexdigest()

def _layer_num(value) -> int:
    """Frontmatter `layer` as an int for sorting (lexicographic '10' < '2' bug guard).
    Unknown/missing layers sort last."""
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return 99

def _top_folder(path: Path) -> str:
    """Layer-1 folder tag for a file ('root' for files at the BRAIN root).
    The identity layer's folder is named Profile/ (human-facing) and carries the
    Folder tag 'profile' (Constitution Article VII)."""
    parts = Path(rel(path)).parts
    if len(parts) <= 1:
        return "root"
    top = parts[0].lower()
    return top

def _brain_version() -> str:
    """Read the BRAIN system version from the changelog Current Version line."""
    try:
        txt = (BRAIN_DIR / "System" / "changelog.md").read_text(encoding="utf-8")
        m = re.search(r'\*\*`(\d{2}\.\d{2}\.\d{2})`\*\*', txt)
        return m.group(1) if m else ""
    except OSError:
        return ""

def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

def _read_xattr_tags(path: Path) -> list:
    """Best-effort read of macOS Finder tags from a binary file. [] off macOS or on any error."""
    if sys.platform != "darwin":
        return []
    try:
        result = subprocess.run(
            ["xattr", "-px", "com.apple.metadata:_kMDItemUserTags", str(path)],
            capture_output=True, text=True, timeout=5)
        if result.returncode != 0 or not result.stdout.strip():
            return []
        raw = bytes.fromhex(result.stdout.replace("\n", "").replace(" ", ""))
        tags = plistlib.loads(raw)
        return [str(t).split("\n")[0] for t in tags] if isinstance(tags, list) else []
    except Exception:
        return []

def _read_text(path: Path) -> str:
    """Tolerant vault read: UTF-8 with replacement characters, so one
    malformed file degrades locally instead of crashing lint, health,
    manifest, or search (a bare strict read once could)."""
    return path.read_text(encoding="utf-8", errors="replace")


def _fm_bounds(text: str):
    """(start, end) bounds of the frontmatter block interior, or None.
    The closing delimiter must sit at a line start, so a '---' inside a
    field value can never truncate the block."""
    if not text.startswith("---"):
        return None
    m = re.search(r"\n---[ \t]*\r?\n", text[3:])
    if not m:
        return None
    return (3, 3 + m.start() + 1)


def _sub_frontmatter(text: str, pattern: str, repl: str, count: int = 1):
    """re.sub applied ONLY inside the frontmatter block. Every engine write
    to a metadata key goes through here so a look-alike line in the body
    (a YAML example in a code block) can never be corrupted: the exact
    incident class that hit the embedded summary template on 2026-07-01.
    Returns (new_text, replacements_made)."""
    b = _fm_bounds(text)
    if not b:
        return text, 0
    s, e = b
    new, n = re.subn(pattern, repl, text[s:e], count=count, flags=re.M)
    return text[:s] + new + text[e:], n


def _safe_dest(dest: Path) -> Path:
    """Collision-proof move destination: suffix -1, -2, ... until free, so
    no engine move can silently replace an existing file (Constitution 3.1
    made mechanical for cascade, archive, trash, and backups alike)."""
    if not dest.exists():
        return dest
    i = 1
    while True:
        cand = dest.with_name(f"{dest.stem}-{i}{dest.suffix}")
        if not cand.exists():
            return cand
        i += 1


def _write_atomic(path: Path, text: str) -> None:
    """Write via a hidden temp file + os.replace, so a crash mid-write can
    never leave a truncated vault file or index artifact."""
    tmp = path.with_name("." + path.name + ".tmp~")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _sync_marker_block(doc: Path, start: str, end: str, body: str, label: str) -> bool:
    """Replace the interior of one engine-owned marker pair in `doc` with
    `body`, writing atomically. The single write path for every auto-block
    (tier summaries, collection/profile entries, open loops, kb files), so
    marker handling can never drift between writers. Never a silent no-op:
    warns when the doc is unreadable or the marker pair is missing. Returns
    True when the file changed."""
    try:
        text = _read_text(doc)
    except OSError as e:
        warn(f"{rel(doc)}: cannot read for the {label} block ({e}) - not synced.")
        return False
    pat = re.escape(start) + r".*?" + re.escape(end)
    if not re.search(pat, text, flags=re.DOTALL):
        # A doc without its marker pair silently strands its auto-list out of
        # sync (found live 2026-07-02) - say so instead of no-op.
        warn(f"{rel(doc)} lacks the {label} marker pair - add the markers so "
             f"the auto-block can sync.")
        return False
    new = re.sub(pat, f"{start}\n{body}\n{end}", text, count=1, flags=re.DOTALL)
    if new == text:
        return False
    try:
        _write_atomic(doc, new)
        return True
    except OSError as e:
        warn(f"{rel(doc)}: write failed for the {label} block: {e}")
        return False


def load_index() -> dict:
    """Return the saved manifest.json index, or {} if absent/unreadable.
    An index whose schema_version differs from INDEX_SCHEMA_VERSION is
    treated as absent too, forcing a clean rebuild instead of consuming an
    old-shape manifest (entries could lack fields the current code expects)."""
    idx = _read_json(MANIFEST_FILE)
    if idx and idx.get("schema_version") != INDEX_SCHEMA_VERSION:
        return {}
    return idx

def _index_by_path(index: dict) -> dict:
    return {e.get("path", ""): e for e in index.get("files", [])}

def _aslist(v):
    """Coerce a frontmatter value to a list. Guards the rare case where a list
    field was hand-edited to a scalar or empty string."""
    if isinstance(v, list):
        return v
    if v in (None, "", "[]"):
        return []
    return [v]


def _slugify(text: str) -> str:
    """Lowercase, hyphen-separated, [a-z0-9-] only - the id/slug convention."""
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    return re.sub(r"-{2,}", "-", s) or "file"


def _all_ids() -> set:
    """Every `id` currently declared across BRAIN-schema markdown files."""
    ids = set()
    for p in iter_md_files():
        fm = parse_frontmatter(p)
        if fm and fm.get("id"):
            ids.add(fm["id"])
    return ids


def _gen_id(path: Path, taken: set) -> str:
    """Generate a stable, prefixed, unique slug id for a file. Appends a numeric
    suffix only on collision. Generated once at creation; never regenerated."""
    prefix = ID_PREFIX.get(_top_folder(path), "xx")
    cand = f"{prefix}-{_slugify(path.stem)}"
    if cand not in taken:
        return cand
    i = 2
    while f"{cand}-{i}" in taken:
        i += 1
    return f"{cand}-{i}"


# A file's lifecycle `status` (Instructions 8.1) doubles as the vault-wide
# staleness signal: deprecated or archived means "no longer the live version", so
# retrieval demotes it - `search` sorts it last and flags it, `load` and the
# session-start auto-load skip it. Nothing is deleted: a stale file stays in the
# vault and stays searchable, just out of the way. There is deliberately no
# separate `superseded` field; `status` already carries this meaning on every file.
STALE_STATUSES = {"deprecated", "archived"}


def _is_stale_status(status) -> bool:
    """True when a `status` value marks a file stale (deprecated/archived), the
    signal retrieval uses to demote it. Empty, active, and draft are all live."""
    return str(status or "").strip().lower() in STALE_STATUSES


def _path_stale(path: Path) -> bool:
    """Staleness check for a file by path (parses its frontmatter). Used where no
    index entry is at hand, e.g. the startup auto-load."""
    return _is_stale_status((parse_frontmatter(path) or {}).get("status"))


# The capture-time importance rating (Memory/Memory.md): an `Importance: N`
# line (1 routine to 5 pivotal) in a record's body. Tolerates the bold forms
# `**Importance:** N` and `**Importance**: N`. Parsed at index time and fed
# into retrieval ranking (_score_entry).
IMPORTANCE_RE = re.compile(r"(?im)^\s*(?:\*\*)?importance(?::\*\*|\*\*:|:)\s*([1-5])\b")


def build_index(incremental: bool = True, progress: bool = False) -> dict:
    """Build (or incrementally refresh) the file index and return it.
    Files whose (mtime, size) match the prior index are reused without being
    re-read or re-hashed, so this stays fast on a large vault. Indexes binaries
    too (path/size/hash/tags) so the index is a complete discovery surface."""
    prev = _index_by_path(load_index()) if incremental else {}
    entries, reused = [], 0
    md_count = bin_count = 0
    for path in iter_all_files():
        r = "BRAIN/" + rel(path)
        try:
            st = path.stat()
        except OSError as e:
            logging.getLogger("index").error("stat failed for %s: %s", r, e)
            continue
        cached = prev.get(r)
        if (cached and cached.get("mtime") == st.st_mtime
                and cached.get("size") == st.st_size and cached.get("sha256")):
            if (cached.get("kind") != "binary" and cached.get("version")
                    and not cached.get("version_sha")):
                # Migration seeding: an unchanged, versioned file gets its
                # version_sha baseline (= its last-indexed content) so the
                # health drift check has a durable anchor from the first
                # rebuild after this field was introduced.
                cached = dict(cached)
                cached["version_sha"] = cached.get("sha256")
            entries.append(cached); reused += 1
            if cached.get("kind") == "binary": bin_count += 1
            else: md_count += 1
            if progress: print(f"  ·  {rel(path)}  (unchanged)")
            continue
        sha = _sha256(path)
        if path.suffix == ".md":
            fm = parse_frontmatter(path) or {}
            entry = {
                "path": r,   # real location - the index key. (Frontmatter `path`
                             # may differ for templates/memory summaries; see declared_path.)
                "kind": "markdown",
                "id": fm.get("id", ""),
                "title": fm.get("title", path.stem),
                "description": fm.get("description", ""),
                "aliases": _aslist(fm.get("aliases", [])),
                "keywords": _aslist(fm.get("keywords", [])),
                "author": fm.get("author", ""),
                "layer": fm.get("layer", ""),
                "folder": fm.get("folder", ""),
                "type": fm.get("type", ""),
                "tags": _aslist(fm.get("tags", [])),
                "status": fm.get("status", ""),
                "policy": fm.get("policy", ""),
                "version": fm.get("version", ""),
                "created": fm.get("created", ""),
                "updated": fm.get("updated", ""),
                "tokens": count_tokens(path),
                "size": st.st_size,
                "mtime": st.st_mtime,
                "sha256": sha,
            }
            # version_sha: the content hash from when `version` last moved -
            # the durable baseline for the health version-drift check. It is
            # inherited while the version stays put and reset when the version
            # changes, so an owed bump keeps flagging across index refreshes.
            cur_v = str(fm.get("version", "") or "")
            if cur_v:
                prev_e = cached or {}
                if str(prev_e.get("version", "") or "") == cur_v:
                    entry["version_sha"] = (prev_e.get("version_sha")
                                            or prev_e.get("sha256") or sha)
                else:
                    entry["version_sha"] = sha
            declared = fm.get("path", "")
            if declared and declared != r:
                # Legitimately differs for templates ([Company] placeholders) and
                # memory summaries (recorded origin tier). Kept for reference.
                entry["declared_path"] = declared
            # Importance (Memory/Memory.md retrieval model): the first
            # `Importance: N` line in the BODY (frontmatter excluded), stored
            # so _score_entry can weight pivotal records above routine ones.
            try:
                ftext = _read_text(path)
            except OSError:
                ftext = ""
            fb = _fm_bounds(ftext)
            im = IMPORTANCE_RE.search(ftext[fb[1]:] if fb else ftext)
            if im:
                entry["importance"] = int(im.group(1))
            entries.append(entry)
            md_count += 1
        else:
            entries.append({
                "path": r,
                "kind": "binary",
                "title": path.stem,
                "type": "binary",
                "folder": _top_folder(path),
                "tags": _read_xattr_tags(path),
                "tokens": 0,
                "size": st.st_size,
                "mtime": st.st_mtime,
                "sha256": sha,
            })
            bin_count += 1
        if progress: print(f"  ✅  {rel(path)}")
    entries.sort(key=lambda e: e.get("path", ""))
    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        "generated": datetime.now(timezone.utc).isoformat(),
        "brain_root_name": BRAIN_DIR.name,
        "brain_version": _brain_version(),
        "file_count": md_count,
        "binary_count": bin_count,
        "total_tokens": sum(e.get("tokens", 0) for e in entries),
        "_reused": reused,
        "files": entries,
    }

def save_index(index: dict) -> bool:
    """Persist the index to manifest.json (drops the transient _reused counter)."""
    out = {k: v for k, v in index.items() if k != "_reused"}
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        _write_atomic(MANIFEST_FILE, json.dumps(out, indent=2))
        _write_catalog(index)   # keep the committed content roll-up in lockstep with the manifest
        _write_agent_catalog()  # keep the derived agent/team catalog in lockstep too
        return True
    except OSError as e:
        logging.getLogger("index").error("Could not write manifest: %s", e)
        return False

def index_drift() -> tuple:
    """Compare the live tree to the saved index. Cheap (mtime,size) pre-check, then
    hash-confirm so a clone's reset mtimes don't show as changes.
    Returns (added, modified, deleted) lists of 'BRAIN/...' relative paths."""
    prev = _index_by_path(load_index())
    seen, added, modified = set(), [], []
    for path in iter_all_files():
        r = "BRAIN/" + rel(path)
        seen.add(r)
        try:
            st = path.stat()
        except OSError as e:
            logging.getLogger("index").error("stat failed for %s: %s", r, e)
            continue
        cached = prev.get(r)
        if not cached:
            added.append(r); continue
        if cached.get("mtime") == st.st_mtime and cached.get("size") == st.st_size:
            continue
        if _sha256(path) != cached.get("sha256"):
            modified.append(r)
    deleted = [p for p in prev if p not in seen]
    return sorted(added), sorted(modified), sorted(deleted)


# ══════════════════════════════════════════════════════════
#  1 - Sync Tags
# ══════════════════════════════════════════════════════════

def _set_macos_tags(filepath: Path, tags: list[str]) -> bool:
    log = logging.getLogger("sync")
    attr = "com.apple.metadata:_kMDItemUserTags"
    try:
        plist_bytes = plistlib.dumps([f"{t}\n0" for t in tags], fmt=plistlib.FMT_BINARY)
    except Exception as e:
        fail(f"Failed to serialise plist for {filepath}: {e}"); log.error(e, exc_info=True)
        return False
    try:
        if sys.platform == "darwin":
            hex_val = " ".join(f"{b:02x}" for b in plist_bytes)
            result = subprocess.run(
                ["xattr", "-wx", attr, hex_val, str(filepath)],
                capture_output=True, text=True
            )
            if result.returncode != 0:
                raise RuntimeError(result.stderr.strip())
        else:
            os.setxattr(str(filepath), attr, plist_bytes)
        return True
    except Exception as e:
        fail(f"setxattr failed on {filepath}: {e}"); log.error(e)
        return False

def _load_sync_state() -> dict:
    """Map of relative path → tags last pushed to Finder metadata."""
    return _read_json(SYNC_STATE_FILE)

def _save_sync_state(state: dict) -> None:
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        SYNC_STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")
    except OSError as e:
        logging.getLogger("sync").error("Could not write sync-state: %s", e)


def _state_manual(entry) -> bool:
    """True when a sync-state entry was written by `sync tag` (dict form
    {"tags": [...], "manual": true}). Manual tags are the Inbox protocol's
    deliberate tagging (Instructions 7.5): the routine binary pass carries them
    forward untouched and `sync verify` treats the on-disk tags as authoritative,
    so a routine sync can never clobber them with location-inferred tags."""
    return isinstance(entry, dict) and bool(entry.get("manual"))

def _sync_verify() -> int:
    """Read-back drift check (Article 7.8): compare each file's expected tags
    against what Finder metadata actually carries. A file whose frontmatter and
    xattrs disagree is in a broken state - sync writes, this detects."""
    header("Sync Verify", "🔄")
    if sys.platform != "darwin":
        warn("Finder metadata exists only on macOS - nothing to verify here.")
        return 0
    drift = checked = 0
    state = _load_sync_state()
    for path in iter_all_files():
        if path.suffix == ".md":
            fm = parse_frontmatter(path)
            expected = fm.get("tags", []) if fm else []
            if not expected:
                continue
        else:
            if _state_manual(state.get(rel(path))):
                # Manually tagged via `sync tag`: the on-disk tags are
                # authoritative for this file - inferred tags don't apply.
                continue
            expected = [_top_folder(path)]
            if path.suffix.lower() in EXEC_SUFFIXES:
                expected.append("script")
            elif _top_folder(path) == "library":
                expected.append("reference")
        checked += 1
        actual = _read_xattr_tags(path)
        if sorted(actual) != sorted(expected):
            fail(f"{rel(path)}: frontmatter {expected} vs Finder {actual or '(none)'}")
            drift += 1
    print()
    print(divider())
    if drift:
        print(f"  🏁  {drift}/{checked} file(s) drifted - run `sync` (or `sync all`) to repair (Article 7.8).")
    else:
        print(f"  🏁  {checked} file(s) verified - frontmatter and Finder agree.")
    print(divider())
    return 1 if drift else 0


def _sync_tag(target: str, tags: list) -> int:
    """Manually tag one binary/non-md file (Inbox protocol, Instructions 7.5 / Article 3.5).
    Tags must come from the closed vocabulary; md files are refused - their tags
    live in frontmatter and flow through `sync`."""
    header("Tag File", "🏷️")
    if not target or not tags:
        warn("Usage: sync tag <file> <tag> [tag ...]"); return 1
    p = Path(target)
    if not p.is_absolute():
        p = BRAIN_DIR / target
    try:
        p = p.resolve(); p.relative_to(BRAIN_DIR.resolve())
    except (OSError, ValueError) as e:
        logging.getLogger("sync").error("tag path resolution failed for %s: %s", target, e)
        fail(f"Not a file inside this BRAIN: {target}"); return 1
    if not p.is_file():
        fail(f"File not found: {rel(p)}"); return 1
    if p.suffix == ".md":
        fail("Markdown files take tags in frontmatter - edit `tags:` and run `sync`."); return 1
    vocab = (VALID_FOLDERS | VALID_FILE_TYPES | VALID_AI_SIGNAL_TAGS
             | VALID_SENSITIVITY_TAGS | VALID_FRESHNESS_TAGS)
    bad = [t for t in tags if t not in vocab]
    if bad:
        fail(f"Non-vocabulary tag(s): {bad} (Article VII is a closed vocabulary)"); return 1
    if _set_macos_tags(p, tags):
        # Record the manual marker so routine sync passes never overwrite
        # these tags with location-inferred ones.
        state = _load_sync_state()
        state[rel(p)] = {"tags": tags, "manual": True}
        _save_sync_state(state)
        ok(f"{rel(p)}  🏷️  {tags}  (manual - preserved across syncs)")
        return 0
    fail(f"Tag write failed - see {LOG_FILE}")
    return 1


def cmd_sync(force: bool = False, verify: bool = False, tag_target: str = "", tag_values: list = None) -> int:
    """🔄 Push frontmatter tags to macOS Finder metadata. Incremental: only files whose
    tag set changed since the last sync are re-tagged (tracked in sync-state.json), so a
    large vault syncs in a fraction of the time instead of spawning one xattr call per
    file every run. Pass `all` to force a full re-sync."""
    if verify:
        return _sync_verify()
    if tag_target:
        return _sync_tag(tag_target, tag_values or [])
    header("Sync Tags", "🔄")
    if sys.platform != "darwin":
        # Mirror _sync_verify's guard: without Finder metadata every xattr
        # write would print one failure per file. Warn once and step aside.
        warn("Finder metadata exists only on macOS - nothing to sync here.")
        return 0
    print(f"  BRAIN root: {BRAIN_DIR}")
    print(f"  Mode: {'full re-sync' if force else 'incremental (changed tags only)'}")
    print()
    saved = _load_sync_state()
    prev = {} if force else saved
    new_state = {}
    tagged = same = none = failed = 0
    for path in iter_md_files():
        r = rel(path)
        fm = parse_frontmatter(path)
        tags = fm.get("tags", []) if fm else []
        if not tags:
            none += 1
            continue
        if (not force) and prev.get(r) == tags:
            new_state[r] = tags
            same += 1
            continue
        if _set_macos_tags(path, tags):
            if sys.stdout.isatty():
                print(f"  ✅  {r}")
                print(f"       🏷️  {tags}")
            new_state[r] = tags
            tagged += 1
        else:
            # Keep the prior recorded tags (if any) so this file retries next run.
            if r in prev:
                new_state[r] = prev[r]
            failed += 1
    # Binary files cannot carry frontmatter, but Article 3.5 requires Finder tags
    # on every file. Infer tags from location: the Layer-1 folder tag, plus
    # `script` for executables and `reference` for binaries filed in Library/.
    for path in iter_all_files():
        if path.suffix == ".md":
            continue
        r = rel(path)
        if _state_manual(saved.get(r)):
            # Tagged by hand via `sync tag` (Inbox protocol): authoritative.
            # Carry the manual entry forward untouched - even on `sync all` -
            # instead of clobbering it with location-inferred tags.
            new_state[r] = saved[r]
            same += 1
            continue
        tags = [_top_folder(path)]
        if path.suffix.lower() in EXEC_SUFFIXES:
            tags.append("script")
        elif _top_folder(path) == "library":
            tags.append("reference")
        if (not force) and prev.get(r) == tags:
            new_state[r] = tags
            same += 1
            continue
        if _set_macos_tags(path, tags):
            if sys.stdout.isatty():
                print(f"  ✅  {r}")
                print(f"       🏷️  {tags}  (binary - tags inferred from location)")
            new_state[r] = tags
            tagged += 1
        else:
            if r in prev:
                new_state[r] = prev[r]
            failed += 1
    # Keep the per-entry Memory collection indexes (People/Decisions) in sync with
    # their folders: a person/decision file created by hand (not via `memory add`)
    # is registered here on the next routine sync, so the index never silently drifts.
    relinked = _sync_collection_doc_links()
    if relinked:
        print(f"  🔗  Refreshed entry lists in {relinked} Memory collection index(es).")
    profiled = _sync_profile_doc_links()
    if profiled:
        print(f"  🔗  Refreshed entry lists in {profiled} Profile facet doc(s).")
    tiered = _sync_tier_doc_links()
    if tiered:
        print(f"  🔗  Refreshed summary links in {tiered} memory tier doc(s).")
    kids = _refresh_all_children_blocks()
    if kids:
        print(f"  🔗  Refreshed subfolder links in {kids} folder doc(s).")
    if _sync_log_open_loops():
        print(f"  🔗  Refreshed the Log's Open Loops view.")
    enriched = _sync_summary_keywords()
    if enriched:
        print(f"  🔗  Enriched topic keywords in {enriched} session summary(ies).")
    _save_sync_state(new_state)
    print()
    print(divider())
    print(f"  🏁  Done - ✅ {tagged} synced  ⏭️  {same} already current  ·  {none} no-tags  ❌ {failed} failed")
    if not force and same:
        print(f"       Incremental: {same} file(s) skipped (tags unchanged). Run `sync all` to force a full re-sync.")
    if failed:
        print(f"       See {LOG_FILE}")
    print(divider())
    return 1 if failed else 0


# ══════════════════════════════════════════════════════════
#  2 - Manifest
# ══════════════════════════════════════════════════════════

def cmd_manifest(full: bool = False) -> int:
    """📋 Rebuild the file index (manifest.json). Incremental by default: only files
    whose (mtime, size) changed are re-read and re-hashed. Pass `full` to force a
    from-scratch rebuild. Indexes markdown and binary files with SHA-256 hashes."""
    header("Rebuild Index", "📋")
    print(f"  Scanning BRAIN...   ({'full rebuild' if full else 'incremental'})")
    print(f"  Output: {MANIFEST_FILE}")
    print()
    index = build_index(incremental=not full, progress=False)
    if not save_index(index):
        fail(f"Could not write index - see {LOG_FILE}")
        return 1
    # Retire the legacy diff snapshot (superseded by the hash-based index diff).
    try:
        (DATA_DIR / "snapshot.json").unlink(missing_ok=True)
    except OSError:
        pass
    reused = index.get("_reused", 0)
    total = index["file_count"] + index["binary_count"]
    print(divider())
    print(f"  🏁  Done - {index['file_count']} markdown + {index['binary_count']} binary "
          f"= {total} files, {index['total_tokens']:,} tokens")
    if reused and not full:
        print(f"       {reused} unchanged file(s) reused from the prior index (not re-read).")
    print(f"       schema v{index['schema_version']} · BRAIN v{index['brain_version'] or '?'} · saved to {MANIFEST_FILE.name}")
    print(divider())
    return 0


# ══════════════════════════════════════════════════════════
#  2.5 - Database (local SQLite FTS5 query engine + committed roll-up)
# ══════════════════════════════════════════════════════════
#  Design: the database/index/retrieval architecture for the whole vault.
#  Markdown+YAML stays the canonical EDITING surface. Two derived layers:
#    • catalog.ndjson - LEAN, COMMITTED, dual-readable roll-up (one JSON record
#      per line -> clean per-record diffs). Ships with the vault; regenerated
#      from the live tree so it can never be committed stale.
#    • index.db - LOCAL, REBUILDABLE SQLite FTS5 query engine. Lives OUTSIDE the
#      iCloud-synced tree (~/Library/Application Support/brain/<vault-id>/) so a
#      binary file never produces an iCloud "(conflicted copy)". The notes are
#      the always-available source of recovery (hybrid-default build decision).
#  Vectors (sqlite-vec) and per-folder table views are staged follow-ons.

CATALOG_FILE      = DATA_DIR / "catalog.ndjson"   # committed, shipping, lean roll-up
DB_SCHEMA_VERSION = 1
_ROLLUP_FIELDS    = ("path", "title", "type", "folder", "layer",
                     "tags", "keywords", "description", "status", "updated")

def _db_cache_dir() -> Path:
    """Per-machine, NON-synced home for the rebuildable SQLite index. Outside the
    vault tree so iCloud never syncs (or conflict-copies) a binary file. Keyed by
    a short hash of the vault root so multiple vaults never collide."""
    vid = hashlib.sha1(str(BRAIN_DIR.resolve()).encode("utf-8")).hexdigest()[:12]
    if sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support" / "brain"
    else:
        base = Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "brain"
    d = base / vid
    d.mkdir(parents=True, exist_ok=True)
    return d

def _db_path() -> Path:
    return _db_cache_dir() / "index.db"

def _doc_path(entry: dict) -> Path:
    """Resolve a manifest entry ('BRAIN/...') back to its file on disk."""
    return BRAIN_DIR / entry.get("path", "").removeprefix("BRAIN/")

def _body_text(path: Path) -> str:
    """Markdown body with the YAML frontmatter block stripped (best-effort)."""
    try:
        text = _read_text(path)
    except OSError:
        return ""
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

def _content_md_entries(index: dict) -> list:
    """Markdown CONTENT entries for the catalog and the search index: drops
    binary files (manifest-only) and `.template/` scaffolding (blueprints, not
    content). The manifest keeps everything for integrity; the catalog stays a
    clean content database."""
    return [e for e in index.get("files", [])
            if e.get("kind") != "binary" and "/.template/" not in e.get("path", "")]

def _write_catalog(index: dict) -> int:
    """Write catalog.ndjson - the lean, committed content roll-up - from the
    index. Idempotent: rewrites only when the projection changed, so a synced
    file gets no needless mtime churn. Returns the record count."""
    md = _content_md_entries(index)
    recs = [json.dumps({k: e.get(k, [] if k in ("tags", "keywords") else "")
                        for k in _ROLLUP_FIELDS}, ensure_ascii=False, sort_keys=True)
            for e in md]
    out = ("\n".join(recs) + "\n") if recs else ""
    try:
        if not CATALOG_FILE.exists() or CATALOG_FILE.read_text(encoding="utf-8") != out:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            CATALOG_FILE.write_text(out, encoding="utf-8")
    except OSError as e:
        logging.getLogger("index").error("Could not write catalog: %s", e)
    return len(md)

def _fts5_ok() -> bool:
    try:
        c = sqlite3.connect(":memory:")
        c.execute("CREATE VIRTUAL TABLE _t USING fts5(x)")
        c.close()
        return True
    except Exception:
        return False

def _markdown_entries(full: bool = False):
    """Fresh manifest, then the markdown CONTENT entries (templates + binaries
    excluded) - the projection source for the search index. save_index writes
    catalog.ndjson in the same pass, so the roll-up can never disagree with the
    manifest."""
    index = build_index(incremental=not full, progress=False)
    save_index(index)
    return _content_md_entries(index), index

def cmd_db_rollup() -> int:
    """Regenerate catalog.ndjson - the lean, committed content roll-up. (It is
    also refreshed automatically by save_index whenever the manifest rebuilds,
    so it cannot be committed stale.)"""
    index = build_index(incremental=True, progress=False)
    save_index(index)   # writes manifest.json + catalog.ndjson in lockstep
    n = len(_content_md_entries(index))
    header("Catalog Roll-up", "🗄️")
    print(f"  🏁  {n} content record(s) -> {rel(CATALOG_FILE)}")
    print( "       committed, dual-readable, ships with the vault (templates + binaries excluded).")
    print(divider())
    return 0

def cmd_db_build(full: bool = False) -> int:
    """Build the LOCAL SQLite FTS5 query index from the notes (rebuildable; lives
    outside the synced tree). Refreshes catalog.ndjson in the same pass."""
    header("Database Build", "🗄️")
    if not _fts5_ok():
        fail("This Python's sqlite3 lacks FTS5; cannot build the query index.")
        return 1
    md, _index = _markdown_entries(full=full)   # save_index already refreshed catalog.ndjson
    dbp = _db_path()
    tmp = dbp.parent / (dbp.name + ".tmp")
    try:
        tmp.unlink(missing_ok=True)
        con = sqlite3.connect(str(tmp))
        con.execute("""CREATE VIRTUAL TABLE docs USING fts5(
            path UNINDEXED, folder UNINDEXED, type UNINDEXED, tags UNINDEXED,
            layer UNINDEXED, updated UNINDEXED,
            title, keywords, description, body, tokenize='unicode61')""")
        rows = []
        for e in md:
            rows.append((
                e.get("path", ""), e.get("folder", ""), e.get("type", ""),
                " ".join(_aslist(e.get("tags", []))), str(e.get("layer", "")),
                str(e.get("updated", "")),
                e.get("title", ""), " ".join(_aslist(e.get("keywords", []))),
                e.get("description", ""), _body_text(_doc_path(e)),
            ))
        con.executemany(
            "INSERT INTO docs (path,folder,type,tags,layer,updated,title,keywords,description,body) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)", rows)
        con.execute("CREATE TABLE meta (k TEXT PRIMARY KEY, v TEXT)")
        con.executemany("INSERT INTO meta VALUES (?,?)", [
            ("schema", str(DB_SCHEMA_VERSION)),
            ("built", datetime.now(timezone.utc).isoformat()),
            ("rows", str(len(rows))),
            ("brain_version", _brain_version() or ""),
        ])
        con.commit()
        con.close()
        os.replace(tmp, dbp)
    except Exception as e:
        fail(f"Index build failed: {e}")
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
        return 1
    print(f"  🏁  Indexed {len(md)} note(s) for full-text search.")
    print(f"       Engine : {dbp}")
    print( "                (local, rebuildable, never synced)")
    print(f"       Roll-up: {rel(CATALOG_FILE)} (committed, ships)")
    print(divider())
    return 0

def _fts_query(raw: str) -> str:
    """Forgiving FTS5 MATCH string: bare words -> AND of quoted terms; leave
    explicit FTS operators (quotes, AND/OR/NOT, *, :, parens) untouched."""
    raw = raw.strip()
    if not raw or re.search(r'["*:()]|\bAND\b|\bOR\b|\bNOT\b', raw):
        return raw
    terms = [t for t in re.split(r"\s+", raw) if t]
    return " AND ".join(f'"{t}"' for t in terms)

def cmd_db_search(query: str = "", folder_filter: str = "",
                  type_filter: str = "", limit: int = 20) -> int:
    header("Database Search", "🔎")
    if not query.strip():
        print('  Usage: db search "terms" [folder=<f>] [type=<t>]')
        print(divider())
        return 1
    dbp = _db_path()
    if not dbp.exists():
        print("  No local index yet - building it now...")
        rc = cmd_db_build()
        if rc:
            return rc
    con = sqlite3.connect(str(dbp))
    where = ["docs MATCH ?"]
    params = [_fts_query(query)]
    if folder_filter:
        where.append("folder = ?"); params.append(folder_filter)
    if type_filter:
        where.append("type = ?"); params.append(type_filter)
    sql = ("SELECT path, title, type, folder, "
           "snippet(docs, 9, '〚', '〛', '…', 12) AS snip "
           f"FROM docs WHERE {' AND '.join(where)} ORDER BY bm25(docs) LIMIT ?")
    params.append(limit)
    try:
        rows = con.execute(sql, params).fetchall()
    except sqlite3.OperationalError:
        try:
            params[0] = '"' + query.replace('"', " ") + '"'
            rows = con.execute(sql, params).fetchall()
        except sqlite3.OperationalError as e2:
            con.close()
            fail(f"Bad search query: {e2}")
            return 1
    con.close()
    if not rows:
        print(f"  No matches for: {query}")
        print(divider())
        return 0
    for path, title, typ, folder, snip in rows:
        # Stored paths carry the catalog's BRAIN/ prefix; print them the way
        # every other command prints paths (vault-relative). Artifacts unchanged.
        disp = path[6:] if path.startswith("BRAIN/") else path
        print(f"  • {title or disp}  [{typ}/{folder}]")
        print(f"      {disp}")
        if snip and snip.strip():
            print(f"      {snip.strip()}")
    print(divider())
    print(f"  {len(rows)} result(s) for: {query}")
    if len(rows) == limit:
        print(f"  showing top {limit}; refine or raise limit= (cap 100)")
    print(divider())
    return 0

def cmd_db_status() -> int:
    header("Database Status", "🗄️")
    print(f"  Roll-up (committed, ships): {rel(CATALOG_FILE)}")
    if CATALOG_FILE.exists():
        n = sum(1 for _ in CATALOG_FILE.open(encoding="utf-8"))
        print(f"     {n} record(s) · {CATALOG_FILE.stat().st_size:,} bytes")
    else:
        print("     (not generated yet - run `db rollup` or `db build`)")
    dbp = _db_path()
    print(f"  Query engine (local, not synced): {dbp}")
    if dbp.exists():
        try:
            con = sqlite3.connect(str(dbp))
            meta = dict(con.execute("SELECT k, v FROM meta").fetchall())
            con.close()
            print(f"     {meta.get('rows','?')} note(s) · schema v{meta.get('schema','?')} "
                  f"· built {meta.get('built','?')}")
        except Exception:
            print("     (present but unreadable - run `db build` to rebuild)")
    else:
        print("     (not built yet - run `db build`)")
    print(divider())
    return 0

def cmd_db(rest=None) -> int:
    """🗄️ Local SQLite FTS5 query engine + committed NDJSON roll-up.
    Subcommands: build | rollup | search "terms" [folder=x type=y limit=N] | status."""
    rest = rest or []
    sub = (rest[0].lower() if rest else "status")
    if sub in ("build", "rebuild", "all", "refresh"):
        return cmd_db_build(full=any(a.lower() in ("full", "--full", "all") for a in rest[1:]))
    if sub == "rollup":
        return cmd_db_rollup()
    if sub == "search":
        # Only folder= / type= / limit= are filters; any other key=value arg
        # is almost always query text (a search for "x=y"), so treat it as
        # query text and say so instead of silently eating it.
        filters, words = {}, []
        for a in rest[1:]:
            if "=" in a:
                k, v = a.split("=", 1)
                if k in ("folder", "type", "limit"):
                    filters[k] = v
                    continue
                print(f"  ℹ️   '{a}' is not a filter (folder=, type=, limit=) - treating it as query text.")
            words.append(a)
        terms = " ".join(words)
        try:
            limit = int(filters.get("limit", "20"))
        except ValueError:
            limit = 20
        limit = max(1, min(100, limit))
        return cmd_db_search(query=terms, folder_filter=filters.get("folder", ""),
                             type_filter=filters.get("type", ""), limit=limit)
    if sub in ("status", ""):
        return cmd_db_status()
    fail(f"Unknown db subcommand: {sub}  (build | rollup | search | status)")
    return 1


# ══════════════════════════════════════════════════════════
#  2.6 - Knowledge Base (offline ZIM reference via libzim)
# ══════════════════════════════════════════════════════════
#  World-knowledge search that sits BESIDE the vault's own SQLite/FTS5 search.
#  External reference works (Wikipedia, Wiktionary, ...) live as READ-ONLY ZIM
#  files in Library/Reference & Encyclopedia/ and are searched through the OPTIONAL `libzim`
#  package (each ZIM ships its own Xapian full-text index). Two engines, two
#  jobs: SQLite/FTS5 = your notes; ZIM = the world's knowledge.
#
#  The ZIMs are large, re-downloadable binaries: never committed (see
#  .gitignore), fetched from Kiwix by `kb refresh`. libzim is the only new
#  dependency and it is OPTIONAL - if it is missing, kb degrades with a clean
#  install hint and nothing else in brain.command is affected.

KB_DIR        = BRAIN_DIR / "Library" / "Reference & Encyclopedia"   # read-only ZIM store (in the vault)
KB_MANIFEST   = KB_DIR / "sources.json"            # committed: which sources to keep (unique name; dodges the System/Data/manifest.json wikilink collision)
KB_BASE_URL   = "https://lb.download.kiwix.org/zim/wikipedia/"
KB_RESULT_CAP = 10

# Sources kb knows how to fetch. `prefix` is the Kiwix filename stem; the dated
# file (e.g. ..._2026-06.zim) is resolved at refresh time, never hardcoded, so a
# refresh always lands the newest monthly build.
KB_DEFAULT_MANIFEST = {
    "sources": [
        {"name": "wikipedia-simple", "prefix": "wikipedia_en_simple_all_nopic",
         "base": KB_BASE_URL, "enabled": True,
         "note": "Simple English Wikipedia, full text, no images (~1 GB)"},
        {"name": "wikipedia", "prefix": "wikipedia_en_all_nopic",
         "base": KB_BASE_URL, "enabled": False,
         "note": "Full English Wikipedia, full text, no images (~50 GB)"},
    ]
}

def _kb_human(n: int) -> str:
    """Human-readable byte size."""
    f = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if f < 1024 or unit == "TB":
            return f"{f:.0f} {unit}" if unit in ("B", "KB") else f"{f:.1f} {unit}"
        f /= 1024
    return f"{f:.1f} TB"

def _kb_zims() -> list:
    """Every .zim currently in Library/Reference & Encyclopedia/, sorted by name."""
    return sorted(KB_DIR.glob("*.zim")) if KB_DIR.exists() else []

def _kb_source_label(fname: str) -> str:
    """Readable corpus label from a ZIM filename (drops the _YYYY-MM.zim tail)."""
    return re.sub(r"_\d{4}-\d{2}\.zim$", "", fname).replace("_", " ")

def _kb_load_manifest() -> dict:
    """Read the committed manifest (which sources to keep). Falls back to a fresh
    copy of the built-in default when the file is missing or unreadable."""
    try:
        return json.loads(KB_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return json.loads(json.dumps(KB_DEFAULT_MANIFEST))

def _kb_save_manifest(man: dict) -> None:
    KB_DIR.mkdir(parents=True, exist_ok=True)
    KB_MANIFEST.write_text(json.dumps(man, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")

KB_LINKS_START = "<!-- kb:files (auto-maintained by brain.command kb - do not edit by hand) -->"
KB_LINKS_END   = "<!-- /kb:files -->"

def _kb_namesake() -> Path:
    """The folder's namesake doc (e.g. Reference & Encyclopedia.md)."""
    return KB_DIR / f"{KB_DIR.name}.md"

def _kb_files_body() -> str:
    """Interior of the kb:files block: one wikilink per ZIM actually on disk
    (the clean `name_date.zim` names are self-describing). Placeholder when
    none are present."""
    zims = _kb_zims()
    if not zims:
        return ("_No knowledge bases downloaded yet. "
                "Run `brain.command kb refresh`._")
    return "\n".join(f"- [[{zp.name}]] ({_kb_human(zp.stat().st_size)})" for zp in zims)

def _kb_sync_links() -> bool:
    """Rewrite the namesake's kb:files block to wikilink the ZIMs now on disk
    (creating a `## Downloaded files` section if absent). Returns True if the doc
    changed. ZIM wikilinks are exempt from the broken-link check (gitignored,
    machine-local data), so this stays health-clean even on a fresh clone."""
    doc = _kb_namesake()
    body = _kb_files_body()
    try:
        text = _read_text(doc)
    except OSError as e:
        warn(f"{rel(doc)}: cannot read for the kb files block ({e}) - not synced.")
        return False
    if KB_LINKS_START not in text:
        # First run: inject the section with its marker pair; every later
        # refresh goes through the shared marker-block writer below.
        block = f"{KB_LINKS_START}\n{body}\n{KB_LINKS_END}"
        try:
            _write_atomic(doc, text.rstrip() + f"\n\n## Downloaded files\n\n{block}\n")
            return True
        except OSError as e:
            warn(f"{rel(doc)}: write failed for the kb files block: {e}")
            return False
    return _sync_marker_block(doc, KB_LINKS_START, KB_LINKS_END, body, "kb files")

def _kb_reader():
    """Import the optional libzim reader+search API. Returns (Archive, Query,
    Searcher) or None after printing a clean install hint. Mirrors the
    ripgrep-optional pattern: probe, bail cleanly, never raise."""
    try:
        from libzim.reader import Archive
        from libzim.search import Query, Searcher
        return Archive, Query, Searcher
    except ImportError:
        fail("libzim is not installed.")
        print("       It powers ZIM knowledge-base search. Install it with:")
        print("           python3 -m pip install libzim")
        print("       or let brain.command do it:  kb setup")
        return None

def _kb_plaintext(arc, path: str) -> str:
    """Full plain text of a ZIM article: drop CSS/JS, turn block-end tags into
    newlines so paragraphs survive, strip the rest, unescape entities."""
    import html as _htmlmod
    try:
        item = arc.get_entry_by_path(path).get_item()
        raw = bytes(item.content).decode("utf-8", "ignore")
    except Exception:
        return ""
    raw = re.sub(r"(?is)<(style|script)\b[^>]*>.*?</\1>", " ", raw)    # drop CSS/JS bodies
    raw = re.sub(r"(?i)</(p|div|li|h[1-6]|tr)\s*>", "\n", raw)         # block ends -> newline
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)                                 # strip remaining tags
    text = _htmlmod.unescape(raw)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def _kb_snippet(arc, path: str, length: int = 160) -> str:
    """Best-effort one-line preview of a ZIM article (built from the plain text)."""
    text = re.sub(r"\s+", " ", _kb_plaintext(arc, path)).strip()
    return (text[:length] + "…") if len(text) > length else text

def _kb_round_robin(results: list, limit: int) -> list:
    """Interleave hits by source so one corpus never crowds out the rest. bm25 is
    per-archive, so cross-source scores are not comparable - round-robin is the
    honest merge."""
    buckets: dict = {}
    order = []
    for r in results:
        if r[0] not in buckets:
            buckets[r[0]] = []
            order.append(r[0])
        buckets[r[0]].append(r)
    out = []
    while len(out) < limit and any(buckets[k] for k in order):
        for k in order:
            if buckets[k]:
                out.append(buckets[k].pop(0))
                if len(out) >= limit:
                    break
    return out

def cmd_kb_search(query: str = "", limit: int = KB_RESULT_CAP) -> int:
    """Search every ZIM in Library/Reference & Encyclopedia/ via libzim's full-text index."""
    header("Knowledge Base Search", "🔎")
    if not query.strip():
        print('  Usage: kb search "terms"')
        print(divider())
        return 1
    zims = _kb_zims()
    if not zims:
        warn("No knowledge bases installed in Library/Reference & Encyclopedia/.")
        print("       Run:  brain.command kb refresh   (downloads from Kiwix)")
        print(divider())
        return 0
    libs = _kb_reader()
    if libs is None:
        print(divider())
        return 1
    Archive, Query, Searcher = libs
    results = []   # (source, path, archive) - titles resolved lazily for shown hits only
    qtok = set(re.findall(r"[a-z0-9]+", query.lower()))
    dropped = 0
    for zp in zims:
        try:
            arc = Archive(str(zp))
        except Exception as e:
            logging.getLogger("kb").error("open %s: %s", zp.name, e)
            continue
        if not getattr(arc, "has_fulltext_index", True):
            continue
        src = _kb_source_label(zp.name)
        seen = set()
        # Title matches first (the article named like the query), then full text -
        # so "DNA" surfaces the DNA article before DNA replication, and "World War
        # II" the article itself before term-dense list pages.
        try:
            from libzim.suggestion import SuggestionSearcher
            for p in SuggestionSearcher(arc).suggest(query).getResults(0, limit):
                if p in seen:
                    continue
                # Relevance floor: a title suggestion that shares no lowercase
                # token with the query (prefixes count, so "stoic" still meets
                # "Stoicism") is suggestion-engine junk - drop it. Full-text
                # hits below earned their rank and are never dropped.
                try:
                    t = str(arc.get_entry_by_path(p).title)
                except Exception:
                    t = p
                ttok = set(re.findall(r"[a-z0-9]+", f"{t} {p}".lower()))
                if qtok and not (qtok & ttok
                                 or any(tt.startswith(qt) for qt in qtok for tt in ttok)):
                    dropped += 1
                    continue
                seen.add(p); results.append((src, p, arc))
        except Exception:
            pass
        try:
            for p in Searcher(arc).search(Query().set_query(query)).getResults(0, limit):
                if p not in seen:
                    seen.add(p); results.append((src, p, arc))
        except Exception as e:
            logging.getLogger("kb").error("search %s: %s", zp.name, e)
            continue
    if not results:
        if dropped:
            print(f"  No strong matches for: {query}  ({dropped} weak title suggestion(s) dropped)")
        else:
            print(f"  No matches for: {query}")
        print(divider())
        return 0
    shown = _kb_round_robin(results, limit)   # resolve titles only for what we show
    for src, p, arc in shown:
        try:
            title = arc.get_entry_by_path(p).title
        except Exception as e:
            logging.getLogger("kb").debug("title %s: %s", p, e)
            title = p
        print(f"  • {title}  [{src}]")
        snip = _kb_snippet(arc, p)
        if snip:
            print(f"      {snip}")
    print(divider())
    print(f"  {len(shown)} result(s) for: {query}   ·   {len(zims)} knowledge base(s)")
    if len(shown) == limit:
        print(f"  showing top {limit} (the kb result cap); refine the query for more precision")
    print(divider())
    return 0

def cmd_kb_read(article: str = "", limit_chars: int = 6000) -> int:
    """Read a knowledge-base article's full text by title or path, resolved across
    the installed ZIMs. The read companion to `kb search`: search finds the title,
    read returns the body, so a finding can be fetched and read, then cited."""
    header("Knowledge Base Read", "📖")
    if not article.strip():
        print('  Usage: kb read "article title or path"  [--chars N]')
        print(divider()); return 1
    zims = _kb_zims()
    if not zims:
        warn("No knowledge bases installed in Library/Reference & Encyclopedia/.")
        print(divider()); return 0
    libs = _kb_reader()
    if libs is None:
        print(divider()); return 1
    Archive, Query, Searcher = libs
    for zp in zims:
        try:
            arc = Archive(str(zp))
        except Exception:
            continue
        src = _kb_source_label(zp.name)
        path = None
        try:
            arc.get_entry_by_path(article)           # exact path hit
            path = article
        except Exception:
            try:
                from libzim.suggestion import SuggestionSearcher
                hits = list(SuggestionSearcher(arc).suggest(article).getResults(0, 1))
                path = hits[0] if hits else None     # best title match
            except Exception:
                path = None
        if not path:
            continue
        try:
            title = arc.get_entry_by_path(path).title
        except Exception:
            title = path
        body = _kb_plaintext(arc, path)
        if not body:
            continue
        total = len(body)
        print(f"  📖  {title}   [{src}]")
        print(f"      path: {path}   ·   {total} chars   ·   {zp.name}")
        print(divider())
        print(body if total <= limit_chars else body[:limit_chars])
        if total > limit_chars:
            print(f"\n  … [{total - limit_chars} more chars; raise --chars to read more]")
        print(divider())
        print(f"  Cite as: {src}, article \"{title}\" ({zp.stem})")
        print(divider())
        return 0
    fail(f"No article matching '{article}' in the installed knowledge bases.")
    print("       Run `kb search` first to find the exact title.")
    print(divider()); return 1

def cmd_kb_list() -> int:
    """List installed ZIM knowledge bases and the manifest's known sources."""
    header("Knowledge Bases", "📚")
    zims = _kb_zims()
    try:
        from libzim.reader import Archive
    except ImportError:
        Archive = None
    if not zims:
        print("  No knowledge bases installed in Library/Reference & Encyclopedia/.")
    for zp in zims:
        detail = ""
        if Archive is not None:
            try:
                arc = Archive(str(zp))
                searchable = "searchable" if getattr(arc, "has_fulltext_index", False) else "no index"
                detail = f"   ·   {arc.entry_count:,} entries   ·   {searchable}"
            except Exception:
                detail = "   ·   (unreadable)"
        print(f"  📖  {zp.name}   ({_kb_human(zp.stat().st_size)}){detail}")
    print()
    print("  Sources (toggle with: kb add <name> | kb remove <name>):")
    for s in _kb_load_manifest().get("sources", []):
        mark = "on " if s.get("enabled") else "off"
        print(f"      [{mark}]  {s['name']:<21} {s.get('note', '')}")
    print(divider())
    print(f"  {len(zims)} installed   ·   {rel(KB_DIR)}")
    print(divider())
    return 0

def _kb_latest(prefix: str, base: str) -> tuple:
    """Resolve the newest dated ZIM for a Kiwix prefix by parsing the directory
    listing (YYYY-MM sorts chronologically). Returns (url, filename) or (None, None)."""
    try:
        html = urllib.request.urlopen(base, timeout=60).read().decode("utf-8", "ignore")
    except Exception as e:
        logging.getLogger("kb").error("list %s: %s", base, e)
        return (None, None)
    pat = r'(?:^|[">/])' + re.escape(prefix) + r"_(\d{4}-\d{2})\.zim"   # anchor to a filename boundary
    dates = sorted(set(re.findall(pat, html)))
    if not dates:
        warn(f"Fetched the Kiwix listing but found no {prefix}_YYYY-MM.zim entries (its index format may have changed).")
        return (None, None)
    fname = f"{prefix}_{dates[-1]}.zim"
    return (base + fname, fname)

def _kb_sha256_ok(part: Path, url: str) -> bool:
    """Verify a download against Kiwix's sibling .zim.sha256. Returns True on a
    match OR when no checksum is published (best-effort), False only on a real
    mismatch. Hashing a 50 GB file is slow, so this is opt-in (kb refresh --verify)."""
    try:
        want = urllib.request.urlopen(url + ".sha256", timeout=30).read().decode().split()[0].lower()
    except Exception:
        warn("No published checksum found; skipping verification.")
        return True
    h = hashlib.sha256()
    with open(part, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest() == want

def _kb_download(url: str, dest: Path, verify: bool = False) -> bool:
    """Stream a (possibly huge) file to dest, resuming a prior .part via an HTTP
    Range request when the server allows it. Validates the byte count (and, with
    verify=True, the sha256) BEFORE an atomic os.replace into place, so a truncated
    or corrupt transfer is never promoted. Returns True on success."""
    part = dest.with_name(dest.name + ".part")
    have = part.stat().st_size if part.exists() else 0
    req = urllib.request.Request(url)
    if have:
        req.add_header("Range", f"bytes={have}-")
    try:
        resp = urllib.request.urlopen(req, timeout=120)
    except urllib.error.HTTPError as e:
        if have and e.code == 416:        # stale/oversized .part: discard and restart clean
            part.unlink(missing_ok=True)
            return _kb_download(url, dest, verify)
        fail(f"Download failed: {e}")
        return False
    except Exception as e:
        fail(f"Download failed: {e}")
        return False
    mode = "ab"
    if have and getattr(resp, "status", 200) != 206:   # server ignored Range
        have, mode = 0, "wb"
    clen = resp.headers.get("Content-Length")
    try:
        total = (have + int(clen)) if clen else 0
    except (TypeError, ValueError):
        total = 0
    done = have
    try:
        with open(part, mode) as f:
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                f.write(chunk)
                done += len(chunk)
                if total:
                    print(f"\r       {done * 100 // total:3d}%  {_kb_human(done)} / {_kb_human(total)}",
                          end="", flush=True)
        if total:
            print()
    except Exception as e:
        print()
        fail(f"Interrupted: {e}   (partial kept; rerun kb refresh to resume)")
        return False
    if total and done != total:
        fail(f"Truncated: got {_kb_human(done)} of {_kb_human(total)}; partial kept, rerun kb refresh to resume.")
        return False
    if verify and not _kb_sha256_ok(part, url):
        fail("Checksum mismatch; partial kept, not installed.")
        return False
    os.replace(part, dest)
    return True

def cmd_kb_refresh(name: str = "", verify: bool = False) -> int:
    """Download/update enabled (or one named) knowledge base from Kiwix."""
    header("Knowledge Base Refresh", "🔄")
    KB_DIR.mkdir(parents=True, exist_ok=True)
    sources = [s for s in _kb_load_manifest().get("sources", [])
               if (s.get("name") == name) or (not name and s.get("enabled"))]
    if not sources:
        if name:
            fail(f"No manifest source named '{name}'.")
        else:
            warn("No sources enabled.  Enable one:  brain.command kb add <name>")
        print(divider())
        return 1
    rc = 0
    for s in sources:
        prefix, base, name = s.get("prefix", ""), s.get("base", KB_BASE_URL), s.get("name", "")
        # Both the Kiwix prefix and the source name become filenames, so neither may
        # contain a path separator or traverse out of the folder (the manifest is
        # hand-editable). Reject anything but a plain stem.
        if (not re.fullmatch(r"[A-Za-z0-9._-]+", prefix) or ".." in prefix
                or not re.fullmatch(r"[A-Za-z0-9._-]+", name) or ".." in name):
            fail(f"Unsafe source prefix/name: {prefix!r} / {name!r}  (letters, digits, '.', '-', '_' only).")
            rc = 1
            continue
        print(f"  • {name}: resolving latest from Kiwix ...")
        url, kiwix = _kb_latest(prefix, base)
        if not kiwix:
            fail(f"Could not resolve a current file for '{prefix}'.")
            rc = 1
            continue
        m = re.search(r"_(\d{4}-\d{2})\.zim$", kiwix)
        date = m.group(1) if m else ""
        fname = f"{name}_{date}.zim" if date else f"{name}.zim"   # clean local name
        dest = KB_DIR / fname
        if dest.exists():
            print(f"      already current: {fname}")
            continue
        print(f"      downloading {fname}   (from {kiwix}; {s.get('note', '')})")
        if not _kb_download(url, dest, verify):
            rc = 1
            continue
        # Remove only older dated builds of THIS source, inside KB_DIR, announced (3.1).
        old_re = re.compile(re.escape(name) + r"_\d{4}-\d{2}\.zim")
        for old in KB_DIR.glob("*.zim"):
            if old.name != fname and old_re.fullmatch(old.name):
                # 3.1: a permanent delete needs its own confirmation, even for
                # a re-downloadable multi-GB blob (.trash staging is impractical
                # at this size, so an explicit confirm is the honest compliance).
                if not confirm(f"      Remove the older build {old.name} permanently? (yes/no): "):
                    print(f"      kept: {old.name}")
                    continue
                print(f"      removing older build: {old.name}")
                old.unlink(missing_ok=True)
        ok(f"installed {fname}   ({_kb_human(dest.stat().st_size)})")
    _kb_sync_links()   # reconnect the namesake doc to the files now on disk
    print(divider())
    if rc == 0:
        print("  🏁  Knowledge bases up to date.")
        print("       In Finder, right-click each .zim -> Keep Downloaded (blocks iCloud eviction).")
    print(divider())
    return rc

def cmd_kb_setup() -> int:
    """First-run: ensure the manifest, install libzim, fetch enabled sources."""
    header("Knowledge Base Setup", "🚀")
    KB_DIR.mkdir(parents=True, exist_ok=True)
    if not KB_MANIFEST.exists():
        _kb_save_manifest(json.loads(json.dumps(KB_DEFAULT_MANIFEST)))
        ok(f"wrote manifest: {rel(KB_MANIFEST)}")
    try:
        import libzim  # noqa: F401
        ok("libzim already installed.")
    except ImportError:
        print("  Installing libzim (one-time, optional dependency) ...")
        installed = False
        for extra in ([], ["--user"]):   # retry with --user for PEP 668 externally-managed Pythons
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", *extra, "libzim"], check=True)
                installed = True
                break
            except Exception as e:
                logging.getLogger("kb").debug("pip install %s failed: %s", extra or "(default)", e)
        if installed:
            ok("libzim installed.")
        else:
            fail("Could not auto-install libzim.")
            print("       Install it manually, then rerun  kb setup :")
            print("           python3 -m pip install libzim")
            print("       If your Python blocks system installs (PEP 668), use a venv.")
            print(divider())
            return 1
    print()
    return cmd_kb_refresh()

def cmd_kb_toggle(name: str, enable: bool) -> int:
    """Flip a manifest source on/off (kb add / kb remove)."""
    man = _kb_load_manifest()
    for s in man.get("sources", []):
        if s.get("name") == name:
            s["enabled"] = enable
            _kb_save_manifest(man)
            header("Knowledge Base", "📚")
            ok(f"{name} {'enabled' if enable else 'disabled'}.")
            if enable:
                print("       Run  brain.command kb refresh  to download it.")
            print(divider())
            return 0
    known = ", ".join(s.get("name", "?") for s in man.get("sources", []))
    fail(f"No manifest source named '{name}'.   Known: {known}")
    return 1

def cmd_kb_relink() -> int:
    """Rewrite the namesake's kb:files block to wikilink the ZIMs now on disk."""
    header("Knowledge Base Relink", "🔗")
    changed = _kb_sync_links()
    n = len(_kb_zims())
    if changed:
        ok(f"Linked {n} file(s) into {rel(_kb_namesake())}.")
    else:
        print(f"  Already in sync ({n} file(s) on disk).")
    print(divider())
    return 0

def cmd_kb(rest=None) -> int:
    """📚 Knowledge Base: offline ZIM reference search and read (Library/Reference & Encyclopedia/).
    Subcommands: search "terms" | read "article" [--chars N] | list | refresh [name] | setup | relink | add <name> | remove <name>."""
    rest = rest or []
    sub = (rest[0].lower() if rest else "list")
    if sub == "search":
        args = rest[1:]
        flags = [a for a in args if a.startswith("--")]
        if flags:
            fail(f"kb search takes no flags; unknown: {' '.join(flags)}.  Usage: kb search \"terms\"")
            return 1
        return cmd_kb_search(query=" ".join(args))
    if sub == "read":
        args = rest[1:]
        chars, out, i = 6000, [], 0
        while i < len(args):
            a = args[i]
            if a == "--chars" and i + 1 < len(args) and args[i + 1].isdigit():
                chars = int(args[i + 1]); i += 2; continue
            if a.startswith("--"):
                fail(f"kb read: unknown flag {a}.  Usage: kb read \"article\" [--chars N]"); return 1
            out.append(a); i += 1
        return cmd_kb_read(article=" ".join(out), limit_chars=chars)
    if sub in ("list", "status", ""):
        return cmd_kb_list()
    if sub == "refresh":
        args = rest[1:]
        target = next((a for a in args if not a.startswith("--")), "")
        return cmd_kb_refresh(name=target, verify=("--verify" in args))
    if sub == "setup":
        return cmd_kb_setup()
    if sub == "relink":
        return cmd_kb_relink()
    if sub == "add":
        if len(rest) < 2:
            fail("Usage: kb add <name>"); return 1
        return cmd_kb_toggle(rest[1], True)
    if sub in ("remove", "rm"):
        if len(rest) < 2:
            fail("Usage: kb remove <name>"); return 1
        return cmd_kb_toggle(rest[1], False)
    fail(f"Unknown kb subcommand: {sub}  (search | read | list | refresh | setup | relink | add | remove)")
    return 1


# ══════════════════════════════════════════════════════════
#  3 - Lint
# ══════════════════════════════════════════════════════════

def _toolkit_brain_doc(path: Path) -> bool:
    """True if a file follows the BRAIN frontmatter schema; False if it is
    external format (a skill spec or the derived catalog) under System/Toolkit/
    and so exempt from BRAIN lint and the wikilink graph. Inside System/Toolkit/,
    Toolkit.md, each section namesake (Skills.md, Agents.md), and each skill's
    namesake (develop/Develop.md, stem matches its folder) are BRAIN docs; the
    skill specs and the catalog are external. Everything outside System/Toolkit/
    follows the normal BRAIN rules - including the AR agent workforce in
    Ventures/Agent Resources (AR)/, whose agents and rosters now carry full
    BRAIN frontmatter and are linted like any other content file."""
    parts = path.parts
    if "Toolkit" not in parts or "System" not in parts:
        return True  # not a Toolkit file - normal rules apply
    after = parts[parts.index("Toolkit") + 1:]
    if after == ("Toolkit.md",):
        return True
    if len(after) == 2 and after[1] == after[0] + ".md":
        return True
    if len(after) == 3 and after[0] == "Skills" \
            and Path(after[2]).suffix == ".md" \
            and Path(after[2]).stem.lower() == after[1].lower():
        return True
    return False


def _is_core_file(path: Path) -> bool:
    """Location-based 'core/contract' test: the files that carry a per-file
    `version`. Mirrors the changelog's core-files definition (Instructions 8.6):
    root governance (Constitution/Instructions/Information/AGENTS/CLAUDE),
    anything under System/, any .template/ file, and the Layer-1
    folder docs (the folder-named doc directly inside a Layer-1 folder, e.g.
    Memory/Memory.md). Everything else - Library content and its subfolder
    docs, Memory/Profile/Projects/Ventures content - is NOT core."""
    try:
        parts = path.resolve().relative_to(BRAIN_DIR.resolve()).parts
    except ValueError:
        return False
    if not parts:
        return False
    name = parts[-1]
    if len(parts) == 1 and name in {"Constitution.md", "Instructions.md",
                                    "Information.md", "AGENTS.md", "CLAUDE.md"}:
        return True
    if parts[0] == "System":
        return True
    if ".template" in parts or "Template" in parts:
        return True
    if len(parts) == 2 and name == parts[0] + ".md":   # Layer-1 folder doc
        return True
    return False


def cmd_lint(target: str = "") -> int:
    """🔍 Validate frontmatter schema across all .md files, or one file with
    `lint <path>` (the Section 10.3 verify-before-clearing-backups step)."""
    header("Frontmatter Lint", "🔍")
    target_path = None
    if target:
        target_path = (BRAIN_DIR / target) if not Path(target).is_absolute() else Path(target)
        try:
            target_path = target_path.resolve()
        except OSError:
            pass
        if not target_path.is_file():
            fail(f"File not found: {target}")
            return 1
    errors, warnings, passed, skipped = [], [], 0, 0
    for path in iter_md_files():
        if target_path and path.resolve() != target_path:
            continue
        # System/Toolkit/ content (Skills/) follows its
        # own external formats, not the BRAIN schema. Only the section docs
        # and each item's namesake doc (develop/Develop.md) are BRAIN
        # documents and validated. See System/Toolkit/Skills/Skills.md.
        if not _toolkit_brain_doc(path):
            if sys.stdout.isatty():
                print(f"  ⊘  {rel(path)}  (toolkit item - external format, exempt)")
            skipped += 1
            continue
        # Single read per file: the empty check, frontmatter parse, template
        # wikilink check, and em-dash check below all reuse this text instead
        # of re-reading the file three or four times.
        try:
            text = _read_text(path)
        except OSError:
            text = None
        fm = _parse_frontmatter_text(text) if text is not None else None
        file_errors = []
        # Article 3.8: a BRAIN file is never cleared to empty. Flag a file with
        # no content (empty or whitespace-only) so an accidental wipe surfaces.
        if text is not None and not text.strip():
            file_errors.append(
                "file is empty - Article 3.8 forbids clearing a BRAIN file's "
                "contents (restore from System/.backups/, or remove via trash)"
            )
        if fm is None:
            file_errors.append("missing frontmatter block entirely")
        else:
            for field in REQUIRED_FIELDS:
                if field not in fm:
                    file_errors.append(f"missing field: {field}")
            ft = fm.get("type", "")
            if ft and ft not in VALID_FILE_TYPES:
                file_errors.append(f"invalid type: '{ft}' (valid: {sorted(VALID_FILE_TYPES)})")
            bf = fm.get("folder", "")
            if bf and bf not in VALID_FOLDERS:
                file_errors.append(f"invalid folder: '{bf}' (valid: {sorted(VALID_FOLDERS)})")
            # v3 schema: id format (uniqueness is checked vault-wide below).
            fid = fm.get("id", "")
            if fid and not ID_RE.fullmatch(str(fid)):
                file_errors.append(
                    f"invalid id: '{fid}' - must match {ID_RE.pattern} "
                    "(lowercase, two-letter folder prefix, hyphenated)")
            # v3 schema: status must be one of the lifecycle enum values.
            stt = fm.get("status", "")
            if stt and stt not in VALID_STATUS:
                file_errors.append(f"invalid status: '{stt}' (valid: {sorted(VALID_STATUS)})")
            # v3 schema: version (MAJOR.MINOR.PATCH) is required on core/contract
            # files (location-based, see _is_core_file / Instructions 8.6) and
            # forbidden on content files, which rely on `updated` + history.
            ver = fm.get("version", "")
            core = _is_core_file(path)
            if core and not ver:
                file_errors.append(
                    "missing field: version (required on core/contract files - MAJOR.MINOR.PATCH)")
            if ver and not core:
                file_errors.append(
                    "version present on a content file - only core/contract files "
                    "carry version (Instructions 8.6); remove the line")
            if ver and not VERSION_RE.fullmatch(str(ver)):
                file_errors.append(
                    f"version is '{ver}' - must be two-digit zero-padded MM.mm.pp")
            # Filename law (Article 2.6): underscores are never word separators
            # in any BRAIN file or folder name. Skill files are exempted above.
            if "_" in path.name:
                file_errors.append(
                    "filename contains an underscore (Article 2.6 - use spaces or hyphens)"
                )
            bp = fm.get("path", "")
            expected = "BRAIN/" + rel(path)
            is_template = "Template" in path.parts or ".template" in path.parts
            # Tiered-memory session summaries move between Current/Recent and the
            # Archive as they cascade, so their `path` frontmatter is allowed to
            # differ from their current tier. They still require frontmatter/tags.
            is_memory_summary = (
                "Memory" in path.parts
                and (path.parent.name in ("Current", "Recent")
                     or "Archive" in path.parts)
            )
            if bp and bp != expected and not is_template and not is_memory_summary:
                file_errors.append(f"path mismatch: '{bp}' expected '{expected}'")
            tags = fm.get("tags", [])
            if isinstance(tags, list):
                # Closed-vocabulary tagging (Constitution Article VII).
                # Every tag must come from the fixed vocabulary below - there is
                # no free-form "content" dimension. The Folder tag must match the
                # `folder` field and the File Role tag must match the `type` field.
                bf = fm.get("folder", "")
                ft = fm.get("type", "")
                CLOSED_VOCAB = (VALID_FOLDERS | VALID_FILE_TYPES |
                                VALID_AI_SIGNAL_TAGS | VALID_SENSITIVITY_TAGS |
                                VALID_FRESHNESS_TAGS)
                # Reject any tag outside the vocabulary (e.g. legacy content tags)
                for t in tags:
                    if t not in CLOSED_VOCAB:
                        file_errors.append(
                            f"non-vocabulary tag: '{t}' (Article VII is a closed vocabulary - no content tags)"
                        )
                # Folder tag required, must match the folder field
                if bf and bf not in tags:
                    file_errors.append(
                        f"missing Folder tag: '{bf}' (must appear in tags per Article 7.2)"
                    )
                # File Role tag required, must match the type field
                if ft and ft not in tags:
                    file_errors.append(
                        f"missing File Role tag: '{ft}' (must appear in tags per Article 7.3)"
                    )
                # Article 7.1: exactly one Folder tag, exactly one File Role
                # tag, at most one Freshness tag - and canonical order
                # (Folder, Role, startup, sensitive, freshness). Order matters
                # because retrieval and Finder filters key off position.
                n_folder = sum(1 for x in tags if x in VALID_FOLDERS)
                n_role = sum(1 for x in tags if x in VALID_FILE_TYPES)
                n_fresh = sum(1 for x in tags if x in VALID_FRESHNESS_TAGS)
                if n_folder > 1:
                    file_errors.append(f"{n_folder} Folder tags - Article 7.1 allows exactly one")
                if n_role > 1:
                    file_errors.append(f"{n_role} File Role tags - Article 7.1 allows exactly one")
                if n_fresh > 1:
                    file_errors.append(f"{n_fresh} Freshness tags - Article 7.1 allows at most one")
                if bf and ft and bf in tags and ft in tags:
                    expected_order = ([bf, ft]
                                      + [x for x in tags if x in VALID_AI_SIGNAL_TAGS]
                                      + [x for x in tags if x in VALID_SENSITIVITY_TAGS]
                                      + [x for x in tags if x in VALID_FRESHNESS_TAGS])
                    if tags != expected_order and not (set(tags) - set(expected_order)):
                        file_errors.append(
                            f"tag order is {tags}; Article 7.1 canonical order is {expected_order}")
            else:
                # A malformed scalar (e.g. `tags: memory`) must fail loudly,
                # not silently skip the whole Article VII gate.
                file_errors.append(
                    f"tags is not a list (got {type(tags).__name__}: '{tags}') - "
                    "Article VII requires a tag array")
            # `policy` flag - required on every file (Section 8.1; REQUIRED_FIELDS
            # enforces presence) and must be boolean
            pol = fm.get("policy")
            if pol is not None and str(pol).lower() not in ("true", "false"):
                file_errors.append(f"policy must be true or false, got '{pol}'")
            # `readable` was removed from the schema in v14.00.00: it was a
            # constant (always true - only .md files can carry frontmatter)
            # that no command ever consumed. Same test that killed `ai-managed`.
            if "readable" in fm:
                file_errors.append("deprecated field: readable (removed in v14.00.00 - delete the line)")
            # Section 8.1: created/updated are ISO dates (YYYY-MM-DD).
            for dfield in ("created", "updated"):
                dval = str(fm.get(dfield, "") or "")
                if dval and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", dval):
                    file_errors.append(f"{dfield} is '{dval}' - must be YYYY-MM-DD (Section 8.1)")
            # Template files must never contain wikilinks (Article 3.7). They are
            # scaffolds, not knowledge-graph nodes. (Backups are not walked by
            # iter_md_files, so they are excluded separately.)
            if "Template" in path.parts or ".template" in path.parts:
                if text is not None and "[[" in text:
                    file_errors.append(
                        "wikilinks not allowed in Template files (Article 3.7)"
                    )
        # Constitution Article 9.1: no em dash (U+2014) anywhere in BRAIN. It is
        # a machine-writing tell; use a comma, colon, parentheses, or a hyphen.
        em_n = text.count(EM_DASH) if text is not None else 0
        if em_n:
            file_errors.append(
                f"{em_n} em dash(es) (U+2014) - banned vault-wide by Article 9.1; "
                "use a comma, colon, parentheses, or a hyphen"
            )
        r = rel(path)
        if file_errors:
            print(f"  ❌  {r}")
            for e in file_errors:
                print(f"       • {e}")
            errors.append(r)
        else:
            # Concise mode for agents: per-file OK lines only on a real terminal.
            # Failures always print. (Token economy: 50+ OK lines say one thing.)
            if sys.stdout.isatty():
                print(f"  ✅  {r}")
            passed += 1
    # Vault-level check (full runs only): the `startup` tag set must equal the
    # four files Section 9 names - "the tag and this checklist are kept in
    # agreement" is a stated invariant with no other enforcement.
    if not target_path:
        # v3 schema: ids must be unique across the vault (stable link targets).
        seen_ids = {}
        for path in iter_md_files():
            if not _toolkit_brain_doc(path):
                continue
            fm = parse_frontmatter(path)
            fid = fm.get("id", "") if fm else ""
            if not fid:
                continue
            if fid in seen_ids:
                print(f"  ❌  duplicate id: '{fid}' in {rel(path)} (also in {seen_ids[fid]})")
                errors.append(rel(path))
            else:
                seen_ids[fid] = rel(path)
        tagged = set()
        for path in iter_md_files():
            fm = parse_frontmatter(path)
            if fm and "startup" in fm.get("tags", []):
                tagged.add(rel(path))
        expected_startup = set(STARTUP_PATHS)
        if tagged != expected_startup:
            print()
            for x in sorted(tagged - expected_startup):
                print(f"  ❌  startup-set: {x} carries `startup` but is not in the Section 9 checklist")
                errors.append(x)
            for x in sorted(expected_startup - tagged):
                print(f"  ❌  startup-set: {x} is in the Section 9 checklist but lacks the `startup` tag")
                errors.append(x)
    else:
        # Single-file mode (the PostToolUse lint hook passes one path): the
        # full-vault duplicate-id and startup-set checks above are skipped, so
        # scope both to the target here - a per-file lint still catches this file
        # colliding with another id, or drifting from the Section 9 startup set.
        tr = rel(target_path)
        tfm = parse_frontmatter(target_path) if _toolkit_brain_doc(target_path) else None
        if tfm is not None:
            tid = str(tfm.get("id", "") or "")
            if tid:
                for other in iter_md_files():
                    if other.resolve() == target_path or not _toolkit_brain_doc(other):
                        continue
                    ofm = parse_frontmatter(other)
                    if ofm and str(ofm.get("id", "") or "") == tid:
                        print(f"  ❌  duplicate id: '{tid}' in {tr} (also in {rel(other)})")
                        if tr not in errors:
                            errors.append(tr)
                        break
            has_startup = "startup" in (tfm.get("tags", []) or [])
            in_set = tr in set(STARTUP_PATHS)
            if has_startup and not in_set:
                print(f"  ❌  startup-set: {tr} carries `startup` but is not in the Section 9 checklist")
                if tr not in errors:
                    errors.append(tr)
            elif in_set and not has_startup:
                print(f"  ❌  startup-set: {tr} is in the Section 9 checklist but lacks the `startup` tag")
                if tr not in errors:
                    errors.append(tr)
    print()
    print(divider())
    skip_note = f"  ⊘ {skipped} exempt" if skipped else ""
    # Unique files, not raw appends: a file failing both a per-file check and a
    # vault-level check (duplicate id, startup set) still counts once.
    bad_files = len(set(errors))
    print(f"  🏁  Done - ✅ {passed} passed  ❌ {bad_files} with errors{skip_note}")
    if errors:
        print(f"       Fix the errors above then re-run lint.")
    print(divider())
    return 1 if errors else 0


# ══════════════════════════════════════════════════════════
#  4 - Tokens
# ══════════════════════════════════════════════════════════

def cmd_tokens() -> int:
    """🪙 Estimate token cost by file, folder, and total across the BRAIN."""
    header("Token Estimates", "🪙")
    folder_totals: dict[str, int] = {}
    grand_total = 0
    rows = []
    for path in iter_md_files():
        t = count_tokens(path)
        grand_total += t
        parts = path.relative_to(BRAIN_DIR).parts
        folder = parts[0] if len(parts) > 1 else "root"
        folder_totals[folder] = folder_totals.get(folder, 0) + t
        rows.append((t, rel(path)))
    rows.sort(reverse=True)
    top = rows[:10]
    col = max(len(r) for _, r in top) if top else 52
    print(f"  Top 10 files by token count")
    print(f"  {'-'*col}  {'-'*8}")
    print(f"  {'File':<{col}}  {'Tokens':>8}")
    print(f"  {'-'*col}  {'-'*8}")
    for t, r in top:
        print(f"  {r:<{col}}  {t:>8,}")
    print()
    print(f"  {'-'*62}")
    print(f"  {'Folder Totals'}")
    print(f"  {'-'*62}")
    for folder, total in sorted(folder_totals.items(), key=lambda x: -x[1]):
        bar_len = int((total / grand_total) * 30) if grand_total else 0
        bar = "█" * bar_len
        print(f"  {folder:<20}  {total:>8,}  {bar}")
    print()
    print(divider())
    print(f"  🏁  Grand total: {grand_total:,} tokens  (~{grand_total//1000}k)")
    led = _read_json(LEDGER_FILE)
    if led:
        started = str(led.get("started", "?"))
        try:
            # The ledger stamps UTC; show it in local wall-clock time, 12-hour.
            dt = datetime.fromisoformat(started).astimezone()
            since = f"{dt.strftime('%Y-%m-%d')} {int(dt.strftime('%I'))}:{dt.strftime('%M %p')}"
        except ValueError:
            since = f"{started[:16]} UTC"
        print(f"       Session ledger: ~{led.get('tokens', 0):,} of {led.get('window', 200000)//1000}k "
              f"({led.get('model', 'claude')}) since {since}")
    print(f"       Based on ~{CHARS_PER_TOKEN} chars/token (Gemini / Claude approximation)")
    print(divider())
    return 0


# ══════════════════════════════════════════════════════════
#  5 - Stale
# ══════════════════════════════════════════════════════════

def _is_tier_summary(path: Path) -> bool:
    """True for tiered session summaries (Current/Recent) and archived summaries
    (Archive/). These are immutable history - old by design - so age and size
    checks never apply to them."""
    return ("Memory" in path.parts
            and (path.parent.name in ("Current", "Recent")
                 or "Archive" in path.parts))

def cmd_stale() -> int:
    """⏰ Flag outdated memory entries, non-timeless library files, and
    lifetime-hygiene issues (oversized memory files, unconsolidated Log, backup pile-up)."""
    header("Stale Content Scan", "⏰")
    today = datetime.now(timezone.utc).date()
    flagged = 0
    for path in iter_md_files():
        fm = parse_frontmatter(path) or {}
        folder = fm.get("folder", "")
        updated = fm.get("updated", "")
        r = rel(path)
        # Permanent Memory files larger than the size threshold (tier summaries
        # are immutable history and exempt; see Memory/Memory.md Growth Protocol)
        if folder == "memory" and not _is_tier_summary(path):
            t = count_tokens(path)
            if t > MEMORY_SHARD_WARN_TOKENS:
                print(f"  ⚠️   {r}")
                print(f"       Memory file is large ({t:,} tokens > {MEMORY_SHARD_WARN_TOKENS:,}) - "
                      f"see the Growth Protocol in Memory/Memory.md")
                flagged += 1
        # Memory files older than 90 days, EXCEPT permanent reference content.
        # The per-entry collections (People/Decisions), their index docs, and
        # Dates.md are reference data (type record/information/
        # index): normal to sit untouched for long stretches, so flagging them is
        # noise. Tier summaries are old by design. The age check therefore applies
        # only to staging-style memory (e.g. an un-promoted Log.md).
        is_perm_ref = fm.get("type", "") in ("record", "information", "index", "template")
        if (folder == "memory" and updated and not _is_tier_summary(path)
                and not is_perm_ref):
            try:
                d = datetime.fromisoformat(updated).date()
                age = (today - d).days
                if age > 90:
                    print(f"  ⚠️   {r}")
                    print(f"       Memory file not updated in {age} days (last: {updated})")
                    flagged += 1
            except ValueError:
                pass
        # Library content files must carry a freshness tag (Article 6.2:
        # timeless / enduring / current). Structural files (index, information,
        # template, log, record, agent) omit freshness per Article 6.2 / 7.6, so
        # they are not flagged; only content (e.g. reference) is. The Library
        # staff agents live at Library/ root and are structure, not holdings.
        if folder == "library":
            ftype = fm.get("type", "")
            tags = fm.get("tags", [])
            if (ftype not in ("index", "information", "template", "log", "record", "agent")
                    and isinstance(tags, list)
                    and not (set(tags) & VALID_FRESHNESS_TAGS)):
                print(f"  ⚠️   {r}")
                print(f"       Library content file has no freshness tag (timeless/enduring/current)")
                flagged += 1
        # Projects with no recent activity (> 180 days). Template scaffolds
        # (type: template) are blank blueprints, not activity-bearing project
        # files, so they are exempt like the memory and library checks above.
        if folder == "projects" and updated and fm.get("type", "") != "template":
            try:
                d = datetime.fromisoformat(updated).date()
                age = (today - d).days
                if age > 180:
                    print(f"  ⚠️   {r}")
                    print(f"       Project file inactive for {age} days (last: {updated})")
                    flagged += 1
            except ValueError:
                pass
    # Unconsolidated Log: too many entries waiting for the Memory Consolidation Loop
    log_path = BRAIN_DIR / "Memory" / "Log.md"
    try:
        entries = [l for l in log_path.read_text(encoding="utf-8").splitlines()
                   if l.startswith("### ") and "[Date]" not in l]
        if len(entries) > LOG_UNPROMOTED_WARN:
            print(f"  ⚠️   Memory/Log.md")
            print(f"       {len(entries)} log entries (> {LOG_UNPROMOTED_WARN}) - run the Memory "
                  f"Consolidation Loop (System/Workflows.md) to promote and prune")
            flagged += 1
    except OSError:
        pass
    # Backup pile-up: large backlog suggests cleared work that was never reviewed
    backups_dir = SYSTEM_DIR / ".backups"
    try:
        n_backups = sum(1 for f in backups_dir.iterdir()
                        if f.is_file() and not f.name.startswith("."))
        if n_backups > BACKUP_PILE_WARN:
            print(f"  ⚠️   System/.backups/")
            print(f"       {n_backups} backup files (> {BACKUP_PILE_WARN}) - review with the user "
                  f"and clear confirmed-done backups (Instructions Section 10.3)")
            flagged += 1
    except OSError:
        pass
    print()
    print(divider())
    if flagged:
        print(f"  🏁  {flagged} item(s) flagged for review.")
        print(f"       No changes made - review and update manually.")
    else:
        print(f"  🏁  All clear - no stale content found.")
    print(divider())
    return 1 if flagged else 0


# ══════════════════════════════════════════════════════════
#  6 - Diff
# ══════════════════════════════════════════════════════════

def cmd_diff() -> int:
    """📊 Show what changed since the index (manifest.json) was last built. Change is
    confirmed by SHA-256, not mtime, so a moved/synced/cloned vault never shows false
    changes. Read-only: run `manifest` (or `health`) to rebuild the index baseline."""
    header("BRAIN Diff", "📊")
    if not MANIFEST_FILE.exists():
        print("  No index found yet.")
        print("  Run `manifest` to build the first index, then diff after your next change.")
        print(divider())
        return 0
    idx = load_index()
    taken = idx.get("generated", "unknown")
    added, modified, deleted = index_drift()
    print(f"  Comparing the live tree to the index built: {taken}")
    print(f"  Changes confirmed by content hash (portable across syncs and clones).")
    print()
    if added:
        print(f"  ➕  Added ({len(added)})")
        for f in added:
            print(f"       {f}")
    if modified:
        print(f"\n  ✏️   Modified ({len(modified)})")
        for f in modified:
            print(f"       {f}")
    if deleted:
        print(f"\n  ➖  Deleted ({len(deleted)})")
        for f in deleted:
            print(f"       {f}")
    if not any([added, modified, deleted]):
        print(f"  No changes since the index was built - the live tree matches the index.")
    print()
    print(divider())
    n = len(added) + len(modified) + len(deleted)
    print(f"  🏁  +{len(added)} added  ~{len(modified)} modified  -{len(deleted)} deleted")
    if n:
        print(f"       Run `manifest` to rebuild the index and reset the baseline.")
    print(divider())
    # diff(1)/git convention: exit 1 when differences exist, so scripts and
    # agents can branch on $? without parsing output.
    return 1 if n else 0


# ══════════════════════════════════════════════════════════
#  7 - Search
# ══════════════════════════════════════════════════════════

def _search_ripgrep(query: str):
    """Return {relpath: [(lineno, text), ...]} via ripgrep, or None if rg is
    unavailable or errors (caller falls back to the pure-Python scan). ripgrep is
    dramatically faster on a large vault; it stays an optional accelerator, never a
    requirement. Backups and generated data are excluded to match the Python scope."""
    if shutil.which("rg") is None:
        return None
    try:
        # Exclusions mirror the Python fallback's iter_all_files scope exactly:
        # SKIP_DIRS (Backups, .obsidian, .trash, .git, __pycache__) plus the
        # hidden dirs the walk prunes (.backups, .claude). System/Data is NOT
        # excluded wholesale: the fallback yields its .md files (Data.md is
        # real), and the *.md include glob already drops its artifacts.
        result = subprocess.run(
            ["rg", "--line-number", "--ignore-case", "--fixed-strings",
             "--no-heading", "--color", "never", "--glob", "*.md",
             "--hidden",
             "--glob", "!**/.git/**", "--glob", "!**/.obsidian/**",
             "--glob", "!**/.trash/**", "--glob", "!**/.backups/**",
             "--glob", "!**/.claude/**", "--glob", "!**/Backups/**",
             "--glob", "!**/__pycache__/**",
             "--", query, str(BRAIN_DIR)],
            capture_output=True, text=True, timeout=30)
    except Exception as e:
        logging.getLogger("search").error("ripgrep failed: %s", e)
        return None
    if result.returncode not in (0, 1):   # 1 just means "no matches"
        return None
    hits: dict = {}
    for line in result.stdout.splitlines():
        parts = line.split(":", 2)
        if len(parts) < 3:
            continue
        fpath, lineno, text = parts
        try:
            r = rel(Path(fpath))
        except Exception:
            r = fpath
        hits.setdefault(r, []).append((int(lineno) if lineno.isdigit() else 0, text))
    return hits

def _search_python(query: str) -> dict:
    """Pure-Python fallback full-text scan (no dependencies)."""
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    hits: dict = {}
    for path in iter_md_files():
        try:
            lines = _read_text(path).splitlines()
        except OSError:
            continue
        ms = [(i + 1, line) for i, line in enumerate(lines) if pattern.search(line)]
        if ms:
            hits[rel(path)] = ms
    return hits

def cmd_search(query: str = "", folder_filter: str = "", type_filter: str = "") -> int:
    """🔎 Full-text search with optional frontmatter filtering. Uses ripgrep when it is
    installed (fast at scale) and falls back to a pure-Python scan when it is not."""
    if not query:
        if not sys.stdin.isatty():
            fail('Usage: search "term" [folder=<f>] [type=<t>]')
            return 1
        query = input("  Search query: ").strip()
    if not query:
        warn("No query provided.")
        return 1
    header(f"Search: '{query}'", "🔎")
    hits = _search_ripgrep(query)
    engine = "ripgrep" if hits is not None else "python"
    if hits is None:
        hits = _search_python(query)
    idx_map = _index_by_path(load_index())   # fast folder/type lookup; no re-parse
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    kws = _tokenize(query)   # query content words, for relevance scoring below
    results = []
    for r in sorted(hits):
        entry = idx_map.get("BRAIN/" + r)
        if entry is None:
            fm = parse_frontmatter(BRAIN_DIR / r) or {}
            folder, ftype, status = fm.get("folder", ""), fm.get("type", ""), fm.get("status", "")
        else:
            folder, ftype, status = entry.get("folder", ""), entry.get("type", ""), entry.get("status", "")
        if folder_filter and folder != folder_filter:
            continue
        if type_filter and ftype != type_filter:
            continue
        results.append((r, folder, ftype, sorted(hits[r]), entry, status))
    # Rank by relevance + recency, not filename. Cold-tier recall (Memory/Context/
    # Archive) is reached only through search, so an alphabetical dump buried the
    # one summary that answered the query. Score = frontmatter relevance
    # (_score_entry: title/tags/keywords/path/desc vs the query terms, already
    # recency-weighted when it hits) + body-hit count; recency is added explicitly
    # for body-only matches so a fresh hit with no title term still rises. This is
    # the recency+relevance scoring `load` already uses (generative-agents memory
    # ranking), now applied to the search path too. Stale files (status
    # deprecated/archived) always sort below live results - still shown, never
    # hidden (nothing is deleted) - then by score, then path for a stable order.
    def _search_rank(rec):
        _r, _folder, _ftype, _matches, _entry, _status = rec
        rel_score = _score_entry(_entry, kws, set()) if _entry else 0
        score = rel_score + len(_matches)
        if rel_score == 0 and _entry is not None:
            score += _recency_boost(_entry)
        return (1 if _is_stale_status(_status) else 0, -score, _r)
    results.sort(key=_search_rank)
    if not results:
        print(f"  No results for '{query}'.   (engine: {engine})")
        print()
        return 0
    # Bounded output: agents lose the thread stepping through huge result sets.
    # Show at most 50 files and say so, rather than dumping everything.
    SEARCH_FILE_CAP = 50
    overflow = len(results) - SEARCH_FILE_CAP
    if overflow > 0:
        print(f"  ⚠️   {len(results)} files matched - showing the first {SEARCH_FILE_CAP}.")
        print(f"       Narrow the query, or filter: search \"{query}\" folder=<f> type=<t>")
        print()
        results = results[:SEARCH_FILE_CAP]
    for r, folder, ftype, matches, entry, status in results:
        flag = f"   ⊘ {status}" if _is_stale_status(status) else ""
        print(f"  📄  {r}  [{folder} / {ftype}]{flag}")
        for lineno, line in matches[:3]:
            # Window ~100 chars around the first match so the matched term is
            # always visible - a flat [:100] cut hid matches past column 100.
            s = line.strip()
            m = pattern.search(s)
            if m:
                start = max(0, m.start() - 50)
                end = start + 100
                seg = ("…" if start > 0 else "") + s[start:end] + ("…" if end < len(s) else "")
            else:
                seg = s[:100]
            highlighted = pattern.sub(lambda mm: f"[{mm.group()}]", seg)
            print(f"       L{lineno}: {highlighted}")
        if len(matches) > 3:
            print(f"       … {len(matches)-3} more match(es)")
        print()
    print(divider())
    print(f"  🏁  {len(results)} file(s) matched '{query}'   ·   engine: {engine}")
    print(divider())
    return 0


# ══════════════════════════════════════════════════════════
#  8 - Load
# ══════════════════════════════════════════════════════════

# Keyword → folder mappings for smart routing
LOAD_ROUTES = {
    "identity": ["profile"],
    "who i am": ["profile"],
    "about me": ["profile"],
    "preference": ["profile"],
    "memory": ["memory"],
    "past session": ["memory"],
    "remember": ["memory"],
    "project": ["projects"],
    "task": ["projects"],
    "venture": ["ventures"],
    "company": ["ventures"],
    "business": ["ventures"],
    "client": ["ventures"],
    "library": ["library"],
    "reference": ["library"],
    "system": ["system"],
    "script": ["system"],
    "inbox": ["inbox"],
}

LOAD_STOPWORDS = {
    "the","a","an","to","for","of","and","or","in","on","at","by","with","my","me",
    "i","help","about","is","it","this","that","how","do","need","want","get","got",
    "make","please","can","you","what","why","when","new","working","work",
}

def _tokenize(text: str) -> set:
    """Lowercase content words from a task description (drops stopwords and short tokens)."""
    return {w for w in re.findall(r'[a-z0-9]+', text.lower())
            if len(w) > 2 and w not in LOAD_STOPWORDS}

def _recency_boost(entry: dict) -> int:
    """Small boost for recently updated files. In a personal vault, recency is one
    of the strongest relevance signals (fresher context usually matters more than
    older reference). Tiered, deterministic, and capped so it can rank among
    keyword matches but never outweigh a strong lexical match on its own."""
    updated = str(entry.get("updated", ""))
    try:
        d = datetime.fromisoformat(updated).date()
    except ValueError:
        return 0
    age = (datetime.now(timezone.utc).date() - d).days
    if age <= 30:  return 2
    if age <= 90:  return 1
    return 0

def _score_entry(entry: dict, kws: set, routed: set) -> int:
    """Lexical relevance of an index entry to the task. Title/tags/folder weigh most,
    then path, then description; routed-folder and recency add small boosts.
    Recency only applies to entries with at least one keyword hit, so an
    irrelevant-but-fresh file is never pulled in by recency alone."""
    # Strong-match surface: title + tags + aliases + keywords + folder. aliases
    # and keywords directly counter the vocabulary-mismatch weakness of keyword
    # ranking (a query term that isn't in the title still hits). Scoring is
    # binary per keyword (any-match below), so a long list can't inflate a score.
    strong = (entry.get("title", "") + " "
              + " ".join(_aslist(entry.get("tags", []))) + " "
              + " ".join(_aslist(entry.get("aliases", []))) + " "
              + " ".join(_aslist(entry.get("keywords", []))) + " "
              + entry.get("folder", "")).lower()
    path = entry.get("path", "").lower()
    desc = entry.get("description", "").lower()
    score = 0
    for kw in kws:
        # Plural-insensitive: "venture" matches "ventures" and vice versa.
        forms = {kw, kw + "s"} | ({kw[:-1]} if kw.endswith("s") and len(kw) > 3 else set())
        if any(f in strong for f in forms): score += 3
        if any(f in path for f in forms):   score += 2
        if any(f in desc for f in forms):   score += 1
    if score == 0:
        return 0
    if entry.get("folder") in routed:
        score += 2
    # Importance term (Memory/Memory.md): the 1-5 capture-time rating,
    # normalized (N/5 of a 3-point strong-hit weight, floored) so a pivotal
    # record outranks a routine one at equal lexical relevance, while
    # importance alone never outweighs a strong keyword match - and, like
    # recency, it never applies without at least one keyword hit.
    try:
        imp = int(entry.get("importance", 0) or 0)
    except (TypeError, ValueError):
        imp = 0
    if 1 <= imp <= 5:
        score += int(3 * imp / 5)
    return score + _recency_boost(entry)

def cmd_load(task: str = "", budget: str = "", json_out: bool = False) -> int:
    """📥 Return a ranked, token-budgeted file set for a task. The startup spine is
    always included; the rest are scored by relevance and added until the token budget is
    hit, so load stays lean even when a folder holds thousands of files. Reads from the
    index for speed. Override the budget: `load "task" 30000`. Pass --json for a
    machine-readable file list. Memory/Context/Archive/ is cold storage and never loads
    here (Instructions 14.2) - reach archived summaries via `search`. Files marked
    stale (status deprecated/archived) are skipped too: retained and searchable, but
    never auto-loaded into a task context (Instructions 8.1)."""
    if not task:
        # Never prompt in machine or piped contexts: --json callers and agents
        # have no TTY, and a bare input() here once crashed with EOFError and
        # polluted the error log (found live 2026-07-02).
        if json_out or not sys.stdin.isatty():
            if json_out:
                print(json.dumps({"error": "no task provided",
                                  "usage": 'load "task description" [budget] [--json]'}))
            else:
                fail('Usage: load "task description" [budget] [--json]')
            return 1
        task = input("  Describe the task: ").strip()
    if not task:
        warn("No task provided."); return 1
    try:
        budget_tokens = int(budget) if budget else LOAD_TOKEN_BUDGET
    except ValueError:
        budget_tokens = LOAD_TOKEN_BUDGET
    if not json_out:
        header(f"Context Load: '{task[:50]}'", "📥")
    kws = _tokenize(task)
    tl = task.lower()
    routed = {"root"}
    for k, fs in LOAD_ROUTES.items():
        if k in tl:
            routed.update(fs)

    index = load_index()
    md = [e for e in index.get("files", []) if e.get("kind") == "markdown"]
    if not md:   # no index yet - build one on the fly
        md = [e for e in build_index(incremental=True).get("files", []) if e.get("kind") == "markdown"]
    # Cold storage stays cold: archived summaries are search-only (Instructions 14.2).
    # The archive lives at Memory/Context/Archive/ (ARCHIVE_DIR); an earlier literal
    # here read Memory/Archive/ and silently matched nothing, so cold summaries were
    # loadable against the documented contract. Stale files (status deprecated/
    # archived) are skipped too - searchable, but never auto-loaded (Instructions 8.1).
    # .template/ scaffolds are blank blueprints, not task context - excluded here
    # like the catalog excludes them (a template surfaced in live load results
    # 2026-07-02); they remain reachable via search and read.
    md = [e for e in md
          if not e.get("path", "").startswith("BRAIN/Memory/Context/Archive/")
          and "/.template/" not in e.get("path", "")
          and not _is_stale_status(e.get("status"))]

    spine, scored = [], []
    for e in md:
        if "startup" in e.get("tags", []):
            spine.append(e)
        else:
            s = _score_entry(e, kws, routed)
            if s > 0:
                scored.append((s, e))
    spine.sort(key=lambda e: (_layer_num(e.get("layer")), e.get("path", "")))
    scored.sort(key=lambda se: (-se[0], _layer_num(se[1].get("layer")), -se[1].get("tokens", 0)))

    chosen, used, omitted = [], 0, 0
    for e in spine:
        chosen.append(("core", None, e)); used += e.get("tokens", 0)
    for s, e in scored:
        t = e.get("tokens", 0)
        if used + t <= budget_tokens:
            chosen.append(("rel", s, e)); used += t
        else:
            omitted += 1

    def _disp(p): return p[6:] if p.startswith("BRAIN/") else p

    if json_out:
        out = [{"path": _disp(e["path"]), "tokens": e.get("tokens", 0),
                "why": why, "score": s} for why, s, e in chosen]
        print(json.dumps({"task": task, "budget": budget_tokens,
                          "total_tokens": used, "omitted": omitted,
                          "files": out}, separators=(",", ":")))
        return 0

    print(f"  Task: {task}")
    print(f"  Keywords: {sorted(kws) or '(none parsed)'}")
    print(f"  Budget: {budget_tokens:,} tokens   ·   Routed folders: {sorted(routed)}")
    print()
    col = max((len(_disp(e['path'])) for _, _, e in chosen), default=40)
    print(f"  {'Why':<5} {'Score':>5}  {'File':<{col}}  {'Tokens':>8}")
    print(f"  {'-'*5} {'-'*5}  {'-'*col}  {'-'*8}")
    for why, s, e in chosen:
        print(f"  {why:<5} {('' if s is None else str(s)):>5}  {_disp(e['path']):<{col}}  {e.get('tokens',0):>8,}")
    print()
    spine_tokens = sum(e.get("tokens", 0) for e in spine)
    rel_tokens = used - spine_tokens
    print(divider())
    print(f"  🏁  {len(chosen)} files  •  {used:,} tokens total  "
          f"({len(spine)} core always-on: {spine_tokens:,}  +  {len(chosen)-len(spine)} relevant: {rel_tokens:,} / {budget_tokens:,} budget)")
    if omitted:
        print(f"       {omitted} relevant file(s) omitted to fit the {budget_tokens:,} budget - raise it, e.g. `load \"…\" {budget_tokens*2}`.")
    if spine_tokens > budget_tokens:
        print(f"       Note: the always-on core ({spine_tokens:,}) already exceeds your {budget_tokens:,} budget; the budget caps only the relevant tier.")
    print(f"       Read top-to-bottom: governance first, then by relevance.")
    print(divider())
    return 0


# ══════════════════════════════════════════════════════════
#  9 - Remember
# ══════════════════════════════════════════════════════════

BACKUP_KEEP = 5      # versions kept per source file (Section 10.1 rotation)


def _backup_dest_name(p: Path, ts: str) -> str:
    """Section 10.1 name: [folder]-[parent dirs]-[stem]-[timestamp].ext.
    Parent dirs (sanitized) disambiguate same-named files in different
    subfolders - Ventures/Acme/Log.md and Ventures/Bcorp/Log.md must never
    share a rotation group."""
    fm = parse_frontmatter(p) if p.suffix == ".md" else None
    base = (fm or {}).get("folder", "") or _top_folder(p)
    rel_parts = p.relative_to(BRAIN_DIR).parts
    mids = [re.sub(r"[^A-Za-z0-9]+", "-", x).strip("-")
            for x in rel_parts[1:-1]]
    mids = [m for m in mids if m]
    # Short path hash keeps the name injective: hyphen-flattening alone can
    # merge two distinct files into one rotation group (found 2026-07-03).
    h = hashlib.sha1("/".join(rel_parts).encode("utf-8")).hexdigest()[:6]
    return "-".join([base] + mids + [p.stem]) + f"-{h}-{ts}{p.suffix}"


def _backup_rotate(quiet: bool = False) -> int:
    """Keep the newest BACKUP_KEEP versions per source file; older versions are
    SOFT-removed to .trash/ (standing authorization, Constitution 3.1 - the
    two-level law holds: nothing is hard-deleted here). Returns count pruned."""
    groups = {}
    for f in _backup_dir_files():
        m = re.match(r"^(.*)-(\d{8}-\d{6})(\..+)$", f.name)
        if not m:
            continue
        groups.setdefault((m.group(1), m.group(3)), []).append((m.group(2), f))
    pruned = 0
    for (_stem, _ext), versions in groups.items():
        versions.sort()
        for _ts, f in versions[:-BACKUP_KEEP]:
            if _soft_remove(f) is not None:
                pruned += 1
                if not quiet:
                    print(f"    ♻️   {f.name} → .trash  (rotation: keeping newest {BACKUP_KEEP})")
    return pruned


def _backup_dir_files():
    d = SYSTEM_DIR / ".backups"
    return sorted(f for f in d.iterdir() if f.is_file()
                  and f.name not in (".gitkeep", ".DS_Store")) if d.exists() else []

def _backup_list() -> int:
    """List current snapshots in System/.backups/ (Section 10.3 review step)."""
    header("Backups", "💾")
    files = _backup_dir_files()
    if not files:
        print("  ✅  No backups - System/.backups/ is clear.")
        return 0
    total = sum(f.stat().st_size for f in files)
    for f in files:
        print(f"  💾  {f.name}  ({f.stat().st_size:,} B)")
    print()
    print(divider())
    print(f"  🏁  {len(files)} snapshot(s), {total:,} bytes. Clear with: backup clear --yes (after a green health).")
    print(divider())
    return 0

def _backup_clear() -> int:
    """Clear all snapshots (Section 10.3). Lint-gated: never clears while any
    file is broken, so no file loses its safety net mid-problem."""
    header("Clear Backups", "💾")
    files = _backup_dir_files()
    if not files:
        print("  ✅  Nothing to clear.")
        return 0
    print(f"  {len(files)} snapshot(s) will be SOFT-removed to .trash/ (two-level deletion, Constitution 3.1).")
    print("  Verifying the vault first (Section 10.3 pre-delete check)...\n")
    if cmd_lint() != 0:
        fail("Lint failed - not clearing backups while any file is broken.")
        return 1
    if not confirm(f"Soft-remove all {len(files)} backup(s) to .trash/? (yes/no): "):
        print("\n  🚫  Aborted.\n")
        return 0
    n = 0
    for f in files:
        if _soft_remove(f) is not None:
            n += 1
        else:
            fail(f"could not move {f.name} to .trash")
    print()
    print(divider())
    print(f"  🏁  {n} backup(s) soft-removed; .gitkeep retained. Hard-remove later with: trash empty")
    print(divider())
    return 0


# ── Backup mode: git-remote-backed vs local-only ──────────────────────────
#
# When this vault has a REACHABLE git remote, git history (local commits plus the
# remote) is the recovery net, so the local pre-edit snapshots in .backups/ and the
# two-stage .trash/ are redundant and are skipped. They are used only when NO remote
# is reachable - a local-only vault (e.g. iCloud with no hosting) where they are the
# sole safety net. Safe bias: any doubt (not a repo, no remote, probe fails) returns
# False, so the protections stay ON. Reachability is cached so a normal edit never
# pays a network round trip.
REMOTE_STATE = DATA_DIR / "remote-state.json"
REMOTE_TTL   = 600   # seconds; re-probe the remote at most this often

def _remote_backed(force: bool = False) -> bool:
    """True when a git remote is reachable, so .backups/ and .trash/ are skipped
    in favour of git history. False on any doubt (protections stay on)."""
    try:
        wt = run(["git", "-C", str(BRAIN_DIR), "rev-parse", "--is-inside-work-tree"], timeout=5)
        if wt.returncode != 0 or wt.stdout.strip() != "true":
            return False
        rem = run(["git", "-C", str(BRAIN_DIR), "remote"], timeout=5)
        if rem.returncode != 0 or not rem.stdout.strip():
            return False
    except (OSError, subprocess.SubprocessError):
        return False
    now = datetime.now(timezone.utc).timestamp()
    if not force:
        try:
            st = json.loads(REMOTE_STATE.read_text(encoding="utf-8"))
            if now - float(st.get("checked_at", 0)) < REMOTE_TTL:
                return bool(st.get("reachable", False))
        except (OSError, ValueError):
            pass
    reachable = False
    try:
        pr = run(["git", "-C", str(BRAIN_DIR), "ls-remote", "--exit-code", "-q", "origin"], timeout=10)
        reachable = (pr.returncode == 0)
    except (OSError, subprocess.SubprocessError):
        reachable = False
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        REMOTE_STATE.write_text(json.dumps({"checked_at": now, "reachable": reachable}),
                                encoding="utf-8")
    except OSError:
        pass
    return reachable

def _git_recoverable(p: Path) -> bool:
    """True when path p (file or dir) is git-tracked and has no uncommitted changes,
    so a `git rm` loses nothing - HEAD can always restore it. Decides whether a
    remote-mode deletion can go through git instead of the .trash/ safety net."""
    try:
        rp = str(p.resolve().relative_to(BRAIN_DIR.resolve()))
    except (OSError, ValueError):
        return False
    try:
        listed = run(["git", "-C", str(BRAIN_DIR), "ls-files", "--", rp], timeout=10)
        if listed.returncode != 0 or not listed.stdout.strip():
            return False   # nothing tracked here - git could not recover it
        status = run(["git", "-C", str(BRAIN_DIR), "status", "--porcelain", "--", rp], timeout=10)
        return status.returncode == 0 and status.stdout.strip() == ""
    except (OSError, subprocess.SubprocessError):
        return False


def cmd_backup(target: str = "", force_local: bool = False) -> int:
    """💾 Copy a file to System/.backups/ using the Section 10.1 naming
    convention ([folder]-[filename]-YYYYMMDD-HHMMSS.ext). This is the standard
    pre-edit step: `backup Memory/Log.md` before editing Memory/Log.md. In a
    remote-backed vault the snapshot is skipped (git history is the backstop);
    `backup <path> local` forces one anyway."""
    if target.strip().lower() == "list":
        return _backup_list()
    if target.strip().lower() == "clear":
        return _backup_clear()
    header("Backup File", "💾")
    if not target:
        # Never prompt without a TTY: piped/agent callers get usage, not a
        # hang-then-EOFError (found live 2026-07-02).
        if not sys.stdin.isatty():
            fail('Usage: backup "<BRAIN-relative path>"')
            return 1
        target = input("  File to back up (BRAIN-relative path): ").strip()
    if not target:
        warn("No file given."); return 1
    p = Path(target)
    if not p.is_absolute():
        p = BRAIN_DIR / target
    try:
        p = p.resolve()
        p.relative_to(BRAIN_DIR.resolve())
    except (OSError, ValueError) as e:
        logging.getLogger("backup").error("path resolution failed for %s: %s", target, e)
        fail(f"Not a file inside this BRAIN: {target}")
        return 1
    if not p.is_file():
        fail(f"File not found: {rel(p)}")
        return 1
    if {"Backups", ".backups"} & set(p.parts):
        fail("That file is already a backup - never back up or edit backups (Section 10.1).")
        return 1
    if _remote_backed() and not force_local:
        ok(f"{rel(p)}: remote-backed vault - git history is the pre-edit backstop; snapshot skipped.")
        print("     Commit to preserve this state. Force a local snapshot with: backup <path> local")
        return 0
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    dest_dir = SYSTEM_DIR / ".backups"
    dest = dest_dir / _backup_dest_name(p, ts)
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = _safe_dest(dest)
        shutil.copy2(str(p), str(dest))
    except OSError as e:
        fail(f"Backup failed: {e}")
        logging.getLogger("backup").error(e, exc_info=True)
        return 1
    ok(f"{rel(p)}  →  {rel(dest)}")
    _backup_rotate()
    print()
    print(divider())
    print(f"  🏁  Backed up verbatim. Safe to edit the original.")
    print(divider())
    return 0


# Memory/Log.md is engine-owned: these markers anchor where `remember` inserts
# entries and where the auto-derived Open Loops view is regenerated. They must
# match the strings in Memory/Log.md exactly.
LOG_ENTRIES_ANCHOR = "<!-- brain:log-entries -->"
LOG_OPENLOOPS_START = "<!-- brain:open-loops (auto-maintained by brain.command from entries marked Status: Open - do not edit by hand) -->"
LOG_OPENLOOPS_END = "<!-- /brain:open-loops -->"


def _log_entries_span(lines: list):
    """(start, end) line indices bounding the body of the '## Log Entries'
    section (heading exclusive, up to the next '## ' heading or EOF), or None."""
    h = next((i for i, l in enumerate(lines) if l.strip() == "## Log Entries"), None)
    if h is None:
        return None
    e = next((i for i in range(h + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return (h + 1, e)


def _sync_log_open_loops() -> int:
    """Regenerate Log.md's Open Loops block from every entry in the Log Entries
    section still marked `**Status:** Open`. The Log analogue of the tier/
    collection auto-lists: the view is derived, never hand-maintained. Returns 1
    if the block changed."""
    log_file = BRAIN_DIR / "Memory" / "Log.md"
    try:
        text = _read_text(log_file)
    except OSError:
        return 0
    lines = text.split("\n")
    span = _log_entries_span(lines)
    opens = []
    if span:
        s, e = span
        j = s
        while j < e:
            if lines[j].startswith("### "):
                k = j + 1
                while k < e and not lines[k].startswith("### "):
                    k += 1
                if re.search(r"(?im)^\s*\*\*Status:\*\*\s*Open\b", "\n".join(lines[j:k])):
                    m = re.match(r"###\s+(\S+)\s+-\s+(.+)", lines[j])
                    opens.append(((m.group(2).strip() if m else lines[j][4:].strip()),
                                  (m.group(1) if m else "")))
                j = k
            else:
                j += 1
    body = ("\n".join(f"- {t}  (opened {d})" for t, d in opens) if opens else "_No open loops._")
    return 1 if _sync_marker_block(log_file, LOG_OPENLOOPS_START,
                                   LOG_OPENLOOPS_END, body, "open loops") else 0


def _remember_add(log_file: Path, text: str, loop: bool) -> int:
    """Insert one entry into Log.md's Log Entries section (newest first), engine-
    formatted and timestamped. With loop=True it carries `**Status:** Open` and
    surfaces in the auto-derived Open Loops view."""
    rows = text.splitlines() if text else []
    if not rows or not rows[0].strip():
        warn("Nothing entered - no memory written."); return 0
    if not IMPORTANCE_RE.search(text):
        # Rate at capture (Memory/Memory.md): advisory, never blocking.
        warn("No 'Importance: N' line (1 routine to 5 pivotal) in the entry - "
             "rate importance at capture so retrieval can rank it.")
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    title = rows[0].strip().rstrip(".")[:80]
    body = "\n".join(rows[1:]).strip()
    entry = f"\n### {date_str} - {title}\n"
    if body:
        entry += f"\n{body}\n"
    if loop:
        entry += "\n**Status:** Open\n"
    try:
        content = log_file.read_text(encoding="utf-8")
    except OSError as e:
        fail(f"Could not read {rel(log_file)}: {e}"); return 1
    if LOG_ENTRIES_ANCHOR not in content:
        fail("Log Entries anchor missing - Memory/Log.md structure changed; refusing to guess."); return 1
    # Drop the placeholder on first entry - but only when it sits inside the
    # Log Entries section (between the anchor and the next heading), so the
    # same placeholder text anywhere else in the file is never touched.
    ph = "\n_No entries yet._\n"
    span_start = content.index(LOG_ENTRIES_ANCHOR) + len(LOG_ENTRIES_ANCHOR)
    next_head = re.search(r"(?m)^#{1,6}\s", content[span_start:])
    span_end = span_start + next_head.start() if next_head else len(content)
    ph_at = content.find(ph, span_start, span_end)
    if ph_at != -1:
        content = content[:ph_at] + "\n" + content[ph_at + len(ph):]
    content = content.replace(LOG_ENTRIES_ANCHOR, LOG_ENTRIES_ANCHOR + entry, 1)
    content, _ = _sub_frontmatter(content, r'^updated:\s*.*$', f'updated: {date_str}')
    try:
        _quiet_backup(log_file)
        _write_atomic(log_file, content)
    except OSError as e:
        fail(f"Could not write {rel(log_file)}: {e}"); return 1
    ok(f"Logged: {title}" + ("  (open loop)" if loop else ""))
    if loop and _sync_log_open_loops():
        print("       🔗  Open Loops view refreshed.")
    print(); print(divider()); print(f"  🏁  Memory written for {date_str}."); print(divider())
    return 0


def _remember_close(log_file: Path, match: str) -> int:
    """Flip the single matching open entry to `**Status:** Resolved (date)` and
    refresh the Open Loops view. Preserves the entry; never deletes."""
    if not match.strip():
        fail('Usage: remember close "text match"'); return 1
    try:
        lines = log_file.read_text(encoding="utf-8").split("\n")
    except OSError as e:
        fail(f"Could not read {rel(log_file)}: {e}"); return 1
    span = _log_entries_span(lines)
    if not span:
        fail("Log Entries section not found."); return 1
    s, e = span
    hits = []
    j = s
    while j < e:
        if lines[j].startswith("### "):
            k = j + 1
            while k < e and not lines[k].startswith("### "):
                k += 1
            status_idx = next((x for x in range(j, k)
                               if re.match(r"(?i)\s*\*\*Status:\*\*\s*Open\b", lines[x])), None)
            if status_idx is not None and match.lower() in "\n".join(lines[j:k]).lower():
                hits.append((re.sub(r"^\S+\s+-\s+", "", lines[j][4:].strip()), status_idx))
            j = k
        else:
            j += 1
    if not hits:
        fail(f"No open loop matches '{match}'."); return 1
    if len(hits) > 1:
        fail(f"'{match}' matches {len(hits)} open loops - be more specific:")
        for t, _ in hits:
            print(f"       - {t}")
        return 1
    title, idx = hits[0]
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines[idx] = re.sub(r"(?i)\*\*Status:\*\*\s*Open\b", f"**Status:** Resolved ({date_str})", lines[idx])
    content, _ = _sub_frontmatter("\n".join(lines), r'^updated:\s*.*$', f'updated: {date_str}')
    try:
        _quiet_backup(log_file)
        _write_atomic(log_file, content)
    except OSError as e:
        fail(f"Could not write {rel(log_file)}: {e}"); return 1
    ok(f"Closed open loop: {title}")
    if _sync_log_open_loops():
        print("       🔗  Open Loops view refreshed.")
    print(); print(divider()); print("  🏁  Loop closed - record preserved."); print(divider())
    return 0


def _remember_route(log_file: Path, parts: list) -> int:
    """Append a row to Log.md's Sort Routing Notes table (engine-formatted)."""
    if len(parts) < 3 or not parts[0].strip() or not parts[2].strip():
        fail('Usage: remember route "<file>" "<destination>" "<why>"'); return 1
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if not _append_table_row(log_file, [date_str, parts[0].strip(), parts[1].strip(), parts[2].strip()],
                             after_heading="Sort Routing Notes"):
        fail("Could not append a routing note (Sort Routing Notes table not found)."); return 1
    ok(f"Routing note logged: {parts[0].strip()} -> {parts[1].strip()}")
    print(); print(divider()); print("  🏁  Routing rationale recorded."); print(divider())
    return 0


def cmd_remember(args=None) -> int:
    """🧠 Write to the engine-owned Memory/Log.md. The AI never hand-edits the Log.
      remember "Title: detail"            append a note (newest first)
      remember "Title: detail" --loop     append an open loop (shows in Open Loops)
      remember close "text match"         resolve the matching open loop
      remember route "<file>" "<dest>" "<why>"   log an Inbox routing rationale
    Rate importance at capture (Memory/Memory.md): include an "Importance: N"
    line in the body, 1 routine to 5 pivotal."""
    args = args or []
    header("Session Memory Writer", "🧠")
    log_file = BRAIN_DIR / "Memory" / "Log.md"
    if not log_file.exists():
        fail(f"Memory/Log.md not found at {log_file}"); return 1
    sub = args[0].lower() if args else ""
    if sub == "close":
        return _remember_close(log_file, args[1] if len(args) > 1 else "")
    if sub == "route":
        return _remember_route(log_file, list(args[1:]))
    loop = "--loop" in args
    textargs = [a for a in args if a != "--loop"]
    if textargs:
        text = textargs[0]
    else:
        print("  Enter what should be remembered. Type END on a new line when done.\n")
        buf = []
        while True:
            try:
                line = input("  > ")
            except EOFError:
                break
            if line.strip().upper() == "END":
                break
            buf.append(line)
        text = "\n".join(buf)
    return _remember_add(log_file, text, loop)


# ══════════════════════════════════════════════════════════
#  Friction ledger - the BRAIN-wide operating-failure signal
# ══════════════════════════════════════════════════════════
#  reports.log records what ran; friction.jsonl records what went WRONG with how
#  the BRAIN operates - a correction, a forgotten step, a skill that mis-fired, a
#  rule that proved ambiguous. It is the signal the reflection loop reads (the
#  per-skill analog is each skill's regression-cases.jsonl). Append-only JSONL,
#  one event per line; the AI captures the moment friction happens. Nothing here
#  edits a vault file - the ledger lives in System/Data/ with the engine's
#  other generated artifacts, exempt from the index and the backup protocol.

FRICTION_KINDS = ("correction", "repeated-mistake", "skill-misfire",
                  "rule-ambiguity", "near-miss", "other")
FRICTION_SEVERITIES = ("low", "med", "high")

def _friction_append(kind: str, what: str, target: str, severity: str) -> int:
    # One UTC clock for both fields: a local-time date next to a UTC ts drifted
    # apart across midnight, putting one event in two different days.
    now = datetime.now(timezone.utc)
    rec = {
        "date": now.strftime("%Y-%m-%d"),
        "ts": now.isoformat(timespec="seconds"),
        "kind": kind,
        "what": what,
        "target": target,
        "severity": severity,
    }
    try:
        FRICTION_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(FRICTION_FILE, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception as exc:
        fail(f"Could not write friction.jsonl: {exc}")
        return 1
    ok(f"Logged friction  [{kind} / {severity}]")
    print(f"      {what[:88]}")
    if target:
        print(f"      target: {target}")
    print(f"\n      Ledger: {FRICTION_FILE.relative_to(BRAIN_DIR)}")
    print(f"      Review it any time with `friction list`; the reflection loop reads it.")
    return 0

def _friction_list(n: int) -> int:
    if not FRICTION_FILE.exists():
        print("  No friction logged yet - the ledger is created on first capture.")
        print(f"      Path (created on demand): {FRICTION_FILE.relative_to(BRAIN_DIR)}")
        return 0
    lines = [l for l in FRICTION_FILE.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not lines:
        print("  friction.jsonl is empty.")
        return 0
    shown = lines[-n:]
    print(f"  {len(lines)} event(s) logged; showing the most recent {len(shown)}:\n")
    for l in shown:
        try:
            r = json.loads(l)
        except Exception:
            print("      ⚠️   (unparseable line skipped)")
            continue
        tgt = f"   →{r.get('target')}" if r.get("target") else ""
        print(f"      {r.get('date','')}  [{r.get('kind','?')}/{r.get('severity','')}]  {r.get('what','')[:78]}{tgt}")
    print(f"\n      Ledger: {FRICTION_FILE.relative_to(BRAIN_DIR)}")
    return 0

def cmd_friction(args=None) -> int:
    """🪵 Append one operating-friction event to System/Data/friction.jsonl -
    the BRAIN-wide failure signal the reflection loop reads (reports.log is the
    success-side companion; each skill's regression-cases.jsonl is the per-skill
    analog). Call it the moment the user corrects you, a step is missed, a skill
    mis-fires, or a rule proves ambiguous. `list` is a read-only review; nothing
    here ever edits a vault file.
      friction "kind: what happened"                    log an event
      friction "kind: what" --target "<file>" --severity <low|med|high>
      friction list [N]                                 show the most recent N (default 10)
    Kinds: correction, repeated-mistake, skill-misfire, rule-ambiguity, near-miss, other."""
    args = list(args or [])
    header("Friction Ledger", "🪵")
    if args and args[0].lower() == "list":
        n = int(args[1]) if len(args) > 1 and args[1].isdigit() else 10
        return _friction_list(n)
    # Pull optional flags out of the argument list; the remainder is the text.
    target, severity, rest, i = "", "med", [], 0
    while i < len(args):
        a = args[i]
        if a == "--target" and i + 1 < len(args):
            target = args[i + 1]; i += 2; continue
        if a == "--severity" and i + 1 < len(args):
            severity = args[i + 1].lower(); i += 2; continue
        rest.append(a); i += 1
    text = rest[0].strip() if rest else ""
    if not text:
        print("  Describe the friction as \"kind: what happened\". Type END on a new line when done.\n")
        buf = []
        while True:
            try:
                line = input("  > ")
            except EOFError:
                break
            if line.strip().upper() == "END":
                break
            buf.append(line)
        text = "\n".join(buf).strip()
    if not text:
        fail("Nothing to log."); return 1
    # Split a leading "kind:" prefix only when it names a known kind; otherwise
    # the whole string is the description and the kind falls back to 'other'.
    kind = "other"
    if ":" in text:
        head, tail = text.split(":", 1)
        cand = head.strip().lower().replace(" ", "-")
        if cand in FRICTION_KINDS:
            kind, text = cand, tail.strip()
    if severity not in FRICTION_SEVERITIES:
        warn(f"--severity '{severity}' is not valid ({' | '.join(FRICTION_SEVERITIES)}) - using 'med'.")
        severity = "med"
    return _friction_append(kind, text, target, severity)


# ══════════════════════════════════════════════════════════
#  14 - New (scaffold project or venture)
# ══════════════════════════════════════════════════════════

def _copy_template(src: Path, dst: Path, replacements: dict) -> list[str]:
    """Recursively copy src → dst, applying frontmatter replacements. Returns list of created paths."""
    import shutil as _shutil
    created = []
    for item in src.rglob("*"):
        # Skip hidden files (e.g. .DS_Store) - check relative path parts only
        rel_item = item.relative_to(src)
        if any(part.startswith(".") for part in rel_item.parts):
            continue
        target = dst / rel_item
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif item.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            if item.suffix == ".md":
                try:
                    content = item.read_text(encoding="utf-8")
                    for old, new in replacements.items():
                        content = content.replace(old, new)
                    target.write_text(content, encoding="utf-8")
                except UnicodeDecodeError:
                    # File has .md extension but is not valid UTF-8 - copy as binary
                    _shutil.copy2(str(item), str(target))
            else:
                _shutil.copy2(str(item), str(target))
            created.append(str(target))
    return created


def cmd_new(kind_arg: str = "", name_arg: str = "") -> int:
    """🆕 Scaffold a new project or venture from its Template/ folder.
    Non-interactive form: `new project "Personal Site" --yes` or `new venture "Acme Corp" --yes`."""
    header("Create New Project or Venture", "🆕")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Choose type - from the argument when given, otherwise interactively
    if kind_arg:
        kind = kind_arg.strip().lower()
        if kind not in ("project", "venture"):
            fail(f"Unknown kind '{kind_arg}' - use 'project' or 'venture'.")
            return 1
    else:
        print("  What would you like to create?")
        print("  1.  Project  (Projects/[name]/)")
        print("  2.  Venture  (Ventures/[name]/)")
        print()
        kind_choice = input("  Choose (1 or 2): ").strip()
        if kind_choice == "1":
            kind = "project"
        elif kind_choice == "2":
            kind = "venture"
        else:
            print("\n  🚫  Aborted.\n"); return 0

    # Get name - from the argument when given
    if name_arg:
        raw_name = name_arg.strip()
    else:
        if not sys.stdin.isatty():
            fail(f'Usage: new {kind} "Name" [--yes]')
            return 1
        print()
        raw_name = input("  Name (e.g. 'Personal Site' or 'Acme Corp'): ").strip()
    if not raw_name:
        print("\n  🚫  No name provided. Aborted.\n"); return 0
    # Validate before touching the filesystem: letters, digits, spaces, hyphens,
    # plus & ( ) ' . which the vault's own folders use (Article 2.6 still bans
    # underscores, path separators, and other special characters).
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 \-&()'.]*", raw_name):
        fail(f"Invalid name '{raw_name}' - use letters, digits, spaces, hyphens, & ( ) ' . only.")
        return 1
    # Convert to hyphenated folder name, preserving the caller's casing
    # (e.g. "Acme Corp" → "Acme-Corp", "iOS App" → "iOS-App")
    folder_name = "-".join(raw_name.split())

    if kind == "project":
        template_dir = BRAIN_DIR / "Projects" / ".template"
        if not template_dir.exists():
            template_dir = BRAIN_DIR / "Projects" / "Template"
        dest_dir     = BRAIN_DIR / "Projects" / folder_name
        folder = "projects"
        placeholder  = "[Project-Name]"
    else:
        template_dir = BRAIN_DIR / "Ventures" / ".template"
        if not template_dir.exists():
            template_dir = BRAIN_DIR / "Ventures" / "Template"
        dest_dir     = BRAIN_DIR / "Ventures" / folder_name
        folder = "ventures"
        placeholder  = "[Company]"

    if not template_dir.exists():
        fail(f"Template not found: {template_dir}"); return 1
    if dest_dir.exists():
        fail(f"Already exists: {rel(dest_dir)}"); return 1

    print()
    print(f"  Creating: BRAIN/{folder.capitalize()}/{folder_name}/")
    if not confirm("Proceed? (yes/no): "):
        print("\n  🚫  Aborted.\n"); return 0

    # Frontmatter replacements: placeholder paths → real paths. Titles are
    # handled first (dict order is application order) so they receive the raw
    # human name; everything else (paths, links) gets the hyphenated folder
    # name. The project templates spell the placeholder "[Project Name]" in
    # titles, hence the space variant. Dates are stamped after the copy via
    # _sub_frontmatter, not by exact-string matching here.
    human_placeholder = placeholder.replace("-", " ")
    replacements = {
        f"BRAIN/Projects/{placeholder}/": f"BRAIN/Projects/{folder_name}/",
        f"BRAIN/Ventures/{placeholder}/": f"BRAIN/Ventures/{folder_name}/",
        f'title: "{human_placeholder}': f'title: "{raw_name}',
        f'title: "{placeholder}': f'title: "{raw_name}',
        placeholder: folder_name,
    }

    step(1, 2, f"Copying template to {folder_name}/...")
    try:
        created = _copy_template(template_dir, dest_dir, replacements)
        ok(f"Created {len(created)} file(s).")
        for c in created:
            p = Path(c)
            print(f"       📄  {p.relative_to(BRAIN_DIR)}")
    except Exception as e:
        fail(f"Failed to copy template: {e}")
        logging.getLogger("new").error(e, exc_info=True)
        return 1

    # Each scaffolded file needs a fresh, unique id - the template's id must
    # never be cloned across instances (it would collide vault-wide). The same
    # pass stamps created/updated with today's date through _sub_frontmatter
    # (frontmatter-only, any template value) - the old literal replacement
    # keyed on one exact quoted string and silently missed the templates.
    taken = _all_ids()
    for c in created:
        p = Path(c)
        if p.suffix != ".md":
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except OSError:
            continue
        dirty = False
        if re.search(r'(?m)^id:\s*.*$', t):
            new_id = _gen_id(p, taken)
            taken.add(new_id)
            t = re.sub(r'(?m)^id:\s*.*$', f'id: "{new_id}"', t, count=1)
            dirty = True
        t, n_created = _sub_frontmatter(t, r"^created:\s*.*$", f"created: {today}")
        t, n_updated = _sub_frontmatter(t, r"^updated:\s*.*$", f"updated: {today}")
        if dirty or n_created or n_updated:
            try:
                _write_atomic(p, t)
            except OSError:
                pass

    step(2, 2, "Syncing Finder tags for new files...")
    synced = 0
    for c in created:
        p = Path(c)
        if p.suffix == ".md":
            fm = parse_frontmatter(p) or {}
            tags = fm.get("tags", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",") if t.strip()]
            if tags and _set_macos_tags(p, tags):
                synced += 1
    ok(f"Tags synced for {synced} file(s).")

    # Fresh scaffolds must pass `gitkeep check`: the template's .gitkeep files
    # are hidden, so _copy_template skips them and empty folders arrive bare.
    # Run the same fix pass the gitkeep command uses.
    g_missing, _g_stale = _gitkeep_scan(fix=True)
    if g_missing:
        ok(f"Added .gitkeep to {len(g_missing)} empty folder(s).")

    print()
    print(divider())
    print(f"  🏁  Done - {folder_name}/ is ready.")
    print(f"       Path: BRAIN/{folder.capitalize()}/{folder_name}/")
    print(f"       It is cataloged automatically (brain.command db); keep "
          f"{folder_name}/Overview.md status current as work progresses.")
    print(divider())
    return 0


# ══════════════════════════════════════════════════════════
#  16 - Health (lint + stale + diff in one pass)
# ══════════════════════════════════════════════════════════

def _health_index() -> int:
    """Report index drift since the last build, then refresh the index so it is never
    silently stale. Returns 0 normally (drift is informational), 1 only on write failure."""
    if not MANIFEST_FILE.exists():
        print("  No index yet - building the first one now.")
    else:
        a, m, d = index_drift()
        n = len(a) + len(m) + len(d)
        if n == 0:
            print("  ✅  Index is fresh - the live tree matches manifest.json.")
        else:
            print(f"  ↻  {n} change(s) since last build:  +{len(a)} ~{len(m)} -{len(d)}")
            for f in a: print(f"       ➕  {f}")
            for f in m: print(f"       ✏️   {f}")
            for f in d: print(f"       ➖  {f}")
    idx = build_index(incremental=True)
    if not save_index(idx):
        fail(f"Could not refresh index - see {LOG_FILE}")
        return 1
    print(f"  💾  Index refreshed: {idx['file_count']} md + {idx['binary_count']} binary, "
          f"{idx['total_tokens']:,} tokens (schema v{idx['schema_version']}).")
    print(f"  💾  Catalog refreshed: {len(_content_md_entries(idx))} content record(s) "
          f"in catalog.ndjson (templates + binaries excluded).")
    return 0


def _health_errors() -> int:
    """Surface recorded errors from the shared error log (System/Data/errors.log).
    Every BRAIN script writes there, and health is where those entries become visible
    (see System/System.md). Returns 1 (warning) when entries exist, 0 when clean."""
    if not LOG_FILE.exists() or LOG_FILE.stat().st_size == 0:
        print("  ✅  Error log is clean - no recorded errors.")
        return 0
    try:
        lines = [l for l in LOG_FILE.read_text(encoding="utf-8").splitlines() if l.strip()]
    except OSError as e:
        fail(f"Could not read {LOG_FILE}: {e}")
        return 1
    if not lines:
        print("  ✅  Error log is clean - no recorded errors.")
        return 0
    n = len(lines)
    print(f"  ⚠️   {n} entr{'y' if n == 1 else 'ies'} in {rel(LOG_FILE)} (newest last):")
    for l in lines[-5:]:
        print(f"       {l[:110]}")
    if n > 5:
        print(f"       … {n - 5} older entr{'y' if n - 5 == 1 else 'ies'} not shown")
    print("       Review the entries; clear the log once their causes are resolved.")
    return 1


def _health_scaffolding() -> int:
    """Verify the Claude Code harness scaffolding that re-injects the BRAIN's rules
    is present and wired: the two reminder hook files plus their references in
    .claude/settings.json. That scaffolding is honor-system support - it reminds the
    AI of the rules at session start and on every prompt - and nothing else notices
    if it rots, so health asserts it. Skipped when .claude/ is absent: the BRAIN is
    portable and may run without the Claude Code harness (Constitution 2.5), the same
    way the macOS-only xattr mandate is skipped off-Mac. Returns 1 (warning) only when
    the harness exists but a piece is missing or broken."""
    claude_dir = BRAIN_DIR / ".claude"
    if not claude_dir.is_dir():
        print("  ⊘  No .claude/ here - Claude Code harness not in use on this host (skipped).")
        return 0
    problems = []
    settings = claude_dir / "settings.json"
    settings_text = ""
    settings_obj = None
    if not settings.is_file():
        problems.append("missing .claude/settings.json")
    else:
        try:
            settings_text = settings.read_text(encoding="utf-8")
            settings_obj = json.loads(settings_text)
        except (OSError, ValueError) as e:
            problems.append(f".claude/settings.json is unreadable or invalid JSON ({type(e).__name__})")
            settings_text = ""
    # The two reminder files the hooks inject (skill-router on session start,
    # prompt-reminder on every prompt) must exist, be non-empty, and be wired.
    for fname in ("skill-router.md", "prompt-reminder.md"):
        f = claude_dir / "hooks" / fname
        if not f.is_file():
            problems.append(f"missing .claude/hooks/{fname}")
            continue
        try:
            empty = not f.read_text(encoding="utf-8").strip()
        except OSError:
            empty = False
        if empty:
            problems.append(f".claude/hooks/{fname} is empty")
        elif settings_text and fname not in settings_text:
            problems.append(f".claude/hooks/{fname} exists but is not referenced in settings.json")
    # The session-start context loader must be wired (the bundle the AI reads first).
    if settings_text and "startup" not in settings_text:
        problems.append("settings.json does not wire `brain.command startup` on session start")
    # The write-time and end-of-turn safety hooks must stay wired, or they rot as
    # silently as the scaffolding they were added to defend. Inspect the parsed
    # config: a PostToolUse hook running `brain.command lint`, and a Stop hook.
    if settings_obj is not None:
        hk = settings_obj.get("hooks", {}) if isinstance(settings_obj, dict) else {}
        def _hook_cmds(event):
            cmds = []
            for grp in hk.get(event, []) or []:
                for h in (grp.get("hooks", []) or []):
                    cmds.append(str(h.get("command", "")))
            return cmds
        if not any("lint" in c for c in _hook_cmds("PostToolUse")):
            problems.append("no PostToolUse hook runs `brain.command lint` (write-time lint guard missing)")
        if not hk.get("Stop"):
            problems.append("no Stop hook wired (the health/Memory checkpoint reminder is missing)")
    if problems:
        print(f"  ⚠️   Harness scaffolding has {len(problems)} issue(s):")
        for p in problems:
            print(f"       • {p}")
        print("       The rule-reinjection scaffolding is degraded - repair via the update-config skill.")
        return 1
    print("  ✅  Harness scaffolding intact - reminder hooks present and wired.")
    return 0


def _health_version_drift() -> int:
    """Flag core/contract files whose content changed but whose `version` did
    not move - a bump is owed. Advisory: returns 1 as a warning, never
    auto-bumps (you classify the segment and run `bump`). The baseline is
    `version_sha` (the content hash from when the version last moved), carried
    in the index across refreshes, so an owed bump keeps flagging on every run
    until it is paid rather than being absorbed by the next index rebuild."""
    idx = _index_by_path(load_index())
    if not idx:
        print("  No index yet - run manifest, then re-check.")
        return 0
    owed = []
    for path in iter_md_files():
        if not _toolkit_brain_doc(path):
            continue
        fm = parse_frontmatter(path)
        if not fm or not _is_core_file(path):
            continue
        cached = idx.get("BRAIN/" + rel(path))
        if not cached:
            continue
        try:
            live = _sha256(path)
        except OSError:
            continue
        base = cached.get("version_sha") or cached.get("sha256")
        if live != base and \
                str(fm.get("version", "")) == str(cached.get("version", "")):
            owed.append(rel(path))
    if not owed:
        print("  ✅  No version drift - core files match their last bumped version.")
        return 0
    print(f"  ⚠️   {len(owed)} core file(s) changed since last index without a version bump:")
    for f in owed:
        print(f'       ⬆️   {f}  (classify, then: bump "{f}" <major|minor|patch>)')
    print("       Then run manifest to refresh the index.")
    return 1


def _health_anchors() -> int:
    """Assert every engine-owned anchor resolves: the fixed headings, marker
    pairs, and table headers that engine writers target blind (date tables,
    log anchors, tier/collection auto-blocks, the changelog's version line and
    sections). A missing anchor turns a later write into a warned no-op, so
    health names each miss by anchor and file. Returns 1 (warning) on any."""
    missing = []

    def _need(cond, name: str, doc: Path):
        if not cond:
            missing.append((name, rel(doc)))

    def _text_of(doc: Path) -> str:
        try:
            return _read_text(doc)
        except OSError:
            return ""

    # Memory/Dates.md: each DATE_SECTIONS heading, each with a table whose
    # header row carries the expected 3 columns (When/Date, Event/Milestone, Notes).
    dates = BRAIN_DIR / "Memory" / "Dates.md"
    dtext = _text_of(dates)
    for sec in sorted(set(DATE_SECTIONS.values())):
        m = re.search(rf"(?m)^##\s+{re.escape(sec)}\s*$", dtext)
        _need(m, f"`## {sec}` heading", dates)
        if m:
            tail = dtext[m.end():]
            nxt = re.search(r"(?m)^##\s+", tail)
            seg = tail[:nxt.start()] if nxt else tail
            hdr = re.search(r"(?m)^\|(.+)\|\s*$", seg)
            cols = len(hdr.group(1).split("|")) if hdr else 0
            _need(cols == 3,
                  f"3-column table header under `## {sec}` (found {cols})", dates)
    # Memory/Log.md: the entries anchor, the open-loops marker pair, and the
    # Sort Routing Notes heading (the routing-table writer's target).
    log = BRAIN_DIR / "Memory" / "Log.md"
    ltext = _text_of(log)
    _need(LOG_ENTRIES_ANCHOR in ltext, "log-entries anchor", log)
    _need(LOG_OPENLOOPS_START in ltext and LOG_OPENLOOPS_END in ltext,
          "open-loops marker pair", log)
    _need(re.search(r"(?m)^##\s+Sort Routing Notes\s*$", ltext),
          "`## Sort Routing Notes` heading", log)
    # Tier docs and Memory collection index docs: their auto-block markers.
    for name, _cap, path in MEMORY_TIERS:
        doc = path / f"{name}.md"
        t = _text_of(doc)
        _need(TIER_LINKS_START in t and TIER_LINKS_END in t,
              "tier-summaries marker pair", doc)
    for cname, mfolder, _kind, _ph in MEMORY_COLLECTIONS:
        doc = mfolder / f"{cname}.md"
        t = _text_of(doc)
        _need(COLLECTION_LINKS_START in t and COLLECTION_LINKS_END in t,
              "collection-entries marker pair", doc)
    # System/changelog.md: the Current Version line and all three sections.
    clog = BRAIN_DIR / "System" / "changelog.md"
    ctext = _text_of(clog)
    _need(re.search(r"\*\*`\d{2}\.\d{2}\.\d{2}`\*\*", ctext),
          "Current Version line", clog)
    for hdr_line in _CHANGELOG_SECTIONS.values():
        _need(re.search(rf"(?m)^{re.escape(hdr_line)}\s*$", ctext),
              f"`{hdr_line}` heading", clog)

    if not missing:
        print("  ✅  All engine-owned anchors resolve (dates, log, tiers, collections, changelog).")
        return 0
    print(f"  ⚠️   {len(missing)} engine-owned anchor(s) missing:")
    for name, docrel in missing:
        print(f"       ⚓  {docrel}: {name}")
    print("       Engine writers target these blind - restore the heading or markers.")
    return 1


# ══════════════════════════════════════════════════════════
#  Secret / PII scan - keep values out of a git-hosted vault
# ══════════════════════════════════════════════════════════
#
# The vault's standing rule is "secrets are pointers, not values" (System/System.md).
# Nothing machine-enforced it: the lint checks frontmatter shape, not content, and
# the vault now lives on a private GitHub remote. This scanner gives the rule teeth.
# `health` surfaces matches as a warning; the pre-push hook (install-hooks) blocks a
# push that would ship one. It favours high-confidence patterns over breadth so it
# does not cry wolf, and honours an inline allowlist marker for reviewed exceptions.

SECRET_ALLOW_MARKER = "brain-allow-secret"   # put this in a line's comment to skip it
SECRET_SCAN_SUFFIXES = (".md", ".txt", ".py", ".sh", ".command", ".json",
                        ".ndjson", ".yaml", ".yml", ".env", ".cfg", ".ini", ".toml")
# The scanner file legitimately contains these patterns as source; never scan it.
SECRET_SCAN_SKIP = {"brain.command"}

SECRET_PATTERNS = [
    ("AWS access key id",       re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("AWS secret access key",   re.compile(r"(?i)aws.{0,20}secret.{0,20}[=:]\s*['\"]?[A-Za-z0-9/+=]{40}\b")),
    ("GitHub token",            re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,255}\b")),
    ("GitHub fine-grained PAT", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{60,255}\b")),
    ("Slack token",             re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("Google API key",          re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("OpenAI / Anthropic key",  re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_\-]{20,}\b")),
    ("Stripe live key",         re.compile(r"\b[sr]k_live_[0-9a-zA-Z]{20,}\b")),
    ("Private key block",       re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("JSON Web Token",          re.compile(r"\beyJ[A-Za-z0-9_\-]{8,}\.eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\b")),
    ("Assigned secret literal", re.compile(r"(?i)\b(?:api[_-]?key|secret|password|passwd|client[_-]?secret|access[_-]?token|auth[_-]?token)\b\s*[=:]\s*['\"][^'\"\s]{12,}['\"]")),
    ("US Social Security no.",  re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
]
# Card numbers only: must open with a real issuer digit (Amex 3, Visa 4, MC 5,
# Discover 6). This excludes the year-leading timestamps and ids that a blank
# 13-to-19 digit rule flagged (e.g. a backup stamp 20260619-143155).
_CC_RE = re.compile(r"\b[3-6]\d{12,18}\b")

def _luhn_ok(s: str) -> bool:
    """Luhn check-digit test - gates the credit-card pattern so ordinary 13-to-19
    digit strings (ISBNs, ids) do not read as card numbers."""
    digits = [int(c) for c in s if c.isdigit()]
    if not (13 <= len(digits) <= 19):
        return False
    # Double every second digit counting from the right: for left-indexed i that
    # is i where i and len have the same parity. (Getting this backwards makes the
    # canonical test card 4111111111111111 read as invalid.)
    total, parity = 0, len(digits) % 2
    for i, d in enumerate(digits):
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def _redact(fragment: str) -> str:
    """Show enough to locate the value without reprinting it in full (and into
    the AI's own context)."""
    f = fragment.strip()
    return (f[:4] + "…" + f[-2:]) if len(f) > 8 else "…"

def _scan_text_for_secrets(text: str, scan_numeric: bool = True) -> list:
    """Return [(label, line_no, redacted), ...] for one file's text. scan_numeric
    gates the SSN and card-number patterns off: machine JSON/config (Obsidian's
    graph, coordinate and colour blobs) is full of long numbers that trip them,
    while the structured token/key patterns stay on everywhere (a plugin's
    data.json can legitimately hold a real API key)."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if SECRET_ALLOW_MARKER in line:
            continue
        for label, pat in SECRET_PATTERNS:
            if not scan_numeric and label == "US Social Security no.":
                continue
            m = pat.search(line)
            if m:
                hits.append((label, i, _redact(m.group(0))))
        if scan_numeric:
            cc = _CC_RE.search(line)
            if cc and _luhn_ok(cc.group(0)):
                hits.append(("Credit-card number", i, _redact(cc.group(0))))
    return hits

def _secret_scan_targets() -> list:
    """Text files to scan: git-tracked when in a repo (only what could be pushed),
    else every text file in the vault. brain.command is always excluded."""
    tracked = None
    try:
        out = subprocess.run(["git", "-C", str(BRAIN_DIR), "ls-files"],
                             capture_output=True, text=True, timeout=30)
        if out.returncode == 0:
            tracked = [BRAIN_DIR / p for p in out.stdout.splitlines() if p]
    except (OSError, subprocess.SubprocessError):
        tracked = None
    paths = tracked if tracked is not None else list(iter_all_files())
    return [p for p in paths
            if p.suffix.lower() in SECRET_SCAN_SUFFIXES
            and p.name not in SECRET_SCAN_SKIP and p.exists()]

def _run_secret_scan() -> list:
    """Scan the target set; return [(rel_path, label, line_no, redacted), ...]."""
    findings = []
    for p in _secret_scan_targets():
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scan_numeric = p.suffix.lower() not in (".json", ".ndjson")
        for label, line_no, red in _scan_text_for_secrets(text, scan_numeric=scan_numeric):
            findings.append((rel(p), label, line_no, red))
    return findings

def cmd_secrets(quiet: bool = False) -> int:
    """🔐 Scan tracked text for secrets and structured PII (keys, tokens, private
    keys, SSNs, card numbers). Returns 1 if anything is found, 0 if clean - the
    pre-push hook blocks on the exit code. Suppress a reviewed false positive with
    an inline `brain-allow-secret` marker on the line."""
    if not quiet:
        header("Secret / PII Scan", "🔐")
    findings = _run_secret_scan()
    if not findings:
        if not quiet:
            print("  ✅  No secrets or structured PII found in tracked text.")
        return 0
    if quiet:
        print(f"  ❌  Secret/PII scan blocked the push: {len(findings)} finding(s).")
    else:
        print(f"  ❌  {len(findings)} potential secret(s) / PII in tracked content:\n")
    for path, label, line_no, red in findings[:40]:
        print(f"    {path}:{line_no}  {label}  ({red})")
    if len(findings) > 40:
        print(f"    … {len(findings) - 40} more")
    print("\n  Move the value out of the vault (store a pointer, not the secret).")
    print(f"  A genuine false positive: add `{SECRET_ALLOW_MARKER}` to the line,"
          " or push with --no-verify.")
    return 1

def _health_secrets() -> int:
    """Health wrapper: warn (1) on findings, pass (0) when clean. Non-blocking in
    health; the pre-push hook is the hard gate."""
    findings = _run_secret_scan()
    if not findings:
        print("  ✅  No secrets or structured PII in tracked text.")
        return 0
    n = len(findings)
    print(f"  ⚠️   {n} potential secret(s)/PII in tracked content (newest scan):")
    for path, label, line_no, red in findings[:8]:
        print(f"       {path}:{line_no}  {label}  ({red})")
    if n > 8:
        print(f"       … {n - 8} more - run `secrets` for the full list")
    print("       Move each value out of the vault, or allowlist a false positive.")
    return 1

# ── Commit message policy: the AI-Driven Commit Process (Conventional Commits) ──
#
# Commits to this vault follow the AI-Driven Commit Process: a Conventional Commit
# header `<type>(<scope>): <emoji> <summary>`, a valid type, one emoji, one intent
# per commit, and a header of 72 characters or fewer. The commit-msg git hook calls
# `commitcheck` to enforce the header on every commit; the required session trailers
# live in the body and are not part of the header, so they are unaffected. Bypass a
# one-off with `git commit --no-verify`.
CONVENTIONAL_TYPES = ("feat", "fix", "docs", "style", "refactor", "perf", "test",
                      "build", "ci", "chore", "revert", "security")
_CC_HEADER = re.compile(
    r"^(?:" + "|".join(CONVENTIONAL_TYPES) + r")"
    r"(?:\([a-z0-9][a-z0-9._\-/ ]*\))?!?: (?P<subject>.+)$")
_CC_EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U00002190-\U000021FF"
    "\U00002B00-\U00002BFF\U0001F1E6-\U0001F1FF\U0000FE0F\U00002139]")

def cmd_commit_check(msgfile: str = "") -> int:
    """✅ Validate a commit message against the AI-Driven Commit Process
    (Conventional Commits): `<type>(<scope>): <emoji> <summary>`, a valid type, an
    emoji in the subject, and a header of 72 chars or fewer. Called by the commit-msg
    hook (install-hooks); comment lines and the body/trailers are ignored, only the
    header is enforced. Bypass a one-off with `git commit --no-verify`."""
    header("Commit Message Check", "✅ ")
    if not msgfile:
        fail("Usage: commitcheck <path-to-commit-msg-file>")
        return 2
    try:
        raw = Path(msgfile).read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        fail(f"Could not read {msgfile}: {e}")
        return 2
    subject = next((l for l in raw.splitlines() if l.strip() and not l.startswith("#")), "")
    problems = []
    m = _CC_HEADER.match(subject)
    if not m:
        problems.append("header must be `<type>(<scope>): <emoji> <summary>` with a valid type ("
                        + ", ".join(CONVENTIONAL_TYPES) + ")")
    elif not _CC_EMOJI.search(m.group("subject")):
        problems.append("the subject needs an emoji (the process expects exactly one), "
                        "e.g. `feat(secrets): ✨ add the scanner`")
    if subject and len(subject) > 72:
        problems.append(f"header is {len(subject)} chars; keep it to 72 or fewer")
    if not subject.strip():
        problems.append("the commit subject is empty")
    if problems:
        fail("Commit message does not follow the AI-Driven Commit Process:")
        for p in problems:
            print(f"       - {p}")
        print(f"\n     Header seen: {subject!r}")
        print("     Fix the message, or bypass a one-off with: git commit --no-verify")
        return 1
    ok(f"Conventional Commit header OK: {subject}")
    return 0


def cmd_install_hooks() -> int:
    """🪝 Wire the tracked git hooks (System/git-hooks) into this clone by pointing
    core.hooksPath at them. Portable by design: the hook scripts travel with the
    vault; this local, per-clone config makes them fire. Re-run after each clone."""
    header("Install Git Hooks", "🪝 ")
    hooks_dir = SYSTEM_DIR / "git-hooks"
    if not (BRAIN_DIR / ".git").exists():
        fail("Not a git repository - nothing to wire. Initialise git first.")
        return 1
    if not hooks_dir.is_dir():
        fail(f"Hook directory missing: {rel(hooks_dir)}")
        return 1
    for hook in hooks_dir.iterdir():
        if hook.is_file():
            try:
                hook.chmod(hook.stat().st_mode | 0o111)   # ensure executable
            except OSError:
                pass
    try:
        subprocess.run(["git", "-C", str(BRAIN_DIR), "config", "core.hooksPath",
                        str(hooks_dir)], check=True, capture_output=True, text=True)
    except (OSError, subprocess.SubprocessError) as e:
        fail(f"Could not set core.hooksPath: {e}")
        return 1
    ok(f"core.hooksPath → {rel(hooks_dir)}")
    print("     Active hooks: " + ", ".join(sorted(h.name for h in hooks_dir.iterdir() if h.is_file())))
    print("     The pre-push hook now runs the secret scan before every push.")
    return 0


def cmd_health() -> int:
    """🩺 Full BRAIN health check: lint, wikilink graph, stale scan, engine-owned
    anchors, version drift, an index drift + refresh, a secret/PII scan, and a review
    of the shared error log, in one pass. Leaves the index fresh."""
    header("BRAIN Health Check", "🩺")
    print("  Running: lint → links → stale → anchors → version drift → index (drift + refresh) → gitkeep → secrets → error log → scaffolding\n")

    results = {}

    print(divider("-"))
    print("  [1/10] Frontmatter Lint")
    print(divider("-"))
    results["lint"] = cmd_lint()

    print()
    print(divider("-"))
    print("  [2/10] Wikilink Graph")
    print(divider("-"))
    results["links"] = cmd_links("check")

    print()
    print(divider("-"))
    print("  [3/10] Stale Content Scan")
    print(divider("-"))
    results["stale"] = cmd_stale()

    print()
    print(divider("-"))
    print("  [4/10] Engine-Owned Anchors")
    print(divider("-"))
    results["anchors"] = _health_anchors()

    print()
    print(divider("-"))
    print("  [5/10] Version Drift")
    print(divider("-"))
    results["version"] = _health_version_drift()

    print()
    print(divider("-"))
    print("  [6/10] Index Drift + Refresh")
    print(divider("-"))
    results["index"] = _health_index()

    print()
    print(divider("-"))
    print("  [7/10] Gitkeep Maintenance")
    print(divider("-"))
    results["gitkeep"] = cmd_gitkeep()

    print()
    print(divider("-"))
    print("  [8/10] Secret / PII Scan")
    print(divider("-"))
    results["secrets"] = _health_secrets()

    print()
    print(divider("-"))
    print("  [9/10] Error Log Review")
    print(divider("-"))
    results["errors"] = _health_errors()

    print()
    print(divider("-"))
    print("  [10/10] Harness Scaffolding")
    print(divider("-"))
    results["scaffolding"] = _health_scaffolding()

    # Summary
    print()
    print("  " + "=" * 58)
    print("  🩺  Health Summary")
    print("  " + "=" * 58)
    icons = {0: "✅", 1: "⚠️ "}
    for name, code in results.items():
        icon = icons.get(code, "❌")
        print(f"  {icon}  {name.capitalize()}")
    overall = max(results.values())
    print()
    if overall == 0:
        print("  🏁  All checks passed - BRAIN is healthy.")
    else:
        print("  🏁  Issues found - review the output above.")
    print("  " + "=" * 58)
    print()
    return overall


def cmd_selftest() -> int:
    """🧪 Regression smoke test for brain.command itself: runs startup, a read-only
    memory-tier capacity check, lint, and links in-process and verifies each completes
    without raising. Catches code regressions (a command broken by an edit), distinct
    from health, which validates vault content. Strictly read-only: the old cascade
    step could move vault files mid-test, so it was replaced by the cap count.
    Sub-command output is suppressed - only pass/fail per command is shown."""
    import io, contextlib
    header("BRAIN Self-Test", "🧪")
    print("  Smoke-testing brain.command: startup → memory tiers → lint → links\n")

    def _tier_caps() -> int:
        """Read-only stand-in for the cascade step: each tier at or under cap."""
        over = 0
        for name, cap, path in MEMORY_TIERS:
            n = len(_memory_files(path))
            print(f"  {name}/: {n} of {cap}" + ("" if n <= cap else "  - OVER CAP (cascade owed)"))
            if n > cap:
                over += 1
        return 1 if over else 0

    checks = [
        ("startup",        lambda: cmd_startup()),
        ("memory tiers",   _tier_caps),
        ("lint",           lambda: cmd_lint()),
        ("links",          lambda: cmd_links("check")),
    ]
    results = {}
    for name, fn in checks:
        try:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = fn()
            if not isinstance(code, int):
                results[name] = "crash"
                fail(f"{name}: returned {type(code).__name__}, expected int exit code")
            elif code == 0:
                results[name] = "pass"
                ok(f"{name}: ran clean (exit 0)")
            else:
                results[name] = "warn"
                warn(f"{name}: ran, reported findings (exit {code})")
        except Exception as exc:
            results[name] = "crash"
            logging.getLogger("selftest").error(f"selftest: '{name}' crashed", exc_info=True)
            fail(f"{name}: raised {type(exc).__name__}: {exc}")

    print()
    print("  " + "=" * 58)
    print("  🧪  Self-Test Summary")
    print("  " + "=" * 58)
    icons = {"pass": "✅", "warn": "⚠️ ", "crash": "❌"}
    for name, st in results.items():
        print(f"  {icons[st]}  {name}")
    crashed = [n for n, s in results.items() if s == "crash"]
    print()
    if crashed:
        print(f"  🏁  REGRESSION: {len(crashed)} command(s) crashed - {', '.join(crashed)}.")
        print("  " + "=" * 58)
        print()
        return 1
    print("  🏁  All commands executed without error - no regressions.")
    print("  " + "=" * 58)
    print()
    return 0


# ══════════════════════════════════════════════════════════
#  17 - Memory (tiered pipeline management)
# ══════════════════════════════════════════════════════════

MEMORY_TIERS = [
    ("Current",  3,  BRAIN_DIR / "Memory" / "Context" / "Current"),
    ("Recent",   6,  BRAIN_DIR / "Memory" / "Context" / "Recent"),
]

# Per-entry Memory collections: one file per entry, with a folder-named index
# doc whose auto-maintained entries block lists those files. People and
# Decisions grow unboundedly (parent-document retrieval); the scaffolder
# (`memory add`) creates entries and the sync keeps each index truthful.
MEMORY_COLLECTIONS = [
    ("People",        BRAIN_DIR / "Memory" / "Entities" / "People",        "person",       "[Person Name]"),
    ("Organizations", BRAIN_DIR / "Memory" / "Entities" / "Organizations", "organization", "[Organization Name]"),
    ("Places",        BRAIN_DIR / "Memory" / "Entities" / "Places",        "place",        "[Place Name]"),
    ("Decisions",     BRAIN_DIR / "Memory" / "Decisions",                  "decision",     "[Decision Title]"),
    ("Events",        BRAIN_DIR / "Memory" / "Events",                     "event",        "[Event]"),
    ("Insights",      BRAIN_DIR / "Memory" / "Insights",                   "insight",      "[Insight]"),
]

# Cold storage for summaries that cascade out of Recent/. Unbounded, organized
# by year, never loaded at startup, reachable via `search`. Nothing is deleted:
# a lifetime of session history stays grep-able (Constitution 3.1, Section 14.2).
ARCHIVE_DIR = BRAIN_DIR / "Memory" / "Context" / "Archive"

# The generic continuity keywords every summary scaffolds with. They are useful
# for "what happened last time" style recall but identical across all summaries,
# so they carry no topic signal. _sync_summary_keywords replaces this default,
# once, with the session's actual Primary topics (kept as the first two anchors)
# so topic-relevant summaries rank in `search`. Defined once and reused by the
# scaffolder so the two never drift.
SUMMARY_KEYWORDS_DEFAULT = ["handoff", "continuity", "recap",
                            "what happened last time", "delta update",
                            "prior session context"]

def _archive_summary(f: Path) -> bool:
    """Move an overflow summary from Recent/ into Archive/<year>/, deriving the
    year from the YYYYMMDD-HHMMSS filename (fallback: 'undated')."""
    year = f.name[:4] if f.name[:4].isdigit() else "undated"
    dest_dir = ARCHIVE_DIR / year
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(f), str(_safe_dest(dest_dir / f.name)))
        return True
    except OSError as e:
        fail(f"Could not archive {f.name}: {e}")
        logging.getLogger("memory").error(e, exc_info=True)
        return False


def _archive_count() -> int:
    """Number of archived summaries across all Memory/Archive/<year>/ folders.
    Excludes the Archive/ namesake folder doc (Archive.md)."""
    if not ARCHIVE_DIR.exists():
        return 0
    return sum(1 for f in ARCHIVE_DIR.rglob("*.md") if f.stem != "Archive")

def _memory_files(tier_path: Path) -> list[Path]:
    """Return sorted list of summary .md files in a tier directory (oldest first
    by filename). The tier's namesake folder doc (e.g. Current/Current.md) is a
    folder document, not a session summary, so it is excluded - it never counts
    toward the tier cap and never cascades."""
    if not tier_path.exists():
        return []
    files = sorted(
        f for f in tier_path.iterdir()
        if f.is_file() and f.suffix == ".md" and f.stem != tier_path.name
    )
    return files


# Markers bounding the auto-maintained summary-link block inside each tier doc.
TIER_LINKS_START = "<!-- brain:tier-summaries (auto-maintained by brain.command - do not edit by hand) -->"
TIER_LINKS_END = "<!-- /brain:tier-summaries -->"


def _sync_tier_doc_links() -> int:
    """Keep each Current/Recent tier doc's auto-maintained block in sync
    with the summary files currently in that tier: one wikilink per summary, by
    basename. Idempotent; called after every cascade so the per-tier links follow
    the summaries as they flow downhill (Memory/Memory.md, Constitution 3.7
    Memory-tier cascade-chain exception). Returns the number of docs changed."""
    changed = 0
    for name, _cap, path in MEMORY_TIERS:
        doc = path / f"{name}.md"
        if not doc.exists():
            continue
        summaries = _memory_files(path)
        body = ("\n".join(f"- [[{f.stem}]]" for f in summaries)
                if summaries else "_No summaries in this tier right now._")
        if _sync_marker_block(doc, TIER_LINKS_START, TIER_LINKS_END,
                              body, "tier-summaries"):
            changed += 1
    return changed


def _summary_topics(text: str) -> list:
    """Pull a session's Primary topics from a summary body, for use as frontmatter
    keywords. Reads the '- Primary topics:' line in the Session Metadata section
    and splits it into lowercase, de-duplicated topic phrases. Returns [] when the
    line is absent or still an unfilled scaffold, so an empty summary is left as is."""
    m = re.search(r"(?im)^[-*]?\s*Primary topics:\s*(.+?)\s*$", text)
    if not m:
        return []
    raw = m.group(1).strip()
    if raw.lower() in ("", "n/a", "none", "tbd", "-"):
        return []
    parts = re.split(r"[,;/]| and | & ", raw)
    seen, out = set(), []
    for p in parts:
        kw = re.sub(r"\s+", " ", p).strip().strip(".").lower()
        # Keep short distinctive phrases; drop empties and overlong fragments.
        if kw and len(kw) <= 40 and kw.count(" ") <= 5 and kw not in seen:
            seen.add(kw); out.append(kw)
    return out[:6]


def _sync_summary_keywords() -> int:
    """Enrich each session summary's frontmatter `keywords` with its actual Primary
    topics, so topic queries rank it in `search` (which weights frontmatter keywords
    heavily). Engine-owned and one-shot per file: it acts only while a summary still
    carries the generic SUMMARY_KEYWORDS_DEFAULT, replacing it with two continuity
    anchors plus the body's topics, then leaves the file alone, so manual edits and
    immutable history are never overwritten. Walks every tier - Current, Recent, and
    the Archive - and returns the number of summaries enriched."""
    summaries = []
    for _name, _cap, path in MEMORY_TIERS:
        summaries.extend(_memory_files(path))
    if ARCHIVE_DIR.exists():
        summaries.extend(f for f in ARCHIVE_DIR.rglob("*.md") if f.stem != "Archive")
    changed = 0
    for f in summaries:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        fm = parse_frontmatter(f) or {}
        # Only session-summary records, and only while keywords are the untouched
        # generic default (one-shot - never fights a later manual edit).
        if fm.get("type") != "record" or fm.get("folder") != "memory":
            continue
        if _aslist(fm.get("keywords", [])) != SUMMARY_KEYWORDS_DEFAULT:
            continue
        topics = _summary_topics(text)
        if not topics:
            continue
        # Two continuity anchors keep "what happened last time" recall working;
        # the topics make the summary findable by subject. Cap at 8 (Section 8.7).
        new_kw = ["handoff", "continuity"] + [t for t in topics
                                              if t not in ("handoff", "continuity")]
        new_line = f"keywords: {json.dumps(new_kw[:8])}"
        new_text, n = re.subn(r"(?m)^keywords:.*$", new_line, text, count=1)
        if n and new_text != text:
            try:
                f.write_text(new_text, encoding="utf-8")
                changed += 1
            except OSError:
                pass
    return changed


# Markers bounding the auto-maintained entries block inside each per-entry
# collection index doc (Memory/Entities/People/People.md, Memory/Decisions/Decisions.md).
COLLECTION_LINKS_START = "<!-- brain:collection-entries (auto-maintained by brain.command - do not edit by hand) -->"
COLLECTION_LINKS_END = "<!-- /brain:collection-entries -->"


def _collection_entry_files(folder: Path) -> list[Path]:
    """Entry .md files in a per-entry Memory collection folder, sorted by name.
    Excludes the folder's namesake index doc and dotfiles - those are not
    entries and never appear in the auto-maintained list."""
    if not folder.exists():
        return []
    return sorted(
        f for f in folder.iterdir()
        if f.is_file() and f.suffix == ".md"
        and f.stem != folder.name and not f.name.startswith(".")
    )


def _sync_collection_doc_links() -> int:
    """Keep each per-entry collection index's entries block in sync with the
    entry files in its folder: one path-qualified wikilink per entry. The
    People/Decisions analogue of _sync_tier_doc_links - the index never drifts
    because the engine, not the AI, rebuilds it from the folder contents. Path
    links are unambiguous and survive same-named entries. Idempotent. Returns
    the number of docs changed."""
    changed = 0
    for name, folder, _kind, _placeholder in MEMORY_COLLECTIONS:
        doc = folder / f"{name}.md"
        if not doc.exists():
            continue
        entries = _collection_entry_files(folder)
        if entries:
            relf = folder.relative_to(BRAIN_DIR).as_posix()
            body = "\n".join(f"- [[{relf}/{f.stem}|{f.stem}]]" for f in entries)
        else:
            body = f"_No {name.lower()} recorded yet._"
        if _sync_marker_block(doc, COLLECTION_LINKS_START, COLLECTION_LINKS_END,
                              body, "collection-entries"):
            changed += 1
    return changed


# Structural hub links: a folder doc may wikilink the namesake docs of its
# immediate subfolders (Constitution 3.7 rule 1). This keeps that second level
# of the hub-and-spoke graph from drifting - e.g. each Library class doc links
# its division docs, so divisions are not orphaned in the graph. The engine,
# not the AI, maintains an auto-block; injection is opt-in per folder doc and
# skips docs that already link all their children by hand (e.g. Library.md).
CHILDREN_LINKS_START = "<!-- brain:children (auto-maintained by brain.command - do not edit by hand) -->"
CHILDREN_LINKS_END = "<!-- /brain:children -->"

def _immediate_subfolder_docs(folder: Path) -> list:
    """Namesake docs of `folder`'s immediate subfolders (subfolder X/ holding
    X.md), excluding hidden and Template dirs. Sorted by name."""
    out = []
    try:
        for d in sorted(folder.iterdir(), key=lambda p: p.name):
            if not d.is_dir() or d.name.startswith(".") or d.name == "Template":
                continue
            doc = d / f"{d.name}.md"
            if doc.exists():
                out.append(doc)
    except OSError:
        pass
    return out

def _children_block(folder: Path) -> str:
    docs = _immediate_subfolder_docs(folder)
    if docs:
        body = "\n".join(
            f"- [[{d.parent.relative_to(BRAIN_DIR).as_posix()}/{d.stem}|{d.stem}]]"
            for d in docs)
    else:
        body = "_No subfolders yet._"
    return f"{CHILDREN_LINKS_START}\n{body}\n{CHILDREN_LINKS_END}"

def _is_folder_doc(doc: Path) -> bool:
    return doc.suffix == ".md" and doc.stem == doc.parent.name

def _sync_children_links(doc: Path) -> bool:
    """Inject or refresh a folder doc's immediate-subfolder-namesake link block.
    Refreshes in place if the block exists; otherwise injects only when the
    folder has subfolder namesakes AND the doc does not already wikilink them all
    (so a hand-linked hub like Library.md is left untouched). Into a `## Divisions`
    section when present, else a new `## Subfolders` section. Returns True if the
    file changed."""
    folder = doc.parent
    try:
        text = doc.read_text(encoding="utf-8")
    except OSError:
        return False
    has_block = CHILDREN_LINKS_START in text
    children = _immediate_subfolder_docs(folder)
    if not has_block:
        if not children:
            return False
        if all(re.search(r"\[\[[^\]]*" + re.escape(c.stem) + r"(\||\])", text)
               for c in children):
            return False   # already a hand-linked hub - leave it alone
    block = _children_block(folder)
    if has_block:
        pat = re.escape(CHILDREN_LINKS_START) + r".*?" + re.escape(CHILDREN_LINKS_END)
        new = re.sub(pat, block, text, count=1, flags=re.DOTALL)
    else:
        anchor = re.search(r"\n## Divisions[^\n]*\n", text)
        if anchor:
            nxt = text.find("\n## ", anchor.end())
            at = nxt if nxt != -1 else len(text)
            new = text[:at].rstrip() + "\n\n" + block + "\n" + text[at:]
        else:
            new = text.rstrip() + f"\n\n## Subfolders\n\n{block}\n"
    if new != text:
        try:
            doc.write_text(new, encoding="utf-8")
            return True
        except OSError:
            return False
    return False

def _refresh_all_children_blocks() -> int:
    """Refresh every folder doc that already carries a brain:children block
    (opt-in maintenance; never injects new blocks). Returns docs changed."""
    changed = 0
    for doc in BRAIN_DIR.rglob("*.md"):
        parts = doc.relative_to(BRAIN_DIR).parts
        if any(p.startswith(".") or p == "Template" for p in parts):
            continue
        if not _is_folder_doc(doc):
            continue
        try:
            if CHILDREN_LINKS_START in doc.read_text(encoding="utf-8"):
                if _sync_children_links(doc):
                    changed += 1
        except OSError:
            pass
    return changed


# Profile entry engine: the four entry-bearing facets (Values/beliefs, Goals,
# Skills, Health/conditions). Mirrors the Memory collection machinery -
# `profile add`/`rm` scaffold and soft-remove entries; each facet namesake
# carries an auto-maintained entries block so its list never drifts. The flat
# facets (Biography, Personality, ...) are filled in place and take no entries.
PROFILE_COLLECTIONS = [
    ("belief",    BRAIN_DIR / "Profile" / "Values", "[Belief]",            "Belief.md"),
    ("goal",      BRAIN_DIR / "Profile" / "Goals",  "[Goal]",              "Goal.md"),
    ("skill",     BRAIN_DIR / "Profile" / "Skills", "[Skill]",             "Skill.md"),
    ("condition", BRAIN_DIR / "Profile" / "Health", "[Condition or Need]", "Health Condition.md"),
]
PROFILE_LINKS_START = "<!-- brain:profile-entries (auto-maintained by brain.command - do not edit by hand) -->"
PROFILE_LINKS_END = "<!-- /brain:profile-entries -->"

# Profile coverage registry (`profile coverage`, the identify skill's targeting
# engine). All 12 facets in canonical Profile.md order; kind decides the file
# scope: "flat" scores Profile/<Name>.md alone, "folder" scores the namesake
# Profile/<Name>/<Name>.md plus every non-namesake *.md directly in the folder
# as entries. Profile/.template/ sits outside the facet folders, so no
# exclusion logic is needed.
PROFILE_FACETS = [
    ("Working Style", "flat"),
    ("Biography",     "flat"),
    ("Personality",   "flat"),
    ("Values",        "folder"),
    ("Goals",         "folder"),
    ("Relationships", "flat"),
    ("Finances",      "flat"),
    ("Lifestyle",     "flat"),
    ("Skills",        "folder"),
    ("Preferences",   "flat"),
    ("Health",        "folder"),
    ("Focus",         "flat"),
]

# Frozen scaffold fingerprint: per facet file, the CRC32 of every normalized
# body line (normalize = strip, collapse internal whitespace, NFC; blank
# lines, headings, and comment-only lines excluded) of the LIVE facet files at
# build time. A scored line whose normalized CRC32 sits in its file's set is
# scaffold prose, never substantive. At runtime the scorer UNIONs these with
# the live hashes of every Profile/.template/*.md body, so freshly scaffolded
# entries score empty too (the dual net: this fingerprint plus the placeholder
# grammar in _cov_is_placeholder, each catching what the other misses).
# Regenerate after a DELIBERATE scaffold change to the facet files:
#   python3 -c "from importlib.machinery import SourceFileLoader as L; print(L('bc','System/brain.command').load_module()._profile_scaffold_crc_render())"
PROFILE_SCAFFOLD_CRC = {
    "Working Style.md": frozenset({
        225209147, 442933976, 497893808, 567785087, 872849886, 1473648760,
        1528284317, 1639605086, 1763157381, 1954678798, 2143291461,
        2399925122, 2434787203, 2487941427, 2677263777, 2808827032,
        2832163386, 3083319045, 3357992108, 3402499179, 3837814167,
        3964262313
    }),
    "Biography.md": frozenset({
        310840053, 354147002, 401978619, 453334733, 482937417, 519194785,
        549516871, 658314844, 762757395, 831918062, 941151755, 1029135874,
        1051983102, 1139149987, 1149532178, 1171063423, 1242860332,
        1445288146, 1537616239, 1707618477, 2038284520, 2124765175,
        2155206015, 2328447477, 2352517808, 2527877439, 2690999041,
        2701507878, 2821568757, 3095903692, 3166980710, 3280337304,
        3326179636, 3349361925, 3375409968, 3436593376, 3533523800,
        3557068584, 3707757044, 3965579265, 4267856163
    }),
    "Personality.md": frozenset({
        43106626, 172949556, 263251845, 385762225, 414789057, 453011166,
        597959258, 766929257, 787799655, 868917294, 940583144, 988814532,
        1286581933, 1336166355, 1440537495, 1469418942, 1502783263,
        1574938528, 1660748535, 1718235761, 1769595493, 1918441090,
        1947656589, 1983469875, 2340378090, 2511452218, 2570411252,
        2627141214, 2678175334, 2731067632, 2774464729, 2881780122,
        2972041163, 2994267298, 3164336382, 3299723511, 3329436946,
        3344212629, 3377343814, 3377466330, 3442278076, 3492840022,
        3517038197, 3633935119, 4094835117, 4106442123, 4147376602
    }),
    "Values/Values.md": frozenset({
        64571753, 133184907, 567585524, 576477779, 664762895, 1100624917,
        1242869265, 1393933323, 1541944181, 1692748845, 1791513285,
        1964396377, 2030850315, 2146954983, 2195606387, 2215321892,
        2460764168, 2470841111, 2536750863, 2547483114, 2970584590,
        3447046022, 3863433903, 4015021805, 4054868288, 4208915591,
        4289391736
    }),
    "Goals/Goals.md": frozenset({
        537310124, 833632538, 1509716455, 1541944181, 3357936836,
        3375049606
    }),
    "Relationships.md": frozenset({
        400581226, 909950840, 1493176178, 1589068732, 2658417594,
        3705302770, 3712249236, 4100675524
    }),
    "Finances.md": frozenset({
        119251758, 158731507, 1543356404, 1637126693, 2408883026,
        3032485432, 3519053553, 3622255849, 4162862514, 4165506174,
        4215442947
    }),
    "Lifestyle.md": frozenset({
        347189939, 501402642, 818900200, 1442215377, 2008339254,
        2452350216, 2590878688, 2728366794, 2827797343, 3999570569
    }),
    "Skills/Skills.md": frozenset({
        1260468728, 1541944181, 1695391521, 3164114714, 3191792892,
        3315365580, 3497773973, 3669970215, 3697358632
    }),
    "Preferences.md": frozenset({
        124895376, 315944096, 322728521, 522087176, 693982146, 1053336049,
        1066299920, 1242246075, 1320195823, 1334221162, 1610036074,
        1807862734, 2152556847, 2511509271, 2574557650, 2869907037,
        2874091983, 2874497879, 2881929483, 3280393706, 3634789523,
        3859953358, 4140291926
    }),
    "Health/Health.md": frozenset({
        42257026, 248177932, 1423946993, 1482471845, 1541944181,
        2750784822, 3376311458
    }),
    "Focus.md": frozenset({
        904439264, 949487940, 1041995441, 1104286287, 1112599439,
        1848870927, 2495542468, 2659992988, 2887700068, 3278924594,
        4067029393, 4086500816
    }),
}


def _sync_profile_doc_links() -> int:
    """Keep each entry-bearing Profile facet namesake's entries block in sync
    with the entry files in its folder: one path-qualified wikilink per entry.
    The Profile analogue of _sync_collection_doc_links - the namesake (a folder
    hub) never drifts because the engine rebuilds it. Idempotent. Returns the
    number of docs changed."""
    changed = 0
    for _kind, folder, _ph, _tpl in PROFILE_COLLECTIONS:
        doc = folder / f"{folder.name}.md"
        if not doc.exists():
            continue
        entries = _collection_entry_files(folder)
        if entries:
            relf = folder.relative_to(BRAIN_DIR).as_posix()
            body = "\n".join(f"- [[{relf}/{f.stem}|{f.stem}]]" for f in entries)
        else:
            body = "_None recorded yet._"
        if _sync_marker_block(doc, PROFILE_LINKS_START, PROFILE_LINKS_END,
                              body, "profile-entries"):
            changed += 1
    return changed


def _memory_list() -> int:
    """Show all files across all three memory tiers."""
    total = 0
    for name, cap, path in MEMORY_TIERS:
        files = _memory_files(path)
        count = len(files)
        total += count
        print(f"  📂  {name}/  ({count}/{cap})")
        if files:
            for f in files:
                tokens = count_tokens(f)
                print(f"       📄  {f.name}  ({tokens:,} tokens)")
        else:
            print(f"       (empty)")
        print()
    n_arch = _archive_count()
    print(f"  📂  Archive/  ({n_arch}, unbounded cold storage by year)")
    print()
    print(divider())
    _maxt = sum(cap for _n, cap, _p in MEMORY_TIERS)
    print(f"  🏁  {total} file(s) across {len(MEMORY_TIERS)} active tiers (max {_maxt})  +  {n_arch} archived")
    print(divider())
    return 0


def _memory_status() -> int:
    """Show file counts per tier and remaining capacity."""
    total = 0
    print(f"  {'Tier':<12}  {'Files':>5}  {'Max':>5}  {'Free':>5}  {'Status'}")
    print(f"  {'-'*12}  {'-'*5}  {'-'*5}  {'-'*5}  {'-'*12}")
    for name, cap, path in MEMORY_TIERS:
        count = len(_memory_files(path))
        total += count
        free = cap - count
        status = "✅ OK" if count < cap else "⚠️  FULL"
        print(f"  {name:<12}  {count:>5}  {cap:>5}  {free:>5}  {status}")
    n_arch = _archive_count()
    print(f"  {'Archive':<12}  {n_arch:>5}      ∞      ∞  🗄️  cold")
    print()
    print(divider())
    print(f"  🏁  Total: {total}/{sum(cap for _n, cap, _p in MEMORY_TIERS)} active slots used  ·  {n_arch} archived (never deleted)")
    print(divider())
    return 0


def _memory_cascade() -> int:
    """Enforce the 3/6/unbounded limits by cascading oldest files down the tiers.
    Recent/ overflow is ARCHIVED to Memory/Context/Archive/<year>/ - never deleted -
    so a lifetime of session history remains searchable (Section 14.2).
    Tiers are processed top-down repeatedly until everything fits, so overflow
    pushed into a lower tier in one pass is handled in the next."""
    log = logging.getLogger("memory")
    moved = archived = 0

    settled = False
    while not settled:
        settled = True
        for i, (name, cap, path) in enumerate(MEMORY_TIERS):
            files = _memory_files(path)
            while len(files) > cap:
                oldest = files.pop(0)
                if i + 1 < len(MEMORY_TIERS):
                    next_name, _, next_path = MEMORY_TIERS[i + 1]
                    try:
                        next_path.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(oldest), str(_safe_dest(next_path / oldest.name)))
                        print(f"  ↓  {oldest.name}: {name}/ → {next_name}/")
                        moved += 1
                        settled = False
                    except OSError as e:
                        fail(f"Could not move {oldest.name}: {e}")
                        log.error(e, exc_info=True)
                        break
                else:
                    if _archive_summary(oldest):
                        year = oldest.name[:4] if oldest.name[:4].isdigit() else "undated"
                        print(f"  🗄️   {oldest.name}: {name}/ → Archive/{year}/")
                        archived += 1
                    else:
                        break

    if moved == 0 and archived == 0:
        print(f"  ✅  All tiers within capacity - no cascading needed.")

    relinked = _sync_tier_doc_links()
    if relinked:
        print(f"  🔗  Resynced summary links in {relinked} tier doc(s).")

    print()
    print(divider())
    print(f"  🏁  Cascade complete - {moved} moved, {archived} archived (nothing deleted)")
    print(divider())
    return 0


def _strip_frontmatter(text: str) -> str:
    """Return a markdown file's body with its leading YAML frontmatter removed."""
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)


def cmd_memory_add(kind: str = "", name: str = "", when: str = "") -> int:
    """🧠 Scaffold one entry in a per-entry Memory collection from its template.
    `memory add person "Jane Doe"` creates Memory/Entities/People/Jane Doe.md (real name,
    casing preserved). `memory add decision "Switched to LLC"` creates a
    date-prefixed Memory/Decisions/YYYY-MM-slug.md. Each gets a fresh id, synced
    tags, and is registered in its index. (Dates rows are added with
    `memory add date` - see cmd_memory_add_row.)"""
    header("Add Memory Entry", "🧠")
    kind = (kind or "").strip().lower()
    coll = next((c for c in MEMORY_COLLECTIONS if c[2] == kind), None)
    if not coll:
        fail(f"Unknown kind '{kind}' - use 'person' or 'decision'.")
        print("  (Dates rows: `memory add date ...`. Facts about the user go to "
              "Profile, not Memory.)")
        return 1
    cname, folder, _kind, placeholder = coll
    if not name.strip():
        fail(f'No name provided. Usage: memory add {kind} "Name".')
        return 1
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    raw = name.strip()
    # Filename + title per collection. Person: real name, casing preserved,
    # only path-illegal characters stripped (Article 2.6 allows spaces in file
    # names). Decision: date-prefixed slug so records sort chronologically.
    if kind in ("person", "organization", "place"):
        title = re.sub(r"[\\/:*?\"<>|]", "", raw).strip()
        if not title:
            fail("Name reduces to nothing after removing illegal characters.")
            return 1
        fname = f"{title}.md"
        tags = ["memory", "record", "sensitive"] if kind == "person" else ["memory", "record"]
        desc = f"{kind.capitalize()} entry for {title} ({cname})."
    else:  # dated record: decision/insight (YYYY-MM-slug); event (YYYY-MM-DD-slug)
        title = raw
        if kind == "event":
            # Filename date is the event date: honor an explicit "When"
            # (YYYY-MM-DD) when given, else stamp today.
            mw = re.match(r"^\d{4}-\d{2}-\d{2}$", when.strip()) if when else None
            stamp = when.strip() if mw else datetime.now(timezone.utc).strftime("%Y-%m-%d")
        else:
            stamp = datetime.now(timezone.utc).strftime("%Y-%m")
        slug = _slugify(title)
        # Idempotent date prefix: a title that already leads with its own
        # YYYY-MM(-DD)- date keeps it (a dated name once produced a doubled
        # 2026-07-2026-07-... filename, found live 2026-07-02).
        fname = f"{slug}.md" if re.match(r"^\d{4}-\d{2}(-\d{2})?-", slug) \
            else f"{stamp}-{slug}.md"
        tags = ["memory", "record"]
        desc = f"{kind.capitalize()} record: {title} ({cname})."
    dest = folder / fname
    if not folder.exists():
        fail(f"Collection folder missing: {rel(folder)}")
        return 1
    if dest.exists():
        fail(f"Already exists: {rel(dest)}")
        print(f"  Disambiguate, e.g. \"{raw} (work)\", rather than overwriting.")
        return 1
    template = BRAIN_DIR / "Memory" / ".template" / (placeholder_template := {
        "person": "Person.md", "organization": "Organization.md", "place": "Place.md",
        "decision": "Decision.md", "event": "Event.md", "insight": "Insight.md"}[kind])
    if not template.exists():
        fail(f"Template not found: {rel(template)}")
        return 1
    # Fresh, unique id from the title (not the dated filename), folder-prefixed.
    rel_folder = folder.relative_to(BRAIN_DIR).as_posix()
    layer = len(folder.relative_to(BRAIN_DIR).parts)
    taken = _all_ids()
    base = f"{ID_PREFIX.get('memory', 'me')}-{_slugify(title)}"
    fid = base
    i = 2
    while fid in taken:
        fid = f"{base}-{i}"; i += 1
    # Instance frontmatter, two-band order (Instructions 8.8). Non-core: no
    # version. Body comes from the template with the placeholder filled.
    tg = ", ".join(f'"{t}"' for t in tags)
    fm = (f"---\n"
          f'title: "{title}"\n'
          f'description: "{desc}"\n'
          f'status: "active"\n'
          f"tags: [{tg}]\n"
          f"aliases: []\n"
          f"keywords: []\n"
          f"created: {today}\n"
          f"updated: {today}\n"
          f'type: "record"\n'
          f'folder: "memory"\n'
          f"layer: {layer}\n"
          f"policy: false\n"
          f'author: "Tanner Golden"\n'
          f'path: "BRAIN/{rel_folder}/{fname}"\n'
          f'id: "{fid}"\n'
          f"---\n")
    try:
        body = _strip_frontmatter(template.read_text(encoding="utf-8"))
        body = body.replace(placeholder, title)
        dest.write_text(fm + body, encoding="utf-8")
    except OSError as e:
        fail(f"Could not write {rel(dest)}: {e}")
        logging.getLogger("memory").error(e, exc_info=True)
        return 1
    ok(f"Created {rel(dest)}  (id: {fid})")
    if _set_macos_tags(dest, tags):
        print(f"       🏷  Finder tags synced.")
    relinked = _sync_collection_doc_links()
    if relinked:
        print(f"       🔗  Registered in {cname}/{cname}.md.")
    print()
    print(divider())
    print(f"  🏁  {cname[:-1] if cname.endswith('s') else cname} entry ready - fill it in, then `sync`.")
    print(divider())
    return 0


# Fixed-file collections: their domain/category files and valid values. The
# engine writes table rows into these so the AI never hand-edits a table.
DATE_SECTIONS = {"recurring": "Recurring", "onetime": "One-Time",
                 "one-time": "One-Time", "milestone": "Milestones",
                 "milestones": "Milestones",
                 "anniversary": "Milestones"}


def _append_table_row(path: Path, cells: list, after_heading: str = None) -> bool:
    """Append a row to a markdown table and bump the file's `updated`. With
    after_heading, target the first table after that heading; else the first
    table in the file. If the table body is only the blank placeholder row, the
    new row replaces it. Cells are pipe-escaped. The engine, not the AI, formats
    and writes the row - this keeps Dates and the Log's routing-notes table free
    of hand-edited tables. Returns True on success."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    lines = text.split("\n")
    start, end = 0, len(lines)
    if after_heading:
        h = next((i for i, l in enumerate(lines)
                  if l.lstrip().startswith("#") and after_heading.lower() in l.lower()), None)
        if h is None:
            return False
        start = h + 1
        # Bound the search to this section's span (stop at the next heading):
        # a missing table must fail here, never write into the next table down-file.
        end = next((i for i in range(start, len(lines))
                    if lines[i].lstrip().startswith("#")), len(lines))
    sep = next((i for i in range(start, end)
                if lines[i].strip().startswith("|")
                and set(lines[i].strip()) <= set("|:- ") and "-" in lines[i]), None)
    if sep is None:
        return False
    body_start = sep + 1
    j = body_start
    while j < len(lines) and lines[j].lstrip().startswith("|"):
        j += 1
    safe = [str(c).replace("|", "\\|").replace("\n", " ").strip() for c in cells]
    row = "| " + " | ".join(safe) + " |"

    def _blank(l):
        return all(c.strip() == "" for c in l.strip().strip("|").split("|"))
    existing = lines[body_start:j]
    if existing and all(_blank(l) for l in existing):
        lines[body_start:j] = [row]
    else:
        lines.insert(j, row)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    new_text, _ = _sub_frontmatter("\n".join(lines), r"^updated:\s*.*$",
                                   f"updated: {today}")
    try:
        _write_atomic(path, new_text)
        return True
    except OSError:
        return False


def cmd_memory_add_row(kind: str, parts: list) -> int:
    """🧠 Engine-write one row into Memory/Dates.md - so the AI supplies content,
    never hand-edits a table.
      memory add date <recurring|onetime|milestone> "When" "Event" [notes]"""
    header("Add Memory Entry", "🧠")
    if kind != "date":
        fail(f"Unknown kind '{kind}' - the only add-row kind is 'date'.")
        return 1
    if len(parts) < 3 or not parts[2].strip():
        fail('Usage: memory add date <recurring|onetime|milestone> "When" "Event" [notes]')
        return 1
    section = DATE_SECTIONS.get(parts[0].strip().lower())
    if not section:
        fail(f"Unknown section '{parts[0]}' - use recurring, onetime, or milestone."); return 1
    notes = parts[3].strip() if len(parts) > 3 else ""
    path = BRAIN_DIR / "Memory" / "Dates.md"
    # Columns: When/Date | Event | Notes - the three-cell tables in Memory/Dates.md.
    _quiet_backup(path)
    if not _append_table_row(path, [parts[1].strip(), parts[2].strip(), notes],
                             after_heading=section):
        fail(f"Could not append under '{section}' in {rel(path)}."); return 1
    ok(f"Added a date under '{section}' in {rel(path)}.")
    print()
    print(divider())
    print("  🏁  Row written and formatted by the engine - no hand-edited tables.")
    print(divider())
    return 0


def _quiet_backup(path: Path) -> None:
    """Pre-edit snapshot to System/.backups (Instructions Section 10), then rotate.
    Best-effort: a backup failure must not block the edit's own error handling.
    Skipped in a remote-backed vault, where git history is the pre-edit backstop."""
    if _remote_backed():
        return
    try:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        bdir = SYSTEM_DIR / ".backups"
        bdir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(path), str(bdir / _backup_dest_name(path, ts)))
        _backup_rotate(quiet=True)
    except OSError:
        pass


def _blank_row(l: str) -> bool:
    return all(c.strip() == "" for c in l.strip().strip("|").split("|"))


def _locate_table(lines: list, after_heading: str = None):
    """Return (sep_idx, body_start, body_end) for the first markdown table (after
    `after_heading` if given, bounded to that section's span - the search stops at
    the next heading so it can never land on a table down-file), or None."""
    start, end = 0, len(lines)
    if after_heading:
        h = next((i for i, l in enumerate(lines)
                  if l.lstrip().startswith("#") and after_heading.lower() in l.lower()), None)
        if h is None:
            return None
        start = h + 1
        end = next((i for i in range(start, len(lines))
                    if lines[i].lstrip().startswith("#")), len(lines))
    sep = next((i for i in range(start, end)
                if lines[i].strip().startswith("|")
                and set(lines[i].strip()) <= set("|:- ") and "-" in lines[i]), None)
    if sep is None:
        return None
    body_start = sep + 1
    j = body_start
    while j < len(lines) and lines[j].lstrip().startswith("|"):
        j += 1
    return (sep, body_start, j)


def _norm(s: str) -> str:
    return re.sub(r"[-\s]+", " ", str(s).lower()).strip()


def _remove_table_row(path: Path, match: str, after_heading: str = None):
    """Remove the single body row matching `match` (case-insensitive substring).
    Returns ('ok', removed) | ('none', None) | ('multi', rows) | ('notable', None).
    Restores a blank placeholder if the table empties, and bumps `updated`."""
    try:
        lines = path.read_text(encoding="utf-8").split("\n")
    except OSError:
        return ("notable", None)
    loc = _locate_table(lines, after_heading)
    if not loc:
        return ("notable", None)
    _sep, bs, be = loc
    hits = [i for i in range(bs, be) if not _blank_row(lines[i]) and match.lower() in lines[i].lower()]
    if not hits:
        return ("none", None)
    if len(hits) > 1:
        return ("multi", [lines[i].strip() for i in hits])
    removed = lines[hits[0]].strip()
    del lines[hits[0]]
    loc2 = _locate_table(lines, after_heading)
    if loc2:
        sep2, bs2, be2 = loc2
        if not any(not _blank_row(l) for l in lines[bs2:be2]):
            ncols = max(lines[sep2].count("|") - 1, 1)
            lines[bs2:be2] = ["|" + " |" * ncols]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    new_text, _ = _sub_frontmatter("\n".join(lines), r"^updated:\s*.*$", f"updated: {today}")
    try:
        _write_atomic(path, new_text)
        return ("ok", removed)
    except OSError:
        return ("notable", None)


def _find_entry_files(folder: Path, match: str) -> list:
    """Entry files in a per-entry collection whose stem or title matches `match`
    (normalized substring, hyphens and spaces equivalent)."""
    out = []
    for f in _collection_entry_files(folder):
        fm = parse_frontmatter(f) or {}
        hay = f"{_norm(f.stem)} {_norm(fm.get('title', ''))}"
        if _norm(match) in hay:
            out.append(f)
    return out


def cmd_memory_rm(parts: list) -> int:
    """🗑  Remove a Memory entry through the engine, never by hand. Files
    (person/decision) soft-remove to .trash (two-level, needs --yes); a Dates row
    is backed up then removed.
      memory rm person|decision "<name match>"     --yes
      memory rm date <recurring|onetime|milestone> "<row text match>"  --yes"""
    header("Remove Memory Entry", "🗑")
    kind = (parts[0].lower() if parts else "")
    if kind in ("person", "organization", "place", "decision", "event", "insight"):
        coll = next((c for c in MEMORY_COLLECTIONS if c[2] == kind), None)
        cname, folder = coll[0], coll[1]
        match = parts[1] if len(parts) > 1 else ""
        if not match.strip():
            fail(f'Usage: memory rm {kind} "<name match>" --yes'); return 1
        hits = _find_entry_files(folder, match)
        if not hits:
            fail(f"No {kind} file matches '{match}' in {cname}/."); return 1
        if len(hits) > 1:
            fail(f"'{match}' matches {len(hits)} files - be more specific:")
            for h in hits:
                print(f"       - {h.name}")
            return 1
        target = hits[0]
        print(f"  Soft-remove {rel(target)} to .trash/ (recoverable)?")
        if not confirm("Proceed? (yes/no): "):
            print("\n  🚫  Aborted (re-run with --yes).\n"); return 0
        dest = _soft_remove(target)
        if not dest:
            fail(f"Could not remove {rel(target)}."); return 1
        ok(f"{rel(target)}  →  .trash/")
        relinked = _sync_collection_doc_links()
        if relinked:
            print(f"       🔗  Unregistered from {cname}/{cname}.md.")
    elif kind == "date":
        if len(parts) < 3 or not parts[2].strip():
            fail('Usage: memory rm date <recurring|onetime|milestone> "<row text match>" --yes'); return 1
        head = DATE_SECTIONS.get(parts[1].strip().lower())
        if not head:
            fail("Section must be recurring, onetime, or milestone."); return 1
        path = BRAIN_DIR / "Memory" / "Dates.md"
        if not AUTO_CONFIRM and not confirm(f"Remove the matching row from {rel(path)}? (yes/no): "):
            print("\n  🚫  Aborted (re-run with --yes).\n"); return 0
        _quiet_backup(path)
        status, payload = _remove_table_row(path, parts[2].strip(), after_heading=head)
        if status == "ok":
            ok(f"Removed from {rel(path)}:  {payload}")
        elif status == "none":
            fail(f"No row in {rel(path)} matches '{parts[2]}'."); return 1
        elif status == "multi":
            fail(f"'{parts[2]}' matches {len(payload)} rows - be more specific:")
            for r in payload:
                print(f"       {r}")
            return 1
        else:
            fail(f"Could not edit {rel(path)}."); return 1
    else:
        fail("Usage: memory rm <person|organization|place|decision|event|insight|date> ..."); return 1
    print()
    print(divider())
    print("  🏁  Removed by the engine - backup/.trash holds the recoverable copy.")
    print(divider())
    return 0


def _supersede_status_body(text: str, successor: str = ""):
    """Flip a decision record's body Status to Superseded. Handles BOTH live
    shapes: a `## Status` heading whose value line is a backticked word
    (`Active` -> `Superseded`, backticks preserved) and the legacy
    `**Status:** ...` line. When a successor plain path is given, a
    `Superseded-by:` pointer line is appended right after the status
    (Memory/Memory.md: supersede, don't silently rewrite). Returns
    (new_text, n_replacements); n == 0 means neither shape was found."""
    pointer = f"\nSuperseded-by: {successor}" if successor.strip() else ""
    new, n = re.subn(
        r"(?m)^(#{1,6}[ \t]+Status\b[ \t]*\n+[ \t]*)`[^`\n]+`",
        lambda m: m.group(1) + "`Superseded`" + pointer,
        text, count=1)
    if not n:
        new, n = re.subn(
            r"(?m)^(\*\*Status:\*\*).*$",
            lambda m: m.group(1) + " Superseded" + pointer,
            text, count=1)
    return new, n


def cmd_memory_supersede(parts: list) -> int:
    """♻️  Supersede (preserve, don't delete) a decision through the engine.
      memory supersede decision "<name match>" ["<successor plain path>"]
    -> body Status: Superseded (plus a Superseded-by: pointer when a successor
    is named) plus frontmatter status: "deprecated" (the staleness signal
    search/load/startup read)."""
    header("Supersede Memory Entry", "♻️")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    kind = (parts[0].lower() if parts else "")
    if kind == "decision":
        match = parts[1] if len(parts) > 1 else ""
        if not match.strip():
            fail('Usage: memory supersede decision "<name match>" ["<successor path>"]'); return 1
        successor = parts[2] if len(parts) > 2 else ""
        folder = BRAIN_DIR / "Memory" / "Decisions"
        hits = _find_entry_files(folder, match)
        if not hits:
            fail(f"No decision matches '{match}'."); return 1
        if len(hits) > 1:
            fail(f"'{match}' matches {len(hits)} decisions - be more specific."); return 1
        path = hits[0]
        _quiet_backup(path)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as e:
            fail(f"Could not read {rel(path)}: {e}"); return 1
        new, n = _supersede_status_body(text, successor)
        if not n:
            fail("No `## Status` heading or **Status:** line found to update."); return 1
        # Also flip the frontmatter status - the engine's actual staleness
        # signal (search demotes it; load and startup skip it).
        new, _ = _sub_frontmatter(new, r"^status:\s*.*$", 'status: "deprecated"')
        new, _ = _sub_frontmatter(new, r"^updated:\s*.*$", f"updated: {today}")
        try:
            _write_atomic(path, new)
        except OSError as e:
            fail(f"Could not write {rel(path)}: {e}"); return 1
        ok(f"{rel(path)}  ->  Status: Superseded, frontmatter status: deprecated (record preserved).")
    else:
        fail('Supersede supports only "decision" (sets Status: Superseded). Memory '
             "no longer holds patterns or learned facts - those live in Profile."); return 1
    print()
    print(divider())
    print("  🏁  Superseded by the engine - history preserved, nothing deleted.")
    print(divider())
    return 0


def cmd_memory(rest=None) -> int:
    """🧠 Manage the memory layer: the tiered summary pipeline (Current → Recent
    → Archive) and the per-entry collections (People, Decisions)."""
    rest = rest or []
    subcmd = rest[0].lower() if rest else ""

    if subcmd == "add":
        kind = rest[1].lower() if len(rest) > 1 else ""
        if kind in ("person", "organization", "place", "decision", "event", "insight"):
            if kind == "event" and len(rest) > 3:
                # memory add event "When" "What" - stamp by the event date
                return cmd_memory_add(kind=kind, name=rest[3], when=rest[2])
            return cmd_memory_add(kind=kind, name=rest[2] if len(rest) > 2 else "")
        if kind == "date":
            return cmd_memory_add_row(kind, rest[2:])
        header("Memory", "🧠")
        fail("Usage: memory add <person|organization|place|decision|event|insight|date> ...")
        return 1
    if subcmd == "rm":
        return cmd_memory_rm(rest[1:])
    if subcmd == "supersede":
        return cmd_memory_supersede(rest[1:])

    header("Memory", "🧠")
    if not subcmd:
        print("  Usage:")
        print("    python3 brain.command memory list                  Show all files across tiers")
        print("    python3 brain.command memory status                Show capacity per tier")
        print("    python3 brain.command memory cascade               Enforce tier limits")
        print('    python3 brain.command memory add person "Name"     Scaffold a person file')
        print('    python3 brain.command memory add decision "..."    Scaffold a decision file')
        print('    python3 brain.command memory add date <section> "When" "Event"   Append a date')
        print('    python3 brain.command memory rm <kind> [target] "match" --yes   Remove a row/file')
        print('    python3 brain.command memory supersede decision "..."   Mark a decision superseded (preserve)')
        print("    python3 brain.command memory sync                  Refresh collection index lists")
        print()
        return 0

    if subcmd == "list":
        return _memory_list()
    elif subcmd == "status":
        return _memory_status()
    elif subcmd == "cascade":
        return _memory_cascade()
    elif subcmd == "sync":
        n = _sync_collection_doc_links()
        ok(f"Collection index lists refreshed ({n} doc(s) changed).")
        return 0
    else:
        fail(f"Unknown subcommand: '{subcmd}'")
        print(f"  Valid: list, status, cascade, add, rm, supersede, sync")
        return 1


def cmd_profile_add(kind: str = "", name: str = "") -> int:
    """🪪 Scaffold one entry in an entry-bearing Profile facet from its template.
    `profile add belief "On Religion"` -> Profile/Values/On Religion.md;
    goal|skill|condition similarly. Each gets a fresh id, self/profile
    frontmatter, synced Finder tags, and is registered in its facet's
    auto-maintained entries list. Flat facets are filled in place."""
    header("Add Profile Entry", "🪪")
    kind = (kind or "").strip().lower()
    coll = next((c for c in PROFILE_COLLECTIONS if c[0] == kind), None)
    if not coll:
        fail(f"Unknown kind '{kind}' - use belief, goal, skill, or condition.")
        print("  (Only the entry-bearing facets take entries: Values/Goals/Skills/Health. "
              "Flat facets like Personality are filled in place. Facts about the user "
              "only - events and people go to Memory.)")
        return 1
    _kind, folder, placeholder, tpl = coll
    if not name.strip():
        fail(f'No name provided. Usage: profile add {kind} "Title".'); return 1
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    title = re.sub(r"[\\/:*?\"<>|]", "", name.strip()).strip()
    if not title:
        fail("Name reduces to nothing after removing illegal characters."); return 1
    dest = folder / f"{title}.md"
    if not folder.exists():
        fail(f"Facet folder missing: {rel(folder)}"); return 1
    if dest.exists():
        fail(f"Already exists: {rel(dest)}")
        print(f'  Disambiguate, e.g. "{title} (work)", rather than overwriting.'); return 1
    template = BRAIN_DIR / "Profile" / ".template" / tpl
    if not template.exists():
        fail(f"Template not found: {rel(template)}"); return 1
    rel_folder = folder.relative_to(BRAIN_DIR).as_posix()
    layer = len(folder.relative_to(BRAIN_DIR).parts)
    taken = _all_ids()
    base = f"{ID_PREFIX.get('profile', 'id')}-{_slugify(title)}"
    fid = base; i = 2
    while fid in taken:
        fid = f"{base}-{i}"; i += 1
    tags = ["profile", "self", "sensitive", "enduring"]
    tg = ", ".join(f'"{t}"' for t in tags)
    fm = (f"---\n"
          f'title: "{title}"\n'
          f'description: "{kind.capitalize()} entry: {title}."\n'
          f'status: "active"\n'
          f"tags: [{tg}]\n"
          f"aliases: []\n"
          f"keywords: []\n"
          f"created: {today}\n"
          f"updated: {today}\n"
          f'type: "self"\n'
          f'folder: "profile"\n'
          f"layer: {layer}\n"
          f"policy: false\n"
          f'author: "Tanner Golden"\n'
          f'path: "BRAIN/{rel_folder}/{title}.md"\n'
          f'id: "{fid}"\n'
          f"---\n")
    try:
        body = _strip_frontmatter(template.read_text(encoding="utf-8"))
        body = re.sub(r"<!--\s*FILING INSTRUCTIONS.*?-->\s*", "", body, count=1,
                      flags=re.DOTALL | re.IGNORECASE)
        body = body.replace(placeholder, title)
        dest.write_text(fm + body, encoding="utf-8")
    except OSError as e:
        fail(f"Could not write {rel(dest)}: {e}")
        logging.getLogger("profile").error(e, exc_info=True); return 1
    ok(f"Created {rel(dest)}  (id: {fid})")
    if _set_macos_tags(dest, tags):
        print(f"       🏷  Finder tags synced.")
    relinked = _sync_profile_doc_links()
    if relinked:
        print(f"       🔗  Registered in {folder.name}/{folder.name}.md.")
    print(); print(divider())
    print(f"  🏁  {kind.capitalize()} entry ready - fill it in, then `sync`.")
    print(divider()); return 0


def cmd_profile_rm(parts: list) -> int:
    """🗑  Remove a Profile entry through the engine (soft-remove to .trash; needs
    --yes).  profile rm belief|goal|skill|condition "<match>"  --yes"""
    header("Remove Profile Entry", "🗑")
    kind = (parts[0].lower() if parts else "")
    coll = next((c for c in PROFILE_COLLECTIONS if c[0] == kind), None)
    if not coll:
        fail('Usage: profile rm <belief|goal|skill|condition> "<match>" --yes'); return 1
    _kind, folder, _ph, _tpl = coll
    match = parts[1] if len(parts) > 1 else ""
    if not match.strip():
        fail(f'Usage: profile rm {kind} "<match>" --yes'); return 1
    hits = _find_entry_files(folder, match)
    if not hits:
        fail(f"No {kind} file matches '{match}' in {folder.name}/."); return 1
    if len(hits) > 1:
        fail(f"'{match}' matches {len(hits)} files - be more specific:")
        for h in hits:
            print(f"       - {h.name}")
        return 1
    target = hits[0]
    print(f"  Soft-remove {rel(target)} to .trash/ (recoverable)?")
    if not confirm("Proceed? (yes/no): "):
        print("\n  🚫  Aborted (re-run with --yes).\n"); return 0
    dest = _soft_remove(target)
    if not dest:
        fail(f"Could not remove {rel(target)}."); return 1
    ok(f"{rel(target)}  →  .trash/")
    relinked = _sync_profile_doc_links()
    if relinked:
        print(f"       🔗  Unregistered from {folder.name}/{folder.name}.md.")
    print(); print(divider())
    print("  🏁  Removed by the engine - .trash holds the recoverable copy.")
    print(divider()); return 0


# ── Profile coverage: the read-only scorer behind `profile coverage` ──
# Deterministic, body-only line scoring per the identify design: a line is
# substantive only when it is neither scaffold (frozen CRC fingerprint UNION
# live .template hashes) nor placeholder-shaped (the grammar net below).

_COV_HEADING_RE    = re.compile(r"^\s*#{1,6}\s")
_COV_H2_RE         = re.compile(r"^\s*##\s+(.+?)\s*$")
_COV_COMMENT_RE    = re.compile(r"<!--[^>]*-->")
_COV_UNCONF_RE     = re.compile(r"<!--[^>]*\bunconfirmed\b[^>]*-->")
_COV_FIELD_STUB_RE = re.compile(r"^\s*[-*]\s+\*\*[^:]+:\*\*\s*$")
_COV_FIELD_VAL_RE  = re.compile(r"^\s*[-*]\s+\*\*[^:]+:\*\*\s*(.+?)\s*$")
_COV_TABLE_RE      = re.compile(r"^\s*\|[\s|:\-]*\|?\s*$")
_COV_BRACKET_RE    = re.compile(r"^\[[^\]]+\]$")


def _cov_crc(line: str) -> int:
    """Normalized line fingerprint: strip, collapse internal whitespace, NFC,
    then CRC32 of the UTF-8 bytes. The one normalization shared by the frozen
    PROFILE_SCAFFOLD_CRC constant, the runtime .template union, and scoring."""
    s = unicodedata.normalize("NFC", re.sub(r"\s+", " ", line.strip()))
    return zlib.crc32(s.encode("utf-8"))


def _scaffold_line_hashes(text: str) -> set:
    """CRC set of a file's hashable body lines: skip frontmatter, blanks, and
    headings; strip single-line HTML comments; skip lines empty after the
    strip; hash what remains via _cov_crc. Used to regenerate the frozen
    constant and to union the live Profile/.template/*.md bodies at runtime."""
    out = set()
    body = text
    b = _fm_bounds(text)
    if b:
        nl = text.find("\n", b[1])
        body = text[nl + 1:] if nl != -1 else ""
    for raw in body.splitlines():
        if not raw.strip() or _COV_HEADING_RE.match(raw):
            continue
        s = _COV_COMMENT_RE.sub("", raw)
        if not s.strip():
            continue
        out.add(_cov_crc(s))
    return out


def _cov_template_hashes() -> frozenset:
    """Live hashes of every Profile/.template/*.md body, computed at runtime
    and unioned with the frozen per-file sets, so a freshly scaffolded entry
    (profile add) scores empty until it is actually filled in."""
    out = set()
    tdir = BRAIN_DIR / "Profile" / ".template"
    if tdir.is_dir():
        for f in sorted(tdir.glob("*.md")):
            try:
                out |= _scaffold_line_hashes(_read_text(f))
            except OSError:
                continue
    return frozenset(out)


def _profile_scaffold_crc_render() -> str:
    """Paste-ready PROFILE_SCAFFOLD_CRC literal recomputed from the LIVE 12
    facet files (the documented regeneration path; see the constant's comment)."""
    lines = ["PROFILE_SCAFFOLD_CRC = {"]
    for name, kind in PROFILE_FACETS:
        key = f"{name}.md" if kind == "flat" else f"{name}/{name}.md"
        p = BRAIN_DIR / "Profile" / key
        try:
            hs = sorted(_scaffold_line_hashes(_read_text(p)))
        except OSError:
            hs = []
        lines.append(f'    "{key}": frozenset({{')
        cur = "        "
        for i, n in enumerate(hs):
            tok = f"{n}" + ("" if i == len(hs) - 1 else ", ")
            if len(cur) + len(tok) > 76:
                lines.append(cur.rstrip())
                cur = "        "
            cur += tok
        lines.append(cur.rstrip())
        lines.append("    }),")
    lines.append("}")
    return "\n".join(lines)


def _cov_is_placeholder(stripped: str, scaffold: frozenset) -> bool:
    """The placeholder grammar net (independent of the CRC fingerprint):
    (a) normalized-line CRC32 in the scaffold set; (b) empty bold-field stub;
    (c) field whose value is only a parenthetical or ends with a bare hyphen
    preceded by a space; (d) table separator or all-empty table row; (e) the
    engine's `_None recorded yet._` line; (f) one bracketed token."""
    s = stripped.strip()
    if _cov_crc(stripped) in scaffold:                                  # (a)
        return True
    if _COV_FIELD_STUB_RE.match(stripped):                              # (b)
        return True
    mv = _COV_FIELD_VAL_RE.match(stripped)                              # (c)
    if mv:
        v = mv.group(1)
        if re.fullmatch(r"\(.*\)", v) or v.endswith(" -"):
            return True
    if _COV_TABLE_RE.match(stripped):                                   # (d)
        return True
    if s == "_None recorded yet._":                                     # (e)
        return True
    if _COV_BRACKET_RE.match(s):                                        # (f)
        return True
    return False


def _cov_score_file(path: Path, scaffold: frozenset):
    """Score one Profile file, body only, in the design's order: (1) skip
    frontmatter, blanks, and headings; (2) strip inline HTML comments first
    and count unconfirmed per stripped comment (a comment-only line with the
    token counts toward unconfirmed, never substantive); (3) skip lines inside
    the engine block between PROFILE_LINKS_START/END; (4) placeholder tests;
    (5) otherwise substantive (an unconfirmed comment on a substantive line
    counts it in both tallies). Returns {"substantive", "unconfirmed",
    "sections": [{heading, substantive, unconfirmed, filled}...]} or None if
    the file cannot be read."""
    try:
        text = _read_text(path)
    except OSError:
        return None
    body = text
    b = _fm_bounds(text)
    if b:
        nl = text.find("\n", b[1])
        body = text[nl + 1:] if nl != -1 else ""
    substantive = unconfirmed = 0
    sections, sec, in_block = [], None, False
    for raw in body.splitlines():
        if PROFILE_LINKS_START in raw:
            in_block = True
            continue
        if PROFILE_LINKS_END in raw:
            in_block = False
            continue
        if not raw.strip():
            continue
        if _COV_HEADING_RE.match(raw):
            h2 = _COV_H2_RE.match(raw)
            if h2:
                sec = {"heading": h2.group(1), "substantive": 0, "unconfirmed": 0}
                sections.append(sec)
            continue
        n_unc = len(_COV_UNCONF_RE.findall(raw))
        stripped = _COV_COMMENT_RE.sub("", raw)
        if n_unc:
            unconfirmed += n_unc
            if sec:
                sec["unconfirmed"] += n_unc
        if in_block:
            continue
        if not stripped.strip():
            continue  # comment-only line: never substantive
        if _cov_is_placeholder(stripped, scaffold):
            continue
        substantive += 1
        if sec:
            sec["substantive"] += 1
    for s in sections:
        s["filled"] = s["substantive"] > 0
    return {"substantive": substantive, "unconfirmed": unconfirmed,
            "sections": sections}


def _facet_coverage():
    """Score all 12 registered Profile facets. Read-only, writes nothing ever.
    Returns (facets, target): facets is a list of dicts in registry order
    (facet, kind, path, files, entries, substantive, unconfirmed, depth,
    status, rank, missing, sections, entry_files); rank is 1..12 ascending by
    depth (ties: ascending substantive, then descending unconfirmed, then
    registry order). Status bands: template iff substantive == 0, else sparse
    (depth < 10), partial (depth < 30), developed (>= 30). The target is
    "Working Style" while its status is template (the standing first target,
    baked in: the least invasive, most AI-actionable facet leads until it
    holds real content), else the rank-1 facet."""
    tpl = _cov_template_hashes()
    profile = BRAIN_DIR / "Profile"
    facets = []
    for name, kind in PROFILE_FACETS:
        key = f"{name}.md" if kind == "flat" else f"{name}/{name}.md"
        fpath = profile / key
        scaffold = frozenset(PROFILE_SCAFFOLD_CRC.get(key, frozenset()) | tpl)
        files = substantive = unconfirmed = 0
        sections, entry_files = [], []
        missing = not fpath.is_file()
        if not missing:
            r = _cov_score_file(fpath, scaffold)
            if r is None:
                missing = True
            else:
                files += 1
                substantive += r["substantive"]
                unconfirmed += r["unconfirmed"]
                sections = r["sections"]
        if kind == "folder":
            folder = profile / name
            if folder.is_dir():
                for f in sorted(folder.glob("*.md")):
                    if f.name == f"{name}.md" or f.name.startswith("."):
                        continue
                    er = _cov_score_file(f, scaffold) or \
                        {"substantive": 0, "unconfirmed": 0, "sections": []}
                    files += 1
                    entry_files.append({
                        "name": f.name,
                        "substantive": er["substantive"],
                        "unconfirmed": er["unconfirmed"],
                        "depth": er["substantive"] - er["unconfirmed"]})
                    substantive += er["substantive"]
                    unconfirmed += er["unconfirmed"]
        depth = substantive - unconfirmed
        if substantive == 0:
            status = "template"
        elif depth < 10:
            status = "sparse"
        elif depth < 30:
            status = "partial"
        else:
            status = "developed"
        facets.append({"facet": name, "kind": kind, "path": f"Profile/{key}",
                       "files": files, "entries": len(entry_files),
                       "substantive": substantive, "unconfirmed": unconfirmed,
                       "depth": depth, "status": status, "missing": missing,
                       "sections": sections, "entry_files": entry_files})
    order = {f["facet"]: i for i, f in enumerate(facets)}
    ranked = sorted(facets, key=lambda f: (f["depth"], f["substantive"],
                                           -f["unconfirmed"], order[f["facet"]]))
    for i, f in enumerate(ranked, 1):
        f["rank"] = i
    ws = next(f for f in facets if f["facet"] == "Working Style")
    target = "Working Style" if ws["status"] == "template" else ranked[0]["facet"]
    return facets, target


def _cov_json_row(f: dict) -> dict:
    """One facet as the JSON contract's base object (missing only when true)."""
    row = {k: f[k] for k in ("facet", "kind", "path", "files", "entries",
                             "substantive", "unconfirmed", "depth", "status",
                             "rank")}
    if f["missing"]:
        row["missing"] = True
    return row


def cmd_profile_coverage(parts: list = None, json_out: bool = False) -> int:
    """🪪 Read-only coverage report over the 12 Profile facets: how substantive
    each is, what is unconfirmed, and which facet the identify skill should
    interview next.  profile coverage [FACET] [--json]  FACET is
    case-insensitive and hyphen/space tolerant; unknown facet exits 2 with the
    valid list; a missing facet file scores zeros with a warning, never a
    crash. Standing first-target rule: Working Style is the target while its
    status is `template`, else the rank-1 (thinnest) facet. Writes nothing,
    ever, and is deliberately absent from _is_mutating's profile set."""
    parts = [p for p in (parts or []) if not p.startswith("--")]
    facet_arg = " ".join(parts).strip()
    facets, target = _facet_coverage()
    ws_rule = target == "Working Style" and \
        next(f for f in facets if f["facet"] == "Working Style")["status"] == "template"
    if facet_arg:
        want = re.sub(r"\s+", " ", facet_arg.replace("-", " ").strip().lower())
        hit = next((f for f in facets if f["facet"].lower() == want), None)
        if hit is None:
            fail(f"Unknown facet: '{facet_arg}'")
            print(f"  Valid: {', '.join(n for n, _k in PROFILE_FACETS)}")
            return 2
        if json_out:
            row = _cov_json_row(hit)
            row["sections"] = hit["sections"]
            row["entry_files"] = hit["entry_files"]
            print(json.dumps(row, indent=2))
            return 0
        header("Profile Coverage", "🪪")
        if hit["missing"]:
            warn(f"Facet file missing: {hit['path']} (scored as zeros).")
        print(f"  {'Rank':>4}  {'Facet':<14}  {'Kind':<6}  {'Files':>5}  "
              f"{'Entries':>7}  {'Subst':>5}  {'Unconf':>6}  {'Depth':>5}  Status")
        print(f"  {'-'*4}  {'-'*14}  {'-'*6}  {'-'*5}  {'-'*7}  {'-'*5}  {'-'*6}  {'-'*5}  {'-'*9}")
        print(f"  {hit['rank']:>4}  {hit['facet']:<14}  {hit['kind']:<6}  "
              f"{hit['files']:>5}  {hit['entries']:>7}  {hit['substantive']:>5}  "
              f"{hit['unconfirmed']:>6}  {hit['depth']:>5}  {hit['status']}")
        if hit["sections"]:
            print()
            width = max(len(s["heading"]) for s in hit["sections"])
            width = max(width, len("Section"))
            print(f"  {'Section':<{width}}  {'Subst':>5}  {'Unconf':>6}  Filled")
            print(f"  {'-'*width}  {'-'*5}  {'-'*6}  {'-'*6}")
            for s in hit["sections"]:
                print(f"  {s['heading']:<{width}}  {s['substantive']:>5}  "
                      f"{s['unconfirmed']:>6}  {'yes' if s['filled'] else 'no'}")
        if hit["kind"] == "folder":
            print()
            if hit["entry_files"]:
                print(f"  Entries ({len(hit['entry_files'])}):")
                for e in hit["entry_files"]:
                    print(f"    📄  {e['name']}  (subst {e['substantive']}, "
                          f"unconf {e['unconfirmed']}, depth {e['depth']})")
            else:
                print("  Entries: none yet.")
        print()
        print(divider())
        note = "  (standing rule: Working Style leads while template)" if ws_rule else ""
        print(f"  🎯  Target: {target}{note}")
        print(divider())
        return 0
    if json_out:
        out = {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
               "target": target,
               "facets": [_cov_json_row(f) for f in facets]}
        print(json.dumps(out, indent=2))
        return 0
    header("Profile Coverage", "🪪")
    for f in facets:
        if f["missing"]:
            warn(f"Facet file missing: {f['path']} (scored as zeros).")
    print(f"  {'Rank':>4}  {'Facet':<14}  {'Kind':<6}  {'Files':>5}  "
          f"{'Entries':>7}  {'Subst':>5}  {'Unconf':>6}  {'Depth':>5}  Status")
    print(f"  {'-'*4}  {'-'*14}  {'-'*6}  {'-'*5}  {'-'*7}  {'-'*5}  {'-'*6}  {'-'*5}  {'-'*9}")
    for f in sorted(facets, key=lambda x: x["rank"]):
        print(f"  {f['rank']:>4}  {f['facet']:<14}  {f['kind']:<6}  "
              f"{f['files']:>5}  {f['entries']:>7}  {f['substantive']:>5}  "
              f"{f['unconfirmed']:>6}  {f['depth']:>5}  {f['status']}")
    print()
    print(divider())
    note = "  (standing rule: Working Style leads while template)" if ws_rule else ""
    print(f"  🎯  Target: {target}{note}")
    print(divider())
    return 0


def cmd_profile(rest=None, json_out: bool = False) -> int:
    """🪪 Manage the entry-bearing Profile facets (add/remove/sync per-item
    entries in Values, Goals, Skills, Health) and report facet fill levels
    (coverage). The flat facets (Biography, Personality, Relationships,
    Finances, Lifestyle, ...) are filled in place and take no entries."""
    rest = rest or []
    subcmd = rest[0].lower() if rest else ""
    if subcmd == "add":
        kind = rest[1].lower() if len(rest) > 1 else ""
        return cmd_profile_add(kind=kind, name=rest[2] if len(rest) > 2 else "")
    if subcmd == "rm":
        return cmd_profile_rm(rest[1:])
    if subcmd == "sync":
        n = _sync_profile_doc_links()
        ok(f"Profile facet entry lists refreshed ({n} doc(s) changed)."); return 0
    if subcmd == "coverage":
        # Read-only coverage report (the identify skill's targeting call).
        # Deliberately NOT in _is_mutating's profile set: writes nothing, ever.
        return cmd_profile_coverage(rest[1:], json_out=json_out)
    header("Profile", "🪪")
    if not subcmd:
        print("  Usage:")
        print('    python3 brain.command profile add belief "On Religion"           Scaffold a belief (Values/)')
        print('    python3 brain.command profile add goal|skill|condition "Title"   Scaffold a goal/skill/condition')
        print('    python3 brain.command profile rm <kind> "match" --yes            Soft-remove an entry')
        print("    python3 brain.command profile sync                               Refresh facet entry lists")
        print('    python3 brain.command profile coverage ["Facet"] [--json]        Read-only facet fill report + next target')
        print()
        print("  Entry-bearing facets: Values (beliefs), Goals, Skills, Health (conditions).")
        print("  Flat facets (Biography, Personality, Relationships, Finances, Lifestyle, Working Style, Preferences, Focus) are filled in place.")
        return 0
    fail(f"Unknown subcommand: '{subcmd}'")
    print("  Valid: add, rm, sync, coverage"); return 1



# ══════════════════════════════════════════════════════════
#  Menu
# ══════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════
#  SKILL - package unpackaged skills into .skill archives
# ══════════════════════════════════════════════════════════

SKILLS_DIR = SYSTEM_DIR / "Skills"                       # root: Skills.md + packaged .skill artifacts
SKILLS_SRC = SKILLS_DIR / ".unpackaged"                  # hidden: skill sources (no wikilinks, not walked)

# Junk never shipped inside a package (transient artifacts per Instructions
# Section 11; .skill excluded so a package never nests an older package).
_SKILL_EXCLUDE_DIRS  = {"__pycache__", ".git", ".obsidian", ".trash"}
_SKILL_EXCLUDE_FILES = {".DS_Store", "Thumbs.db"}  # .gitkeep ships (develop v1.5.0): empty-folder markers are skill content
_SKILL_EXCLUDE_EXTS  = {".pyc", ".pyo", ".skill", ".swp"}


def _skill_dirs() -> list:
    """Skill source directories in Skills/.unpackaged/ (anything with a SKILL.md,
    plus folders without one so validation can flag them)."""
    if not SKILLS_SRC.is_dir():
        return []
    return sorted([d for d in SKILLS_SRC.iterdir()
                   if d.is_dir() and not d.name.startswith(".")],
                  key=lambda d: d.name.lower())


def _skill_excluded(path: Path) -> bool:
    if any(part in _SKILL_EXCLUDE_DIRS for part in path.parts):
        return True
    if path.name in _SKILL_EXCLUDE_FILES or path.name.startswith("._"):
        return True
    return path.suffix.lower() in _SKILL_EXCLUDE_EXTS


def _skill_meta_team(skill_md: Path) -> str:
    """The skill's declared `metadata.team`, or "" if none. parse_frontmatter is
    a flat col-0 parser that returns the nested `metadata:` block as an empty
    string, so the team pointer (an indented sub-key) is read here directly from
    the frontmatter text: enter the `metadata:` block, then take its `team:`
    line, stopping at the first dedent to a new top-level key."""
    try:
        content = skill_md.read_text(encoding="utf-8")
    except OSError:
        return ""
    if not content.startswith("---"):
        return ""
    end = content.find("---", 3)
    if end == -1:
        return ""
    in_meta = False
    for line in content[3:end].splitlines():
        if re.match(r'^metadata:\s*$', line):
            in_meta = True
            continue
        if in_meta:
            if re.match(r'^\S', line):  # dedent: the metadata block has ended
                break
            m = re.match(r'^\s+team:\s*(.*)', line)
            if m:
                return m.group(1).strip().strip('"\'')
    return ""


def _skill_meta_block(skill_md: Path) -> dict:
    """The SKILL.md indented `metadata:` block as a flat dict (team, version, id,
    author, status). parse_frontmatter returns the nested block as empty, so its
    sub-keys are read here from the frontmatter text, like _skill_meta_team."""
    out = {}
    try:
        content = skill_md.read_text(encoding="utf-8")
    except OSError:
        return out
    if not content.startswith("---"):
        return out
    end = content.find("---", 3)
    if end == -1:
        return out
    in_meta = False
    for line in content[3:end].splitlines():
        if re.match(r'^metadata:\s*$', line):
            in_meta = True
            continue
        if in_meta:
            if re.match(r'^\S', line):
                break
            m = re.match(r'^\s+([A-Za-z0-9_-]+):\s*(.*)$', line)
            if m:
                out[m.group(1).strip()] = m.group(2).strip().strip('"\'')
    return out


def _skill_validate(d: Path) -> tuple:
    """The full Gate-1 skill check set (references/validation.md): the Agent
    Skills manifest spec, the BRAIN skill layout (required files and folders, no
    `agents/`/`scripts/`), version consistency across every site, the namesake
    and Changelog BRAIN frontmatter, no em dash, and the canonical skeleton's
    fixed points. Returns (errors, warnings); errors block packaging. The
    qa-auditor (Gate 2) still judges what code cannot (prose, full slot order)."""
    import re as _re
    errors, warnings = [], []
    skill_md = d / "SKILL.md"
    if not skill_md.is_file():
        return ([f"no SKILL.md at {rel(d)}/SKILL.md"], warnings)
    # Exactly one SKILL.md per bundle: a second one (e.g. a template manifest
    # named SKILL.md) ships two manifests and the install fails on claude.ai.
    # Template manifests are named t-SKILL.md, which this check ignores. (rc-0002)
    strays = [str(f.relative_to(d)) for f in d.rglob("*")
              if f.is_file() and f != skill_md and f.name.lower() == "skill.md"]
    if strays:
        errors.append(
            "a skill must contain exactly one SKILL.md, at its root; found a "
            f"second manifest at {', '.join(strays)} "
            "(a template manifest must be named t-SKILL.md, not SKILL.md)")
    fm = parse_frontmatter(skill_md) or {}
    name, desc = str(fm.get("name", "") or ""), str(fm.get("description", "") or "")
    if not name:
        errors.append("SKILL.md frontmatter is missing `name`")
    if not desc:
        errors.append("SKILL.md frontmatter is missing `description`")
    if desc and len(desc) > 1024:
        errors.append(f"description is {len(desc)} chars (spec max 1024)")
    if name:
        if not _re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"`name: {name}` is not spec-conforming "
                          "(kebab-case, max 64 chars, no leading/trailing hyphen)")
        elif name != d.name:
            # Spec requires name == directory name; conforming runtimes reject
            # mismatches, so this blocks rather than warns.
            errors.append(f"`name: {name}` does not match folder name `{d.name}`")
    if "_" in d.name:
        warnings.append("folder name contains underscores (Constitution 2.6)")
    # Unpackaged sources carry no wikilinks (Skills.md layout policy): they are
    # hidden from Obsidian, so a wikilink there is dead weight that breaks on
    # install anyway.
    wl = []
    for f in sorted(d.rglob("*.md")):
        try:
            if "[[" in _read_text(f):
                wl.append(str(f.relative_to(d)))
        except OSError as e:
            errors.append(f"unreadable file {f.relative_to(d)}: {e}")
    if wl:
        warnings.append(f"wikilinks found in {', '.join(wl[:3])}{'…' if len(wl) > 3 else ''} - skill sources carry none")
    # metadata.team, when named, must resolve to a staffed team roster somewhere
    # in the shared agent library (any AGENT_HOMES home). A skill that points at
    # a deleted or misspelled team would dispatch into the void, so the gate
    # refuses its own broken pointer here. This check's absence is exactly how a
    # skill's dangling team reference once survived its own validator. Absent
    # metadata.team is fine: a skill may run its pipeline inline with no team.
    team_ref = _skill_meta_team(skill_md)
    if team_ref:
        rosters = {nm for home in AGENT_HOMES for _, nm in _team_files(home)}
        if team_ref not in rosters:
            errors.append(
                f"`metadata.team: {team_ref}` does not resolve to a staffed team "
                "roster in the shared agent library; point it at an existing team "
                "or drop the key to run inline")
    # name must not contain 'claude'/'anthropic' (Agent Skills spec)
    if name and re.search(r"claude|anthropic", name, re.I):
        errors.append(f"`name: {name}` must not contain 'claude' or 'anthropic' (Agent Skills spec)")
    # SKILL.md frontmatter must carry license, allowed-tools, and a metadata block
    for key in ("license", "allowed-tools"):
        if not str(fm.get(key, "") or "").strip():
            errors.append(f"SKILL.md frontmatter is missing `{key}`")
    meta = _skill_meta_block(skill_md)
    if not meta:
        errors.append("SKILL.md frontmatter is missing the `metadata` block")
    # Required BRAIN skill layout: namesake + License.txt + Changelog.md, the
    # assets/references/templates folders, and no agents//scripts/ in source
    namesakes = [f for f in d.glob("*.md")
                 if f.name != "SKILL.md" and f.stem.lower() == d.name.lower()]
    namesake = namesakes[0] if namesakes else None
    for req in ("License.txt", "Changelog.md"):
        if not (d / req).is_file():
            errors.append(f"required file missing: {req}")
    if namesake is None:
        errors.append(f"required namesake doc missing: {d.name.capitalize()}.md")
    for sub in ("assets", "references", "templates"):
        if not (d / sub).is_dir():
            errors.append(f"required folder missing: {sub}/")
    for bad in ("agents", "scripts"):
        if (d / bad).is_dir():
            errors.append(f"`{bad}/` is not allowed in a skill source "
                          "(agents are vendored only at Publish; scripts live in brain.command)")
    # Version consistency: metadata.version == Changelog Current Version ==
    # Changelog frontmatter == namesake (the namesake versions with the skill)
    vn = lambda x: str(x or "").strip().strip('"').strip("'").strip()
    sk_ver = vn(meta.get("version"))
    if not sk_ver:
        # A skill with no declared version has no version-agreement anchor at
        # all: every drift check below would silently skip. Error, not skip.
        errors.append("SKILL.md `metadata.version` is missing or empty "
                      "(version agreement cannot be verified without it)")
    else:
        clog = d / "Changelog.md"
        if clog.is_file():
            try:
                ctext = _read_text(clog)
            except OSError as e:
                errors.append(f"Changelog.md cannot be read: {e}")
                ctext = ""
            cur = re.search(r"##\s+Current Version\b.*?\*\*`([^`]+)`\*\*", ctext, re.S)
            if not cur:
                errors.append("Changelog.md has no readable `Current Version` "
                              "line (version agreement cannot be verified)")
            elif vn(cur.group(1)) != sk_ver:
                errors.append(f"version drift: SKILL.md `{sk_ver}` != Changelog Current Version `{vn(cur.group(1))}`")
            cfv = vn((parse_frontmatter(clog) or {}).get("version"))
            if cfv and cfv != sk_ver:
                errors.append(f"version drift: SKILL.md `{sk_ver}` != Changelog.md frontmatter version `{cfv}`")
        if namesake is not None:
            nfv = vn((parse_frontmatter(namesake) or {}).get("version"))
            if not nfv:
                errors.append(f"{namesake.name} has no readable `version:` in its "
                              "frontmatter (version agreement cannot be verified)")
            elif nfv != sk_ver:
                errors.append(f"version drift: SKILL.md `{sk_ver}` != {namesake.name} version `{nfv}`")
    # Namesake and Changelog are BRAIN documentation nodes: require the schema fields
    for doc in (namesake, d / "Changelog.md"):
        if doc and doc.is_file():
            dfm = parse_frontmatter(doc) or {}
            miss = [k for k in REQUIRED_FIELDS if k not in dfm]
            if "version" not in dfm:
                miss.append("version")
            if miss:
                errors.append(f"{doc.name} is missing BRAIN frontmatter field(s): {', '.join(miss)}")
    # No em dash (U+2014) anywhere in the source (Constitution 9.1). Every
    # packaged file that decodes as UTF-8 text is scanned, whatever its
    # extension, so no text format dodges the ban; true binaries skip via the
    # decode test itself.
    em = []
    for f in sorted(d.rglob("*")):
        if not f.is_file() or _skill_excluded(f):
            continue
        try:
            raw = f.read_bytes()
        except OSError as e:
            errors.append(f"unreadable file {f.relative_to(d)}: {e}")
            continue
        try:
            ftext = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue  # binary content: nothing textual to scan
        if EM_DASH in ftext:
            em.append(str(f.relative_to(d)))
    if em:
        errors.append(f"em dash (U+2014) in {', '.join(em[:3])}{'…' if len(em) > 3 else ''}"
                      " - banned by Constitution 9.1; use ' - ' or punctuation")
    # Canonical skeleton fixed points (references/architecture.md): every skill
    # ends with Boundaries; Bootstrap is develop-only. Full slot order is Gate 2.
    try:
        body = _read_text(skill_md)
    except OSError as e:
        errors.append(f"SKILL.md cannot be read: {e}")
        body = ""
    if not re.search(r"^##\s+Boundaries\b", body, re.M):
        errors.append("SKILL.md has no `## Boundaries` section (required by the canonical skeleton)")
    if d.name != "develop" and re.search(r"^##\s+Bootstrap\b", body, re.M):
        errors.append("`## Bootstrap` is develop-only; the canonical skeleton ends at Boundaries for other skills")
    return (errors, warnings)


def _skill_package_one(d: Path) -> int:
    """Validate then zip one skill folder to Skills/<name>.skill (folder at
    archive root, junk excluded). Returns 0 on success."""
    import zipfile
    errors, warnings = _skill_validate(d)
    for w in warnings:
        warn(f"{d.name}: {w}")
    if errors:
        for e in errors:
            fail(f"{d.name}: {e}")
        return 1
    out = SKILLS_DIR / f"{d.name}.skill"
    if out.exists() and not confirm(f"{rel(out)} exists. Overwrite? (yes/no): "):
        warn(f"{d.name}: skipped (package exists)")
        return 1
    files = sorted(f for f in d.rglob("*")
                   if f.is_file() and not f.is_symlink() and not _skill_excluded(f))
    if not files:
        fail(f"{d.name}: nothing to package")
        return 1
    try:
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in files:
                arc = f"{d.name}/{f.relative_to(d)}"
                if (f.parent == d and f.suffix == ".md"
                        and f.stem.lower() == d.name.lower()):
                    # Namesake doc: vault YAML frontmatter never ships
                    # (develop v1.7.1) - the guide travels, the metadata stays.
                    text = _read_text(f)
                    if text.startswith("---\n"):
                        end = text.find("\n---\n", 4)
                        if end != -1:
                            text = text[end + 5:].lstrip("\n")
                    zf.writestr(arc, text)
                    continue
                zf.write(f, arc)
    except OSError as e:
        fail(f"{d.name}: packaging failed: {e}")
        logging.getLogger("skill").error(e, exc_info=True)
        return 1
    size_kb = out.stat().st_size / 1024
    ok(f"{d.name}  →  {rel(out)}  ({len(files)} files, {size_kb:.0f} KB)")
    return 0


def _skill_list() -> int:
    dirs = _skill_dirs()
    if not dirs:
        warn(f"No skill sources in {rel(SKILLS_SRC)}.")
        return 0
    print(f"  {len(dirs)} skill source(s) in {rel(SKILLS_SRC)}:\n")
    for d in dirs:
        errors, warnings = _skill_validate(d)
        n_files = sum(1 for f in d.rglob("*") if f.is_file() and not _skill_excluded(f))
        pkg = SKILLS_DIR / f"{d.name}.skill"
        if pkg.exists():
            newest = max((f.stat().st_mtime for f in d.rglob("*")
                          if f.is_file() and not _skill_excluded(f)),
                         default=0)
            pkg_state = ("packaged" if pkg.stat().st_mtime >= newest
                         else "package STALE (folder changed since packaging)")
        else:
            pkg_state = "not packaged"
        state = "valid" if not errors else f"INVALID ({len(errors)} error(s))"
        print(f"    {d.name}  -  {n_files} files  -  {state}  -  {pkg_state}")
        for e in errors:
            fail(e)
        for w in warnings:
            warn(w)
    print()
    print("  Package with: skill package <name>   |   skill package all")
    return 0


def _skill_validate_cmd(target: str = "") -> int:
    """Validate skill source(s) against the Agent Skills spec without packaging.
    Read-only and shared: every skill, current or future, is checked from one
    place. Skills carry no scripts/ of their own - validation lives here, so it
    tracks the live BRAIN rather than a copy frozen inside each skill."""
    header("Skill Validator", "🔎")
    dirs = _skill_dirs()
    if not dirs:
        warn(f"No skill sources in {rel(SKILLS_SRC)}.")
        return 1
    t = (target or "").strip()
    if t and t.lower() != "all":
        match = next((d for d in dirs if d.name == t), None) or \
                next((d for d in dirs if d.name.lower() == t.lower()), None)
        if match is None:
            fail(f"No skill folder named '{t}'. Available: {', '.join(d.name for d in dirs)}")
            return 1
        dirs = [match]
    bad = 0
    for d in dirs:
        errors, warnings = _skill_validate(d)
        for e in errors:
            fail(f"{d.name}: {e}")
        for w in warnings:
            warn(f"{d.name}: {w}")
        if errors:
            bad += 1
        elif not warnings:
            print(f"  ✅  {d.name}: valid")
    print()
    print(divider())
    print(f"  🏁  {len(dirs) - bad}/{len(dirs)} valid."
          + ("" if not bad else f"  {bad} with error(s)."))
    print(divider())
    return 1 if bad else 0


def cmd_skill(subcmd: str = "", name: str = "") -> int:
    """📦 List, validate, or package the skill sources in Skills/.unpackaged/.
    `skill` / `skill list` shows each folder with validation + package state.
    `skill validate <name|all>` runs the spec check without packaging (shared:
    skills carry no scripts/ of their own). `skill package <name>` zips one
    folder to Skills/<name>.skill after a spec-level validation; `skill package
    all` does every valid folder. The .skill is a zip with the skill folder at
    its root, junk excluded - the install format for Claude."""
    sub = (subcmd or "").strip().lower()
    if sub == "validate":
        return _skill_validate_cmd(name)
    header("Skill Packager", "📦")
    if sub in ("", "list"):
        rc = _skill_list()
        if sub == "" and sys.stdin.isatty() and _skill_dirs():
            choice = input("\n  Package which skill? (name, 'all', or Enter to exit): ").strip()
            if choice:
                return cmd_skill("package", choice)
        return rc
    if sub != "package":
        fail(f"Unknown subcommand '{subcmd}'. Use: skill | skill list | skill validate <name|all> | skill package <name|all>")
        return 1
    dirs = _skill_dirs()
    if not dirs:
        warn(f"No skill sources in {rel(SKILLS_SRC)}.")
        return 1
    target = (name or "").strip()
    if not target:
        fail("Name required: skill package <name>  (or: skill package all)")
        return 1
    if target.lower() == "all":
        results = [_skill_package_one(d) for d in dirs]
        failed = sum(1 for r in results if r != 0)
        print()
        print(divider())
        print(f"  🏁  Packaged {len(results) - failed}/{len(results)}."
              + ("" if not failed else f"  {failed} failed - see above."))
        print(divider())
        if failed == 0:
            print("  Run `sync` so the new .skill files get Finder tags (Article 3.5).")
        return 1 if failed else 0
    match = next((d for d in dirs if d.name == target), None) or \
            next((d for d in dirs if d.name.lower() == target.lower()), None)
    if match is None:
        fail(f"No skill folder named '{target}'. Available: {', '.join(d.name for d in dirs)}")
        return 1
    rc = _skill_package_one(match)
    if rc == 0:
        print()
        print(divider())
        print(f"  🏁  Install from {rel(SKILLS_DIR / (match.name + '.skill'))} "
              "(Cowork: Save skill; claude.ai: Settings > Capabilities).")
        print(divider())
        print("  Run `sync` so the new .skill gets Finder tags (Article 3.5).")
    return rc


# ══════════════════════════════════════════════════════════
#  AGENT LIBRARY COMMANDS - validate single-file agent specs,
#  team rosters, and the federated agent library; regenerate
#  the derived agent catalog. The library is ONE logical
#  namespace across THREE domain homes: Ventures/Agent Resources
#  (AR) (the corporate workforce), Inbox/Faculties (the standing teams:
#  Research, Discovery, Development, Editorial, Design), and Library (the Library's own
#  staff). One role key and one
#  spoken agent-name per agent, unique across the union of all
#  homes - the name is the address, so a collision would misroute
#  a "Hey <name>". Agents are full BRAIN documents, linted like any
#  content; the derived catalog is the machine-managed JSON at
#  System/Data/agent-catalog.json, refreshed in lockstep
#  with the manifest by save_index (regenerate on demand with
#  `agents catalog`).
# ══════════════════════════════════════════════════════════

AR_DIR      = BRAIN_DIR / "Ventures" / "Agent Resources (AR)"
FACULTIES_DIR = BRAIN_DIR / "Inbox" / "Faculties"
LIBRARY_DIR = BRAIN_DIR / "Library"
AGENT_HOMES = [AR_DIR, FACULTIES_DIR, LIBRARY_DIR]
# Direct subfolders of a home that are NOT team/department folders.
_AGENT_NONTEAM_DIRS = {"assets", "references", "templates", "scripts"}
# The nine required sections of a single-file agent spec, Identity first.
# Extra sections (e.g. Stance) are allowed; these nine are the floor.
AGENT_SECTIONS = [
    "Identity", "Role & Objective", "Inputs", "Method", "Output contract",
    "Examples", "Boundaries", "Recovery", "Non-negotiables",
]
# Lead-tools doctrine ("Leads orchestrate, they do not labor", AR charter):
# a ★-prefixed lead holds exactly the orchestration set. The one documented
# solo exception is the Library's ★ Librarian, which stewards its own
# collection and holds the labor tools itself. Among non-star specialists,
# only the Development team's Full-Stack Engineer may hold Write/Edit.
LEAD_TOOLS = frozenset({"Read", "Grep", "Glob", "Task"})
LIBRARIAN_TOOLS = frozenset({"Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task"})
STAR_PREFIX = "★"


def _agent_tools(fm: dict) -> set:
    """The frontmatter `tools:` line as a set of tool names (order-insensitive,
    whitespace-tolerant). Empty set when the field is missing."""
    return {t.strip() for t in str(fm.get("tools", "") or "").split(",") if t.strip()}


def _agent_text(path: Path) -> str:
    """Body text of an agent or roster spec; empty string on read error."""
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _team_dirs(home: Path):
    """Yield each real team/department folder in a library home: a direct,
    non-hidden subdirectory that is not a shared content folder. A FLAT home,
    one that is itself a single team (its own namesake carries `members`),
    yields the home itself, so a standing team needs no redundant domain
    wrapper."""
    if not home.is_dir():
        return
    flat_roster = home / f"{home.name}.md"
    if flat_roster.is_file() and "members" in (parse_frontmatter(flat_roster) or {}):
        yield home
        return
    for d in sorted(home.iterdir()):
        if d.is_dir() and not d.name.startswith(".") \
                and d.name.lower() not in _AGENT_NONTEAM_DIRS:
            yield d


def _agent_files(home: Path):
    """Yield (agent_path, team_name) for every agent spec in a home: a .md file
    inside a team folder that is not that folder's namesake roster."""
    for team in _team_dirs(home):
        for f in sorted(team.glob("*.md")):
            if f.stem.lower() != team.name.lower():
                yield f, team.name


def _team_files(home: Path):
    """Yield (roster_path, team_name) for each team folder's namesake roster. A
    department namesake counts as a roster only once it carries `members`;
    before that it is an unstaffed department's folder doc (linted as a normal
    BRAIN doc, not team-validated), so the workforce can hold a department that
    exists but has not been staffed with its lead yet."""
    for team in _team_dirs(home):
        roster = team / f"{team.name}.md"
        if roster.is_file() and "members" in (parse_frontmatter(roster) or {}):
            yield roster, team.name


def _agent_validate(path: Path) -> tuple:
    """Validate one single-file agent spec against the agent standard
    (references/agent-standard.md) - an external format, not the BRAIN schema.
    Returns (errors, warnings). Cross-file name and role uniqueness is the
    library pass's job, not this one's."""
    errors, warnings = [], []
    text = _agent_text(path)
    fm = parse_frontmatter(path) or {}
    stem = path.stem
    title = str(fm.get("title", "") or "").strip()
    if not title:
        errors.append("frontmatter `title` (the role) is missing")
    elif title != stem:
        errors.append(f"`title: {title}` does not match the file name `{stem}`")
    # The role is the file `title`, equal to the file stem (Title Case with
    # spaces, "Chief Executive Officer"; a team lead carries a leading star).
    # The `name` field holds the spoken American first name, the addressing
    # handle ("Hey Jonathan"); it is no longer the role key.
    if not str(fm.get("name", "") or "").strip():
        errors.append("frontmatter `name` (the spoken name) is missing")
    if not str(fm.get("description", "") or "").strip():
        errors.append("frontmatter `description` (the routing key) is missing")
    for sec in AGENT_SECTIONS:
        if not re.search(r"(?im)^#{1,6}\s+" + re.escape(sec) + r"\b", text):
            errors.append(f"missing required section `## {sec}`")
    # Identity block must carry Name / Persona / Voice lines under its heading.
    if re.search(r"(?im)^#{1,6}\s+Identity\b", text):
        for field in ("Name", "Persona", "Voice"):
            if not re.search(rf"(?im)^\s*[-*]\s*\*\*{field}", text):
                warnings.append(f"Identity block has no **{field}:** line")
    # Lead-tools enforcement: a ★-prefixed lead holds exactly LEAD_TOOLS;
    # the sole documented exception is the Library's ★ Librarian, which holds
    # LIBRARIAN_TOOLS. A non-star specialist never holds Write or Edit unless
    # it is the Development team's Full-Stack Engineer.
    tools = _agent_tools(fm)
    role = title or stem
    if stem.startswith(STAR_PREFIX):
        if role == "★ Librarian" and path.parent == LIBRARY_DIR:
            if tools != set(LIBRARIAN_TOOLS):
                errors.append(
                    "★ Librarian tools must be exactly "
                    f"`{', '.join(sorted(LIBRARIAN_TOOLS))}` (its documented solo "
                    f"set); found `{', '.join(sorted(tools)) or '(none)'}`")
        elif tools != set(LEAD_TOOLS):
            errors.append(
                "a ★ lead's tools must be exactly "
                f"`{', '.join(sorted(LEAD_TOOLS))}` (leads orchestrate, they do "
                f"not labor); found `{', '.join(sorted(tools)) or '(none)'}`")
    elif tools & {"Write", "Edit"} and role != "Full-Stack Engineer":
        errors.append(
            "a non-lead agent may not hold Write or Edit (only the Development "
            f"team's Full-Stack Engineer may); found `{', '.join(sorted(tools))}`")
    if EM_DASH in text:
        errors.append(f"contains {text.count(EM_DASH)} em dash(es); use ' - ' or punctuation")
    return errors, warnings


def _parse_members(fm: dict):
    """Normalise a roster's `members` field to a list. parse_frontmatter only
    expands tags/aliases/keywords as lists, so members arrives as a raw
    '[a, b]' inline-array string and is split here."""
    raw = fm.get("members", "")
    if isinstance(raw, list):
        return [str(m).strip() for m in raw if str(m).strip()]
    return [m.strip().strip("\"'") for m in str(raw).strip("[]").split(",") if m.strip()]


def _team_validate(path: Path, known_roles=None) -> tuple:
    """Validate one team roster. Returns (errors, warnings). When known_roles is
    supplied, every member must resolve to an agent file in the library."""
    errors, warnings = [], []
    text = _agent_text(path)
    fm = parse_frontmatter(path) or {}
    for key in ("title", "description", "lead"):
        if not str(fm.get(key, "") or "").strip():
            errors.append(f"frontmatter `{key}` is missing")
    members = _parse_members(fm)
    if not members:
        errors.append("frontmatter `members` is missing or empty")
    lead = str(fm.get("lead", "") or "").strip()
    if lead and members and lead not in members:
        errors.append(f"`lead: {lead}` is not listed in `members`")
    # Roster/star agreement: the lead carries the star prefix, and a team
    # holds exactly one ★-prefixed member (its lead).
    if lead and not lead.startswith(STAR_PREFIX + " "):
        errors.append(f"`lead: {lead}` does not start with the star prefix '★ '")
    if members:
        stars = [m for m in members if m.startswith(STAR_PREFIX)]
        if len(stars) != 1:
            errors.append(
                f"a roster must hold exactly one ★-prefixed member; found "
                f"{len(stars)}: {', '.join(stars) or '(none)'}")
    if known_roles is not None:
        for m in members:
            if m not in known_roles:
                errors.append(f"member `{m}` resolves to no agent file in either home")
    if EM_DASH in text:
        errors.append(f"contains {text.count(EM_DASH)} em dash(es)")
    return errors, warnings


def _library_agents():
    """Collect every agent across both homes once: a list of
    (path, team_name, home, frontmatter)."""
    out = []
    for home in AGENT_HOMES:
        for f, team in _agent_files(home):
            out.append((f, team, home, parse_frontmatter(f) or {}))
    return out


def _library_validate(target: str = "all") -> int:
    """Validate the federated agent library. With a target name, validate just
    that one agent (matched by role key, file stem, or spoken agent-name).
    Otherwise validate every agent and roster in both homes, then enforce
    global uniqueness of the role key AND the spoken agent-name across the
    union of both homes."""
    homes = [h for h in AGENT_HOMES if h.is_dir()]
    if not homes:
        warn("No agent library found yet (neither home exists).")
        return 0
    agents = _library_agents()
    known_roles = {(fm.get("title") or f.stem) for f, _, _, fm in agents}

    t = (target or "").strip()
    if t and t.lower() != "all":
        match = next((a for a in agents
                      if (a[3].get("title") or a[0].stem) == t
                      or a[0].stem == t
                      or (a[3].get("name") or "").strip().lower() == t.lower()),
                     None)
        if not match:
            fail(f"No agent named '{t}' in either home.")
            return 1
        errors, warnings = _agent_validate(match[0])
        for e in errors:
            fail(f"{rel(match[0])}: {e}")
        for w in warnings:
            warn(f"{rel(match[0])}: {w}")
        if not errors:
            ok(f"{rel(match[0])} is valid.")
        return 1 if errors else 0

    bad = 0
    for f, _team, _home, _fm in agents:
        errors, warnings = _agent_validate(f)
        for e in errors:
            fail(f"{rel(f)}: {e}")
        for w in warnings:
            warn(f"{rel(f)}: {w}")
        if errors:
            bad += 1
    if agents and bad == 0:
        ok(f"{len(agents)} agent spec(s) valid.")

    teams = []
    for home in homes:
        for f, _team in _team_files(home):
            teams.append(f)
            errors, warnings = _team_validate(f, known_roles)
            for e in errors:
                fail(f"{rel(f)}: {e}")
            for w in warnings:
                warn(f"{rel(f)}: {w}")
            if errors:
                bad += 1
    if teams and bad == 0:
        ok(f"{len(teams)} team roster(s) valid.")

    # Roster agreement across files: every ★-prefixed agent file must be its
    # team roster's lead, and every agent file on disk must be listed in its
    # team roster's members (the reverse of the member-resolves check above).
    rosters = {}
    for home in homes:
        for f, team in _team_files(home):
            rosters[(home, team)] = (f, parse_frontmatter(f) or {})
    roster_bad = 0
    for f, team, home, fm in agents:
        role = str(fm.get("title") or f.stem).strip()
        entry = rosters.get((home, team))
        if f.stem.startswith(STAR_PREFIX):
            if entry is None:
                fail(f"{rel(f)}: ★ agent's team `{team}` has no roster naming it lead")
                roster_bad += 1
            else:
                lead = str(entry[1].get("lead", "") or "").strip()
                if lead != role:
                    fail(f"{rel(f)}: ★ agent is not its roster's lead "
                         f"(`{rel(entry[0])}` names `{lead}`)")
                    roster_bad += 1
        if entry is not None and role not in _parse_members(entry[1]):
            fail(f"{rel(f)}: `{role}` is not listed in `{rel(entry[0])}` members")
            roster_bad += 1
    if agents and rosters and roster_bad == 0:
        ok(f"roster agreement holds: every ★ lead matches its roster; "
           f"all agent files are roster members.")
    bad += roster_bad

    # Federated uniqueness across the union of both homes.
    role_map, name_map = {}, {}
    for f, _team, _home, fm in agents:
        role = fm.get("title") or f.stem
        role_map.setdefault(role, []).append(rel(f))
        aname = (fm.get("name") or "").strip()
        if aname:
            name_map.setdefault(aname.lower(), []).append((aname, rel(f)))
    for role, paths in sorted(role_map.items()):
        if len(paths) > 1:
            fail(f"duplicate role `{role}` across the library: {', '.join(paths)}")
            bad += 1
    for _, entries in sorted(name_map.items()):
        if len(entries) > 1:
            fail(f"duplicate spoken name `{entries[0][0]}` across the library: "
                 + ", ".join(p for _, p in entries))
            bad += 1
    if agents and all(len(p) <= 1 for p in role_map.values()):
        ok(f"all {len(role_map)} role(s) unique across {len(homes)} home(s).")
    if name_map and all(len(e) <= 1 for e in name_map.values()):
        ok(f"all {len(name_map)} spoken name(s) unique across {len(homes)} home(s).")

    print()
    print(divider())
    print(f"  🏁  {len(agents)} agent(s), {len(teams)} team(s), {len(homes)} home(s); "
          f"{bad} item(s) with errors.")
    print(divider())
    return 1 if bad else 0


def _build_agent_catalog() -> dict:
    """Walk the federated agent homes and return the derived catalog as a plain
    dict: every agent (spoken name, role key, home, team, description, path) and
    every team roster (name, home, lead, members, description, path). This is the
    machine-readable source of truth for who exists in the library. It carries a
    `generated` stamp and the BRAIN version, like manifest.json, and is keyed for
    a reader by the spoken name (the addressing handle)."""
    homes = [h for h in AGENT_HOMES if h.is_dir()]
    home_label = {AR_DIR: "Agent Resources (AR)", FACULTIES_DIR: "Faculties",
                  LIBRARY_DIR: "Library"}
    agents, teams = [], []
    for home in homes:
        label = home_label.get(home, rel(home))
        for f, team in _agent_files(home):
            fm = parse_frontmatter(f) or {}
            agents.append({
                "name": (fm.get("name") or "").strip(),
                "role": (fm.get("title") or f.stem).strip(),
                "home": label,
                "team": team,
                "description": (fm.get("description") or "").strip(),
                "path": "BRAIN/" + rel(f),
            })
        for f, team in _team_files(home):
            fm = parse_frontmatter(f) or {}
            teams.append({
                "team": team,
                "home": label,
                "lead": (fm.get("lead") or "").strip(),
                "members": _parse_members(fm),
                "description": (fm.get("description") or "").strip(),
                "path": "BRAIN/" + rel(f),
            })
    agents.sort(key=lambda a: (a["home"], a["team"], a["role"].lstrip("★ ")))
    teams.sort(key=lambda t: (t["home"], t["team"]))
    return {
        "schema_version": 1,
        "generated": datetime.now(timezone.utc).isoformat(),
        "brain_version": _brain_version(),
        "home_count": len(homes),
        "team_count": len(teams),
        "agent_count": len(agents),
        "homes": [home_label.get(h, rel(h)) for h in homes],
        "agents": agents,
        "teams": teams,
    }


def _write_agent_catalog() -> dict:
    """Regenerate agent-catalog.json from the live homes and return the catalog
    dict ({} on failure). Called by save_index so the catalog is refreshed in
    lockstep with the manifest on every index rebuild, and by `agents catalog`
    for an on-demand write. A derived, non-critical artifact: a failure here is
    logged and swallowed so it can never block the manifest write."""
    try:
        cat = _build_agent_catalog()
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        AGENT_CATALOG_FILE.write_text(json.dumps(cat, indent=2), encoding="utf-8")
        return cat
    except Exception as e:
        logging.getLogger("catalog").error("Could not write agent catalog: %s", e)
        return {}


def _agent_catalog() -> int:
    """Force a fresh write of agent-catalog.json - the machine-managed JSON
    roll-up of the federated agent library in System/Data/. save_index
    already keeps it current in lockstep with the manifest; this is the explicit
    on-demand regenerate."""
    cat = _write_agent_catalog()
    if not cat:
        fail(f"Could not write {rel(AGENT_CATALOG_FILE)}.")
        return 1
    ok(f"Regenerated {rel(AGENT_CATALOG_FILE)}: {cat['agent_count']} agent(s), "
       f"{cat['team_count']} team(s) across {cat['home_count']} home(s).")
    return 0


def cmd_agents(subcmd: str = "", name: str = "") -> int:
    """Agent-library CLI: validate the federated library or one agent, or
    regenerate the derived catalog. No subcommand validates the whole library."""
    sub = (subcmd or "").strip().lower()
    if sub in ("", "validate"):
        header("Agent Library Validator", "🧩")
        return _library_validate(name or "all")
    if sub == "catalog":
        header("Agent Catalog Generator", "🧩")
        return _agent_catalog()
    fail(f"Unknown subcommand '{subcmd}'. "
         "Use: agents | agents validate <name|all> | agents catalog")
    return 1


# ══════════════════════════════════════════════════════════
#  AGENT COMMANDS - session bootstrap, surgical reads, graph
#  integrity, registry drift, memory lifecycle, versioning
# ══════════════════════════════════════════════════════════

# The four startup files (Instructions Section 9 / the `startup` tag).
STARTUP_PATHS = [
    "Constitution.md", "Instructions.md", "Profile/Working Style.md",
    "Memory/Log.md",
]


TRASH_DIR = BRAIN_DIR / ".trash"


def _os_trash_dir():
    """The host computer's own Trash, or None. macOS: ~/.Trash. Linux: the
    XDG trash, only if it already exists - never invent one on a host that
    may be a sandbox mounting a Mac-resident vault (a file moved into a VM's
    trash would silently leave the Mac with no 30-day recovery)."""
    t = Path.home() / ".Trash"
    if t.is_dir():
        return t
    xdg = Path.home() / ".local" / "share" / "Trash" / "files"
    if xdg.is_dir():
        return xdg
    return None


def _soft_remove(p: Path):
    """Stage 1 of the two-level deletion law (Constitution 3.1): move an item
    into .trash/, preserving its BRAIN-relative path so restores are exact and
    collisions are rare. Returns the trash destination, or None on failure.
    Nothing is ever permanently deleted here - that is `trash empty`, stage 2."""
    try:
        rel_p = p.relative_to(BRAIN_DIR)
        dest = TRASH_DIR / rel_p
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest = _safe_dest(dest)
        shutil.move(str(p), str(dest))
        return dest
    except (OSError, ValueError) as e:
        logging.getLogger("trash").error(e, exc_info=True)
        return None


def _trash_items():
    """Files currently in .trash/ (BRAIN-relative-inside-trash, Path) pairs."""
    if not TRASH_DIR.exists():
        return []
    return sorted((str(f.relative_to(TRASH_DIR)), f)
                  for f in TRASH_DIR.rglob("*")
                  if f.is_file() and f.name not in (".gitkeep", ".DS_Store"))


def cmd_trash(arg1: str = "", arg2: str = "") -> int:
    """🗑  Two-level deletion (Constitution 3.1). `trash <path>` = SOFT removal:
    the item moves to .trash/ keeping its relative path (confirmation required).
    `trash list` shows what's there with age; `trash restore <item>` puts it
    back; `trash empty [item]` = HARD removal, permanent, its own confirmation.
    Nothing is permanently deleted except from .trash - deletion is two doors,
    and the second one only opens after the first."""
    header("Two-Stage Trash", "🗑")
    sub = (arg1 or "list").strip()
    low = sub.lower()
    if low == "list":
        items = _trash_items()
        pending = []
        remote = _remote_backed()
        if remote:
            gd = run(["git", "-C", str(BRAIN_DIR), "diff", "--cached", "--name-only",
                      "--diff-filter=D"], timeout=10)
            if gd.returncode == 0:
                pending = [l for l in gd.stdout.splitlines() if l.strip()]
        if not items and not pending:
            ok(".trash is empty." + (" No staged git deletions." if remote else ""))
            return 0
        now = datetime.now(timezone.utc).timestamp()
        for relpath, f in items:
            age_d = int((now - f.stat().st_mtime) / 86400)
            print(f"    🗑  {relpath}  ({f.stat().st_size:,} B, {age_d}d in trash)")
        for pd in pending:
            print(f"    🗑  {pd}  (git-staged deletion; restore: trash restore {pd})")
        print()
        print(divider())
        tail = f"{len(items)} in .trash"
        if pending:
            tail += f", {len(pending)} staged git deletion(s)"
        print(f"  🏁  {tail}. Restore: trash restore <item>   Hard-remove (.trash): trash empty [item]")
        print(divider())
        return 0
    if low == "restore":
        if not arg2:
            fail("Usage: trash restore <item as shown by `trash list`>")
            return 2
        src = TRASH_DIR / arg2
        if not src.exists():
            # A remote-backed deletion lives in git, not .trash - restore it from there.
            if _remote_backed():
                rc = run(["git", "-C", str(BRAIN_DIR), "restore", "--staged", "--worktree",
                          "--", arg2], timeout=15)
                if rc.returncode == 0 and (BRAIN_DIR / arg2).exists():
                    _gitkeep_scan(fix=True)
                    ok(f"Restored from git: {arg2}")
                    return 0
            fail(f"Not in .trash: {arg2}")
            print("       If this was a committed deletion in a remote-backed vault, recover it from git "
                  "history:\n       git log --diff-filter=D -- '" + arg2 + "'  then  git checkout <commit>~1 -- '" + arg2 + "'")
            return 1
        dest = BRAIN_DIR / arg2
        if dest.exists():
            fail(f"Cannot restore - {arg2} already exists in the vault. Resolve the collision first.")
            return 1
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
        except OSError as e:
            fail(f"Restore failed: {e}")
            logging.getLogger("trash").error(e, exc_info=True)
            return 1
        _gitkeep_scan(fix=True)
        ok(f"Restored: {arg2}")
        return 0
    if low == "empty":
        items = _trash_items()
        if arg2:
            items = [(r, f) for r, f in items if r == arg2 or r.startswith(arg2.rstrip("/") + "/")]
            if not items:
                fail(f"Not in .trash: {arg2}")
                return 1
        if not items:
            ok(".trash is already empty.")
            return 0
        os_trash = _os_trash_dir()
        if os_trash is None:
            fail("No OS trash on this host - Hard Removal hands items to the computer's own "
                 "Trash (Constitution 3.1), so run `trash empty` on the Mac.")
            return 1
        print(f"  HARD removal - {len(items)} item(s) move to the computer's Trash ({os_trash}).")
        print("  The OS's own retention (Finder's 30-day auto-empty, when enabled) finishes the job.\n")
        for relpath, _f in items[:10]:
            print(f"    🗑  {relpath}")
        if len(items) > 10:
            print(f"    … and {len(items) - 10} more")
        if not confirm(f"Move {len(items)} item(s) to the computer's Trash? (yes/no): "):
            print("\n  🚫  Aborted - items remain in .trash.\n")
            return 0
        n = 0
        for _relpath, f in items:
            try:
                dest = _safe_dest(os_trash / f.name)
                shutil.move(str(f), str(dest)); n += 1
            except OSError as e:
                fail(f"could not move {_relpath}: {e}")
                logging.getLogger("trash").error(e, exc_info=True)
        # sweep now-empty dirs inside .trash
        for d in sorted((x for x in TRASH_DIR.rglob("*") if x.is_dir()), reverse=True):
            try:
                next(d.iterdir())
            except StopIteration:
                try:
                    d.rmdir()
                except OSError:
                    pass
            except OSError:
                pass
        print()
        print(divider())
        print(f"  🏁  {n} item(s) handed to the computer's Trash - the OS finishes the job.")
        print(divider())
        return 0
    # default: soft-remove the given path
    p2 = BRAIN_DIR / sub
    if not p2.exists():
        fail(f"Not found: {sub}")
        return 1
    try:
        rp = p2.resolve().relative_to(BRAIN_DIR.resolve())
    except (OSError, ValueError):
        fail(f"Not inside this BRAIN: {sub}")
        return 1
    parts = rp.parts
    if not parts or parts[0] in (".trash", ".obsidian", ".git"):
        fail("That is infrastructure (or already in .trash) - not a trash target.")
        return 1
    if p2.name == ".DS_Store":
        fail(".DS_Store is ignored by policy (Instructions Section 11) - the AI leaves it alone; macOS manages it.")
        return 1
    kind = "folder" if p2.is_dir() else "file"
    rp = str(p2.resolve().relative_to(BRAIN_DIR.resolve()))
    if _remote_backed() and _git_recoverable(p2):
        # Remote-backed vault: git history is the recovery net, so a tracked+clean
        # item is removed with `git rm` (recoverable from HEAD) instead of staged
        # into .trash/. Deletion stays confirmed; only the mechanism changes.
        if not confirm(f"Remove {kind} {rel(p2)} via git (recoverable from history)? (yes/no): "):
            print("\n  🚫  Aborted.\n")
            return 0
        rc = run(["git", "-C", str(BRAIN_DIR), "rm", "-r", "-q", "--", rp], timeout=30)
        if rc.returncode == 0:
            _gitkeep_scan(fix=True)
            ok(f"{rel(p2)} removed (git-tracked deletion).")
            print("\n  Recover before commit:  trash restore " + rp)
            print("  After commit: recover from git history. No .trash stage in a remote-backed vault.")
            return 0
        warn("git rm failed - falling back to the .trash safety net.")
        logging.getLogger("trash").error("git rm failed for %s: %s", rp, rc.stderr)
    # Local vault, or an untracked/modified item git could not recover: the
    # two-stage .trash/ net (Constitution 3.1).
    if not confirm(f"SOFT-remove {kind} {rel(p2)} to .trash/? (yes/no): "):
        print("\n  🚫  Aborted.\n")
        return 0
    dest = _soft_remove(p2)
    if dest is None:
        fail("Soft removal failed - see the error log.")
        return 1
    _gitkeep_scan(fix=True)
    ok(f"{rel(p2)}  →  {rel(dest)}")
    print("\n  Stage 1 of 2 complete. Restore with: trash restore " + str(dest.relative_to(TRASH_DIR)))
    print("  Hard-remove later with: trash empty")
    return 0


# Root infrastructure folders that must exist even when empty. `.trash/` is the
# soft-removal stage of the two-level deletion law (Constitution 3.1); it is
# frequently empty, so it carries a .gitkeep to survive git/zip/sync. A raw
# delete that bypasses the trash engine can remove it - gitkeep/health
# maintenance restores it rather than letting the BRAIN silently lose a
# required folder.
REQUIRED_INFRA_DIRS = [".trash"]


def _ensure_infra_dirs() -> list:
    """Restore any missing required root infrastructure folder, each with its
    .gitkeep marker. Idempotent; returns the BRAIN-relative names it restored
    (empty when everything was already present)."""
    restored = []
    for name in REQUIRED_INFRA_DIRS:
        d = BRAIN_DIR / name
        keep = d / ".gitkeep"
        if d.is_dir() and keep.exists():
            continue
        try:
            d.mkdir(parents=True, exist_ok=True)
            if not keep.exists():
                keep.touch()
            restored.append(name)
        except OSError as e:
            logging.getLogger("infra").error(e, exc_info=True)
    return restored


def _gitkeep_scan(fix: bool = False):
    """Empty-folder preservation rule: every empty folder in the BRAIN carries
    a .gitkeep so it survives git, zips, and sync tools; the moment a folder
    gains real files, its .gitkeep goes. Returns (missing, stale) lists of
    BRAIN-relative dirs; with fix=True, applies both directions. Hidden infra
    dirs are never touched."""
    missing, stale = [], []
    skip = {".obsidian", ".trash", ".git", "__pycache__", ".venv"}
    for d in sorted(BRAIN_DIR.rglob("*")):
        if not d.is_dir():
            continue
        parts = d.relative_to(BRAIN_DIR).parts
        if any(s in parts for s in skip) or any(p2.startswith(".") for p2 in parts):
            continue
        try:
            entries = [e for e in d.iterdir()
                       if e.name not in (".gitkeep", ".DS_Store")]
        except OSError:
            continue
        keep = d / ".gitkeep"
        if not entries and not keep.exists():
            missing.append(rel(d))
            if fix:
                try:
                    keep.touch()
                except OSError as e:
                    logging.getLogger("gitkeep").error(e, exc_info=True)
        elif entries and keep.exists():
            stale.append(rel(d))
            if fix:
                try:
                    keep.unlink()
                except OSError as e:
                    logging.getLogger("gitkeep").error(e, exc_info=True)
    return missing, stale


def cmd_logs(subcmd: str = "", target: str = "") -> int:
    """🧹 Inspect and clear the two operational logs (errors.log, reports.log).
    Bare `logs` reports each log's entry count and size. `logs clear [errors|
    reports|all]` snapshots the chosen log(s) verbatim to System/.backups/, then
    truncates them to empty - the clean state `health` reads. Constitution
    3.8-safe: the recoverable snapshot is taken before every clear, and the file
    itself is kept (emptied, never deleted). Asks to confirm unless --yes is
    given. CLI: logs · logs clear errors|reports|all."""
    logs = {"errors": LOG_FILE, "reports": REPORTS_FILE}

    def _count(p: Path) -> tuple:
        """Return (non_blank_lines, size_bytes) for a log; (0, 0) if absent."""
        if not p.exists():
            return (0, 0)
        try:
            n = sum(1 for l in p.read_text(encoding="utf-8").splitlines() if l.strip())
        except OSError:
            n = 0
        try:
            size = p.stat().st_size
        except OSError:
            size = 0
        return (n, size)

    sub = subcmd.strip().lower()

    # Read-only status view: bare `logs`, `logs status`, `logs list`.
    if sub in ("", "status", "list"):
        header("Operational Logs", "🧹")
        for name, p in logs.items():
            n, size = _count(p)
            state = "clean" if n == 0 else f"{n} entr{'y' if n == 1 else 'ies'}"
            print(f"    {name + '.log':<12} {state:<14} {size:>8,} bytes   {rel(p)}")
        print(divider())
        print("  Clear with:  logs clear errors | reports | all   (snapshots first)")
        print(divider())
        return 0

    if sub != "clear":
        fail(f"Unknown subcommand: 'logs {sub}'. Use: logs | logs clear [errors|reports|all]")
        return 1

    # Which log(s) to clear - default to all.
    which = target.strip().lower() or "all"
    if which in ("both", "*"):
        which = "all"
    if which == "all":
        selected = list(logs.items())
    elif which in logs:
        selected = [(which, logs[which])]
    else:
        fail(f"Clear what? Use: logs clear errors | reports | all  (got '{target}')")
        return 1

    header("Clear Logs", "🧹")

    # Only non-empty logs need clearing; report the rest as already clean.
    to_clear = []
    for name, p in selected:
        n, _ = _count(p)
        if n == 0:
            ok(f"{name}.log is already clean - nothing to clear.")
        else:
            to_clear.append((name, p, n))
    if not to_clear:
        print(divider()); print("  🏁  Nothing to clear."); print(divider())
        return 0

    summary = ", ".join(f"{name}.log ({n} entr{'y' if n == 1 else 'ies'})"
                        for name, _p, n in to_clear)
    if not confirm(f"  Snapshot and clear {summary}? (yes/no): "):
        warn("Aborted - logs untouched.")
        return 1

    dest_dir = SYSTEM_DIR / ".backups"
    cleared = 0
    for name, p, n in to_clear:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        try:                                            # snapshot first (recoverable)
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / _backup_dest_name(p, ts)
            shutil.copy2(str(p), str(dest))
        except OSError as e:
            fail(f"Backup of {name}.log failed - leaving it untouched: {e}")
            logging.getLogger("logs").error(e, exc_info=True)
            continue
        try:                                            # then empty in place (3.8: keep the file)
            p.write_text("", encoding="utf-8")
        except OSError as e:
            fail(f"Could not clear {name}.log: {e}")
            logging.getLogger("logs").error(e, exc_info=True)
            continue
        ok(f"{name}.log cleared - {n} entr{'y' if n == 1 else 'ies'} saved to {rel(dest)}")
        cleared += 1
    _backup_rotate()
    print()
    print(divider())
    print(f"  🏁  {cleared} log(s) cleared. Restore from System/.backups/ if needed.")
    print(divider())
    return 0


def cmd_gitkeep(subcmd: str = "") -> int:
    """📌 Enforce the empty-folder preservation rule. Default: fix - add
    .gitkeep to every empty folder, remove it from folders that gained files
    (both directions are standing user authorization, like the cascade).
    `gitkeep check` is the read-only dry run, exit 1 on violations."""
    header("Gitkeep Maintenance", "📌")
    check_only = (subcmd or "").strip().lower() == "check"
    infra_missing = 0
    if check_only:
        for name in REQUIRED_INFRA_DIRS:
            d = BRAIN_DIR / name
            if not (d.is_dir() and (d / ".gitkeep").exists()):
                print(f"    ❌  {name}/ - required infrastructure folder MISSING "
                      "(Constitution 3.1); restore with: gitkeep")
                infra_missing += 1
    else:
        for name in _ensure_infra_dirs():
            print(f"    🔧  {name}/ - restored required infrastructure folder (Constitution 3.1)")
    missing, stale = _gitkeep_scan(fix=not check_only)
    verb_m = "missing .gitkeep" if check_only else "added .gitkeep"
    verb_s = "stale .gitkeep (folder has files)" if check_only else "removed stale .gitkeep"
    for d in missing:
        print(f"    📌  {d}/ - {verb_m}")
    for d in stale:
        print(f"    📌  {d}/ - {verb_s}")
    if not missing and not stale and not infra_missing:
        ok("Every empty folder is preserved; no stale keeps.")
        return 0
    print()
    print(divider())
    if check_only:
        print(f"  🏁  {len(missing) + len(stale) + infra_missing} violation(s). Fix with: gitkeep")
        print(divider())
        return 1
    print(f"  🏁  {len(missing)} added, {len(stale)} removed.")
    print(divider())
    return 0


def _strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans - wikilinks inside code
    are not rendered by Obsidian, so the graph tools must ignore them."""
    out, fenced = [], False
    for line in text.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
            continue
        if not fenced:
            out.append(re.sub(r"`[^`\n]*`", "", line))
    return "\n".join(out)


_WIKILINK_RE = re.compile(r"(!?)\[\[([^\[\]\n]+?)\]\]")


def _extract_wikilinks(text: str) -> list:
    """Return wikilink targets (path part only - alias/heading/block stripped).
    Same-file heading links ([[#H]]) and comment-wrapped text are skipped."""
    targets = []
    stripped = _strip_code(text)
    # Obsidian %%...%% comment spans are not rendered: a wikilink inside one
    # is commented out, not a live graph edge. Strip whole spans (an unclosed
    # %% comments out the rest of the file, matching Obsidian) rather than
    # only rejecting %% inside the brackets.
    stripped = re.sub(r"%%.*?(?:%%|\Z)", "", stripped, flags=re.S)
    for _embed, raw in _WIKILINK_RE.findall(stripped):
        # Markdown tables escape the alias pipe as \| - normalize first.
        t = raw.replace("\\|", "|").split("|")[0].split("#")[0].strip()
        if t and "%%" not in t:
            targets.append(t)
    return targets


def _toolkit_item_root(path: Path):
    """If path lives inside a Toolkit item (System/Toolkit/<Section>/<Item>/...),
    return that item's directory; else None."""
    parts = path.parts
    if "Toolkit" not in parts or "System" not in parts:
        return None
    i = parts.index("Toolkit")
    after = parts[i + 1:]
    if len(after) >= 2 and after[0] == "Skills":
        candidate = Path(*parts[:i + 2], after[1])
        return candidate if candidate.is_dir() else None
    return None


def _graph_sources():
    """Markdown files whose wikilinks count as graph edges. Template/ files
    are forbidden wikilinks (Art. 3.7). Toolkit item files ARE sources, with
    scoped rules enforced by the graph builder: internals link only within
    their own item; the namesake doc is the one bridge to the BRAIN (and to
    other items' namesake docs, when related)."""
    for path in iter_md_files():
        if "Template" in path.parts or ".template" in path.parts:
            continue
        yield path


def _build_link_graph():
    """Resolve every wikilink in the vault. Returns (broken, ambiguous,
    inbound, outbound) where broken is [(src_rel, target)], ambiguous is
    [(src_rel, target, candidates)], inbound/outbound map rel→count."""
    # Target map: basename (lowercase, .md optional) → [rel paths]. Built over
    # all files because links may point at binaries ([[figure.png]]).
    by_name = {}
    all_rel = []
    template_names = set()
    for f in iter_all_files():
        r = rel(f)
        # Templates are scaffolds, not graph nodes (Article 3.7): they never
        # resolve as link targets, and linking to them is a violation.
        if "Template" in f.parts or ".template" in f.parts:
            template_names.add(f.stem.lower())
            template_names.add(f.name.lower())
            continue
        all_rel.append(r)
        keys = {f.name.lower()}
        if f.suffix == ".md":
            keys.add(f.stem.lower())
        for k in keys:
            by_name.setdefault(k, []).append(r)
    # Generated artifacts in System/Data/ are excluded from the index (churn)
    # but are real files and lawful link targets for Data.md (Art. 3.7).
    if DATA_DIR.is_dir():
        for f in sorted(DATA_DIR.iterdir()):
            if f.is_file() and not f.name.startswith(".") and f.suffix != ".md":
                r = rel(f)
                all_rel.append(r)
                by_name.setdefault(f.name.lower(), []).append(r)
    broken, ambiguous, violations = [], [], []
    edges = set()
    inbound = {r: 0 for r in all_rel}
    outbound = {}
    for src in _graph_sources():
        src_rel = rel(src)
        try:
            targets = _extract_wikilinks(src.read_text(encoding="utf-8"))
        except OSError:
            continue
        outbound[src_rel] = len(targets)
        # Toolkit scoping (Skills.md graph policy): an item's internal files
        # link only within their own item folder; the namesake doc alone
        # bridges to the BRAIN, and item-to-item links go docs-to-docs only.
        item = _toolkit_item_root(src)
        is_doc = _toolkit_brain_doc(src)
        item_rel = rel(item) + "/" if item else None
        for t in targets:
            tl = t.lower()
            if "/" in t:
                # Path link: resolve on an exact rel-path match or a suffix
                # preceded by "/" (a path-segment boundary), .md optional, so
                # [[Projects/X]] can never match "Archived Projects/X.md".
                hits = []
                for r in all_rel:
                    rl = r.lower()
                    if any(rl == cand or rl.endswith("/" + cand)
                           for cand in (tl, tl + ".md")):
                        hits.append(r)
            else:
                hits = by_name.get(tl, []) or by_name.get(tl + ".md", [])
                if len(hits) > 1:  # case-insensitive collision: exact-case basename wins
                    exact = [h for h in hits
                             if h.rsplit("/", 1)[-1] in (t, t + ".md")]
                    if len(exact) == 1:
                        hits = exact
            # Toolkit scoping filters BEFORE ambiguity/inbound accounting:
            # an item's internals are reachable only from inside that item, so
            # they never collide with vault names like [[People]].
            def _reachable(h):
                t_item = _toolkit_item_root(BRAIN_DIR / h)
                if t_item is None:
                    return True                      # plain vault file
                t_item_rel = rel(t_item) + "/"
                if item and t_item_rel == item_rel:
                    return True                      # same item - internal link
                return _toolkit_brain_doc(BRAIN_DIR / h)  # other items: docs only
            in_scope = [h for h in hits if _reachable(h)]
            if item and not is_doc:
                own = [h for h in in_scope if h.startswith(item_rel)]
                if hits and not own:
                    violations.append((src_rel, t,
                        "internal skill files link only within their own skill - "
                        "the namesake doc is the one bridge to the BRAIN"))
                    continue
                in_scope = own
            elif hits and not in_scope:
                violations.append((src_rel, t,
                    "cross-skill links go docs-file to docs-file only "
                    "(and only when the skills are related)"))
                continue
            hits = in_scope
            # Hub-only topology (Constitution 3.7, tenth amendment): only
            # folder docs and the fixed root chain carry links; content files
            # reference everything by plain path.
            if hits:
                h0 = hits[0]
                sp, dp = src_rel.split("/"), h0.split("/")
                sibling = sp[:-1] == dp[:-1]
                src_is_root = len(sp) == 1
                src_is_doc = (not src_is_root
                              and sp[-1].rsplit(".", 1)[0] == sp[-2])
                folder = sp[:-1]
                child_doc = (len(dp) == len(folder) + 2
                             and dp[:len(folder)] == folder
                             and dp[-1].rsplit(".", 1)[0] == dp[-2])
                if src_is_root:
                    chain = {"CLAUDE.md": ("AGENTS.md",),
                             "AGENTS.md": ("Instructions.md",),
                             "Instructions.md": ("Constitution.md", "Information.md"),
                             "Constitution.md": ()}
                    allowed = chain.get(sp[0], ())
                    ok = ((len(dp) == 1 and dp[0] in allowed)
                          or (sp[0] == "Instructions.md" and child_doc))
                    why = ("root chain - CLAUDE.md > AGENTS.md > Instructions.md > "
                           "Constitution.md; Instructions also links Layer-1 docs (3.7)")
                elif src_is_doc:
                    ok = sibling or child_doc
                    why = ("hub topology - a folder doc links its own files and its "
                           "immediate subfolders' docs; nothing else (3.7)")
                else:
                    ok = False
                    why = ("hub-only topology - content files carry no wikilinks; "
                           "reference by plain path (Constitution 3.7)")
                if not ok and h0 != src_rel:
                    violations.append((src_rel, t, why))
                    continue
            if not hits:
                base = t.split("/")[-1].lower()
                if base.endswith(".zim"):
                    # ZIM knowledge bases (Library/Reference & Encyclopedia/) are
                    # gitignored, machine-local, re-downloadable data files (kb
                    # refresh). Their absence on a machine - e.g. a fresh clone
                    # before kb refresh - is expected, not a broken link.
                    continue
                if base in {"errors.log", "reports.log", "manifest.json",
                            "catalog.ndjson", "agent-catalog.json", "sync-state.json",
                            "session-ledger.json", "friction.jsonl"}:
                    # Generated System/Data/ artifacts, documented (not navigated)
                    # in Data.md. Regenerable and partly gitignored, so any one can
                    # be absent on a fresh clone or before its producing command has
                    # run - expected, like the .zim case above, not a broken link.
                    continue
                if base in template_names or base + ".md" in template_names \
                        or ".template" in t.lower() or "/template/" in t.lower():
                    violations.append((src_rel, t,
                        "links to a template scaffold - templates are not graph "
                        "nodes; reference them by plain path (Article 3.7)"))
                else:
                    broken.append((src_rel, t))
            else:
                # Resolution is by basename, case-insensitive (Obsidian rule).
                # >1 hit = ambiguous: Obsidian's tie-break is undocumented, so
                # flag it for a path-qualified link rather than guessing.
                if len(set(hits)) > 1:
                    ambiguous.append((src_rel, t, sorted(set(hits))))
                inbound[hits[0]] = inbound.get(hits[0], 0) + 1
                if hits[0] != src_rel:  # self-links carry no graph information
                    edges.add((src_rel, hits[0]))
    return broken, ambiguous, inbound, outbound, violations, edges


def cmd_links(subcmd: str = "check", target: str = "") -> int:
    """🔗 Wikilink graph integrity. `links` / `links check`: broken + ambiguous
    links (exit 1 on broken - a broken link is a lie in the knowledge graph).
    `links orphans`: notes nothing links to. `links stats`: hubs and counts.
    `links subfolders [<folder>]`: maintain each folder doc's auto-block of links
    to its immediate-subfolder namesake docs (Constitution 3.7). With a folder,
    walk its subtree and inject/refresh; with no target, refresh existing blocks."""
    header("Wikilink Graph", "🔗")
    sub = (subcmd or "check").strip().lower()
    if sub in ("subfolders", "children"):
        if target:
            root = (BRAIN_DIR / target).resolve()
            if not root.exists():
                fail(f"No such path under the BRAIN: {target}")
                print(divider()); return 1
            if root.is_file():
                root = root.parent
            candidates = [root] + sorted((p for p in root.rglob("*") if p.is_dir()),
                                         key=lambda p: p.as_posix())
            docs = []
            for d in candidates:
                rp = d.relative_to(BRAIN_DIR).parts
                if any(p.startswith(".") or p == "Template" for p in rp):
                    continue
                doc = d / f"{d.name}.md"
                if doc.exists():
                    docs.append(doc)
            changed = sum(1 for doc in docs if _sync_children_links(doc))
            ok(f"Subfolder links: {changed} folder doc(s) updated of {len(docs)} scanned under {target}/.")
        else:
            changed = _refresh_all_children_blocks()
            ok(f"Refreshed {changed} existing subfolder-link block(s).")
        print(divider())
        return 0
    broken, ambiguous, inbound, outbound, violations, edges = _build_link_graph()
    if sub == "orphans":
        # Orphan = a content note with no inbound links. Root/startup files and
        # folder docs are entry points by design, so they are not flagged.
        # Excludes are path-segment tests (a folder literally named Skills,
        # State, or Archive), never substring matches that a note title like
        # "Real Estate" could trip.
        orphans = [r for r, n in sorted(inbound.items())
                   if n == 0 and r.endswith(".md")
                   and ("/" in r)                                   # not a root file
                   and (Path(r).name != Path(r).parent.name + ".md")  # folder doc
                   and ("Template" not in r) and (".template" not in r)
                   and ("Skills" not in Path(r).parts)
                   and ("State" not in Path(r).parts)
                   and ("Archive" not in Path(r).parts)
                   and not (r.startswith("Memory/")
                            and Path(r).parent.name in ("Current", "Recent"))]
        if orphans:
            print(f"  {len(orphans)} orphan note(s) - nothing links to them:\n")
            for r in orphans:
                print(f"    📄  {r}")
            print("\n  Advisory only: link them from a relevant note or index, or confirm they are intentional.")
        else:
            ok("No orphan notes.")
        return 0
    if sub == "stats":
        n_sources = len(outbound)
        n_edges = sum(outbound.values())
        print(f"  Sources scanned : {n_sources}")
        print(f"  Total wikilinks : {n_edges}")
        print(f"  Broken          : {len(broken)}")
        print(f"  Ambiguous       : {len(ambiguous)}")
        print(f"  Boundary breaks : {len(violations)}")
        mutual_n = len({tuple(sorted(e)) for e in edges if (e[1], e[0]) in edges})
        print(f"  Reciprocal pairs: {mutual_n}")
        hubs = sorted(((n, r) for r, n in inbound.items() if n), reverse=True)[:8]
        if hubs:
            print("\n  Most-linked files (inbound):")
            for n, r in hubs:
                print(f"    {n:>3}  {r}")
        out_hubs = sorted(((n, r) for r, n in outbound.items() if n), reverse=True)[:5]
        if out_hubs:
            print("\n  Most outbound:")
            for n, r in out_hubs:
                print(f"    {n:>3}  {r}")
        return 0
    # default: check
    # Cascade law (Constitution 3.7): links flow downhill, never back.
    mutual = sorted({tuple(sorted(e)) for e in edges if (e[1], e[0]) in edges})
    for a, b in mutual:
        fail(f"{a} ⇄ {b}: reciprocal links - cascade law: the file nearer root keeps the link, "
             "the other references by plain path (backlinks are automatic)")
    # longer cycles: warn (rare; cutting an edge is a judgment call)
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
    color, cyc_found = {}, []
    def _dfs(u, path):
        color[u] = 1
        for v in adj.get(u, ()):
            if color.get(v, 0) == 1 and v in path:
                cyc_found.append(path[path.index(v):] + [v])
            elif color.get(v, 0) == 0:
                _dfs(v, path + [v])
        color[u] = 2
    for n0 in list(adj):
        if color.get(n0, 0) == 0:
            _dfs(n0, [n0])
    for cyc in cyc_found:
        if len(cyc) > 3:
            warn("link cycle: " + " → ".join(cyc) + "  (cascade prefers a DAG - cut the uphill edge)")
    for src_rel, t, why in violations:
        fail(f"{src_rel}: [[{t}]] - {why}")
    for src_rel, t, cands in ambiguous:
        warn(f"{src_rel}: [[{t}]] is ambiguous - {len(cands)} files match: {', '.join(cands[:3])}{'…' if len(cands) > 3 else ''}. Use a path-qualified link.")
    if broken or violations or mutual:
        print()
        for src_rel, t in broken:
            fail(f"{src_rel}: [[{t}]] points at no existing file")
        print()
        print(divider())
        print(f"  🏁  {len(broken)} broken, {len(violations)} boundary violation(s), "
              f"{len(mutual)} reciprocal pair(s). Links cascade downhill - fix and re-run.")
        print(divider())
        return 1
    ok(f"All wikilinks resolve ({sum(outbound.values())} links, {len(ambiguous)} ambiguous warning(s)).")
    return 0


def _md_sections(text: str) -> list:
    """Parse ATX headings (fence-aware). Returns [(level, title, start, end)]
    line index spans - a section runs to the next heading of same-or-higher
    level, subsections included (the [[Note#Heading]] embed convention)."""
    lines = text.split("\n")
    heads, fenced = [], False
    for i, ln in enumerate(lines):
        if re.match(r"^\s*(```|~~~)", ln):
            fenced = not fenced
            continue
        m = re.match(r"^(#{1,6})\s+(.+?)(?:\s+#+)?\s*$", ln)
        if m and not fenced:
            heads.append((len(m.group(1)), m.group(2).strip(), i))
    sections = []
    for idx, (lvl, title, start) in enumerate(heads):
        end = len(lines)
        for lvl2, _t2, s2 in heads[idx + 1:]:
            if lvl2 <= lvl:
                end = s2
                break
        sections.append((lvl, title, start, end))
    return sections


def _resolve_md(target: str):
    """Resolve a user-given path: exact BRAIN-relative first, then unique
    basename match across the vault. Returns Path or None."""
    p = BRAIN_DIR / target
    if p.is_file():
        return p
    tl = target.lower()
    hits = [f for f in iter_all_files()
            if f.name.lower() in (tl, tl + ".md") or rel(f).lower() == tl]
    return hits[0] if len(hits) == 1 else None


def cmd_read(target: str = "", section: str = "", fm_only: bool = False,
             toc: bool = False) -> int:
    """📖 Surgical reads (Article 10.4): print one section of a file instead of
    the whole thing. `read <path> <section>` prints that heading's span;
    `read <path> --toc` lists headings with line numbers and token costs so you
    can pick; `read <path> --fm` prints frontmatter only."""
    if not target:
        print("  Usage: read <path> [section title]   |   read <path> --toc   |   read <path> --fm")
        return 2
    p = _resolve_md(target)
    if p is None:
        fail(f"No unique file matches '{target}'. Give a BRAIN-relative path.")
        return 1
    if p.suffix.lower() != ".md":
        fail(f"{rel(p)} is not a markdown file - read serves .md only "
             f"(binaries would load whole into memory).")
        return 1
    try:
        text = _read_text(p)
    except OSError as e:
        fail(f"Cannot read {rel(p)}: {e}")
        logging.getLogger("read").error(e, exc_info=True)
        return 1
    if fm_only:
        m = re.match(r"^---\n.*?\n---\n?", text, re.DOTALL)
        print(m.group(0).rstrip() if m else "  (no frontmatter block)")
        return 0
    secs = _md_sections(text)
    if toc or not section:
        print(f"  {rel(p)} - {count_tokens(p)} tokens total\n")
        if not secs:
            print("  (no headings)")
            return 0
        lines = text.split("\n")
        for lvl, title, start, end in secs:
            body = "\n".join(lines[start:end])
            print(f"    L{start + 1:<5} {'  ' * (lvl - 1)}{'#' * lvl} {title}  (~{max(1, len(body) // 4)} tokens)")
        if not section:
            print("\n  Print one with: read \"%s\" \"<section title>\"" % rel(p))
        return 0
    # Match: exact (case-insensitive, numbering-tolerant) → prefix → contains.
    want = section.strip().lower()
    pick = None
    for s in secs:
        if s[1].lower() == want:
            pick = s; break
    if pick is None:
        starts = [s for s in secs if s[1].lower().startswith(want)]
        pick = starts[0] if len(starts) == 1 else None
    if pick is None:
        contains = [s for s in secs if want in s[1].lower()]
        pick = contains[0] if len(contains) == 1 else None
    if pick is None:
        fail(f"No unique heading matches '{section}'. Run: read \"{rel(p)}\" --toc")
        return 1
    lines = text.split("\n")
    print("\n".join(lines[pick[2]:pick[3]]).rstrip())
    return 0


def cmd_startup(json_out: bool = False, manifest: bool = False) -> int:
    """🚀 The Instructions Section 9 session-init bundle in one call: the four
    startup files in stable→volatile (cache-optimal) order, the 2 newest
    completed Memory/Context/Current/ summaries, then the Inbox check. `--json` lists
    paths + token costs instead of contents (for budgeting). `--manifest`
    emits a compact hook-safe orientation card (paths to Read, not bodies):
    harness hooks truncate large stdout, so the full ~30k-token bundle never
    survives that channel; the manifest always does."""
    # 2 newest live summaries; _memory_files excludes Current.md. A summary marked
    # stale (status deprecated/archived, e.g. a later one overrides it) is skipped
    # here so the session never auto-loads stale context - retained, just demoted.
    summaries = [f for f in sorted(_memory_files(BRAIN_DIR / "Memory" / "Context" / "Current"),
                                   reverse=True) if not _path_stale(f)][:2]
    inbox = _inbox_files()
    bundle = [BRAIN_DIR / s for s in STARTUP_PATHS if (BRAIN_DIR / s).is_file()]
    missing = [s for s in STARTUP_PATHS if not (BRAIN_DIR / s).is_file()]
    if json_out:
        files = [{"path": rel(f), "tokens": count_tokens(f)} for f in bundle + summaries]
        print(json.dumps({"files": files,
                          "total_tokens": sum(f["tokens"] for f in files),
                          "inbox_pending": [rel(f) for f in inbox],
                          "missing": missing}, indent=2))
        return 0
    if manifest:
        # Hook-safe orientation card. Everything here must survive a truncating
        # hook channel, so the budget is roughly 1.5 KB: paths and one-line
        # state, never file bodies. The session Reads each READ line itself.
        print("===== BRAIN STARTUP MANIFEST (Section 9) =====")
        print("  The startup set is listed, not inlined. Read every READ line")
        print("  below with the Read tool before substantive work; in a plain")
        print("  terminal, `startup` (no flag) inlines the full bundle instead.")
        for f in bundle:
            print(f"  READ  {rel(f)}  (~{count_tokens(f)} tokens)")
        for s in missing:
            warn(f"startup file missing: {s}")
        for f in summaries:
            print(f"  READ  {rel(f)}  (session summary)")
        if not summaries:
            print("  (no completed session summaries in Memory/Context/Current/)")
        if inbox:
            for f in inbox:
                print(f"  📨  {rel(f)}")
            print(f"  ⚠️   {len(inbox)} Inbox file(s) await sorting - handle per Inbox/Inbox.md first.")
        else:
            print("  ✅  Inbox clear.")
        return 0
    header("Session Startup Bundle", "🚀")
    total = sum(count_tokens(f) for f in bundle + summaries)
    print(f"  {len(bundle)} startup files + {len(summaries)} session summaries  (~{total} tokens)\n")
    for f in bundle + summaries:
        print(f"===== FILE: {rel(f)}  (~{count_tokens(f)} tokens) =====")
        try:
            print(f.read_text(encoding="utf-8").rstrip())
        except OSError as e:
            logging.getLogger("startup").error("unreadable startup file %s: %s", rel(f), e)
            fail(f"unreadable: {e}")
        print()
    for s in missing:
        warn(f"startup file missing: {s}")
    # Inbox last - the volatile, action-required tail (Section 15.2 recency slot).
    print("===== INBOX CHECK (Section 9, step 2) =====")
    if inbox:
        for f in inbox:
            print(f"  📨  {rel(f)}")
        print(f"\n  ⚠️   {len(inbox)} file(s) await sorting - handle per Inbox/Inbox.md before other work.")
    else:
        print("  ✅  Inbox clear.")
    return 0


def _inbox_files() -> list:
    """Sortable Inbox files: the loose drops at Inbox/ root. Excludes hidden
    files, the Inbox.md fixture, Backups/, and the permanent sub-homes Reports/,
    Faculties/, Visuals/, and Ideas/ (the held reports library, the standing-teams
    home, the held visuals library, and the held idea pool) - these are kept and
    indexed, never sorted, per Inbox/Inbox.md."""
    inbox_dir = BRAIN_DIR / "Inbox"
    if not inbox_dir.is_dir():
        return []
    out = []
    for f in sorted(inbox_dir.rglob("*")):
        if not f.is_file() or f.name.startswith("."):
            continue
        parts = f.relative_to(inbox_dir).parts
        if parts[0] in ("Backups", "Reports", "Faculties", "Visuals", "Ideas") \
                or (len(parts) == 1 and f.name == "Inbox.md"):
            continue
        out.append(f)
    return out


def cmd_inbox() -> int:
    """📨 Inbox status (Section 9, step 2). Lists files awaiting the sorting
    protocol with size, age, and frontmatter state. Exit 1 when sorting is
    pending so scripts and agents can branch on it."""
    header("Inbox Status", "📨")
    files = _inbox_files()
    if not files:
        ok("Inbox clear - nothing to sort.")
        return 0
    now = datetime.now(timezone.utc).timestamp()
    print(f"  {len(files)} file(s) awaiting the Inbox protocol (Inbox/Inbox.md):\n")
    for f in files:
        age_d = int((now - f.stat().st_mtime) / 86400)
        size_kb = f.stat().st_size / 1024
        fm_state = ""
        if f.suffix == ".md":
            fm_state = "frontmatter ✓" if parse_frontmatter(f) else "no frontmatter - needs enrichment"
        print(f"    📨  {rel(f)}  ({size_kb:.0f} KB, {age_d}d old{', ' + fm_state if fm_state else ''})")
    print("\n  Nothing moves un-enriched or unconfirmed (Constitution 5.3).")
    return 1


def cmd_index(subcmd: str = "verify") -> int:
    """🗂  Registry/tree agreement for the Memory collections: each collection
    doc's auto-maintained entries block must list exactly the entry files
    present. (Project and venture listing is now the `db` catalog, generated
    from the tree, so it cannot drift the way a hand-kept index could.) Exit 1
    on drift."""
    header("Index Verify", "🗂")
    drift = 0
    # Memory per-entry collections: the index's auto-maintained entries block
    # must list exactly the entry files present. The block is engine-kept, so
    # drift means manual tampering or a missed `memory sync`.
    for cname, mfolder, _kind, _ph in MEMORY_COLLECTIONS:
        doc = mfolder / f"{cname}.md"
        if not doc.exists():
            continue
        files = {f.stem for f in _collection_entry_files(mfolder)}
        try:
            mtext = doc.read_text(encoding="utf-8")
        except OSError:
            continue
        mm = re.search(re.escape(COLLECTION_LINKS_START) + r"(.*?)"
                       + re.escape(COLLECTION_LINKS_END), mtext, re.DOTALL)
        listed = set()
        if mm:
            for lm in re.finditer(r"\[\[([^\]]+?)\]\]", mm.group(1)):
                listed.add(lm.group(1).split("|")[0].split("#")[0].strip().rsplit("/", 1)[-1])
        print(f"  Memory/{cname}: {len(files)} entry file(s), {len(listed)} listed")
        for nm in sorted(files - listed):
            fail(f"Memory/{cname}/{nm}.md is not listed in {cname}.md - run `memory sync`")
            drift += 1
        for nm in sorted(listed - files):
            # A phantom entry (listed, no file on disk) is drift too: the
            # registry is promising a record that does not exist.
            fail(f"Memory/{cname}/{cname}.md lists '{nm}' but no such entry file exists (run `memory sync`)")
            drift += 1
    print()
    if drift:
        print(divider())
        print(f"  🏁  {drift} unregistered folder(s) - the AI's orientation registry is lying. Fix now.")
        print(divider())
        return 1
    ok("Indexes agree with the folder tree.")
    return 0


def cmd_summary(subcmd: str = "") -> int:
    """🗒  Session-summary lifecycle (Section 14 + Memory/Memory.md). `summary
    new` scaffolds Memory/Context/Current/YYYYMMDD-HHMMSS.md with the canonical
    frontmatter and the six mandatory sections, then runs the cascade.
    `summary latest` prints the newest summary path. Bare `summary` = status."""
    header("Session Summary", "🗒")
    cur = BRAIN_DIR / "Memory" / "Context" / "Current"
    sub = (subcmd or "").strip().lower()
    existing = _memory_files(cur)   # excludes the Current.md namesake doc
    if sub == "latest":
        if existing:
            print(f"  {rel(existing[-1])}")
            return 0
        warn("No summaries in Memory/Context/Current/.")
        return 1
    if sub != "new":
        print(f"  Memory/Context/Current/ holds {len(existing)} of 3 summaries.")
        for f in existing:
            print(f"    🗒  {rel(f)}  (~{count_tokens(f)} tokens)")
        print("\n  Subcommands: summary new   |   summary latest")
        return 0
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y%m%d-%H%M%S")
    day = now.strftime("%Y-%m-%d")
    dest = cur / f"{ts}.md"
    body = f'''---
title: "Session Summary - {day}"
description: "Tiered-memory session summary (delta update)."
status: "active"
tags: ["memory", "record", "sensitive"]
aliases: []
keywords: {json.dumps(SUMMARY_KEYWORDS_DEFAULT)}
created: {day}
updated: {day}
type: "record"
folder: "memory"
layer: 3
policy: false
author: "{AUTHOR}"
path: "BRAIN/Memory/Context/Current/{ts}.md"
id: "me-summary-{ts}"
---

# Session Summary - {day}

<!-- Delta-update ledger (Memory/Memory.md §1): separate what stands, what
changed, and what is overridden. Compose for recall first, then prune.
Keep verbatim blocks for anything load-bearing. -->

## 1. Session Metadata

- Date: {day}
- Duration estimate:
- Model:
- Primary topics:

## 2. Current State

### Established Foundations
<!-- prior state that remains valid -->

### Active Changes
<!-- modified, added, or decided THIS session -->

### Overrides
<!-- explicitly supersedes earlier statements - declare precedence -->

## 3. Critical Decisions Made

## 4. Unresolved Questions

## 5. Immediate Next Steps

## 6. Verbatim Preservation
'''
    try:
        cur.mkdir(parents=True, exist_ok=True)
        dest.write_text(body, encoding="utf-8")
    except OSError as e:
        fail(f"Could not write summary: {e}")
        logging.getLogger("summary").error(e, exc_info=True)
        return 1
    _gitkeep_scan(fix=True)  # Current/ just gained a file - its .gitkeep goes
    ok(f"Scaffolded {rel(dest)} - fill the sections, then it cascades.")
    print("\n  Same-session continuation: OVERWRITE this file, don't create another (Memory.md §3).")
    print("  Running cascade to enforce tier caps:\n")
    _memory_cascade()
    print("\n  Reminder: run `sync` so the new file gets Finder tags.")
    return 0


_PROMOTION_HINTS = [
    (("decided", "decision", "chose", "going with", "we will"), 'Memory/Decisions/ (memory add decision "...")'),
    (("met", "introduced", "friend", "colleague", "partner", "neighbor"), 'Memory/Entities/People/ (memory add person "...")'),
    (("learned", "realized", "turns out", "fact:", "prefers"), "Profile/ (propose via Constitution 4.2 - not Memory)"),
    (("pattern", "always", "every time", "tends to", "habit"), "Profile/Personality.md (propose via 4.2 - not Memory)"),
    (("deadline", "anniversary", "birthday", "due", "renewal"), "Memory/Dates.md"),
]


def cmd_consolidate() -> int:
    """🧹 Memory Consolidation Loop prep (System/Workflows.md). Read-only:
    extracts unpromoted Log.md entries, finds near-duplicates in the permanent
    Memory files, and emits an ADD/UPDATE/SUPERSEDE/NOOP worksheet for the AI
    to adjudicate. Flags only - writing is the AI's judgment call (Art. 3.4)."""
    import difflib
    header("Consolidation Worksheet", "🧹")
    log_file = BRAIN_DIR / "Memory" / "Log.md"
    try:
        text = log_file.read_text(encoding="utf-8")
    except OSError as e:
        fail(f"Cannot read Memory/Log.md: {e}")
        return 1
    entries = [(m.group(1).strip(), m.start())
               for m in re.finditer(r"^### (.+)$", text, re.MULTILINE)
               if "[Date]" not in m.group(1)]
    if not entries:
        ok("Log.md has no unpromoted entries - nothing to consolidate.")
        return 0
    # Candidate lines from the permanent memory content: headings + table rows +
    # bullets across every MEMORY_COLLECTIONS folder (People, Organizations,
    # Places, Decisions, Events, Insights) plus the flat Dates.md. Keyed by
    # Memory-relative path so the worksheet shows exactly where each
    # near-duplicate lives.
    targets = {}
    mem = BRAIN_DIR / "Memory"
    perm_files = []
    for _cname, folder, _kind, _ph in MEMORY_COLLECTIONS:
        if folder.is_dir():
            perm_files.extend(sorted(f for f in folder.iterdir()
                                     if f.is_file() and f.suffix == ".md"))
    if (mem / "Dates.md").is_file():
        perm_files.append(mem / "Dates.md")
    for p in perm_files:
        key = rel(p)[len("Memory/"):] if rel(p).startswith("Memory/") else rel(p)
        try:
            targets[key] = [ln.strip("#|-* ").strip() for ln in
                            p.read_text(encoding="utf-8").split("\n")
                            if len(ln.strip("#|-* ").strip()) > 8]
        except OSError:
            targets[key] = []
    print(f"  {len(entries)} Log entries to adjudicate. For each: ADD (promote as new),")
    print("  UPDATE (merge into the match), SUPERSEDE (replaces the match), or NOOP (drop/stays in Log).\n")
    for title, _pos in entries:
        best_ratio, best_line, best_file = 0.0, "", ""
        tnorm = title.lower()
        for fname, lines in targets.items():
            for cand in lines:
                r2 = difflib.SequenceMatcher(None, tnorm, cand.lower(), autojunk=False).ratio()
                if r2 > best_ratio:
                    best_ratio, best_line, best_file = r2, cand, fname
        print(f"  ### {title}")
        if best_ratio >= 0.75:
            print(f"      near-duplicate ({best_ratio:.0%}) of Memory/{best_file}: \"{best_line[:70]}\"")
            print(f"      → likely UPDATE or NOOP")
        elif best_ratio >= 0.55:
            print(f"      possible match ({best_ratio:.0%}) in Memory/{best_file}: \"{best_line[:70]}\"")
            print(f"      → review: UPDATE vs ADD")
        else:
            dest = next((d for kws, d in _PROMOTION_HINTS
                         if any(k in tnorm for k in kws)), "")
            print(f"      no existing match → ADD candidate{' to ' + dest if dest else ' (pick destination)'}")
        print()
    print(divider())
    print(f"  🏁  Worksheet only - nothing was changed. Promote per Memory/Memory.md, then prune Log.md with user approval.")
    print(divider())
    return 0


_CHANGELOG_SECTIONS = {"major": "## Major Updates", "minor": "## Minor Updates",
                       "patch": "## Patch Updates"}


def cmd_changelog(raw: list = None) -> int:
    """🧾 Changelog discipline (Constitution 3.6) without the manual version
    math. `changelog` prints the current version. `changelog add <patch|minor|
    major> "description" [files="a, b"]` backs up changelog.md, computes the
    bump, inserts a correctly formatted entry at the top of the right section,
    enforces the 4-entry cap, and updates the Current Version line."""
    raw = raw or []
    cl = SYSTEM_DIR / "changelog.md"
    if not raw or raw[0] in ("version", "current"):
        v = _brain_version()
        print(f"  Current BRAIN version: {v or 'unreadable'}")
        if not raw:
            print('  Add an entry: changelog add <patch|minor|major> "description" [files="a, b"]')
        return 0 if v else 1
    if raw[0] != "add" or len(raw) < 3 or raw[1].lower() not in _CHANGELOG_SECTIONS:
        fail('Usage: changelog add <patch|minor|major> "description" [files="a, b"] [backup="name"]')
        return 2
    level, desc = raw[1].lower(), raw[2].strip()
    kv = {k: v for k, v in (a.split("=", 1) for a in raw[3:] if "=" in a)}
    if len(desc) < 15:
        fail("Description too thin - say what changed and where (one or two sentences).")
        return 1
    header("Changelog Entry", "🧾")
    try:
        text = cl.read_text(encoding="utf-8")
    except OSError as e:
        fail(f"Cannot read changelog: {e}")
        return 1
    m = re.search(r"\*\*`(\d{2})\.(\d{2})\.(\d{2})`\*\*", text)
    if not m:
        fail("Current Version line not found - changelog structure changed; refusing to guess.")
        return 1
    major, minor, patch = (int(x) for x in m.groups())
    if level == "major":
        major, minor, patch = major + 1, 0, 0
    elif level == "minor":
        minor, patch = minor + 1, 0
    else:
        patch += 1
    new_v = f"{major:02d}.{minor:02d}.{patch:02d}"
    if f"### `{new_v}`" in text:
        fail(f"An entry for {new_v} already exists - refusing to duplicate.")
        return 1
    section = _CHANGELOG_SECTIONS[level]
    sm = re.search(re.escape(section) + r"\s*\n+(>[^\n]*\n+)?", text)
    if not sm:
        fail(f"Section heading '{section}' not found - refusing to guess.")
        return 1
    # Backup before editing (Section 10) - quiet, same naming convention.
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    bdir = SYSTEM_DIR / ".backups"
    bname = f"system-changelog-{ts}.md"
    try:
        bdir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(cl), str(bdir / bname))
    except OSError as e:
        logging.getLogger("changelog").error("pre-edit backup failed: %s", e)
        fail(f"Backup failed - not editing without one: {e}")
        return 1
    _backup_rotate(quiet=True)
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    entry = f"### `{new_v}` - {day}\n\n{desc}\n"
    if kv.get("files"):
        entry += f"\n**Files affected:** {kv['files']}\n"
    if kv.get("backup"):
        entry += f"**Backup:** {kv['backup']}\n"
    entry += "\n"
    text = text[:sm.end()] + entry + text[sm.end():]
    # 4-entry cap: drop the oldest block(s) in this section only.
    sec_start = text.find(section)
    next_sec = re.search(r"^## ", text[sec_start + len(section):], re.MULTILINE)
    sec_end = sec_start + len(section) + (next_sec.start() if next_sec else len(text))
    sec_text = text[sec_start:sec_end]
    blocks = list(re.finditer(r"^### `", sec_text, re.MULTILINE))
    if len(blocks) > 4:
        cut_from = sec_start + blocks[4].start()
        text = text[:cut_from] + text[sec_end:]
        warn(f"Section over the 4-entry cap - oldest entry aged out (the cap is hard; history lives in backups/git).")
    text = re.sub(r"\*\*`\d{2}\.\d{2}\.\d{2}`\*\*", f"**`{new_v}`**", text, count=1)
    # The changelog's own per-file version moves one PATCH with every entry:
    # this write changes the file, and a version left unmoved would flag as
    # drift debt in health (Instructions 8.6) for the engine's own edit.
    fmb2 = _fm_bounds(text)
    fvm = re.search(r'(?m)^version:\s*"(\d+)\.(\d+)\.(\d+)"\s*$',
                    text[fmb2[0]:fmb2[1]] if fmb2 else "")
    if fvm:
        cM, cN, cP = (int(x) for x in fvm.groups())
        text, _ = _sub_frontmatter(text, r'^version:\s*".*"\s*$',
                                   f'version: "{cM:02d}.{cN:02d}.{cP + 1:02d}"')
    text, _ = _sub_frontmatter(text, r'^updated:\s*.*$', f'updated: {day}')
    try:
        cl.write_text(text, encoding="utf-8")
    except OSError as e:
        fail(f"Write failed: {e} - original is safe in {bname}")
        logging.getLogger("changelog").error(e, exc_info=True)
        return 1
    ok(f"Version {m.group(0).strip('*`')} → {new_v}  ({level.upper()})")
    ok(f"Entry added under {section}.  Backup: {bname}")
    return 0


def cmd_bump(raw: list = None) -> int:
    """⬆️ Bump a core file's per-file version (MAJOR.MINOR.PATCH). Usage:
    bump "<file>" <major|minor|patch>. The level is required - you classify the
    change (major = breaking/restructure, minor = additive, patch = fix); the
    command does the math, backs the file up, and writes `version` + `updated`.
    Content files carry no version (see _is_core_file)."""
    header("Version Bump", "⬆️ ")
    raw = raw or []
    if len(raw) < 2:
        fail('Usage: bump "<file>" <major|minor|patch>')
        return 1
    target, level = raw[0], raw[1].strip().lower()
    if level not in ("major", "minor", "patch"):
        fail(f"Level must be major, minor, or patch - got '{raw[1]}'")
        return 1
    p = (BRAIN_DIR / target) if not Path(target).is_absolute() else Path(target)
    try:
        p = p.resolve()
        p.relative_to(BRAIN_DIR.resolve())
    except (OSError, ValueError):
        fail(f"Not a file inside this BRAIN: {target}")
        return 1
    if not p.is_file():
        fail(f"File not found: {target}")
        return 1
    fm = parse_frontmatter(p)
    if not fm:
        # Refuse a file with no YAML frontmatter block: the version regexes
        # would otherwise hit look-alike lines deep in the body (a scaffold
        # template inside this engine was corrupted exactly that way on
        # 2026-07-01). Non-markdown core files (the engine itself) are
        # versioned by the system changelog, not per-file frontmatter.
        fail(f"{rel(p)} has no YAML frontmatter - only markdown core files "
             f"carry a per-file version (Instructions 8.6); the engine is "
             f"versioned by System/changelog.md.")
        return 1
    cur = str(fm.get("version", "") or "")
    if cur and not VERSION_RE.fullmatch(cur):
        fail(f"Current version '{cur}' is not MM.mm.pp - fix it before bumping.")
        return 1
    if not cur:
        # No version yet: seed at 01.00.00 (a created file's starting point).
        new_major, new_minor, new_patch = 1, 0, 0
    else:
        major, minor, patch = (int(x) for x in cur.split("."))
        if level == "major":
            new_major, new_minor, new_patch = major + 1, 0, 0
        elif level == "minor":
            new_major, new_minor, new_patch = major, minor + 1, 0
        else:
            new_major, new_minor, new_patch = major, minor, patch + 1
    new_v = f"{new_major:02d}.{new_minor:02d}.{new_patch:02d}"
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # Pre-edit backup (Section 10.1), quiet.
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    bdir = SYSTEM_DIR / ".backups"
    try:
        bdir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(p), str(bdir / _backup_dest_name(p, ts)))
    except OSError as e:
        fail(f"Backup failed - not editing without one: {e}")
        return 1
    _backup_rotate(quiet=True)
    try:
        text = p.read_text(encoding="utf-8")
    except OSError as e:
        fail(f"Cannot read file: {e}")
        return 1
    fmb = _fm_bounds(text)
    fm_block = text[fmb[0]:fmb[1]] if fmb else ""
    if not fm_block:
        fail("No frontmatter block found - refusing to guess an insertion point.")
        return 1
    if re.search(r'(?m)^version:\s*', fm_block):
        text, _ = _sub_frontmatter(text, r'^version:\s*.*$', f'version: "{new_v}"')
    elif re.search(r'(?m)^policy:\s*', fm_block):
        text, _ = _sub_frontmatter(text, r'^(policy:\s*.*)$', r'\1' + f'\nversion: "{new_v}"')
    elif re.search(r'(?m)^created:\s*', fm_block):
        text, _ = _sub_frontmatter(text, r'^(created:\s*.*)$', f'version: "{new_v}"' + r'\n\1')
    else:
        fail("No insertion point for version (no policy/created field in frontmatter).")
        return 1
    text, _ = _sub_frontmatter(text, r'^updated:\s*.*$', f'updated: {day}')
    try:
        p.write_text(text, encoding="utf-8")
    except OSError as e:
        fail(f"Write failed: {e}")
        return 1
    ok(f"{rel(p)}:  {cur or 'none'} -> {new_v}  ({level.upper()})")
    print(divider())
    print(f"  🏁  Version bumped. Run manifest to refresh the index.")
    print(divider())
    return 0


def _git(args: list, timeout: int = 60):
    return run(["git", "-C", str(BRAIN_DIR)] + args, timeout=timeout)


def _in_icloud() -> bool:
    return "Mobile Documents" in str(BRAIN_DIR)


def cmd_git(subcmd: str = "status", message: str = "") -> int:
    """🌿 Vault versioning. `git status`: repo state + uncommitted changes.
    `git init`: create the repo (in iCloud, uses --separate-git-dir outside the
    synced folder - iCloud corrupts live .git dirs via sync-conflict duplicates
    and file eviction). `git snapshot ["msg"]`: stage everything and commit -
    the multi-file restore point that per-file Backups/ cannot give you."""
    header("Vault Git", "🌿")
    sub = (subcmd or "status").strip().lower()
    probe = run(["git", "--version"])
    if probe.returncode != 0:
        fail("git is not installed or not on PATH.")
        return 1
    has_repo = _git(["rev-parse", "--is-inside-work-tree"]).stdout.strip() == "true"
    if sub == "init":
        if has_repo:
            ok("Repo already exists.")
            return 0
        print(f"  BRAIN root: {BRAIN_DIR}")
        if _in_icloud():
            print("\n  ⚠️   This vault lives in iCloud Drive. A live .git directory inside iCloud")
            print("       gets corrupted by sync (conflict-duplicated refs, evicted objects).")
            print("       Using --separate-git-dir: the repo lives outside iCloud; only a tiny")
            print("       .git pointer file sits in the vault. The pointer is machine-local")
            print("       infrastructure (like .obsidian/) - on a new machine, re-run `git init`.")
        if not confirm("Initialize git for this BRAIN? (yes/no): "):
            warn("Cancelled.")
            return 1
        if _in_icloud():
            gd = Path.home() / ".local" / "share" / "brain-git" / (BRAIN_DIR.name + ".git")
            gd.parent.mkdir(parents=True, exist_ok=True)
            r = run(["git", "init", "--separate-git-dir", str(gd), str(BRAIN_DIR)])
        else:
            r = _git(["init"])
        if r.returncode != 0:
            fail(f"git init failed: {r.stderr.strip()}")
            logging.getLogger("git").error(r.stderr.strip())
            return 1
        # Repo-local identity so snapshots work even on a machine with no
        # global git config (identity is metadata, not authentication).
        if not _git(["config", "user.email"]).stdout.strip():
            _git(["config", "user.name", AUTHOR])
            _git(["config", "user.email", "brain@local"])
        ok("Repository initialized.")
        print("  Also recommended: disable 'Optimize Mac Storage' for iCloud Drive, and")
        print("  never run git on two Macs syncing this folder at once.")
        print("  First snapshot: python3 System/brain.command git snapshot \"initial\"")
        return 0
    if not has_repo:
        warn("No git repo. Create one with: git init  (via this command).")
        return 1
    if sub == "snapshot":
        st = _git(["status", "--porcelain"]).stdout.strip()
        if not st:
            ok("Nothing to snapshot - working tree clean.")
            return 0
        n = len(st.split("\n"))
        msg = message.strip() or f"snapshot: {n} file(s) changed (v{_brain_version() or '?'})"
        if _git(["add", "-A"]).returncode != 0:
            fail("git add failed.")
            return 1
        r = _git(["commit", "-m", msg])
        if r.returncode != 0 and "Author identity unknown" in (r.stderr or ""):
            _git(["config", "user.name", AUTHOR])
            _git(["config", "user.email", "brain@local"])
            r = _git(["commit", "-m", msg])
        if r.returncode != 0:
            fail(f"commit failed: {(r.stderr or r.stdout).strip()[:200]}")
            logging.getLogger("git").error(r.stderr.strip())
            return 1
        ok(f"Committed: {msg}")
        stat = _git(["show", "--stat", "--oneline", "-s", "HEAD"]).stdout.strip()
        if stat:
            print(f"    {stat.splitlines()[0]}")
        return 0
    # status (default)
    st = _git(["status", "--porcelain"]).stdout.strip()
    last = _git(["log", "-1", "--format=%h %ad %s", "--date=short"]).stdout.strip()
    print(f"  Last commit : {last or '(none yet)'}")
    print(f"  Uncommitted : {len(st.split(chr(10))) if st else 0} file(s)")
    if st:
        for ln in st.split("\n")[:15]:
            print(f"    {ln}")
        if len(st.split(chr(10))) > 15:
            print(f"    … and {len(st.split(chr(10))) - 15} more")
        print("\n  Snapshot them: git snapshot \"message\"")
    return 1 if st else 0


def cmd_rename(old: str = "", new: str = "") -> int:
    """✏️  Backlink-safe rename (Articles 2.6 + 3.7). Renames a file AND
    rewrites every [[wikilink]] that points at it, with backups of everything
    touched first - a bare `mv` silently breaks the knowledge graph."""
    header("Backlink-Safe Rename", "✏️")
    if not old or not new:
        print("  Usage: rename <BRAIN-relative path> <new filename (same folder)>")
        return 2
    p = BRAIN_DIR / old
    if not p.is_file():
        rp = _resolve_md(old)
        if rp is None:
            fail(f"File not found: {old}")
            return 1
        p = rp
    if {"Backups", ".backups"} & set(p.parts):
        fail("Never rename backups - they are verbatim restore copies.")
        return 1
    new = new.strip()
    if "/" in new:
        fail("Give a filename only - rename keeps the file in its folder (use a separate move for relocation).")
        return 1
    if not Path(new).suffix:
        new += p.suffix
    if "_" in new or re.search(r"[<>:\"\\|?*]", new):
        fail(f"'{new}' breaks naming law (Article 2.6): no underscores or special characters.")
        return 1
    dest = p.parent / new
    if dest.exists():
        fail(f"Target already exists: {rel(dest)}")
        return 1
    old_stem, new_stem = p.stem, Path(new).stem
    # Resolve-then-rewrite: a link is touched only when it actually resolves
    # to the renamed file. A path-qualified target must match p's vault path
    # at a path boundary; a bare stem matches only when p is the unique file
    # with that stem in the graph. Basename-only matching once rewrote links
    # aimed at an unrelated same-named file (found live 2026-07-03).
    old_rel = rel(p).lower()
    old_rel_noext = old_rel[:-len(p.suffix)] if p.suffix else old_rel
    stem_unique = not any(f != p and f.stem.lower() == old_stem.lower()
                          for f in _graph_sources())

    def _link_resolves_to_renamed(target: str) -> bool:
        t = target.strip().lower()
        if not t:
            return False
        tn = t[:-len(p.suffix)] if p.suffix and t.endswith(p.suffix.lower()) else t
        if "/" in tn:
            return old_rel_noext == tn or old_rel_noext.endswith("/" + tn)
        return stem_unique and tn == old_stem.lower()
    # Find every md file whose wikilinks resolve to this file.
    pat = re.compile(r"\[\[([^\]\|#\n\\]+)(\\?[#\|][^\]]*)?\]\]")
    referers = []
    for src in _graph_sources():
        if src == p:
            continue
        try:
            text = src.read_text(encoding="utf-8")
        except OSError:
            continue
        hit = any(_link_resolves_to_renamed(m.group(1)) for m in pat.finditer(text))
        if hit:
            referers.append(src)
    print(f"  {rel(p)}  →  {new}")
    print(f"  {len(referers)} file(s) link to it and will be rewritten:")
    for srf in referers:
        print(f"    🔗  {rel(srf)}")
    if not confirm("Proceed with rename + rewrite? (yes/no): "):
        warn("Cancelled.")
        return 1
    # Backups first (Section 10) - the renamed file and every referer.
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    bdir = SYSTEM_DIR / ".backups"
    bdir.mkdir(parents=True, exist_ok=True)
    for f in [p] + referers:
        try:
            shutil.copy2(str(f), str(bdir / _backup_dest_name(f, ts)))
        except OSError as e:
            logging.getLogger("rename").error("backup failed for %s: %s", rel(f), e)
            fail(f"Backup failed for {rel(f)} - aborting before any change: {e}")
            return 1
    _backup_rotate(quiet=True)

    def _rewrite(match):
        target, tail = match.group(1), match.group(2) or ""
        if not _link_resolves_to_renamed(target):
            return match.group(0)
        tpath = Path(target.strip())
        parent = str(tpath.parent)
        newname = new_stem if tpath.suffix == "" else new
        fixed = (parent + "/" if parent not in (".", "") else "") + newname
        return f"[[{fixed}{tail}]]"

    changed = 0
    for src in referers:
        try:
            text = src.read_text(encoding="utf-8")
            new_text = pat.sub(_rewrite, text)
            if new_text != text:
                src.write_text(new_text, encoding="utf-8")
                changed += 1
        except OSError as e:
            fail(f"Rewrite failed in {rel(src)}: {e}")
            logging.getLogger("rename").error(e, exc_info=True)
    try:
        p.rename(dest)
    except OSError as e:
        logging.getLogger("rename").error("rename failed: %s", e)
        fail(f"Rename failed: {e}")
        return 1
    # Fix the file's own path frontmatter.
    if dest.suffix == ".md":
        try:
            text = dest.read_text(encoding="utf-8")
            text = text.replace(f'path: "BRAIN/{rel(p)}"', f'path: "BRAIN/{rel(dest)}"', 1)
            dest.write_text(text, encoding="utf-8")
        except OSError:
            pass
    ok(f"Renamed to {rel(dest)}; rewrote links in {changed} file(s). Backups: *-{ts}.*")
    print("\n  Now run: sync  →  manifest  →  links check   (tags, index, graph all moved)")
    print("  Review the file's `title:` frontmatter - rename does not rewrite titles.")
    return 0


def _bundle_print(title: str, files: list, json_out: bool, extra_json: dict = None) -> int:
    """Shared renderer for folder bundles: token total first, then contents.
    Past 30k tokens, asks before printing (lean-loading guard, Section 15)."""
    files = [f for f in files if f.is_file()]
    total = sum(count_tokens(f) for f in files)
    if json_out:
        out = {"bundle": title, "total_tokens": total,
               "files": [{"path": rel(f), "tokens": count_tokens(f)} for f in files]}
        if extra_json: out.update(extra_json)
        print(json.dumps(out, separators=(",", ":")))
        return 0
    header(f"Bundle: {title}", "📂")
    print(f"  {len(files)} file(s), ~{total:,} tokens\n")
    if total > 30000 and not AUTO_CONFIRM:
        warn("Large bundle (> 30,000 tokens). Prefer load for routine work (Section 15).")
        if not confirm("Print it anyway? (yes/no): "):
            print("\n  🚫  Aborted.\n"); return 0
    for f in files:
        print(f"===== FILE: {rel(f)}  (~{count_tokens(f)} tokens) =====")
        try:
            print(f.read_text(encoding="utf-8").rstrip())
        except OSError as e:
            logging.getLogger("folder").error("unreadable %s: %s", rel(f), e)
            fail(f"unreadable: {e}")
        print()
    print(divider())
    print(f"  🏁  {title}: {len(files)} file(s), ~{total:,} tokens.")
    print(divider())
    return 0


def cmd_folder(preset: str = "", name: str = "", json_out: bool = False) -> int:
    """📂 Curated folder bundles - a whole context area in one call, without reading
    files one by one. Presets: profile (hub + key self facets) · memory (map, Log,
    Dates, the collection indexes + 2 newest summaries) · ventures [Name] (portfolio snapshot, or one venture
    deep) · projects [Name] (same) · library (catalog only - titles and token
    costs, never contents). Menu accelerators: i r v p l. --json lists paths/costs."""
    preset = preset.strip().lower()
    if preset in ("profile", "identity", "i"):
        base = BRAIN_DIR / "Profile"
        return _bundle_print("Profile", [
            base / "Profile.md",
            base / "Working Style.md",
            base / "Biography.md",
            base / "Personality.md",
            base / "Values" / "Values.md",
            base / "Focus.md",
        ], json_out)
    if preset in ("memory", "recall", "r"):
        base = BRAIN_DIR / "Memory"
        # Lean snapshot: the map (Memory.md), staging (Log), dates, and every
        # collection index doc from MEMORY_COLLECTIONS (individual entries read
        # on demand, not in a whole-area bundle), plus the 2 newest summaries.
        files = [base / "Memory.md", base / "Log.md", base / "Dates.md"]
        files += [folder / f"{cname}.md" for cname, folder, _kind, _ph in MEMORY_COLLECTIONS]
        files += sorted(_memory_files(base / "Context" / "Current"), reverse=True)[:2]
        files = [f for f in files if f.exists()]
        return _bundle_print("Memory Recall", files, json_out)
    if preset in ("ventures", "v", "projects", "p"):
        kind = "Ventures" if preset in ("ventures", "v") else "Projects"
        base = BRAIN_DIR / kind
        if name:
            hits = [d for d in base.iterdir() if d.is_dir() and d.name != "Template"
                    and d.name.lower() == name.strip().lower()]
            if not hits:
                fail(f"No {kind[:-1].lower()} folder named '{name}'. List with: db search folder={kind.lower()}")
                return 1
            inst = hits[0]
            return _bundle_print(f"{kind[:-1]}: {inst.name}",
                                 sorted(inst.rglob("*.md")), json_out)
        files = [base / f"{kind}.md"]
        for d in sorted(base.iterdir()):
            if d.is_dir() and d.name != "Template":
                files += [d / "Overview.md"] + ([d / "Goals.md"] if kind == "Ventures" else [])
        return _bundle_print(f"{kind} Snapshot", files, json_out)
    if preset in ("library", "l"):
        # Catalog only - Library is never read whole (Section 15).
        idx = load_index()
        cats = {}
        for e in idx.get("files", []):
            path = e.get("path", "")
            if not path.startswith("BRAIN/Library/"):
                continue
            parts = path.split("/")
            cat = "/".join(parts[2:4]) if len(parts) > 4 else (parts[2] if len(parts) > 3 else "(root)")
            cats.setdefault(cat, []).append((e.get("title", parts[-1]), e.get("tokens", 0)))
        if json_out:
            print(json.dumps({"bundle": "Library Catalog",
                              "categories": {c: [{"title": t, "tokens": k} for t, k in v]
                                             for c, v in sorted(cats.items())}}, separators=(",", ":")))
            return 0
        header("Bundle: Library Catalog", "📂")
        total_files = sum(len(v) for v in cats.values())
        for c in sorted(cats):
            print(f"  📚 {c}  ({len(cats[c])} file(s))")
            for t, k in sorted(cats[c]):
                print(f"      {t}  (~{k:,} tokens)")
        print()
        print(divider())
        print(f"  🏁  {total_files} file(s) across {len(cats)} categories. Read sources with read, find with search.")
        print(divider())
        return 0
    print("  Usage: folder profile | memory | ventures [Name] | projects [Name] | library")
    print("  Menu accelerators: i (Profile) · r (Recall) · v (Ventures) · p (Projects) · l (Library)")
    return 0 if not preset else 1



def cmd_help() -> int:
    """❓ One-screen explanation of every command, generated from the commands'
    own docstrings so it can never drift from the code. Menu key: h. CLI: help."""
    header("Command Guide", "❓")
    # Emoji set stripped from each docstring's first line: built from the MENU
    # itself (plus legacy docstring emoji) so a new menu entry cannot drift it.
    emoji_set = ("".join(e for _, e, _, _ in MENU)
                 + "🩺📥🔎💾🧠🆕📋📊🔄🪙📝⏰🔍🚀📖🔗📨🗂🗒🧹🧾🌿✏️📦🪵📚❓📂️ ")
    for pg in range(N_PAGES):
        title = PAGE_TITLES[pg] if pg < len(PAGE_TITLES) else "More"
        items = MENU[pg * PAGE_SIZE:(pg + 1) * PAGE_SIZE]
        print(f"  -- {title} " + "-" * max(1, 40 - len(title)))
        for name, emoji, _label, fn in items:
            doc = (fn.__doc__ or "").strip().splitlines()
            first = doc[0].lstrip(emoji_set).strip() if doc else ""
            print(f"  {emoji} {name:<11} {first[:88]}")
        print()
    print("  -- Subcommands " + "-" * 26)
    print("  memory list|status|cascade|add|rm|supersede|sync · summary new|latest|status")
    print("  profile add|rm|sync|coverage [\"Facet\"] [--json]  (coverage is read-only)")
    print("  backup list|clear · logs · logs clear errors|reports|all  (snapshot, then empty)")
    print("  friction \"kind: what\" [--target <f>] [--severity low|med|high] · friction list [N]")
    print("  sync all|verify|tag <file> <tags…> · skill list|validate|package <name|all>")
    print("  agents validate <name|all>|catalog · db build|rollup|search|status")
    print("  kb search|read|list|refresh · trash <path>|list|restore <item>|empty [item]")
    print("  git status|init|snapshot \"msg\" · changelog add <patch|minor|major> \"desc\"")
    print("  bump \"<file>\" <patch|minor|major>  (per-file version, core files only)")
    print("  manifest full · links check|orphans|stats|subfolders · read <file> [section]|--toc|--fm")
    print("  index verify · gitkeep|gitkeep check")
    print("  folder profile|memory|ventures [Name]|projects [Name]|library  (menu: i r v p l)")
    print()
    print("  -- Agent notes " + "-" * 26)
    print("  --yes auto-confirms · --json on load/startup for machine output")
    print("  Exit codes: lint/stale/diff/inbox exit 1 on findings - branch on $?")
    print("  Context gauge: every command ends with [ctx ~N tokens served]; startup resets it.")
    print("  At 60k+: update the session summary at a task boundary. At 90k+: write it and tell the user.")
    print("  The situation→command playbook: Instructions.md Section 4.4")
    print(divider())
    return 0



# Paged interactive menu: 5 commands per page, ordered by importance
# (most-used first). `n` pages forward, `b` pages back, `q` quits; typing a
# command name works from any page. Direct CLI invocation accepts every name.
MENU = [
    # Page boundaries below follow the PAGE_SIZE=5 slicing exactly - keep the
    # comments, PAGE_TITLES, and the 5-per-page arithmetic in agreement.
    # Page 1 - Session Core
    ("startup",  "🚀", "Session Startup",       cmd_startup),
    ("health",   "🩺", "Health Check",          cmd_health),
    ("load",     "📥", "Context Load",          cmd_load),
    ("read",     "📖", "Surgical Read",         cmd_read),
    ("backup",   "💾", "Backup File",           cmd_backup),
    # Page 2 - Capture & Create
    ("remember", "🧠", "Log Memory",            cmd_remember),
    ("summary",  "📝", "Session Summary",       cmd_summary),
    ("inbox",    "📬", "Inbox Status",          cmd_inbox),
    ("new",      "🆕", "New Project / Venture", cmd_new),
    ("memory",   "🧠", "Tiered Memory",         cmd_memory),
    # Page 3 - Profile, Graph & Sync
    ("profile",  "🪪", "Profile entries",        cmd_profile),
    ("consolidate", "🧹", "Consolidation Worksheet", cmd_consolidate),
    ("links",    "🕸️ ", "Wikilink Graph",        cmd_links),
    ("rename",   "✏️ ", "Rename (backlink-safe)", cmd_rename),
    ("sync",     "🔄", "Sync Finder Tags",      cmd_sync),
    # Page 4 - Index & History
    ("manifest", "📋", "Rebuild Index",         cmd_manifest),
    ("diff",     "📊", "Change Diff",           cmd_diff),
    ("db",       "🗄️ ", "Database / Search",      cmd_db),
    ("kb",       "📚", "Knowledge Base",        cmd_kb),
    ("changelog","🧾", "Changelog Entry",       cmd_changelog),
    # Page 5 - Toolkit & Checks
    ("git",      "🌱", "Git Snapshot",          cmd_git),
    ("skill",    "📦", "Skill Packager",        cmd_skill),
    ("agents",   "🧩", "Agent Library",         cmd_agents),
    ("lint",     "🔍", "Frontmatter Lint",      cmd_lint),
    ("stale",    "⏰", "Stale Scan",            cmd_stale),
    # Page 6 - Maintenance
    ("gitkeep",  "📌", "Gitkeep Maintenance",   cmd_gitkeep),
    ("trash",    "🗑️ ", "Two-Stage Trash",       cmd_trash),
    ("index",    "🗂️ ", "Registry Verify",       cmd_index),
    ("tokens",   "🪙", "Token Estimates",       cmd_tokens),
    ("bump",     "⬆️ ", "Version Bump",          cmd_bump),
    # Page 7 - Logs & Friction
    ("logs",     "🧽", "Clear Logs",            cmd_logs),
    ("friction", "🪵", "Friction Ledger",       cmd_friction),
]
PAGE_TITLES = ["Session Core", "Capture & Create", "Profile, Graph & Sync",
               "Index & History", "Toolkit & Checks", "Maintenance",
               "Logs & Friction"]
PAGE_SIZE   = 5
N_PAGES     = (len(MENU) + PAGE_SIZE - 1) // PAGE_SIZE

# Flat name → command map for direct CLI invocation (all commands)
NAME_MAP = {name: (name, emoji, label, fn) for name, emoji, label, fn in MENU}


def _clear() -> None:
    """Clear the terminal completely: screen AND scrollback, so every menu render
    starts truly fresh with no residue from prior commands. \033[3J erases the
    scrollback buffer (supported by Terminal.app and iTerm2); \033[2J\033[H
    clears the visible screen and homes the cursor. Falls back silently when
    not attached to a terminal."""
    if sys.stdout.isatty():
        print("\033[2J\033[3J\033[H", end="")
        sys.stdout.flush()


def _menu_header() -> None:
    """Print the shared banner shown at the top of every menu."""
    W   = "=" * 54
    now = datetime.now(timezone.utc)
    print()
    print(W)
    print("🧠  BRAIN System Tools")
    print(W)
    print(f"  Developer : {AUTHOR}")
    print(f"  Website   : {WEBSITE}")
    # Show the live BRAIN system version from the changelog, so the banner is
    # never stale. Falls back to the static VERSION constant if unreadable.
    print(f"  Version   : {('v' + _brain_version()) if _brain_version() else VERSION}")
    print(f"  Created   : {CREATED}")
    print(f"  Updated   : {_fmt_date(now)}")
    print(W)


def _run_and_return(fn) -> None:
    """Clear screen, run a command, then pause so the user can read output."""
    _clear()
    fn()
    input("\n  Press Enter to return to menu...")


def print_menu(page: int) -> None:
    RULE = "-" * 26
    _clear()
    _menu_header()
    items = MENU[page * PAGE_SIZE:(page + 1) * PAGE_SIZE]
    print()
    print(f"🧭 {PAGE_TITLES[page] if page < len(PAGE_TITLES) else 'More'}   (page {page + 1}/{N_PAGES})")
    print(RULE)
    print()
    for i, (_name, emoji, label, _fn) in enumerate(items, 1):
        print(f"{i})  {emoji}  {label}")
    print(RULE)
    print()
    print("📂  Bundles")
    print()
    print("i)  🪪  Profile")
    print("r)  💭  Recall (Memory)")
    print("v)  🏢  Ventures")
    print("p)  🧩  Projects")
    print("l)  📚  Library")
    print()
    print(RULE)
    print()
    print(f"s)  Search  ·  n)  Next  ·  b)  Back  ·  h)  Help  ·  q)  Quit")
    print()


def menu_loop() -> int:
    page = 0
    while True:
        print_menu(page)
        try:
            choice = input("  Choose (1–5, s, i/r/v/p/l, n, b, h, or q): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            # No TTY (piped or non-interactive) or Ctrl-D/Ctrl-C: quit cleanly
            # rather than crashing with an uncaught EOFError into errors.log.
            _clear(); print("\n  👋  Goodbye.\n"); return 0
        if choice in ("q", "quit", "exit"):
            _clear(); print("\n  👋  Goodbye.\n"); return 0
        if choice in ("n", "next"):
            page = (page + 1) % N_PAGES; continue
        if choice in ("b", "back"):
            page = (page - 1) % N_PAGES; continue
        if choice in ("h", "help", "?"):
            _run_and_return(cmd_help); continue
        if choice in ("s", "search"):
            _run_and_return(cmd_search); continue
        if choice in ("i", "r", "v", "p", "l"):
            _run_and_return(lambda c=choice: cmd_folder(c)); continue
        items = MENU[page * PAGE_SIZE:(page + 1) * PAGE_SIZE]
        fn = None
        if choice.isdigit() and 1 <= int(choice) <= len(items):
            fn = items[int(choice) - 1][3]
        elif choice in NAME_MAP:
            fn = NAME_MAP[choice][3]
        if fn:
            _run_and_return(fn); continue
        print(f"\n  ⚠️   '{choice}' is not a valid option. Try 1–5, s, n, b, h, i/r/v/p/l, or q.")
        try:
            input("  Press Enter to continue...")
        except EOFError:
            pass


# ══════════════════════════════════════════════════════════
#  Entry Point
# ══════════════════════════════════════════════════════════

def _heal_exec_bit() -> None:
    """Re-grant the executable bit on this script if an editor stripped it.
    AI tools that rewrite files routinely drop +x, which breaks Finder's
    double-click ('you do not have appropriate access privileges'). Any run via
    `python3 brain.command …` repairs it automatically, so routine maintenance
    keeps double-click working. Best-effort: failure is silently ignored."""
    try:
        if not os.access(__file__, os.X_OK):
            os.chmod(__file__, os.stat(__file__).st_mode | 0o700)
    except OSError:
        pass


def _validate_brain() -> bool:
    """Confirm we are running inside a valid BRAIN (Instructions.md + Constitution.md at root)."""
    ok_flag = (BRAIN_DIR / "Instructions.md").exists() and (BRAIN_DIR / "Constitution.md").exists()
    if not ok_flag:
        print(f"\n  ❌  BRAIN root not found.")
        print(f"       Expected Instructions.md and Constitution.md at: {BRAIN_DIR}")
        print(f"       This file must live at BRAIN/System/brain.command\n")
    return ok_flag


def _finish_ledger(rc: int, json_out: bool) -> int:
    """Count this command's output into the session ledger and, for non-JSON
    output, print the context gauge line (JSON stays parseable)."""
    out = sys.stdout
    if isinstance(out, _CountingWriter):
        sys.stdout = out.stream
        data = _ledger_add(max(1, out.chars // CHARS_PER_TOKEN))
        if not json_out:
            print(f"  {_ledger_footer(data)}")
    _cmd, _argv = _INVOKED
    _mut, _label = _is_mutating(_cmd, _argv)
    if _mut:
        _report(_label, rc)
    return rc


def main() -> int:
    global AUTO_CONFIRM
    _heal_exec_bit()
    if not _validate_brain():
        return 1
    try:
        args = sys.argv[1:]
        # Global flags, position-independent (agent-friendly)
        if "--yes" in args:
            AUTO_CONFIRM = True
            args = [a for a in args if a != "--yes"]
        json_out = "--json" in args
        if json_out:
            args = [a for a in args if a != "--json"]
        if not args:
            return menu_loop()
        cmd = args[0].lower()
        # --json honesty: only load, startup, folder, and profile coverage
        # implement a JSON mode. Anything else would strip the flag and print
        # human text an agent then tries to parse - fail fast and loud instead.
        if json_out and cmd not in ("load", "startup", "folder") \
                and not (cmd == "profile" and len(args) > 1
                         and args[1].lower() == "coverage"):
            print(f"  ❌  --json is not supported by '{cmd}'")
            return 2
        extra = args[1] if len(args) > 1 else ""
        extra2 = args[2] if len(args) > 2 else ""
        global _INVOKED
        _INVOKED = (cmd, args)
        sys.stdout = _CountingWriter(sys.stdout)
        if cmd in ("help", "-h", "--help", "?"):
            return _finish_ledger(cmd_help(), json_out)
        # Commands that accept extra arguments
        if cmd == "search":
            # Optional filters anywhere after the query: folder=<f> type=<t>.
            # Every other bare word joins the query, so `search lean build`
            # searches "lean build" instead of silently dropping "build".
            filters = {k: v for k, v in
                       (a.split("=", 1) for a in args[1:] if "=" in a)}
            words = [a for a in args[1:] if "=" not in a and not a.startswith("--")]
            return _finish_ledger(cmd_search(query=" ".join(words),
                              folder_filter=filters.get("folder", ""),
                              type_filter=filters.get("type", "")), json_out)
        if cmd == "load":
            # Every bare word joins the task; a lone integer is the token
            # budget (documented form: load "task" 30000), never task text.
            words = [a for a in args[1:] if "=" not in a and not a.startswith("--")]
            nums = [a for a in words if a.isdigit()]
            task = " ".join(a for a in words if not a.isdigit())
            return _finish_ledger(cmd_load(task=task, budget=nums[0] if nums else "",
                                           json_out=json_out), json_out)
        if cmd == "remember":
            return _finish_ledger(cmd_remember(args[1:]), json_out)
        if cmd == "friction":
            return _finish_ledger(cmd_friction(args[1:]), json_out)
        if cmd == "backup":
            force_local = extra2.strip().lower() in ("local", "--force", "force", "--local")
            return _finish_ledger(cmd_backup(target=extra, force_local=force_local), json_out)
        if cmd == "new":
            return _finish_ledger(cmd_new(kind_arg=extra, name_arg=extra2), json_out)
        if cmd == "memory":
            return _finish_ledger(cmd_memory(args[1:]), json_out)
        if cmd == "profile":
            return _finish_ledger(cmd_profile(args[1:], json_out=json_out), json_out)
        if cmd == "skill":
            return _finish_ledger(cmd_skill(subcmd=extra, name=extra2), json_out)
        if cmd in ("agents", "agent"):
            return _finish_ledger(cmd_agents(subcmd=extra, name=extra2), json_out)
        if cmd == "startup":
            man = "--manifest" in args[1:]
            # Ledger model: the first non-flag word, wherever it sits - so
            # `startup --manifest claude-1m` still sets the window.
            model = next((a for a in args[1:] if not a.startswith("--")), "")
            _ledger_reset(model=model)  # a new session begins - fresh context gauge
            return _finish_ledger(cmd_startup(json_out=json_out, manifest=man), json_out)
        if cmd == "read":
            flags = [a for a in args[1:] if a.startswith("--")]
            rest = [a for a in args[1:] if not a.startswith("--")]
            return _finish_ledger(cmd_read(target=rest[0] if rest else "",
                            section=" ".join(rest[1:]),
                            fm_only="--fm" in flags, toc="--toc" in flags), json_out)
        if cmd == "links":
            return _finish_ledger(cmd_links(subcmd=extra or "check", target=extra2), json_out)
        if cmd == "index":
            return _finish_ledger(cmd_index(subcmd=extra or "verify"), json_out)
        if cmd == "summary":
            return _finish_ledger(cmd_summary(subcmd=extra), json_out)
        if cmd == "changelog":
            return _finish_ledger(cmd_changelog(raw=args[1:]), json_out)
        if cmd == "bump":
            return _finish_ledger(cmd_bump(raw=args[1:]), json_out)
        if cmd == "git":
            return _finish_ledger(cmd_git(subcmd=extra or "status", message=" ".join(args[2:])), json_out)
        if cmd == "rename":
            return _finish_ledger(cmd_rename(old=extra, new=extra2), json_out)
        if cmd == "gitkeep":
            return _finish_ledger(cmd_gitkeep(subcmd=extra), json_out)
        if cmd == "trash":
            return _finish_ledger(cmd_trash(arg1=extra, arg2=extra2), json_out)
        if cmd == "logs":
            return _finish_ledger(cmd_logs(subcmd=extra, target=extra2), json_out)
        if cmd == "lint":
            return _finish_ledger(cmd_lint(target=extra), json_out)
        if cmd == "secrets":
            quiet = "--quiet" in args[1:]
            return _finish_ledger(cmd_secrets(quiet=quiet), json_out)
        if cmd in ("install-hooks", "hooks"):
            return _finish_ledger(cmd_install_hooks(), json_out)
        if cmd in ("commitcheck", "commit-check"):
            return _finish_ledger(cmd_commit_check(msgfile=extra), json_out)
        if cmd == "selftest":
            return _finish_ledger(cmd_selftest(), json_out)
        if cmd == "manifest":
            return _finish_ledger(cmd_manifest(full=extra.lower() in ("full", "--full", "all", "--all")), json_out)
        if cmd == "db":
            return _finish_ledger(cmd_db(args[1:]), json_out)
        if cmd == "kb":
            return _finish_ledger(cmd_kb(args[1:]), json_out)
        if cmd == "folder":
            return _finish_ledger(cmd_folder(preset=extra, name=extra2, json_out=json_out), json_out)
        if cmd == "sync":
            if extra.lower() == "verify":
                return _finish_ledger(cmd_sync(verify=True), json_out)
            if extra.lower() == "tag":
                return _finish_ledger(cmd_sync(tag_target=extra2, tag_values=list(args[3:])), json_out)
            return _finish_ledger(cmd_sync(force=extra.lower() in ("all", "--all", "full", "--full")), json_out)
        if cmd in NAME_MAP:
            _, _, _, fn = NAME_MAP[cmd]
            return _finish_ledger(fn(), json_out)
        print(f"\n  ❌  Unknown command: '{cmd}'")
        print(f"  Valid: {', '.join(NAME_MAP.keys())}")
        print(f"  Run without arguments for the interactive menu.\n")
        return _finish_ledger(1, json_out)
    except KeyboardInterrupt:
        print("\n\n  👋  Interrupted.\n")
        return 130  # the conventional 128+SIGINT code, so callers see the abort


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # the umbrella: nothing crashes without a log entry
        logging.getLogger("uncaught").error("Uncaught exception", exc_info=True)
        print(f"\n  ❌  Unexpected error: {exc}")
        print(f"       Full traceback logged to System/Data/errors.log - `health` will surface it.\n")
        sys.exit(1)
