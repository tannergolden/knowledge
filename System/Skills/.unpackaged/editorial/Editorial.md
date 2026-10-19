<!--
title: "Editorial - Skill Information"
description: "BRAIN documentation node for the editorial skill: dispatches the standing Editorial team to write, edit, and format any prose, scaled to the piece, to the one standard of clarity with voice fidelity from Profile."
type: "index"
keywords: ["/editorial", "editorial skill", "write skill", "writing skill", "editing", "line editor", "voice fidelity", "ai slop"]
-->

# ✍️ editorial - Information Guide

Filed in `System/Skills/.unpackaged/` - skill sources live hidden and carry no wikilinks; the packaged `editorial.skill` artifact sits at the `Skills/` root. Governance: `AGENTS.md` and the Rules in each folder's note.

## What this skill does

`editorial` is the BRAIN's own writing, editing, and formatting skill. It dispatches the standing Editorial team (`Inbox/Faculties/Editorial/`), scaled to the piece across three tiers (quick, standard, deep): on quick the lead drafts and self-edits inline in a single pass; on standard and deep the Writer drafts and a fresh Line Editor gates it, with the Developmental Editor and the Long-Form or Technical Writer firing on a long or specialized piece. It writes to one overriding standard, clarity, with voice fidelity from `Profile/` ranked beneath it. It handles all of the owner's prose: emails, messages, correspondence, memos, documents, essays, books, notes, and the bodies of Library, Project, and Venture files, plain `.txt` included. It is preferred over a generic writer because it runs the vault preflight, obeys `AGENTS.md` (no em dashes, DOC-002; plain writing, DOC-003), and exits on `lint-notes.py`.

## How it fits the architecture

The skill names the **Editorial team** in `metadata.team: Editorial`, the standing writing team in the federated agent library (`Inbox/Faculties/Editorial/`, lead Editorial Lead / Edith, plus the Writer, Line Editor, Long-Form Writer, Technical Writer, and Developmental Editor). It carries no `agents/` folder of its own: agents are referenced by name and vendored in only at Publish, exactly as `develop` composes the Development team and `research` composes the Research team. The skill is a thin orchestration and doctrine layer. Its `references/` carry the writing method: the tier-and-dispatch table that maps each tier onto the roster, the slop rubric anchored to standards' Plain Words list, the formatting doctrine (with a full markdown-syntax reference and a callout reference: GitHub's five, and Obsidian's set for a target that renders it) that holds a vault note to `AGENTS.md`, Conventions and a page GitHub renders to standards' Document Styling guide, the voice-loading protocol, and the email-and-message conventions. Its `templates/` scaffold the everyday deliverables (an email, a message, a formatted document), and its `assets/` carry the reference data the gate leans on (the callout-type tables and the slop-pattern catalog). The agents themselves live once in `Inbox/Faculties/Editorial/`; every agent returns its artifact and persists nothing, and the lead alone writes any working file and owns the ship gate. A finished piece is delivered to its real home (a Project, a Venture, a Memory or Profile destination), or to the `Inbox/` root when no home is named.

## Design basis

Built by `develop` from a locked requirements brief and a research pass on how to write the best AI writing-and-editing skill: the generate-then-critique architecture (a maker and a fresh reader as different agents), the externalized-rubric finding (naked self-critique degrades, so the standard is written down and the critic cites the offending span), a 51-pattern AI-slop taxonomy reduced to five groups and anchored to standards' Plain Words list, the vault's conventions and standards' Document Styling guide for the formatting doctrine, and register theory (Field/Tenor/Mode and Joos's ladder) for the email-and-message conventions. Three design decisions are load-bearing here: the quick tier is genuinely lightweight (a two-line reply never spins up the team), the voice behavior is honest on day one (the `Profile/` facets are empty scaffolds, so the skill uses neutral defaults, says so, and offers to capture the real voice rather than inventing one), and the markdown-skill boundary is a deferred build decision the orchestrator surfaces rather than silently wiring.
