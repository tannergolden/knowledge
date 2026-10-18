# Validation - the two-gate quality model

Every build passes two gates in parallel, and both must pass. They are complementary: one is objective and never hallucinates a pass; the other judges what rules cannot.

## Gate 1 - the deterministic validator (`brain.command skill validate` and `agents validate`)

Deterministic checks belong in code, never an agent (a model is worse than code at counting lines and checking schema), and they live in `brain.command`, shared across every skill, so the rules enforced are the live BRAIN's and not a copy frozen inside one skill. It checks what is mechanically true or false:

- **Skill**: `SKILL.md` exists at the skill root and is the only `SKILL.md` in the tree (a template manifest must be named `t-SKILL.md`); the manifest frontmatter carries `name`, `description`, `license`, `allowed-tools`, and a `metadata` block; `name` is kebab-case, 64 characters or fewer, equals the directory name, and contains no "claude" or "anthropic"; `description` is 1024 characters or fewer; `metadata.team`, when present, resolves to a staffed roster; the required files (`License.txt`, `Changelog.md`, the `<Skill>.md` namesake) and folders (`assets`, `references`, `templates`) are present, with no `agents/` or `scripts/` folder in source; `metadata.version` equals the Changelog Current Version, the Changelog frontmatter version, and the namesake version (one version, every site); the namesake and Changelog carry the BRAIN frontmatter schema (Instructions Section 8); no em dash anywhere; and the body has a `## Boundaries` section and no `## Bootstrap` (develop-only). It WARNS (does not block) on underscores in the folder name and on wikilinks in skill sources.
- **Agent**: frontmatter (`title`, `name`, `description`); `title` (the role key, Title Case) equals the file name; `name` (the spoken American first name) is present; an **Identity block** is present (name, persona, voice); the file lives in a real team folder; all core sections present (Identity, Role & Objective, Inputs, Method, Output contract, Examples, Boundaries, Recovery, Non-negotiables); no em dash.
- **Team**: frontmatter (`name`, `description`, `members`, `lead`); `lead` appears in `members`; every member resolves to an agent file somewhere in the library; no em dash.
- **Library (federated)**: walks every agent home, validates each agent and roster in each, and confirms both the role key (`title`) and the spoken `name` are unique across the union of all homes (the filesystem guarantees neither once agents are foldered and split across trees). No two agents anywhere share a name or a role.

A validator error blocks the build. Run it first; it is cheap. The check set above is the spec, read from the live BRAIN, and the skill carries no validator of its own. **Status: built.** `brain.command` implements all four check sets in full, including the complete Skill set above. Skills are checked by `skill validate`; agents, teams, and the federated library by `agents validate` (the whole library across all homes), `agents validate <name|all>` (one agent, matched by role key, file stem, or spoken `name` - so `agents validate Ruth` and `agents validate Fact-Checker` resolve to the same file), and `agents catalog` (regenerate the derived `System/Data/agent-catalog.json`). The Identity block and the cross-home name-and-role uniqueness are enforced by the deterministic gate now, not by hand; the QA Engineer and the Application Security Engineer remain Gate 2 for what code cannot judge.

## Gate 2 - the independent reviewers (the QA Engineer and the Application Security Engineer)

The Development team's QA Engineer, joined by the Application Security Engineer where the build is security-relevant: fresh-context reviewers who never touch the build (the QA Engineer runs the validator and tests via Bash; neither holds Write) and review what they did not write, so a reviewer structurally cannot fix-and-rubber-stamp. They judge what code cannot: clarity, completeness, spec conformance, whether the description would actually trigger, whether the method is coherent. An author anchored to its own context declares work ready that a fresh instance flags as flawed, and same-context self-critique can score worse than none. Never "now check your own work"; always a separate invocation. Withhold the builder's notes from them, so they do not inherit the builder's blind spots.

## Tiered heavy tests (not every build)

- **Trigger smoke test** - the ~20-query description test above. Reserve for Publish or the complex tier.
- **Test-drive** - run the built skill against verifiable assertions, with-skill versus baseline, to confirm it actually works, not just that it triggers. Publish or complex tier.

## The fix loop

Validator errors or an auditor NEEDS-FIX verdict resume the builder on the cited issues only. Re-run the validator always; re-audit only the cited items with a fresh reviewer. If the same error survives two rounds, stop and surface a likely requirement-level conflict.
