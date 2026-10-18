# Founding checklist - the gated idea-to-launch scaffold for FOUND mode

*The seven-stage, gated checklist a found run works through: validate, MVP, incorporate, equity, GTM, hire, raise. Each stage carries a go/no-go gate that must clear before the next stage opens, and the two irreversible founding clocks (the 83(b) 30-day window and the QSBS 5-year hold) are flagged hard at the top and again at the stage that starts them. This is a working scaffold: copy it into the new venture and fill the brackets. The chair runs the stages in order; the skill writes the results back behind the write-gate (see write-gate.md), and the standing FOUND-stage doctrine that scales the run is in lifecycle.md.*

Stage and rigor for everything below come from lifecycle.md (FOUND, Idea to Seed): protect runway and learning velocity, resist premature process and premature hiring, and run the smallest sufficient roster (often the chair plus the CSO and CFO, the CMO on a first-customer question). The dominant question of the whole stage is one line: **is there real evidence of product-market fit?** Every gate below is a way of asking it again at higher resolution. The chair holds the question, the convened functions form independent views, the Head of Quality (Grace) verifies anything consequential before it lands, and the skill is the sole writer. Every angle heard, one owner accountable.

How to read a gate: a gate is a **go / no-go / pivot** decision, not a checkbox. A `no-go` stops the stage and protects runway; a `pivot` resets the loop with a changed assumption (Build-Measure-Learn); a `go` opens the next stage. Run each gate as a small decide pass (see deliberation.md) and record the call to the venture's `Log.md`. Do not let a stage's tasks open before its predecessor's gate has cleared. Found is sequential by design; the gates are where the venture earns the right to spend the next dollar.

---

## ⚠️ HARD-DEADLINE FLAGS - read first, these clocks do not pause

Two founding actions start irreversible legal clocks. Missing either is expensive and usually uncurable. Both are **red / Founder-gated** actions (changing equity or the cap table, see write-gate.md); the skill drafts and models them, the Founder executes them, and the deadline is logged the day the clock starts.

- [ ] 🚩 **83(b) election - file within 30 DAYS of the stock grant. No extensions, ever.** When a founder receives restricted stock subject to vesting, an 83(b) election tells the IRS to tax the equity at grant (when it is worth ~nothing) rather than as it vests (when it may be worth a great deal). The window is **30 calendar days from the grant date**, it cannot be extended, and a missed election can create a large ordinary-income tax bill on paper gains the founder never received in cash. Action: at incorporation, the moment founder stock is issued, record the **grant date** here → `[grant date]`, the **filing deadline (grant + 30 days)** → `[grant date + 30]`, and confirm each founder mails their election (certified, return receipt). Owner: General Counsel (Robert) drafts; **Founder signs and mails.** This is the single most time-sensitive item in the entire founding process.
- [ ] 🚩 **QSBS - the 5-YEAR holding clock starts at original issuance.** Qualified Small Business Stock (Section 1202) can exempt a large share of the gain from federal tax on a later sale, but only if the stock is **held for at least 5 years** from the date it was originally issued, and only if the company qualified at issuance (a domestic C-corp, gross assets under the cap at and just after issuance, an active qualified trade or business). The clock does not start at sale or at a round; it starts at **original issuance**. Action: record the **issuance date** here → `[issuance date]` and the **5-year maturity date** → `[issuance date + 5 years]`, and confirm the entity is a C-corp at issuance (the LLC path forfeits QSBS, see Incorporate). Owner: CFO (Eleanor) tracks the clock; General Counsel confirms qualification. Flagging it now protects an exit five years out.

> Both clocks are set in the **Incorporate** and **Equity** stages below. They are surfaced here at the top because by the time they are visible in the workflow it is often already too late. If a found run opens with stock already granted, the chair's first move is to check the 83(b) window before anything else.

---

## Stage 1 - VALIDATE (riskiest assumption first)

*Find real, urgent demand before building anything. The product is a hypothesis; the customer is the experiment. Output: a lean canvas, evidence from real conversations, and a single named riskiest assumption that the next stages are built to retire.*

Convene: chair (CEO, wearing the strategy hat) on the thesis, CRO (Xavier, with PMM Felix) on the customer. Roster stays small (lifecycle.md, FOUND).

