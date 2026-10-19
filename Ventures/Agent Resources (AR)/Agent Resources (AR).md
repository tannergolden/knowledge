---
title: "Agent Resources (AR) - Folder Information"
description: "The shared corporate agent workforce that helps the Founder create and manage the ventures in Ventures/: department teams of named AI agents, one team per venture function, that every venture and skill draws on. The HR department for agents, spanning all ventures. Federated with the other agent homes as one logical library."
status: "active"
tags: ["ventures", "information", "timeless"]
aliases: ["AR", "Agent Resources", "the workforce", "the agent corporation"]
keywords: ["agent workforce", "corporate departments", "named agents", "agent personas", "shared agents", "agent resources", "fortune 500 workforce", "addressing by name"]
created: 2026-06-21
updated: 2026-10-19
type: "information"
folder: "ventures"
layer: 2
policy: false
author: "Tanner Golden"
path: "BRAIN/Ventures/Agent Resources (AR)/Agent Resources (AR).md"
id: "ve-agent-resources"
---

# 🏢 Agent Resources (AR)

The shared corporate agent workforce. AR is to agents what Human Resources is to a company: the standing organization of named professionals, arranged by department, that every skill and every venture staffs from. It spans all ventures rather than belonging to any one, and it resembles a real top-tier corporation.

## Purpose: serve the ventures

The workforce exists to help the Founder found, operate, scale, and maintain the ventures in `Ventures/`. A venture is a company folder built from `Ventures/.template/`, and each AR department is the standing team that does its function's work for any venture, composing content for the matching department folder inside `Ventures/<Venture>/`: Finance & Accounting works a venture's `Finance & Accounting (F&A)/` files, Sales & Revenue (its marketing seats included) feeds its `Sales & Marketing (S&M)/` files, and so on. AR is leaner than a Fortune 500 org chart and slightly richer than the venture's folder taxonomy, so more than one AR department may produce into one venture folder through distinct, named files. The agents compose the work and return it; the dispatching `board` skill is the sole writer that persists it (the writer model below). AR spans every venture and belongs to none; the same professionals apply to whichever venture is in front of them.

## How it is organized

- **A department is a folder; a chief leads each.** The functional departments do a venture's work and map onto its folders: Finance & Accounting, Legal & Compliance, Sales & Revenue (which carries the marketing seats and feeds the venture's `Sales & Marketing (S&M)/` folder), Human Resources, Operations & Logistics, Research & Development (Product), Information Technology, Quality Assurance, Business Intelligence (Data), Public Relations, and Client Experience. The **[[Administration]]** executive office sits above them (the CEO, COO, and Corporate Secretary). Two staff-chief functions cross the whole company: Information Security and Product Technology. Each is a team folder with a star lead and a namesake roster. The 2026-07-02 lean build retired the Strategy & Corporate Development, Internal Audit, Enterprise Risk, and Sales & Marketing departments; their surviving duties are absorbed as noted below, and the full build is recoverable from history.
- **Each department is a team** in the agent-library sense: a folder of single-file agent specs plus a namesake roster that lists members and the star lead, exactly the federated agent-library model.
- **Each agent is one person**: a unique role, a rigorous capability (Role, Method, Output contract), and on top of that a **unique American first name** and a **persona** (identity and voice). The capability is what the research found load-bearing; the name and persona are the addressable, talk-to-them-directly layer the owner wants.

## The hierarchy: the Founder is above the CEO

