# Metrics and KPIs - the measurement glossary

*The metric dictionary for strategize and review. One trusted definition per metric, indexed by function and by stage, so the same number means the same thing every run.*

This is the reference strategize reaches for when it sets the North Star and the OKRs, and review reaches for when it grades them and statuses the venture. Each metric below carries: a definition, the formula, a 2025/26 benchmark band where one is known, a leading-vs-lagging tag, the AR function that owns it, and the stage where it first becomes load-bearing. Two rules hold throughout. First, every number is grounded in a tool or a source, never asserted (see `verification.md`); a benchmark band is a reference point, not a measurement of this venture. Second, a metric is reported against the stage it belongs to: a pre-revenue idea is not graded on the Rule of 40, and a mature company is not run on raw activation. The stage model and the dominant question per stage are in `lifecycle.md`; the benchmark bands that status a number red/amber/green live in `assets/benchmark-bands.json` and back the venture scorecard.

> [!abstract] How to read a metric
> **Leading** metrics move before the outcome and you can still act on them (activation, pipeline coverage, MQL-to-SQL). **Lagging** metrics confirm what already happened (ARR, churned revenue, gross margin). A function should be steered by its leading indicators and judged by its lagging ones. The single canonical KPI source for a live venture is its `Business Intelligence (BI)/Metrics.md`; `Goals.md` references that definition rather than redefining it, so the North Star does not drift between two files.

## The two metrics that sit above the rest

Before the function-by-function glossary, two ideas govern how the others are chosen and used. They are not formulas; they are the discipline that keeps a scorecard from becoming a wall of numbers nobody acts on.

- **The North Star Metric (NSM).** The single output metric that best captures the core value the product delivers to a customer, the one number the whole company is trying to move over the long run. It is durable across quarters and it leads revenue rather than restating it: Airbnb's nights booked, Slack's messages sent within a team, an enterprise tool's weekly active accounts. It must pass three tests: it reflects realized customer value (not vanity reach), the company's growth genuinely depends on it, and a team can actually influence it. Owned by the CEO (Jonathan) as the company's, set in strategize, and written canonically into `Metrics.md` with `Goals.md` pointing at it. Lagging-to-leading: the NSM is a leading indicator of revenue and a lagging indicator of the input metrics beneath it.
- **The One Metric That Matters (OMTM).** The single metric the company concentrates on right now, for this stage and this constraint, to the deliberate exclusion of the rest (Croll and Yoskovitz, *Lean Analytics*). Unlike the durable NSM, the OMTM rotates: at found it is usually an evidence-of-retention or willingness-to-pay number; at scale it is usually an efficiency number (CAC payback, burn multiple, NRR); at maintain it is usually a durability number (Rule of 40, FCF margin). The OMTM is how strategize picks what the quarter is actually about, and how review knows whether the company won the quarter. One company, one NSM; one quarter, one OMTM.

The rest of this file is the inventory the NSM and OMTM are chosen from. Read it twice: once down the **function** index (who owns what), once down the **stage** index (when each becomes load-bearing).

---

## Index by FUNCTION

Each block is the metrics one AR function owns and is judged by. The owning lead is named; the venture file the metric lands in is named; the producing specialist is dispatched per `specialist-dispatch.md`. Definitions are deliberately exact so the number is reproducible.

### Finance and Accounting (CFO Eleanor) - owns the company-level financial and growth set, in `Financials.md`

These are the vital signs the whole board reads. Most are lagging by nature (they confirm an outcome), which is exactly why the function is also judged on the leading inputs to each.

