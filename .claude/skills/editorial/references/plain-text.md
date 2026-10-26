# Plain-text reference

How editorial formats true plain text: a `.txt` file, a plain-text email, or a
plain-text message, where no renderer will interpret syntax. The companion
syntax reference `references/markdown-reference.md` covers a rendering surface;
this file covers the absence of one. The single shared decision, know your
destination surface, is stated canonically there; everything below is specific
to non-rendering targets. For per-platform chat dialects (Slack, Discord,
WhatsApp, and the rest) see `references/messaging-formats.md`.

For each element: the rule, a short example, and a scope note saying where it
applies. The line-length and reflow rules cite RFC 5322, RFC 3676, and RFC 1849
in prose, not as links.

## The headline footgun: never emit Markdown into raw text

**Rule.** Do not emit Markdown (or any other markup) into a destination that
will not render it. In a plain-text email, a `.txt` file, an SMS or iMessage, or
any box that shows raw text, syntax does not format, it shows up as literal
noise. `**bold**` keeps its asterisks, `# Heading` keeps its hash, backtick
fences print the backticks, and a pipe-and-dash Markdown table prints as a wall
of punctuation. The most damaging case is the link: `[label](url)` shows the
brackets and parentheses and *buries* the actual URL inside them, so the reader
loses the one thing they needed. Write **bare URLs** in plain text.

