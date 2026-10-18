# Deliverable dependency chains

*The producing order and handoffs across the workforce: what must exist before what, so a deliverable is never built on a missing input.*

A deliverable rarely stands alone. Build in dependency order, and when a request asks for a downstream artifact whose upstream input is missing, produce or flag the input first. The chains below are the common ones; the owning venture files are in `department-deliverable-catalog.md`.

## Product
Market and customer evidence to MRD (market requirements) to PRD (product spec) to architecture and design to build to release plan to test plan and requirements-traceability matrix. Product cannot spec what discovery has not validated; engineering cannot build what the PRD has not defined.

## Finance
Strategy and OKRs to the operating budget to the monthly close (actuals) to the board deck and the forward model. The model's assumptions trace to the strategy; the board deck reconciles plan against actuals.

## Go-to-market
Positioning and ICP to the GTM plan to the demand-gen campaign and content to sales enablement to the pipeline and forecast. Sales cannot enable what marketing has not positioned.

## Data
Metric definitions (the semantic layer) to the data model and pipelines to the dashboards and the scorecard. A dashboard built before the metric definitions are agreed reports numbers no one trusts.

## People and operations
Org design to the hiring plan and comp bands to onboarding to the SOPs and runbooks. Hiring without the comp bands creates the very inconsistency the bands exist to prevent.

## The rule
Before producing a downstream artifact, confirm its upstream input exists and is current; if not, the lead produces or flags it first (see `specialist-dispatch.md`). The independent verifier (`verification.md`) checks that a deliverable's inputs were real, not assumed.
