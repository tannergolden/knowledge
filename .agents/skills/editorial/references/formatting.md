# Formatting doctrine

How editorial formats prose, subordinate to the vault's conventions in `AGENTS.md` (Conventions) and, for a page GitHub renders, to standards' [Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md). Read this before any markdown beautification.

This file is the **doctrine** layer: the beauty principle, the precedence,
and the scope by destination. The exhaustive **syntax** lives
in four companions, loaded on demand: `references/markdown-reference.md` (every
markdown element, with the exact syntax, a worked example, and a portability note),
`references/admonitions.md` (callouts: GitHub's five, and Obsidian's full set
for a target that renders it),
`references/plain-text.md` (true plain text: `.txt`, plain-text email, the
no-Markdown-into-raw-text rule, line wrapping, format=flowed, the `-- ` signature),
and `references/messaging-formats.md` (the per-platform chat-dialect matrix for
Slack, Discord, WhatsApp, Telegram, Teams, iMessage, and Reddit). The
machine-readable callout aliases are in `assets/callout-types.json`. Reach for the
syntax references when you need the precise form of an element; this file tells you
when and why to use it.

## Precedence (read first)

> [!WARNING]
> **The vault's rules outrank this file.**
> A **vault note** follows the conventions in `AGENTS.md` (Conventions): GitHub-Flavored Markdown with wikilinks, a single H1 that opens with one fitting emoji, a plain `title`, and no decorative header or footer. It opens with the hidden frontmatter in `.docs/technical/vault/Note-Schema.md`, and holds no em dash (DOC-002). `lint-notes.py` is the **exit gate**: a piece that fails lint is not done, no matter how it reads. A **page GitHub renders** (any `README.md`, `AGENTS.md`, and the files under `.docs/` and `.github/`) follows standards' [Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md) instead.

The order, hardest first: `AGENTS.md` and the folder's Rules, then `lint-notes.py` for a vault note or the Document Styling guide for a page GitHub renders, then this file, then the owner's per-document override (which can raise density but never break a hard rule).

## Scope - where the file lives

Three destinations, three rule sets. Do not invent a parallel "portability tier" vocabulary; the destination already draws the line.

