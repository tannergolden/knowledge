# Agent standard - one file per agent

The settled standard for an agent spec. Template: `templates/agent.md`. The validator enforces the header and the core sections.

## Header (YAML)

An agent file is a full BRAIN document with the File Role `type: agent` (Constitution Article VII). It carries the standard frontmatter schema (Instructions Section 8.1: `title` through `id`, no `version` since agents are content, not core files), the `folder` tag of its home, and `tags: [<folder>, agent]`. Only two fields are agent-specific: `name` (in the visible band, directly under `title`) and `tools` (also in the visible band, just above `created`/`updated`).

- `title` - the role; equals the file name, in Title Case with spaces (for example `Chief Executive Officer`, the file `Chief Executive Officer.md`); unique across the whole library (both homes). A team **lead** carries a `★ ` prefix on its file name and `title` (`★ Chief Executive Officer.md`), which marks the lead in the file tree and the catalog.
- `name` - the agent's spoken name, a unique American first name, the addressing handle ("Hey Michael"), placed directly under `title`. Globally unique across both homes. The role (`title`) and the spoken name (`name`) are two separate uniqueness axes; the library validator enforces both.
- `description` - the routing key, which doubles as the BRAIN `description`. Write it as "Dispatch this agent when ..." so an orchestrator can route from this line alone.
- `tools` - the agent's tool allowance, comma-separated; placed just above `created`/`updated` so the dates stay the last visible properties. Delete to inherit.

## Core body, in order (all required)

0. **Identity** - the very top bracket. A tight card, not a biography: `Name` (the spoken American first name), `Persona` (one line, the professional character, no competence or expertise claim), `Voice` (one line, how it sounds), and a `Global rules` pointer to `Agent Resources (AR).md` (where the owner-addressing rule and other workforce-wide conventions live, stated once rather than repeated per agent). This is the talk-to-them-directly layer; it shapes voice and disposition only; it never restates Method and never claims expertise.
1. **Role & Objective** - top bracket. Who it is, the one job, the success test, the isolated-subagent framing.
2. **Inputs** - what it reads every run; what is conditional; what to assume; what to flag and stop on.
3. **Method** - numbered steps, each with its decision rule. Decision criteria hardest-first.
4. **Output contract** - the exact artifact shape. Reason first, emit the formatted result last.
5. **Examples** - the one load-bearing hard case, input to output.
6. **Boundaries** - scope, the forbidden actions, the write-scope.
7. **Recovery** - missing input, ambiguous case, cannot-complete failure shape.
8. **Non-negotiables** - bottom bracket. 2 to 4 lines restating only the hardest constraints and the one output essential. The deliberate exception to "say each thing once"; recency protects it.

## Composable add-ons (include any whose trigger applies, delete the rest)

- **Voice & Style** - when the agent ships prose a human reads. Example-driven (before to after).
- **Stance** - when the agent holds a deliberate disposition, especially as one of several seats that must diverge. Carry a calibrated 1-to-3 scale and a standing question.
- **Coordination** - when the agent is the team lead. Dispatch order, conflict rule, ship gate.

## Detail discipline

- **Carry an Identity, cut the biography.** Every agent carries the tight Identity block above: a unique American name, a one-line persona, a one-line voice, the addressing-and-voice layer the workforce is built on. It is not a backstory: no invented history, hobbies, or life story. The persona is one line that sharpens disposition and voice, never a paragraph of color, never a competence claim, never a substitute for Method. (Decorative backstory still adds nothing to task quality, Zheng et al., EMNLP 2024; a thin identity for addressing and voice is the deliberate, bounded exception, because the addressing layer never enters the reasoning path.)
- **Comprehensive by coverage, not volume.** Generalizable right-altitude heuristics plus one canonical example beat enumerating every case. State each fact once; cut padding, keep all method.
- **Deepen the decision kernel, not every section.** Where an agent makes a load-bearing judgment, give each Method step its decision rule and state the role's framework once, and give Examples a contrasting decide-versus-escalate pair: those buy decision consistency. Leave Identity, Recovery, and Non-negotiables lean. Govern by instruction count and signal density, not length (a spec past ~150 lines is a smell; over-trimming costs only 1 to 2 points, so cut filler freely but never method). Deepen a section on an observed failure, not on spec: length for its own sake degrades performance (lost-in-the-middle, instruction overload).
- **Bracket the spec.** Most critical framing at the top (Role), hardest reminders at the bottom (Non-negotiables). At spec lengths a single file is not in the lost-in-the-middle zone; the two brackets are the cheap insurance that scales if it grows.
- **No em dashes.** Anywhere. The validator fails on the character.
