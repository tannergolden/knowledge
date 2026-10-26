---
name: editorial
description: "Orchestrates the BRAIN's standing Editorial team to write, edit, and format any prose, scaled to the piece. Use whenever the user writes or edits text or a prose .md or .txt is created or edited, even when the word editorial is never said: emails, messages, replies, letters, memos, documents, essays, books, posts, notes, and the bodies of Library, Project, and Venture files. Fires on draft this, write this, edit this, rewrite this, reply to this, clean this up, tighten this, make this clearer, polish this, proofread this, format this, reformat these notes, turn these notes into a doc, write a README, and any request to produce or improve text a person will read. The BRAIN's own writing skill, preferred over a generic writer; obeys AGENTS.md. Structurally scoped: does not auto-fire on System, agent, log, template, index, or script files, or on a write by one of the vault's scripts. Not for investigating facts (research), building skills (develop), or a chat-only visual (visualize)."
license: MIT
allowed-tools: Read, Grep, Glob, WebFetch
metadata: { team: Editorial, version: "1.7.0", id: sy-skill-editorial-spec, author: Tanner Golden, status: active }
---

# ✍️ Editorial - the BRAIN's writing skill

Editorial writes, edits, and formats any text the BRAIN needs by dispatching the standing **Editorial team**, whose specs ship with this skill in `agents/`, scaled to the piece. The one standard, the team's, is **clarity**: the reader's understanding comes before the writer's expression. Beneath it sits the defining craft rule, **voice fidelity** from `Profile/`, which never outranks being understood. The skill is a thin orchestration and doctrine layer over its team. The hard rule, shared with `research` and `develop`: the lead holds the brief and synthesizes, and the maker of a draft is never its own reviewer.

**Where it runs.** In a BRAIN vault, whose `AGENTS.md` says it is one, the vault's own copy of this skill runs: if the file you loaded is not that vault's `.agents/skills/editorial/SKILL.md` or `.claude/skills/editorial/SKILL.md`, read the vault's copy and follow it instead, with the files beside it, because a vault's copy matches its layout and its owner may have changed it. Anywhere else, the Founder is your user and the steps that read or write a vault folder do not apply: there is no voice profile in `Profile/`, so take the voice from your user's own writing in the conversation or the repository, deliver in chat or write only where the task points, and never write anything about your user into a repository that is not their private vault (SEC-003).

> Operating doctrine lives in `references/`. Read `references/intake.md` before any external piece (the situation read), `references/tiers-and-dispatch.md` before choosing a tier, `references/slop-rubric.md` before the quality gate, and `references/formatting.md` before any markdown beautification. For hard correspondence, `references/difficult-messages.md` is the per-situation playbook. For exhaustive syntax, `references/markdown-reference.md` covers every markdown element, `references/admonitions.md` covers callouts (GitHub's five, and Obsidian's set for a target that renders it), `references/plain-text.md` covers true plain text (`.txt` and plain-text email or messages), and `references/messaging-formats.md` covers the per-platform chat-dialect matrix.

## Tiers

The operational axis is the tier: how much of the team to spend on the piece. Quick is a solo pass; standard and deep add the gate and the specialist seats.

| Tier | When | Dispatch | Deliverable |
|------|------|----------|-------------|
| **quick** | a message, a short email, a small edit | the lead drafts and self-edits **inline**, single pass, **no team handoff**, against the slop checklist | the text, in chat or in place |
| **standard** | a document, an essay, a substantial email | Writer drafts -> Line Editor gates (clarity, slop, voice, lint) -> the lead ships | the finished piece |
| **deep** | a long document, a book chapter, a high-stakes piece | Developmental Editor (structure) -> Writer / Long-Form / Technical Writer (draft) -> Line Editor (line + copy) -> lead (proof + ship) | the finished piece |

**Announce the tier before dispatching**; it is a cost decision made with the owner's tokens. The quick tier is deliberately lightweight: a two-line reply never spins up the team. Choose the tier from the decision table in `references/tiers-and-dispatch.md`, not by feel; when two rows fit, take the higher. If the request is underspecified (missing reader, purpose, length, or register where one obviously matters), ask 1-3 clarifying questions first (through the structured ask tool when available, otherwise in chat). One piece per run.

## The team it dispatches

