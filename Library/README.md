<!--
title: '📚 LIBRARY'
description: 'A universal, discipline-based reference library built to hold all of human knowledge: 10 plain-named classes as the shelf order, a controlled-keyword faceted catalog, boundary rulings and a routing table for hard cases, cataloging at intake, freshness weeding, and a vector-ready design. Classification is what keeps retrieval precise at scale, so read it before filing, cataloging, weeding or changing anything here.'
type: 'index'
keywords: ["universal classification", "ten classes", "routing table", "boundary rulings", "controlled facet keywords", "shelf vs catalog", "retrieval at scale", "freshness weeding"]
-->

<div align="center">

# 📚 LIBRARY

<a name="top"></a>

**The vault's reference library: all of human knowledge, in ten classes.**

_Each work on one shelf, found from every angle._

</div>

---

## 💡 Purpose

Reference knowledge about the world, in ten classes, never personal. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

`Library/` is the reference library of this BRAIN: a universal collection built to hold **all of human knowledge**, organized by discipline so it can be drawn on to answer questions and reason. It holds general practical knowledge too (how budgeting works), but never anything personal (Rules, below).

---

## 📜 Rules

- **Not personal.** `Library/` holds reference knowledge about the world, never the owner's own data, identity, memory or company specifics: those live in `Profile/`, `Memory/` and `Ventures/`.
- **No opinion.** A holding is factual, of reference quality: it never holds personal opinions, the owner's preferences or a company's context.
- **Freshness gates entry.** A holding's useful lifespan is assessed when it is filed, and its keywords lead with the matching freshness token, which `lint-notes.py` requires on every holding:

  | Tier      | Lifespan    | Token                | What qualifies                                                                          |
  | :-------- | :---------- | :------------------- | :-------------------------------------------------------------------------------------- |
  | Timeless  | 25+ years   | `freshness/timeless` | Mathematical principles, philosophy, anatomy, historical fact, established frameworks   |
  | Enduring  | 10-25 years | `freshness/enduring` | Mature best practice, established science, slowly evolving fields, classic methodology  |
  | Current   | 5-10 years  | `freshness/current`  | Present best practice, recent research, mature but evolving technology                  |
  | Ephemeral | under 5     | (rejected)           | News, specific software versions, current trends, market commentary                     |

  Five years is the floor: ephemeral content never enters `Library/`; it goes to `Projects/`, `Ventures/`, `Memory/` or a confirmed deletion instead. Only a holding carries a freshness token: a folder's README.md, a record and a template carry none, and neither does a note outside `Library/`, since freshness is how the Library is weeded.
- **The scheme changes only with a yes.** Adding, renaming or removing a class or division is a structural change the owner approves (the root `README.md`, Ask First).

---

## 📥 What Lands Here

- **A source filed from `Inbox/`**: checked for freshness, classified, cataloged and shelved in one class and division, by the Inbox's sorting protocol (`Inbox/README.md`) and the rules on this page. An outside source gets a catalog card (The catalog record, below).
- **A finding promoted from a held report** (`Inbox/Reports/`) when it must outlive the report: it becomes a holding here, written from `Library/.template/Reference Note.md`.
- **What is learned about the world**, such as what the `research-and-development` skill learns for the owner, written as a holding from `Library/.template/Reference Note.md`. The owner's own progress and competence are not holdings: a learning plan goes to `Projects/`, and what the owner can do to `Profile/Skills/`.
- **An offline reference work**, such as Wikipedia, kept in `Library/Reference & Encyclopedia/` and managed with `python3 .github/scripts/knowledge-base.py`; every source ships turned off (`Library/Reference & Encyclopedia/README.md`).

---

## 🚀 Quick reference

To file something: (1) check that it stays true for five years or more, and give it its freshness tier (Rules, above); (2) pick the **one** class it most belongs to; (3) pick a division in that class; (4) catalog it: its frontmatter, plus a catalog card if it is an outside source; (5) shelve it, then run `lint-notes.py` on it, then `update-vault.py` and `check-vault.py` (the root `README.md`, Commands). A hard call is settled by the **Classification rules**, then the **Boundary rulings** and **Worked examples** below. Weeding uses the freshness tiers plus **MUSTIE**.

