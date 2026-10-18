---
title: "Archive"
description: "The context cold-storage tier - unbounded lifetime history by year, search-only, with optional period digests that link to (never replace) the raw episodes."
status: "active"
tags: ["memory", "information", "timeless"]
aliases: []
keywords: ["archive", "cold storage", "lifetime", "by year", "period digest", "search only", "unbounded"]
created: 2026-06-18
updated: 2026-06-18
type: "information"
folder: "memory"
layer: 3
policy: false
author: "Tanner Golden"
path: "BRAIN/Memory/Context/Archive/Archive.md"
id: "me-archive"
---

# 🧊 Archive

The cold-storage tier of context memory: the complete lifetime record. It is unbounded, never auto-loaded, and reached only by scored search. This is where session summaries come to rest once they age past the mid tier.

## Organized by year

Summaries are filed by year in subfolders, for example `Memory/Context/Archive/2026/`, each keeping its original `YYYYMMDD-HHMMSS.md` name. They arrive here when they overflow from `Memory/Context/Recent/` via `brain.command memory cascade`.

## Period digests (fast long-span recall)

Scanning a whole year of files to answer "what happened in 2026" is slow. Each year folder may carry a **digest** (`<year> Digest.md`) that lists the year's episodes with a one-line gist of each and a plain-path link to the raw file. A long-span query is then answered by one read, and only the relevant raw episodes are opened. A digest **links to, never replaces** the raw summaries and events, so no detail is ever lost (raw stays the source of truth; the digest is a navigational gist). Digests are generated during cascade or reflection; monthly digests are optional for heavy years.

## Notes

- Unbounded - no cap; the archive grows for the life of the BRAIN.
- Search-only, but importance-aware: a high-importance episode stays a live retrieval candidate even from deep in the archive (see `Memory/Context/Context.md`).
- Nothing is ever deleted from the archive (Constitution 3.1).
