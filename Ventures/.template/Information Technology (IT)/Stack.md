<!--
title: '[Company] - Tech Stack'
description: '[Company]''s systems and their security: the systems register, the architecture, the security program, the runbooks, the change reviews, the access reviews, the incidents, the system choices and the domains. Read it before any work on a [Company] system, an integration, someone''s access or a security question.'
type: 'template'
keywords: ["[the main platform the company builds on]", "[the password manager the company uses]", "template"]
-->

<!-- On copying: this file is copied with the venture's folder to Ventures/[Company]/Information Technology (IT)/Stack.md. In the copy, replace [Company] with the venture's name everywhere, the title and description included; set type to "reference"; replace each keyword placeholder with a word a person would type to find this note that its title does not say (lowercase, at most eight), delete one that nothing true fills, drop "template", and delete the keywords line if none is left. Information Technology keeps it: a change updates its system's row, and each change review, access review and incident adds a row. A secret is never written here, only where it is kept and who holds it; what a system costs is in the vendor register in Operations & Logistics (O&L)/Operations.md. Write only what the owner says or confirms, or what [Company]'s own records show, and leave the rest blank; replace each [bracketed] prompt as it is filled, or delete its line once it does not apply (Ventures/README.md, Rules). Delete this note from the copy. -->

# 🧱 [Company] - Tech Stack

> The systems [Company] runs on and how each one is secured. A secret never appears here: only where it lives and who holds it.

---

## Systems Register

<!-- One row per tool or platform, the communication tools (chat, email, video calls) included; a change updates its row. A system's vendor, cost and renewal are in the vendor register in Operations & Logistics (O&L)/Operations.md, and its contract in Legal & Compliance (L&C)/Compliance.md. -->

**As of:** [YYYY-MM-DD]

| System | Purpose | Owner | Access by role | Admins | Sign-in | Data held | Secrets kept in | Connects to | Backup | Next access review |
| ------ | ------- | ----- | -------------- | ------ | ------- | --------- | --------------- | ----------- | ------ | ------------------ |
| [identity provider] | | [one person or role] | [roles or groups, and what each may do] | [as few as the work allows] | [single sign-on / second factor] | [its kind and sensitivity] | [the store, and who holds it] | | [what, how often, last restored on [YYYY-MM-DD]] | [YYYY-MM-DD] |
| [email and calendar] | | | | | | | | | | |
| [chat and video calls] | | | | | | | | | | |

---

## Architecture

**Diagram:** [where the diagram of how the systems connect is kept]
**Hosting:** [the provider and regions]
**Build and deploy:** <!-- how changes reach the live systems -->
**Monitoring and alerting:**
**Logging:**

<!-- The product's own architecture belongs to its build, kept by Research & Development (R&D) in the product's repository; this is the internal stack. -->

---

## Security Program

**Access policy:** [where it is kept], last reviewed on [YYYY-MM-DD]
**Single sign-on:** <!-- required for which systems -->
**Second factor:** <!-- required everywhere it can be; each exception, and why -->
**Admin access:** <!-- how it is granted, and when it expires -->
**Automations:** <!-- each one under its own identity, never a person's account -->
**Access reviews:** [how often]
**Secrets and passwords:** [the manager they are kept in, and who administers it]
**Monitoring:** <!-- what is watched, by whom, and what raises an alarm -->

| Control | The threat it closes | Owner | Since |
| ------- | -------------------- | ----- | ----- |
| | | | [YYYY-MM-DD] |

---

## Runbooks

| Runbook | Covers | Owner | Last tested | Kept in |
| ------- | ------ | ----- | ----------- | ------- |
| [Joiners, movers and leavers] | | | [YYYY-MM-DD / untested] | |
| [Restoring [a critical system]] | | | | |
| [Incident playbook: [kind]] | | | | |

---

## Change Reviews

<!-- One row per change to [Company]'s systems; the review itself, with its blast radius, design, way back and threat review, is a working file. -->

| Date | Change | Verdict | Security call | Gated steps confirmed by the owner | Review kept in |
| ---- | ------ | ------- | ------------- | ---------------------------------- | -------------- |
| [YYYY-MM-DD] | | [pass / pass with mitigations / block] | [accept / mitigate / refuse / not needed] | [YYYY-MM-DD / waiting] | |

---

## Access Reviews

| Date | Scope | Found | Removals | Confirmed by the owner |
| ---- | ----- | ----- | -------- | ---------------------- |
| [YYYY-MM-DD] | | [standing admin, shared accounts, accounts of people who left, automations running as a person] | [prepared / done] | [YYYY-MM-DD / waiting] |

---

## Incidents

| Opened | What happened | Kind | Severity | Status | Record kept in |
| ------ | ------------- | ---- | -------- | ------ | -------------- |
| [YYYY-MM-DD] | | [security incident / outage] | [high / medium / low] | [contained / eradicated / recovered / closed] | |

---

## System Choices

<!-- One entry per choice of system; Administration/Decisions.md points here. -->

| Date | Chosen | For | Alternatives considered | Why | Revisit if |
| ---- | ------ | --- | ----------------------- | --- | ---------- |
| [YYYY-MM-DD] | | | | | |

---

## Domains

| Domain | Purpose | Registrar | Renews | Owner |
| ------ | ------- | --------- | ------ | ----- |
| | | | [YYYY-MM-DD] | |

---

## Retiring or Under Evaluation

| System | Status | Replacement | By |
| ------ | ------ | ----------- | -- |
| | [evaluating / retiring] | | [YYYY-MM] |

---

## Notes

<!-- Technical debt, migration plans, and anything else worth knowing before a change to [Company]'s systems. -->
