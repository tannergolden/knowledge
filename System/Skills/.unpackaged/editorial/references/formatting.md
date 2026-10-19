# Formatting doctrine

How editorial formats prose, subordinate to the vault's conventions in `AGENTS.md` (Conventions) and, for a page GitHub renders, to standards' [Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md). Read this before any markdown beautification.

This file is the **doctrine** layer: the beauty principle, the precedence,
and the scope by destination. The exhaustive **syntax** lives
in four companions, loaded on demand: `references/markdown-reference.md` (every
markdown element, with the exact syntax, a worked example, and a portability note),
`references/admonitions.md` (the complete Obsidian callout system),
`references/plain-text.md` (true plain text: `.txt`, plain-text email, the
no-Markdown-into-raw-text rule, line wrapping, format=flowed, the `-- ` signature),
and `references/messaging-formats.md` (the per-platform chat-dialect matrix for
Slack, Discord, WhatsApp, Telegram, Teams, iMessage, and Reddit). The
machine-readable callout aliases are in `assets/callout-types.json`. Reach for the
syntax references when you need the precise form of an element; this file tells you
when and why to use it.

## Precedence (read first)

> [!warning] The vault's rules outrank this file
> A **vault note** follows the conventions in `AGENTS.md` (Conventions): Obsidian markdown, a single H1 that opens with one fitting emoji, a plain YAML `title`, and no decorative header or footer. It carries the two-band frontmatter in `.docs/vault/Note-Schema.md`, tagged only from `.docs/vault/Tag-Vocabulary.md`, and holds no em dash (DOC-002). `lint-notes.py` is the **exit gate**: a piece that fails lint is not done, no matter how it reads. A **page GitHub renders** (any `README.md`, `AGENTS.md`, and the files under `.docs/` and `.github/`) follows standards' [Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md) instead.

The order, hardest first: `AGENTS.md` and the folder's Rules, then `lint-notes.py` for a vault note or the Document Styling guide for a page GitHub renders, then this file, then the owner's per-document override (which can raise density but never break a hard rule).

## Scope - where the file lives

Three destinations, three rule sets. Do not invent a parallel "portability tier" vocabulary; the destination already draws the line.

- **A vault note** (a Markdown note in the BRAIN): follow `AGENTS.md`, Conventions. Obsidian Flavored Markdown is available in full, because the vault renders it: callouts, highlights, comments, block refs, and wikilinks and embeds wherever `.docs/vault/Link-Topology.md` allows the edge. The emoji-H1 rule applies; the no-em-dash rule applies. Frontmatter properties and tags follow the two-band schema in `.docs/vault/Note-Schema.md` and the closed vocabulary in `.docs/vault/Tag-Vocabulary.md`, not freeform Obsidian properties or `#tags`.
- **A page GitHub renders** (any `README.md`, `AGENTS.md`, and the files under `.docs/` and `.github/`): follow standards' [Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md). GitHub's own syntax, including the five uppercase alert types **NOTE, TIP, IMPORTANT, WARNING, CAUTION**, belongs only in these pages (`AGENTS.md`, Conventions).
- **Leaving the vault** (an email, a post, a file handed to someone): follow the **target's own format**. The portable core is CommonMark; drop everything the target cannot render.

