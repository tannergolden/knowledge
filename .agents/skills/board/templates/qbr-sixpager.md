# Board and QBR six-pager

*A written, prose pre-read for the quarterly board meeting and the internal quarterly business review: a narrative, not slides. Page 1 opens with the recommendation and the asks; the outward BOARD UPDATE (governance, financials, runway, the asks the Founder must answer) is separated from the inward QBR (last quarter's OKR grades, the next 90 days, the trade-offs). Filed to the venture's `Administration/` by the review mode behind the write-gate, with the Head of Quality verifying every number against a tool or source first (see verification.md, write-gate.md). The skill is the sole writer; agents compose and return.*

This template scaffolds the **review** mode's quarterly deliverable. The review run reads the venture's `Overview.md`, `Goals.md`, `Strategy.md`, and recent `Log.md`, detects the stage (see lifecycle.md), grades the quarter's OKRs, and assembles this six-pager. The CFO (Eleanor) and the FP&A Analyst (Priya) own the financial pages; the Corporate Secretary (Margaret) composes the governance record; the CEO (Jonathan) holds the synthesis and states the recommendation; the Head of Quality (Grace) verifies before the skill persists. One owner is named on every ask and every objective. The standard holds: **every angle heard, one owner accountable**.

## How to use this scaffold

- **Write prose, not bullets-as-slides.** This is a Bezos-style six-pager: full sentences and paragraphs, read in silence at the top of the meeting. The tables here are for the financial and OKR data only; the surrounding analysis is narrative. A reader who only had this document, and never the meeting, should understand the state of the company and the decisions in front of it.
- **Recommendation first.** Page 1 leads with the headline and the asks. Do not bury the recommendation on page 4. The reader learns what you want them to conclude, then reads the case for it.
- **Two audiences, one document, kept separate.** Pages 1 to 3 are the **outward board update** (what owners and directors govern and oversee: financials, runway, governance, the asks). Pages 4 to 6 are the **inward QBR** (how the team ran the company: OKR grades, the next 90 days, the trade-offs being made). Do not blend them; a director reads the first half, the operating team lives in the second.
- **Stage-scale the document.** A found-stage venture leads with PMF evidence, learning velocity, and runway; suppress Rule of 40 and the Magic Number as not-yet-applicable (see metrics-and-kpis.md). A scale-stage venture leads with unit economics and efficiency (CAC payback, NRR, burn multiple). A maintain-stage venture leads with durability and the next S-curve (Rule of 40, FCF, H2/H3 pipeline). Grey out, or drop, any metric not yet load-bearing for the stage rather than reporting a vanity number.
- **Ground every number in a source.** Each financial figure and each OKR grade carries its source (the model, the close, the dashboard, the metric definition). The Head of Quality verifies the document against those sources before the skill writes it; an unverifiable number does not ship (see verification.md).
- **One owner per ask and per objective.** Every ask resolves to a single decider (CEO for in-mandate calls, Founder for the irreversible or major ones), and every objective has one accountable owner. No ask is addressed to "the board" in general.
- **Delete the prompts.** Bracketed text is instruction. Replace it, and remove any section that does not apply to this venture at this stage rather than leaving it empty.

Fill the frontmatter the venture's `Administration/` files use (id rewritten to `<venture>-qbr-<YYYYQn>`, real path, no `[Company]` placeholder, no wikilinks except a deliberate index); this scaffold below the title is plain payload.

---

# [Venture] - Board update and Q[n] [YYYY] review

**Prepared by:** [CEO, with CFO on the financials and Corporate Secretary on the record]   **For:** [the board / the Founder as chair]   **Quarter:** Q[n] [YYYY] ([start date] to [end date])   **Stage:** [found / scale / maintain, per lifecycle.md]   **Verified by:** [Head of Quality, date]

---

## Page 1 - The recommendation and the asks (read this first)

> [!TIP]
> **The headline.**
> [One paragraph. The single most important thing the reader must take away from this quarter, stated as a conclusion, not a teaser. What the company is, where it stands against its thesis, what the quarter proved or disproved, and what you are recommending the board do or approve. If a director read only this paragraph, they would know the state of the company and what is being asked of them.]

**The quarter in one line:** [the result, the way you would say it out loud: "we hit X, missed Y, and the riskiest open question is now Z."]

**The asks.** [Each ask is a specific decision or approval the board or the Founder must make, with the one decider named and the consequence of a yes and a no. Order by what is gating. Asks that need money, a contract, external comms, a delete, or a change to equity or the cap table are hard-gated to the Founder; route them here and do not act on them inside this run (see write-gate.md).]

| # | The ask | Decider | Why now / what it unblocks | Recommended answer |
|---|---|---|---|---|
| 1 | [the specific decision or approval] | [Founder / CEO] | [the gating reason and the consequence] | [your recommendation] |
| 2 | [the specific decision or approval] | [Founder / CEO] | [the gating reason and the consequence] | [your recommendation] |

**What is going well, what is at risk, what changed since last quarter.** [Three short paragraphs or a tight list. The wins worth defending, the risks worth the board's attention, and the one or two things that are materially different from the last board meeting. Name the trend, not just the snapshot.]

---

## Page 2 - Financials, runway, and the plan-versus-actual (outward)

*Owner: CFO (Eleanor), with the FP&A Analyst (Priya) on the model and the Controller (Walter) on the close. Every figure ties to the financial model, the close package, or `Financials.md`; the source is named.*

**Cash and runway (the survival number).** [Cash on hand, monthly net burn, and runway in months at current burn, then at planned burn. State the date the company runs out of money under each case and what the plan is to extend it. This is the number a board reads first; lead the page with it.]

| Metric | This quarter (actual) | Plan | Prior quarter | Source |
|---|---|---|---|---|
| Cash on hand | [$] | [$] | [$] | [model / close] |
| Net monthly burn | [$] | [$] | [$] | [model / close] |
| Runway (months) | [n] | [n] | [n] | [derived] |
| Revenue [/ ARR / MRR] | [$] | [$] | [$] | [close / dashboard] |
| Gross margin | [%] | [%] | [%] | [close] |
| [stage-relevant headline: Rule of 40 / NRR / burn multiple / CAC payback] | [value] | [value] | [value] | [definition] |

**Plan versus actual, and why the variance.** [Narrative. Walk the material variances against the operating plan: what beat, what missed, and the cause of each, not just the size. A variance with no explanation is a flag, not a report. Distinguish a timing variance from a structural one.]

**Stage-relevant unit economics.** [For a scale or maintain venture: CAC, LTV, LTV:CAC, CAC payback, NRR, burn multiple, against their 2025/26 benchmark bands (see metrics-and-kpis.md), each statused. For a found venture: state explicitly that unit economics are not yet load-bearing and report the learning and activation metrics instead. Do not report a metric the stage has not earned.]

**The forward look.** [The next-quarter and next-12-month projection in a sentence or two: the trajectory, the key assumption it rests on, and the point at which the company must raise, cut, or change course. Tie this to the asks on Page 1.]

---

## Page 3 - Governance, risk, and the corporate record (outward)

*Owner: Corporate Secretary (Margaret) for the record, General Counsel (Robert) for legal and compliance, with the relevant chief on each risk. Margaret composes; the skill writes.*

**Decisions of record this quarter.** [The board-level and major management decisions made since the last meeting, each as a one-line entry: the call, the decider, the date, and a pointer to its decision memo in `Administration/Decisions.md`. This is the governance trail; it ties this six-pager to the decisions behind it.]

**Governance and compliance status.** [Entity, cap-table, and filing status in brief: anything the board must ratify, any consent needed, any deadline approaching. Surface the irreversible clocks where they apply: the 83(b) 30-day window and the QSBS 5-year clock for a recently incorporated venture (see founding-playbook.md). Note any open legal or regulatory exposure and its owner.]

**The risk register (top risks, owned).** [The handful of enterprise risks that warrant board attention, each rated by likelihood and impact, with a named owner and the current mitigation. This is the inward-facing pre-mortem made visible to the board; do not launder a real risk into a reassurance.]

| Risk | Likelihood | Impact | Owner | Mitigation / status |
|---|---|---|---|---|
| [the risk] | [H/M/L] | [H/M/L] | [chief] | [what is being done] |
| [the risk] | [H/M/L] | [H/M/L] | [chief] | [what is being done] |

---

## Page 4 - Last quarter's OKRs, graded (inward)

*Owner: CEO (Jonathan), grading against `Goals.md`. Grades are 0.0 to 1.0; committed objectives are expected to land near 1.0, aspirational ones near 0.7. Grade honestly: a board that only ever sees green learns nothing, and a sandbagged 1.0 is as useless as a missed commitment.*

**The grades.** [Each objective and its key results, with the numeric grade, the actual-versus-target, and a one-line "what the grade means." Tag each objective committed or aspirational so a 0.6 on an aspirational moonshot is not read as a 0.6 on a commitment.]

| Objective | Type | Key result | Target | Actual | Grade (0.0-1.0) |
|---|---|---|---|---|---|
| [O1] | [committed / aspirational] | [KR] | [target] | [actual] | [0.0-1.0] |
| | | [KR] | [target] | [actual] | [0.0-1.0] |
| [O2] | [committed / aspirational] | [KR] | [target] | [actual] | [0.0-1.0] |

**What the grades mean, in prose.** [The narrative behind the numbers. Which objectives we hit and why, which we missed and why, and what we now know that we did not at the start of the quarter. Separate a miss caused by a wrong bet from a miss caused by poor execution; they call for different responses. Name the single biggest learning of the quarter.]

**What we are stopping.** [The work, the experiment, or the bet we are explicitly ending because the quarter disproved it or deprioritized it. A QBR that only adds and never stops is not making real trade-offs. Name what dies so the next 90 days have room.]

---

## Page 5 - The next 90 days (inward)

*Owner: CEO (Jonathan), with the COO (Patricia) on the execution plan. These objectives become the venture's `Goals.md` for the coming quarter; this page is the catchball, not a fait accompli.*

**The dominant question for the quarter.** [One sentence. The single question this quarter exists to answer, scaled to the stage: for found, "is there real evidence of PMF?"; for scale, "is the founder the bottleneck, and is each channel actually efficient?"; for maintain, "is the core defended and is there a funded next S-curve?" (see lifecycle.md). Everything below should ladder up to this.]

**Next quarter's OKRs.** [Three to five objectives, each with two to four measurable key results, each tagged committed or aspirational, each with one accountable owner. These ladder up to the thesis in `Strategy.md` and the dominant question above. Set them as catchball: the team proposes, the chair and Founder shape, the owner commits.]

| Objective | Type | Owner | Key results (measurable) |
|---|---|---|---|
| [O1] | [committed / aspirational] | [single owner] | [KR / KR / KR] |
| [O2] | [committed / aspirational] | [single owner] | [KR / KR / KR] |
| [O3] | [committed / aspirational] | [single owner] | [KR / KR / KR] |

**The plan to deliver them.** [Short narrative. The handful of bets and workstreams that move these objectives, who owns each, and the sequencing where one gates another. This is the COO's execution plan in prose, not a Gantt chart. Name the one or two things that, if they slip, put the quarter at risk.]

---

## Page 6 - The trade-offs and the bets (inward)

*Owner: CEO (Jonathan), wearing the strategy hat on the trade-offs. This is the page that earns the document: the honest case for where the company is choosing to spend its finite attention and capital, and what it is choosing not to do.*

**The central trade-off this quarter.** [Prose. The real fork the company faces: the two or three things it could pour the next quarter into and the one it is choosing, with the cost of that choice named. State the road not taken and why. A QBR without a visible trade-off is hiding the decision, not making it.]

**Resource allocation and the horizon mix.** [Where the quarter's capital and attention go, framed by the Three-Horizons split appropriate to the stage (roughly 100/0/0 at found, 70/20/10 at scale and maintain; see lifecycle.md). For a maintain venture, make the case that H2 and H3 are funded and not starved by the defended core. Name the bet that, if it pays off, changes the company.]

**The pre-mortem: how this quarter fails.** [Write the failure story a quarter out, then the mitigations. The ways the plan on Page 5 does not happen, ranked by likelihood, each with what would catch it early and who owns watching for it. This is the inward counterpart to the risk register on Page 3, in the team's own voice.]

**The minority view.** [The dissent, by name and reason, on the recommendation and the plan. Present even when the call is confident. A quarter's plan with no recorded dissent usually means it was smoothed over in the room, not that everyone genuinely agreed (see deliberation.md). Record who disagreed and on what, so the next QBR can check who was right.]

---

*Filed by the review mode to `Administration/` and summarized in `Log.md`; the OKRs on Page 5 are written into `Goals.md` and the stage on `Overview.md` is advanced or flagged if the quarter changed it. Money, contracts, external comms, deletes, and equity in the asks are routed to the Founder, never executed inside this run (see write-gate.md).*
