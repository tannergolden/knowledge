<!--
title: "Ventures - Folder Information"
description: "Explains the purpose of the Ventures/ folder: one subfolder per venture, each holding that company's full context and department folders."
type: "index"
keywords: ["companies", "businesses", "company subfolders", "department folders", "business context", "folder overview", "venture structure"]
-->

# 🏢 Ventures/

## Rules

- Before any venture work, look in `Ventures/` for the company's folder: never assume one exists, or that it does not.
- Ask before creating a venture folder, then copy `Ventures/.template/` and give it a short hyphenated name (`Golden-Media`). A business with clients, employees, revenue or a brand is a venture; one without them is a project.
- Fill a venture's files only with what your user tells you, and confirm before writing. Never guess or invent.
- Keep ventures apart: never merge or cross-reference two ventures' context unless asked.
- Personal information goes to `Profile/` or `Memory/`, and general business knowledge to `Library/`, never here.
- Keep each venture's `Overview.md` stage and status current, and log meaningful work in its `Log.md`.

## Purpose

`Ventures/` holds context and working files for every company or business the user owns or operates. Each venture gets its own named subfolder containing company-wide `.md` context files at the root, an `Administration/` executive office, 11 standard department folders, and a `Miscellaneous/` catch-all, for organizing assets, data, and documents.

This folder is for **company-specific** context and materials. General domain knowledge belongs in `Library/`. Personal context belongs in `Profile/` or `Memory/`.

One subfolder of `Ventures/` is not a venture. [[Ventures/Agent Resources (AR)/Agent Resources (AR)|Agent Resources (AR)/]] is the shared corporate agent workforce: the standing organization of named, persona-rich AI agents arranged by department, that every skill and every venture staffs from. It spans all ventures rather than belonging to one, and it is federated with the other agent homes as a single logical library. See its folder doc for the model.

---

## Structure

Each venture follows the template defined in `Ventures/.template/`:

```bash
Ventures/
└── Company-Name/
    │
    ├── Overview.md                              Company profile, mission, vision, industry, stage
    ├── Goals.md                                 OKRs, strategic goals, north star metric, milestones
    ├── Log.md                                   Session log - decisions, milestones, progress over time
    │
    ├── Administration/                          Executive office: strategy, decisions, operating cadence
    │   ├── Strategy.md                          Company thesis, market and competition, strategic bets
    │   ├── Decisions.md                         Governance and decision record (the board's memos)
    │   └── Cadence.md                           Weekly / monthly / quarterly / annual operating rhythm
    │
    ├── Sales & Marketing (S&M)/
    │   ├── Brand.md                             Voice, tone, visual identity, messaging guidelines
    │   ├── Products.md                          Product catalog - descriptions, pricing, status, roadmap
    │   └── Services.md                          Services catalog - scope, pricing, delivery, capacity
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
    ├── Client Experience (CX)/
    │   └── Clients.md                           Client roster - accounts, contacts, status
    │
    └── Business Intelligence (BI)/
        └── Metrics.md                           KPIs, dashboards, data sources, reporting cadence
```

