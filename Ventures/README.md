<!--
title: '🏢 VENTURES'
description: 'Explains the purpose of the Ventures/ folder: one subfolder per venture, each holding that company''s full context and department folders. Read it before creating a venture folder or doing any work for a company the owner runs.'
type: 'index'
keywords: ["companies", "businesses", "company subfolders", "department folders", "business context", "write-gate", "strategic core"]
-->

<div align="center">

# 🏢 VENTURES

<a name="top"></a>

**The companies the owner runs, each with its own context and department folders.**

_Each venture kept apart, and written only as the owner confirms._

</div>

---

## ⚖️ What Belongs Here

`Ventures/` holds the context and working files of every company the owner owns or operates, one folder each: company-specific context and materials only. Each venture's folder, copied from `.template/`, holds its company-wide `.md` context files at the root (`Overview.md`, `Goals.md` and `Log.md`), the `Administration/` executive office, a folder for each of the other eleven departments, from Finance & Accounting to Public Relations, and a `Miscellaneous/` catch-all. A department folder holds both `.md` context files and other working files (assets, decks, exports, documents): it is a working folder, not just notes. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

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

---

## 📥 What Lands Here

A company's work lands here, department by department. Administration (founding, strategy, decisions across departments and the operating cadence) keeps each venture in `Ventures/[Company]/`, copied from `Ventures/.template/`, records each decision in the venture's `Administration/Decisions.md`, logs its work in the venture's `Log.md`, and keeps its `Overview.md` and `Goals.md` current. Every department's records go in that venture's department folder, whose own `README.md` says what belongs there:

| Department folder | The work that lands there |
|-------------------|---------------------------|
| `Administration/` | The founding, the strategy, the decision record and the operating cadence |
| `Finance & Accounting (F&A)/` | The books and each month's close, the financial model and budget, the cap table and company tax |
| `Legal & Compliance (L&C)/` | Formation, the entity and its IP, contracts, the filings calendar, policies, privacy, open matters and insurance |
| `Sales & Marketing (S&M)/` | Positioning and the brand, the products and services, the sales plan, the pipeline and forecast, and the revenue plan with the demand that feeds it |
| `Operations & Logistics (O&L)/` | Processes and SOPs, vendors and their costs, programs, and the operations KPIs |
| `Human Resources (HR)/` | Org design, roles, hiring, pay, onboarding and the people records |
| `Information Technology (IT)/` | The systems register and the security program, with the runbooks and the incident record |
| `Research & Development (R&D)/` | Research, ideas, and the building of products, skills and software, with the roadmap |
| `Business Intelligence (BI)/` | The governed metric definitions and the north star, data, dashboards, and any chart or diagram |
| `Quality Assurance (QA)/` | Independent verification of consequential work, with the definitions of done, test plans, the verification record and the defect log |
| `Customer Experience (CX)/` | Onboarding, success and support, with each account's health and renewal and the voice of the customer |
| `Public Relations (PR)/` | Announcements, press and crises, with the messaging house, the press kit and public log, and the crisis plan |
| `Miscellaneous/` | Anything for the venture that fits no department |

The same departments' work in the owner's own life never lands here: the root `README.md`, Where Each Kind Of Work Goes, gives its homes.

---

## 👔 Who Keeps Each File

When the owner runs the AI workforce from `tannergolden/intelligence` (the root `README.md`, When The Workforce Works Here), each department folder is kept by the department of the same name, and that department's ⭐ Director answers for it. The seat named below decides what its file says and sends it as a record through the Chief of Staff; the Knowledge Vault Manager alone writes it, by the folder's README. Where these pages say a department writes a file, under the workforce that department keeps it and the Knowledge Vault Manager writes it.

| File | Kept by |
|------|---------|
| `README.md` and `Overview.md` | The ⭐ Chief Executive Officer |
| `Goals.md` | The Chief Operating Officer: the objectives, OKRs, rocks and their grades |
| `Log.md` | Every department, an entry for its meaningful work |
| `Administration/Strategy.md` and `Decisions.md` | The ⭐ Chief Executive Officer |
| `Administration/Cadence.md` | The Chief Operating Officer |
| `Finance & Accounting (F&A)/Financials.md` and `Cap-Table.md` | The ⭐ Director of Finance |
| `Finance & Accounting (F&A)/Financial-Model.md` | The Financial Analyst |
| `Legal & Compliance (L&C)/Compliance.md` | The ⭐ Director of Legal & Compliance, with the Risk & Compliance Manager's obligations register and policies, and the Paralegal's contracts and filings |
| `Sales & Marketing (S&M)/`, every file | The ⭐ Director of Sales & Marketing, with the Account Executive's deals in `Pipeline.md`, and the style guide Public Relations' Editor keeps with `Brand.md` |
| `Operations & Logistics (O&L)/Operations.md` | The ⭐ Director of Operations, with the Process & Systems Analyst's processes and SOPs and the Supply Chain & Procurement Manager's vendor register |
| `Human Resources (HR)/Hierarchy.md` | The ⭐ Director of Human Resources, with the HR Generalist's roster |
| `Information Technology (IT)/Stack.md` | The ⭐ Director of Information Technology, with the Security Engineer's incident record |
| `Research & Development (R&D)/Roadmap.md` | The ⭐ Director of Research & Development |
| `Business Intelligence (BI)/Metrics.md` | The ⭐ Director of Business Intelligence |
| `Quality Assurance (QA)/Standards.md` | The ⭐ Director of Quality Assurance |
| `Customer Experience (CX)/Clients.md` | The ⭐ Director of Customer Experience, with the Support Specialist's support record |
| `Public Relations (PR)/Press.md` | The ⭐ Director of Public Relations, with the Communications Specialist's coverage log |
| `Miscellaneous/` | No team: the Chief of Staff routes what fits no department, and the Knowledge Vault Manager files it here |
| A working file in a department folder | The seat that made it, named as that folder's README says |

