<!--
title: '🪪 PROFILE'
description: 'Who the owner is, in twelve facets: eleven of the stable self, from Working Style and Biography to Finances and Health, and the dynamic Focus layer, the foundation for personalized, contextually appropriate help. Read it before using or recording anything about the owner, for where each fact goes and how it is read and written with discretion.'
type: 'index'
keywords: ["identity", "self", "about me", "who the owner is", "personal profile", "stable self", "personalization", "identity layer"]
-->

<div align="center">

# 🪪 PROFILE

<a name="top"></a>

**The owner in twelve facets: eleven of the stable self, and the dynamic Focus layer.**

_The owner's own account, absorbed as context and never quoted back._

</div>

---

## 📏 Rules

Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it. These govern every write to `Profile/`, and every write to `Memory/` that touches who the owner is.

- **Read-only by default.** Every note here is read-only unless the owner asks for an update: it is their own description of themselves, and never changes on inference alone.
- **Propose, never write silently.** Something learned about the owner that belongs here or in `Memory/` is proposed first, as a question: _"Noticed: [X]. Add it to [file]?"_
- **Facts, not guesses.** Only what the owner said, or what was observed directly, is recorded. Nobody speculates about them across sessions or presents an inference as a fact: a proposed inference carries its marker and stays `unconfirmed` until approved (Provenance And Freshness, below).
- **One home for who the owner is.** A fact about them lives here and only here, never copied into `Memory/`.
- **The most care for sensitive categories.** Health and medical conditions, finances, relationships, political or religious views, legal matters and mental health are surfaced only when the task needs them, in any folder. A profile is absorbed as context and never quoted back.

---

## 💡 What This Folder Is

Who the owner is, facet by facet, with `Working Style.md`, read at the start of every session, saying how they want to be helped. In the public template every facet is a blank scaffold; in a vault generated from it, which stays private, these are the most personal notes it holds.

Everything needed to understand **who the owner is as a person**, and the foundation for personalized, contextually appropriate help. These files are a **personal profile, not reference material**: they inform the work as context, applied naturally, and are never a checklist to work through.

`Profile/` is the **stable self**: the durable, slowly-changing facts about who the owner is. It is organized the way personality and identity are described in both psychology and modern personalization research, **by facet of the self** (working style, background, traits, values, goals, relationships, money, daily life, skills, tastes, health), with one dynamic exception, [[Profile/Focus|Focus]], for what is true only right now.

---

## 🧩 The Facets

| Facet | Holds | When it is read |
|-------|-------|-----------------|
| [[Profile/Working Style\|Working Style]] | How the owner wants to be helped and how they collaborate: do's, don'ts, tone, length, format, feedback and decision style | First, at every session start |
| [[Profile/Biography\|Biography]] | Life history and facts: name, location, work, education, family, formative years, life story | When biographical context helps |
| [[Profile/Personality\|Personality]] | Traits, temperament, cognitive and working style, character strengths, behavior under pressure | To calibrate tone, pacing and depth |
| [[Profile/Values/README\|Values]] | Core values, ethics, purpose, life philosophy, and held beliefs (sensitive) | When weighing options or giving advice |
| [[Profile/Goals/README\|Goals]] | Enduring aspirations and direction (the stable "what I am working toward") | When advising on direction and weighing options |
| [[Profile/Relationships\|Relationships]] | The relational self: family and household structure, roles, social network, attachment and relational style; the people themselves are in Memory (sensitive) | When relationships matter |
| [[Profile/Finances\|Finances]] | The personal financial picture: situation, assets and liabilities, money style, estate pointers (sensitive) | When money or planning is involved |
| [[Profile/Lifestyle\|Lifestyle]] | How the owner lives: daily rhythm, sleep, diet, exercise, substances, environment, recreation | When daily life is relevant |
| [[Profile/Skills/README\|Skills]] | Competencies and the per-domain expertise map | When calibrating how much to explain |
| [[Profile/Preferences\|Preferences]] | Interests, tastes, tools, lifestyle, likes and dislikes | When personalizing suggestions |
| [[Profile/Health/README\|Health]] | Stable health attributes and accessibility needs that affect how to help (sensitive) | Only when directly relevant |
| [[Profile/Focus\|Focus]] | The **dynamic** layer: current priorities, routines, and the current life chapter. It changes often, so it outranks older notes and is refreshed when used | When acting on current context |

---

## 🔄 Stable Vs. Dynamic

Every facet except [[Profile/Focus|Focus]] is **stable**: traits, values, and background that hold over months and years. `Focus.md` is the deliberate **dynamic** layer, current priorities, routines and the current life chapter, and it is the pressure-release valve that keeps the rest of the profile timeless. A standing goal is a `Goals/` fact; this week's priority is a `Focus.md` fact. The test is whether it would still be true in a year: if yes, it is stable; if no, it is Focus (or it belongs in Memory or Projects).

---

## 🏗️ How The Facets Are Built