- **A vault note** (a Markdown note in the BRAIN): follow `AGENTS.md`, Conventions. The markdown renders on GitHub, the vault's home renderer: CommonMark plus GitHub-Flavored Markdown (tables, task lists, strikethrough, footnotes, the five alerts, math, Mermaid), with wikilinks as the one addition, wherever `.docs/technical/vault/Link-Topology.md` allows the edge. Embeds, highlights, `%%` comments, block references and callout types beyond the five are not used. The emoji-H1 rule applies; the no-em-dash rule applies. Frontmatter follows the hidden schema in `.docs/technical/vault/Note-Schema.md`, never freeform properties or `#tags`.
- **A page GitHub renders** (any `README.md`, `AGENTS.md`, and the files under `.docs/` and `.github/`): follow standards' [Document Styling guide](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md). Its syntax is the same GitHub-Flavored Markdown, without wikilinks.
- **Leaving the vault** (an email, a post, a file handed to someone): follow the **target's own format**. For a markdown target, GitHub-Flavored Markdown is the default; the portable core is CommonMark, so drop everything the target cannot render. A target that renders more, such as someone's Obsidian vault, may take its own constructs (`references/admonitions.md` has Obsidian's callout set).

> [!CAUTION]
> **Wikilinks never leave the vault notes.**
> They are the notes' own link syntax, resolved by `check-links.py`; every other renderer shows the raw double brackets as literal text. They stay in vault notes, never on a page GitHub renders. When a piece is leaving, convert each wikilink to a real link or plain text; the wikilink forms, and where a wikilink may go, are in `.docs/technical/vault/Link-Topology.md`.

## Callouts: the GitHub five

A callout (GitHub calls it an alert) is a blockquote whose first line is a
bracketed bang-type marker, in uppercase and alone on its line. The body is
ordinary markdown on the following `>` lines.

```markdown
> [!NOTE]
> **An optional bold lead-in.**
> The body is ordinary markdown. Keep a blank `>` line before any list or code
> block inside.
```

The vault uses exactly the five types GitHub renders:

- **NOTE** - context worth knowing even when skimming; also the stop-early summary at the top of a long piece.
- **TIP** - advice: a better or faster way to do the thing.
- **IMPORTANT** - the one point the reader needs to succeed.
- **WARNING** - a hazard that needs attention now.
- **CAUTION** - the risk or negative outcome of an action, such as data loss.

The doctrine points to keep in mind:

- **No title after the marker.** GitHub takes none; give a callout a title as a bold lead-in on its first body line.
- **Sparingly, and never nested.** GitHub advises one or two per document; signal-scarcity (below) agrees.
- **No folding.** For optional depth in a long doc, use a collapsible `<details>` block.
- **Obsidian's full set** (abstract, info, todo, success, question, failure, danger, bug, example, quote, the foldable `-` and `+` variants, custom titles) is for a target that renders it. The catalog, with every alias and the degradation behavior, is in `references/admonitions.md`, and the machine-readable list in `assets/callout-types.json`.

## Rich markdown the doctrine reaches for (where it earns its place)

- **Tables** (GFM) for genuinely tabular data; set alignment in the delimiter row; keep them narrow, a wide table loses to a list.
- **Fenced code** with a language tag on every fence; `text` for output, `diff` for diffs.
- **Mermaid** diagrams kept as code (`mermaid` fence), matched to the relationship (`flowchart` for process, `sequenceDiagram` over time, `stateDiagram` for transitions). A Mermaid diagram **inside a file under edit is editorial**; a diagram asked for **as a chat answer is `visualize`**.
- **Math** in LaTeX (`$inline$`, `$$block$$`) where the target renders it.
- **Collapsible `<details>`** for optional depth, the density tool for a long doc (renders on GitHub).
- **Footnotes, task lists, strikethrough** where the target supports them (GFM, not plain CommonMark).

Match the element to the content, never reach for variety. The principle holds: structure before style, whitespace is structural, the right element for the job, restraint with rich content, keep the source readable.

## Other lightweight markup

When the target document is itself written in a non-Markdown lightweight markup, reStructuredText, AsciiDoc, MediaWiki, Org-mode, BBCode, or Textile, match **that target's** native syntax rather than emitting Markdown. These languages reuse Markdown's glyphs with different meanings, so do not pattern-match from habit: a single asterisk is bold in AsciiDoc but italic in reStructuredText, and a leading hash starts an ordered-list item in MediaWiki, not a heading. The glyphs collide, so verify the few constructs you actually need at the target's own primary docs before writing rather than carrying a stale table in your head.

## The beauty principle (default restraint, owner overrides)

> [!TIP]
> **Signal-scarcity, not maximalism.**
> "If every paragraph is important, nothing is." A callout, table, or diagram earns its place **only when it helps the reader understand faster than prose would.** That is the test for every rich element.

**Default:** master every element, deploy each only where it earns its place, with density scaled to the piece's length and stakes. A two-line note is a two-line note, not a callout with a table. A long technical document carries a `<details>` block or two, a table, and a diagram where the structure is genuinely spatial.

This is a **default, not a ceiling.** The owner overrides per document: "make this note rich," "go heavy on the formatting," "plain text only" all win over the default. State the default when you apply it, then follow the owner's instruction when it differs. A collapsible `<details>` block lets a long doc stay rich without becoming a wall, putting depth one click away.

## The exit gate

For any vault note: after formatting, run `python3 .github/scripts/lint-notes.py` and clear every error. Confirm the single emoji-led H1 (`AGENTS.md`, Conventions), zero em dashes (DOC-002), only the five callout types, and the hidden frontmatter (`.docs/technical/vault/Note-Schema.md`). The piece is done when it reads clear, sounds true, and lints clean.
