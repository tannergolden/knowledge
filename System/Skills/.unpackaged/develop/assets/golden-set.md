# Golden set - the v0 acceptance gate

v0 of develop is hand-authored, so it has no crew to have built it and no deterministic oracle for the judgment it makes. Before its output is trusted, especially the independent review it gates with (the QA Engineer and, where security-relevant, the Application Security Engineer), it is checked against this golden set with the human as the fresh reviewer. This is the bootstrap's safety net: it breaks the circularity of a crew-less factory authoring its own quality lever.

## How to run the gate

1. Have develop produce each artifact below from a cold prompt.
2. Run `brain.command skill validate` on it. The known-good must pass; each known-bad must fail on the stated check.
3. Read the output yourself as the independent reviewer. Confirm the fresh reviewers it dispatches, the QA Engineer and, where security-relevant, the Application Security Engineer, would actually catch the known-bad cases.
4. Only after all rows pass do you trust develop to build unattended.

## Known-good (must validate clean)

| Artifact | What good looks like |
|----------|---------------------|
| A single-file agent | Header with `name` = file name and a routing `description`; all eight core sections; composable add-ons only where triggered; a Non-negotiables bracket; no em dash. |
| A team roster | `members` and `lead` in frontmatter, lead listed in members, a star on the lead in the body, a dispatch order. |
| A skill | All required files and folders; `name` = directory; `metadata.version` = Changelog top; a description with 4 to 6 concrete trigger phrases and an anti-undertrigger clause. |

## Known-bad (must be caught)

| Defect | Caught by |
|--------|-----------|
| Agent missing its Method section | validator (missing required section) |
| Agent `name` not equal to file name | validator (identity mismatch) |
| Skill `metadata.version` ahead of the Changelog | validator (version mismatch) |
| Roster lead not in the members list | validator (lead not in roster) |
| An em dash anywhere | validator (no-em-dash rule) |
| A passive description ("helps with skills") that would not trigger | QA Engineer (judgment; the validator cannot see this) |
| A decorative persona backstory padding an agent | QA Engineer (spec-conformance; cut persona) |

The last two rows are the point of the human gate: they are exactly what a crew-less v0 might get wrong in the review it relies on, and only a fresh human reviewer can confirm v0 caught them.
