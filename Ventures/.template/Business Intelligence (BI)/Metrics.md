<!--
title: '[Company] - Metrics'
description: '[Company]''s metrics: the one governed definition of each metric, the north star among them, the scorecard of current values, and the data sources and dashboards behind them. Read it before defining, reporting or grading any number for [Company].'
type: 'template'
keywords: ["[the north star metric]", "[the reporting tool]", "template"]
-->

<!-- On copying: this file is copied with the venture's folder to Ventures/[Company]/Business Intelligence (BI)/Metrics.md. In the copy, replace [Company] with the venture's name everywhere, the title and description included; set type to "reference"; replace each keyword placeholder with a word a person would type to find this note that its title does not say (lowercase, at most eight), delete one that nothing true fills, drop "template", and delete the keywords line if none is left. Business Intelligence keeps it: every other file names a metric from here and never redefines it, and a definition in use is never edited in place, since a change is a new version the owner approves, with the old one kept in its change history. No row about a person is kept here. Copy the definition block for each new metric. Write only what the owner says or confirms, or what [Company]'s own records show, and leave the rest blank; replace each [bracketed] prompt as it is filled, or delete its line once it does not apply (Ventures/README.md, Rules). Delete this note from the copy. -->

# 📊 [Company] - Metrics

> The one definition of every number [Company] runs on. `Goals.md`, the department files and every report name a metric from here; a financial figure itself lives in `Finance & Accounting (F&A)/Financials.md`, and the scorecard below reads it from there.

---

## North Star and the One Metric That Matters

**North star:** [the metric's name] <!-- defined below; the owner chooses it -->
**Why it is the north star:** <!-- it reflects value customers actually get, the company's growth depends on it, and a team can move it -->
**Input metrics that move it:**
**One metric that matters now:** [the metric's name] <!-- the one the stage concentrates on; it changes as the stage does -->
**Chosen by the owner on:** [YYYY-MM-DD]

---

## Metric Definitions

<!-- One entry per metric, listed in the index. Typical metrics by stage: at found, activation, cohort retention, willingness to pay, net burn and runway; at scale, CAC payback, net revenue retention, burn multiple, gross margin, win rate and pipeline coverage; at maintain, the rule of 40, free cash flow margin and gross revenue retention. -->

| Metric | Version | Owner | Leading or lagging | Load-bearing from | North star |
| ------ | ------- | ----- | ------------------ | ----------------- | ---------- |
| [Metric Name] | [1] | | [leading / lagging] | [found / scale / maintain] | [yes / no] |

### [Metric Name]

- **Version:** [1], approved by the owner on [YYYY-MM-DD]
- **Owner:** [the department that acts on it]
- **Question it answers:**
- **Formula:**
- **Unit and population:** [what one unit is, and who is counted]
- **Excluded:** [test accounts, internal users, refunds, free tiers, and why]
- **Sources:** [each input's table or system, and its owner]
- **Window:** [the period, the time zone, and how a partial period is handled]
- **Leading or lagging:** [leading / lagging]
- **Load-bearing from:** [found / scale / maintain]
- **Guard metric:** [the metric that would move if this one were gamed]
- **Benchmark band:** [the band, its source and its date, or none cited]
- **Change history:** [each version, its date, what changed, and whether the history was restated or the break marked]

**Not yet meaningful at this stage:** <!-- the metrics the stage cannot support yet, named rather than reported -->

---

## Scorecard

<!-- The current value of each metric the stage makes load-bearing, read from the record that owns it (a financial figure from Finance & Accounting (F&A)/Financials.md, a pipeline figure from Sales & Marketing (S&M)/Pipeline.md), each with the date it was true and its source. -->

| Metric | Value | As Of | Source | Target or band | Status |
| ------ | ----- | ----- | ------ | -------------- | ------ |
| | | [YYYY-MM-DD] | | | [green / amber / red / not yet meaningful] |

**Retention:** scorecard values are updated in place, and their history stays in the source records and the reporting tool. A definition is versioned, never edited in place, and a metric no longer tracked is marked retired rather than deleted. The policy flags; the owner decides.

---

## Data Sources

<!-- The documentation of the data model: the curated tables, their grain, their tests, and where each source comes from. The model itself lives where the company's data platform keeps it. -->

| Source | System | Grain | Owner | Refresh | Tests | Notes |
| ------ | ------ | ----- | ----- | ------- | ----- | ----- |
|        |        |       |       |         |       |       |

---

## Dashboards and Reports

<!-- What each one watches: each view reads one governed metric and computes nothing of its own. -->

| Dashboard or report | Purpose and reader | Metrics shown, with version | Refresh | Owner | Where it lives |
| ------------------- | ------------------ | --------------------------- | ------- | ----- | -------------- |
|                     |                    |                             |         |       |                |

---

## Notes

<!-- How data is collected, gaps in tracking, known data-quality issues, and anything else worth knowing before analyzing [Company]'s numbers. -->
