<!--
title: "Ventures - Folder Information"
description: "Explains the purpose of the Ventures/ folder: one subfolder per venture, each holding that company's full context and department folders."
type: "index"
keywords: ["companies", "businesses", "company subfolders", "department folders", "business context", "folder overview", "venture structure"]
-->

# 🏢 Ventures/

Each company the user owns or runs, one folder each, copied from `.template/`: an `Overview.md`, `Goals.md` and `Log.md`, the `Administration/` executive office, and a folder for each department, from Sales & Marketing to Legal & Compliance. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

## Rules

- Venture work starts by looking in `Ventures/` for the company's folder: whether one exists is checked, never assumed.
- A venture folder is created only with a yes, by copying `Ventures/.template/` whole and giving the copy a short hyphenated name (`Golden-Media`). A business with clients, employees, revenue or a brand is a venture; one without them is a project.
- Every copied file gets its real `title`, `description` and `type`, and `[Company]` the venture's name: each copied `README.md` becomes its folder's note, typed `index`, so no placeholder reaches the catalog.
- A venture's files hold only what the user says, confirmed before it is written. Nothing is guessed or invented.
- Ventures stay apart: two ventures' context is never merged or cross-referenced unless the user asks.
- Personal information goes to `Profile/` or `Memory/`, and general business knowledge to `Library/`, never here.
- Each venture's `Overview.md` keeps its stage and status current, and its `Log.md` records meaningful work.

## Purpose

`Ventures/` holds context and working files for every company or business the user owns or operates. Each venture gets its own named subfolder containing company-wide `.md` context files at the root, an `Administration/` executive office, 11 standard department folders, and a `Miscellaneous/` catch-all, for organizing assets, data, and documents.

This folder is for **company-specific** context and materials. General domain knowledge belongs in `Library/`. Personal context belongs in `Profile/` or `Memory/`.

---

## What Lands Here

A company's work lands here from the twelve department skills the home kit installs, each named for its department. The `administration` skill (founding, strategy, decisions across departments and the operating cadence) keeps each venture in `Ventures/<Venture>/`, copied from `Ventures/.template/`, records each decision in the venture's `Administration/Decisions.md`, logs its work in the venture's `Log.md`, and keeps its `Overview.md` and `Goals.md` current. Every department's records go in that venture's department folder, whose own `README.md` says what belongs there:

| Department folder | The skill whose work lands there |
|-------------------|----------------------------------|
| `Administration/` | `administration`: the founding, the strategy, the decision record and the operating cadence |
| `Legal & Compliance (L&C)/` | `legal-and-compliance`: formation, the entity, contracts, IP, licenses, compliance, privacy and insurance |
| `Sales & Marketing (S&M)/` | `sales-and-marketing`: the pipeline and deals, positioning and demand, with the brand, the products and the services |
| `Operations & Logistics (O&L)/` | `operations-and-logistics`: processes, programs and vendors, from the SOPs to the recurring tasks |
| `Human Resources (HR)/` | `human-resources`: roles, hiring, pay, onboarding and the people records, with the org structure and key people |
| `Information Technology (IT)/` | `information-technology`: the internal systems and their security, from the stack and tools to infrastructure and integrations |
| `Business Intelligence (BI)/` | `business-intelligence`: metrics, data, dashboards and reporting, and any chart or diagram |
| `Quality Assurance (QA)/` | `quality-assurance`: independent verification of consequential work, with the standards, review processes, checklists and quality metrics |
| `Customer Experience (CX)/` | `customer-experience`: onboarding, success and support, with the client roster, accounts, contacts and status |
| `Public Relations (PR)/` | `public-relations`: announcements, press and crises, with media contacts, coverage and the press kit |
| `Finance & Accounting (F&A)/` | `finance-and-accounting`: the books, the financial model, the cap table and company tax |
| `Research & Development (R&D)/` | `research-and-development`: research, ideas, and the building of products, skills and software, with the roadmap |
| `Miscellaneous/` | Anything for the venture that fits no department |

The same skills' work in the user's own life never lands here: the root `README.md`, Where Each Kind Of Work Goes, gives its homes.

A department folder holds both `.md` context files and other working files (assets, decks, exports, documents): it is a working folder, not just notes.

---

## Structure

Each venture follows the template defined in `Ventures/.template/`:

<details>
<summary>The venture template, folder by folder</summary>