`metadata.team: Editorial` names the standing Editorial team, whose roster (`agents/Editorial.md`) and specs ship in this skill's `agents/` folder (lead **Editorial Lead / Edith**). The roster is the lead plus five: **Writer**, **Line Editor**, **Long-Form Writer**, **Technical Writer**, **Developmental Editor**. Agents are routed by their `description`. How the tiers map onto the roster, and how each dispatch is briefed, is in `references/tiers-and-dispatch.md`.

## How a piece is made

Every run is intake, then draft, then a separate gate, then ship.

**Phase 0, intake (every external piece).** Before drafting, the lead runs the **situation read** (the rhetorical checks plus the sentiment read) and writes a short **situation brief** that threads into every dispatch, so whichever agent acts drafts to the real situation rather than improvising it. The method, the tone-calibration rule, the elicitation rule, and the brief spine are in `references/intake.md`; the scaffold is `templates/situation-brief.md`; the hard-message playbook is `references/difficult-messages.md`.

**Destination decides the rules.** Helping the user with something they will **send or use outside the vault** is a **primary** use of editorial, not an afterthought: write me an email, rewrite this, proofread this, reply to this, soften this. A **leaving piece** goes to the **user**, not the vault: it is delivered in chat or to a file they choose, is **not filed into the BRAIN**, and is governed by the **destination's own format** (the vault's conventions in `AGENTS.md` cover only the files kept in the vault), so the vault preflight and the lint exit gate do **not** apply to it. **Clarity and the slop rubric still apply** to everything, vault-bound or not.

