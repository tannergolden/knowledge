# Venture health check (the REVIEW-mode maintenance scaffold)

*The upkeep instrument a review run fills before it decides whether a venture is current, correctly staged, fully deliverable, and balanced between too little structure and too much. Four scans, run in order: staleness (is the record current), stage (does the declared stage match the signals), deliverables (what is missing or stale per department), and flexibility-versus-control (is the venture drifting toward death-by-chaos or death-by-bureaucracy). Every finding is one line, one owner, one next step. The chair fills it; the skill writes the result back behind the write-gate (see write-gate.md). This is plain payload, not a filed memo: it scaffolds the run, then its findings land in Log.md and, where they change the record, in Overview.md or Goals.md.*

This scaffold is run during a **review** mode pass (SKILL.md), after the venture-context preflight has read `Overview.md`, `Goals.md`, `Strategy.md`, and recent `Log.md`, and after stage detection (`lifecycle.md`). It does not replace the operating cadence (the weekly business review, the monthly financials, the quarterly OKR grading and QBR); it is the **health check** that runs alongside the cadence to catch the things a cadence meeting glides past: a record that has gone stale, a stage label that has outrun reality, a deliverable that should exist and does not, and the slow drift toward chaos or bureaucracy. The standard is unchanged: **every angle heard, one owner accountable**. Every scan that touches a function convenes that function's chief for the read; every finding resolves to a single accountable owner and a single next step. The skill is the sole writer; nothing here is written by an agent.

Fill the header, then run the four scans in order. A scan that finds nothing still records "clean" with the date, so the next review can see the gap was checked and not skipped.

## Header

- **Venture:** [name; the one venture this run holds, per SKILL.md "one venture per run"]
- **Review date:** [YYYY-MM-DD]
- **Declared stage (from `Overview.md`):** [Idea | Validation | Pre-revenue | Early Revenue | Growth | Scaling | Established | Mature | Plateau | Decline]
- **Detected operating stage:** [FOUND | SCALE | MAINTAIN, from the signals; `lifecycle.md`]
- **Last review:** [YYYY-MM-DD of the prior health check, or "first"]
- **Tier this run:** [quick | standard | deep, from `dispatch.md`; a quick review is the chair plus one or two chiefs, a deep review convenes the relevant chiefs and the verifier]
- **Headline (BLUF):** [one line: is the venture current, correctly staged, deliverable-complete, and balanced, or which of the four is the problem]

## Scan 1 - Staleness (is the record current)

The record is the company's memory between runs. A stale `Overview`, `Goals`, or `Log` means the next run starts blind, which is the failure the whole grounded-in-the-venture doctrine exists to prevent. Read each of the three core files, find its last real update, and judge it against the cadence the stage expects (`lifecycle.md`, `operating-cadence.md`). "Last updated" is the date of the last *substantive* change, not a frontmatter touch.

| File | Last updated | Expected cadence at this stage | Verdict | What is stale |
|---|---|---|---|---|
| `Overview.md` | [date] | [FOUND: as the riskiest assumption changes; SCALE: quarterly; MAINTAIN: quarterly] | [current / stale / contradicts signals] | [the specific field: stage, traction, thesis line, market surface] |
| `Goals.md` | [date] | [FOUND: monthly PMF check; SCALE: quarterly OKRs; MAINTAIN: quarterly OKRs] | [current / stale / ungraded] | [OKRs un-refreshed, prior quarter ungraded, North Star drifted from `Metrics.md`] |
| `Log.md` | [date of last entry] | [every run appends; gaps signal unrecorded work or decisions] | [current / gap of N weeks] | [the period with no entries; any decision made off-record] |

**Staleness checklist:**

- [ ] `Overview.md` reflects the venture as it is **today**, not as it was at the last raise. The stage, the one-line thesis, the traction block, and the thin market surface each match reality.
- [ ] `Goals.md` OKRs are for the **current** cycle; the **prior** cycle was graded 0.0 to 1.0 and the grade is recorded (an ungraded prior cycle is a stale goal, even if the new one is fresh).
- [ ] The **North Star** in `Goals.md` still matches the canonical definition in `Business Intelligence (BI)/Metrics.md`; if they have drifted apart, that is a finding (`Metrics.md` is canonical, `Goals.md` references it).
- [ ] `Log.md` has no unexplained multi-week gap; every consequential decision and every produced deliverable since the last review left a trace.
- [ ] `Strategy.md` thesis still holds, or the gap between thesis and reality is named as a finding for a `strategize` run.

**Findings (one line each):** `[file/field] - [what is stale] - [owner to refresh] - [refresh now (autonomous) | route to strategize | confirm with Founder]`

