<!--
title: '[Company] - Roadmap'
description: '[Company]''s product roadmap: the vision, the MVP definition, the bets by horizon, the items now, next and later with the decision behind each, the requirements and their acceptance criteria, the release plan and the experiment log. Read it before any work on what [Company] builds, in what order, and how a release is judged.'
type: 'template'
keywords: ["[the product's name]", "[the current release, as the company names it]", "template"]
-->

<!-- On copying: this file is copied with the venture's folder to Ventures/[Company]/Research & Development (R&D)/Roadmap.md. In the copy, replace [Company] with the venture's name everywhere, the title and description included; set type to "reference"; replace each keyword placeholder with a word a person would type to find this note that its title does not say (lowercase, at most eight) and drop "template". Research & Development keeps it, on the product decisions recorded in Administration/Decisions.md: each item names the decision behind it, and an item with none waits for one. Each requirement carries acceptance criteria a verifier can check, and an invalidated assumption is recorded as such, never quietly dropped. Scale it to the stage: at found, the MVP definition and the experiment log; the roadmap, the requirements and the release plan join at scale. Write only what the owner says or confirms, or what [Company]'s own records show, and leave the rest blank; replace each [bracketed] prompt as it is filled, or delete its line once it does not apply (Ventures/README.md, Rules). Delete this note from the copy. -->

# 🗺️ [Company] - Roadmap

> What [Company] is building, in what order, and how each release is judged. The call on what to build is made in `Administration/Decisions.md`; this file carries it out.

---

## Product Vision

<!-- Where the product is headed in the long run: what the fully realized version does, and for whom. -->

---

## MVP Definition

**Core job:** <!-- the single job the MVP does -->
**Not yet:** <!-- what it deliberately does not do yet -->
**Activation:** <!-- the moment a customer first gets the core value, and how it is measured -->
**Decided:** [YYYY-MM-DD], in `Administration/Decisions.md`

---

## Horizons

<!-- At found, nearly all effort goes to the first horizon; from scale on, a share is kept for the second and third. -->

| Horizon | The bet | Share of effort | Decision | Status |
| ------- | ------- | --------------- | -------- | ------ |
| 1, the core | | | [YYYY-MM-DD] | |
| 2, the next adjacency | | | | |
| 3, the long bet | | | | |

---

## Now

<!-- In active development. Each item's decision is its entry in Administration/Decisions.md, by date. -->

| Item | Horizon | Decision | Requirements | Owner | Target | Status |
| ---- | ------- | -------- | ------------ | ----- | ------ | ------ |
| | [1 / 2 / 3] | [YYYY-MM-DD] | [R-1, R-2] | | [YYYY-MM-DD] | |

---

## Next

<!-- Committed and scoped, not yet started. -->

| Item | Horizon | Decision | Priority | Starts |
| ---- | ------- | -------- | -------- | ------ |
| | | [YYYY-MM-DD] | | [YYYY-MM] |

---

## Later

<!-- Planned but not scoped; each waits for its decision. -->

| Item | Horizon | Why it matters | Decision needed |
| ---- | ------- | -------------- | --------------- |
| | | | |

---

## Backlog

<!-- Ideas and requests: a customer theme from Customer Experience (CX)/Clients.md, an idea promoted from Inbox/Ideas/, or a research finding. A request is evidence for a decision, never a promise. -->

| Item | Source | Weight |
| ---- | ------ | ------ |
| | | |

---

## Requirements

<!-- The requirements each build is held to; Quality Assurance (QA)/Standards.md maps every criterion to a check in its test plan. A requirement with no testable criterion goes back to its decision. -->

| ID | Item | Requirement | Acceptance criteria | Status |
| -- | ---- | ----------- | ------------------- | ------ |
| [R-1] | | | [an observable check, and its pass condition] | [locked / met / changed by the decision of [YYYY-MM-DD]] |

---

## Release Plan

| Release | Items | Target | Go or no-go | Test plan | Shipped |
| ------- | ----- | ------ | ----------- | --------- | ------- |
| | | [YYYY-MM-DD] | [the decision of [YYYY-MM-DD]] | [in Quality Assurance (QA)/Standards.md] | [YYYY-MM-DD] |

---

## Experiment Log

<!-- One row per build-measure-learn loop: the hypothesis, the metric that decides it, the smallest build that tests it, and what was decided on the result. -->

| Started | Hypothesis | The metric that decides it | Smallest build | Result | Then |
| ------- | ---------- | -------------------------- | -------------- | ------ | ---- |
| [YYYY-MM-DD] | | [as Business Intelligence (BI)/Metrics.md defines it] | | [validated / invalidated / unclear], [YYYY-MM-DD] | [persevere / pivot / stop] |

---

## Recently Shipped

| Item | Release | Shipped |
| ---- | ------- | ------- |
| | | [YYYY-MM-DD] |

**Retention:** shipped items are kept for six months. An older one is flagged for removal once any launch or pivot worth remembering is recorded in `Log.md` or `Overview.md`. The policy flags; the owner decides.

---

## Research and Exploration

<!-- Investigations, spikes and prototypes not yet on the committed roadmap. -->

| Topic | The question it answers | Owner | Status | Report |
| ----- | ----------------------- | ----- | ------ | ------ |
| | | | | [the report promoted from Inbox/Research/, or none yet] |

---

## Roadmap Principles

<!-- How trade-offs between items are decided. -->

- [A principle that settles a trade-off]

---

## Notes

<!-- Dependencies, blockers, constraints, and anything else worth knowing about the roadmap. -->
