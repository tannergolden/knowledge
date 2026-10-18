# Architecture - the model develop builds into

Read this before any build. It is the shape of the system develop produces; everything else serves it.

## Three kinds of thing

- **Agent**: one Markdown file in `<agent-home>/<team>/<role>.md`, living in its home team folder. One capability. Its `description` is the routing key; its `name` is the identity and is unique across the library. The folder groups by real professional team; it is cosmetic to invocation (the model routes by name and description) but is the human-browsable org chart.
- **Team**: a folder named for a real professional team, carrying a namesake roster `<agent-home>/<team>/<team>.md`. The roster lists `members` (agent names) and a `lead`. A team owns no agents elsewhere; it references them, and a roster may name a member whose home is another team folder. The body holds dispatch order and conflict rules.
- **Skill**: a folder in `Skills/.unpackaged/<skill>/`. It names its team in `metadata.team` and scales dispatch in its body. It carries no `agents/` in source.

## Four rules that govern the model

1. **Reference locally, vendor on export.** Day to day, a skill references its team's agents by name and routes by description; nothing is copied. Only at Publish are the referenced agents copied into the skill's `agents/`, making a shipped package self-contained. The library is always present locally, so local copying would only create drift.
2. **Parameterized capability.** An agent spec encodes a broad capability. The skill-specific objective, inputs, and boundaries are injected by the dispatch brief at call time. One agent serves many skills; each call is anchored by its brief. Capability in the spec, objective in the brief.
3. **Rule of Three, repointed.** Every agent is born in the shared library, so there is no skill-local stage to promote from. It survives in three forms: placement (assign each agent a home team at birth, the real profession that owns its capability), consumption (reuse only on a clean capability fit, else author the right one, never force-fit), and team restraint (do not mint a new team folder when an existing one fits). The library grows by demand, not up front.
4. **The lead is marked with a star.** In any roster the lead carries the black-star character before its role name. Never a word-label like (lead), never a different glyph.

## Where develop writes

| Artifact | Path | When |
|----------|------|------|
| New agent | `<agent-home>/<team>/<role>.md` | authored on a clean-fit miss, into its home team folder |
| Team roster | `<agent-home>/<team>/<team>.md` | the team folder's namesake, per team |
| Skill source | `Skills/.unpackaged/<skill>/` | every build |
| Catalog | `System/Data/agent-catalog.json` | derived JSON, refreshed in lockstep with the manifest by save_index, machine-managed |
| Vendored agents | `<skill>/agents/` | only at Publish |

## The canonical SKILL.md skeleton

Every skill's `SKILL.md` body follows one skeleton, so all skills read the same and a reader learns the shape once. `develop`'s own `SKILL.md` is the exemplar; `templates/skill/t-SKILL.md` scaffolds it. The spine order is fixed: a skill may title a slot for its own domain (a `## Modes` table may be `## Tiers`) and may insert domain sections between the pipeline and `## Quality bars`, but it never reorders the spine.

1. `# <emoji> <Name> - <identity>`, then a one-paragraph intro (what it does and its one standard), then `> Operating doctrine lives in references/...` when the skill has references.
2. `## Modes` - the operational table: the axis the skill runs on (modes, tiers). First, so the reader sees how to invoke it before anything else.
3. `## The architecture it serves` - the model the skill operates on; for a team skill, the team it dispatches and the reference-then-vendor rule.
4. `## <Pipeline>` - the main method, named for the skill (a Create pipeline, an intake-to-ship flow).
5. `## Dispatch scaling` - the smallest-sufficient dispatch, scaled to the task.
6. `## Conformance with the live BRAIN` - the preflight and read-before-acting contract, for a BRAIN-resident skill.
7. `## Quality bars` - the non-negotiable quality rules, as a bulleted list.
8. `## Boundaries` - the scope limits and the vs-other-skills rulings.

A skill without a team folds slots 3 and 5 into its method; a skill that never touches the vault drops slot 6. Everything else is present and in order. `develop`'s own `SKILL.md` closes with a `## Bootstrap` origin note; that section is develop-only, the meta skill's self-hosting story, and is not part of the skeleton other skills carry.