A staleness finding inside the green lane (an internal `Overview`/`Goals`/`Log` refresh) the skill may write **now**, with the file's last state committed first; record it in `Log.md` (`write-gate.md`). A finding that changes the thesis or the OKR set routes to a `strategize` run rather than being patched here.

## Scan 2 - Stage check (does the declared stage match the signals)

The declared stage string is a claim; the signals are the measurement (`lifecycle.md`, "Stage detection"). Founders round up and labels go stale, so this scan reconciles the two. Read the signals from the venture's real context and decide whether the venture is being **run** at the right stage.

| Signal | Reads from | Value now | Points to | 
|---|---|---|---|
| ARR / revenue | `Finance & Accounting (F&A)/Financials.md`, `Metrics.md` | [value] | [FOUND / SCALE / MAINTAIN] |
| Headcount | `Human Resources (HR)/Hierarchy.md` | [value] | [FOUND <10 / SCALE 10s to low 100s / MAINTAIN ~150+ with divisions] |
| Retention / NRR | `Metrics.md`, `Client Experience (CX)/Clients.md` | [any cohort retention? NRR %?] | [FOUND: any retention at all / SCALE+MAINTAIN: durable NRR] |
| Last round and date | `Financials.md`, `Log.md` | [round, date] | [Seed/none FOUND / A-B-C SCALE / D+ or profitable MAINTAIN; >18mo old = suspect] |
| Motion repeatability | `Strategy.md`, `Sales & Marketing (S&M)`, `Log.md` | [founder-led non-repeatable? documented, instrumented?] | [the seam-breaker: non-repeatable = still FOUND; repeatable = SCALE] |

**Reconciliation:**

- **Declared:** [stage string]  **Detected:** [FOUND / SCALE / MAINTAIN]
- [ ] **Agree.** Proceed and note the agreement with the date.
- [ ] **Disagree.** Trust the **signals** over the label (`lifecycle.md`, reconciliation rule). State the discrepancy plainly. Run the venture at the **detected** stage. Update the `Overview.md` stage with the evidence (autonomous, internal field, its prior state committed) and append the advance to `Log.md`. A review run that finds a venture has outgrown its label is the moment to **advance the stage on the record**.
- [ ] **Thin or contradictory signals on a consequential gap.** Do not guess silently. Ask **one** framing question (SKILL.md, 1 to 3 framing questions when underspecified) before running the wrong playbook.

**Why the stage matters here:** the wrong stage runs the wrong everything. Scan 3's deliverable expectations, the metrics that count as load-bearing, the cadence that defines "stale" in Scan 1, and the chaos-versus-bureaucracy axis in Scan 4 are all keyed to the operating stage. Get this scan right first; the other three inherit it.

**Stage finding:** `[declared vs detected] - [the evidence] - [advance / hold / ask] - [owner: chair]`

## Scan 3 - Missing or stale deliverable list (per department)

Each AR department owns a venture file and a small set of standing deliverables that **should** exist by a given stage (`department-deliverable-catalog.md`, `write-gate.md` producer-to-file map). This scan walks the departments the stage makes load-bearing, checks the owning file for the deliverable, and flags it **missing** (should exist at this stage, does not), **stale** (exists, but its definition-of-done no longer holds or its data is out of date), or **present** (current). Convene only the chiefs the stage makes relevant; a FOUND venture does not get a Risk-committee deliverable scan, and a board of eleven on a three-function venture is wasted tokens and false weight (`lenses.md`).

**Read the owning file, judge against the stage's expected deliverable, record the verdict.** Expected-by-stage is the discipline: a 3-statement model is **expected** at SCALE and **premature** at early FOUND; an SOP written before there is a repeatable motion is premature process, itself a finding (`lifecycle.md`). Grey out, do not flag, a deliverable that is correctly not-yet-applicable for the stage.

