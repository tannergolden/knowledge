# Department deliverable catalog - who produces what, and where it lands

The producing map for **operate** runs. One entry per AR function: the chair convenes the owning lead, the lead frames a brief and dispatches its specialists (`specialist-dispatch.md`), the Head of Quality verifies against completion evidence (`verification.md`), and the skill (the sole writer) persists the result into the named venture file behind the write-gate (`write-gate.md`). Every artifact resolves to one owning file and one accountable lead: **every angle heard, one owner accountable**, in producing form. No agent writes; agents compose and return, the skill persists.

Read this with `lenses.md` (what each function brings on a decide run) and `dispatch.md` (how the tiers scale the roster). The lenses reference is the advisory voice; this catalog is the deliverable surface. The same lead that advises on a decide run owns the file on an operate run.

## How to read an entry

- **Standing assets** are the durable, version-over-time documents the function maintains, not one-off outputs. They are the files an operate run updates rather than re-creates.
- **Recurring outputs** are the real work products, with their trigger and cadence. Each names the artifact, not a vague capability.
- **Owning venture file** is the single `Ventures/<Venture>/<Dept>/` file the artifact lands in. The producer-to-artifact handoff is specified end to end: a deliverable with no owning file is not producible.
- **Definition of Done (DoD)** is the completion bar the Head of Quality checks before the skill writes. A producer never verifies its own work.

Stage scales the catalog. A **found**-stage venture produces the lean, runway-protecting subset (a one-page model, a lean canvas, a founder-led GTM note); a **scale** venture produces the repeatable-motion set (the 3-statement model, the sales playbook, the org design); a **maintain** venture produces the durability set (the board package, the QBR, the anti-aging R&D review). Convene the smallest sufficient producing team for the stage, never the full bench by reflex (`lifecycle.md`, `dispatch.md`).

---

## Administration (Executive office) - CEO Jonathan

The C-suite tier: enterprise direction, cross-department allocation, strategy framing, and the governance record. Owns the venture's strategic core and its decision history. On a decide run this office runs the deliberation; on an operate run it produces the strategy and cadence artifacts the functions ladder up to.

- **Standing assets:** the company thesis and strategy; the decision and governance log; the operating-cadence record.
- **Recurring outputs:**
  - **Strategy / business plan** (CEO Jonathan, with the chair): the thesis, the market and competitor surface, the chosen framework's output, the OKRs the functions ladder to. Trigger: a strategize run or a stage change. Lands in **Administration/Strategy.md**.
  - **Decision record** (Corporate Secretary Margaret composes, the skill writes): the BLUF call, the rationale, the convened functions, the minority view by name, the owner, the success measure. Trigger: every decide run. Lands in **Administration/Decisions.md** (`memo.md`).
  - **Operating cadence and board record** (COO Patricia): the weekly / monthly / quarterly rhythm, the board and QBR pre-reads, tracked follow-through. Trigger: a review run. Lands in **Administration/Cadence.md** (`operating-cadence.md`).
  - **Execution plan** (COO Patricia): the decided call turned into owned, dated next steps across functions. Trigger: a deep decide run or an operate kickoff. Folded into **Administration/Cadence.md** and the venture `Log.md`.
- **DoD, Strategy.md:** thesis stated in one paragraph; a named strategy framework with its output; OKRs that are specific and measurable and ladder to the thesis; the metric definitions referenced to **Metrics.md**, not redefined here.
- **DoD, Decisions.md:** one decision per entry with the call, the rationale, the convened functions, the minority view, the single owner, the success measure, and the reversibility class; nothing material left to memory.

## Finance and Accounting (F&A) - CFO Eleanor

Cash, runway, capital allocation, controls, the books, budgets, forecasts. The function that keeps the venture solvent and tells the truth about the numbers. Specialists: Controller Walter (the books, the close), FP&A Analyst Priya (model, budget, forecast).