Facets come in two shapes, the same split as `Memory/`. A facet read as a whole is a single **flat file** at the `Profile/` root (Working Style, Biography, Personality, Relationships, Finances, Lifestyle, Preferences, Focus). A facet that accretes many independent items is a **folder** whose `README.md` is the facet's overview, plus one **entry file per item** (Values holds belief entries; Goals, Skills, and Health hold one entry per goal, skill, or condition), listed in its README by `update-vault.py`. A new facet or entry is copied from `.template/`, whose `README.md` says which scaffold makes what: `Facet Overview.md` for a flat facet, `Folder Facet.md` for a folder's `README.md`.

A flat facet becomes a folder only once it grows entries, such as Biography gaining life-chapter entries, and never speculatively. The promotion moves its overview to the folder's `README.md`, in the page shape of `.template/Folder Facet.md`, adds the folder to `PROFILE_COLLECTIONS` in `.github/scripts/vault.py` and the facet's new shape to `FACETS` in `.github/scripts/profile-coverage.py`, so its entries are listed and scored, and points the facet's row in the table above to its `README.md`.

Each independently-answerable fact is its own `## H2`, so it chunks cleanly for retrieval, with the subject restated in the heading and discrete facts kept in tables and lists. The facet files carry `type: "reference"`; this README carries `index`, and the scaffolds `template` (`.docs/technical/vault/Note-Schema.md`). No field marks a file personal: everything under `Profile/` is personal by its path, and it is found by folder path plus `keywords`, never tags (`.docs/technical/vault/Keywords.md`).

---

## 📥 What Lands Here

Every write here follows the Rules above, whatever work makes it:

- **Human resources work for the owner's own life**: the profile interview (Filling These Files, below), their career and skills (`Biography.md`, `Skills/`, `Goals/`) and their health and wellbeing (`Health/`, `Lifestyle.md`).
- **The owner's money facts**, from finance and accounting work, in `Finances.md` alone: the picture and pointers, never a secret number.
- **What any other work learns about who the owner is**, proposed first: a goal or priority set in administration work (`Goals/`, `Focus.md`), where a will or a lease handled in legal and compliance work is kept (`Finances.md`, Legal & Estate), the routines planned in operations and logistics work (`Focus.md`), and the devices, accounts and tools set up in information technology work (`Preferences.md`), never a password or a key.

---

## 🧱 Profile Vs. The Other Layers

`Profile/` is the **single home for who the owner is** (Rules, above): background, personality, values, preferences, skills, beliefs, goals, and health, whether the owner stated it or it was observed.

- **Memory** holds only what Profile cannot: what happened (sessions, the Log, Events), who is around the owner (Entities/People), what they decided (Decisions), and when things occur (Dates). Something learned about the owner *themselves* is proposed as a `Profile/` edit; a parallel copy is never stored in Memory.
- **Ventures** holds business context and business contacts; `Profile/` is the *personal* self.
- **Library** holds general and world knowledge; `Profile/` is never reference material (`Library/README.md`, Rules).
- **Projects** holds project execution and tasks; `Profile/` holds the person, not the work.

---

## 🏷️ Provenance And Freshness

Profile entries carry their origin and stay fresh by use, not by schedule. The convention is deliberately lightweight: it puts the Rules' propose-first into practice without adding any frontmatter field.

- **Self-reported is the default.** Anything the owner states needs no marker; a plain entry is a self-reported fact.
- **What is inferred is marked.** An entry inferred rather than stated by the owner carries an inline HTML comment, which renders invisibly on GitHub and in any Markdown preview but stays in the source:
  `**Field:** value <!-- observed 2026-06-19 · confidence: low|medium|high · unconfirmed -->`
  On the owner's confirmation, it is shortened to `<!-- confirmed 2026-06-19 -->` or dropped (a confirmed fact is just a fact). An entry left `unconfirmed` is a proposal awaiting approval, never treated as established (Rules, above).
- **Refreshed on use, not on a calendar.** A section that still holds when it is used is current; something stale is fixed then. A drift-prone section (occupation, current chapter) may carry `<!-- reviewed 2026-06-19 -->` at its end once it is confirmed.

**The provenance markers.** The marker tokens are fixed so they stay machine-filterable across the whole layer: a state token (`observed` | `confirmed` | `reviewed`) with an ISO date, an optional `confidence: low | medium | high`, and the proposal flag `unconfirmed`. The lifecycle is `observed` + `unconfirmed` (an inference, a proposal) -> `confirmed` (the owner approved it) -> `reviewed` (re-verified later). Because the tokens are fixed, the profile is queryable: a search for `unconfirmed` lists every pending proposal, and one for `confidence: low` surfaces the weakest inferences to re-check. Self-reported facts stay unmarked, so a marker only ever appears on an exception.

---

## 🛡️ Sensitivity

