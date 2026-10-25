<!--
title: '🤖 CONTEXT ASSEMBLY'
description: 'How an agent assembles context from the vault so nothing it must remember sits where models forget.'
type: guide
keywords: [context-window, retrieval, ai-agents]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🤖 CONTEXT ASSEMBLY

<a name="top"></a>

**How an agent loads the vault so nothing it must remember sits where models forget.**

_A short context has no middle to lose._

</div>

---

## 🎯 Why It Matters

Language models attend reliably to the **beginning** and the **end** of a long context and
under-weight what sits in the **middle**: a fact buried mid-context is often missed although it is
present. The vault's structure is the main defence: it lets an agent load only what a task needs.
This page says how to assemble context so the vault never depends on a model recalling something
from a low-attention position.

---

## 📥 Retrieve Lean, Not Whole

- **Load the smallest set that answers the task, never the whole vault.** Use the folder notes,
  the catalog (`System/Data/catalog.ndjson`) and the frontmatter filters in
  [Note Schema](Note-Schema.md) to pull only what the task turns on.
- **Prefer many small reads to one large one.** Read the section you need, not the whole file.
- **Never assemble a full-vault context**, even for a fresh agent. Orientation comes from
  [`AGENTS.md`](../../../AGENTS.md) and its start-of-session list; everything else loads on demand.

---

## 📐 When A Long Context Cannot Be Avoided

Place material by attention, not by convenience:

- **Front:** the rules and the task's key files: `AGENTS.md`, `Profile/Working Style.md`, and the
  notes the task turns on.
- **Middle:** bulk reference material, such as `Library/`, whose exact wording is least likely to
  be needed word for word.
- **End:** the single most important constraint, open loop or next step, restated last so it lands
  where recall is highest.

**Never bury a must-not-miss item.** A critical instruction, deadline or constraint goes at the
start or the end of what you assemble. In a session summary or a handoff, keep the active changes
and the next steps at the top or the bottom, never between long background sections.

**A recap that restates a rule names its precedence.** Where a closing recap repeats a rule stated
earlier, such as a summary's overrides, it says plainly that the recap's version supersedes any
earlier one. Without that, a model facing two versions picks one unpredictably.

---

## 🧮 Spend Tokens Where They Count

- **Stable content first, volatile content last.** The order above is also the one prompt caching
  rewards: an identical stable prefix is cached, and a timestamp or a session value placed early
  breaks it. Never open an assembled context, or a note loaded often, with anything that changes
  each session.
- **ASCII over decoration in anything an agent reads.** Box-drawing characters cost several times
  their ASCII equivalents in common tokenizers. The vault's scripts print plain ASCII for that
  reason; do the same in generated reports and tool output.
- **Pick the cheap format for the data's shape.** For bulk tables, CSV or TSV costs about a third
  of JSON, and minified JSON beats pretty-printed. A Markdown table costs more than prose for simple
  facts: use one where scanning matters. Frontmatter arrays stay inline.
- **Load less; never compress.** Summarizing or compressing notes to save tokens trades away the
  exact wording Memory and the Library depend on. The savings come from loading less.

---

<div align="center">

**Load little, place it well, and say the last thing last.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
