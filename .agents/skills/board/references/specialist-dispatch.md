# Specialist dispatch - the produce loop for OPERATE

*How a lead frames a brief, dispatches its specialists (not just itself) to do the work, hands the returned work to the verifier (Grace), and then to the skill, which alone writes it into the venture. Read before any operate run.*

OPERATE is the mode that produces real work product into a venture folder. DECIDE convenes leads as advisors and resolves to a recommendation (`deliberation.md`, `dispatch.md`); OPERATE reaches one tier deeper, to the specialists who actually build the artifact, and lands it. This file is the producing half of the workforce that `dispatch.md` is the deciding half of. The chain is fixed: the chair frames and routes, the **lead frames the brief and dispatches its specialists**, the specialists produce, the **Head of Quality (Grace) verifies**, and the **skill writes** behind the write-gate. No agent in that chain holds Write or Edit. The standard is unchanged: every angle heard, one owner accountable.

## Why the dispatch reaches below the lead tier

Leads orchestrate and never labor (Agent Resources (AR) charter: "leads orchestrate, they do not labor"). A lead carries `Task` and can dispatch; a specialist carries only `Read, Grep, Glob` and does the hands-on work. DECIDE only ever convened leads, because a decision needs judgment, not a built artifact. That is exactly why DECIDE cannot produce: a lead returns advice, not a financial model. The producers are the specialists beneath each lead (the FP&A Analyst, the Controller, the Product Marketing Manager, the Process Analyst, the Brand Strategist). An operate run that stops at the lead tier returns a plan or an opinion and nothing lands. To produce a real deliverable the run must reach the specialist who builds it, and the lead must dispatch that specialist rather than do the work itself. A lead doing the labor is the same failure as a chair grading their own view: the orchestrator collapses into the worker, and the seam where the work gets checked disappears.

Two consequences follow, and both hold on every operate run:

- **The lead frames and dispatches; it does not type the artifact.** The lead's product is a precise brief and, at the end, an approval. The specialist's product is the artifact.
- **No producer verifies its own work.** The specialist who built it does not grade it; Grace does. A producer checking its own output is the generate-and-self-check pattern the AI-operating-system research flags as worse than no check (see `verification.md`).

## The four roles in a produce loop

| Role | Seat | Holds | Produces | Tools it does NOT hold |
|---|---|---|---|---|
| **Chair** | CEO (Jonathan) | the Founder's real question, the venture context, the synthesis | the framed deliverable request and the owner | (orchestrates only) |
| **Lead** | the owning department chief (e.g. CFO Eleanor) | the department's standard and the output contract | the dispatch brief, then the approval | Write, Edit |
| **Specialist(s)** | the producer(s) under the lead (e.g. FP&A Analyst Priya) | the craft | the actual artifact, with completion evidence | Write, Edit, Task |
| **Verifier** | Head of Quality (Grace) | the independent check | a pass or a fail against the completion evidence | Write, Edit |
| **Writer** | the skill | the only Write/Edit in the system | the persisted file, the `Log.md` entry | (is not an agent) |

The skill is the sole writer. Agents compose and return; the skill persists, behind the write-gate (`write-gate.md`). Every reference that once said an agent "files" or "records" a deliverable is wrong: the agent returns content, the skill writes it.

## The produce loop, end to end

This is step 2 and 3 of the universal run shape (SKILL.md) expanded for OPERATE. Route, preflight, and stage detection (step 0) and the chair's frame (step 1) have already happened; the chair has read the venture's `Overview.md`, `Goals.md`, `Strategy.md`, and recent `Log.md`, and detected the stage (`lifecycle.md`).

1. **The chair scopes and routes.** From the framed request, the chair names the exact deliverable, the owning department, the acceptance criteria, and the target venture file, then routes to the one lead who owns it. One deliverable and one owning lead per loop; a request that needs three artifacts is three loops, sequenced on their dependencies (`deliverable-dependency-chains.md`).

