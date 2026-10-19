<!--
title: "Library - Folder Information"
description: "A universal, discipline-based reference library built to hold all of human knowledge: 10 plain-named classes as the shelf order, a controlled-keyword faceted catalog, boundary rulings and a routing table for hard cases, AI-cataloged intake, freshness weeding, and a vector-ready design. Classification is what keeps AI retrieval precise at scale."
type: "index"
keywords: ["universal classification", "ten classes", "routing table", "boundary rulings", "controlled facet keywords", "shelf vs catalog", "retrieval at scale", "freshness weeding"]
-->

# 📚 Library/

## Rules

- **Not personal.** `Library/` holds reference knowledge about the world, never your user's own data, identity, memory or company specifics: those live in `Profile/`, `Memory/` and `Ventures/`.
- **No opinion.** A holding is factual, of reference quality: never add personal opinions, your user's preferences or a company's context to one.
- **Freshness gates entry.** Assess a holding's useful lifespan when it is filed, and lead its keywords with the matching freshness token, which `lint-notes.py` requires on every holding:

  | Tier      | Lifespan    | Token                | What qualifies                                                                          |
  | :-------- | :---------- | :------------------- | :-------------------------------------------------------------------------------------- |
  | Timeless  | 25+ years   | `freshness/timeless` | Mathematical principles, philosophy, anatomy, historical fact, established frameworks   |
  | Enduring  | 10-25 years | `freshness/enduring` | Mature best practice, established science, slowly evolving fields, classic methodology  |
  | Current   | 5-10 years  | `freshness/current`  | Present best practice, recent research, mature but evolving technology                  |
  | Ephemeral | under 5     | (rejected)           | News, specific software versions, current trends, market commentary                     |

  Five years is the floor: ephemeral content never enters `Library/`, so offer `Projects/`, `Ventures/`, `Memory/` or a confirmed deletion instead. Only a holding carries a freshness token: a folder's own note, a record and a template carry none, and neither does a note outside `Library/`, since freshness is how the Library is weeded.
- **The scheme changes only with a yes.** Adding, renaming or removing a class or division is a structural change your user approves.

## Purpose

`Library/` is the reference library of this BRAIN: a universal collection built to hold **all of human knowledge**, organized by discipline so the AI can draw on it to answer questions and reason. It is **not personal context** (Rules, above). It holds knowledge about the world, including general practical knowledge (how budgeting works), but never the user's own data, identity, memory, or company specifics, which live in `Profile/`, `Memory/`, and `Ventures/`.

## Quick reference

To file something: (1) pick the **one** class it most belongs to; (2) pick a division; (3) catalog it (frontmatter, plus a catalog card if it is an external source); (4) shelve it, then run `lint-notes.py` on it. For a hard call, use the **Classification rules**, then the **Boundary rulings** and **Worked examples** below. Weed with freshness plus **MUSTIE**.

The ten classes: **Information & Computing · Philosophy & Mind · Religion & Spirituality · Society & Social Sciences · Science & Mathematics · Technology & Applied Science · Arts & Recreation · Language & Literature · History & Geography · Life & Practice.** Each is a subfolder with its own namesake doc; the full division map is the "The ten classes" section below, and live listings come from the catalog (`System/Data/catalog.ndjson`, its `BRAIN/Library/` records).

## How this Library works

- **Folders are the shelf order, for humans.** A file lives in exactly one folder, its single subject home, like a call number. People browse better by navigating folders than by search alone.
- **Frontmatter and search are the catalog, for the AI.** A file is reachable from many angles at once (subject, freshness, form, place, period) without ever moving. One location, many access points.
- **The AI is the cataloger and reference librarian.** Classifying and cataloging happen at filing time, done by the AI, not as a chore for the owner.

## The Librarian

The Library is kept by a single resident **Librarian** ([[★ Librarian]], Marian) who lives here at the Library's root and runs the whole collection single-handed, modeled on the one-person librarian. Unlike the Faculties (the Founder's cognitive teams) or Agent Resources (the venture workforce), the Library needs no team: cataloging, curation, and reference are one coherent stewardship role, done by one mind in one pass, with no independent-verification split to staff.

