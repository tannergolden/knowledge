# Formatting doctrine

How editorial formats prose. Built on the vault's `Library/Technology & Applied Science/Applied Computing & Software/Markdown Style Guide.md` (the house style) and subordinate to it and to the Constitution. Read this before any markdown beautification.

This file is the **doctrine** layer: the beauty principle, the Article IX
precedence, and the internal-versus-leaving scope. The exhaustive **syntax** lives
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

> [!warning] The Constitution outranks this file
> A **vault-internal** file obeys **Constitution Article IX** and the **Instructions Section 8** frontmatter schema, and `brain.command lint` is the **exit gate**. Specifically: rule 9.7 (only Obsidian-compatible markdown by default, with GitHub-Flavored Markdown reserved for a repo-front-page file like a `README.md`), rule 9.6 (every BRAIN markdown file's single H1 begins with one leading emoji, then a space, then the title; the YAML `title` stays plain), rule 9.1 (no em dash, U+2014), and the two-band frontmatter schema on every file. A piece that fails lint is not done, no matter how it reads.

The order, hardest first: the Constitution, then `brain.command lint`, then the Markdown Style Guide, then this file, then the owner's per-document override (which can raise density but never break a hard rule).

## Scope - internal vs leaving the vault

Use **Article IX's own internal-vs-leaving-the-vault split**. Do not invent a parallel "portability tier" vocabulary; the Constitution already draws this line.

- **Vault-internal** (the file lives in the BRAIN): follow the **Constitution**. Obsidian Flavored Markdown is available in full, because the vault renders it: callouts, wikilinks, embeds, highlights, comments, block refs. The emoji-H1 rule applies; the no-em-dash rule applies. Frontmatter properties and tags follow the **Instructions Section 8** two-band schema and the **Article VII** closed tag vocabulary, not freeform Obsidian properties or `#tags`.
- **Leaving the vault** (an email, a GitHub README, a post, a file handed to someone): follow the **target's own format**, and per **Constitution 9.7** keep markdown **Obsidian-compatible by default**. GitHub-Flavored Markdown, including the five uppercase alert types **NOTE, TIP, IMPORTANT, WARNING, CAUTION**, is used **only in a markdown file GitHub renders in its web interface**, its recognized repository and community-health files (`README.md`, `LICENSE.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `GOVERNANCE.md`, and the issue and pull-request templates, per **Constitution 9.7**), never in ordinary leaving-the-vault markdown. The portable core is CommonMark; drop everything the target cannot render.

> [!danger] Obsidian-only constructs never leave the vault
> Wikilinks and embeds (Obsidian's double-bracket link and transclusion syntax), highlights `==text==`, comments `%% %%`, and block refs `^id` are **Obsidian-only** and degrade to **literal text** everywhere else (a non-Obsidian renderer shows the raw double-bracket markup). They stay inside the vault. When a piece is leaving, convert wikilinks to real links or plain text and strip the rest; the exact wikilink and embed syntax lives in the vault's Markdown Style Guide.

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
  GitHub-rendered alert set, used only in GitHub's recognized repository and
  community-health files (`README.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`,
  `SECURITY.md`, and the rest, Constitution 9.7). In the vault, use Obsidian's native lowercase callouts and its
  full type set; a non-Obsidian renderer degrades any callout to a plain nested blockquote.

## Rich markdown the doctrine reaches for (where it earns its place)

- **Tables** (GFM) for genuinely tabular data; set alignment in the delimiter row; keep them narrow, a wide table loses to a list.
- **Fenced code** with a language tag on every fence; `text` for output, `diff` for diffs.
- **Mermaid** diagrams kept as code (`mermaid` fence), matched to the relationship (`flowchart` for process, `sequenceDiagram` over time, `stateDiagram` for transitions). A Mermaid diagram **inside a file under edit is editorial**; a diagram asked for **as a chat answer is `visualize`**.
- **Math** in LaTeX (`$inline$`, `$$block$$`) where the target renders it.
- **Collapsible `<details>`** for optional depth (renders on GitHub and Obsidian).
- **Footnotes, task lists, strikethrough** where the target supports them (GFM and Obsidian, not plain CommonMark).

Match the element to the content, never reach for variety. The Markdown Style Guide's principle holds: structure before style, whitespace is structural, the right element for the job, restraint with rich content, keep the source readable.

## Other lightweight markup

When the target document is itself written in a non-Markdown lightweight markup, reStructuredText, AsciiDoc, MediaWiki, Org-mode, BBCode, or Textile, match **that target's** native syntax rather than emitting Markdown. These languages reuse Markdown's glyphs with different meanings, so do not pattern-match from habit: a single asterisk is bold in AsciiDoc but italic in reStructuredText, and a leading hash starts an ordered-list item in MediaWiki, not a heading. The glyphs collide, so verify the few constructs you actually need at the target's own primary docs before writing rather than carrying a stale table in your head.

## The beauty principle (default restraint, owner overrides)

> [!tip] Signal-scarcity, not maximalism
> "If every paragraph is important, nothing is." A callout, table, or diagram earns its place **only when it helps the reader understand faster than prose would.** That is the test for every rich element.

**Default:** master every element, deploy each only where it earns its place, with density scaled to the piece's length and stakes. A two-line note is a two-line note, not a callout with a table. A long technical document carries foldable callouts, a table or two, and a diagram where the structure is genuinely spatial.

This is a **default, not a ceiling.** The owner overrides per document: "make this note rich," "format this for Obsidian, go heavy," "plain text only" all win over the default. State the default when you apply it, then follow the owner's instruction when it differs. Foldable callouts (`[!type]-`) let a long doc stay rich without becoming a wall, putting depth one click away.

## The exit gate

For any vault-internal file: after formatting, run `python3 System/brain.command lint` and clear every error. Confirm the single emoji-prefixed H1 (9.6), zero em dashes (9.1), and the full two-band frontmatter (Section 8). The piece is done when it reads clear, sounds true, and lints clean.
