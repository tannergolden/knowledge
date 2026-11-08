<!--
title: '[Company] - QA Standards'
description: '[Company]''s quality bar and its record: the definitions of done, the review process, the test plans, the verification record, the defect log, the quality metrics, and the audits and certifications. Read it before checking any consequential [Company] work, or before making a kind of work that must meet a written bar.'
type: 'template'
keywords: ["[the tool the company tracks defects in]", "[the main kind of work the company checks]", "template"]
-->

<!-- On copying: this file is copied with the venture's folder to Ventures/[Company]/Quality Assurance (QA)/Standards.md. In the copy, replace [Company] with the venture's name everywhere, the title and description included; set type to "standard"; replace each keyword placeholder with a word a person would type to find this note that its title does not say (lowercase, at most eight) and drop "template". The quality-assurance skill keeps it. Every clause of a definition of done is a check a stranger could run, agreed with the department that makes the work, and one the whole company holds itself to is accepted by the owner. A verdict comes from someone who did not make the work, and personal data met in a check is cited by where it lives, never copied. Scale it to the stage: at found, a check of what is load-bearing or goes outside; the definitions of done, the test plans and the defect log join at scale. Write only what the owner says or confirms, or what [Company]'s own records show, and leave the rest blank; replace each [bracketed] prompt as it is filled, or delete its line once it does not apply (Ventures/README.md, Rules). Delete this note from the copy. -->

# ✅ [Company] - QA Standards

> The bar [Company]'s work is held to, and the record of every check against it. Nothing passes without evidence, and no one verifies their own work.

---

## Quality Bar

<!-- What done means at [Company], and why the bar sits where it does. -->

---

## Definitions of Done

<!-- One row per kind of deliverable; work that arrives without one goes back to its maker to define done first. -->

| Kind of work | Definition of done, as testable clauses | What it protects | Agreed with | Agreed on |
| ------------ | --------------------------------------- | ---------------- | ----------- | --------- |
| | | | [the department that makes it] | [YYYY-MM-DD] |

---

## Review Process

### Before Anything Goes Out

<!-- The checks made before anything goes to a client or ships. -->

- [ ] [A check]
- [ ] [A check]
- [ ] [A check]

### Who Verifies

**Verifier:** <!-- someone other than the maker, and never shown the maker's reasoning -->
**Turnaround:** [the time a review takes]
**Escalation:** <!-- where a verdict goes when the work contradicts the record or touches an act the owner must approve -->

---

## Test Plans

<!-- Each plan maps every requirement or acceptance criterion to a check, edge and error cases included; the requirements come from Research & Development (R&D)/Roadmap.md or the department that owns the work. -->

| Work under test | Standard | Approved by | Approved on | Status | Plan kept in |
| --------------- | -------- | ----------- | ----------- | ------ | ------------ |
| | | [never the plan's author] | [YYYY-MM-DD] | [draft / approved / run / closed] | |

| Test type | Owner | Frequency | Notes |
| --------- | ----- | --------- | ----- |
| Unit | | | |
| Integration | | | |
| End to end | | | |
| Performance | | | |
| Security | | | [reviewed by the `information-technology` skill] |

---

## Verification Record

<!-- Every verdict on file, newest first, so a pass can be reproduced and a recurring failure seen. -->

| Date | Work checked | Made by | Verdict | Defects | Report kept in |
| ---- | ------------ | ------- | ------- | ------- | -------------- |
| [YYYY-MM-DD] | | | [PASS / PASS WITH NOTED DEFECTS / FAIL / ESCALATE] | | |

---

## Defect Log

**Tracked in:** [the tool, as Information Technology (IT)/Stack.md lists it]
**Response times:** [critical: the time], [major: the time], [minor: the time]

| ID | Found | Summary | Severity | Class | Root cause | Corrective and preventive actions | Status |
| -- | ----- | ------- | -------- | ----- | ---------- | --------------------------------- | ------ |
| [D-1] | [YYYY-MM-DD] | | [critical / major / minor / trivial] | | | [each action, its owner and its date] | [new / confirmed / unconfirmed anomaly / fixed / verified closed] |

---

## Quality Metrics

<!-- Each metric takes its definition from Business Intelligence (BI)/Metrics.md. -->

| Metric | Target | Current | As of | Source |
| ------ | ------ | ------- | ----- | ------ |
| [defect rate] | | | [YYYY-MM-DD] | |
| [rework rate] | | | | |
| [first-pass rate] | | | | |
| [customer-reported issues per month] | | | | |

---

## Audits and Certifications

| Audit or certification | Standard audited against | Last done | Findings | Renews | Report kept in |
| ---------------------- | ------------------------ | --------- | -------- | ------ | -------------- |
| | | [YYYY-MM-DD] | | [YYYY-MM-DD] | |

---

## Notes

<!-- Exceptions to a standard, known quality gaps, and anything else worth knowing before checking [Company]'s work. -->
