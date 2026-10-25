# Email and letters - conventions

Email and the formal letter are the **furniture-bearing** correspondence genres: they carry a subject or dateline, a salutation, a sign-off, and a register chosen for the reader. The fast, no-furniture genre, chat and text, is in `references/messages.md`. For a plain-text email body see `references/plain-text.md`.

## Branch on the medium first

The first decision is not tone, it is **medium**. An email, a letter, and a chat message are different genres, and a draft that ignores the genre reads wrong no matter how clean the sentences are.

| Medium | Subject line | Salutation | Sign-off | Shape |
|--------|-------------|------------|----------|-------|
| **Email** | yes, short and specific | yes (`Hi [Name],`) | yes (`Best,`) | BLUF, scannable, one explicit ask |
| **Letter** | no (a dateline and address block instead) | formal (`Dear [Name],`) | formal (`Sincerely,`) | sustained, paragraphed, a single arc |
| **Chat / message** | no | no | no | one thought, plain (see `references/messages.md`) |

## Email: bottom-line-up-front

- **BLUF.** The point, the ask, or the answer goes in the **first one or two sentences**. The reader should know why the email exists before they scroll. Context comes after the bottom line, not before it.
- **Subject line.** Short and specific, **under about 55 characters** so it survives truncation. It names the actual topic, not "Quick question" or "Touching base." Optionally prefix the intent: **INFO** (no action needed), **REQUEST** (a reply is needed), **ACTION** (the reader must do something).
- **One explicit call-to-action.** State exactly what you need and by when. "Can you approve the budget by Thursday?" beats "Let me know your thoughts." One ask per email where possible.
- **Scannable.** Short paragraphs; a tight list only when the items are genuinely parallel (not to dress up prose, per `slop-rubric.md`); the ask easy to find on a skim.
- **Greeting and sign-off keyed to the relationship.** See the register ladder below; the default sign-off is "Best regards," cooling to "Best," or "Thanks," as a thread warms.

## Register: tone and formality are two different axes

Do not collapse "how warm" and "how formal" into one dial. **Register** (the formality and situation of the language) and **tone** (the attitude) are independent: a message can be formal and warm, or casual and cold.

**Register has three dimensions** (Field, Tenor, Mode):

- **Field** - what the writing is about (the subject and its technicality).
- **Tenor** - the relationship between writer and reader (peer, senior, client, stranger). This is the dimension that most drives a greeting and a sign-off.
- **Mode** - the channel and its conventions (a written email differs from a spoken-style chat).

**Joos's five-rung ladder** of formality, from most to least formal:

1. **Frozen** - fixed, ceremonial wording (a legal notice, a motto). Rare in correspondence.
2. **Formal** - one-directional, careful, no contractions (a cover letter, a first contact with a senior stranger). `Dear Dr. Reyes,` ... `Sincerely,`.
3. **Consultative** - the professional default: warm, complete, some contractions (most work email). `Hi Sarah,` ... `Best,`. **This is the neutral default** when `Profile/` is empty (`references/voice.md`).
4. **Casual** - relaxed, elliptical, in-group (a colleague you know well). `Hey Sam,` ... `Thanks!` or no sign-off.
5. **Intimate** - private shorthand (close personal ties). Minimal structure.

Pick the rung from the **tenor** (who the reader is), then set the **tone** (warm, neutral, firm) independently. The voice, once captured, carries per-relationship register overrides (`references/voice.md`).

## Greetings and sign-offs (a quick map)

| Relationship | Greeting | Sign-off |
|--------------|----------|----------|
| First contact, senior or formal | `Dear [Title Last],` | `Sincerely,` / `Best regards,` |
| Professional default (consultative) | `Hi [First],` | `Best regards,` / `Best,` |
| Warm, ongoing thread | `Hi [First],` or none | `Best,` / `Thanks,` |
| Close colleague (casual) | `Hey [First],` | `Thanks!` / none |
| Chat / message | none, or a bare `[First]` | none |

When the owner's voice is captured, its actual greeting and sign-off habits override this map. Until then, this is the neutral default and the draft says so on a first send (`references/voice.md`).

## Writing for HTML email

Editorial writes the prose for an HTML email, the body copy, its plain-text twin, and the alt text. These are the writing-side constraints:

- **The plain-text twin is mandatory.** An HTML email is sent as `multipart/alternative` carrying both a `text/html` and a faithful `text/plain` part; a missing plain-text part is a known spam signal, and a one-line plain part behind a large HTML part looks just as suspicious. Author a real plain-text version alongside the HTML, following `references/plain-text.md` (bare URLs, no markup, wrap near 72).
- **Write image-blocking-aware copy.** Images are routinely blocked or proxied, so the email must read fine with no images loaded. Never hide the core message, the call to action, or a link target only inside an image; every essential idea must exist as real text. Give every image meaningful `alt` text.
- **The paste caveat.** Markdown pasted into Gmail, Word, or Google Docs shows as literal symbols (`**bold**`, `# Heading`), because those editors auto-convert Markdown only while you type, not on paste. When formatting must survive a paste, hand off **rich text or HTML**, which the clipboard carries into those editors, not raw Markdown.

A hand-built HTML email (nested-table layout, inline CSS, the Outlook Word-engine quirks) is front-end or dev work, outside a prose skill's lane. For that rare case, consult `caniemail.com` and the Litmus client guides for what each email client actually supports.

## The standing rules still apply

No em dash (DOC-002). No slop, including the chatbot tells "I hope this helps" and "Let me know if you need anything else" (DOC-003 and `slop-rubric.md`). Preserve the sender's length and register unless asked to change them. The template `templates/email.md` scaffolds the most common case.
