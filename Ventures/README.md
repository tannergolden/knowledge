<!--
title: "Ventures - Folder Information"
description: "Explains the purpose of the Ventures/ folder: one subfolder per venture, each holding that company's full context and department folders."
type: "index"
keywords: ["companies", "businesses", "company subfolders", "department folders", "business context", "folder overview", "venture structure"]
-->

# 🏢 Ventures/

Each company the owner runs, one folder each, copied from `.template/`: an `Overview.md`, `Goals.md` and `Log.md`, the `Administration/` executive office, and a folder for each department, from Sales & Marketing to Legal & Compliance. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

## Rules

- Venture work starts by looking in `Ventures/` for the company's folder: whether one exists is checked, never assumed.
- A venture folder is created only with a yes, by copying `Ventures/.template/` whole and giving the copy a short hyphenated name (`Acme-Corp`). A business with clients, employees, revenue or a brand is a venture; one without them is a project.
- Every copied file gets its real `title`, `description` and `type`, its keywords lose `template`, and `[Company]` becomes the venture's name: each copied `README.md` becomes its folder's note, typed `index`, so no placeholder reaches the catalog.
- A venture's files hold only what the owner says, confirmed before it is written. Nothing is guessed or invented.
- Ventures stay apart: two ventures' context is never merged or cross-referenced unless the owner asks.
- Personal information goes to `Profile/` or `Memory/`, and general business knowledge to `Library/`, never here.
- The strategic core is written only behind the write-gate (Structure, below).
- Each venture's `Overview.md` keeps its stage and status current, and its `Log.md` records meaningful work.

## What Belongs Here

`Ventures/` holds the context and working files of every company the owner owns or operates: company-specific context and materials only. Each venture's folder holds its company-wide `.md` context files at the root, the `Administration/` executive office, a folder for each of the other 11 departments, and a `Miscellaneous/` catch-all. A department folder holds both `.md` context files and other working files (assets, decks, exports, documents): it is a working folder, not just notes.

| Content Type | Belongs In |
|-------------|-----------|
| A venture's profile, goals and running log | `Ventures/[Company]/Overview.md`, `Goals.md` and `Log.md` |
| A venture's team, pipeline, products, brand or other department records | `Ventures/[Company]/[Department]/` |
| Sales decks, contracts, data exports for a venture | `Ventures/[Company]/[Department]/` |
| A decision for a venture | `Ventures/[Company]/Administration/Decisions.md` |
| How org structures generally work | `Library/` |
| The owner's personal career history | `Profile/Biography.md` |
| A decision in the owner's own life | `Memory/Decisions/` (an entry from `Memory/.template/Decision.md`) |
| A personal project not tied to a venture | `Projects/` |

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

The same skills' work in the owner's own life never lands here: the root `README.md`, Where Each Kind Of Work Goes, gives its homes.

## Structure

Each venture follows the template in `Ventures/.template/`:

<details>
<summary>The venture template, folder by folder</summary>