| Department | Owning venture file | Expected-by-stage deliverable | Status | Owner (chief) | Action |
|---|---|---|---|---|---|
| Administration (exec office) | `Administration/Strategy.md`, decisions record | thesis + OKR ladder; governance/decision record current | [present/stale/missing] | CEO Jonathan / CorpSec Margaret | [route to strategize / refresh / clean] |
| Finance & Accounting (F&A) | `Finance & Accounting (F&A)/Financials.md` | FOUND: runway + cash; SCALE+: 3-statement model, budget, unit economics, board package | [present/stale/missing] | CFO Eleanor | [produce via operate / refresh] |
| Sales & Marketing (S&M) | `Sales & Marketing (S&M)/Brand.md`, `Products.md` | positioning + GTM; SCALE: demand plan, sales playbook, pipeline + forecast | [present/stale/missing] | CRO Xavier | [produce / refresh] |
| Client Experience (CX) | `Client Experience (CX)/Clients.md` | FOUND: activation + cohort retention read; SCALE: success plan, SLAs, QBR deck | [present/stale/missing] | Chief Customer Officer Caleb | [produce / refresh] |
| Operations & Logistics (O&L) | `Operations & Logistics (O&L)/Operations.md` | SCALE: SOPs/runbooks, ops KPI dashboard, vendor scorecards, capacity plan | [present/stale/missing] | Head of Operations Hannah | [produce / refresh] |
| Human Resources (HR) | `Human Resources (HR)/Hierarchy.md` | SCALE: org design, comp bands, hiring plan, performance system | [present/stale/missing] | CHRO Vivian | [produce / refresh] |
| Legal & Compliance (L&C) | `Legal & Compliance (L&C)/Compliance.md` | entity pack + key contracts tracker; SCALE+: compliance program, governance calendar | [present/stale/missing] | General Counsel Robert | [produce / refresh] |
| Research & Development (R&D) | `Research & Development (R&D)/Products.md`, `Roadmap.md` | FOUND: MVP + experiment log; SCALE: roadmap, PRD, release plan | [present/stale/missing] | Chief Product Officer Oliver | [produce / refresh] |
| Business Intelligence (BI) | `Business Intelligence (BI)/Metrics.md` | governed metric definitions, North Star, the stage's load-bearing KPIs | [present/stale/missing] | Chief Data Officer Nora | [produce / refresh] |
| Information Technology (IT) | `Information Technology (IT)/Stack.md` | reference architecture, security posture; SCALE: SRE runbooks | [present/stale/missing] | Chief Information Officer Samuel | [produce / refresh] |
| Public Relations (PR) | `Public Relations (PR)/Press.md` | comms plan; SCALE+: press kit, crisis plan, IR materials | [present/stale/missing] | Chief Communications Officer Vanessa | [produce / refresh] |
| Quality Assurance (QA) | `Quality Assurance (QA)/Standards.md` | quality standard; the verifier seat for every produced deliverable | [present/stale/missing] | Head of Quality Grace | [produce / refresh] |

**Deliverable rules:**

- [ ] **Missing** means missing **for this stage**, not missing absolutely. Use the stage column in `department-deliverable-catalog.md`; do not flag a MAINTAIN-grade artifact absent from a FOUND venture.
- [ ] **Premature** is also a finding. A deliverable that exists too early (the SOP before the repeatable motion, the divisional org chart at FOUND) is structure ahead of need; it feeds Scan 4.
- [ ] A **stale** deliverable fails its definition-of-done **now**, even if it passed when written (a financial model on six-month-old actuals, a comp band benchmarked to last year, a metric definition that drifted from `Metrics.md`).
- [ ] Each fix is a **separate run**: a missing or stale deliverable routes to an `operate` run (a lead frames a brief, specialists produce, the Head of Quality verifies, the skill writes it behind the gate, `specialist-dispatch.md`, `verification.md`). The health check **names** the gap and its owner; it does not produce the artifact in place.
- [ ] **One owner per finding.** Every missing or stale deliverable resolves to a single accountable chief, never "the team."

**Deliverable findings (one line each):** `[department / file / deliverable] - [missing-for-stage | stale | premature] - [chief owner] - [operate run | refresh | retire]`

## Scan 4 - Flexibility versus control (death-by-chaos or death-by-bureaucracy)

The diagnostic that the other three feed. Every venture sits somewhere on one axis: too little structure (**death-by-chaos**, the FOUND and early-SCALE failure mode) or too much (**death-by-bureaucracy**, the MAINTAIN failure mode). The risk **flips** as the venture matures (`lifecycle.md`): a FOUND venture dies of chaos (no process, no record, founder-in-everything, nothing repeatable), a MAINTAIN venture dies of bureaucracy (process for its own sake, loss of hunger, buying innovation instead of building it). The health check's job is to locate the venture on this axis and flag drift toward the nearer cliff. This is not a call to split the difference; the right amount of structure is **stage-dependent**, and the diagnostic asks whether this venture has the right amount **for its stage**, not the most or the least.

**Which cliff is nearer, by stage:**

- **FOUND** - the cliff is **chaos**. The named transition crises are Greiner's **Leadership crisis** (the founders can no longer run everything by feel) and Adizes **Infant Mortality** (death from running out of cash or commitment before the product works). Watch for: nothing repeatable, no record between runs, the founder personally inside every decision, premature *hiring* into a motion that is not yet repeatable. The opposite risk (premature *process*) is real here too, so chaos is the default cliff but bureaucracy-at-FOUND is the over-correction to watch.
- **SCALE** - the venture crosses **both** crises. Greiner's **Autonomy crisis** (central direction now suffocates the people closest to the work) and **Control crisis** (delegation has spread decisions so wide the center lost coordination), and Adizes' **Founder's Trap** (the company cannot function without the founder personally). This is the balance stage: too little structure and coordination breaks, too much and speed dies. Watch for the founder as the bottleneck and for process installed in a way that kills speed.
- **MAINTAIN** - the cliff is **bureaucracy**. Greiner's **red-tape crisis**; Adizes' aging path Prime into Stability into Aristocracy, run with **active anti-aging pressure**. Watch for the earliest aging signals: loss of hunger, a drift from **building** innovation to **buying** it, chronic R&D underinvestment, and an empty H2/H3 pipeline while H1 scores well. A MAINTAIN venture that is healthy on the core and empty on the next S-curve is **flagged, not congratulated**.