- [ ] Name the **single riskiest unvalidated assumption** in one sentence → `[the one thing that, if false, kills this]`. Everything downstream tests it.
- [ ] Draft the **lean canvas**: problem, customer segment, unique value proposition, solution, channels, revenue streams, cost structure, key metrics, unfair advantage. File to `Administration/Strategy.md` (the thesis the OKRs will ladder up to).
- [ ] Identify and reach the **first 10 target customers** (named, not personas) → `[list]`. Daily founder-led outreach (lifecycle.md cadence).
- [ ] Run **problem-validation interviews** (aim for 15 to 30): is the problem real, urgent, and currently being paid for in time or money? Record raw notes, not summaries that flatter the idea.
- [ ] Test **willingness to pay** with a real ask (a pre-order, a letter of intent, a paid pilot, a deposit). A "yes I'd use that" is not evidence; a card on file or a signed LOI is.
- [ ] Confirm **founder-market fit**: why this team for this problem, what unfair insight or access they hold → `[the unfair advantage]`.
- [ ] Map the **competitive and substitute landscape** (including "do nothing" and the spreadsheet they use today). Thin is fine here; honest is required.

> **Metrics that count (and the ones that do not).** Count: interviews completed, willingness-to-pay signals, problem-validation rate, early activation among any pilots. Suppress as not-yet-applicable (lifecycle.md, metrics-and-kpis.md): Rule of 40, Magic Number, CAC payback, NRR. Revenue here is a lagging vanity signal; do not report it as a headline.

### 🚦 GATE 1 - Problem/solution evidence

- [ ] **Go:** real, urgent problem confirmed by independent customers, a credible willingness-to-pay signal, and founder-market fit. → opens **MVP**.
- [ ] **Pivot:** the problem is real but the segment, value proposition, or willingness-to-pay is wrong. Reset the canvas, change the assumption, re-run the loop. Record what changed.
- [ ] **No-go:** no urgent problem, or no one will pay. Stop and protect runway. A clean no-go here is the cheapest decision the venture will ever make.

Record the gate call to `Log.md` (decision, rationale, owner, the assumption it retired or exposed).

---

## Stage 2 - MVP (build the smallest thing that produces learning)

*Build the minimum that lets a real customer get real value and lets you measure whether they come back. The goal is learning velocity, not feature completeness. Output: a working MVP in the hands of the first customers, and the first cohort-retention signal.*

Convene: chair + R&D (Oliver / Naomi on the what, Victor on the build) + CMO on early customers. Resist premature process: no SOPs for a thing that does not yet work (lifecycle.md).

- [ ] Write a **one-page MVP definition**: the single core job the MVP does, and the explicit list of what it deliberately does **not** do yet. File to `Research & Development (R&D)/Products.md`.
- [ ] Define the **Build-Measure-Learn loop**: the hypothesis, the metric that confirms or refutes it, and the smallest build that tests it. Weekly BML standup (lifecycle.md cadence).
- [ ] Define **activation** ("first value") precisely → `[the moment a user first gets the core value]`, and instrument it.
- [ ] Ship the MVP to the **first paying or design-partner customers** (the 10 from Stage 1 where possible).
- [ ] Measure **cohort retention** and **meaningful (not vanity) usage**: do they come back, and do they do the core action again without prompting?
- [ ] Capture **qualitative feedback** at the point of use; sort signal (a pattern across customers) from noise (one loud voice).
- [ ] Decide **pivot or persevere** after each loop, on evidence, not attachment.

> Stay reversible and fast: FOUND favors a quick reversible decision over a slow perfect one (lifecycle.md, rigor). A pre-mortem on the one riskiest assumption beats a full dissent battery at this stage.

### 🚦 GATE 2 - First signs of retention (the PMF gate at low resolution)

- [ ] **Go:** an MVP that delivers the core value, a defined activation event customers reach, and an early cohort-retention signal (some cohort comes back). → opens **Incorporate**.
- [ ] **Pivot:** customers activate but do not return, or the core job is wrong. Change the product hypothesis, not the customer's mind. Reset the BML loop.
- [ ] **No-go:** no path to retention after honest iteration. Stop or pivot hard. Building more features is not the fix for a missing why.

Record to `Log.md`.

---

## Stage 3 - INCORPORATE (form the entity, set both founding clocks)