The ten classes, in reading order: **Information & Computing · Philosophy & Mind · Religion & Spirituality · Society & Social Sciences · Science & Mathematics · Technology & Applied Science · Arts & Recreation · Language & Literature · History & Geography · Life & Practice.** Each is a subfolder whose README.md lists its divisions and what belongs elsewhere (The ten classes, below); live listings come from the catalog (`System/Data/catalog.ndjson`, its `BRAIN/Library/` records).

---

## ⚙️ How this Library works

- **Folders are the shelf order, for people.** A file lives in exactly one folder, its single subject home, like a call number. People browse better by navigating folders than by search alone.
- **Frontmatter and search are the catalog, for retrieval.** A file is reachable from many angles at once (subject, freshness, form, level, period, place) without ever moving. One location, many access points.
- **Cataloging happens at filing time.** Whoever files a holding classifies and catalogs it in the same pass, so it is never left as a chore for later.
- **The Library answers before the web.** A question about the world is grounded here first: in the notes and the catalog's `BRAIN/Library/` records, then in an installed reference work (`python3 .github/scripts/knowledge-base.py search` to find an article, then `read` for its text), citing what was used. Anything current goes straight to the web (the root `README.md`, How A Session Goes).

---

## 🤝 Stewardship

The Library has no keeper of its own: whoever works in the vault, a person or any AI, keeps it by the rules on this page. Cataloging, curation and reference are one job, done in one pass, to one overriding standard: **every holding earns its place**. Each holding is acquired, classified, cataloged, curated, weeded, preserved and served to that standard; the collection is judged by what it leaves out as much as by what it serves, and findability is what curation is for. On request, a class gets deeper work: a subject review, a link and authority-control pass (`.github/scripts/check-vault.py`), and a Conspectus-style assessment of its depth. A genuinely contested class, weed or tier goes to the owner.

- **The `research-and-development` skill** grounds a question about the world here before the web, files its reports in `Inbox/Reports/`, and adds to the Library only holdings: a finding promoted from a report, or what it learns about the world for the owner. A class found thin is a question for it to research.
- **The Inbox sort** files a source here by this page's rules: the source's freshness is assessed, and it is classified and cataloged, before it moves (`Inbox/README.md`, Pre-Sorting Enrichment).

---

## 🎯 Why classification matters for retrieval (not just for people)