- **ARR / MRR.** Annual (or Monthly) Recurring Revenue: the normalized run-rate of contracted recurring revenue, excluding one-time fees. MRR x 12 = ARR. *Lagging. Load-bearing from scale* (at found it is a vanity signal: revenue lags PMF and tells you little about whether the problem is real).
- **ARR / MRR growth rate.** Period-over-period growth of the run-rate, usually expressed year-over-year. *Benchmark (2025/26):* early-scale SaaS that is on track roughly doubles to triples in the first venture-backed years (T2D3 as the aspirational shape), with year-over-year growth commonly in the 2x-3x band below ~$10M ARR and decaying as the base grows; ~30-40% remains strong at scale. *Lagging. Load-bearing from scale.*
- **Gross margin.** (Revenue - cost of goods sold) / revenue, where COGS for software is hosting, support, and delivery cost to serve. *Benchmark:* 70-80%+ for healthy SaaS; below ~60% signals a services-heavy or infrastructure-heavy model that will not scale like software. *Lagging. Load-bearing from scale.*
- **Net burn.** Cash out minus cash in over a period: the monthly rate at which the bank balance falls. *Leading* (it predicts the runway wall). *Load-bearing from found* (at found, burn and runway are the survival metrics).
- **Runway.** Cash on hand / net monthly burn = months of life left at the current rate. *Leading. Load-bearing from found.* The single most important number at the earliest stage; strategize and review both flag it when it drops below the fundraise-plus-buffer threshold (commonly ~12 months as the line to be already raising).
- **Burn multiple.** Net burn / net new ARR added in the same period: dollars burned to add one dollar of new recurring revenue (David Sacks). *Benchmark:* under 1x is great, 1x-1.5x good, 1.5x-2x suspect, over 2x bad. *Leading* (efficiency of the growth engine). *Load-bearing from scale.* The stage-honest efficiency metric because it works even when growth is lumpy.
- **Rule of 40.** Revenue growth rate (%) + profit margin (%) >= 40, where margin is usually FCF or EBITDA margin. The trade-off rule: a company may grow fast and burn, or grow slower and profit, but the sum should clear 40. *Benchmark:* >= 40 is the bar; top-quartile public SaaS clears it, the median has run below it in 2024/25. *Lagging. Load-bearing from scale (headline above ~$5-10M ARR); suppressed at found* as not-yet-applicable.
- **Magic number.** Net new ARR in a period / sales-and-marketing spend in the prior period: ARR returned per dollar of go-to-market spend. *Benchmark:* ~0.75 and above means the GTM engine is efficient enough to lean into; below ~0.5 means fix efficiency before adding spend. *Leading. Load-bearing from scale; suppressed at found.*
- **FCF / FCF margin.** Free cash flow (operating cash flow minus capex) and FCF as a percent of revenue. *Lagging. Load-bearing from maintain* (durability), though it feeds the Rule of 40 earlier.
- **DSO (Days Sales Outstanding).** (Accounts receivable / revenue) x days in period: average days to collect cash after a sale. *Benchmark:* ~30-45 days is healthy for B2B on net-30 terms; a rising DSO is an early collections or customer-health warning. *Leading. Load-bearing from scale* (it is real once there is a billed book of business). Owned in finance, read by the collections side of operations.

### The unit-economics set (CFO Eleanor, with the revenue and customer functions) - in `Financials.md`, definitions in `Metrics.md`

The economics of acquiring and keeping one customer. These decide whether growth creates or destroys value, so they become load-bearing the moment a repeatable acquisition motion exists.

- **CAC (Customer Acquisition Cost).** Fully loaded sales-and-marketing spend in a period / new customers acquired in that period. Use blended CAC early and paid CAC by channel once channels matter. *Leading. Load-bearing late-found into scale.*
- **LTV (Lifetime Value).** (Average revenue per account x gross margin) / customer churn rate; the gross-margin-adjusted revenue a customer returns over its life. Report LTV on a gross-margin basis, not revenue, or it flatters a low-margin model. *Lagging. Load-bearing from scale.*
- **LTV / CAC ratio.** LTV divided by CAC: dollars of lifetime value returned per dollar spent to acquire. *Benchmark:* ~3x is the healthy floor; below 1x is value-destroying, well above ~5x usually means under-investing in growth. *Lagging. Load-bearing from scale.*
- **CAC payback period.** CAC / (monthly recurring revenue per customer x gross margin): months to recover the acquisition cost from a customer's gross profit. *Benchmark:* under ~12 months is strong, 12-18 acceptable, beyond ~24 is a cash trap. *Leading* (it predicts how cash-hungry growth will be). *Load-bearing from scale.* The most stage-relevant of the four because it speaks directly to runway.