The Librarian acquires, classifies, catalogs, curates, weeds, preserves, and serves every holding, to one overriding standard: **every holding earns its place**. The collection is judged by what it excludes as much as what it serves, and findability is the purpose that curation serves. By demand the Librarian also does deep per-class subject work, a link and authority-control integrity pass (via `.github/scripts/check-vault.py`), and a Conspectus-style depth assessment per class; a genuinely contested class, weed, or tier goes to the Founder.

Boundaries: the Research team (`Inbox/Faculties/Research/`) gathers evidence and files reports to `Inbox/Reports/`, and the single handoff is the promotion of a finding into a `Library/` doc; the Librarian owns the durable collection here and commissions the Research team to fill thin classes. The Inbox sort protocol makes a coarse provisional freshness screen and routes Library-bound files; the Librarian makes the authoritative tier and class assignment at catalog time.

## Why classification matters for AI (not just humans)

A flat pile plus pure vector search degrades as the collection grows: dense similarity loses discriminative power and returns plausible-but-wrong matches ("context dilution" - in one 2026 study, scaling a corpus from 54 to 1,128 documents dropped retrieval accuracy from 75% to under 40%). The fix is not better embeddings, it is **domain scoping**: filter by class and facet first, then search within (the same study restored precision and cut the search space by 85 to 98%). So the 10-class spine and the controlled facet keywords are not decoration; they are what keep AI retrieval precise at scale. Hybrid retrieval (keyword plus semantic) over a classified, metadata-rich corpus is the target.

## The ten classes

A universal, discipline-first scheme, deliberately de-biased (one neutral class per domain, no religious or geographic center, explicitly revisable), with one addition - **Life & Practice** - for the practical knowledge the library schemes scatter or omit.

| Class | Holds |
|-------|-------|
| [[Library/Information & Computing/Information & Computing\|Information & Computing]] | Information science, knowledge organization, computing, data, internet, publishing, reference |
| [[Library/Philosophy & Mind/Philosophy & Mind\|Philosophy & Mind]] | Logic, metaphysics, epistemology, ethics, aesthetics, psychology, cognitive science |
| [[Library/Religion & Spirituality/Religion & Spirituality\|Religion & Spirituality]] | All traditions as equals, theology, mythology, contemplative and secular spirituality |
| [[Library/Society & Social Sciences/Society & Social Sciences\|Society & Social Sciences]] | Sociology, politics, law, economics, education, media, military and security |
| [[Library/Science & Mathematics/Science & Mathematics\|Science & Mathematics]] | Mathematics, statistics, physics, chemistry, biology, earth and space sciences |
| [[Library/Technology & Applied Science/Technology & Applied Science\|Technology & Applied Science]] | Engineering, medicine, applied computing, agriculture, energy, operations, infrastructure |
| [[Library/Arts & Recreation/Arts & Recreation\|Arts & Recreation]] | Visual, performing and media arts, music, design, architecture, sport, games |
| [[Library/Language & Literature/Language & Literature\|Language & Literature]] | Linguistics, the world's languages, writing, literature and criticism |
| [[Library/History & Geography/History & Geography\|History & Geography]] | History, biography, geography, area studies, travel, archaeology |
| [[Library/Life & Practice/Life & Practice\|Life & Practice]] | General practical knowledge: health, food, home, money, work, relationships, self-development |

Beyond the ten classes, [[Library/Reference & Encyclopedia/Reference & Encyclopedia|Reference & Encyclopedia]] is a special-purpose folder rather than a class: it stores offline reference works (Wikipedia and other Kiwix knowledge bases) as read-only ZIM files, searched with `.github/scripts/knowledge-base.py`. The works it holds span every class, so it is the store, not a shelf.

## Classification rules

A work goes on exactly one shelf. To choose its class:

1. **Rule of application** - the class whose subject the work treats most.
2. **Interdisciplinary home** - if it spans fields, file it where its primary discipline or broadest treatment sits.
3. **First of two** - equal treatment of two subjects goes to the first in reading order.
4. **Last resort** - if it fits nowhere cleanly, use the broadest fitting class, or `Information & Computing` for the genuinely general.

Then record every other aspect as a facet keyword or a plain-path "see also" in the class doc. One shelf, many catalog entries.

## Boundary rulings

The predictable seams, each with the rule that decides them:

- **Theory vs applied:** the *study* of a field goes to its discipline class; *building a working artifact* goes to Technology & Applied Science.
- **Study vs practice:** the academic or scientific treatment goes to its discipline; the individual's *how-to for living* goes to Life & Practice.
- **General vs personal:** general reference stays in the Library; the *user's own data* goes to Profile or Memory; a *company's* data goes to Ventures.
- **Ethics of X** goes to Philosophy & Mind / Ethics, unless it is operational professional conduct, which files with the domain.
- **History vs theory:** the *history* of X goes to History & Geography and the present *theory* of X to its discipline - except the **history and philosophy of science** (and of a specific science), which is its own metascientific field in Science & Mathematics / Philosophy & Method of Science.
- **Philosophy of X:** the philosophy of a non-science subject goes to Philosophy & Mind; the philosophy of science (or of a specific science) goes to Science & Mathematics / Philosophy & Method of Science.
- **Tie:** when two fit equally, the first class in reading order wins; record the rest as facets and see-also.

## Worked examples

| Topic | Files under | Because |
|-------|-------------|---------|
| Data science | Information & Computing / Data & Information Management (method); Science / Statistics (math); Technology / Applied Computing & Software (production) | the treatment decides |
| Programming, software | Information & Computing / Computing & Computer Science (as a field); Technology / Applied Computing & Software (building it) | study vs build |
| Statistics | Science / Statistics & Probability (theory); Information & Computing / Data & Information Management (applied data) | theory vs data |
| Media, journalism | Society / Media & Communication (social science); Information & Computing / Publishing & Broadcasting (institutions); Arts / Film & Media Arts (as art) | the angle decides |
| Management | Society / Economics or Commerce (theory); Technology / Operations & Management (technique); Life / Career & Work (the individual) | theory vs technique vs personal |
| AI ethics, bioethics | Philosophy & Mind / Ethics & Moral Philosophy | ethics-of-X is philosophy |
| Psychology | Philosophy & Mind / Psychology (science); Life / Health & Wellness (self-help); Technology / Medicine (psychiatry) | science vs self-help vs clinical |
| Mythology | Religion / Mythology & Folklore (as belief); Language / Oral & Folk Literature (as verbal art) | belief vs art |
| Environment | Science / Environmental Science (natural); Society / Social Policy & Issues (policy); Technology / Energy & Materials (tech) | the angle decides |
| Architecture | Arts / Architecture (art, history); Technology / Infrastructure & Built Environment (engineering) | art vs engineering |
| Cryptocurrency | Society / Economics (money); Technology / Applied Computing & Software (the protocol) | money vs tech |
| Military science | Society / Military & Security (discipline); History (specific wars); Technology / Engineering (weapons) | discipline vs history vs tech |
| Sign language | Language & Literature / Linguistics | a language |
| Cookbook | Life & Practice / Food & Cooking | practical how-to |
| Behavioral economics | Society / Economics, or Philosophy & Mind / Psychology | route by primary method; a tie breaks to reading order |
| Public health policy | Society / Social Policy & Issues (policy); Technology / Medicine & Health Sciences (the science) | policy vs science |
| Machine translation | Language & Literature / Translation (theory); Technology / Applied Computing & Software (the system) | theory vs build |
| Meditation technique | Religion & Spirituality / Contemplative & Secular Spirituality (the tradition); Life & Practice / Health & Wellness (everyday how-to) | tradition vs daily wellbeing |
| Product design | Arts & Recreation / Design (as design); Technology / Engineering (as product engineering) | design vs engineering |
| Accounting | Society / Commerce & Organizations (as a discipline); Life & Practice / Personal Finance (the individual's own) | discipline vs personal |
| Veterinary medicine | Technology / Agriculture & Food Science (animal health) | Medicine & Health Sciences is human-scoped |
| Cybersecurity | Technology / Applied Computing & Software (practice); Society / Military & Security (cyber-defense) | practice vs security discipline |
| Paleontology | Science & Mathematics / Biology & Life Sciences | life and evolution, drawing on Earth Sciences |
| History or philosophy of a science | Science & Mathematics / Philosophy & Method of Science | metascience travels with the science, not History |
| Semiotics | Language & Literature / Linguistics | the study of signs as language |

## Facets and controlled keywords

Five orthogonal facets. Subject is the folder; freshness and the rest live in the `keywords` field (`.docs/vault/Keywords.md`) as **slash-namespaced tokens**, so an AI or a script can filter by exact match. Freshness is required on every holding (Rules, above); use the others when they add retrieval value:

- **Freshness:** `freshness/timeless`, `freshness/enduring`, `freshness/current`

- **Form:** `form/reference`, `form/primer`, `form/howto`, `form/dataset`, `form/source`
- **Level:** `level/intro`, `level/intermediate`, `level/advanced`
- **Period:** `period/ancient`, `period/medieval`, `period/early-modern`, `period/modern`, `period/contemporary`
- **Place:** `place/<region>` (e.g. `place/east-asia`, `place/global`)
- **Shelf scope (for pre-filtering before semantic search):** `class/<class-slug>`, `div/<division-slug>` (e.g. `class/science-mathematics`, `div/physics`). Slugs derive from the folder name: lowercase, drop `&`, collapse spaces to single hyphens (so `Data & Information Management` becomes `div/data-information-management`)

The scope tokens are what make "filter by class, then search within" executable: an agent narrows to a `class/...` set first, then runs semantic search inside it.

## Naming and notation

Folders use **plain-language names**, never call numbers: plain words are what keyword and semantic search match on and what carries information scent, while a notation like `510` is a near-dead token for retrieval. A library cross-walk (Dewey / UDC / LCC) is optional and lives in each class doc as a note, never as a frontmatter field and never in the path.

## Subfolder convention

The named hierarchy stays shallow; specificity lives in facets, not depth.

- **Layer 2 (class):** the ten disciplines, `A & B` naming.
- **Layer 3 (division):** recognized sub-disciplines, 7 to 12 per class, plain `A & B` or plain compound names.
- **Layer 4 and deeper:** only when a division genuinely needs it.
- No underscores anywhere (`AGENTS.md`, Conventions).

## The catalog record

Every holding carries a catalog record, with no new brain-wide frontmatter fields:

- **A synthesized note** is already a complete record under the standard schema (`.docs/vault/Note-Schema.md`): `title`, `description`, `type: reference`, and `keywords` with its facet tokens. Its path is its shelf mark, and git keeps its dates. Template: `.template/Reference Note.md`.
- **A source document** (an external book, paper, or media) gets a companion **catalog card** note; the work's own bibliography lives in the card body. Template: `.template/Source Catalog Card.md`.

## Acquisition, weeding, and finding aids

- **Acquisition:** material lands in `Inbox/`, is appraised against the 6.2 freshness floor, classified into one class and division, cataloged, and shelved.
- **Weeding:** the 6.2 freshness model plus **MUSTIE** - weed what is **M**isleading, **U**gly or superseded, **S**uperseded, **T**rivial, **I**rrelevant, or available **E**lsewhere. Remove a weeded item only with the Founder's confirmation, as a `git rm` that history keeps (`AGENTS.md`, Ask first).
- **Finding aids:** each class doc is a finding aid (scope, divisions, "class here / not here", see-also, cross-walk); the generated catalog view (OPAC) is `System/Data/catalog.ndjson`, one record per note, drawn by `update-vault.py`; filter its `BRAIN/Library/` records.

## Engine-agnostic and vector-ready

Source of truth is the markdown plus frontmatter, human-readable and portable. Any future vector index is a derived, disposable artifact built from these files. Clean headings double as chunk boundaries; the path is each item's key, and a move is a git rename that history follows; hybrid retrieval scoped by class and facet is the target.

## Revisability

No enumerated scheme is provably complete; it is a snapshot that must be revised. New and cross-disciplinary fields are placed by the rules above and surfaced through facets and see-also links until, if warranted, the scheme itself is amended. Adding, renaming, or removing a class or division is a Layer 2 structural change requiring user approval (`AGENTS.md`, Ask first). The scheme is intentionally neutral: no privileged religion, no geographic or cultural center.

## Templates

`.template/` holds the cataloging templates (no wikilinks; `.docs/vault/Link-Topology.md`): `Reference Note.md` (the standard holding), `Source Catalog Card.md` (an external source), and `Division.md` (a division folder doc, added under literary warrant).