**Diagnostic checklist (mark each toward the nearer cliff):**

Chaos-side signals (too little structure for the stage):

- [ ] No repeatable motion where the stage expects one (SCALE+ with founder-led, non-instrumented selling).
- [ ] No record between runs (Scan 1 found a `Log.md` gap; decisions made off-record).
- [ ] Founder personally inside decisions a chief should own (the Founder's Trap forming).
- [ ] Deliverables the stage expects are missing (Scan 3 missing list is long for the stage).
- [ ] Goals exist but nothing grades or closes them (Scan 1 found ungraded prior cycles).

Bureaucracy-side signals (too much structure for the stage):

- [ ] Process exists ahead of need (Scan 3 flagged premature deliverables: SOPs before a repeatable motion, divisional org charts at FOUND).
- [ ] Cadence meetings produce reports, not decisions (storytelling has crowded out the numbers-and-thresholds discipline; `operating-cadence.md`).
- [ ] Innovation is bought, not built; R&D reinvestment is below the anti-aging gauge (MAINTAIN).
- [ ] H2/H3 pipeline is empty while H1 is healthy (the next S-curve is unfunded; `lifecycle.md` Three-Horizons split).
- [ ] Loss of hunger: the venture is comfortable, defensive, and slow to decide a reversible call.

**Verdict:**

- **Position:** [healthy-for-stage | drifting toward chaos | drifting toward bureaucracy]
- **Nearer cliff:** [chaos | bureaucracy], expected for the [FOUND | SCALE | MAINTAIN] stage
- **The one corrective:** [the single highest-leverage move back toward stage-appropriate balance] - **owner:** [chief] - **route:** [decide run for a structural call | operate run to build the missing structure | strategize run to refund the next S-curve | Founder for an irreversible or major move]

## Write-back (the skill, behind the write-gate)

The health check produces findings; the **skill** persists them, and only inside the lanes `write-gate.md` allows. The chair holds the four scans; the skill alone writes.

- **Autonomous (green), prior state committed first:** refreshing `Overview.md`, `Goals.md`, or `Log.md` (Scan 1 staleness fixes), advancing the `Overview.md` stage with its evidence (Scan 2 reconciliation), and the standing `Log.md` append that records this health check ran, what it found, and what it routed. Commit an existing file's last state before editing it; git history is the backup, a `Log.md` append included.
- **Routed, not written here:** every missing or stale **deliverable** (Scan 3) becomes its own `operate` run, every thesis or OKR drift becomes a `strategize` run, and every structural balance call (Scan 4) becomes a `decide` run. The health check names the gap, the owner, and the route; it does not produce the artifact in place. A producer never verifies its own work, and consequential output is verified by the Head of Quality before the skill persists it (`verification.md`).
- **Hard-gated (red), the Founder confirms:** nothing in a health check moves money, sends an external communication, signs a contract, deletes a file, or changes equity. If a corrective implies one of those, the health check **stages** it and the skill waits for the Founder (`write-gate.md`). A "yes" from the CEO seat is advice, not authorization.

**Standing `Log.md` entry for the run:** `[date] - Health check ([tier]): record [current/refreshed], stage [held/advanced X to Y], [N] deliverable findings routed, balance [healthy/drifting toward chaos|bureaucracy]. Correctives owned by [chiefs].`

## How to read a completed health check

A good health check resolves to four one-line verdicts and a short list of routed findings, each with one owner and one route. It is **current** (Scan 1 clean or refreshed), **correctly staged** (Scan 2 agrees, or advanced the stage on evidence), **deliverable-honest** (Scan 3 names what is missing-for-stage without flagging the not-yet-applicable), and **balanced for its stage** (Scan 4 names the nearer cliff and the one corrective). A health check that finds nothing is a real result, recorded with the date so the next review sees the scan was run and not skipped. A health check that finds everything at once is itself a signal: a venture that is stale **and** mis-staged **and** missing core deliverables **and** drifting toward chaos is usually one root cause (the founder-in-everything bottleneck, an unrecorded pivot, a raise that moved the company past its label) showing up in four mirrors. Name the root cause, not just the four reflections, and route the single corrective that addresses it.