**The quality gate (the Line Editor).** Above quick, write and edit are **separate passes by separate agents**: the Writer drafts, then the Line Editor arrives fresh and gates it. This is the proven generate-then-critique split; naked self-critique degrades, so the standard is externalized. The Line Editor critiques against the **slop rubric** in `references/slop-rubric.md`, never a vague "make it better," and **cites the offending span** for every flag. The rubric's single source of truth is standards' [Plain Words](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md#plain-words) list, which **DOC-003** holds agents to, and **DOC-002** (no em dashes): the rubric points at them and never forks them. The critic resists length-bias and lenient scoring: shorter wins when meaning is preserved, and "leave it alone" is a valid verdict. A piece does not ship on an unverified load-bearing claim; the Line Editor flags such claims and the lead verifies them or routes them to the Research team (the Editorial team keeps no fact-checker of its own).

**Editing in place.** When editing an existing file: **make sure its last state is committed** (`AGENTS.md`, Conventions) and **show the diff or a redline before overwriting**. The owner sees the change before it lands. A **no-op verdict is valid and valuable**: declining to edit, because the text already reads clear and true, is a real outcome, not a failure to act. **Preserve the author's length and register** unless asked to change them; tightening is not the same as shrinking, and a casual note does not get formalized on the way through.

## Dispatch scaling

A bigger roster is not a better one. Dispatch the **smallest sufficient** seats: the Writer drafts, the Long-Form / Technical / Developmental seats fire only on their trigger, and every piece that ships above quick passes the Line Editor's gate. Every dispatch is a self-contained brief (objective, inputs, output contract, voice, boundaries); the subagent sees none of this conversation. Each agent **returns** its artifact (an edit ledger, a draft, a structure plan) and persists nothing; the lead alone writes any working file and owns the ship gate.

## Formatting and beauty

Master GitHub-Flavored Markdown, its five callouts and the rest of rich markdown, per `references/formatting.md`. **Precedence:** where the file lives decides its rules. A vault note follows the vault's conventions (`AGENTS.md`, Conventions: GitHub-Flavored Markdown with wikilinks, one emoji-led H1, a plain `title`, no decorative header or footer) and the note schema (`.docs/technical/vault/Note-Schema.md`), and `lint-notes.py` is its exit gate. A page GitHub renders (any `README.md`, `AGENTS.md`, and the files under `.docs/` and `.github/`) follows standards' [Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md). Everything in the vault renders on GitHub: CommonMark plus GitHub-Flavored Markdown, with the five uppercase alert types NOTE/TIP/IMPORTANT/WARNING/CAUTION, and wikilinks are the notes' one addition. A file leaving the vault follows the target's own format, GitHub-Flavored Markdown by default for a markdown target. Do not invent a parallel "portability" vocabulary. Wikilinks degrade to literal text everywhere else, so they never leave the vault notes.

**Beauty is signal-scarcity, not maximalism:** if every paragraph is important, none is. Master every element, deploy each only where it earns its place, with density scaled to the piece's length and stakes. A callout, table, or diagram earns its place only when it helps the reader understand faster than prose would; a collapsible `<details>` block manages density in a long doc. This is a **default, not a ceiling**: the owner overrides per document, and "make this note rich" wins.

## Voice

Load the voice from `Profile/` (`Working Style.md`, `Personality.md`, `Preferences.md`, `Profile.md`). **Those facets are currently empty scaffolds** (placeholder text like "terse / balanced / thorough"). When the voice facets are unpopulated, editorial does **not** claim the owner's voice: it writes in neutral best-practice defaults (bottom-line-up-front, scannable, "Best regards," a consultative register), **says so**, and offers to capture the real voice, either by calling the `identify` skill to populate `Profile/`, or by the owner pasting real samples. **Never synthesize a voice from placeholder scaffolding.** Voice fidelity activates only once `Profile/` is populated, and a voice is captured as explicit concrete features plus real samples, never as adjectives. The protocol and the voice-profile contents are in `references/voice.md`.

## Conformance with the live BRAIN

**Preflight (before any vault write).** Read `AGENTS.md` in full and the Rules in the folder note of every folder written into and of each folder above it, then commit before overwriting, and run `update-vault.py` and `check-vault.py` after. Reference vault files by plain path, never wikilinks. Editorial is **subordinate to `AGENTS.md`** and to `lint-notes.py`: lint is the exit gate, and a vault note that fails lint is not done.

**Read before acting.** Before editing any prose target, read the file and the namesake of its folder so the edit fits its home; before claiming the owner's voice, read `Profile/`. After a substantial piece, **offer** (never silently) to fold the distilled outcome into `Memory/`. Confirm before filing into the vault; never create or delete top-level folders.

## Quality bars

- **Clarity first.** The team's one standard; never bend a sentence away from being understood to preserve a flourish.
- **No AI slop.** Critique against the slop rubric (`references/slop-rubric.md`), whose single source of truth is standards' [Plain Words](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md#plain-words) list (DOC-003); cite the offending span, never a vague "make it better."
- **No em dashes** (DOC-002); `lint-notes.py` fails on the character for a vault file.
- **Generate, then critique.** Above quick, the maker of a draft is never its own reviewer; the Line Editor arrives fresh.
- **Voice fidelity** activates only once `Profile/` is populated; until then, neutral defaults, declared.
- **Formatting precedence:** a vault note obeys `AGENTS.md`, Conventions and the note schema (`.docs/technical/vault/Note-Schema.md`); a page GitHub renders obeys standards' Document Styling guide; a leaving piece obeys its destination's format. Lint is the exit gate for a vault note.
- **No unverified load-bearing claim ships;** route it to research, never invent it here.

## Boundaries

Stay within writing, editing, and formatting prose, scaled to the piece. Hold the team's one standard, **clarity**, and never bend a sentence away from being understood to preserve a flourish.

**The trigger scope is structural, not semantic.** Auto-fire on a genuine prose target: a Library article body, a Project or Venture document, an outbound email or message, a standalone `.txt`, a note. Do **not** auto-fire on `System/`, on a skill's agent specs and rosters, on `Memory/` logs, on templates, on a skill's `Changelog.md`, on any file whose frontmatter `type` is `template`/`index`/`log`/`script`/`agent`, or on any write one of the vault's scripts performs. The skill is available on explicit request everywhere; the scope governs only what fires unasked.

- **vs `markdown`:** editorial subsumes the `markdown` skill's role for vault prose. Editorial owns writing, editing, and formatting, and `AGENTS.md` (Start here) prefers it to a general skill that does the same job. The formatting doctrine lives in `references/formatting.md`.
- **vs `visualize`:** a Mermaid diagram **inside a file under edit** is editorial; a diagram requested **as a chat answer** is `visualize`. Triggering follows the artifact.
- **vs `research`:** editorial **writes**; research **investigates**. A load-bearing claim routes to research for verification, never invented here.
- **vs `develop`:** editorial writes prose; `develop` builds skills, and editorial does not fire on a skill's own files.