The whole `Profile/` tree is **sensitive by default**, by its path (`.docs/technical/vault/Keywords.md`): no tag marks it, because the folder already does. Discretion is applied when information is surfaced, not by hiding files: this information is surfaced only when the task needs it (Rules, above). The most private facts are **isolated into their own entry files**, a health condition in `Health/` and a held belief in `Values/`, and the people in the owner's life live in `Memory/Entities/People/`, so that a benign query never drags them in: the per-entry granularity is itself the privacy control. The most sensitive entries are kept terse and factual, recording the minimum needed to be considerate, not a full record.

---

## 🎙️ Filling These Files: The Profile Interview

The recommended way to fill or deepen these files is a structured interview rather than hand-editing: the profile interview this section describes, which any AI assistant working here runs when the owner asks. When the owner runs the AI workforce, Human Resources' HR Generalist runs it, and the Knowledge Vault Manager writes each change only after the owner's yes, an inference marked `unconfirmed` until the owner confirms it (the root `README.md`, When The Workforce Works Here). `python3 .github/scripts/profile-coverage.py --json` scores each facet and names the next one to ask about, starting with `Working Style.md` while it is still blank. The interview reads what each file holds, targets what is thin or unconfirmed, and asks structured questions drawn from validated frameworks: **Big Five** for Personality, **Schwartz's basic values** for Values, the **McAdams life-story** method for Biography, mixing direct questions for facts with indirect ones that surface traits the owner would not think to state. Sensitive facets (Health, Finances, Values, Relationships) open only on the owner's opt-in. What it writes follows the rules on this page: an inference is **marked, evidence-cited, confidence-rated and left unconfirmed until approved**, sensitive topics come with skip options, and each file's last state is committed before it is written. Hand-editing is fine for a quick correction, but misses the inference layer and those safeguards.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                    | Purpose                                                                                                                                                                                                                                                                                                       |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`.template/`](.template/README.md)      | The Profile scaffolds: a flat facet, the README of a facet that is a folder, a generic entry, and the entries of the folder facets (a belief, a goal, a skill, a health condition, a life chapter). Read it before copying one to add a facet or an entry, each copied on its own and never edited in place.  |
| [`Goals/`](Goals/README.md)              | The owner's enduring aspirations and direction: the stable, long-horizon goals that define what they are working toward, distinct from this week's priorities. Read it when advising on direction or weighing options.                                                                                        |
| [`Health/`](Health/README.md)            | Stable health attributes and accessibility needs that affect how to help. For awareness, not diagnostic use; surfaced only when directly relevant. Conditions are isolated as their own sensitive entries.                                                                                                    |
| [`Skills/`](Skills/README.md)            | The owner's competencies and the per-domain expertise map that calibrates how much to explain: skip the basics where the owner is expert, define terms where they are new. Read it before explaining anything, to pitch the depth to the owner's level in that domain.                                        |
| [`Values/`](Values/README.md)            | What the owner cares about and how they decide what is right: core values, orientation axes, life philosophy, ethics, motivation, purpose, role models, and what they stand for and against, plus held beliefs as sensitive entries. Read it when weighing options or giving advice.                          |
| [`Biography.md`](Biography.md)           | The owner's life facts and life story: name, contact, location, work, education, family, formative years, key events, and the McAdams narrative themes that give the facts meaning.                                                                                                                           |
| [`Finances.md`](Finances.md)             | The owner's stable personal financial picture and money-management self: financial situation, assets and liabilities, insurance, risk posture, money style, financial goals, and the existence and location of legal and estate documents. Sensitive; records the picture and pointers, never secret numbers. |
| [`Focus.md`](Focus.md)                   | The dynamic layer: the owner's current priorities, how to help right now, routines, current life chapter, and what is on the horizon. Changes often; trust it over older notes and refresh it on use.                                                                                                         |
| [`Lifestyle.md`](Lifestyle.md)           | How the owner lives day to day: the stable patterns of sleep, diet, exercise, substances, daily rhythm, rituals, living environment, and recreation. The enduring counterpart to the dynamic Focus layer.                                                                                                     |
| [`Personality.md`](Personality.md)       | How the owner thinks, focuses, feels, works, learns, and behaves under pressure: personality typing, Big Five with BFI-2 facets, temperament, cognitive/working/learning style, emotional and social style, strengths, blind spots, and behavior under pressure.                                              |
| [`Preferences.md`](Preferences.md)       | The owner's interests, tastes, media, food and lifestyle, tools, aesthetics, and dislikes: the topical likes that personalize suggestions, distinct from how they like to be worked with (Working Style) and their competencies (Skills).                                                                     |
| [`README.md`](README.md)                 | This file.                                                                                                                                                                                                                                                                                                    |
| [`Relationships.md`](Relationships.md)   | The owner's relational self and social world: family and household structure, the roles they hold, their social network, attachment and relational style, and key contacts. The individual people themselves live in Memory; this holds the relational self.                                                  |
| [`Working Style.md`](<Working Style.md>) | How the owner likes to work with anyone who works with them, a person or an AI: how to address them, the do's, don'ts, tone, length, and format rules followed in every reply, plus communication, terminology, feedback, and decision style. The facet acted on most.                                        |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch.

---

<div align="center">

**Their words, their yes, their profile.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
