# Messages and chat - conventions

A chat or text message is the **no-furniture** genre: one thought, delivered plain. It is defined mostly by what it leaves out. For email and formal letters (the salutation, the sign-off, the full register ladder) see `references/email.md`; for the exact per-platform syntax (Slack, Discord, WhatsApp, and the rest) see `references/messaging-formats.md`.

## One thought, delivered plain

A message is one thought, often one line, with no ceremony. It gets **no** subject line, **no** salutation (a bare first name at most), and **no** sign-off.

> [!WARNING]
> **Do not put email furniture on a chat.**
> Writing "Hi Sarah, ... Best, Tanner" in a Slack or text message is the most common medium error. A chat reply gets no subject line, salutation, or sign-off. A message is one thought delivered plain.

## Register: keep it light, match the thread

A message usually sits at the **casual** or **consultative** rung (Joos's lower-middle): contractions, brevity, and in-group shorthand where the relationship supports it. Pick the rung from the **tenor** (who the reader is) and match the thread you are already in, do not formalize a casual exchange on the way through. The full register ladder and its three dimensions (Field, Tenor, Mode) live in `references/email.md`. Once the owner's voice is captured, its actual chat habits override the default (`references/voice.md`).

## Platform syntax does not travel

What renders as bold, a quote, or a link differs by app, and Markdown is not portable across them: a CommonMark `**bold**` shows literal asterisks in Slack or WhatsApp, where bold is a single asterisk. Before sending, match the destination's dialect from `references/messaging-formats.md`. On SMS, iMessage, and RCS there is no markup at all: emit plain text and let a bare URL autolink, with emphasis carried by caps or punctuation.

## The standing rules still apply

No em dash (DOC-002). No slop, including the chatbot tells "I hope this helps" and "Let me know if you need anything else" (DOC-003 and `slop-rubric.md`). Preserve the sender's length and register; a chat reply stays a chat reply. The template `templates/message.md` scaffolds the common case.