---

## 📏 Rules

- Venture work starts by looking in `Ventures/` for the company's folder: whether one exists is checked, never assumed.
- A venture folder is created only with a yes, by copying `Ventures/.template/` whole and giving the copy a short hyphenated name (`Example-Company`). A business with clients, employees, revenue or a brand is a venture; one without them is a project.
- Every copied file is filled as the note at its top says, and that note is then deleted: `[Company]` becomes the venture's name, its keyword placeholders become real keywords without `template`, and it takes its real `title`, `description` and `type`, so no placeholder reaches the catalog. Each copied `README.md` becomes its folder's note, typed `index`; `Log.md`, `Decisions.md`, `Financials.md` and `Cap-Table.md` are typed `record`, `Brand.md` and `Standards.md` `standard`, `Sales-Plan.md` `guide`, and every other file `reference`.
- Facts about a venture come only from the owner or the venture's own records: a fact noticed in passing is proposed, and written after a yes. Nothing is guessed or invented.
- Ventures stay apart: two ventures' context is never merged or cross-referenced unless the owner asks.
- Personal information goes to `Profile/` or `Memory/`, and general business knowledge to `Library/`, never here.
- Each fact has one home: a fact another file owns, such as who owns what in `Cap-Table.md` or a metric's definition in `Metrics.md`, is pointed to, never copied.
- Work here goes through the write-gate (`Ventures/README.md`, Structure): internal drafts go ahead; moving money, a contract, outside communication, a change to equity and a deletion need the owner's yes.
- Each venture's `Overview.md` keeps its stage and status current, and its `Log.md` records meaningful work.

---

## 🏗️ Structure

Each venture follows the template in `Ventures/.template/`:

<details>
<summary>The venture template, folder by folder</summary>

```bash
Ventures/
└── [Company]/
    │
    ├── README.md                                The venture's folder note, copied from the template's
    ├── Overview.md                              Profile, market, stage and status, owners and board
    ├── Goals.md                                 The year's objectives, the quarter's OKRs, rocks, grades
    ├── Log.md                                   Running record: decisions, milestones, progress
    │
    ├── Administration/                          Executive office: strategy, decisions, operating cadence
    │   ├── Strategy.md                          Thesis, diagnosis, growth bets, the year's direction
    │   ├── Decisions.md                         One entry per decision, with its memo
    │   └── Cadence.md                           Review loops, board, commitments, loop record
    │
    ├── Finance & Accounting (F&A)/
    │   ├── Financials.md                        Actuals: monthly close, cash, burn, runway, deadlines
    │   ├── Financial-Model.md                   Drivers, projection, budget, scenarios, a round's math
    │   └── Cap-Table.md                         Holders, option pool, convertibles, rounds, founding clocks
    │
    ├── Legal & Compliance (L&C)/
    │   └── Compliance.md                        Entity and IP, contracts, filings, privacy, matters
    │
    ├── Sales & Marketing (S&M)/
    │   ├── Brand.md                             Positioning, voice and tone, visual identity
    │   ├── Products.md                          Product catalog, pricing, each go-to-market
    │   ├── Services.md                          Services catalog: scope, pricing, delivery, capacity
    │   ├── Sales-Plan.md                        Stages, close motion, territory and quota, RevOps
    │   ├── Pipeline.md                          Open deals, the forecast, pricing exceptions
    │   └── Revenue.md                           The revenue plan and the demand plan feeding it
    │
    ├── Operations & Logistics (O&L)/
    │   └── Operations.md                        Processes, SOPs, vendors and costs, programs, KPIs
    │
    ├── Human Resources (HR)/
    │   └── Hierarchy.md                         Org design, role charters, roster, advisors, next hires
    │
    ├── Information Technology (IT)/
    │   └── Stack.md                             Systems register, security, runbooks, incidents
    │
    ├── Research & Development (R&D)/
    │   └── Roadmap.md                           Vision, MVP, experiments, requirements, releases
    │
    ├── Business Intelligence (BI)/
    │   └── Metrics.md                           Metric definitions, north star, scorecard, sources
    │
    ├── Quality Assurance (QA)/
    │   └── Standards.md                         Definitions of done, tests, verifications, defects
    │
    ├── Customer Experience (CX)/
    │   └── Clients.md                           Accounts, health and renewals, playbooks, support
    │
    ├── Public Relations (PR)/
    │   └── Press.md                             Messaging house, press kit, public log, crisis plan
    │
    └── Miscellaneous/
```