> [!danger] Obsidian-only constructs never leave the vault
> Wikilinks and embeds (Obsidian's double-bracket link and transclusion syntax), highlights `==text==`, comments `%% %%`, and block refs `^id` are **Obsidian-only** and degrade to **literal text** everywhere else (a non-Obsidian renderer shows the raw double-bracket markup). They stay in vault notes, never on a page GitHub renders. When a piece is leaving, convert wikilinks to real links or plain text and strip the rest; the wikilink forms, and where a wikilink may go, are in `.docs/vault/Link-Topology.md`.

## The Obsidian callout (admonition) system

A callout is a blockquote whose first line is a bracketed bang-type marker, and
the body is **arbitrary markdown**: lists, code, tables, even nested callouts.

```markdown
> [!note]
> The body is ordinary markdown. Blank line after the type line is not required,
> but keep one before any list or code block inside.
```

Editorial masters the **full** type set (note, abstract, info, todo, tip,
success, question, warning, failure, danger, bug, example, quote, with their
aliases), the foldable variants (`-` collapsed, `+` expanded), custom titles,
nesting to about two levels, and custom types via a CSS snippet. The complete
catalog, with every alias, worked examples, the GitHub-five subset, and the
degradation behavior, is in `references/admonitions.md`; the machine-readable
alias list is `assets/callout-types.json`. The doctrine points to keep in mind
here:

- **Case-insensitive.** The same type renders the same in any case. Vault prose
  conventionally uses lowercase; the GitHub five are uppercase.
- **Foldable callouts are the density tool** for long docs: depth one click away
  instead of a wall.
- **The GitHub five** (NOTE, TIP, IMPORTANT, WARNING, CAUTION, uppercase) are the
  GitHub-rendered alert set, used only in a page GitHub renders (any `README.md`,
  `AGENTS.md`, and the files under `.docs/` and `.github/`; `AGENTS.md`, Conventions).
  In a vault note, use Obsidian's native lowercase callouts and its full type set; a non-Obsidian renderer degrades any callout to a plain nested blockquote.

## Rich markdown the doctrine reaches for (where it earns its place)

- **Tables** (GFM) for genuinely tabular data; set alignment in the delimiter row; keep them narrow, a wide table loses to a list.
- **Fenced code** with a language tag on every fence; `text` for output, `diff` for diffs.
- **Mermaid** diagrams kept as code (`mermaid` fence), matched to the relationship (`flowchart` for process, `sequenceDiagram` over time, `stateDiagram` for transitions). A Mermaid diagram **inside a file under edit is editorial**; a diagram asked for **as a chat answer is `visualize`**.
- **Math** in LaTeX (`$inline$`, `$$block$$`) where the target renders it.
- **Collapsible `<details>`** for optional depth (renders on GitHub and Obsidian).
- **Footnotes, task lists, strikethrough** where the target supports them (GFM and Obsidian, not plain CommonMark).

Match the element to the content, never reach for variety. The principle holds: structure before style, whitespace is structural, the right element for the job, restraint with rich content, keep the source readable.

## Other lightweight markup

When the target document is itself written in a non-Markdown lightweight markup, reStructuredText, AsciiDoc, MediaWiki, Org-mode, BBCode, or Textile, match **that target's** native syntax rather than emitting Markdown. These languages reuse Markdown's glyphs with different meanings, so do not pattern-match from habit: a single asterisk is bold in AsciiDoc but italic in reStructuredText, and a leading hash starts an ordered-list item in MediaWiki, not a heading. The glyphs collide, so verify the few constructs you actually need at the target's own primary docs before writing rather than carrying a stale table in your head.

## The beauty principle (default restraint, owner overrides)

> [!tip] Signal-scarcity, not maximalism
> "If every paragraph is important, nothing is." A callout, table, or diagram earns its place **only when it helps the reader understand faster than prose would.** That is the test for every rich element.

**Default:** master every element, deploy each only where it earns its place, with density scaled to the piece's length and stakes. A two-line note is a two-line note, not a callout with a table. A long technical document carries foldable callouts, a table or two, and a diagram where the structure is genuinely spatial.

This is a **default, not a ceiling.** The owner overrides per document: "make this note rich," "format this for Obsidian, go heavy," "plain text only" all win over the default. State the default when you apply it, then follow the owner's instruction when it differs. Foldable callouts (`[!type]-`) let a long doc stay rich without becoming a wall, putting depth one click away.

## The exit gate

For any vault note: after formatting, run `python3 .github/scripts/lint-notes.py` and clear every error. Confirm the single emoji-led H1 (`AGENTS.md`, Conventions), zero em dashes (DOC-002), and the full two-band frontmatter (`.docs/vault/Note-Schema.md`). The piece is done when it reads clear, sounds true, and lints clean.
