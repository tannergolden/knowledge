# Operating cadence - the rhythm of REVIEW mode

*The operating rhythm for review runs: the four nested loops (weekly business review, monthly review, quarterly QBR plus planning, annual planning) and the board cadence, each with a fixed agenda, its inputs and outputs, and the metric and ownership discipline that keeps the loops honest.*

REVIEW is the mode that keeps a running venture honest over time. Where strategize sets the OKRs and operate produces the work, review runs the clock: it grades what the OKRs said against what actually happened, keeps `Overview.md`/`Goals.md`/`Log.md` current, and advances or flags the lifecycle stage. The cadence is a set of **nested loops at decreasing frequency and increasing altitude**: the weekly loop runs the numbers, the monthly loop reads the money, the quarterly loop grades the OKRs and resets them, and the annual loop sets the thesis the quarters ladder up to. A shorter loop never re-decides what a longer loop owns; it executes inside the frame the longer loop set. The standard holds here as everywhere: **every angle heard, one owner accountable**. Each review reads the relevant functions, the chair synthesizes, one owner is named per number and per action, and the skill is the sole writer (see `write-gate.md`).

This file gives each loop its fixed agenda, inputs (which venture files), and outputs (what gets written where), then the cross-cutting disciplines every loop obeys: input-vs-output metrics, single-threaded owners, catchball, and disagree-and-commit. Scale the loops to the venture's stage (see `lifecycle.md`); a pre-revenue idea and a mature company do not run the same cadence, and the stage-by-stage cadence is in the last section. The named operating systems this draws on (OKRs, EOS Level 10 and the scorecard, Amazon WBR and the six-pager, V2MOM) are cited where they apply.

## The principle: nested loops, fixed agendas

A review meeting with no fixed agenda becomes storytelling, and storytelling is how a number that is quietly drifting stays unspoken. Every loop below has a **fixed agenda run in the same order every time**, so the same questions get asked whether the news is good or bad. This is the EOS *Level 10 Meeting* discipline (Wickman, *Traction*): a same-agenda, same-time weekly meeting that ends with a clear IDS pass (Identify, Discuss, Solve) on the issues, not a recap. It is the Amazon WBR discipline: a standing deck of metrics reviewed in the same sequence every week so anomalies surface by their shape, not by who chooses to mention them.

The loops nest. Each longer loop **owns the frame the shorter loops execute inside**:

| Loop | Frequency | Altitude | Owns | Reads from the loop below |
|------|-----------|----------|------|----------------------------|
| Weekly business review (WBR / L10) | Weekly | The numbers and this week's blockers | Whether the plan is on track this week | (the floor: live operating data) |
| Monthly review | Monthly | Money and plan-vs-actual | Spend, runway, and the monthly trend | The four weeklies' resolved and unresolved issues |
| Quarterly QBR + planning | Quarterly | OKR grading and the next 90 days | The quarter's grade and the next quarter's OKRs | The three monthlies' financial trend |
| Annual planning | Yearly | Thesis and annual objectives | The year's strategy and the OKR ladder's top | The four quarters' grades |

The board cadence runs alongside, not inside, this stack: the board governs and oversees (the Founder as chair), management executes. Its frequency and the pre-read are below.

## Loop 1: Weekly business review (WBR / Level 10)

The floor of the cadence: a short, same-agenda weekly that reads the numbers, confirms the plan is on track, and resolves this week's blockers. Models drawn on: the EOS **Level 10 Meeting** (a 90-minute weekly with a fixed agenda ending in IDS) and the Amazon **WBR** (a standing metrics review where the deck is the same every week so the trend reads itself).