2. **The lead frames the brief.** The lead translates the request into a self-contained dispatch brief for its specialists. The brief carries: the artifact and its purpose; the inputs (the venture files, the numbers, the upstream deliverables it depends on); the template or output contract to fill (`department-deliverable-catalog.md`); the acceptance criteria the verifier will check against; the stage-scaled rigor (a Seed model is a driver-based projection, not an audit-grade three-statement build); and the **completion-evidence** the specialist must return with the work (every number traced to a source or a tool, every assumption named). The brief is self-contained: the specialist sees none of this conversation.

3. **The lead dispatches its specialists.** The lead spawns the producer(s). One specialist for a single-craft artifact; several in parallel for a composite one (a board deck pulls the model from the FP&A Analyst and the close numbers from the Controller). Parallel specialists run blind to each other on independent slices, exactly as parallel leads do in DECIDE; the lead, not the specialists, integrates the slices. The lead does not write any part of the artifact itself.

4. **The specialists produce and return.** Each specialist builds its slice to the contract and returns it with completion evidence. It persists nothing; it returns the content and the evidence to its lead.

5. **The lead assembles and approves (first-line check, not the verification).** The lead integrates the slices into the candidate deliverable and checks it against the department standard. This is the producer's own quality bar, not the independent check, and the lead's approval is necessary but not sufficient. The lead names itself as the artifact's accountable owner.

6. **Grace verifies (independent, before anything lands).** The candidate goes to the Head of Quality, who did not build it. Grace checks it against the acceptance criteria and the completion evidence: are the numbers grounded, the assumptions named, the contract met, the claims supported. Grace returns a pass, or a fail with the specific defects. A fail returns to the lead, which re-dispatches the specialist to fix the named defects; it does not return to Grace's desk as someone else's problem. Consequential output does not land unverified (`verification.md`).

7. **The chair assembles and states a view last.** The chair, who alone holds the Founder's real question and the venture context, confirms the verified artifact answers the request, attaches the one accountable owner (the lead), and notes any reservation last so it does not anchor the work.