### The retention set (CFO Eleanor and Chief Customer Officer Caleb, jointly) - in `Financials.md` and `Clients.md`

Retention is where SaaS value compounds. These are the metrics a scaling and a mature company are most honestly judged on, because they reveal whether the product is keeping the value it sold.

- **NRR / NDR (Net Revenue Retention).** Recurring revenue from a cohort one year later, including expansion and contraction, divided by its starting revenue, before new logos. Above 100% means the existing book grows on its own. *Benchmark:* >100% is the floor, ~110% solid, 120%+ elite. *Lagging. Load-bearing from scale.* Often the single best predictor of durable growth, and a natural OMTM at scale.
- **GRR (Gross Revenue Retention).** The same cohort's retained revenue excluding expansion, capped at 100%: the pure leak rate before any upsell masks it. *Benchmark:* ~90%+ for SMB, mid-to-high 90s for enterprise; GRR strips out the expansion that can hide real churn. *Lagging. Load-bearing from scale.*
- **Customer / logo churn.** Customers lost in a period / customers at the start of the period. *Benchmark:* low-single-digit monthly for SMB, low-single-digit annual for enterprise. *Lagging, with leading early-warning signals (declining usage, slipped renewals) tracked by CX. Load-bearing from late-found* (the first retention signal that PMF is real) *through maintain.*
- **Revenue churn.** Recurring revenue lost to cancellation and contraction in a period / starting recurring revenue. The dollar-weighted companion to logo churn; the two diverge when churn concentrates in large or small accounts. *Lagging. Load-bearing from scale.*

### Sales and Revenue (CRO Xavier, with AE Brandon; the marketing seats sit here too) - in `Pipeline.md` / `Revenue.md` / `Sales-Plan.md` and `Metrics.md`

The conversion and capacity metrics of the deal engine. Leading where they predict the number, lagging where they record it.

- **Win rate.** Deals won / total deals that reached a decision (won + lost) in a period. *Benchmark:* ~20-30% of qualified opportunities is a common B2B band; track the trend more than the absolute, since stage definitions vary. *Lagging (records closed outcomes), with leading signal in stage-conversion rates. Load-bearing from scale.*
- **Quota attainment.** Closed bookings / assigned quota, per rep and in aggregate. *Benchmark:* a healthy org has the majority (~60%+) of reps at or above quota; if almost none clear it, the quota or the motion is broken, not the reps. *Lagging. Load-bearing from scale* (it needs a repeatable, quota-carrying motion to mean anything).
- **Pipeline coverage.** Open qualified pipeline value / the bookings target for the period. *Benchmark:* ~3x-4x coverage of the target is the common rule of thumb for a normal win rate. *Leading. Load-bearing from scale.* The clearest forward read on whether the number is reachable.
- **Sales cycle length.** Average days from qualified opportunity to closed-won. *Leading* (it sets how fast pipeline converts to cash, and feeds the forecast). *Load-bearing from scale.*

### Marketing (produced from S&R: PMM Felix and Demand Gen Derek, under CRO Xavier) - in `Brand.md` and the GTM surface in `Products.md`

The demand engine's funnel and its efficiency. Almost entirely leading: marketing's job is to move the inputs that revenue lags.

