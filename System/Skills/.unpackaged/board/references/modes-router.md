# Modes router - the front door

*How to read a request, pick exactly one mode, run the venture-context preflight, and convene the right AR seats. This is the first reference every run reads (`SKILL.md`, phase 0). The router decides nothing on its own; it routes to a mode, and the mode does the work.*

A run is one mode on one venture. The five modes (found, strategize, decide, operate, review) share one workforce, one venture-context preflight, and one write-gate (`write-gate.md`). Routing is two questions answered in order: **is this board's job at all** (or does it belong to a sibling skill), and if so **which mode**. Answer the first with the near-miss negatives below, the second with the signal table. When the request is underspecified (no clear venture, question, options, or criteria where they matter), ask 1 to 3 framing questions before routing, not after.

## Signal phrase to mode

The request's verb is the strongest signal. Map it, then confirm against the "fires on" column before announcing the mode.

| Signal phrase in the request | Mode | Why this mode |
|---|---|---|
| "found a company", "start a venture", "we have an idea for X", "incorporate", "stand up the company" | **found** | Stands up a new venture: scaffold the folder (copy `Ventures/.template/`, rewrite ids and paths), run the gated idea-to-launch checklist, write `Overview.md` / `Goals.md` / `Strategy.md` at the starting stage |
| "set our strategy", "refresh the OKRs", "what is our north star", "plan the quarter", "plan the year", "should we enter market X" | **strategize** | Runs a planning cycle: set or refresh the thesis and the OKRs, pick the strategy framework, write `Strategy.md` and the `Goals.md` the OKRs ladder up to |
| "should I", "which should I choose", "go or no-go", "build vs buy", "make the call on X", "weigh the options and recommend one" | **decide** | The multi-perspective decision engine: independent functional views, structured dissent, one accountable decider, a BLUF memo with the minority view recorded to `Administration/Decisions.md` and `Log.md` |
| "build the financial model", "draft the brand", "write the SOP", "populate Metrics.md", "produce the GTM plan", "run the venture", "execute the plan" | **operate** | Produces a real deliverable: a lead frames a brief, dispatches its specialists, the verifier checks it, the skill writes it into the owning `Ventures/<Venture>/<Dept>/` file behind the write-gate |
| "how is the venture doing", "run the weekly", "run the QBR", "grade the OKRs", "keep it current", "health check", recurring or scheduled upkeep | **review** | Runs the operating cadence (weekly business review, monthly financials, quarterly OKR grading and QBR), health-checks the venture, keeps `Overview` / `Goals` / `Log` current, and advances or flags the lifecycle stage |

Tie-break rule: when two rows fit, the verb wins over the noun. "Should we set a new strategy" is **decide** if it is asking for a yes-or-no on one move, **strategize** if it is asking to actually run the planning cycle and produce the plan; ask one framing question if the line is genuinely unclear. A request that asks to both decide and then produce ("decide whether to rebrand, and if yes draft it") is two runs, sequenced: decide first, then operate on the outcome. One mode and one venture per run; never collapse two modes into one pass.

## The venture-context preflight (runs before every mode)

No mode runs context-blind. Before framing anything, the chair (CEO Jonathan) runs the same preflight on the named venture, so the call or the deliverable is grounded in the real company and not in the request alone.

1. **Resolve the venture.** Identify which `Ventures/<Venture>/` the request targets. If none is named and the request is ambiguous, ask. If the mode is **found** and no venture exists yet, the preflight is deferred: found scaffolds the venture first (copy `Ventures/.template/`, rewrite every `id` and `path` so ids stay globally unique), then proceeds.
2. **Read the venture's spine.** Read `Overview.md`, `Goals.md`, `Strategy.md` (if present), and the recent tail of `Log.md`. These carry the thesis, the live OKRs, and the running record. A decision that contradicts a settled one, or a deliverable that duplicates an existing one, is caught here.
3. **Detect the stage.** Read the declared stage from `Overview.md`, then check it against the real signals (revenue, headcount, retention, last round) per `lifecycle.md`. The detected stage, not just the declared string, sets the convened roster, the rigor, the metrics, and the cadence for the run. A pre-revenue idea and a mature company are not run the same way.
4. **Dedup check.** Search the vault for the question or the deliverable so a settled decision is not re-litigated and existing context is not duplicated.
5. **Conformance read.** Because every mode may end in a vault write, read `Instructions.md` and `Constitution.md` and the namesake of any folder to be written into, and commit an existing file's last state before editing it (git history is the backup). The write itself is the skill's, behind the write-gate; the preflight only makes the run ready to write.

Only after the preflight does the chair frame the exact question, deliverable, or plan and convene the functions the work touches. The preflight is identical across modes; what changes downstream is which seats are convened and whether the run deliberates (decide), produces (operate), plans (strategize, found), or grades (review).

## Routing to the right AR seats

