<!--
title: '[Company] - Financials'
description: '[Company]''s financial record: every monthly close, the last one in detail, unit economics, debt, and the finance deadlines and open loops. Read it before any work on [Company]''s books, cash, burn, runway or what is due.'
type: 'template'
keywords: ["[the accounting system the company uses]", "template"]
-->

<!-- On copying: this file is copied with the venture's folder to Ventures/[Company]/Finance & Accounting (F&A)/Financials.md. In the copy, replace [Company] with the venture's name everywhere, the title and description included; set type to "record"; replace the keyword placeholder with a word a person would type to find this note that its title does not say (lowercase, at most eight) and drop "template". Finance & Accounting keeps it: once Quality Assurance's check clears a monthly close, it adds the month's row to the close record, rewrites the last close in detail, and brings the deadlines and open loops up to date. Exact figures belong here, but never an account, card or tax ID number, a statement copied in, or one person's pay. At found, the reconciliations and the cash, burn and runway are enough; the statements, the variance and the receivables join at scale. Write only what the owner says or confirms, or what [Company]'s own records show, and leave the rest blank; replace each [bracketed] prompt as it is filled, or delete its line once it does not apply (Ventures/README.md, Rules). Delete this note from the copy. -->

# 💰 [Company] - Financials

> What [Company]'s books show, close by close. Every figure here is an actual from a closed month, tied to its support; the forecast is in `Financial-Model.md`, and who owns [Company] is in `Cap-Table.md`.

---

## Basis

**Books kept in:** [the accounting system]
**Basis:** [cash / accrual]
**Fiscal year ends:** [the month]
**Tax classification:** <!-- how the entity is taxed, where its jurisdiction lets it choose, and why -->
**Currency:**
**Runway floor:** <!-- the cash line the owner has set, below which [Company] starts raising or cutting -->

---

## Close Record

<!-- One row per closed month, newest first. A closed month is never reopened: a correction is booked forward in a later close. -->

| Period | Closed on | Revenue | Net burn | Cash at close | Runway | Cash-zero date | Largest variance, and its cause | Package kept in |
| ------ | --------- | ------- | -------- | ------------- | ------ | -------------- | ------------------------------- | --------------- |
| [YYYY-MM] | [YYYY-MM-DD] | | | | [months] | [YYYY-MM-DD] | | |

**Retention:** [Company]'s financial records are kept for the longest period that the record-keeping rules of each jurisdiction where it files require, checked at the official source: [the period and the rule], as of [YYYY-MM-DD]. Once the record grows long, the months older than that may be condensed into one row a year, with their detail left in the accounting system. The policy flags; the owner decides.

---

## The Last Close in Detail

**Period:** [YYYY-MM]
**Gross margin:**
**Operating spending:**
**Gross burn:**
**Net burn, trailing three months:** <!-- with one-time items split out and named -->
**Days to collect:**

### Reconciliations

| Account | Reconciled to | Status | Notes |
| ------- | ------------- | ------ | ----- |
| [each bank account, by bank and kind, never its number] | [its statement, as of [YYYY-MM-DD]] | [reconciled / open] | |
| [each card account, the same way] | | | |
| Receivables | | | |
| Payables | | | |
| Payroll | | | |

### Entries Booked

| Entry | Kind | Treatment, and its basis |
| ----- | ---- | ------------------------ |
| | [accrual / deferral / revenue recognized / other] | |

### Statements

**Income statement, balance sheet and cash flow statement:** [where the closed statements are kept]

### Revenue by Stream

| Stream | This month | Share of total | Notes |
| ------ | ---------- | -------------- | ----- |
| | | | |

### Spending by Category

| Category | This month | Three-month average | Notes |
| -------- | ---------- | ------------------- | ----- |
| | | | |

### Variance to Budget

<!-- Against the operating budget in Financial-Model.md, explained by cause, never only shown. -->

| Line | Budget | Actual | Variance | Cause | One-time or run-rate |
| ---- | ------ | ------ | -------- | ----- | -------------------- |
| | | | | [volume / price / timing / mix] | [one-time / run-rate] |

### Receivables by Age

| Age | Amount | Accounts |
| --- | ------ | -------- |
| Current | | |
| 1 to 30 days | | |
| 31 to 60 days | | |
| Over 60 days | | |

### Judgment Calls

<!-- The calls the close left for the owner, each with what rides on it. -->

---

## Unit Economics

<!-- Actuals from the closed books, on the definitions in Business Intelligence (BI)/Metrics.md, and only from the stage at which each one is load-bearing; the values the model assumes are in Financial-Model.md. -->

| Metric | Value | Period | Reference band | Notes |
| ------ | ----- | ------ | -------------- | ----- |
| [CAC / LTV / LTV to CAC / CAC payback / burn multiple] | | [YYYY-MM] | | |

---

## Debt

| Lender | Balance at close | Rate | Payment | Matures | Agreement kept in |
| ------ | ---------------- | ---- | ------- | ------- | ----------------- |
| | | | | [YYYY-MM-DD] | |

---

## Funding and Targets

- Who owns [Company], every round, and every SAFE or note outstanding are recorded in `Cap-Table.md` alone; the cash a round brought in shows in the close of the month it landed.
- Revenue, profit and runway targets are set in the venture's `Goals.md`, and the budget behind them in `Financial-Model.md`; each close is read against both.

---

## Finance Deadlines

<!-- In date order: payroll tax deposits and returns, estimated tax payments, sales or value-added tax returns where [Company] is registered, the year-end forms to workers, the company's tax return or its extension, and a fresh valuation before new option grants. Each date is checked every year at its official source and shifted for the fiscal year. The founding clocks are kept in Cap-Table.md, and the legal and regulatory filings on the calendar in Legal & Compliance (L&C)/Compliance.md. -->

| Due | What is due | Rule, and its source | Owner | Status |
| --- | ----------- | -------------------- | ----- | ------ |
| [YYYY-MM-DD] | | [the rule, as of [YYYY-MM-DD]] | | [open / done / missed] |

---

## Open Loops

| Opened | Thread | Owner | Next step |
| ------ | ------ | ----- | --------- |
| [YYYY-MM-DD] | | | |

---

## Notes

<!-- The accounting method, who keeps the books and prepares the returns (by firm or role), and anything else worth knowing before working on [Company]'s money. -->