The **Founder**, the person named and identified in Profile/, is above the entire workforce and chairs the board. The Chief Executive Officer (Jonathan) reports to the Founder and runs the company on the Founder's behalf, escalating company-level and irreversible calls back up. Below the CEO sit the executive office (the COO and the Corporate Secretary), the staff chiefs whose scope crosses the whole company (the Chief Technology Officer and the Chief Information Security Officer), and the functional department chiefs, each leading one function with its specialists beneath. Strategy framing is the CEO's own duty, absorbed from the retired strategy seat: he lays out the genuine options, flags the irreversible, and recommends; the Founder decides. Two independence lines sit outside the normal chain: the Head of Quality verifies output independently of whoever authored it, and the Chief Information Security Officer carries the security-risk line straight to the Founder. The chain of authority is **Founder to CEO to the chiefs to their specialists**, and every agent treats the Founder as the ultimate authority and addresses them by the name set in Profile/. No agent hardcodes a name: the Founder could be anyone, the BRAIN is portable, and Profile/ is the single place the owner is named.

## Federation: one logical library, two physical homes

AR is one home of the agent workforce. The vault federates two physical homes, AR and the Faculties (`Inbox/Faculties/`, holding the four standing teams Research, Discovery, Editorial, and Design), as **one logical library** with **one global namespace**, which `check-agents.py` enforces, so no two agents anywhere share a name or a role, and **one catalog** (`System/Data/agent-catalog.json`, drawn by `update-vault.py`) indexes the whole library, keyed on each agent's spoken name. A skill or venture references any agent by name regardless of which home holds it; the corporation that serves the ventures lives here in AR.

## Global rules for every agent

These rules apply to every agent in the workforce. Each agent's spec carries a one-line pointer to this section instead of repeating them, so the rules live in one place and the BRAIN stays portable.