Routing does not stop at the mode; it names the opening seats so the chair convenes the smallest sufficient roster (`dispatch.md` scales the tier on every run; `specialist-dispatch.md` covers how a lead reaches its specialists in operate). The chair (CEO Jonathan) holds every run. Beyond the chair:

- **found** opens with the chair (CEO Jonathan) framing the thesis and the riskiest assumption, General Counsel (Robert) for entity choice and the irreversible gates (83(b) within 30 days, QSBS 5-year clock), and the CFO (Eleanor) for founder equity and runway. The Corporate Secretary (Margaret) composes the governance record. See `founding-playbook.md`.
- **strategize** opens with the chair (CEO Jonathan) picking the framework and framing the options, the CFO (Eleanor) for the financial envelope, and the functional leads the thesis touches. See `strategy-toolkit.md` and `metrics-and-kpis.md`.
- **decide** convenes only the lenses the decision touches (`lenses.md`), each returning an independent written view in parallel, plus one dissent role (devil's advocate or pre-mortem), the Corporate Secretary for the record, and on deep runs the COO (Patricia) for the execution plan. The decider is one seat. See `deliberation.md`, `frameworks.md`, `synthesis.md`, `memo.md`.
- **operate** routes to the one lead who owns the deliverable's department (the venture-file owner: CFO to `Financials.md`, CRO Xavier to `Brand.md`, Head of Operations Hannah to `Operations.md`, CDO Nora to `Metrics.md`, and so on per the department-deliverable catalog). That lead frames a brief and dispatches its specialists; the Head of Quality (Grace) verifies before the skill writes. See `specialist-dispatch.md`, `department-deliverable-catalog.md`, `verification.md`, `write-gate.md`.
- **review** convenes the COO (Patricia) for the operating cadence, the CFO (Eleanor) for financials-versus-plan, the chair (CEO Jonathan) grading the OKRs, and the leads whose metrics moved. See `operating-cadence.md`.

The standard holds in every mode: **every angle heard, one owner accountable.** Every relevant function is heard before the company converges, work is verified before it lands, and the run resolves to a single recommendation or deliverable with one accountable owner. Functions form their views in isolation and no function grades its own input; the chair alone holds the synthesis; and the skill alone writes, behind the write-gate.

## Near-miss negatives (route elsewhere)

Board runs the company; it is not the only skill near the company's work. Route the following away before picking a mode. The test is the verb and the deliverable, not the topic.

- **Pure ideation, divergence, "what are my options" routes to `discover`.** Discover *generates* options; board *decides among them and acts on them*. "Brainstorm ways to grow the audience", "what are my options for monetizing this", "give me ten ideas for the launch" are discover. The moment the request asks to choose among options or to act on one ("which should I choose", "should we do X", "run the venture"), it is board. Found is the boundary case: "we have an idea for X, let's start the company" is board (found) because it asks to *stand up and act*, not to *generate ideas*; pure idea generation with no intent to found stays in discover.
- **Fact-finding, "what is known" routes to `research`.** Research *finds and verifies* what is known; board *uses it to run the company*. "Research the market size for this product", "what is the current state of X", "get me sources on the competitor" are research. Board convenes research (or its BI and R&D chiefs) as an *input* to a mode, but a request whose whole job is the evidence, not a call or a deliverable, is research.
- **Building a skill, an agent, or a team routes to `develop`.** Develop builds the workforce; board runs ventures with the workforce develop built. "Build me a skill that makes decisions", "create a new agent for the sales team", "turn this workflow into a team" are develop. Board never edits the AR roster or authors agents; it convenes them.
- **Writing or polishing a single artifact routes to `editorial`.** Editorial writes and refines one piece of prose; board orchestrates the whole company and may *dispatch* editorial as a producer inside an operate run. "Write up the decision once it is made", "tighten this memo", "proofread the press release" are editorial. The signal is a single self-contained artifact with no functional deliberation or cross-department production behind it.
- **Rendering a chart, diagram, or visual routes to `visualize`.** Visualize renders one graphic; board may dispatch it as a producer within operate, but "make a chart of the revenue", "diagram the org", "render this as a dashboard image" with no analysis to run is visualize, not a board run.

When a near-miss negative fires, say which skill owns it and stop; do not start a board run to be helpful. When the request genuinely spans board and a sibling (decide a call, then have editorial draft the announcement), board runs its mode and *dispatches* the sibling as a producer behind the write-gate, rather than handing the whole request away.

## Routing summary

1. Run the near-miss test first: ideation to discover, fact-finding to research, building a skill or agent to develop, a single artifact to editorial, a chart to visualize. If any fires, route away and stop.
2. If it is board's job, map the request's verb to one mode with the signal table; break ties by verb over noun and by asking one framing question when the line is unclear.
3. Run the venture-context preflight on the named venture (resolve, read the spine, detect the stage, dedup, conformance read); found defers it and scaffolds first.
4. Announce the mode and the tier (a cost decision made with the owner's tokens), convene the smallest sufficient roster, and hand off to the mode's references.

One mode, one venture, one run. Every angle heard, one owner accountable.
