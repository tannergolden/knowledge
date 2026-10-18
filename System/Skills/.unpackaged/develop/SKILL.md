---
name: develop
description: Builds, updates, and self-improves skills and the agents and teams they compose. Use this whenever the user wants to build a skill, create an agent, make a team, turn a workflow into a skill, fix or improve a skill that misbehaved, or package one to share, even when they never say the word skill. Authors single-file agents into the shared Agents library, composes a team roster, writes the skill, and gates it with a deterministic validator and an independent reviewer.
license: proprietary
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, Task
metadata:
  team: Development
  version: "03.06.02"
  id: "sy-skill-develop-spec"
  author: "Tanner Golden"
  status: "active"
---

# 🏭 Develop - the skill and agent factory

Develop builds skills, the single-file agents they use, and the team rosters that group those agents. It is the one skill that creates other skills, and it improves them and itself after a mistake. It is lean by design: it ships the parts the evidence justifies and grows the rest by demand.

> Operating doctrine lives in `references/`. Read `references/` before a build.

## Modes

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Create** (default) | "build a skill", "create an agent", "make a team" | The full pipeline below. |
| **Update** | "improve this skill", "/develop update PATH" | A scoped change to an existing skill or agent, then the gate. |
| **Recursive** | "the skill made a mistake", "fix what it got wrong", "learn from this" | Self-improvement: a blameless postmortem to a minimal fix, applied on approval, verified independently, frozen as a regression case. Works on any skill, including develop itself. |
| **Publish** | "package this", "get this ready to share" | Vendor the referenced agents into the skill and build the distributable artifact. |

## The architecture it serves

- **Agents are single files** in `<agent-home>/<team>/<role>.md`, grouped into folders named for the real professional team that is the agent's home (the standard: `references/agent-standard.md`, the layout: `references/architecture.md`). One capability each; the `description` is the routing key; the `name` is unique across the library.
- **A team is its folder.** Each team folder carries a namesake roster (`<agent-home>/<team>/<team>.md`) that lists member agents by name and marks the star lead. A team owns no agents elsewhere; another team reuses one by naming it in its own roster.
- **Skills are folders** in `Skills/.unpackaged/<skill>/`. A skill that dispatches a standing team names it in `metadata.team`, and the validator rejects a `metadata.team` that does not resolve to a staffed roster; develop names the Development team, the BRAIN's engineering team (`Inbox/Faculties/Development/`). A skill carries no `agents/` folder locally; agents are referenced from the shared library and vendored in only at Publish.
- **Reference locally, vendor on export.** Day to day a skill references its team's agents by name; only Publish copies them into the package so a shipped skill is self-contained.

## Create pipeline

1. **Requirements** (interactive, inline): develop runs this itself; mine the request, ask only the gaps, lock a requirements note in the run workspace.
2. **Research** (mandatory): never author from memory. Use the `research` skill, depth-scaled. For a team skill, name the real-world team it mirrors.
3. **Reuse-first design**: search the agent catalog by capability (each agent's `description`). For each role, decide reuse, extend, or create. Reuse is advisory: take a clean fit, otherwise author the right agent in its home team folder. Place each new agent in the real professional team that owns its capability, and do not mint a new team folder when an existing one fits. Design the team roster and the skill (its `metadata.team` and its body dispatch-scaling rule).
4. **Build**: author any new agents as single-file specs from `templates/agent.md` into their team folder `<agent-home>/<team>/`; write or update the team's namesake roster from `templates/team.md` at `<agent-home>/<team>/<team>.md`; write the skill from `templates/skill/` into `Skills/.unpackaged/<name>/` with the full mandatory structure (below). After writing or changing any agent or roster, regenerate the derived index with `brain.command agents catalog`.
5. **Gate** (both, in parallel, both must pass): the deterministic validator (`brain.command skill validate` for a skill, and `brain.command agents validate` for the agents, rosters, and the federated library, both shared across all skills and run against the live BRAIN), and the Development team's fresh-context independent reviewers, the QA Engineer and the Application Security Engineer, who never touch the build (the QA Engineer runs the validator and tests via Bash; neither holds Write) and never review their own work. Fix loop resumes the builder on cited issues only.
6. **Trigger check + test-drive** (tiered): every build gets a light trigger check on the description, against the skill's own should-trigger and near-miss set (`assets/trigger-evals.json`; develop's own set is the worked example). Activation is proven by observing a `Skill` tool-use event in a real run, never by reading the description, so the observation is a `brain.command` or harness concern. Reserve the full smoke test and the with-skill-versus-baseline test-drive for the Publish or complex tier.
7. **Package** at Publish: vendor the referenced agents into the skill's `agents/` and build the artifact.

## How develop runs: it dispatches the Development

Develop builds with the Development team, the BRAIN's standing engineering team (`Inbox/Faculties/Development/`), named in its `metadata.team`. When it orchestrates, develop embodies the Development team's ★ Engineering Lead (Maxwell), the same way the research skill embodies its lead. Develop runs the interactive requirements and the research itself, then dispatches the Development team's roles for the build, each briefed from scratch per `references/orchestration.md` with the skill-specific objective: the **Software Architect** designs the skill or agent, the **Full-Stack Engineer** writes the files, and the **QA Engineer** and **Application Security Engineer** verify it independently in a fresh context. The deterministic validator (`brain.command`) is a script, not an agent. The premium seat is that independent verification: a builder cannot honestly review its own work, so the reviewers arrive fresh, never "now check your work." The one rule that never bends, which the Development team's own doctrine also enforces, is that the reviewer is a fresh context, never the builder grading itself.

