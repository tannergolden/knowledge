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

| Folder | The skill whose work lands there |
| ------ | -------------------------------- |
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
| `Miscellaneous/` | Anything for [Company] that fits no department |

Each skill named is that department's own, installed with the home kit. The `administration` skill also keeps `Overview.md`, `Goals.md` and `Log.md` current, records each decision in `Administration/Decisions.md` and logs its work in `Log.md`.

## Rules

- Only what the user says or confirms is written here; nothing is guessed or invented.
- [Company]'s context stays apart from every other venture's, unless the user asks to connect them.
- The strategic core (`Administration/`, and in Finance & Accounting `Financial-Model.md` and `Cap-Table.md`) is written only behind a write-gate, by the `administration` skill, or by `finance-and-accounting` for its two files: internal files are drafted directly; money, contracts, outside communication and deletions need the owner's yes.
- `Overview.md` keeps the stage and status current, and `Log.md` gains an entry after meaningful work: a date and 2 to 5 bullet points.
- Personal information goes to `Profile/` or `Memory/`, and general business knowledge to `Library/`, never here.

## Departments

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_The department folders are listed here once update-vault.py runs in the venture's own folder._
<!-- /brain:children -->
