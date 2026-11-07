<!--
title: "Archive"
description: "The context cold-storage tier - unbounded lifetime history by year, search-only, with optional period digests that link to (never replace) the raw episodes."
type: "index"
keywords: ["cold storage", "lifetime", "by year", "period digest", "search only", "unbounded"]
-->

# 🧊 Archive

The cold-storage tier of context memory: the complete lifetime record. It is unbounded, never read at session start, and reached only by scored search. This is where session summaries come to rest once they age past the mid tier.

## Organized by year

Summaries are filed by year in subfolders, for example `Memory/Context/Archive/2026/`, each keeping its original `YYYYMMDD-HHMMSS.md` name. They arrive here when `update-vault.py` moves them on from `Memory/Context/Recent/`, into the year their name starts with, or into `undated/` when it starts with no year. A name already taken in the year folder gets `-1`, `-2` and so on: nothing is overwritten.

## Period digests (fast long-span recall)

Scanning a whole year of files to answer "what happened in 2026" is slow. Each year folder may carry a **digest** (`<year> Digest.md`) that lists the year's episodes with a one-line gist of each and a plain-path reference to the raw file. A long-span query is then answered by one read, and only the relevant raw episodes are opened. A digest **links to, never replaces** the raw summaries and events, so no detail is ever lost: the raw files stay the source of truth, and the digest is a navigational gist. A digest is written by hand, on the consolidation pass or after a reflection (`System/Workflows.md`), never drawn by `update-vault.py`; monthly digests are optional for heavy years.

## Notes

- Unbounded: no cap; the archive grows for the life of the BRAIN.
- Search-only, but importance-aware: a high-importance episode stays a live retrieval candidate even from deep in the archive (`Memory/Context/README.md`).
- Nothing is ever deleted from the archive (the root `README.md`, Ask First).