- **Standing assets:** the books and current financials; the forward model; the cap table.
- **Recurring outputs:**
  - **3-statement financial model** (FP&A Priya): trailing actuals plus a forward projection with scenarios; unit economics (CAC, LTV, LTV:CAC, payback). Trigger: a planning cycle, a raise, a major spend decision. Lands in **F&A/Financial-Model.md** (distinct from the Financials snapshot).
  - **Annual operating budget** (FP&A Priya): the spend plan the cadence measures against. Lands in **F&A/Financial-Model.md** and is referenced by **Administration/Cadence.md**.
  - **Monthly financial close and reporting package** (Controller Walter): the closed books, the KPI / cash / runway summary, the board financials. Trigger: month-end. Lands in **F&A/Financials.md**.
  - **Cap table** (CFO Eleanor): real ownership by holder and class, the option pool, the dilution view. Trigger: incorporation, a round, an option grant. Lands in **F&A/Cap-Table.md**. Equity changes are hard-gated to the Founder (`write-gate.md`).
- **DoD, Financial-Model.md:** every number traces to a source or a stated assumption (`verification.md`); the three statements tie; scenarios are labeled and their drivers named; runway is computed and stated in months.
- **DoD, Financials.md:** the close reconciles to source and to the model; variance to budget is explained, not just shown; cash and runway are current as of the close date.
- **DoD, Cap-Table.md:** shares by holder and class sum to the fully diluted total; the pool is shown; the 83(b) (30-day) and QSBS (5-year) clocks are flagged where they apply.

## Legal and Compliance (L&C) - General Counsel Robert

Contracts, IP, entity, regulatory risk, the compliance program. The function that keeps the venture permissible. Specialists: Commercial Counsel Adrian (drafting, review, negotiation), Compliance Officer Lillian (the program, filings, monitoring).

- **Standing assets:** the compliance program and governance calendar; the contract and obligation register; the entity and IP record.
- **Recurring outputs:**
  - **Contract draft and review** (Commercial Counsel Adrian): MSA / SOW / NDA drafts and redlines with the obligation summary. Trigger: a deal, a vendor, a hire. Composed into **L&C/Compliance.md**; signing or sending is hard-gated to the Founder.
  - **Entity-formation pack** (GC Robert): certificate of incorporation, bylaws, board consents, the founder agreements. Trigger: a found run. Lands in **L&C/Compliance.md**; the 83(b) and QSBS flags hand off to F&A.
  - **Compliance program and policy set** (Compliance Officer Lillian): privacy policy, ToS, DPA, the regulatory-filing calendar. Trigger: a regulated surface, a new market. Lands in **L&C/Compliance.md**.
  - **IP filings and assignment** (GC Robert): trademark and patent filings, assignment-of-invention agreements. Lands in **L&C/Compliance.md**.
- **DoD, Compliance.md:** each obligation has an owner and a date; each policy names the regulation it satisfies; nothing asserts a legal conclusion as settled without the caveat that outside counsel confirms execution; gated actions (sign, file, send) are flagged for Founder confirmation, never taken autonomously.

## Marketing (S&M surface) - produced from Sales and Revenue (S&R), CRO Xavier