```bash
Ventures/
└── Company-Name/
    │
    ├── README.md                                The venture's folder note, copied from the template's
    ├── Overview.md                              Company profile, mission, vision, industry, stage
    ├── Goals.md                                 OKRs, strategic goals, north star metric, milestones
    ├── Log.md                                   Session log: decisions, milestones, progress over time
    │
    ├── Administration/                          Executive office: strategy, decisions, operating cadence
    │   ├── Strategy.md                          Company thesis, market and competition, strategic bets
    │   ├── Decisions.md                         Governance and decision record, with its decision memos
    │   └── Cadence.md                           Weekly / monthly / quarterly / annual operating rhythm
    │
    ├── Sales & Marketing (S&M)/
    │   ├── Brand.md                             Voice, tone, visual identity, messaging guidelines
    │   ├── Products.md                          Product catalog: descriptions, pricing, status, roadmap
    │   └── Services.md                          Services catalog: scope, pricing, delivery, capacity
    │
    ├── Research & Development (R&D)/
    │   └── Roadmap.md                           Active development, upcoming work, product vision
    │
    ├── Quality Assurance (QA)/
    │   └── Standards.md                         QA standards, review processes, checklists, metrics
    │
    ├── Public Relations (PR)/
    │   └── Press.md                             Media contacts, coverage log, press kit, PR strategy
    │
    ├── Operations & Logistics (O&L)/
    │   └── Operations.md                        Core processes, SOPs, vendors, recurring tasks
    │
    ├── Miscellaneous/
    │
    ├── Legal & Compliance (L&C)/
    │   └── Compliance.md                        Legal entity, contracts, IP, licenses, insurance
    │
    ├── Information Technology (IT)/
    │   └── Stack.md                             Tech stack, tools, infrastructure, integrations
    │
    ├── Human Resources (HR)/
    │   └── Hierarchy.md                         Org structure, reporting lines, key people
    │
    ├── Finance & Accounting (F&A)/
    │   ├── Financials.md                        Revenue, expenses, burn rate, runway, unit economics
    │   ├── Financial-Model.md                   Forward projections, scenarios, runway, unit economics
    │   └── Cap-Table.md                         Ownership, share classes, option pool, funding rounds
    │
    ├── Customer Experience (CX)/
    │   └── Clients.md                           Client roster: accounts, contacts, status
    │
    └── Business Intelligence (BI)/
        └── Metrics.md                           KPIs, dashboards, data sources, reporting cadence
```

Every department folder also holds its own `README.md`, copied with it, saying what belongs there.

</details>

Subfolder names are short and hyphenated (for example `Golden-Media` or `Acme-Corp`). When a venture is created, `Ventures/.template/` is copied whole and **each copied file gets its real `title`, `description` and `type`**: the `[Company]` placeholder becomes the venture's name, and `template` the type the copy is (`index` for each `README.md`), so the catalog stays clean.

The template carries a **strategic core**: the `Administration/` executive office (`Strategy.md`, the thesis the OKRs ladder up to; `Decisions.md`, the governance record; `Cadence.md`, the operating rhythm) and, in Finance & Accounting, a forward `Financial-Model.md` and a real `Cap-Table.md`. These files are written only behind a write-gate, by the `administration` skill, or by `finance-and-accounting` for the model and the cap table: internal files are drafted directly; money, contracts, outside communication and deletions need the owner's yes.

---

## Creating A Venture Folder

A venture folder is made when the user mentions a company they own, operate, or are starting, and only once they say yes to the question:

> _"Create a venture folder for [Company]?"_

It is made by copying the `.template/` structure whole and naming the copy in short hyphenated form (for example `Golden-Media` or `Acme-Corp`). The new folder is picked up automatically by the catalog (`System/Data/catalog.ndjson`, drawn by `update-vault.py`): there is no hand-maintained index to update.

**Signs a venture folder is needed:**

- The user mentions a company they own, operate, co-found, or actively run
- The work is clearly a business, not just a personal project
- The user refers, across sessions, to a company that has no folder yet
- The user asks to set up a company in the BRAIN
- The nature of the work (clients, revenue, employees, brand) makes it clear a venture context is needed

**Venture or project:** if it involves clients, employees, revenue, or a brand operating independently in the market, it is a venture. If it is something the user is personally building or exploring without that organizational dimension, it is a project.

---

## Filling Out Context Over Time

**A venture's `Overview.md` and `Sales & Marketing (S&M)/Brand.md` are living documents, not one-time forms.** They are not filled out in a single session: they build up gradually as the user works on the venture and talks it through.

When a venture folder is first created, the most essential baseline comes first:

> _"What does [Company] do, and what stage is it at?"_

Only what the user provides is filled in. Everything else stays blank: nothing is fabricated or guessed.

As later sessions touch on the venture:

- Information the conversation reveals that belongs in a context file is noticed,
- surfaced before it is written:
  > _"[Company]'s target customer is X: add that to `Ventures/[Company]/Overview.md`?"_
- and written to the relevant fields after confirmation.

**`Overview.md` builds from conversations about:** the company's mission, what it does, its stage, target customers, business model, revenue, key hires, strategic priorities, competitive landscape, and founding story.

**`Sales & Marketing (S&M)/Brand.md` builds from conversations about:** marketing, copywriting, messaging, visual identity, tone of voice, target audience, what the brand stands for, and any session that writes on behalf of the company.