- **MQL (Marketing Qualified Lead).** A lead whose behavior and fit clear the agreed scoring threshold to be worked. *Leading. Load-bearing from scale* (it requires a defined ICP and a scoring model to be meaningful, not a raw signup count).
- **SQL (Sales Qualified Lead).** An MQL that sales has accepted as worth active pursuit. The MQL-to-SQL conversion rate is the real quality signal; a high MQL count with a low conversion is a scoring problem, not a demand win. *Leading. Load-bearing from scale.*
- **Pipeline generated (sourced pipeline).** Qualified pipeline value attributable to marketing in a period, and marketing-sourced as a share of total pipeline. *Leading. Load-bearing from scale.* The metric that ties marketing to revenue rather than to traffic.
- **CAC by channel and blended CAC.** Defined under unit economics above; marketing owns the channel-level decomposition that tells which sources are efficient. *Leading. Load-bearing late-found into scale.*

### Product and R&D (CPO Oliver / Product) - in `Products.md` and `Roadmap.md`

The metrics of whether the product creates and keeps value. These are the earliest honest signals a venture has, which is why product carries the load-bearing metrics at found.

- **Activation rate.** New users (or accounts) reaching the defined first-value milestone / new users in the cohort, within a set window. The milestone is product-specific and must be the moment value is actually felt, not merely a completed signup. *Leading. Load-bearing from found.* One of the truest early PMF signals, and a frequent OMTM in founding.
- **Product / feature retention (cohort retention).** The share of a signup cohort still meaningfully active at day N (D1/D7/D30, or week N for B2B), plotted as a retention curve. A curve that flattens above zero is evidence of product-market fit; one that decays to zero is not. *Leading (of revenue retention and NRR). Load-bearing from found.* The single most important found-stage signal alongside willingness-to-pay.
- **Engagement (DAU/WAU/MAU and the stickiness ratio).** Active users by window, and DAU/MAU as a stickiness measure of how often value is returned to. *Leading. Load-bearing from found through scale,* with the right window chosen for the product's natural cadence (daily tools vs weekly vs monthly).
- **Willingness-to-pay / problem-validation signal.** Qualitative-to-quantitative evidence that a real, urgent problem exists and customers will pay: interview conversion, pre-orders, paid pilots, letters of intent. Not a single formula; the found-stage substitute for revenue. *Leading. Load-bearing at found only,* then it gives way to ARR and retention.

### Operations (Head of Operations Hannah) - in `Operations.md`

The metrics of whether the company can deliver, repeatably and on time.

- **Cycle time.** Average elapsed time from the start to the completion of a defined unit of work (a build, an order, an onboarding, a ticket-to-resolution). *Leading. Load-bearing from scale,* when process and throughput start to matter more than raw founder effort.
- **Throughput.** Units of work completed per period. The capacity-side companion to cycle time; the two together (with SLA attainment) are the operations dashboard. *Leading. Load-bearing from scale.*
- **SLA / on-time attainment.** Share of work delivered within the committed time or quality target. *Lagging on each unit, leading on customer-health trend. Load-bearing from scale.*

### Client Experience (Chief Customer Officer Caleb) - in `Clients.md`

The voice-of-the-customer metrics. They lead retention and therefore lead revenue.

- **NPS (Net Promoter Score).** Share of promoters (9-10) minus share of detractors (0-6) on the 0-10 "would you recommend" question; range -100 to +100. *Benchmark:* positive is table stakes, ~30+ is good, ~50+ is excellent, with wide variance by category. *Leading (of retention and referral). Load-bearing from scale,* and usable as a directional signal earlier. Treat the trend and the verbatim comments as the real signal, not the headline number alone.
- **CSAT (Customer Satisfaction).** Average satisfaction rating on a specific interaction (commonly a 1-5 scale, reported as the percent in the top boxes). *Benchmark:* ~80%+ top-box is a common healthy bar for support. *Lagging on the interaction, leading on churn. Load-bearing from scale.*
- **Time-to-first-value and onboarding completion.** Days for a new customer to reach the activation milestone, and the share completing onboarding. The CX-side companion to product activation; a leading indicator of GRR. *Leading. Load-bearing from late-found.*

---

## Index by STAGE

The same metrics, re-sorted by when they first carry weight. This is the view strategize uses to pick the OMTM and review uses to grade only what the stage warrants. Greying out a not-yet-meaningful metric is a feature, not an omission (see the venture scorecard).

