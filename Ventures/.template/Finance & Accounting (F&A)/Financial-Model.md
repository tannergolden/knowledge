<!--
title: '[Company] - Financial Model'
description: '[Company]''s forward model: the drivers, the projection, the scenarios and the runway each one gives, the unit economics it assumes, the operating budget, the change from the last model, and a round''s math when one is in play. Read it before a plan, a raise, a major spend or hire, or any question about how long [Company]''s money lasts.'
type: 'template'
keywords: ["[the round or plan the model serves]", "template"]
-->

<!-- On copying: this file is copied with the venture's folder to Ventures/[Company]/Finance & Accounting (F&A)/Financial-Model.md. In the copy, replace [Company] with the venture's name everywhere, the title and description included; set type to "reference"; replace the keyword placeholder with a word a person would type to find this note that its title does not say (lowercase, at most eight), or delete it when nothing true fills it, drop "template", and delete the keywords line if none is left. Finance & Accounting builds it on the closed actuals in Financials.md, the Chief Financial Officer approves it, or the owner where [Company] has none, and it lands only once Quality Assurance's check clears it; it is rolled forward each quarter. Every number traces to a source or a marked assumption, and none is backsolved. Scale it to the stage: at found, a monthly cash projection through the next raise plus a buffer; at scale, the three statements tied and the unit economics; at maintain, free cash flow and the rule of 40. Write only what the owner says or confirms, or what [Company]'s own records show, and leave the rest blank; replace each [bracketed] prompt as it is filled, or delete its line once it does not apply (Ventures/README.md, Rules). Delete this note from the copy. -->

# 🧮 [Company] - Financial Model

> Where [Company]'s money is headed, built from named drivers on the last closed month. The actuals are in `Financials.md`; this file holds the forecast, the budget and the runway they give.

---

## Basis

**The question it serves:** [a planning cycle / a raise / a major spend or hire / a runway question]
**Basis and periods:** [cash / accrual]; monthly for the first [12 to 24] months, then by year
**Actuals base:** the close of [YYYY-MM], from `Financials.md`
**Horizon:** through [YYYY-MM], at least the next raise plus a buffer
**Operating stage when built:** [found / scale / maintain], from `Overview.md` on [YYYY-MM-DD]

---

## Bottom Line

**Runway, base case:** [months], cash-zero on [YYYY-MM-DD]
**Runway, downside:** [months], cash-zero on [YYYY-MM-DD]
**When to raise:** [YYYY-MM] <!-- the month the downside case's cash reaches the runway floor in Financials.md, Basis; with no floor set, the month its runway reaches about twelve months -->
**The driver that moves it most:** <!-- the driver, and how far the runway moves for a stated change in it -->

---

## Drivers

<!-- Everything below derives from these. Each carries its source, or is marked as an assumption naming the department that owns it, so the model can be checked rather than taken on trust. -->

| Driver | Value | Source or assumption | Owner | Sensitivity |
| ------ | ----- | -------------------- | ----- | ----------- |
| New bookings per month | | [the forecast in Sales & Marketing (S&M)/Pipeline.md and the revenue plan in Sales & Marketing (S&M)/Revenue.md, as of [YYYY-MM-DD], or a marked assumption] | Sales & Marketing (S&M) | [high / medium / low] |
| Price and billing terms | | | | |
| Churn | | | | |
| Gross margin | | | | |
| Headcount, by role and start month, fully loaded | | [the hiring plan Human Resources (HR)/Hierarchy.md points to, as of [YYYY-MM-DD], or a marked assumption] | Human Resources (HR) | |
| Other spending, by driver or contract | | | | |

---

## Projection

| Period | Revenue | Gross margin | Operating spending | Net burn | Cash at period end |
| ------ | ------- | ------------ | ------------------ | -------- | ------------------ |
| [YYYY-MM] | | | | | |

**The three statements:** [where the tied income statement, balance sheet and cash flow statement are kept, from scale on]

---

## Scenarios

<!-- Each scenario flexes its own drivers: the downside has its own churn, bookings and hiring pace, never the base case with a haircut. -->

| Scenario | Drivers flexed, with their values | Runway | Cash-zero date | Breakeven month |
| -------- | --------------------------------- | ------ | -------------- | --------------- |
| Base | | [months] | [YYYY-MM-DD] | [YYYY-MM] |
| Downside | | | | |
| Upside, where it informs the call | | | | |

---

## Unit Economics

<!-- The values the model assumes, from the stage at which each one is load-bearing, on the definitions in Business Intelligence (BI)/Metrics.md; the actuals are in Financials.md. -->

| Metric | Value assumed | Reference band |
| ------ | ------------- | -------------- |
| [CAC / LTV / LTV to CAC / CAC payback / gross margin / burn multiple] | | [the band, its source and its date] |

---

## Operating Budget

<!-- Tied to the base case: spending by department and month, and headcount by role and start month. Each monthly close in Financials.md is measured against it. -->

**Covers:** [the fiscal year]
**Authorized by the owner on:** [YYYY-MM-DD]

| Department | [YYYY-MM] | [YYYY-MM] | [YYYY-MM] | Year | Owner |
| ---------- | --------- | --------- | --------- | ---- | ----- |
| [each department that spends] | | | | | |

<!-- Open and planned roles only: a filled role is counted in its department's line above, so no row shows one person's pay. -->

| Role | Department | Starts | Fully loaded cost |
| ---- | ---------- | ------ | ----------------- |
| | | [YYYY-MM] | |

---

## Change From the Last Model

<!-- How this model differs from the one before it, line by line. Each close's variance against the budget is in Financials.md, The Last Close in Detail. -->

| Line | Last model | This model | Change | Cause |
| ---- | ---------- | ---------- | ------ | ----- |
| | | | | [volume / price / timing / mix / a new assumption] |

---

## A Round, When One Is in Play

<!-- The math only. The instruments are drafted in Legal & Compliance (L&C)/ and signed by the owner, and the result enters Cap-Table.md once the documents are executed. -->

**Size and milestone:** <!-- the months of runway it buys at the model's burn, the buffer, and the milestone it reaches -->
**Valuation:** [pre-money / post-money / price per share]
**Pool and instruments:** <!-- the option pool's top-up and whom it dilutes; each SAFE and note converted by its own terms, stacked caps converting together, with the price or valuation each converts at stated as an assumption -->
**Dilution:** <!-- each holder's percentage before and after, as a pro forma cap table -->

---

## Review

**Approved by:** [the Chief Financial Officer / the owner], on [YYYY-MM-DD]
**Independent check:** [PASS / PASS WITH NOTED DEFECTS / FAIL / ESCALATE], on [YYYY-MM-DD], recorded in `Quality Assurance (QA)/Standards.md`, Verification Record, with its findings applied
**Next reforecast:** [YYYY-MM-DD]

---

## Notes

<!-- What the model leaves out, the assumptions still to confirm, and anything else worth knowing before relying on it. -->
