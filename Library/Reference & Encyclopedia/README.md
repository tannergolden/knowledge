<!--
title: '📚 REFERENCE & ENCYCLOPEDIA'
description: 'Offline reference works (Wikipedia and other Kiwix knowledge bases) stored as read-only ZIM files and searched through .github/scripts/knowledge-base.py. Read it before enabling, refreshing or searching a knowledge base, or to judge what the set covers offline and what it does not.'
type: 'index'
keywords: ["knowledge bases", "wikipedia", "kiwix", "zim files", "offline search", "wiktionary", "libretexts", "stacks"]
-->

<div align="center">

# 📚 REFERENCE & ENCYCLOPEDIA

<a name="top"></a>

**The Library's offline store of whole reference works, beside the ten classes.**

_Fetched by the script, read offline, never committed._

</div>

---

## 💡 Purpose

Offline reference works, Wikipedia and other Kiwix knowledge bases, stored as read-only ZIM files and searched through `.github/scripts/knowledge-base.py`. This is the Library's store of whole reference works, kept beside the ten classes rather than filed in one, since each work spans them all. The vault's own notes are searched as notes; this folder holds the world's established knowledge, locally and offline.

They are databases for a local AI model. Once the owner has cloned the vault to a machine, they give the AI that runs there more knowledge to draw on, with no browser to connect and no paid tool to scrape the web: a question about the world is answered from the works on the disk.

---

## 📦 What lives here

- `*.zim`: whole reference works (Wikipedia, Wiktionary, ...) in Kiwix's compressed single-file format, each carrying its own built-in full-text index. Read-only, large (from about 200 MB to over 200 GB each), and managed by the script, never by hand.
- [[sources.json]]: the committed list of the knowledge bases below, which `knowledge-base.py` reads and its `enable` and `disable` edit.
- This README.

---

## 🛠️ How it is managed

Everything runs through one script, `python3 .github/scripts/knowledge-base.py`:

| Command | Does |
|---------|------|
| `search "terms"` | search every installed work, title matches first, then full text (needs `libzim`) |
| `read "article"` | print an article's text by title or path, up to 6,000 characters (`--chars N` for another length), with a line to cite it by |
| `list` | show the installed works and every known source, on or off; it runs when no command is given |
| `enable` / `disable <name>` | turn a source on or off in `sources.json` |
| `refresh [name]` | download the newest build of each source that is on, or of the one named, checked against the checksum Kiwix publishes (`--no-verify` to skip the check, `--yes` to remove older builds without asking) |
| `check [name]` | say whether each source that is on, or the one named, still names a build Kiwix lists, reading each listing and downloading nothing (`--all` for every source); 📚 Offline Sources runs it every Monday and keeps an issue open for a prefix that names no build |

`libzim`, the vault's one optional dependency (the root `README.md`, Commands), is installed once by hand: `python3 -m pip install --user libzim` (or into a venv). Only `knowledge-base.py` uses it, and without it `list` still works. Full English Wikipedia (~49 GB) is added with `enable wikipedia`, then `refresh wikipedia`.

---

## 🗃️ Knowledge bases

The 23 sources are defined in [[sources.json]]. `refresh` fetches each from Kiwix's newest dated build (such as `wikipedia_en_all_nopic_2026-06.zim`) and installs it here as `<name>_<YYYY-MM>.zim` (`wikipedia_2026-06.zim`). The dated names change with each refresh, so the files are named through the manifest rather than wikilinked one by one (a dated link would break on the next refresh). Every source ships turned off, so a fresh vault downloads nothing; a source is turned on with `enable <name>` and fetched with `refresh`.

| Source | Knowledge units | Size | Default |
|--------|-----------------|------|---------|
| wikipedia-simple | ~250,000 articles | ~1 GB | off (the small one to try first) |
| wikipedia | ~7,000,000 articles | ~49 GB | off |
| wiktionary | ~7,000,000+ entries | ~14 GB | off |
| wikivoyage | ~35,000 guides | ~260 MB | off |
| wikiquote | ~52,000 pages | ~380 MB | off |
| wikibooks | ~90,000 pages | ~3.3 GB | off |
| wikisource | ~1,000,000 texts | ~3.6 GB | off |
| wikiversity | ~30,000 lessons | ~1.5 GB | off |
| stackoverflow | ~24,000,000 questions | ~107 GB | off (English, the 2026-07 build) |
| gutenberg | ~75,000 books | ~206 GB | off (includes media) |
| medicine | ~35,000 medical articles | ~10 GB | off (mdwiki / WikiProject Medicine) |
| ifixit | ~90,000 repair guides | ~3.3 GB | off |