### FOUND (Idea to Seed/MVP) - the dominant question is "is there real evidence of PMF?"

Survival and learning velocity, not optimization. Revenue is a lagging vanity signal here; the load-bearing metrics are qualitative-to-leading.

- **Load-bearing:** runway, net burn, cohort/product retention, activation, meaningful engagement, willingness-to-pay and problem-validation evidence, time-to-first-value.
- **Owner emphasis:** Product/R&D (Oliver) for the value signals; Finance (Eleanor) for runway and burn.
- **Typical OMTM:** an evidence-of-retention or willingness-to-pay number.
- **Explicitly suppressed as not-yet-applicable:** Rule of 40, Magic Number, LTV/CAC at scale, NRR. Reporting them here implies precision the business does not have. Revenue itself is reported but read as a weak lagging signal, not as proof of fit.

### SCALE (Series A to C) - the dominant question is "is the founder the bottleneck, and is each channel actually efficient?"

Turn a validated motion into a repeatable, efficient one. The metrics shift from "does it work" to "does it work profitably and at scale."

- **Load-bearing:** CAC payback, NRR (>100% floor, 120%+ elite), burn multiple, Magic Number, ARR growth rate, gross margin, LTV/CAC, win rate, quota attainment, pipeline coverage, MQL/SQL conversion, sourced pipeline, cycle time, throughput, DSO, NPS/CSAT.
- **Owner emphasis:** Finance (Eleanor) for efficiency and retention economics; Sales and Revenue (CRO Xavier) for the revenue number, pipeline, close, and the demand funnel (the marketing seats sit in S&R); Operations (Hannah) for delivery.
- **Typical OMTM:** an efficiency number (CAC payback, burn multiple, or NRR).
- **Becomes the headline:** the Rule of 40, above roughly $5-10M ARR, once growth and margin are both real enough to trade off against each other.

### MAINTAIN (Established to Mature) - the dominant question is "is the core defended AND is there a funded next S-curve?"

Defend the core and fund the next S-curve; the risk flips from death-by-chaos to death-by-bureaucracy.

- **Load-bearing:** Rule of 40, FCF and FCF margin, durable NRR, GRR, gross margin, durable ARR growth, plus the reinvestment-in-R&D rate read as an anti-aging gauge (loss of hunger and under-investment in the next horizon are the earliest decline signals).
- **Owner emphasis:** Finance (Eleanor) for durability; the CEO (Jonathan) for the horizon-pipeline health that no single financial metric captures.
- **Typical OMTM:** a durability number (Rule of 40 or FCF margin).
- **Watch for:** vanity stability. High current margins with a starved H2/H3 pipeline is the classic pre-decline reading; the scorecard pairs the financial durability metrics with pipeline-of-the-next-S-curve health so the board does not mistake harvesting for health.

---

## How strategize and review use this file

- **Strategize** sets the NSM (once, durable) and chooses the OMTM for the cycle from the stage block above, then writes the OKRs so each key result is a metric from this glossary with a target relative to its benchmark band. It writes the canonical definition into `Metrics.md` and points `Goals.md` at it. If a proposed key result is a metric the stage suppresses, strategize flags it rather than committing the venture to a number that cannot yet mean anything.
- **Review** grades the OKRs and statuses each vital sign red/amber/green against its benchmark band (`assets/benchmark-bands.json`), reads only the stage-appropriate metrics, and greys the rest. It surfaces the leading indicators that moved before any lagging number did, so a problem is caught while it is still a leading metric. Every number it reports is grounded in a tool or source per `verification.md`, and the result is written back to the venture per `write-gate.md`.

The standard holds here as everywhere in board: every angle heard, one owner accountable. Each metric in this glossary has exactly one owning function that is steered by its leading version and judged by its lagging version, and the chair (not the loudest function) decides which metrics the stage makes load-bearing this cycle. Benchmark bands are reference points the BI function refreshes; treat them as the band a number is statused against, never as a measurement of this particular venture.