**`Goals.md` builds from conversations about:** strategic priorities, OKRs, targets, milestones, north star metrics, and any session where the user discusses what the company is trying to accomplish this quarter or year.

**`Log.md` gains an entry** at the end of any session where meaningful work was done on the venture: decisions made, milestones hit, pivots, hires, launches. Entries stay concise: a date and 2 to 5 bullet points. Routine questions and answers are not logged.

**The other department files** (`Human Resources (HR)/Hierarchy.md`, `Customer Experience (CX)/Clients.md`, `Sales & Marketing (S&M)/Products.md`, `Sales & Marketing (S&M)/Services.md`, `Finance & Accounting (F&A)/Financials.md`, `Information Technology (IT)/Stack.md`, `Business Intelligence (BI)/Metrics.md`, `Research & Development (R&D)/Roadmap.md`, `Operations & Logistics (O&L)/Operations.md`, `Legal & Compliance (L&C)/Compliance.md`, `Public Relations (PR)/Press.md`, `Quality Assurance (QA)/Standards.md`) follow the same pattern: they are updated when relevant information surfaces, always with the user's confirmation.

---

## Working Within A Venture

**An existing folder is always looked for before any venture work.** When the user mentions or starts work on a specific company, the first step is to check whether a folder for it already exists under `Ventures/`, by looking at the actual directory rather than assuming.

- **The folder exists:** work happens inside it. Its `Overview.md` is read first, then `Goals.md` and `Log.md` for current priorities and recent context, then the department files the task needs, each department's `README.md` saying what its folder holds.
- **No folder exists:** the user is asked:
  > _"There is no venture folder for [Company] yet. Create one?"_
  With a yes, it is created from `Ventures/.template/` and cataloged automatically. With a no, the conversation goes on without a folder.

The check runs every time a venture comes up, not just on first mention: the user may have renamed or restructured folders.

- Department folders hold both `.md` context files and other working files (assets, decks, exports, documents): they are working folders, not just notes
- Two ventures' context is never merged or cross-referenced unless the user explicitly asks
- Personal (non-work) information is never stored here: it belongs in `Profile/` or `Memory/`
- General business knowledge is never stored here: it belongs in `Library/`
- Each venture's `Overview.md` is kept current: its stage and status change as the venture evolves

---

## What Belongs Here vs. Elsewhere

| Content Type | Belongs In |
|-------------|-----------|
| A venture's team, products, or brand context | `Ventures/[Company]/*.md` |
| Sales decks, contracts, data exports for a venture | `Ventures/[Company]/[Department]/` |
| How org structures generally work | `Library/` |
| The user's personal career history | `Profile/Biography.md` |
| A business decision the user made | `Memory/Decisions/` (an entry from `Memory/.template/Decision.md`) |
| A personal project not tied to a venture | `Projects/` |

---

## Ventures

Each venture folder's README, listed by `update-vault.py` from the folders here:

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No subfolders yet._
<!-- /brain:children -->

## Venture Stage & Status

There is no hand-maintained index. Each venture is a folder whose `Overview.md` says its stage and status; the live list comes from the catalog: the `BRAIN/Ventures/` records of the committed `System/Data/catalog.ndjson`.

**Each venture's `Overview.md` stays current:**

- A new venture folder is created: it is cataloged automatically
- A venture's stage changes (for example Pre-revenue to Early Revenue): the Stage in its `Overview.md` is updated
- A venture goes on hold, closes, or is sold: its Status (and Outcome) in its `Overview.md` is updated

**Stage values** (used consistently):

| Stage           | Meaning                                                               |
| --------------- | --------------------------------------------------------------------- |
| `Idea`          | Concept only: nothing built or validated yet                          |
| `Validation`    | Testing demand before building: customer discovery, MVPs, waitlists   |
| `Pre-revenue`   | Product or service exists, no paying customers yet                    |
| `Early Revenue` | First customers, actively searching for product-market fit            |
| `Growth`        | Product-market fit found, scaling sales, marketing, and team          |
| `Scaling`       | Aggressive expansion: new markets, significant hiring                 |
| `Established`   | Stable, predictable revenue and defined market position               |
| `Mature`        | Dominant or well-settled in market, focus on efficiency and retention |
| `Plateau`       | Growth has stalled: may signal a need to pivot or reinvent            |
| `Decline`       | Revenue or market share actively shrinking                            |

For a closed or exited venture, the Outcome is one of:
`Acquired` · `IPO` · `Wind-down` · `Merged` · `Sold`

A venture is referred to by its folder name exactly as it appears under `Ventures/` (for example `Golden-Media`).

## File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                               | Purpose                                                                                                                                                                   |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`.template/`](.template/README.md) | The blueprint every venture folder is copied from, whole: this README becomes the venture folder's own, with [Company] replaced and its real title, description and type. |
| [`README.md`](README.md)            | This file.                                                                                                                                                                |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.
