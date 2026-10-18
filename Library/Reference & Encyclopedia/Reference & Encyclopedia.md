---
title: "Reference & Encyclopedia - Folder Information"
description: "Offline reference works (Wikipedia and other Kiwix knowledge bases) stored as read-only ZIM files and searched through brain.command kb."
status: "active"
tags: ["library", "information", "timeless"]
aliases: ["Stacks", "Knowledge Bases", "ZIM Stacks"]
keywords: ["wikipedia", "zim", "kiwix", "offline", "knowledge base", "reference", "libzim", "full-text search"]
created: 2026-06-28
updated: 2026-06-28
type: "information"
folder: "library"
layer: 2
policy: false
author: "Tanner Golden"
path: "BRAIN/Library/Reference & Encyclopedia/Reference & Encyclopedia.md"
id: "li-reference-encyclopedia"
---

# 📚 Library / Reference & Encyclopedia /

## Purpose
Offline reference works - Wikipedia and other Kiwix knowledge bases - stored as read-only ZIM files and searched by the AI through `brain.command kb`. This is the library's store of whole reference works, kept beside the curated subject folders rather than filed among them. SQLite/FTS5 still searches your own notes; this folder gives the AI the world's established knowledge, locally and offline.

## What lives here
- `*.zim` - whole reference corpora (Wikipedia, Wiktionary, ...) in Kiwix's compressed single-file format, each carrying its own built-in full-text index. Read-only, large (tens of GB), machine-managed.
- [[sources.json]] - the committed manifest of the nine knowledge bases below, read by `kb refresh`.
- This namesake.

## How it is managed
Everything runs through one command group (`brain.command kb`):

| Command | Does |
|---------|------|
| `kb search "terms"` | full-text search across every ZIM here (needs `libzim`) |
| `kb read "article"` | print one article's full text by title or path, with a citation line (`--chars N` to read more) |
| `kb list` | show installed bases and the known sources |
| `kb refresh [name]` | download or update enabled bases from Kiwix |
| `kb setup` | first run: install libzim, then fetch the enabled bases |
| `kb add` / `kb remove <name>` | enable or disable a source in the manifest |

To add full English Wikipedia (~49 GB): `kb add wikipedia` then `kb refresh wikipedia`.

## Knowledge bases
The 23 sources are defined in [[sources.json]] and download from Kiwix as dated ZIM files (e.g. `wikipedia_en_all_nopic_2026-06.zim`). The dated names change each refresh, so the files are referenced through the manifest rather than wikilinked one by one (a dated link would break on the next refresh). All are off by default except the small pipeline-test source; enable any with `kb add <name>`, then `kb refresh` (add `--verify` to checksum large downloads).

| Source | Knowledge units | Size | Default |
|--------|-----------------|------|---------|
| wikipedia-simple | ~250,000 articles | ~940 MB | on (pipeline-test source) |
| wikipedia | ~7,000,000 articles | ~49 GB | off |
| wiktionary | ~7,000,000+ entries | ~8.5 GB | off |
| wikivoyage | ~35,000 guides | ~220 MB | off |
| wikiquote | ~52,000 pages | ~310 MB | off |
| wikibooks | ~90,000 pages | ~3.3 GB | off |
| wikisource | ~1,000,000 texts | ~11 GB | off |
| wikiversity | ~30,000 lessons | ~1.5 GB | off |
| stackoverflow | ~24,000,000 questions | ~75 GB | off (English, frozen 2023-11) |
| gutenberg | ~75,000 books | ~206 GB | off (includes media) |
| medicine | ~35,000 medical articles | ~10 GB | off (mdwiki / WikiProject Medicine) |
| ifixit | ~90,000 repair guides | ~3.3 GB | off |

**LibreTexts open college textbooks** (the academic-depth tier; each enables separately as `libretexts-<subject>`):

| Subject | Size | Subject | Size |
|---------|------|---------|------|
| libretexts-math | ~790 MB | libretexts-geo | ~1.1 GB |
| libretexts-chem | ~2 GB | libretexts-med | ~1.1 GB |
| libretexts-phys | ~530 MB | libretexts-socialsci | ~1.9 GB |
| libretexts-bio | ~2.1 GB | libretexts-human | ~3.5 GB |
| libretexts-stats | ~210 MB | libretexts-biz | ~800 MB |
| libretexts-eng | ~650 MB | | |

## Scale and coverage
All 23 together give the Library roughly **40 million primary entries** (about 75 million text units if every Stack Overflow answer is counted). The mass sits in three giants: Stack Overflow (technical Q&A), Wiktionary (every word), and Wikipedia (everything else); the rest add depth and breadth rather than raw count. Figures are approximate; `kb list` prints each ZIM's exact entry count once it is downloaded.

With the full set, the AI can answer offline, from a citable local source: what is / who was / explain (Wikipedia), define and etymology (Wiktionary), how do I code or why this error (Stack Overflow), the actual text of a book, law, or speech (Gutenberg and Wikisource), college-textbook depth in math, science, and engineering (LibreTexts), clinical and medical reference (medicine), how to repair a device (iFixit), plus courses, travel, and quotations. Most factual lookups, definitions, explanations, coding help, academic study, and literary or historical reference become answerable without the internet, which makes the brain a strong offline generalist with deep ends in programming, medicine, academia, and literature.

Honest gaps, so robustness is not oversold: these are snapshots, not current events (Stack Overflow is frozen at 2023-11); college-textbook depth is covered (LibreTexts) but primary research is not (no journal papers, arXiv, or PubMed, which Kiwix does not publish); English-centric and text-only (the nopic builds drop images); and breadth over niche or proprietary depth. Robust for established reference, technical, academic, and literary knowledge; not a replacement for the live web on current or specialized-research questions.

## Downloaded files
Auto-maintained by `brain.command kb` (refresh, setup, or relink): it wikilinks the ZIM files actually present in this folder on this machine, so the namesake connects to the real downloads. The dated names change each refresh and the block rewrites itself to match. ZIM links are exempt from the broken-link check (the files are gitignored and machine-local), so this stays clean on a fresh clone before anything is downloaded.

<!-- kb:files (auto-maintained by brain.command kb - do not edit by hand) -->
- [[wikipedia-simple_2026-05.zim]] (937.3 MB)
<!-- /kb:files -->

## Boundaries
- The `.zim` files are re-downloadable data, never source. They are git-ignored (fetched from Kiwix, not committed); only the manifest and this doc travel with the repo. iCloud mirrors the files across your own devices; a fresh git clone rehydrates them with `kb refresh`.
- They are read-only binaries: not linted, not part of the wikilink graph, exempt from frontmatter. Their only obligation is Finder tags via `sync`.
- `libzim` is the one optional dependency, and only `kb` uses it. Vault search (SQLite/FTS5) is unaffected if it is absent.
- Because a live SQLite database on a synced filesystem can corrupt, this folder stores read-only ZIMs rather than a writable index: safe to keep here in iCloud (pin each file "Keep Downloaded" to block eviction).

<!-- brain:children (auto-maintained by brain.command - do not edit by hand) -->
_No subfolders yet._
<!-- /brain:children -->

## Library cross-walk
Not a Dewey class. A special-purpose store within the Library; the reference works it holds span every class.

## See also
- `Library/Library.md` - the library's classification rules and conventions
- `System/brain.command` - the `kb` command group that manages this folder