A flat pile plus pure vector search degrades as the collection grows: dense similarity loses discriminative power and returns plausible-but-wrong matches ("vector search dilution": in one 2026 study, growing a corpus from 54 to 1,128 documents cut retrieval precision by 63%, from 0.76 to 0.28; Subedi et al., arXiv:2606.11350). The fix is not better embeddings, it is **domain scoping**: filter by class and facet first, then search within (the same study's domain-scoped retrieval shrank each search space by 65 to 98%). So the ten-class spine and the controlled facet keywords are not decoration; they are what keep retrieval precise at scale. Hybrid retrieval (keyword plus semantic) over a classified, metadata-rich corpus is the target.

---

## 🗂️ The ten classes

A universal, discipline-first scheme, deliberately de-biased (one neutral class per domain, no religious or geographic center, explicitly revisable), with one addition - **Life & Practice** - for the practical knowledge the library schemes scatter or omit. The classes are listed in reading order.

| Class | Holds |
|-------|-------|
| [[Library/Information & Computing/README\|Information & Computing]] | Information science, knowledge organization, computing, data, internet, publishing, reference |
| [[Library/Philosophy & Mind/README\|Philosophy & Mind]] | Logic, metaphysics, epistemology, ethics, aesthetics, psychology, cognitive science |
| [[Library/Religion & Spirituality/README\|Religion & Spirituality]] | All traditions as equals, theology, mythology, contemplative and secular spirituality |
| [[Library/Society & Social Sciences/README\|Society & Social Sciences]] | Sociology, politics, law, economics, education, media, military and security |
| [[Library/Science & Mathematics/README\|Science & Mathematics]] | Mathematics, statistics, physics, chemistry, biology, earth and space sciences |
| [[Library/Technology & Applied Science/README\|Technology & Applied Science]] | Engineering, medicine, applied computing, agriculture, energy, operations, infrastructure |
| [[Library/Arts & Recreation/README\|Arts & Recreation]] | Visual, performing and media arts, music, design, architecture, sport, games |
| [[Library/Language & Literature/README\|Language & Literature]] | Linguistics, the world's languages, writing, literature and criticism |
| [[Library/History & Geography/README\|History & Geography]] | History, biography, geography, area studies, travel, archaeology |
| [[Library/Life & Practice/README\|Life & Practice]] | General practical knowledge: health, food, home, money, work, relationships, self-development |

Beyond the ten classes, [[Library/Reference & Encyclopedia/README|Reference & Encyclopedia]] is a special-purpose folder rather than a class: it stores offline reference works (Wikipedia and other Kiwix knowledge bases) as read-only ZIM files, searched with `.github/scripts/knowledge-base.py`. The works it holds span every class, so it is the store, not a shelf.

---

## 📐 Classification rules

A work goes on exactly one shelf. To choose its class:

1. **Predominance** - the class whose subject the work treats most.
2. **Interdisciplinary home** - if it spans fields, file it where its primary discipline or broadest treatment sits.
3. **First of two** - equal treatment of two subjects goes to the first in reading order: the order of the ten classes (The ten classes, above), and within a class the order of its Divisions table.
4. **Last resort** - if it fits nowhere cleanly, use the broadest fitting class, or `Information & Computing` for the genuinely general.

Then record every other aspect as a facet keyword, or as a plain-path pointer in the holding's own See Also. One shelf, many catalog entries.

---

## ⚖️ Boundary rulings

The predictable seams, each with the rule that decides them:

- **Theory vs applied:** the *study* of a field goes to its discipline class; *building a working artifact* goes to Technology & Applied Science.
- **Study vs practice:** the academic or scientific treatment goes to its discipline; the individual's *how-to for living* goes to Life & Practice.
- **General vs personal:** general reference stays in the Library; the *owner's own data* goes to Profile or Memory; a *company's* data goes to Ventures.
- **Ethics of X** goes to Philosophy & Mind / Ethics & Moral Philosophy, unless it is operational professional conduct, which files with the domain.
- **History vs theory:** the *history* of X goes to History & Geography and the present *theory* of X to its discipline, with three exceptions, where tracing a field's past is part of studying it: the history of an art, a sport or a game travels with it in Arts & Recreation or Language & Literature (a history of jazz to Arts & Recreation / Music, of the novel to Language & Literature / Literary Criticism); the history of philosophy goes to Philosophy & Mind / Philosophical Traditions; and the **history and philosophy of science** (and of a specific science) is its own metascientific field, in Science & Mathematics / Philosophy & Method of Science.
- **Philosophy of X:** the philosophy of a non-science subject goes to Philosophy & Mind (the philosophy of art to Aesthetics), except where the subject's own division holds its theory: the philosophy of history stays in History & Geography / Historiography, and jurisprudence, the theory of law, in Society & Social Sciences / Law & Justice. The philosophy of science (or of a specific science) goes to Science & Mathematics / Philosophy & Method of Science.
- **Tradition vs aspect:** in Religion & Spirituality, a work on one tradition files with that tradition, whatever its aspect; theology, myth, ritual or contemplative practice in general, or across traditions, files with that aspect's division.
- **Tie:** when two fit equally, the first class in reading order wins; record the rest as facets and see-also pointers.

---

## 🧩 Worked examples

| Topic | Files under | Because |
|-------|-------------|---------|
| Data science | Information & Computing / Data & Information Management (method); Science & Mathematics / Statistics & Probability (the mathematics); Technology & Applied Science / Applied Computing & Software (production) | the treatment decides |
| Programming, software | Information & Computing / Computing & Computer Science (as a field); Technology & Applied Science / Applied Computing & Software (building it) | study vs build |
| Statistics | Science & Mathematics / Statistics & Probability (theory); Information & Computing / Data & Information Management (applied data) | theory vs data |
| Media, journalism | Society & Social Sciences / Media & Communication (social science); Information & Computing / Publishing & Broadcasting (institutions); Arts & Recreation / Film & Media Arts (as art) | the angle decides |
| Management | Society & Social Sciences / Economics or Commerce & Organizations (theory); Technology & Applied Science / Operations & Management (technique); Life & Practice / Career & Work (the individual) | theory vs technique vs personal |
| AI ethics, bioethics | Philosophy & Mind / Ethics & Moral Philosophy | ethics-of-X is philosophy |
| Psychology | Philosophy & Mind / Psychology (science and therapy); Life & Practice / Health & Wellness (self-help); Technology & Applied Science / Medicine & Health Sciences (psychiatry) | science vs self-help vs medicine |
| Mythology | Religion & Spirituality / Mythology & Folklore (as belief); Language & Literature / Oral & Folk Literature (as verbal art) | belief vs art |
| Buddhist or Confucian thought | Religion & Spirituality / Dharmic Traditions or East Asian Traditions (argued within the tradition); Philosophy & Mind / Philosophical Traditions (read as philosophy) | within vs outside a tradition |
| Christian liturgy | Religion & Spirituality / Abrahamic Traditions; prayer across faiths goes to Religion & Spirituality / Ritual & Practice | tradition vs aspect |
| Environment | Science & Mathematics / Environmental Science (natural); Society & Social Sciences / Social Policy & Issues (policy); Technology & Applied Science / Energy & Materials (tech) | the angle decides |
| Architecture | Arts & Recreation / Architecture (art, history); Technology & Applied Science / Infrastructure & Built Environment (engineering) | art vs engineering |
| History of an art | The art's own division, such as Arts & Recreation / Music for a history of jazz | the history of an art travels with it |
| Cryptocurrency | Society & Social Sciences / Economics (money); Technology & Applied Science / Applied Computing & Software (the protocol) | money vs tech |
| Military science | Society & Social Sciences / Military & Security (discipline); History & Geography / World History or Regional & Area Histories (specific wars); Technology & Applied Science / Engineering (weapons) | discipline vs history vs tech |
| Sign language | Language & Literature / Linguistics (its study); Language & Literature / Languages of the World (one sign language, and learning it) | a language like any other |
| Cookbook | Life & Practice / Food & Cooking | practical how-to |
| Behavioral economics | Society & Social Sciences / Economics, or Philosophy & Mind / Psychology | route by primary method; a tie breaks to reading order |
| Public health policy | Society & Social Sciences / Social Policy & Issues (policy); Technology & Applied Science / Medicine & Health Sciences (the science) | policy vs science |
| Machine translation | Language & Literature / Translation (theory); Technology & Applied Science / Applied Computing & Software (the system) | theory vs build |
| Meditation technique | Religion & Spirituality / Contemplative & Secular Spirituality (as contemplative practice); Life & Practice / Health & Wellness (everyday how-to) | contemplative practice vs daily wellbeing |
| Product design | Arts & Recreation / Design (as design); Technology & Applied Science / Engineering (as product engineering) | design vs engineering |
| Accounting | Society & Social Sciences / Commerce & Organizations (as a discipline); Life & Practice / Personal Finance (an individual's money, as general method) | discipline vs personal |
| Veterinary medicine | Technology & Applied Science / Agriculture & Food Science (animal health) | Medicine & Health Sciences is human-scoped |
| Cybersecurity | Technology & Applied Science / Applied Computing & Software (practice); Society & Social Sciences / Military & Security (cyber defense) | practice vs security discipline |
| Paleontology | Science & Mathematics / Biology & Life Sciences | life and evolution, drawing on Earth Sciences |
| History or philosophy of a science | Science & Mathematics / Philosophy & Method of Science | metascience travels with the science, not History & Geography |
| Semiotics | Language & Literature / Linguistics | the study of signs as language |

---

## 🏷️ Facets and controlled keywords

Six orthogonal facets. Subject is the folder; the other five, freshness, form, level, period and place, live in the `keywords` field (`.docs/technical/vault/Keywords.md`) as **slash-namespaced tokens**, so a search or a script can filter by exact match. Freshness is required on every holding (Rules, above); use the others when they add retrieval value:

- **Freshness:** `freshness/timeless`, `freshness/enduring`, `freshness/current`
- **Form:** `form/reference`, `form/primer`, `form/howto`, `form/dataset`, `form/source`
- **Level:** `level/intro`, `level/intermediate`, `level/advanced`
- **Period:** `period/ancient`, `period/medieval`, `period/early-modern`, `period/modern`, `period/contemporary`
- **Place:** `place/<region>` (e.g. `place/east-asia`, `place/global`)
- **Shelf scope** (the subject again, as tokens for pre-filtering before semantic search): `class/<class-slug>`, `div/<division-slug>` (e.g. `class/science-mathematics`, `div/physics`). Slugs derive from the folder name: lowercase, drop `&`, collapse spaces to single hyphens (so `Data & Information Management` becomes `div/data-information-management`)

The scope tokens are what make "filter by class, then search within" executable: a search narrows to a `class/...` set first, then runs semantically inside it.

---

## 🔤 Naming and notation

Folders use **plain-language names**, never call numbers: plain words are what keyword and semantic search match on and what carries information scent, while a notation like `510` is a near-dead token for retrieval. A library cross-walk (Dewey / UDC / LCC) is optional and lives in each class's README.md as a note, never as a frontmatter field and never in the path.

---

## 📂 Subfolder convention

The named hierarchy stays shallow; specificity lives in facets, not depth.

- **Layer 2 (class):** the ten disciplines, `A & B` naming.
- **Layer 3 (division):** recognized sub-disciplines, 7 to 12 per class, plain `A & B` or plain compound names.
- **Layer 4 and deeper (subdivision):** only under literary warrant, when a division holds enough on one sub-subject to need a shelf of its own, and only with the owner's yes (the root `README.md`, Ask First).
- Each folder explains itself in its own `README.md`.
- No underscores anywhere (the root `README.md`, Conventions).

---

## 🗃️ The catalog record

Every holding carries a catalog record, with no new brain-wide frontmatter fields:

- **A synthesized note** is already a complete record under the standard schema (`.docs/technical/vault/Note-Schema.md`): `title`, `description`, `type: reference`, and `keywords` with its facet tokens. Its path is its shelf mark, and git keeps its dates. Template: `Library/.template/Reference Note.md`.
- **A source document** (an external book, paper, or media) gets a companion **catalog card** note, filed beside any held copy of the work; the work's own bibliography lives in the card body. Template: `Library/.template/Source Catalog Card.md`.

---

## ♻️ Acquisition, weeding, and finding aids

- **Acquisition:** material lands in `Inbox/`, is appraised against the freshness floor (Rules, above), classified into one class and division, cataloged, and shelved.
- **Weeding:** the freshness tiers plus **MUSTIE** - weed what is **M**isleading, **U**gly (too badly formed to repair), **S**uperseded, **T**rivial, **I**rrelevant, or available **E**lsewhere. A weeded item is removed only with the owner's confirmation, as a `git rm` that history keeps (the root `README.md`, Ask First).
- **Finding aids:** each class's README.md is a finding aid (scope, divisions, "class here / not here", see-also, cross-walk), and each division's README.md gives its scope and its nearest neighbors; the generated catalog view (OPAC) is `System/Data/catalog.ndjson`, one record per note, drawn by `update-vault.py`; filter its `BRAIN/Library/` records.

---

## 📦 Engine-agnostic and vector-ready

Source of truth is the markdown plus frontmatter, human-readable and portable. Any future vector index is a derived, disposable artifact built from these files. Clean headings double as chunk boundaries; the path is each item's key, and a move is a git rename that history follows; hybrid retrieval scoped by class and facet is the target.

---

## 🔄 Revisability

No enumerated scheme is provably complete; it is a snapshot that must be revised. New and cross-disciplinary fields are placed by the rules above and surfaced through facets and see-also pointers until, if warranted, the scheme itself is amended. Adding, renaming, or removing a class or division is a structural change made only with the owner's yes (Rules, above). The scheme is intentionally neutral: no privileged religion, no geographic or cultural center.

---

## 📝 Templates

`Library/.template/` holds the cataloging templates (no wikilinks; `.docs/technical/vault/Link-Topology.md`), and its own `README.md` says how each is copied: `Reference Note.md` (the standard holding), `Source Catalog Card.md` (an external source), and `Division.md` (the `README.md` of a new division, written when the division is added).

---

## 📋 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                                       | Purpose                                                                                                                                                                                                                                                                                    |
| :-------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`.template/`](.template/README.md)                                         | The cataloging scaffolds: a reference note, a source catalog card and a division README. Read it before copying one to make a new Library note; each is copied on its own and never edited in place.                                                                                       |
| [`Arts & Recreation/`](<Arts & Recreation/README.md>)                       | What people create as art and how they play: the arts by form, architecture, sport, games and recreation. Read it to file a holding in this class or to choose among its divisions.                                                                                                        |
| [`History & Geography/`](<History & Geography/README.md>)                   | The human record across time and place: history at every scale, biography, geography and maps, travel and exploration, archaeology, and genealogy and heritage. Read it to file a holding in this class or to choose among its divisions.                                                  |
| [`Information & Computing/`](<Information & Computing/README.md>)           | How knowledge and information are organized, stored, computed, and transmitted, plus the general reference works that span every subject. Read it to file a holding in this class or to choose among its divisions.                                                                        |
| [`Language & Literature/`](<Language & Literature/README.md>)               | Human language and its literature, written and oral: linguistics, the world's languages, writing and rhetoric, translation, and literature by form. Read it to file a holding on language or literature, or to choose among its divisions.                                                 |
| [`Life & Practice/`](<Life & Practice/README.md>)                           | General practical knowledge for the business of living, written for anyone: health, food, the home, money, work, relationships and personal growth. Read it to file a how-to holding, to choose among its divisions, or to keep the owner's own data out of the Library.                   |
| [`Philosophy & Mind/`](<Philosophy & Mind/README.md>)                       | The examined questions of reason, value, beauty, and mind, and the science of mind and behavior. Read it to file a holding on philosophy, psychology or cognitive science, or to choose among its divisions.                                                                               |
| [`Reference & Encyclopedia/`](<Reference & Encyclopedia/README.md>)         | Offline reference works (Wikipedia and other Kiwix knowledge bases) stored as read-only ZIM files and searched through .github/scripts/knowledge-base.py. Read it before enabling, refreshing or searching a knowledge base, or to judge what the set covers offline and what it does not. |
| [`Religion & Spirituality/`](<Religion & Spirituality/README.md>)           | Religion and spirituality studied neutrally, with every tradition treated as a peer and none privileged. Read it to file a holding in this class, or to choose between a tradition's own division and the one for a theme that spans traditions.                                           |
| [`Science & Mathematics/`](<Science & Mathematics/README.md>)               | The formal and natural sciences and how scientific knowledge is made. Read it to file a holding in this class, or to tell science apart from engineering, medicine, computing and environmental policy.                                                                                    |
| [`Society & Social Sciences/`](<Society & Social Sciences/README.md>)       | How human societies are structured, governed, and sustained. Read it to file a holding in this class, or to tell the study of society apart from history, management technique, personal finance and psychology.                                                                           |
| [`Technology & Applied Science/`](<Technology & Applied Science/README.md>) | Knowledge applied to practical ends: the making of working things and the running of operations, from engineering and medicine to software, farming and transport. Read it to file a holding in this class or to choose among its divisions.                                               |
| [`README.md`](README.md)                                                    | This file.                                                                                                                                                                                                                                                                                 |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.

---

<div align="center">

**Every holding earns its place on the shelf.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