## Dispatch scaling

Scale the Development team to the build. A single-agent or roster edit runs the Full-Stack Engineer plus the validator, adding the QA Engineer for anything non-trivial. A full skill build runs requirements (interactive, with develop), then the Software Architect, then the Full-Stack Engineer, then the QA Engineer and Application Security Engineer and the validator in parallel, then a builder fix loop on cited issues only. The fresh-context reviewers are the premium seats; keep them whenever the result will be used unattended. Recursive mode adds the blameless postmortem, run interactively with develop.

## Self-improvement (Recursive mode)

Develop improves other skills and itself. The loop: capture the failure from the transcript and notes; run a blameless postmortem to the root cause, not the symptom; design the minimal corrective diff; **propose, then apply only on approval**; verify independently (re-run `brain.command skill validate` plus a conformance check against the live BRAIN, a scoped re-audit by a fresh QA Engineer, joined by the Application Security Engineer where the change is security-relevant, and a trigger check if the description changed); and append a frozen case to `assets/regression-cases.jsonl` that every future self-edit must re-pass. Self-correction is trusted only against an oracle (the validator, a test, a golden example), never on the model's own say-so, and the no-self-grading rule holds even when develop edits develop.

## Mandatory output structure (every skill develop builds)

```
Skills/.unpackaged/<skill>/
  SKILL.md          frontmatter (name, description, license, allowed-tools, metadata) + body; authored from `templates/skill/t-SKILL.md` and renamed to SKILL.md so the package ships exactly one SKILL.md
  License.txt       the license text
  Changelog.md      BRAIN changelog format, ships at 01.00.00
  <Skill>.md        the namesake doc (capitalized skill name); BRAIN global frontmatter, not the Agent Skills one
  assets/           static files the skill ships
  references/       domain knowledge loaded on demand
  templates/        output scaffolds the skill fills in
```

The `SKILL.md` **body** follows the canonical skeleton in `references/architecture.md` (Modes, the architecture it serves, the pipeline, dispatch scaling, conformance with the live BRAIN, quality bars, boundaries), scaffolded by `templates/skill/t-SKILL.md`. Every skill mirrors it and never reorders the spine.

No `agents/` folder and no `scripts/` folder in the source. Agents are referenced from the shared library and vendored in only at Publish. Scripts are not per-skill: every deterministic helper a skill needs (validation, packaging, catalog generation) lives in `brain.command` and is shared across all skills, invoked as a subcommand (for example `brain.command skill validate`). A script frozen inside one skill would duplicate the engine and drift from the live BRAIN.

Two frontmatter schemas live in a skill, and they do not mix. `SKILL.md` carries the Agent Skills frontmatter (`name`, `description`, `license`, `allowed-tools`, `metadata`). The namesake `<Skill>.md` and `Changelog.md` are BRAIN documentation nodes and carry the BRAIN global frontmatter schema in its canonical two-band order (Instructions Section 8), with `version` because they live under `System/`. `brain.command` checks the namesake against the live schema; build it from `templates/skill/Namesake.md`.

## Conformance with the live BRAIN

The BRAIN changes: its frontmatter schema, tag vocabulary, and rules evolve over time. So develop never freezes a copy of a BRAIN rule inside a skill or a reference, because a frozen copy drifts the moment the rule changes. For any BRAIN rule (the frontmatter schema in Instructions Section 8, the tag vocabulary in Article VII, naming, layout), develop reads the live governance or runs `brain.command`, which checks against the current rules. The gate and the self-improvement loop therefore include a conformance pass: `brain.command skill validate` plus `brain.command lint` and `health` against the live BRAIN. Every skill develop builds, and develop itself, is held to the BRAIN as it is now, not as it was when the skill was written. This is also why scripts live in `brain.command`, not in skills: the engine already tracks the live rules, so validation done there is dynamic by construction.

## Quality bars

- **Agents** follow `references/agent-standard.md` (single file, header plus bracketed body, cut decorative persona, comprehensive by coverage).
- **No em dashes** anywhere in a generated skill or agent; the shared validator fails on the character.
- **Tools declared exactly**: every skill lists in its SKILL.md `allowed-tools` the minimal set of tools its workflow actually calls, no more and no less (least privilege); `brain.command skill validate` requires the field.
- **Descriptions** are written to trigger: `references/descriptions.md`.
- **BRAIN-resident skills** honor the standing contract (preflight, read-before-acting, memory write-back offer).

## Boundaries

- Stay within building, updating, and improving skills, agents, and teams. Never rename an existing skill's `name` or its directory; installed users lose it on a rename.
- Apply a self-improvement diff only on explicit approval, and never self-grade a fix; verification is the validator, a fresh auditor, and the regression ledger.
- Inside a BRAIN: back up before editing a vault file, confirm before any delete or structural change, and never create or delete top-level folders. Reference agents from the shared library; vendor them into a skill's `agents/` only at Publish.

## Bootstrap

Develop began as a hand-authored v0, because the first factory cannot build itself (the self-hosting problem). It now dispatches the Development team for design, build, and independent verification. Before its output is trusted, it is checked against the golden set in `assets/golden-set.md` with the human as fresh reviewer. From here, develop builds the other skills and rebuilds later versions of itself, each gated by the validator, the Development team's independent reviewers, and the regression ledger.
