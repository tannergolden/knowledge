# Venture scorecard - the stage-aware tiered KPI dashboard

*The one-screen health read for a venture, produced in review mode and written into the venture record. The North Star and the one-metric-that-matters sit on top, then the company vital signs, then a row per function, each number paired with its benchmark band and a red/amber/green status. Metrics not yet load-bearing at the venture's stage are greyed out, not reported as a misleadingly small or empty number. This is a plain markdown scaffold; fill it from the venture's real files, never from recall.*

The scorecard is the standing artifact of a **review** run: the chair reads the venture context and detects the stage (`lifecycle.md`), the functional chiefs return their numbers, the Head of Quality (Grace) verifies that every figure traces to a source (`verification.md`), and the skill writes the assembled scorecard into the venture behind the write-gate (`write-gate.md`). It is one screen on purpose. A board that has to scroll has already lost the read. The standard holds here as everywhere: **every angle heard, one owner accountable**. Every function reports its own row and no other's, each row names the one chief who owns that number, and the chair alone assembles the screen and states the single most important thing on it.

## How to fill it (read before writing a cell)

- **Detect the stage first.** Run the `lifecycle.md` detection (FOUND, SCALE, MAINTAIN) from the venture's real signals before you decide which rows are live. The stage decides which metrics are load-bearing and which are greyed. Put the detected stage in the header; if it disagrees with the declared stage, run the detected one and note the discrepancy (the reconciliation rule in `lifecycle.md`).
- **Ground every number in a source.** Every figure traces to a tool call, a venture file (`Financials.md`, `Metrics.md`, `Hierarchy.md`, recent `Log.md`), or a connected system of record read at run time. A number you cannot trace is not reported; it is left blank with a `no source` note. This is the verifier's first check and the scorecard's first rule.
- **One canonical definition.** The North Star and the core KPIs are defined once, in `Metrics.md` (the BI-owned canonical source). The scorecard reads them; it does not redefine them. If `Goals.md` and `Metrics.md` disagree, that is a finding for the run, not a cell to paper over.
- **Pair every number with its band and a status.** A bare number is not a health read. Each metric carries the benchmark band that makes it legible and a red/amber/green status against that band. The band names its vintage so a 2026 number is not judged against a stale year (`metrics-and-kpis.md`).
- **Grey what is not yet meaningful.** A metric that is not load-bearing at the detected stage is shown greyed with the marker `(n/a at <stage>)`, not filled with a small or empty number. Reporting revenue as a headline for a pre-revenue FOUND venture, or the Rule of 40 below ~$5 to 10M ARR, invites the company to optimize the wrong thing. Greying is an honest signal; a misleading zero is not.
- **Status is a judgment, and it is recorded as one.** R/A/G is a call against the band, not a fact. Where the call is close or the data is thin, say so in the row note. The verifier checks that a green was earned, not asserted.

## Status legend

| Status | Marker | Meaning |
|---|---|---|
| **Green** | 🟢 | At or above the healthy band for the stage; no action implied. |
| **Amber** | 🟡 | Below the healthy band but inside the watch range; a trend to monitor, an action to consider. |
| **Red** | 🔴 | Below the watch range, or a hard floor breached (runway, a covenant, an NRR floor); needs a decision this cycle. |
| **Greyed** | ⚪ | Not yet load-bearing at this stage; suppressed by design, not missing. Shown as `(n/a at <stage>)`. |
| **No source** | ◻️ | Load-bearing but untraceable this run; reported blank with `no source`, flagged for the run, never guessed. |

A status is never inferred from a wished-for answer. A green that the band does not support is the exact failure the verifier exists to catch.

---

# [Venture name] - Venture scorecard

- **Stage (detected):** [FOUND / SCALE / MAINTAIN]   (declared: [taxonomy stage]; [agrees / detected differs, see note])
- **As of:** [YYYY-MM-DD]   **Cycle:** [weekly / monthly / quarterly review]   **Prepared by:** the chair (CEO), verified by the Head of Quality (Grace)
- **Sources:** [Financials.md, Metrics.md, Hierarchy.md, Log.md, and any connected system read this run]