Subfolder names should be short and hyphenated (e.g., `Golden-Media`, `Acme-Corp`). When creating a new venture, copy `Ventures/.template/` and **give each copied file its real `title`, `description` and `type`** (replace the `[Company]` placeholder with the venture's name, and `template` with the type the copy is), so the catalog stays clean; the `board` skill does this in its found mode.

The template carries a **strategic core**: the `Administration/` executive office (`Strategy.md`, the thesis the OKRs ladder up to; `Decisions.md`, the governance record; `Cadence.md`, the operating rhythm) and, in Finance, a forward `Financial-Model.md` and a real `Cap-Table.md`. The Agent Resources (AR) workforce produces a venture's deliverables by **composing** content for these files and returning it; the `board` skill is the **sole writer** that persists it, behind its write-gate (AR drafts internal files autonomously; money, contracts, external comms, and deletes need the Founder). See [[Ventures/Agent Resources (AR)/Agent Resources (AR)|Agent Resources (AR)]].

---

## Creating A Venture Folder

**The AI creates venture folders. The user does not need to do this manually.**

When the user mentions a company they own, operate, or are in the process of starting, the AI should ask:
> *"Want me to create a venture folder for [Company]?"*

If confirmed, the AI creates the folder by copying the `.template/` structure and names it using short hyphenated format (e.g., `Golden-Media`, `Acme-Corp`). The new folder is picked up automatically by the catalog (`System/Data/catalog.ndjson`, drawn by `update-vault.py`) - there is no hand-maintained index to update.

**Triggers for creating a venture folder:**
- User mentions a company they own, operate, co-found, or actively run
- User is working on something that is clearly a business - not just a personal project
- User references a company across sessions that doesn't have a folder yet
- User explicitly asks to set up a company in the BRAIN
- The nature of the work (clients, revenue, employees, brand) makes it clear a venture context is needed

**Venture vs. project - how to tell them apart:**
If it involves clients, employees, revenue, or a brand operating independently in the market - it's a venture. If it's something the user is personally building or exploring without that organizational dimension - it's a project.

---

## Filling Out Context Over Time

**`Ventures/.template/Overview.md` and `Ventures/.template/Sales & Marketing (S&M)/Brand.md` are living documents, not one-time forms.** They are not filled out in a single session - they are built up gradually as the user works on the venture and discusses it with the AI.

When a venture folder is first created, the AI should prompt for the most essential baseline:
> *"To get started, what does [Company] do and what stage is it at?"*

Fill in only what the user provides. Leave everything else blank - do not fabricate or guess.

As subsequent sessions touch on the venture, the AI should:
- Notice when the conversation reveals information that belongs in a context file
- Surface it explicitly before writing:
  > *"You mentioned [Company]'s target customer is X - want me to add that to `Ventures/.template/Overview.md`?"*
- Update the relevant fields after confirmation

**`Ventures/.template/Overview.md` builds from conversations about:**
the company's mission, what it does, its stage, target customers, business model, revenue, key hires, strategic priorities, competitive landscape, and founding story.

**`Ventures/.template/Sales & Marketing (S&M)/Brand.md` builds from conversations about:**
marketing, copywriting, messaging, visual identity, tone of voice, target audience, what the brand stands for, and any session where the AI is writing on behalf of the company.

**`Ventures/.template/Goals.md` builds from conversations about:**
strategic priorities, OKRs, targets, milestones, north star metrics, and any session where the user discusses what the company is trying to accomplish this quarter or year.

**`Ventures/.template/Log.md` is updated by the AI** at the end of any session where meaningful work was done on the venture - decisions made, milestones hit, pivots, hires, launches. Keep entries concise: date + 2–5 bullet points. Do not log routine Q&A.

**Other department files** (`Ventures/.template/Human Resources (HR)/Hierarchy.md`, `Ventures/.template/Client Experience (CX)/Clients.md`, `Ventures/.template/Sales & Marketing (S&M)/Products.md`, `Ventures/.template/Sales & Marketing (S&M)/Services.md`, `Ventures/.template/Finance & Accounting (F&A)/Financials.md`, `Ventures/.template/Information Technology (IT)/Stack.md`, `Ventures/.template/Business Intelligence (BI)/Metrics.md`, `Ventures/.template/Research & Development (R&D)/Roadmap.md`, `Ventures/.template/Operations & Logistics (O&L)/Operations.md`, `Ventures/.template/Legal & Compliance (L&C)/Compliance.md`, `Ventures/.template/Public Relations (PR)/Press.md`, `Ventures/.template/Quality Assurance (QA)/Standards.md`) follow the same pattern - update them when relevant information surfaces, always with user confirmation.

---

## Working Within A Venture

**Always check for an existing folder before doing any venture work.**

When the user mentions or begins working on a specific company, the first step is always to check whether a folder already exists under `Ventures/`. Do not assume - look at the actual directory.

- **Folder exists** → work inside it. Read `Ventures/.template/Overview.md` first, then `Ventures/.template/Goals.md` and `Ventures/.template/Log.md` for current priorities and recent context, then load the relevant department `.md` files for the task.
- **No folder found** → ask:
  > *"I don't see a venture folder for [Company] yet - want me to create one?"*
  If confirmed, create it from `Ventures/.template/`; it is cataloged automatically. If declined, continue the conversation without a folder.

This check applies every time a venture is referenced, not just on first mention. The user may have renamed or restructured folders, so always verify.

- When the user asks about a specific company, read `Ventures/.template/Overview.md` first, then load the relevant department `.md` files for the task
- Department folders hold both `.md` context files and non-AI files (assets, decks, exports, documents) - they are working folders, not just notes
- Do not merge or cross-reference context between ventures unless the user explicitly asks
- Do not store personal (non-work) information here - that belongs in `Profile/` or `Memory/`
- Do not store general business knowledge here - that belongs in `Library/`
- Keep each venture's `Overview.md` current - update its stage and status as the venture evolves

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

## Venture stage & status

There is no hand-maintained index. Each venture is a folder whose `Overview.md` says its stage and status; the live list comes from the catalog: the `BRAIN/Ventures/` records of the committed `System/Data/catalog.ndjson`.

**Keep each venture's `Overview.md` current:**
- A new venture folder is created → it is cataloged automatically
- A venture's stage changes (e.g., Pre-revenue → Early Revenue) → update the Stage in its `Overview.md`
- A venture goes on hold, closes, or is sold → update its Status (and Outcome) in its `Overview.md`

**Stage values** (use these consistently):

| Stage           | Meaning                                                               |
| --------------- | --------------------------------------------------------------------- |
| `Idea`          | Concept only - nothing built or validated yet                         |
| `Validation`    | Testing demand before building - customer discovery, MVPs, waitlists  |
| `Pre-revenue`   | Product or service exists, no paying customers yet                    |
| `Early Revenue` | First customers, actively searching for product-market fit            |
| `Growth`        | Product-market fit found, scaling sales, marketing, and team          |
| `Scaling`       | Aggressive expansion - new markets, significant hiring                |
| `Established`   | Stable, predictable revenue and defined market position               |
| `Mature`        | Dominant or well-settled in market, focus on efficiency and retention |
| `Plateau`       | Growth has stalled - may signal a need to pivot or reinvent           |
| `Decline`       | Revenue or market share actively shrinking                            |

For a closed or exited venture, use one of these as the Outcome value:
`Acquired` · `IPO` · `Wind-down` · `Merged` · `Sold`

Reference a venture by its folder name exactly as it appears under `Ventures/` (e.g., `Golden-Media`).