*Stand up the legal entity, and with it the two irreversible clocks. This stage is where the 83(b) window opens and the QSBS clock starts. The default is a Delaware C-corp when a venture-capital track is realistic; the LLC path is the explicit deviation for a lifestyle or cash-flow business and forfeits QSBS. Output: a formed entity, an EIN, a bank account, founding agreements, and both deadline clocks set on the record.*

Convene: chair + General Counsel (Robert / Adrian) + CFO (Eleanor). Entity choice and equity are **red / Founder-gated** (write-gate.md): the team drafts and models, the Founder signs.

- [ ] Decide and record the **entity type** → `[Delaware C-corp | LLC | other]`. **Default: Delaware C-corp** if a VC raise is realistically on the table (clean for priced rounds, SAFEs, options, and QSBS). **LLC** is the explicit deviation for a lifestyle/cash-flow venture and **forfeits QSBS eligibility** (QSBS requires a C-corp at issuance). Owner: General Counsel recommends; **Founder decides.**
- [ ] File the **certificate of incorporation**; adopt **bylaws** and the **initial board consent**. File the entity-formation pack to `Legal & Compliance (L&C)/Compliance.md`.
- [ ] Obtain the **EIN** (federal tax id) → `[EIN]`.
- [ ] Open the **business bank account** (separate from personal funds from day one; commingling pierces the liability shield).
- [ ] Execute **founding agreements**: founders' agreement, IP and invention assignment (every founder assigns all relevant IP to the company), and any cofounder vesting terms. IP assignment is not optional; unassigned founder IP is a fatal diligence flag later.
- [ ] Issue **founder restricted stock** and record the **grant date** → `[grant date]`. **This starts the 83(b) 30-day clock and the QSBS 5-year clock.**
- [ ] 🚩 **Set the 83(b) deadline now:** grant + 30 days → `[grant date + 30]`. Each founder files (certified mail, return receipt). Owner: General Counsel drafts; **Founder signs and mails within 30 days. No extensions.**
- [ ] 🚩 **Set the QSBS clock now:** issuance date → `[issuance date]`; 5-year maturity → `[issuance date + 5 years]`. Confirm C-corp status and qualification at issuance. Owner: CFO tracks.
- [ ] Stand up the **cap table** as a real artifact (model it; do not just point at a location) → `Finance & Accounting (F&A)/Financials.md` or `Administration/`. Modeling the cap table is green; **changing the real cap table is red** (write-gate.md).
- [ ] Record **founding-state baseline** in `Overview.md` (entity, formation date, stage) and `Goals.md` (the first OKR set).

> Verify before it lands: the entity pack and the cap-table model are consequential. Grace verifies them against completion evidence before the skill persists them (verification.md). A producer never verifies its own work.

### 🚦 GATE 3 - Clean cap table and clocks set

- [ ] **Go:** entity formed, EIN and bank account live, IP assigned, founder stock issued, **83(b) filed within 30 days**, QSBS clock recorded, cap table clean. → opens **Equity**.
- [ ] **No-go / fix-first:** any open item, especially a missed or at-risk 83(b) window, before proceeding. A broken cap table or a missed 83(b) compounds with every later round.

Record to `Log.md`; note the gated actions the Founder confirmed.

---

## Stage 4 - EQUITY (split founders, set vesting, size the pool)

*Allocate ownership and align it to future contribution, not just to who showed up first. The equity split is one of the highest-regret decisions a founding team makes; vesting and a clean pool are the guardrails. Output: a founder split, standard vesting, an option pool, and the 409A baseline for option pricing.*

Convene: chair + CFO + General Counsel + CHRO (Vivian) on the option pool. All cap-table changes are **red / Founder-gated** (write-gate.md).

- [ ] Decide the **founder equity split** → `[founder: %]`. Anchor it to expected future contribution, role, and risk taken, not only to the idea or to time served. Document the rationale; an undocumented split is a future dispute.
- [ ] Apply **founder vesting** (standard: 4-year vest, 1-year cliff) so equity is earned over time and a departing founder does not walk with a dead-weight stake. Confirm this is the stock the 83(b) covers.
- [ ] Size the **employee option pool** → `[pool %]` (commonly ~10 to 20% reserved pre-Series-A). Note that investors usually require the pool be set **before** the round, diluting founders, so size it deliberately.
- [ ] Establish the **409A valuation** baseline so option strike prices are defensible.
- [ ] Confirm **83(b) elections are filed** for any restricted stock subject to vesting (re-check the Stage 3 clock; this is the last natural place to catch a miss).
- [ ] Record the equity structure into the **cap-table model**; keep the single canonical cap table as the source of truth.