Every department folder also holds its own `README.md`, copied with it, saying what belongs there.

</details>

The template carries a **strategic core**: the `Administration/` executive office (`Strategy.md`, the thesis the OKRs ladder up to; `Decisions.md`, the decision record; `Cadence.md`, the operating rhythm) and, in Finance & Accounting, the forward `Financial-Model.md` and the `Cap-Table.md`. Administration writes `Administration/`, and Finance & Accounting writes the model and the cap table, or Administration when it convenes the departments; the cap table records only executed documents.

The **write-gate** holds every write in a venture, by the act, not by the file: internal drafts go ahead; moving money, a contract, outside communication, a change to equity and a deletion need the owner's yes.

---

## 🌱 Creating A Venture Folder

A venture folder is made when the owner mentions a company they own, operate, or are starting, and only once they say yes to the question:

> _"Create a venture folder for [Company]?"_

It is made by copying `.template/` whole and naming the copy in short hyphenated form, and each copied file is then filled as the note at its top says (Rules, above). `update-vault.py` lists it under Ventures, below, and the catalog (`System/Data/catalog.ndjson`) picks up its notes: there is no hand-maintained index to update.

**Signs a venture folder is needed:**

- The owner mentions a company they own, operate, co-found, or actively run
- The work is clearly a business, not just a personal project
- The owner refers, across sessions, to a company that has no folder yet
- The owner asks to set up a company in the BRAIN
- The nature of the work (clients, revenue, employees, brand) makes it clear a venture context is needed

**Venture or project:** if it involves clients, employees, revenue, or a brand operating independently in the market, it is a venture. If it is something the owner is personally building or exploring without that organizational dimension, it is a project.

---

## 🧰 Working Within A Venture

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
- **`Log.md`** gains an entry at the end of any session where meaningful work was done on the venture: decisions made, milestones hit, pivots, hires, launches. Entries stay concise: a date and 2 to 5 bullet points. A gated act the owner confirmed is logged with the confirmation noted. Routine questions and answers are not logged.
- **The other department files** (`Administration/Strategy.md`, `Decisions.md` and `Cadence.md`, `Finance & Accounting (F&A)/Financials.md`, `Financial-Model.md` and `Cap-Table.md`, `Legal & Compliance (L&C)/Compliance.md`, `Sales & Marketing (S&M)/Products.md`, `Services.md`, `Sales-Plan.md`, `Pipeline.md` and `Revenue.md`, `Operations & Logistics (O&L)/Operations.md`, `Human Resources (HR)/Hierarchy.md`, `Information Technology (IT)/Stack.md`, `Research & Development (R&D)/Roadmap.md`, `Business Intelligence (BI)/Metrics.md`, `Quality Assurance (QA)/Standards.md`, `Customer Experience (CX)/Clients.md` and `Public Relations (PR)/Press.md`) follow the same pattern: they are updated when relevant information surfaces, always with the owner's confirmation.

---

## 📈 Venture Stage & Status

Each venture's `Overview.md` says its stage and its status, and stays current:

- A venture's stage changes (for example Pre-revenue to Early Revenue): the change is proposed first, with its evidence, and its **Current Stage** is updated only on the owner's yes.
- A venture goes on hold, closes, or is sold: its **Status**, and once it is closed its **Outcome**, are updated.

Administration reads the declared stage against the venture's real signals (revenue, headcount, retention, the last round, and whether the sales motion repeats) whenever it works on the venture. The ten stages below fold into three operating stages, which set how the venture is run: **found** (Idea, Validation, Pre-revenue, and Early Revenue before the motion repeats), **scale** (Early Revenue once it repeats, Growth and Scaling) and **maintain** (Established, Mature, Plateau and Decline). Where the signals and the declared stage disagree, Administration works at the stage the signals show, names the gap with its evidence, and proposes the change; `Overview.md` changes only on the owner's yes, and the change is logged.

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

A venture is referred to by its folder name exactly as it appears under `Ventures/` (for example `Example-Company`).

---

## 🗂️ Ventures

Each venture folder's README, listed by `update-vault.py` from the folders here; the catalog's `BRAIN/Ventures/` records list every note inside them.

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_No subfolders yet._
<!-- /brain:children -->

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                               | Purpose                                                                                                                                                                        |
| :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`.template/`](.template/README.md) | [Company]'s folder: what its overview, goals and log, its executive office and each department folder hold, and where to begin reading. Read it before any work for [Company]. |
| [`README.md`](README.md)            | This file.                                                                                                                                                                     |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.

---

<div align="center">

**One company, one folder, nothing guessed.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
