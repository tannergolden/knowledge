<!--
title: "Skills - Folder Information"
description: "The System/Skills/ folder: the .skill archives for the Claude app, built from the vault's skills in .agents/skills/, where the agent apps read them, with a copy in .claude/skills/ for Claude Code. A faculty keeps its team in its own agents/ folder."
type: "index"
keywords: ["skills folder", "skill sources", "skill packaging", "agents folder", "metadata.team", "skill artifacts", "claude code copy", "hand-over"]
-->

# 🛠️ Skills - the consumers

Each skill is a folder with a `SKILL.md` entrypoint. It names the team it dispatches in `metadata.team`, and a faculty keeps that team in its own `agents/` folder. Skills are authored by `develop`, the universal skill, which comes from tannergolden/intelligence with its home kit, so the vault keeps no copy of it.

## Where a skill lives

- **The source** is `.agents/skills/<skill>/`, a hidden folder at the vault root, where Codex, Copilot, Cursor, Gemini and Antigravity read a repository's skills. It is what `develop` edits, and it is not walked as notes.
- **The Claude Code copy** is `.claude/skills/<skill>/`, because Claude Code reads nothing under `.agents/`. `.github/scripts/update-vault.py` draws it byte for byte, and CI fails when it differs from the source; never edit it by hand.
- **The Claude app archive** is `<skill>.skill`, here beside this note, built from the source with its team, the same bytes every time; upload one in the Claude app to use it there. Each archive is the graph node linked here as a sibling file: currently [[research.skill]], [[editorial.skill]], [[visualize.skill]], [[discover.skill]], [[identify.skill]], [[board.skill]], and [[finance.skill]].

## Per-skill folder (the mandatory structure)

Every skill carries exactly these files and folders, `agents/` only when it keeps its own team:

```bash
.agents/skills/<skill-name>/
├── SKILL.md          # entrypoint: frontmatter + workflow; metadata.team names the team
├── License.txt       # the license text
├── Changelog.md      # the skill's version history; its Current Version matches SKILL.md metadata.version
├── <Skill-Name>.md   # the namesake doc
├── agents/           # a faculty's own team: its roster and one spec per agent
├── assets/           # static files the skill ships
├── references/       # domain knowledge loaded on demand
└── templates/        # output scaffolds the skill fills in
```

No `scripts/` folder. Every deterministic helper a skill needs (validation, packaging, the agent catalog) lives once in `.github/scripts/` and serves every skill: `check-skills.py` validates each skill and `update-vault.py` draws the copy and builds the archives. Keeping them there means one implementation, and because they read the live vault, a rule change in the vault is picked up without editing any skill.

Every skill also meets the reader of tannergolden/intelligence's home kit, which carries the five faculties to every repository: only the frontmatter keys the Agent Skills format defines, each on one line, with `metadata` as a one-line map; a quoted value wherever YAML would misread it; a description that says "Use when"; read-only `allowed-tools`; paths written with forward slashes; files at most one folder below `SKILL.md`; and no en or em dash. `check-skills.py` holds all of it.

## How a skill names its team

- `SKILL.md` frontmatter carries `metadata.team: <team-name>`. A faculty (`research`, `discover`, `editorial`, `visualize`, `finance`) keeps that team in its own `agents/`: the roster is the one note there named for the team, and the specs beside it are the members. `board` and `identify` name a `Ventures/Agent Resources (AR)/` department instead and keep no `agents/`; their archives vendor the department in when they are built. `check-skills.py` rejects a `metadata.team` that does not resolve to a staffed roster, and an `agents/` that holds any team but the one the skill names.
- The SKILL.md BODY carries the dispatch-scaling rule: which members of the team run at which task complexity. The body is the real behavior; the annotation is documentation.
- Agents are selected and invoked by their `description`; a brief names the spec to read, `<skill>/agents/<Role>.md`, by the absolute path of the skill's folder.

## Where a faculty runs

A faculty runs from any copy: this vault's, a home install from tannergolden/intelligence, or another vault's. Each opens with the same rule: in a BRAIN vault, the vault's own copy runs, so a home copy that finds itself here reads `.agents/skills/<skill>/SKILL.md` and follows it instead; anywhere else, it skips the vault's steps and returns its work in chat. A vault's copy and its layout always arrive together, from the same release of this template. `check-skills.py` holds every faculty to the rule word for word, because the home kit refuses a faculty without it, and tannergolden/intelligence's loader probe proves each app follows it.

To keep a skill of your own, change it in `.agents/skills/` and add three lines under "Your rules" in `.github/template-sync`, so that Template Sync leaves the skill, its copy and its archive alone: `!/.agents/skills/<skill>/**`, `!/.claude/skills/<skill>/**` and `!/System/Skills/<skill>.skill`.

## How develop works here

`develop` is universal: it is installed with the home kit, not kept here, and its own Development team ships inside it. In this vault it follows the vault's rules over its own defaults. It writes each skill into `.agents/skills/` from the develop skill's `templates/`, in the mandatory structure above; puts a faculty's agents in that skill's `agents/` and a venture role in its `Ventures/Agent Resources (AR)/` department; writes or updates the team's roster and marks its lead with a star; gates every build with `.github/scripts/check-skills.py` and `check-agents.py`; and leaves the copy and the archives to `update-vault.py`.