### 🚦 GATE 4 - Aligned, vesting ownership

- [ ] **Go:** founder split agreed and documented, vesting in place, pool sized, 409A baseline set, 83(b) confirmed filed. → opens **GTM**.
- [ ] **Fix-first:** an unvested split, an undocumented rationale, or any unfiled 83(b). Resolve before adding the first hires or investors, who both make the cap table harder to change.

Record to `Log.md`.

---

## Stage 5 - GTM (founder-led first go-to-market)

*Prove you can repeatedly find and win a customer, by hand, before you try to systematize it. Early GTM is the founder selling, learning the motion, and writing down what works. The goal is a repeatable motion in embryo, not a scaled machine. Output: an ICP, a first positioning and message, an early channel that works, and the first real revenue.*

Convene: chair + CRO (Xavier; Felix on positioning, Derek on channel) + CEO selling. Resist premature scaling: do not pour fuel on a motion that is not yet repeatable (lifecycle.md).

- [ ] Define the **ideal customer profile (ICP)** sharply → `[who, in one line]`. Narrow beats broad at this stage.
- [ ] Write **positioning and core message**: the why-now and the how-we-win, in the customer's words. File to `Sales & Marketing (S&M)/Brand.md`.
- [ ] Run **founder-led sales / outreach**: the founder closes the first deals personally and hears every objection unfiltered.
- [ ] Test **one or two channels** to first signal; kill what does not work fast. Do not build a multi-channel plan before one channel works.
- [ ] Land the **first paying customers** and record real revenue (now a real signal, where Stage 1 it was vanity).
- [ ] Capture the **emerging motion**: what consistently moves a prospect from interest to paid. This is the seed of the future sales playbook, not the playbook itself.

> The seam to watch (lifecycle.md): first dollars from non-repeatable, founder-led selling is still **FOUND**. A documented, repeatable, instrumented motion is the signal the venture is leaving FOUND for SCALE. Do not declare the motion repeatable before the evidence says so.

### 🚦 GATE 5 - A repeatable motion in sight

- [ ] **Go:** an ICP that converts, a message that lands, at least one channel showing signal, and real paying customers. → opens **Hire** (and unlocks the case for **Raise**). → may advance the operating stage toward SCALE on the record (lifecycle.md, stage detection).
- [ ] **Pivot:** customers buy but the wrong ones, or the channel does not repeat. Re-segment the ICP or change the channel before scaling spend.
- [ ] **No-go:** no repeatable path to a won customer. Return to MVP or Validate; do not hire or raise against a motion that does not work.

Record to `Log.md`.

---

## Stage 6 - HIRE (the first hire, only against a real bottleneck)

*Make the first hire only when the founders are the bottleneck on a validated motion, not to do work that is not yet repeatable. Premature hiring burns the scarce resource (runway) on an unproven motion. Output: a first key hire that unlocks the founders' highest-leverage time, with comp that fits the stage.*

Convene: chair + CHRO (Vivian / Gabriel sourcing, Yvonne on comp) + the hiring function's lead. Any offer is a **red / Founder-gated** action (signing/sending a contract, write-gate.md): the team drafts the offer; the Founder sends it.

- [ ] Confirm the **bottleneck is real and named** → `[the specific work the founders can no longer hold]`. Hire to unlock founder leverage, not to offload a task that is not yet repeatable.
- [ ] Write the **role definition and the first 90-day success measure** before opening the search. File the hiring need to `Human Resources (HR)/` and the org context to `Hierarchy.md`.
- [ ] Set **stage-appropriate compensation**: lower cash, meaningful equity, against the option pool sized in Stage 4. Use the comp bands the CHRO sets.
- [ ] Run a **structured, evidence-based hiring process** (consistent questions, a work sample, references). One bad early hire is outsized at this size.
- [ ] Issue the **offer with equity from the pool**, vesting and (if restricted stock) an 83(b) reminder for the new hire. Owner: CHRO drafts; **Founder sends.**
- [ ] Plan **onboarding to first contribution**; the first hire sets the cultural baseline every later hire inherits.

> Stage check (lifecycle.md): hiring a function before its motion is repeatable is premature process and premature hiring at once. Hire behind proven leverage, not ahead of it.

