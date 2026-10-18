# OKR cycle - the scaffold for an annual-to-quarterly OKR ladder (strategize mode)

*The fill-in scaffold a strategize run uses to write the venture's OKRs into `Goals.md`: annual objectives at the top, the quarterly OKRs that ladder up to them below, each key result tagged committed or aspirational and carrying a 0.0-to-1.0 grading line. It connects the company thesis in `Strategy.md` to the north-star in `Metrics.md`, and it is the spine the four review loops grade against. Fill only the brackets the venture actually has; never fabricate a target.*

The chair fills this in a **strategize** run, then the skill writes the result into the venture's `Goals.md` behind the write-gate (see `write-gate.md`). The OKRs ladder up: a few annual objectives state what the year is for, and each quarter's OKRs are the slice of that year the venture commits to next. The ladder has to hold in both directions, every quarterly objective serves a named annual objective, and every annual objective is served by at least one live quarterly OKR, or the cycle has a gap. The north-star metric is not redefined here; it is canonical in `Metrics.md` (BI owns it) and referenced, so the OKRs and the scoreboard cannot drift apart. Stage-scale the whole cycle (`lifecycle.md`): a **found** venture writes few OKRs against learning and survival signals and grades loosely; a **scale** venture writes efficiency and repeatability OKRs and grades hard on the numbers; a **maintain** venture splits the ladder across Three Horizons so defending the core does not starve the next S-curve. Keep the standard: **every angle heard, one owner accountable**. Each objective and each key result has exactly one single-threaded owner, OKRs are set by catchball (the chair frames the target, the owning chief returns what is committable; see `operating-cadence.md`), and the skill is the sole writer.

---

## How to read this scaffold

- **Objective** is qualitative and directional: what success looks like, in a sentence a human would be proud to hit. It is not a metric.
- **Key result (KR)** is the measurable proof the objective moved: a number with a start, a target, and a date, so a grade is unambiguous at the QBR. If you cannot grade it 0.0 to 1.0 from data, it is a task, not a KR.
- **Owner** is one named person (one AR chief or specialist), single-threaded. Two owners is no owner.
- **Tag** is `committed` or `aspirational`, defined below. The tag sets the bar the grade is read against.
- **Grade** is the 0.0-to-1.0 line, blank at planning, filled at the QBR. Carry the line from the start so grading is mechanical, not a renegotiation.

---

## Cycle header

- **Venture:** [name]
- **Stage:** [found / scale / maintain, from `Overview.md`, reconciled with the real signals per `lifecycle.md`]
- **Annual period:** [FY2026, or the fiscal year this ladder covers]
- **Quarter being set:** [Q_ 2026]
- **Thesis it serves:** [one line from `Strategy.md`: where we play and how we win this year]
- **North-star metric:** [the single metric, by reference to `Metrics.md`; current value and as-of date] - *canonical in `Metrics.md`, not redefined here*
- **Set by:** [the chair plus the chiefs whose functions own the KRs; catchball recorded]
- **Framework feeding this:** [the strategize output that produced the objectives, e.g. Balanced Scorecard, V2MOM at the annual tier; see `strategy-toolkit.md`]

---

## Committed vs aspirational (tag every KR)

Every key result carries one tag, and the tag is a promise about the bar, not a mood.

- **Committed.** A KR the venture is on the hook to fully deliver. The expected grade is **1.0**; anything less is a miss that needs a reason and usually a recovery plan. Resource it as if failure is not an option, because that is the commitment. Use it sparingly, for the load-bearing few (runway, a shipped launch, a contractual or survival number).
- **Aspirational.** A stretch KR set deliberately beyond comfortable reach. The expected grade is **~0.7** on the Google convention: consistently scoring 1.0 means the bar was set too low (sandbagged), and consistently scoring below 0.3 means it was fantasy. Aspirational OKRs are where real ambition lives; they are graded generously and missing one is information, not failure.

Do not blur the two. A quarter that is all-committed is a venture not reaching; a quarter that is all-aspirational is a venture with nothing it can be held to. Most quarters carry a small committed core and a larger aspirational stretch, and the split itself is a stage decision: **found** leans aspirational against learning, **scale** holds a hard committed efficiency core, **maintain** commits the core defense and aspires on the H2/H3 bets.

---

## The grading line (0.0 to 1.0)

Each KR carries a grading line, written at planning and scored at the QBR (`operating-cadence.md`, Loop 3). The score is the fraction of the target achieved, clamped to [0.0, 1.0], read against the KR's tag.

```
KR grade = clamp( (final - start) / (target - start), 0.0, 1.0 )
```

- **Committed** target the score at **1.0**. A committed KR landing at 0.6 is a real miss, not a near-pass.
- **Aspirational** target the score at **~0.7**. A 0.7 on a true stretch is a good quarter; do not treat it as a 70% failure.
- **The objective's score** is the mean (or a stated weighting) of its KRs, reported alongside a one-line *why* for each, learning not excuse.
- A KR that cannot be scored from data at the QBR was mis-written; fix the KR, do not argue the grade.

Leave the score blank at planning. At the QBR the verifier checks the grades against the evidence before the skill writes them back (a function does not grade its own OKR unchecked; see `verification.md`), and the regraded closing OKRs plus the new quarter's OKRs are written into `Goals.md`.

---

## Annual objectives (the top of the ladder)