## Tier 1 - North Star and the one metric that matters

The single number the company is built to move, and the one metric that matters most **right now** at this stage. These two sit alone on top because everything below is in service of them.

| | Metric | Value | Trend (vs prior) | Band | Status | Owner | Note / source |
|---|---|---|---|---|---|---|---|
| **North Star** | [from Metrics.md, the canonical definition] | [value] | [▲ / ▼ / flat, with delta] | [healthy band] | [🟢/🟡/🔴] | [CEO / BI] | [the one source] |
| **OMTM** | [the one metric that matters this stage and cycle] | [value] | [▲ / ▼ / flat] | [band] | [🟢/🟡/🔴] | [owning chief] | [why this one, now] |

The OMTM is stage-bound and changes as the venture moves: in FOUND it is almost always a learning or retention signal (activation, cohort retention, willingness-to-pay), not revenue; in SCALE it is an efficiency signal (CAC payback, NRR, burn multiple); in MAINTAIN it is a durability signal (Rule of 40, FCF margin, H2/H3 pipeline health). Pick the one the dominant question of the stage turns on (`lifecycle.md`), and state in the note why it is the one that matters this cycle.

## Tier 2 - Company vital signs

The handful of numbers that say whether the company is alive and on plan, regardless of function. Read these every cycle in every stage; their bands and which are load-bearing shift with the stage.

| Vital sign | Value | Band (2025/26) | Status | Owner | Note / source |
|---|---|---|---|---|---|
| **Runway (months)** | [from Financials.md] | 🔴 <6 / 🟡 6 to 12 / 🟢 >12 (FOUND: >18 preferred) | [status] | CFO (Eleanor) | the hard floor; a red here outranks every green below |
| **Cash / burn (monthly)** | [net burn] | stage-dependent; tie to runway | [status] | CFO (Eleanor) | [source] |
| **Revenue / ARR** | [value] | `(n/a at FOUND - lagging vanity signal)` once detected FOUND | [status or ⚪] | CFO (Eleanor) | greyed at FOUND; load-bearing at SCALE+ |
| **Growth rate** | [%, period] | SCALE: triple-then-double as a rough arc; MAINTAIN: durable single/double digit | [status] | CEO / CFO | `(n/a at FOUND)` |
| **Gross margin** | [%] | software 🟢 ~70%+; services lower by model | [status] | CFO (Eleanor) | [source] |
| **Rule of 40** | [growth% + FCF margin%] | 🟢 ≥40 / 🟡 30 to 40 / 🔴 <30 | [status or ⚪] | CFO (Eleanor) | `(n/a below ~$5 to 10M ARR)`; headline at SCALE-late and MAINTAIN |
| **Headcount** | [from Hierarchy.md] | context, not a band | n/a | CHRO (Vivian) | watch the Dunbar (~150) coordination seam |

A red on runway is the one status that overrides the screen: a venture can be green on every functional row and still be a red company if it runs out of cash. Report it first among the vital signs and never let a healthy function bury it.

## Tier 3 - Function rows

One row per convened function, each reporting its own headline metric (or the two or three that matter at this stage), each paired with its band and status, each owned by one chief. Convene only the functions the venture's stage makes real (`lifecycle.md`, `lenses.md`): a FOUND venture greys most of these, a MAINTAIN venture lights them all. A row a function does not yet have is greyed with `(n/a at <stage>)`, not deleted, so the screen stays stable as the venture grows into its functions.