**LibreTexts open college textbooks** (the academic-depth tier; each enables separately as `libretexts-<subject>`):

| Subject | Size | Subject | Size |
|---------|------|---------|------|
| libretexts-math | ~790 MB | libretexts-geo | ~1.1 GB |
| libretexts-chem | ~2 GB | libretexts-med | ~1.1 GB |
| libretexts-phys | ~530 MB | libretexts-socialsci | ~1.9 GB |
| libretexts-bio | ~2.1 GB | libretexts-human | ~4.1 GB |
| libretexts-stats | ~210 MB | libretexts-biz | ~800 MB |
| libretexts-eng | ~650 MB | | |

The sizes are those of the newest builds Kiwix listed in November 2026. A later build is usually larger, and `refresh` always fetches the newest, so check Kiwix's listing for the size before a large download.

---

## 📊 Scale and coverage

All 23 together give the Library roughly **40 million primary entries** (about 75 million text units if every Stack Overflow answer is counted). The mass sits in three giants: Stack Overflow (technical Q&A), Wiktionary (every word), and Wikipedia (everything else); the rest add depth and breadth rather than raw count. Figures are approximate; `list` prints each ZIM's exact entry count once it is downloaded and `libzim` is installed.

With the full set, these can be answered offline, from a citable local source: what is / who was / explain (Wikipedia), define and etymology (Wiktionary), how do I code or why this error (Stack Overflow), the actual text of a book, law, or speech (Gutenberg and Wikisource), college-textbook depth in math, science, and engineering (LibreTexts), clinical and medical reference (medicine), how to repair a device (iFixit), plus courses, travel, and quotations. Most factual lookups, definitions, explanations, coding help, academic study, and literary or historical reference become answerable without the internet, which makes the vault a strong offline generalist with deep ends in programming, medicine, academia, and literature.

Honest gaps, so the coverage is not oversold: these are snapshots, not current events (each is as old as its build: Stack Overflow's newest is from 2026-07, Gutenberg's from 2025-11); college-textbook depth is covered (LibreTexts) but primary research is not (no journal papers, arXiv, or PubMed, which Kiwix does not publish); English-centric and text-only (the nopic builds drop images); and breadth over niche or proprietary depth. Strong for established reference, technical, academic, and literary knowledge; not a replacement for the live web on current or specialized-research questions.

---

## 🚧 Boundaries

- The `.zim` files are re-downloadable data, never source. They are git-ignored (fetched from Kiwix, not committed); only the manifest and this README travel with the repository. A vault kept in a synced folder, such as iCloud Drive, carries them to the owner's other machines; a fresh clone fetches them with `refresh`. `list` shows which are on this machine; no committed note records it, since that differs per machine.
- They are read-only binaries: not linted, not part of the wikilink graph, exempt from frontmatter, and never holdings, so they carry no freshness token. A note about one of these works, such as its catalog card, is a holding filed in a class, such as Information & Computing / General Reference.
- Because a live SQLite database on a synced filesystem can corrupt, this folder stores read-only ZIMs rather than a writable index, which keeps it safe in a synced folder (in iCloud Drive, each file is set to Keep Downloaded so it is never evicted).

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No subfolders yet._
<!-- /brain:children -->

---

## 🔗 See also

- `Library/README.md` - the Library's classification rules and conventions
- `Library/Information & Computing/General Reference/README.md` - notes and catalog cards about general reference works
- `.github/scripts/knowledge-base.py` - the script that manages this folder

---

## 🧭 Library cross-walk

Not a Dewey class. A special-purpose store within the Library; the reference works it holds span every class.

---

<div align="center">

**The world's established knowledge, kept local and read-only.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