The few things the whole year is for. Each quarterly OKR below must ladder up to one of these. Annual objectives are usually qualitative with one or two annual measures (the V2MOM "Measures" line; see `operating-cadence.md`, Loop 4); the quarters carry the gradeable detail.

### Annual Objective A: [the qualitative outcome, in one line]

- **Why this year:** [the thesis link: why this objective is what the year turns on]
- **Annual measure(s):** [the one or two numbers that prove the year delivered it, with target and as-of]
- **Owner (annual):** [the one accountable chief]
- **Three Horizons:** [H1 defend / H2 build / H3 seed - only at scale and maintain, where the ladder is split across horizons per `lifecycle.md`]

### Annual Objective B: [...]

- **Why this year:** [...]
- **Annual measure(s):** [...]
- **Owner (annual):** [...]
- **Three Horizons:** [...]

### Annual Objective C: [...]

- **Why this year:** [...]
- **Annual measure(s):** [...]
- **Owner (annual):** [...]
- **Three Horizons:** [...]

> Keep annual objectives to roughly three to five. More than five is not a strategy, it is a wish list, and the quarters cannot serve them all.

---

## Quarterly OKRs (the gradeable slice)

The quarter being set. Each objective names the annual objective it ladders up to. Each KR carries an owner, a committed-or-aspirational tag, and the start to target to grade line. Set by catchball and recorded so the next QBR grades against what was actually agreed.

### Objective 1: [the qualitative quarterly outcome]

- **Ladders up to:** [Annual Objective A / B / C]
- **Owner (objective):** [one accountable chief]

| # | Key result | Owner | Tag | Start | Target | By | Grade (0.0-1.0) |
|---|------------|-------|-----|-------|--------|----|-----------------|
| KR1 | [measurable result, a number] | [name] | committed / aspirational | [baseline] | [target] | [date] | [blank at planning] |
| KR2 | [...] | [name] | committed / aspirational | [...] | [...] | [...] |  |
| KR3 | [...] | [name] | committed / aspirational | [...] | [...] | [...] |  |

- **Objective grade (at QBR):** [mean or stated weighting of the KR grades]
- **Why (one line each at QBR):** [hit / missed / de-scoped, and the reason, learning not excuse]

### Objective 2: [...]

- **Ladders up to:** [...]
- **Owner (objective):** [...]

| # | Key result | Owner | Tag | Start | Target | By | Grade (0.0-1.0) |
|---|------------|-------|-----|-------|--------|----|-----------------|
| KR1 | [...] | [...] | committed / aspirational | [...] | [...] | [...] |  |
| KR2 | [...] | [...] | committed / aspirational | [...] | [...] | [...] |  |

- **Objective grade (at QBR):** [...]
- **Why:** [...]

### Objective 3: [...]

- **Ladders up to:** [...]
- **Owner (objective):** [...]

| # | Key result | Owner | Tag | Start | Target | By | Grade (0.0-1.0) |
|---|------------|-------|-----|-------|--------|----|-----------------|
| KR1 | [...] | [...] | committed / aspirational | [...] | [...] | [...] |  |
| KR2 | [...] | [...] | committed / aspirational | [...] | [...] | [...] |  |

- **Objective grade (at QBR):** [...]
- **Why:** [...]

> Keep it to roughly three objectives with two to four KRs each. A quarter with eight objectives has no priorities. Over-scoping the quarter is the most common OKR failure, and it shows up as a wall of 0.4 grades the venture explains away.

---

## Ladder check (do not skip)

Before the skill writes this into `Goals.md`, confirm the ladder holds both ways:

- **Up:** every quarterly objective names exactly one annual objective it serves. No orphans.
- **Down:** every annual objective is served by at least one live quarterly OKR this quarter, or it is explicitly parked with a reason. No dead annual objectives.
- **North-star:** at least one KR moves, or directly protects, the north-star metric in `Metrics.md`. If nothing in the quarter touches the north-star, the quarter is busywork, not progress.
- **Owners:** every objective and every KR has exactly one named owner. Zero unowned, zero double-owned.
- **Tags:** every KR is tagged. The committed core is small and survival-or-contract critical; the rest is aspirational. The split matches the stage.
- **Gradeability:** every KR has a start, a target, and a date, so its 0.0-to-1.0 grade will be mechanical at the QBR.

---

## Where this lands and how it is graded

- **Written to:** the venture's `Goals.md` (the OKRs ladder lives there), by the skill, behind the write-gate, backing up the existing file first. The annual objectives are the top of `Goals.md`; the quarterly OKRs are the current cycle.
- **Grounded in:** `Strategy.md` (the thesis the objectives serve) and `Metrics.md` (the canonical north-star and KPIs; the OKRs reference it, never redefine it).
- **Graded by:** the quarterly QBR (`operating-cadence.md`, Loop 3): each KR scored 0.0 to 1.0 against its tag, the verifier checks the grades (`verification.md`), the chair synthesizes, and the regraded closing OKRs plus the next quarter's OKRs are written back to `Goals.md` with a dated `Log.md` entry.
- **Reset by:** catchball at the QBR and annual planning (`operating-cadence.md`, Loop 4, V2MOM at the annual tier). The next ladder is set against the grades this one earned, so honest grading now is what makes the next cycle realistic.

> The OKR ladder is the one artifact every review loop reads: the weekly loop checks rocks against it, the monthly loop checks mid-quarter pace against it, the quarterly loop grades and resets it, the annual loop sets the objectives it ladders up to. Set it once, well, and the cadence runs on it. Set it loosely, and every loop inherits the slack.
