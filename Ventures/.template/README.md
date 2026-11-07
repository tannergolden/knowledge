<!--
title: "[Company]"
description: "The blueprint every venture folder is copied from, whole: this README becomes the venture folder's own, with [Company] replaced and its real title, description and type."
type: "template"
keywords: ["venture folder", "company context", "department folders", "folder readme", "template"]
-->

<!-- On copying: this README comes with the venture's folder. Replace [Company] with the venture's name, set type to "index", and give the copy its real title and description, as for every file copied with it (Ventures/README.md, Rules). Then run update-vault.py, which lists the department folders below. -->

# 🏢 [Company]

The folder of [Company], a venture the user owns or runs: its company-wide context at the root, its executive office in `Administration/`, and a folder for each department. Read this README before changing anything in this folder; its rules add to `Ventures/README.md` and the root `README.md`, and never loosen them.

## Start Here

1. `Overview.md`: what [Company] is, its stage and its status. Read it first.
2. `Goals.md`: current priorities, OKRs and strategic initiatives.
3. `Log.md`: what happened with the venture over time, for recent context.

Then the department files the task needs: each department's `README.md` says what its folder holds.

## Where Each Kind Of Work Goes

| Folder | The work that lands there |
| ------ | ------------------------- |
| `Administration/` | Board work's own records: the strategy, the decision record and the operating cadence |
| `Legal & Compliance (L&C)/` | Legal work, such as the legal skill's: the entity, contracts, IP, licenses, compliance and insurance |
| `Sales & Marketing (S&M)/` | Sales and marketing: the brand, the products and the services |
| `Operations & Logistics (O&L)/` | Operations: core processes, SOPs, vendors and recurring tasks |
| `Human Resources (HR)/` | People: the org structure, reporting lines, roles and key people |
| `Information Technology (IT)/` | Systems, security included: the stack, tools, infrastructure and integrations |
| `Business Intelligence (BI)/` | Analytics: KPIs, dashboards, data sources and reporting |
| `Quality Assurance (QA)/` | Quality: standards, review processes, checklists and quality metrics |
| `Client Experience (CX)/` | Customers: the client roster, accounts, contacts and status |
| `Public Relations (PR)/` | Communications: media contacts, coverage, the press kit and PR strategy |
| `Finance & Accounting (F&A)/` | The company's money, such as the finance skill's: financials, the financial model and the cap table |
| `Research & Development (R&D)/` | Product work, from research, discovery and development: the roadmap and what is being built |
| `Miscellaneous/` | Anything for [Company] that fits no department |

Board work records each decision in `Administration/Decisions.md` and logs its work in `Log.md`.

## Rules

- Only what the user says or confirms is written here; nothing is guessed or invented.
- [Company]'s context stays apart from every other venture's, unless the user asks to connect them.
- Board work is the sole writer of the strategic core (`Administration/`, and in Finance `Financial-Model.md` and `Cap-Table.md`), behind a write-gate: internal files are drafted directly; money, contracts, outside communication and deletions need the owner's yes.
- `Overview.md` keeps the stage and status current, and `Log.md` gains an entry after meaningful work: a date and 2 to 5 bullet points.
- Personal information goes to `Profile/` or `Memory/`, and general business knowledge to `Library/`, never here.

## Departments

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_The department folders are listed here once update-vault.py runs in the venture's own folder._
<!-- /brain:children -->