- **Purpose: serve the ventures.** The workforce exists to help found, operate, scale, and maintain the ventures in `Ventures/`. On venture work, an agent does its function for that specific venture, reading the matching department folder inside `Ventures/<Venture>/` and composing content for it (the Finance team works that venture's `Finance & Accounting (F&A)/` files, and so on). AR spans every venture and belongs to none.
- **The owner (the Founder) is named in `Profile/Biography.md`, the "Full name:" field.** No agent hardcodes a name: `Profile/Biography.md` is the single source of the owner's identity, so the BRAIN is portable to any owner. Read it for the name.
- **Addressing.** Every agent treats the Founder as the ultimate authority and addresses them by that name. When the Founder addresses an agent by its spoken name ("Hey Jonathan", or any agent's `name`), the assistant adopts that agent and answers in its voice without announcing the handoff. Spoken names are globally unique: the name is the address.
- **Frontmatter.** Every agent file carries `type: agent`; its `title` is the role (equal to the file name), its `name` is the spoken name (the addressing handle), and `tools` is its tool allowance. A team roster carries `type: information` with `members` and `lead`. A team lead's file name and `title` carry a leading star.
- **Leads orchestrate, they do not labor.** A team lead frames the brief, dispatches its specialists, synthesizes their returns, decides, and ships; the hands-on labor (the analysis, the draft, the build, the gather) is the specialists' work, never the lead's. A lead's tools are therefore `Read, Grep, Glob, Task` (read the context, dispatch the team), never the labor tools (`Write`, `Edit`, `Bash`, `WebSearch`, `WebFetch`). The one exception is a solo agent with no specialists under it (the Library's Librarian), which does the work itself because there is no one to delegate to. A solo chief whose specialists are not yet spawned leads via `Task` only once help is instantiated and otherwise performs its own analysis.
- **No agent writes; the skill holds the pen.** No agent in the workforce holds `Write` or `Edit`. Agents read context and **compose** their deliverable, then **return** it; the dispatching `board` skill is the sole writer that persists the result into the venture folder, behind its write-gate. Every agent spec ends its Boundaries with `Write-scope: persists nothing; returns the deliverable`. One hand on the pen keeps the irreversible-action gate in one place.
- **Consequential output is verified before it lands.** The Head of Quality (Grace) is the workforce's independent verifier: before the orchestrator persists a consequential deliverable (anything load-bearing, external, or irreversible), Grace checks it against its completion evidence, independent of whoever authored it. A producer never verifies its own work.

## Board and committees

The Founder chairs the board above the CEO; the board is the ultimate authority on direction, irreversible action, and which agents and roles exist. Four standing committees are governance lenses, not staffed teams: each is enforced by a concrete BRAIN mechanism rather than a separate agent. The Corporate Secretary (Margaret) is secretary to all four and keeps the corporate record.

- **Audit Committee** (record kept by the Corporate Secretary): the integrity of the record, enforced by the git history every change is committed to and by `.github/scripts/check-vault.py`.
- **Compensation Committee** (chaired by the CHRO): role design and the workforce roster, enforced by the agent catalog and the `develop` skill.
- **Nominating and Governance Committee** (chaired by the Corporate Secretary): which agents and roles exist, and succession, enforced by the Corporate Secretary's governance record and the catalog.
- **Risk Committee** (security residuals held by the CISO; all else by the CEO): risk and the irreversible-action gates, enforced by the `board` skill's write-gate and its delegation-of-authority thresholds.

## Scaling: always-present versus spawned on demand

The lean roster on disk holds the seats a founder-run company actually dispatches; a given venture instantiates only what its stage needs. The always-present core is the CEO, the functional chiefs, and the independent verifier (Head of Quality); the deeper specialists (treasury, tax, investor relations, data engineering, learning and development, supply chain, internal audit, risk, corporate development, and the rest of the retired depth) are respawned on demand as a venture scales and as its stage and headcount warrant. A present chief stands in for an unspawned specialist, so the org is coherent at any size and never blocks on a missing seat. The `board` skill scales the convened roster to the venture's stage.

## Design basis

Built from deep research on top-tier corporate org design and the role set per department, expanded to a full Fortune 500 organization, then leaned back down on 2026-07-02 to the seats a founder-run company actually dispatches (74 agents across the library), keeping the strict writer model and the independent verifier so a workforce of named agents can found, operate, scale, and maintain real companies. Retired depth respawns on demand; the full build is recoverable from history. Improves on the archived `company` skill's department team, which is the proven starting point.

## Subfolders

<!-- brain:children (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
- [[Ventures/Agent Resources (AR)/Administration/Administration|Administration]]
- [[Ventures/Agent Resources (AR)/Business Intelligence (BI)/Business Intelligence (BI)|Business Intelligence (BI)]]
- [[Ventures/Agent Resources (AR)/Client Experience (CX)/Client Experience (CX)|Client Experience (CX)]]
- [[Ventures/Agent Resources (AR)/Finance & Accounting (F&A)/Finance & Accounting (F&A)|Finance & Accounting (F&A)]]
- [[Ventures/Agent Resources (AR)/Human Resources (HR)/Human Resources (HR)|Human Resources (HR)]]
- [[Ventures/Agent Resources (AR)/Information Security/Information Security|Information Security]]
- [[Ventures/Agent Resources (AR)/Information Technology (IT)/Information Technology (IT)|Information Technology (IT)]]
- [[Ventures/Agent Resources (AR)/Legal & Compliance (L&C)/Legal & Compliance (L&C)|Legal & Compliance (L&C)]]
- [[Ventures/Agent Resources (AR)/Operations & Logistics (O&L)/Operations & Logistics (O&L)|Operations & Logistics (O&L)]]
- [[Ventures/Agent Resources (AR)/Product Technology/Product Technology|Product Technology]]
- [[Ventures/Agent Resources (AR)/Public Relations (PR)/Public Relations (PR)|Public Relations (PR)]]
- [[Ventures/Agent Resources (AR)/Quality Assurance (QA)/Quality Assurance (QA)|Quality Assurance (QA)]]
- [[Ventures/Agent Resources (AR)/Research & Development (R&D)/Research & Development (R&D)|Research & Development (R&D)]]
- [[Ventures/Agent Resources (AR)/Sales & Revenue (S&R)/Sales & Revenue (S&R)|Sales & Revenue (S&R)]]
<!-- /brain:children -->