Example, the same line wrong then right for a plain-text target:

    Wrong:  See the **Q4 report** at [the dashboard](https://acme.co/q4).
    Right:  See the Q4 report at the dashboard: https://acme.co/q4

**Scope.** Applies to every non-rendering target. The flip side: a
Markdown-rendering surface (a GitHub comment, Obsidian, a Discord or Slack
message box) wants Markdown and should get it. The two are mutually exclusive;
know which surface you are writing for before the first character.

## Line wrapping: wrap near 72, the 998 wall is not a target

**Rule.** Wrap prose near **72 columns**. RFC 5322 says an email line SHOULD be
no more than 78 characters and MUST be no more than 998, excluding the CRLF. The
78 figure is the working display ceiling, set so that clients which truncate or
hard-wrap a long line do not mangle the message; 72 sits under it with headroom.
The 998 (from the RFC 5321 SMTP 1000-octet line limit) is the **hard wall** a
relay can bounce or corrupt a message for crossing, not a width to aim at. A
2,000-character single "line" is the failure this prevents.

Why 72 specifically: it leaves room for several levels of `> ` reply-quoting to
be added before any line overflows an 80-column terminal, and 80 itself is risky
because the 80th column is often where a terminal draws its line-wrap marker, so
78 is the safe display width and 72 the safe wrap width. The 76 you may also see
is the MIME base64 / quoted-printable encoded-line ceiling, not a prose width;
do not chase it unless you are matching an encoded payload.

Example, a body wrapped near 72:

    The quarterly numbers are in. Revenue is up nine percent over the prior
    quarter, driven almost entirely by the two enterprise renewals that closed
    in the final week. Margin held flat.

**Scope.** The 78 and 998 figures are email-body rules from RFC 5322 and RFC
5321. A `.txt` file on disk has no RFC governing it, but the same display logic
(editors and terminals wrap or truncate long lines) carries over, so wrap there
too. Never assume the reader's window is exactly 80 columns.

## format=flowed: soft breaks that reflow on a phone

**Rule.** When sending **email** (not a `.txt` file or an SMS), the way to get
text that is hard-wrapped for old clients yet reflows to fit a phone screen is
RFC 3676 `format=flowed`. The mechanic: end every line you want to be joinable
with a single **trailing space** before the line break (a soft break); end a
line with no trailing space to force a hard break. A flowed-aware reader rejoins
the soft-broken lines into one paragraph and re-wraps to its own width; a plain
reader just shows your original wrap. Generate flowed lines at 78 or fewer
characters (72 is the suggested wrap).

**Space-stuffing** is the companion rule and a footgun: to send a line that
genuinely begins with a space, with `>`, or with the literal text `From `, add
one leading space on generation; the receiver deletes one leading space on
reception.

Example, a flowed paragraph (the middle line ends in a trailing space, marked
here with a dot, so it stays joinable; the last line has none and ends the
paragraph):

    The quarterly numbers are in. Revenue is up nine percent over the·
    prior quarter, driven by two enterprise renewals. Margin held flat.

**Scope.** `format=flowed` is signaled by a MIME parameter on the email's
`Content-Type` header (`text/plain; format=flowed`). It does **nothing** in a
bare `.txt` file or an SMS, and means nothing unless the message is a properly
typed MIME email whose header you control. If you emit raw body text without
that header, hard-wrap at 72 for the widest correctness. The trailing-space
convention is also invisible and fragile: an editor that strips trailing
whitespace silently destroys it.

## The signature delimiter: dash dash space

**Rule.** Precede a signature with a line containing exactly two hyphens and one
**trailing space**, `-- `, and nothing else. This is the long-standing Usenet and
email convention named in RFC 1849 (and confirmed by RFC 3676): a conformant
client recognizes the delimiter and can auto-trim or de-emphasize everything
below it, and correctly excludes the signature when quoting your message in a
reply. RFC 1849 suggests keeping a signature to about four lines.

Example:

    Looking forward to the review on Thursday.

    -- 
    Jane Okafor
    Field Operations · Acme Corp
    jane@example.com

**Scope.** The trailing space is **load-bearing and invisible**; RFC 1849 itself
calls the choice "somewhat unfortunate" because it relies on preserving trailing
whitespace, "but it is too well-established to change." Many editors and some
webmail compose boxes strip trailing whitespace, turning `-- ` into `--` and
breaking recognition. If you write this delimiter, preserve the one space and do
not let a formatter trim it.

## Structure without markup

**Rule.** Use only structure that survives as literal characters, because
nothing will interpret syntax:

- **Blank lines** are the primary separator: one between paragraphs, one or two
  to set off a heading block.
- **Headings**: ALL-CAPS or Title Case on their own line. No `#`. You may
  underline with a run of `=` or `-`, which reads fine as plain text.
- **Indentation**: indent with literal **spaces**, not tabs, which render at
  unpredictable widths, to show a block quote, a code sample, or nesting.
- **Horizontal rules**: a run of `-`, `=`, or `*` makes a visible divider.
- **Lists**: a leading `- `, `* `, or `1. ` reads as a list to a human even with
  nothing rendering it. Keep the marker consistent and align wrapped lines under
  the text.
- **Tables**: only simple **fixed-width ASCII**, aligned with spaces.

Example:

    QUARTERLY SUMMARY
    =================

    Revenue is up. Two themes:

      - Enterprise renewals carried the quarter.
      - Self-serve signups were flat.

    Region      Q3      Q4
    --------   -----   -----
    AMER        120     141
    EMEA         88      88

**Scope.** The fixed-width ASCII table is the trap: it collapses into garbage the
instant it is shown in a proportional font, which is the default in most webmail
and on phones. Reserve a table for a known-monospace context and prefer a short
list otherwise. Everything else here reads correctly in any monospace view.

## Emphasis in plain text: ambiguous, so use it sparingly

**Rule.** The plain-text emphasis conventions are `*asterisks*`, `_underscores_`,
and CAPS for the one word that must stand out. Treat them as conventions read by
humans, not as guaranteed formatting, and use them sparingly. The catch:
`*word*` and `_word_` are now **ambiguous**, because some clients auto-style
them. Microsoft's own documentation describes current Outlook converting
`_italic_` to real italics and `*bold*` to real bold, a behavior users report
being unable to disable. So the same run may render as literal characters in one
client and as actual bold or italic in another, and you cannot predict which.

Example:

    The single *most important* thing is the renewal pipeline.

That line is fine whether the asterisks show literally or render as italic,
which is exactly the test.

**Scope.** Use asterisk or underscore emphasis only where **either outcome is
acceptable**, and never rely on it to carry meaning. For a word that truly must
stand out regardless of client, CAPS is the only fully portable choice.

## Reply quoting: the `>` prefix, interleaved replies

**Rule.** Quote prior text by prefixing each quoted line with `> `; each
additional nesting level adds another `>`, so `>> ` is a quote of a quote. RFC
3676 makes this the canonical quote indicator and defines quote depth by the
count of leading `>` characters. **Interleaved** (bottom-posting), trimming the
quote to the relevant lines and replying directly below each point, keeps
question and answer adjacent and is the convention these RFCs assume.

Example, interleaved:

    > Can we move the review to Thursday?

    Thursday works. Morning or afternoon?

    > And do you have the Q4 margin number?

    Yes, flat versus Q3. Numbers attached.

**Scope.** Interleaving is correct and readable in plain text and is what the
flowed-quoting machinery is built around, but it is a minority practice in
business email, where many readers expect top-posting (the whole reply above the
quoted message). Match the thread you are in. Whichever you pick, the mechanical
rule is invariant: every quoted line gets a `>` prefix, and you trim quoted
material to what is actually relevant rather than quoting an entire message.

## Source notes

The line-length, reflow, signature, and quoting rules are verified verbatim at
the primary RFCs: RFC 5322 (Internet Message Format) §2.1.1 for the 78 SHOULD and
998 MUST line limits; RFC 3676 (the text/plain Format and DelSp parameters) for
`format=flowed`, the soft-break and space-stuffing mechanics, the 80-column
rationale, and the `>` quote indicator; and RFC 1849 ("Son of 1036") §4.3.2 for
the `-- ` two-hyphens-plus-blank signature delimiter and its trailing-whitespace
caveat. The Outlook asterisk and underscore auto-styling is verified at a
first-party Microsoft support page rather than an RFC, since no RFC governs how a
client renders those runs.
