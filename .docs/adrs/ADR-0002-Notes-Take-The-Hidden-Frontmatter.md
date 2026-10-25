<!--
title: '🧭 ADR-0002: NOTES TAKE THE HIDDEN FRONTMATTER'
description: 'The vault drops its Obsidian and Claude Code configuration: every note opens with the account''s hidden frontmatter, renders as GitHub-Flavored Markdown and keeps its wikilinks.'
type: record
keywords: [frontmatter, governance, markdown, wikilinks]
status: 'Accepted'
date: '2026-10-19'
evidence: 'N/A'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🧭 ADR-0002: NOTES TAKE THE HIDDEN FRONTMATTER

<a name="top"></a>

**Every note opens with the account's hidden frontmatter and renders on GitHub, wikilinks kept.**

_Five fields that say what a note is, hidden on every page._

</div>

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above and feed the
> [ADR index](README.md).

| Attribute     | Specification                                     |
| :------------ | :------------------------------------------------ |
| **Deciders**  | The vault's owner                                 |
| **Consulted** | The AI agent that carried out the change          |
| **Informed**  | Everyone who generates a vault from this template |

---

## 🎯 Context & Problem Statement

The vault was built for Obsidian. Every note opened with a 15-field `---` block in two bands, one
of them hidden from Obsidian's properties panel by a CSS snippet, tagged from a closed
five-dimension vocabulary, and wrote Obsidian's own markdown: its callouts, embeds and highlights.
On GitHub, where the vault lives, that block renders as a table at the top of every note and the
callouts render as raw text, and seven of the fifteen fields repeat what the path or git already
say. Claude Code hooks in `.claude/` ran the session start, the lint after each edit and the
end-of-turn redraw, for Claude Code alone, while the agent rules now come from the intelligence
stub in [`AGENTS.md`](../../AGENTS.md).

---

## 🚦 Decision Drivers

- **Frontmatter is always hidden**, in every repository the account owns.
- **One standard.** A note reads the same way as every document the account writes.
- **Keep the purpose.** The frontmatter exists so an agent knows what a note is before it reads
  the body.
- **Keep the graph.** The wikilinks stay.
- **Agent rules from one place**, the intelligence stub, not a per-repository configuration.

---

## 🏗️ Considered Options

1. **Keep the `---` block for Obsidian**, and exempt the vault from the account's standard, as
   ADR-0001 left it.
2. **Move every note to the account's hidden frontmatter**, drop the Obsidian and Claude Code
   configuration, and keep the wikilinks.
3. **Carry both**: the hidden block for GitHub, and a `---` block for Obsidian.

---

## ✅ Decision Outcome

**Chosen Option**: Option 2, the hidden frontmatter.

### Rationale for Selection

It is the only option that keeps frontmatter hidden everywhere, and the account's five fields keep
what agents navigated by: a title, a description of what the note is and when to read it, a type,
keywords and a status. Option 3 doubles every note's head, and the two copies drift.

### What Changed

| Was                                                                                  | Is now                                                                                              |
| :----------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| The 15-field `---` block in two bands                                                | The hidden block: `title`, `description`, `type`, `keywords`, `status` (`.docs/technical/vault/Note-Schema.md`) |
| Nine File Role types                                                                 | Six types: `index`, `guide`, `standard`, `reference`, `record`, `template`                          |
| The closed tag vocabulary                                                            | The path, and a few keywords (`.docs/technical/vault/Keywords.md`)                                            |
| The `startup` and `sensitive` tags                                                   | `STARTUP` in `.github/scripts/vault.py`, and the `Profile/` path                                    |
| Freshness tags                                                                       | `freshness/` keyword tokens, on Library holdings                                                    |
| `aliases`, `created`, `updated`, `folder`, `layer`, `policy`, `author`, `path`, `id` | Retired: the path and git say them, and a record may still keep a field of its own kind              |
| A roster's `members` and `lead`                                                      | The team's folder, and its starred spec                                                             |
| An agent spec's 15 fields                                                            | The `---` block its loader reads: `name`, `description` and `tools`                                 |
| Obsidian's markdown and callouts                                                     | GitHub-Flavored Markdown, its five alerts, and wikilinks                                            |
| `.obsidian/` and `.claude/`                                                          | Removed: the session helpers in `.github/scripts/` run by hand                                      |

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                                             |
| :--------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Positive (+)** | Every note renders cleanly on GitHub, follows the account's one standard, and opens with five fields, not fifteen |
| **Negative (-)** | Obsidian loses its properties panel and callout styling, and no hook lints a note as it is written               |
| **Neutral (~)**  | ADR-0001's consequence that notes keep their `---` properties no longer holds; the rest of it stands             |

---

## ⚖️ Trade-off Comparative

### Option 1: Keep The `---` Block

- ✅ Obsidian's properties panel keeps working.
- ❌ Every note shows its frontmatter as a table on GitHub, and the vault is the one repository
  outside the account's standard.

### Option 3: Carry Both Blocks

- ✅ Both renderers show a clean page.
- ❌ Every note carries its head twice, and nothing keeps the two copies in step.

---

## 🔗 Traceability & Links

- [Note schema](../technical/vault/Note-Schema.md) and [keywords](../technical/vault/Keywords.md)
- [ADR-0001](ADR-0001-AGENTS-Holds-The-Vaults-Rules.md), whose note-format consequence this
  replaces
- The account's standard:
  [Frontmatter Metadata](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md#-frontmatter-metadata)

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
> If you rename or move a file, update every reference to it across the repository to prevent link
> drift.

---

<div align="center">

**Hidden on every page. Clear to every agent.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