8. **The skill writes back, behind the write-gate.** The skill, the only writer, persists the verified artifact into the owning `Ventures/<Venture>/<Dept>/` file (with an existing file's last state committed first), appends a dated entry to that venture's `Log.md`, and updates `Goals.md` or the `Overview.md` stage if they changed. Internal drafts and models land autonomously; anything irreversible or external (money, a contract, external comms, a delete, an equity or cap-table change) is hard-gated and escalates to the Founder before the write (`write-gate.md`, `assets/delegation-of-authority.json`).

## Selecting the specialists

Convene the smallest sufficient set of producers, the same discipline as the deciding tier. The lead picks specialists by craft against the artifact, not by seniority or by who is named first:

- **Match the producer to the craft.** A forward projection is the FP&A Analyst (Priya); the booked actuals and the close are the Controller (Walter); positioning and launch messaging is the Product Marketing Manager, not the Demand Generation Manager. The `department-deliverable-catalog.md` names the owning producer for each standing artifact.
- **One specialist unless the artifact is genuinely composite.** Add a second producer only when the artifact has two distinct crafts in it, and run them in parallel and blind, with the lead integrating.
- **Validate the named agent at dispatch.** Each specialist is checked against `System/Data/agent-catalog.json` before the dispatch, so a renamed or retired agent fails loudly, not silently.
- **Stage scales the producer set.** Found-stage artifacts are lighter and use fewer producers; scale and maintain artifacts are heavier and may pull a Treasurer or a Tax Director into a finance deliverable that a Seed model never needs (`lifecycle.md`).

## Worked example: the financial model

The Founder, on a Series A venture, asks: "Build the financial model." The chair has already run the preflight (read `Overview.md`, `Goals.md`, `Strategy.md`, recent `Log.md`) and detected the stage (scale).

1. **Chair scopes and routes.** Deliverable: a forward three-statement model with a 24-month actuals base and a 12-month projection, two scenarios (base and downside), and a unit-economics block (CAC, LTV, payback). Owning department: Finance and Accounting. Owning lead: CFO Eleanor. Target file: `Ventures/<Venture>/Finance & Accounting (F&A)/Financial-Model.md` (the forward 3-statement model; `Financials.md` is reserved for the close/snapshot). Acceptance criteria: every projection line traces to a named driver; the actuals tie to the closed books; the scenarios flex on stated assumptions; the unit economics reconcile to the model. The chair routes the brief to Eleanor.

2. **Eleanor frames the brief.** She splits the work by craft: the actuals base and the historical statements are the Controller's; the forward projection, the scenarios, and the unit economics are the FP&A Analyst's. She writes one brief per producer, each carrying the inputs, the template (the model contract from `department-deliverable-catalog.md`), the acceptance criteria, the scale-stage rigor, and the completion-evidence requirement.

3. **Eleanor dispatches, in parallel and blind.** She dispatches **Controller Walter** to return the 24-month actuals tied to the close, and **FP&A Analyst Priya** to build the 12-month driver-based projection, the base and downside scenarios, and the unit-economics block on top of those actuals. Eleanor writes none of it herself.

4. **The specialists produce and return.** Walter returns the actuals with each line tied to its booked source. Priya returns the projection, scenarios, and unit economics, each line tagged with its driver and assumption, the LTV:CAC and payback shown, and the breakpoints where the estimate fails. Both return completion evidence; neither persists anything.

5. **Eleanor assembles and approves.** She integrates Walter's base and Priya's forward case into one candidate model, checks it against the F&A standard (do the statements articulate, do the scenarios flex correctly, do the unit economics reconcile), fixes the seam, and names herself the accountable owner. Her approval is the first-line check, not the verification.

6. **Grace verifies.** The candidate goes to **Head of Quality Grace**, who did not build it. She checks every number against its completion evidence, confirms the actuals tie to the books, the drivers are named, the scenarios flex on stated assumptions, and the unit economics reconcile. She finds the downside scenario reuses the base-case churn; she fails it on that defect. Eleanor re-dispatches Priya to correct the downside churn; the fixed model returns to Grace, who passes it.

7. **Chair assembles.** The chair confirms the verified model answers the Founder's request, attaches CFO Eleanor as the accountable owner, and notes the one reservation last (the downside leans on a single churn assumption worth revisiting next cycle).

8. **The skill writes.** The model is an internal financial draft, autonomous under the write-gate. The skill makes sure the last state of `Finance & Accounting (F&A)/Financial-Model.md` is committed, writes the verified model into that same `Financial-Model.md` (the forward 3-statement model; `Financials.md` stays reserved for the close/snapshot), appends a dated entry to the venture's `Log.md` ("Financial model built and verified; owner CFO; downside churn flagged for next cycle"), and updates `Goals.md` if a metric definition changed. Had the model recommended moving cash or changing the cap table, that action would have hard-gated to the Founder before any write (`write-gate.md`).

The same loop produces every artifact, only the seats change: the SOP is Operations (lead Hannah, Process Analyst Wesley producing); the brand guide and positioning are Sales & Revenue (lead Xavier, Product Marketing Manager Felix producing, brand-voice consistency checked with PR); the PRD is R&D (lead Oliver, Product Manager producing). In every case the lead frames and dispatches, the specialist produces, Grace verifies, the skill writes, and one lead is the named owner.

## The rules that do not bend

- **Leads orchestrate, specialists produce.** A lead frames the brief and approves; it never types the artifact. Reaching below the lead tier is required, because the producers live there.
- **No producer verifies its own work.** The specialist builds it, Grace checks it, and consequential output does not land unverified. Self-checking is not verification.
- **The skill is the sole writer.** Agents compose and return; the skill persists, behind the write-gate. The irreversible-action gate is never bypassed.
- **Every angle heard, one owner accountable.** Every craft the artifact needs is produced; the result is one deliverable with one accountable lead.
- **Stage-scaled and grounded.** The producer set, the rigor, and the artifact match the venture's stage, and every loop reads the venture's real context first and writes its result back, so the next run is not blind.
- **Smallest sufficient dispatch.** Convene only the specialists the artifact's crafts require; a bigger producing team is not a better one.

See `dispatch.md` for the deciding tier, `department-deliverable-catalog.md` for the owning producer and target file per artifact, `deliverable-dependency-chains.md` for producing order, `verification.md` for Grace's discipline, and `write-gate.md` for what lands autonomously versus what escalates to the Founder.