### 🚦 GATE 6 - First leverage hire landed

- [ ] **Go:** a real bottleneck, a defined role and success measure, a stage-fit offer accepted, onboarding planned. → the venture can scale the team behind proven leverage.
- [ ] **No-go / wait:** the bottleneck is not yet real, or the motion is not yet repeatable. Hold the hire; protect runway.

Record to `Log.md`.

---

## Stage 7 - RAISE (only if the model needs venture capital)

*Raise outside capital only if the business genuinely needs it to reach the next milestone and the venture path fits the founders' intent (the LLC / cash-flow path may not raise at all). A raise sells future ownership; do it from a position of demonstrated traction, against a specific use of funds. Output: a clear raise decision, and if go, the round mechanics, the deck, and the milestone the money buys.*

Convene: chair + CFO (Eleanor) + CEO (Jonathan, strategy hat) + General Counsel. The financing itself (terms, SAFEs, the round) is **red / Founder-gated** and trips the equity/cap-table gate; several items also touch the QSBS clock (write-gate.md).

- [ ] Decide **whether to raise at all** → `[raise | bootstrap]`. A capital-efficient or cash-flow business may not need it; raising dilutes ownership and resets expectations to a venture-scale outcome. This is a strategy decision, not a default.
- [ ] If raising, define the **milestone the round buys** → `[the specific milestone, e.g. repeatable motion at X scale]` and the **use of funds**. Investors fund a milestone, not a runway.
- [ ] Choose the **instrument** → `[SAFE | priced round | note]` and the **target amount and runway** it buys (commonly ~18 to 24 months). Confirm the C-corp structure supports it (SAFEs and priced rounds assume a C-corp; QSBS qualification persists if the C-corp conditions hold).
- [ ] Build the **forward financial model / projections** (3-statement, scenarios) and the **investor narrative / deck**: problem, why-now, traction, model, team, ask. File the model to `Finance & Accounting (F&A)/Financials.md`; drafting is green, but **sending the deck or signing terms is red.**
- [ ] Confirm **diligence readiness**: clean cap table, IP fully assigned, 83(b) filed, corporate records in order. The Stage 3 to 4 hygiene is what makes this stage fast.
- [ ] Note the **cap-table and QSBS impact** of the round before committing; a new issuance starts its own QSBS clock for the new shares.

### 🚦 GATE 7 - Raise decision (go / no-go / bootstrap)

- [ ] **Go (raise):** the business needs capital to hit a specific milestone, traction supports a credible story, diligence is clean. The Founder authorizes the terms (red action). → the venture moves into SCALE with funded runway.
- [ ] **Bootstrap:** the model reaches the next milestone without dilution. A valid, often superior, outcome. Record the choice and why.
- [ ] **No-go (not yet):** traction does not yet support a raise on good terms. Return to GTM, build the proof, raise later from strength.

Record to `Log.md`; any executed financing is a confirmed red action, logged with the Founder's confirmation noted.

---

## Closing the found run

When the gates have cleared and the venture has a working motion (and funded or bootstrapped runway), the venture has left **FOUND**. The chair:

- [ ] **Advances the operating stage** on the record toward SCALE when the signals warrant it (lifecycle.md, stage detection): a documented, repeatable, instrumented motion is the seam-breaker, not the round name. Update `Overview.md` and append to `Log.md` (green, autonomous; back up first).
- [ ] **Confirms both founding clocks are honored**: 83(b) filed within 30 days (closed, not pending), QSBS issuance date and 5-year maturity recorded and tracked by the CFO.
- [ ] **Hands off to strategize** to set the next stage's OKRs against the new motion (the SCALE-stage dominant question becomes: *is the founder the bottleneck, and is each channel actually efficient?*).
- [ ] **Files the founding record**: `Strategy.md` (thesis), the cap-table model, the entity pack, and the decision log of every gate, so the next run is not blind.

The throughline holds across all seven stages: one workforce scaled small for FOUND, every angle heard with one owner accountable, consequential output verified by Grace before it lands, and the skill as the sole writer behind the write-gate. The Founder alone authorizes the red actions, of which founding has the most of any mode: the entity, the equity, the offers, and the round. See write-gate.md for the autonomous-versus-gated line, verification.md for the verify-before-write discipline, lifecycle.md for the FOUND-stage doctrine, and deliberation.md for how to run each gate as a decision.
