# Messaging-formats reference

The per-platform chat-dialect reference, loaded on demand. These dialects are
**mutually incompatible**: the same characters mean different things on
different platforms, so the value here is the **contrast**, read the matrix
across a row before formatting a message. Scope is **text markup only**: this
covers what you type into a normal message, not Slack Block Kit, Teams Adaptive
Cards, or any bot or webhook API payload. For true plain text (a `.txt` file or
plain-text email) see `references/plain-text.md`; for the rendering-surface
Markdown syntax see `references/markdown-reference.md`.

The syntax below was verified at each platform's own official documentation on
2026-06-24. Platforms change their dialects (recent moves: WhatsApp lists,
Reddit retiring raw Markdown on mobile, Discord masked links), so re-verify at
the source if a send looks wrong.

## The one-sentence footgun

Do not send CommonMark or GitHub-Flavored Markdown into a chat app and assume it
renders. Slack and WhatsApp use **single** emphasis characters; Discord and
Reddit use **double**. The `[text](url)` bracket-paren link works on some
platforms and not others. iMessage, SMS, and RCS render **no** markup at all.

## Cross-platform matrix

Legend: Y supported, N not supported, ~ supported with a caveat (see that
platform's notes). "CM" is how CommonMark or GitHub does it, for contrast. The
link row shows the bracket-paren form as `[text](url)`.

| Feature | CM | Slack | Discord | WhatsApp | Telegram | Teams (client) | iMsg/SMS/RCS | Reddit |
|---|---|---|---|---|---|---|---|---|
| Bold | `**x**` | `*x*` | `**x**` | `*x*` | `*x*` | `*x*` single | N | `**x**` |
| Italic | `*x*` | `_x_` | `*x*` / `_x_` | `_x_` | `_x_` | `_x_` | N | `*x*` / `_x_` |
| Strikethrough | `~~x~~` | `~x~` | `~~x~~` | `~x~` | `~x~` | `~x~` single | N | `~~x~~` |
| Inline code | `` `x` `` | `` `x` `` | `` `x` `` | `` `x` `` ~ | `` `x` `` | `` `x` `` | N | `` `x` `` |
| Code block | ` ``` ` | ` ``` ` | ` ```lang ` | ` ``` ` ~ | ` ```lang ` | ` ``` ` | N | ` ``` ` / 4-space |
| Quote | `> ` | `> ` | `> ` / `>>> ` | `> ` ~ | N (entity) | `> ` | N | `> ` |
| List | `- ` | N (manual) | `- ` / `* ` | `* ` / `- ` ~ | N | `* ` / `- ` | N | `*` `-` `+` |
| Link | Y | N (angle) | Y ~ | N (raw URL) | Y | Y | N | Y |
| Spoiler / heading | n/a | N / N | spoiler / `#`..`###` | N / N | spoiler / N | N / `#`..`###` | N / N | spoiler / `#`..`######` |

Notes on the matrix: Telegram blockquote exists only as an API entity, not as a
MarkdownV2 string, so treat it as unavailable when authoring MarkdownV2.
Telegram and WhatsApp have **no** headings; Slack has none either. Reddit's
fenced code and pipe tables are desktop-accurate; on `old.reddit.com` use the
4-space-indent code block for portability.

## The footguns, in prose

**Single versus double emphasis characters.** Slack and WhatsApp bold is a
**single** asterisk (`*important*`); the Teams client also uses single-character
bold. Discord, Reddit, and Teams-bot output use the **double** asterisk
(`**important**`). Send a CommonMark `**bold**` into Slack or WhatsApp and the
user literally sees the asterisks. Italic is `_x_` almost everywhere, with the
trap that on Slack and WhatsApp `*x*` is bold, not italic. The strikethrough
character count splits the same way: single `~x~` on Slack, WhatsApp, Telegram,
and the Teams client; double `~~x~~` on Discord and Reddit. Wrong count means
literal tildes or no effect.

**Links split the platforms.** The `[text](url)` bracket-paren link works on
**Discord, Reddit, Telegram, and Teams**. It does **not** work in a normal
**Slack** message, which uses an angle-bracket form with a pipe separating URL
and label, `<https://example.com|display text>`; and it does **not** work in
**WhatsApp**, which takes a **raw URL** only and autolinks it with no custom
label. iMessage, SMS, and RCS also take a bare URL only. Picking the wrong link
form is the most visible failure.

**Telegram MarkdownV2 escaping.** In MarkdownV2, a set of reserved characters
(`_ * [ ] ( ) ~ ` `` `` ` > # + - = | { } . !`) must each be **backslash-escaped**
anywhere they appear as literal text, or the send fails or mis-renders. A stray
unescaped `.`, `-`, `!`, or `(` in ordinary prose breaks the whole message. For
prose-heavy copy, prefer Telegram's **HTML** parse mode, which uses tags like
`<b>`, `<i>`, and `<a href="...">` and only needs `<`, `>`, and `&` escaped,
dodging the escape minefield entirely.

**Headings and strikethrough vary.** Headings (`#`, `##`, `###`) work on
**Discord, Reddit, and the Teams client**. **Slack, WhatsApp, and Telegram have
no headings**, so a leading `# ` is sent literally. As above, the strikethrough
character count is single on some platforms and double on others; do not assume.

**iMessage, SMS, and RCS render no markup.** There is no bold, italic,
strikethrough, code, quote, list, link-label, heading, or spoiler syntax. Typing
`*bold*` sends the literal asterisks; `[label](url)` sends the literal brackets
and parentheses. Emphasis is by **convention only**: ALL-CAPS, punctuation,
spacing, line breaks, or emoji. A bare URL autolinks into a tappable link (and
may show a preview card), but there is no way to attach custom anchor text.
iMessage bubble effects, Tapbacks, and send-time text effects are **UI
features**, not markup an author can encode in the message string. For any
iMessage, SMS, or RCS target, **emit plain text**.

## Scope boundary

This reference is **text markup only**, the characters you type into a normal
message and expect to render. It does **not** cover Slack Block Kit, Teams
Adaptive Cards, or bot and webhook API payloads, which are separate structured
formats with their own schemas and a different (often smaller) set of supported
markers. When the target is an app surface or an automated message rather than a
person's compose box, treat this matrix as a starting point and check that
surface's own developer docs.