| Function | Owner | Headline metric | Value | Band (2025/26) | Status | Note / source |
|---|---|---|---|---|---|---|
| **Finance (F&A)** | CFO (Eleanor) | CAC payback (months) | [value] | 🟢 <12 / 🟡 12 to 18 / 🔴 >18 | [status] | `(n/a at FOUND)` |
| **Revenue (Sales)** | CRO | Net Revenue Retention | [value] | 🔴 <100% / 🟡 100 to 120% / 🟢 ≥120% | [status] | floor is 100%; `(n/a at FOUND)` |
| **Revenue (Sales)** | CRO | Burn multiple | [net burn / net new ARR] | 🟢 <1 / 🟡 1 to 2 / 🔴 >2 | [status] | `(n/a at FOUND)` |
| **Revenue (Sales)** | CRO | Magic Number | [net new ARR / prior-Q S&M spend] | 🟢 ≥0.75 / 🟡 0.5 to 0.75 / 🔴 <0.5 | [status] | `(n/a at FOUND)` |
| **Marketing (S&M)** | CRO (Xavier) | Pipeline coverage / qualified pipeline | [value] | vs quota: 🟢 ≥3x / 🟡 2 to 3x / 🔴 <2x | [status] | [source] |
| **Product / R&D** | CPO (Oliver) | Activation / meaningful usage | [value] | stage and product specific | [status] | the FOUND OMTM candidate; cite the cohort |
| **Client Experience (CX)** | Chief Customer Officer (Caleb) | Logo + revenue retention; CSAT/NPS | [value] | retention floors above; NPS context | [status] | split gross vs net retention |
| **Operations (O&L)** | Head of Operations (Hannah) | Cycle time / SLA attainment | [value] | vs the SLA on file | [status] | [source] |
| **People (HR)** | CHRO (Vivian) | Regrettable attrition; time-to-fill | [value] | 🟢 <10% regrettable / 🟡 10 to 15% / 🔴 >15% | [status] | `(thin at FOUND)` |
| **Engineering / IT** | Chief Information Officer (Samuel) | Uptime / SLO attainment; incident MTTR | [value] | vs the SLO on file | [status] | [source] |
| **Data / BI** | Chief Data Officer (Nora) | Metric-definition coverage / data freshness | [value] | governance gauge, not a market band | [status] | owns the canonical defs this scorecard reads |
| **Legal & Compliance** | General Counsel (Robert) | Open obligations / filing calendar status | [value] | 🟢 all current / 🟡 due soon / 🔴 overdue | [status] | surface the 83(b) and QSBS clocks at FOUND |
| **Risk / Audit** | Mechanized: write-gate + health (CISO for security residuals) | Top risks open vs mitigated | [value] | `(dedicated seat respawns on demand)` | [status or ⚪] | greyed until a dedicated seat is real |

The bands above are the 2025/26 starting set; the canonical, vintaged bands live in `metrics-and-kpis.md` and override these when present. Where a function reports more than one metric (Finance and Revenue often do), give it the two or three rows its stage makes load-bearing rather than collapsing it into one and losing the signal. Where a function is not yet seated at the detected stage (Risk/Audit before MAINTAIN, a distinct Sales chief before SCALE), grey the row rather than inventing a number for an owner who does not exist yet.

## The one thing on this screen

[The single most important thing the scorecard says this cycle, stated in one or two sentences, by the chair. Not a summary of every row: the one number that has crossed a band, or the one trend that decides the dominant question of the stage. Name the owner and whether it needs a `decide` run. This is the line the Founder reads first; everything above is the evidence for it.]

## Status changes since last cycle

[What moved across a band since the prior scorecard: each metric that flipped status (🟢→🟡, 🟡→🔴, or recovered), the direction, and the likely cause. A scorecard with no change-log is a snapshot; a scorecard with one is a trend. Keep it to the flips that matter.]

- [metric] - [old status → new status] - [direction and cause] - [owner]

## Stage and write-back

- **Stage on the record:** [confirmed at the detected stage / advanced this cycle, with evidence]. If detection moved the venture across a stage seam (FOUND→SCALE, SCALE→MAINTAIN), this is the moment to advance the stage on the record: the skill updates `Overview.md` (autonomous, an internal field, behind `write-gate.md`) and appends the change with its evidence to `Log.md`.
- **Where this lands:** the assembled scorecard is written by the skill into the venture (the review artifact lives with `Metrics.md` / the Administration cadence record), and a one-line entry is appended to `Log.md` noting the cycle, the stage, and the one thing. Agents compose the rows and the verifier clears them; the skill alone writes, behind the gate. Nothing on this screen moves money, sends a communication, or touches the cap table; if a red row triggers an action that does, that action escalates to the Founder (`write-gate.md`), it is not taken from the scorecard.