**Fixed agenda (same order every week):**
1. **Scorecard read.** The 5 to 15 weekly numbers, each with its owner, its target, and on-track / off-track. This is the EOS **scorecard**: a handful of leading numbers that predict the result, read in under five minutes. No discussion yet, just on or off track.
2. **OKR / rock check.** Each quarterly priority (EOS calls them rocks) is on-track or off-track, one word each. Off-track drops to the issues list, it is not solved in the read.
3. **Headlines and customer/employee signal.** A sentence each: what changed, what a customer or the market did.
4. **Prior-action review.** Last week's to-dos: done or not done. Not-done rolls forward or becomes an issue.
5. **IDS the issues.** Identify, Discuss, Solve the off-track items and new blockers, hardest-first, until time or the list is out. Each solved issue ends with a single owner and a due date.

**Inputs (venture files read):** `Metrics.md` (the scorecard definitions and live numbers, the canonical KPI source), `Goals.md` (the active OKRs and rocks), recent `Log.md` (last week's actions), and whatever live operating data the dispatched functions return (BI for the numbers, the relevant chiefs for their lines). See `specialist-dispatch.md` for how a lead frames the read.

**Outputs (what the skill writes):** a dated `Log.md` entry, the week's scorecard status and the new action list with owners and due dates; off-track rocks flagged; any decision made in IDS recorded per `write-gate.md`. No `Goals.md` rewrite, the weekly executes the quarter, it does not reset it.

**Discipline:** keep it to leading numbers and this week's blockers. The weekly is where input metrics live (see the metric discipline below); a weekly that debates the annual revenue number is mis-altitude. Storytelling is the failure mode, so the read is numbers-first and the discussion is issues-only.

## Loop 2: Monthly review

The money loop: read plan-vs-actual, the cash and runway, and the month's trend across the four weeklies. This is the management complement to the monthly board update at early stage, and the internal close review once the books are real.

**Fixed agenda:**
1. **Financials vs plan.** Actuals against the operating budget: revenue, spend, burn, cash, runway. Variances named and explained, not just shown (see Finance's variance analysis in `department-deliverable-catalog.md`).
2. **The month's metric trend.** The scorecard rolled up to the month: what moved, what is drifting, what crossed a threshold.
3. **OKR mid-quarter check.** Are the quarter's OKRs trending to their targets at the one-third and two-thirds marks. Off-pace OKRs get a recovery plan or an explicit de-scope, named now rather than discovered at the QBR.
4. **Risks and decisions.** What needs a decision this month, routed to a decide run if consequential (see `modes-router.md`); what risk crossed its threshold.

**Inputs:** `Financials.md` (the model, the budget, the close package), `Metrics.md` (the monthly roll-up), `Goals.md` (OKR mid-quarter status), the four weeklies' `Log.md` entries.

**Outputs:** a dated `Log.md` entry with the month's financial summary and variance notes; updated trend status on the OKRs in `Goals.md`; any recovery plan or de-scope recorded; the monthly reporting package (the board deck at board-cadence months) assembled into `Administration/` per `write-gate.md`. Moving money or sending anything external is hard-gated to the Founder.

## Loop 3: Quarterly business review (QBR) plus planning

The grading-and-reset loop, the most consequential of the four. It does two distinct jobs back to back: **grade the quarter that closed**, then **set the quarter that opens**. Keep them separate; grading the old honestly is what makes the new realistic.

**Part A, grade the quarter (the QBR):**
1. **OKR grading.** Each key result scored **0.0 to 1.0** on the Google OKR convention: ~0.7 is the target for a well-set aspirational OKR (consistently hitting 1.0 means the OKRs were sandbagged; consistently missing 0.3 means they were fantasy). Committed OKRs are expected at 1.0; aspirational OKRs at ~0.7 (see the committed-vs-aspirational split below).
2. **What the grade means.** For each OKR: hit, missed, or de-scoped, and *why* in one line, learning not excuse.
3. **The number trend across the quarter.** The three monthlies read as one arc: durable progress or a flattering spike.
4. **Stage check.** Do the real signals (ARR, retention, headcount, last round) still match the declared stage, or has the venture crossed into the next one (see `lifecycle.md`). The QBR is where a stage advance is proposed.

**Part B, set the next quarter (planning):**
5. **Next-quarter OKRs**, laddering up from the annual objectives, set by **catchball** (the disciplined back-and-forth between altitude and function, below), each committed-or-aspirational and each with a single-threaded owner.
6. **The rocks** (the 3 to 7 priorities that must get done) and their owners.
7. **Recalibrate the operating plan and the budget** to the new OKRs.

**Inputs:** `Goals.md` (the closing OKRs and the annual objectives above them), `Strategy.md` (the thesis the OKRs serve), `Financials.md` (the trend and the budget to recalibrate), `Metrics.md`, the three monthlies. This is a deeper run: convene the relevant chiefs for their function's OKRs, BI for the numbers, the chair (CEO) holding the stage and strategy fit, the verifier on the grades (a function does not grade its own OKR unchecked; see `verification.md`).

**Outputs:** the QBR narrative (the six-pager, below) filed to `Administration/`; the **regraded closing OKRs and the new quarter's OKRs written into `Goals.md`**; a stage advance written to `Overview.md` if the QBR carried it (a gated change, confirm per `write-gate.md`); a dated `Log.md` entry recording the grade and the reset. This is the loop that most changes the venture's files, so the commit-before-write and sole-writer rules are load-bearing here.

## Loop 4: Annual planning

The top loop: set or refresh the company thesis and the annual objectives the four quarters ladder up to. Annual planning is a **strategize** run in substance (see `strategy-toolkit.md`), surfaced in the cadence because it is the frame every shorter loop executes inside. The named system here is **V2MOM** (Salesforce: Vision, Values, Methods, Obstacles, Measures), a one-document annual alignment artifact that states the year's vision and the measures that prove it, and OKRs at the annual tier (annual objectives that the quarterly OKRs serve).

**Fixed agenda:**
1. **Read the year that closed.** The four QBR grades as one arc: what the year actually delivered against what it promised.
2. **Refresh the thesis.** Does `Strategy.md` still hold; what changed in the market, the model, the stage.
3. **Set the annual objectives** (or the V2MOM) for the year: the 3 to 5 objectives everything ladders up to, with their annual measures.
4. **Allocate.** The Three-Horizons split for the stage (see `lifecycle.md`): how much to the core, the next S-curve, and the bets.
5. **Cascade to Q1 OKRs** by catchball, so the year opens with the first quarter already set.

**Inputs:** `Strategy.md`, `Goals.md` (the year's OKR history), `Financials.md` (the annual model and the next year's budget), `Overview.md` (the stage), the four QBR narratives.

**Outputs:** a refreshed `Strategy.md` (the thesis and the annual objectives or V2MOM); the year's top-level objectives in `Goals.md`; the Q1 OKRs; a dated `Log.md` entry. A material change of thesis is a consequential change, so it is offered, framed, and confirmed, never silently rewritten.

## The board cadence (governance, alongside the stack)

The board is the owners' layer; here the **Founder is the board chair**, and the board governs and oversees while management (the CEO and the AR executive office) executes. The board cadence is not one of the four nested management loops, it runs parallel to them, and its job is governance, not operating the numbers.

**The board pre-read is written, not slides.** The model is the Amazon **six-pager**: a narrative memo read in silence at the top of the meeting, no bullet-slide deck, because a sentence forces a logic that a bullet hides ("the narrative structure of a good memo forces better thought and better understanding than the bullet points of PowerPoint" - Bezos shareholder letter). The board six-pager separates the **outward board update** (governance, financials, the asks, the risks) from any **inward operating detail**, and ends with the explicit asks that need the board's call.

**Board agenda:** financials and runway; progress against the annual objectives; the material decisions and risks since last board; the asks (capital, hires, gated approvals); and governance items (the Corporate Secretary's record). Anything that moves money, changes equity or the cap table, or commits the company externally is a Founder-gated action regardless of board discussion (see `write-gate.md`).

**Frequency scales with stage** (detailed below): monthly at found, monthly trending to quarterly through scale, quarterly at maintain.

**Inputs:** `Financials.md`, `Goals.md`, `Strategy.md`, `Administration/` (decisions and governance record), recent `Log.md`. **Outputs:** the board six-pager to `Administration/`; the decisions and minutes to the governance record; a dated `Log.md` entry. The Corporate Secretary composes the governance record and the skill writes it (a Read-only agent never files; the skill is the sole writer).

## Cross-cutting discipline 1: input vs output metrics (leading vs lagging)

The single most important metric discipline in the cadence. **Output metrics are lagging** (revenue, ARR, NRR, profit), they tell you the result but you cannot act on them directly. **Input metrics are leading** (the controllable activities that drive the outputs: outreach sent, activation rate, time-to-first-value, pipeline created, cycle time), they predict the result and you *can* act on them this week. This is the Amazon doctrine of **controllable input metrics**: manage the inputs you control, and the outputs follow; chase the outputs directly and you have nothing to pull.

The cadence enforces this by altitude:
- **The weekly loop is the home of input metrics.** The scorecard is leading numbers, the things a team can move in a week. A weekly that stares at the lagging revenue number is mis-built, because no action this week changes it.
- **The output metrics belong to the monthly, quarterly, and annual loops**, where the time-base is long enough for a lagging number to mean something.
- **Every metric carries its leading-or-lagging tag** (see `metrics-and-kpis.md`), and the scorecard pairs each input metric with the output it is supposed to predict, so a drifting input is caught before the lagging output confirms the damage.
- **Stage-grey the not-yet-meaningful metrics.** Revenue is a lagging vanity signal at the found stage; Rule of 40 and the Magic Number do not apply until scale (see `lifecycle.md`). The scorecard greys what does not yet bear weight rather than tracking it for false comfort.

## Cross-cutting discipline 2: single-threaded owners

**Every number and every action in every loop has exactly one accountable owner.** Not a team, not a function, a single named person (a single AR seat). This is the Amazon **single-threaded owner / single-threaded leader** model: one person owns the outcome and has no competing priority on it, because shared ownership is no ownership. It is the EOS **accountability chart** discipline: one name in every seat, one seat accountable for every number. It is the `Goals.md` OKR rule: each key result has one owner who answers for it.

In the cadence this means: each scorecard line names its owner; each OKR and rock names its owner; each issue solved in IDS ends with one owner and one due date; each action in `Log.md` is attributed. When a number is off-track, the review goes to that one owner, not to the room. This is the operating-cadence expression of the skill's standard, **every angle heard, one owner accountable**: the review hears every function on the way in, and resolves to a single accountable name on the way out.

## Cross-cutting discipline 3: catchball goal-setting

OKRs are not handed down and not invented bottom-up; they are set by **catchball** (the Japanese *nemawashi*-adjacent practice in OKR and Hoshin Kanri planning): the objective is "thrown" down from the altitude above, the function "throws back" what it believes is achievable and what it needs, and the goal is settled in that back-and-forth. Top-down alone produces goals nobody owns; bottom-up alone produces goals that do not ladder to the thesis. Catchball produces goals that both ladder up *and* carry real commitment, because the owner had a hand in setting the number.

In the quarterly and annual loops, OKRs are set this way: the chair (or the annual objective) frames the target, the owning chief returns what is committable and what it would take, and the OKR is fixed in the exchange. The catchball is recorded so the next QBR grades against what was actually agreed, not against a number imposed and resented.

## Cross-cutting discipline 4: disagree and commit

A review must be able to make a call when the functions do not agree, without either steamrolling the dissent or stalling forever. The doctrine is **disagree and commit** (Amazon Leadership Principle): air the disagreement fully, name it, and once the single accountable owner makes the call, everyone commits to executing it as if they had agreed, the dissent recorded but the team moving as one. "I disagree and commit" is a legitimate and fast position; it is not "I disagree, so I will quietly under-execute."

This pairs with the skill's existing decision discipline (see `synthesis.md` and `deliberation.md`): the minority view is heard and **recorded by name**, the single decider (RAPID's one D) makes the call, and the venture commits. In the cadence, disagree-and-commit is what lets a weekly resolve an issue or a QBR set an OKR over a live objection without the objection either being suppressed or blocking the loop. The dissent goes into the record (`Log.md` or the memo); the commitment goes into the work.

## The named operating systems, and what each contributes

The cadence is a synthesis, not an adoption of any single system. Each named system contributes a specific, load-bearing piece:

- **OKRs (Doerr / Google / Intel).** The objective-and-key-results spine that connects all four loops: annual objectives at the top, quarterly OKRs laddering up to them, 0.0-to-1.0 grading at the QBR, the committed-vs-aspirational split, and catchball goal-setting. The OKRs live in `Goals.md`; the cadence is the clock that grades and resets them.
- **EOS / Traction (Wickman): the Level 10 Meeting and the scorecard.** The weekly loop's fixed same-agenda meeting ending in IDS, the 5-to-15-number leading scorecard, the quarterly **rocks**, and the **accountability chart** (one name per seat) that backs single-threaded ownership.
- **Amazon: the WBR, the six-pager, controllable input metrics, single-threaded owners, and disagree-and-commit.** The standing weekly metrics review, the written narrative pre-read that replaces slide decks (board and QBR), the lead-vs-lag input-metric doctrine, the one-owner-per-outcome model, and the disagree-and-commit call.
- **V2MOM (Salesforce).** The annual loop's one-document alignment artifact (Vision, Values, Methods, Obstacles, Measures), an alternative or complement to annual OKRs for stating the year's vision and the measures that prove it.

The chair reaches for the piece each loop needs and names it in the brief; the cadence runs the loops, not the brand of any one system.

## Stage-scaled cadence

A pre-revenue idea and a mature company do not run the same clock. Scale the loops to the venture's stage (the full stage model is in `lifecycle.md`); the cadence below is the default, tuned by stage.

- **FOUND (Idea to Seed/MVP).** **Monthly board** (60 to 90 minutes, a one-page update on PMF, runway, and pivots); a **weekly Build-Measure-Learn standup** in place of a full WBR (the scorecard is qualitative: problem-validation interviews, willingness-to-pay, activation, cohort retention, runway); daily founder-led outreach. Suppress the scale metrics (Rule of 40, Magic Number) as not-yet-applicable; revenue is a lagging vanity signal here. The loops are light because process is the enemy of learning velocity at this stage.
- **SCALE (Series A to C).** Board **monthly trending to quarterly**; a weekly **flight-check** WBR (numbers, thresholds, decisions, no storytelling); **quarterly OKRs** with operating-plan recalibration; the monthly financial review becomes real once the books are. The scorecard turns quantitative: CAC payback, NRR, burn multiple, Magic Number, growth rate, gross margin; Rule of 40 becomes the headline above ~$5-10M ARR. This is where the full four-loop stack and single-threaded ownership become load-bearing.
- **MAINTAIN (Established to Mature).** **Quarterly board and quarterly OKRs**; the recurring upkeep loop that keeps `Overview.md`/`Goals.md`/`Log.md` current and detects stale context. The metric set is durability: Rule of 40, FCF and margin, durable NRR, and the H2/H3 pipeline health that reads as the anti-aging gauge. The cadence here guards against death-by-bureaucracy as much as it tracks the numbers; the review explicitly asks whether the core is defended *and* the next S-curve is funded.

In every stage, the loop reads the venture's real context first and writes its result back (see the inputs and outputs per loop above), so the next review is never blind, and the skill alone writes, behind the write-gate.