```bash
Ventures/
└── Company-Name/
    │
    ├── README.md                                The venture's folder note, copied from the template's
    ├── Overview.md                              Company profile, mission, vision, industry, stage, status
    ├── Goals.md                                 OKRs, strategic goals, north star metric, milestones
    ├── Log.md                                   Session log: decisions, milestones, progress over time
    │
    ├── Administration/                          Executive office: strategy, decisions, operating cadence
    │   ├── Strategy.md                          Company thesis, market and competition, strategic bets
    │   ├── Decisions.md                         Governance and decision record, with its decision memos
    │   └── Cadence.md                           Weekly / monthly / quarterly / annual operating rhythm
    │
    ├── Sales & Marketing (S&M)/
    │   ├── Pipeline.md                          Open prospects: stage, value, owner, next step, close
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

The template carries a **strategic core**: the `Administration/` executive office (`Strategy.md`, the thesis the OKRs ladder up to; `Decisions.md`, the governance record; `Cadence.md`, the operating rhythm) and, in Finance & Accounting, a forward `Financial-Model.md` and a real `Cap-Table.md`. These files are written only behind the **write-gate**: the `administration` skill writes them, or `finance-and-accounting` the model and the cap table. Internal drafts go ahead directly; moving money, contracts, outside communication, a change to equity and deletions need the owner's yes.

## Creating A Venture Folder

A venture folder is made when the owner mentions a company they own, operate, or are starting, and only once they say yes to the question:

> _"Create a venture folder for [Company]?"_

It is made by copying `.template/` whole and naming the copy in short hyphenated form (Rules, above). `update-vault.py` lists it under Ventures, below, and the catalog (`System/Data/catalog.ndjson`) picks up its notes: there is no hand-maintained index to update.

**Signs a venture folder is needed:**

- The owner mentions a company they own, operate, co-found, or actively run
- The work is clearly a business, not just a personal project
- The owner refers, across sessions, to a company that has no folder yet
- The owner asks to set up a company in the BRAIN
- The nature of the work (clients, revenue, employees, brand) makes it clear a venture context is needed

**Venture or project:** if it involves clients, employees, revenue, or a brand operating independently in the market, it is a venture. If it is something the owner is personally building or exploring without that organizational dimension, it is a project.

## Working Within A Venture

The folder is looked for every time a venture comes up, not just on first mention, in the actual directory rather than from memory: folders may have been renamed or restructured.

- **The folder exists:** work happens inside it. Its `Overview.md` is read first, then `Goals.md` and `Log.md` for current priorities and recent context, then the department files the task needs, each department's `README.md` saying what its folder holds.
- **No folder exists:** the owner is asked:
  > _"There is no venture folder for [Company] yet. Create one?"_
  With a yes, it is created from `Ventures/.template/`. With a no, the work goes on without a folder.

A venture's files are **living documents, not one-time forms**: they build up as the owner works on the venture and talks it through. When a venture folder is first created, the most essential baseline comes first:

> _"What does [Company] do, and what stage is it at?"_

Only what the owner provides is filled in. Everything else stays blank: nothing is fabricated or guessed. As later work touches the venture, information that belongs in a context file is noticed, proposed before it is written, and written after a yes:

> _"[Company]'s target customer is X: add that to `Ventures/[Company]/Overview.md`?"_

- **`Overview.md`** builds from the company's mission, what it does, its stage and status, target customers, business model, revenue, key hires, strategic priorities, competitive landscape, and founding story.
- **`Sales & Marketing (S&M)/Brand.md`** builds from marketing, copywriting, messaging, visual identity, tone of voice, target audience, what the brand stands for, and any work that writes on behalf of the company.
- **`Goals.md`** builds from strategic priorities, OKRs, targets, milestones, north star metrics, and any discussion of what the company is trying to accomplish this quarter or year.
- **`Log.md`** gains an entry at the end of any session where meaningful work was done on the venture: decisions made, milestones hit, pivots, hires, launches. Entries stay concise: a date and 2 to 5 bullet points. Routine questions and answers are not logged.
- **The other department files** (`Sales & Marketing (S&M)/Pipeline.md`, `Products.md` and `Services.md`, `Customer Experience (CX)/Clients.md`, `Human Resources (HR)/Hierarchy.md`, `Finance & Accounting (F&A)/Financials.md`, `Information Technology (IT)/Stack.md`, `Business Intelligence (BI)/Metrics.md`, `Research & Development (R&D)/Roadmap.md`, `Operations & Logistics (O&L)/Operations.md`, `Legal & Compliance (L&C)/Compliance.md`, `Public Relations (PR)/Press.md` and `Quality Assurance (QA)/Standards.md`) follow the same pattern: they are updated when relevant information surfaces, always with the owner's confirmation.

## Venture Stage & Status

Each venture's `Overview.md` says its stage and its status, and stays current:

- A venture's stage changes (for example Pre-revenue to Early Revenue): its **Current Stage** is updated.
- A venture goes on hold, closes, or is sold: its **Status**, and once it is closed its **Outcome**, are updated.

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

The **Status** is `Active`, `On Hold` or `Closed`. For a closed or exited venture, the **Outcome** is one of:
`Acquired` · `IPO` · `Wind-down` · `Merged` · `Sold`

A venture is referred to by its folder name exactly as it appears under `Ventures/` (for example `Acme-Corp`).

## Ventures

Each venture folder's README, listed by `update-vault.py` from the folders here; the catalog's `BRAIN/Ventures/` records list every note inside them.

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No subfolders yet._
<!-- /brain:children -->

## File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                               | Purpose                                                                                                                                                                   |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`.template/`](.template/README.md) | The blueprint every venture folder is copied from, whole: this README becomes the venture folder's own, with [Company] replaced and its real title, description and type. |
| [`README.md`](README.md)            | This file.                                                                                                                                                                |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.