Demand, brand, positioning. The function that wins the market's attention and intent. Marketing is produced from **Sales and Revenue (S&R)**: Product Marketing Manager Felix (positioning, messaging, launch) and Demand Generation Manager Derek (pipeline across channels, plus the lifecycle motion) produce under CRO Xavier, and the brand-voice consistency gate sits with PR (Chief Communications Officer Vanessa). Deliverables continue to land in the venture's **Sales & Marketing (S&M)/** folder (Brand, Products, Services, plus marketing ops).

- **Standing assets:** the brand and positioning system; the product GTM surface; the demand plan.
- **Recurring outputs:**
  - **Positioning and brand guide** (PMM Felix): the positioning statement, the messaging hierarchy, the brand voice and visual system, with brand-voice consistency gated by PR. Trigger: a launch, a rebrand, a new segment. Lands in **S&M/Brand.md**.
  - **GTM plan** (CRO Xavier, PMM Felix): ICP, why-now, how-we-win, launch tiers, the channel mix. Trigger: a launch, a new market. Lands in **S&M/Products.md** (the GTM surface) and the offer detail in **S&M/Services.md**.
  - **Demand-generation and campaign plan** (Demand-gen Derek): the campaign calendar, the content plan, the lifecycle motion, the demand targets. Trigger: a quarter, a launch. Lands in **S&M/Products.md**.
- **DoD, Brand.md:** positioning is one sentence a stranger can repeat; the messaging maps to the ICP's jobs-to-be-done; the brand line is consistent across the voice and visual sections.
- **DoD, Products.md (GTM surface):** the ICP is specific (not "everyone"); the why-now is evidenced; launch tiers have owners and dates; published external assets are gated to the Founder (`write-gate.md`).

## Sales and Revenue (S&R) - CRO Xavier

Pipeline, forecast, the close, RevOps, and the single revenue number across marketing, sales, and Client Experience. The function that turns demand into booked, collected revenue. The marketing seats sit here now: Product Marketing Manager Felix and Demand Generation Manager Derek produce the marketing deliverables under CRO Xavier (the Marketing entry above). S&R deliverables land in distinct **Sales & Marketing (S&M)/** files (Pipeline.md, Revenue.md, Sales-Plan.md). Specialists: Account Executive Brandon (the individual deal to close), Product Marketing Manager Felix (positioning, messaging, launch), Demand Generation Manager Derek (demand and lifecycle).

- **Standing assets:** the pipeline and forecast; the sales plan and quota model; the RevOps definitions.
- **Recurring outputs:**
  - **Sales plan and playbook** (CRO Xavier, AE Brandon): the ICP-to-close motion, the territory / quota view, the RevOps process. Trigger: a scale-stage motion build. Lands in **S&M/Sales-Plan.md**.
  - **Pipeline and forecast** (CRO Xavier, AE Brandon): the open-pipeline view, coverage against target, and the forward bookings forecast. Trigger: a quarter, a review run. Lands in **S&M/Pipeline.md**.
  - **Revenue plan** (CRO Xavier): the single revenue number reconciled across marketing, sales, and Client Experience, with the bookings-to-revenue bridge. Trigger: a planning cycle. Lands in **S&M/Revenue.md**; the numbers reference **Metrics.md**.
- **DoD, Sales-Plan.md:** the close motion has named stages with exit criteria; quota is costed against the forecast; the RevOps process is repeatable, not founder-dependent.
- **DoD, Pipeline.md / Revenue.md:** coverage and forecast trace to named opportunities and stated win rates (`verification.md`); the single revenue number reconciles across marketing, sales, and CX; metrics reference **Metrics.md**.

## Operations and Logistics (O&L) - Head of Operations Hannah

Process, SOPs, cross-department delivery (the PMO), vendor and supply management. The function that turns a good plan into delivered work. Specialists: Process Analyst Wesley (maps and improves processes), Program and Project Manager Tessa (the shared PMO), Vendor Manager Roland (sourcing on total cost of ownership, scorecards, single-source risk).

- **Standing assets:** the SOP and runbook library; the operations KPI view; the vendor register and scorecards.
- **Recurring outputs:**
  - **SOP / runbook** (Process Analyst Wesley): the procedure with a RACI, a flowchart, and the exception paths. Trigger: a process that lives in one head, an audit, a handoff. Lands in **O&L/Operations.md**.
  - **Operations KPI dashboard** (Head of Ops Hannah): cycle time, throughput, SLA attainment. Trigger: a review run. Lands in **O&L/Operations.md**; the numbers reference **Metrics.md**.
  - **Vendor scorecard / sourcing plan** (Vendor Manager Roland): the TCO comparison, the scorecard, the single-source-risk flag. Trigger: a procurement decision, a renewal. Lands in **O&L/Operations.md**; signing or committing spend is gated to the Founder.
  - **Capacity and delivery plan** (PM Tessa): the cross-department program plan with owners and dates. Trigger: a multi-function deliverable. Folded into **O&L/Operations.md** and **Administration/Cadence.md**.
- **DoD, Operations.md:** each SOP has a RACI and named exception handling; each KPI has a definition, a target band, and a current value; vendor choices show the TCO basis, not just price.

## Human Resources (HR) - CHRO Vivian

Hiring, compensation, org design, performance, onboarding. The function that builds and holds the team. CHRO Vivian carries the function directly (people strategy, sourcing and closing, pay bands and total rewards); specialist seats respawn on demand.

- **Standing assets:** the org design and chart; the compensation bands; the hiring plan.
- **Recurring outputs:**
  - **Org design / org chart** (CHRO Vivian): roles, reporting lines, spans, the next-hire sequence. Trigger: a scale-stage reorg, a funding round. Lands in **HR/Hierarchy.md**.
  - **Compensation bands** (CHRO Vivian): benchmarked ranges by level and function, the equity guidelines, the approval workflow. Trigger: a hiring wave, an annual review. Lands in **HR/Hierarchy.md**; an actual offer is gated to the Founder.
  - **Hiring plan** (CHRO Vivian): headcount by quarter, the open requisitions, the JDs, the pipeline. Trigger: a planning cycle. Lands in **HR/Hierarchy.md**.
  - **Performance and onboarding system** (CHRO Vivian): the review cadence and framework, the onboarding checklist. Lands in **HR/Hierarchy.md**.
- **DoD, Hierarchy.md:** every role has one manager and a clear charter; bands are benchmarked to a named source and stated as ranges; the hiring plan is costed against **Financial-Model.md** runway; no real person's compensation or termination is decided here (those escalate to the Founder).

## Information Technology (IT) - CIO Samuel

Internal tooling, reliability, security, the internal platform. The function that runs the systems the venture operates on. Specialists: Platform Engineer Devin (the internal platform, CI/CD, availability, incident response), Security Engineer Marisol (operational security).

- **Standing assets:** the stack and reference architecture; the security program; the reliability runbooks.
- **Recurring outputs:**
  - **Reference architecture and ADRs** (CIO Samuel): the solution architecture and the Architecture Decision Records. Trigger: a system decision, a new build. Lands in **IT/Stack.md**.
  - **Security program** (Security Eng Marisol): the controls, the monitoring posture, the incident runbooks. Trigger: a new surface, a review. Lands in **IT/Stack.md**. The independent-verifier doctrine treats security findings as completion evidence, not opinion.
  - **SRE runbooks / on-call playbooks** (Platform Eng Devin): the procedures that reduce MTTR, the SLIs and SLOs. Lands in **IT/Stack.md**.
  - **Platform / CI-CD reference** (Platform Eng Devin): the internal platform and pipeline design. Lands in **IT/Stack.md**.
- **DoD, Stack.md:** each architecture choice has an ADR with the alternatives considered; SLOs have numbers and an owner; the runbooks are runnable step-by-step, not prose; secrets and credentials are never written into the file.

## Research and Development (R&D) - CPO Oliver

Product roadmap, requirements, prototypes. The function that decides what to build and proves it can be built. Specialists: Product Manager Naomi (vision, roadmap, the what and why), Applied Researcher Victor (validated prototypes, the how).

- **Standing assets:** the product roadmap; the requirement and spec record; the research synthesis.
- **Recurring outputs:**
  - **Product roadmap** (PM Naomi): the vision, the priorities, the timing, the bets by horizon. Trigger: a planning cycle, a launch. Lands in **R&D/Roadmap.md**.
  - **PRD / product spec** (PM Naomi): the requirements that are the engineering contract, with acceptance criteria. Trigger: a build. Lands in **R&D/Roadmap.md**; the GTM surface for the same product lands in **S&M/Products.md**.
  - **User-research synthesis** (Applied Researcher Victor): the evidence behind the requirements, the validated and invalidated assumptions. Trigger: discovery, a pivot decision. Lands in **R&D/Roadmap.md**.
  - **Release plan** (PM Naomi): scope, sequence, the go / no-go gates. Folded into **R&D/Roadmap.md**.
- **DoD, Roadmap.md:** each roadmap item ties to a strategy objective in **Strategy.md** or **Goals.md**; each PRD has acceptance criteria a verifier can check; research claims cite the evidence, and an invalidated assumption is recorded as such, not quietly dropped.

## Business Intelligence (BI) - CDO Nora

Metrics, analytics, data models, evidence. The function that replaces opinion with measurement where measurement exists, and owns the single trusted definition of every metric. Specialists: Data Analyst Aaron (answers business questions), Analytics Engineer Priscilla (tested, trusted data models).

- **Standing assets:** the metric definitions (the semantic layer); the data model; the dashboards.
- **Recurring outputs:**
  - **Governed metric definitions** (Analytics Eng Priscilla): one trusted definition and formula per metric, the North Star, the canonical KPI source for the whole venture. Trigger: any new metric, any drift. Lands in **BI/Metrics.md**, which is the single canonical KPI source; **Goals.md** and **Strategy.md** reference it, never redefine it.
  - **Dashboards and reporting** (Data Analyst Aaron): the live KPI view, the function rows, each number against its benchmark band. Trigger: a review run. Lands in **BI/Metrics.md** and feeds the venture scorecard.
  - **Data model** (Analytics Eng Priscilla): the curated tables and the semantic top layer. Lands in **BI/Metrics.md** as the definition surface.
- **DoD, Metrics.md:** each metric has exactly one definition and formula; the North Star is named and is leading, not a vanity lag; each KPI carries its benchmark band and its leading-or-lagging tag; the stage where each metric first becomes load-bearing is noted (`metrics-and-kpis.md`).

## Quality Assurance (QA) - Head of Quality Grace

Standards, independent verification, defect prevention, the QC system. The function that checks the work before it lands. **Grace is the independent verifier for every operate run**: she checks each consequential deliverable against its completion evidence before the skill persists it, and a producer never verifies its own output (`verification.md`). Specialists: QA Test Engineer Trevor (executes verification and designs the QC system, with Grace).

- **Standing assets:** the quality standards and QMS; the test strategy and plans; the verification record.
- **Recurring outputs:**
  - **Verification report** (Head of Quality Grace): the pass / fail against the named DoD and the completion evidence, the defects found, the recommendation to write or to return. Trigger: every operate deliverable before the write. Recorded in **QA/Standards.md** and gates the skill's write.
  - **Test strategy and plans** (QA Engineer Trevor): the test cases, the requirement traceability matrix. Trigger: a build, a release. Lands in **QA/Standards.md**.
  - **Quality management plan** (QA Engineer Trevor, with Head of Quality Grace): the controlled-document set, the standards the venture holds itself to. Lands in **QA/Standards.md**.
  - **Audit / assessment report** (Head of Quality Grace): findings feeding corrective action. Lands in **QA/Standards.md**.
- **DoD, Standards.md:** each standard is testable; the verification report names the specific evidence checked, not a general thumbs-up; a deliverable that fails is returned to its producer, not written; the verifier's pass is on record before any consequential write.

## Client Experience (CX) - Chief Customer Officer Caleb

Onboarding, customer success, retention, support. The function that turns a sale into a lasting relationship. Specialists: Customer Success Manager Colin (adoption, value, renewal, and onboarding to first value), Support Specialist Darnell (resolution to root cause).

- **Standing assets:** the onboarding and success playbooks; the support SLAs; the customer health and renewal record.
- **Recurring outputs:**
  - **Onboarding playbook** (CSM Colin): the modules, the owners, the time-to-first-value milestones. Trigger: a new motion, a segment. Lands in **CX/Clients.md**.
  - **Customer success plan** (CSM Colin): the success metrics, the renewal and expansion plays, the health scoring. Trigger: a scale-stage retention build. Lands in **CX/Clients.md**.
  - **Support SLAs** (Support Specialist Darnell): the response and resolution targets, the ticket-theme tracking that feeds product. Lands in **CX/Clients.md**.
  - **QBR deck** (Chief Customer Officer Caleb): the recurring customer review. Trigger: quarterly. Composed into **CX/Clients.md** and surfaced through **Administration/Cadence.md**.
- **DoD, Clients.md:** each playbook has owners and a measurable first-value milestone; SLAs have numbers and a tracked attainment rate; retention and renewal metrics reference **Metrics.md**; no customer-facing send goes out autonomously (external comms are gated).

## Public Relations (PR) - Chief Communications Officer Vanessa

Reputation, press, internal and external communications. The function that owns how the venture reads to the outside and the inside. Specialists: Media Relations Manager Camille (earned coverage), Crisis and Issues Communications Manager Nathaniel (the crisis plan).

- **Standing assets:** the communications plan; the press kit and newsroom; the crisis-communication plan.
- **Recurring outputs:**
  - **Communications plan** (CCO Vanessa): the stakeholder map, the channels, the owners, the message calendar. Trigger: a launch, a milestone, a raise. Lands in **PR/Press.md**.
  - **Press kit / newsroom** (Media Relations Camille): releases, boilerplate, fact sheets. Trigger: a launch, an announcement. Lands in **PR/Press.md**; any actual external publication is hard-gated to the Founder.
  - **Crisis-communication plan** (Crisis and Issues Communications Manager Nathaniel, under CCO Vanessa): pre-approved templates, the escalation path, the holding statements. Trigger: a risk surface, a stage change. Lands in **PR/Press.md**.
  - **Internal communications** (CCO Vanessa): employee-facing announcements and change messaging. Composed into **PR/Press.md**.
- **DoD, Press.md:** every external-facing asset carries a clear approval marker and is never sent without Founder confirmation; the crisis plan names who speaks and the escalation trigger; messaging is consistent with **S&M/Brand.md** positioning (PR holds the brand-voice consistency gate).

---

## The producing chain (read with deliverable-dependency-chains.md)

Deliverables have a producing order; a function does not build on a missing input. The common chains:

- **Product:** user research to MRD to PRD (R&D/Roadmap.md) to architecture (IT/Stack.md) to release to test plan and RTM (QA/Standards.md).
- **Finance:** budget to monthly close to board package (F&A/Financial-Model.md to Financials.md to Administration/Cadence.md).
- **Go-to-market:** positioning (S&M/Brand.md, Marketing) to GTM plan to campaign (S&M/Products.md, Services.md, Marketing) to sales plan, pipeline, and forecast (S&M/Sales-Plan.md, Pipeline.md, Revenue.md, Sales & Revenue) to onboarding and success (CX/Clients.md).
- **Measurement:** metric definitions (BI/Metrics.md) to data model to dashboards, which every other function's KPIs reference rather than redefine.
- **Strategy:** thesis and framework (Administration/Strategy.md) to OKRs (Goals.md) that every function's deliverables ladder up to.

## The write rule (read with write-gate.md)

For each artifact above: the lead frames, the specialists produce, the Head of Quality verifies against the DoD, and **the skill writes** the verified artifact into the named owning file, backing up the existing file first and appending a one-line entry to the venture `Log.md`. AR composes and returns; AR never persists. Internal drafts are autonomous; anything irreversible or external (moving money, signing or sending a contract, publishing external comms, deleting a file, changing equity or the cap table) is hard-gated and escalates to the Founder before the write. The owning file is the single home for the artifact: every angle heard in producing it, one lead accountable for it, one writer who lands it.
