<!--
title: "Profile - Folder Information"
description: "Who the user is: the stable self (Biography, Personality, Values, Goals, Skills, Preferences, Working Style, Health) plus the dynamic Focus layer. The foundation for personalized, contextually appropriate help, and how it is read and written with discretion."
type: "index"
keywords: ["identity", "self", "about me", "who the user is", "personal profile", "stable self", "personalization", "identity layer"]
-->

# 🪪 Profile/

Who the user is, facet by facet, with `Working Style.md`, read at the start of every session, saying how they want to be helped. In the public template every facet is a blank scaffold; in a vault generated from it, which stays private, these are the most personal notes it holds. Read this README before changing anything in this folder; its rules add to the root `README.md` and never loosen it.

## Rules

These govern every write to `Profile/`, and every write to `Memory/` that touches who the user is.

- **Read-only by default.** Every note here is read-only unless the user asks for an update: it is their own description of themselves, and never changes on inference alone.
- **Propose, never write silently.** Something learned about the user that belongs here or in `Memory/` is proposed first, as a question: _"Noticed: [X]. Add it to [file]?"_
- **Facts, not guesses.** Only what the user said, or what was observed directly, is recorded. Nobody speculates about them across sessions or presents an inference as a fact: a proposed inference carries its marker and stays `unconfirmed` until approved (Provenance and freshness, below).
- **One home for who the user is.** A fact about them lives here and only here, never copied into `Memory/`.
- **The most care for sensitive categories.** Health and medical conditions, finances, relationships, political or religious views, legal matters and mental health: surface them only when the task needs them, in any folder. Absorb a profile as context; never quote it back.

> [!NOTE]
> **What this folder is.**
> Everything needed to understand **who the user is as a person**, and the foundation for personalized, contextually appropriate help. These files are a **personal profile, not reference material.** Treat them with discretion: absorb them as context, never quote them back, and let them inform behavior rather than serve as a checklist to work through.

`Profile/` is the **stable self**: the durable, slowly-changing facts about who the user is. It is organized the way personality and identity are described in both psychology and modern AI personalization research - **by facet of the self** (background, traits, values, goals, skills, tastes, working style, health) - with one dynamic exception, [[Profile/Focus|Focus]], for what is true only right now.

## What Lands Here

Every write here follows the Rules above, whichever skill makes it:

- **The `human-resources` skill's work for the user's own life**: the profile interview (Filling These Files, below), their career and skills (`Biography.md`, `Skills/`, `Goals/`) and their health and wellbeing (`Health/`, `Lifestyle.md`).
- **The `finance-and-accounting` skill's money facts** about the user, in `Finances.md` alone: the picture and pointers, never a secret number.
- **What any other skill learns about who the user is**, proposed first: a goal or priority the `administration` skill helps set (`Goals/`, `Focus.md`), where a will or a lease the `legal-and-compliance` skill handles is kept (`Finances.md`, Legal & Estate), the routines `operations-and-logistics` plans (`Focus.md`), and the devices, accounts and tools `information-technology` sets up (`Preferences.md`), never a password or a key.

## Frontmatter here

The facet files describing the user carry `type: "reference"`; this hub carries `index`, and the scaffolds `template` (`.docs/technical/vault/Note-Schema.md`). No field marks a file personal: everything under `Profile/` is personal by its path (`.docs/technical/vault/Keywords.md`).

## The facets

| Facet | Holds | When to read |
|-------|-------|--------------|
| [[Profile/Working Style\|Working Style]] | How the user wants to be helped and how they collaborate: do's, don'ts, tone, length, format, feedback and decision style | Every session (a startup note) |
| [[Profile/Biography\|Biography]] | Life history and facts: name, location, work, education, family, formative years, life story | When biographical context helps |
| [[Profile/Personality\|Personality]] | Traits, temperament, cognitive and working style, character strengths, behavior under pressure | To calibrate tone, pacing, depth |
| [[Profile/Values/README\|Values]] | Core values, ethics, purpose, life philosophy, and held beliefs (sensitive entries) | When helping with decisions |
| [[Profile/Goals/README\|Goals]] | Enduring aspirations and direction (the stable "what I am working toward") | When advising on direction |
| [[Profile/Relationships\|Relationships]] | The relational self: family and household structure, roles, social network, attachment and relational style (the people themselves are in Memory) | When relationships matter |
| [[Profile/Finances\|Finances]] | The personal financial picture: situation, assets and liabilities, money style, estate pointers (sensitive) | When money or planning is involved |
| [[Profile/Lifestyle\|Lifestyle]] | How the user lives: daily rhythm, sleep, diet, exercise, substances, environment, recreation | When daily life is relevant |
| [[Profile/Skills/README\|Skills]] | Competencies and the per-domain expertise map that calibrates how much to explain | When calibrating how much to explain |
| [[Profile/Preferences\|Preferences]] | Interests, tastes, tools, lifestyle, likes and dislikes | When personalizing suggestions |
| [[Profile/Health/README\|Health]] | Stable health attributes and accessibility needs that affect how to help (sensitive) | Only when directly relevant |
| [[Profile/Focus\|Focus]] | The **dynamic** layer: current priorities, routines, and current life chapter | When acting on current context |

## How to use Profile/

- **Read [[Profile/Working Style|Working Style]] first.** It says how the user wants to be helped, and is read at every session start.
- [[Profile/Focus|Focus]] holds current priorities and situational context; it changes often, so it outranks older notes and is refreshed when used.
- [[Profile/Personality|Personality]] calibrates tone, pacing and depth, and [[Profile/Skills/README|Skills]] the explanation depth per domain.
- [[Profile/Values/README|Values]] and [[Profile/Goals/README|Goals]] weigh options.
- **These files are never a checklist.** They are absorbed as context and applied naturally.
- **Propose, never write silently:** something new learned about the user is proposed (Rules, above), never written on inference alone.

## Profile vs. the other layers

`Profile/` is the **single home for who the user is** (Rules, above): background, personality, values, preferences, skills, beliefs, goals, and health, whether the user stated it or it was observed. A fact about the user lives in exactly one place, and that place is `Profile/`.

- **Memory** holds only what Profile cannot: what happened (sessions, the Log, Events), who is around the user (Entities/People), what they decided (Decisions), and when things occur (Dates). Something learned about the user *themselves* is proposed as a `Profile/` edit; a parallel copy is never stored in Memory.
- **Ventures** holds business context and business contacts; `Profile/` is the *personal* self.
- **Library** holds general and world knowledge; `Profile/` is never reference material (`Library/README.md`, Rules).
- **Projects** holds project execution and tasks; `Profile/` holds the person, not the work.

## Stable vs. dynamic

Every facet except [[Profile/Focus|Focus]] is **stable**: traits, values, and background that hold over months and years. `Focus/` is the deliberate **dynamic** layer - current priorities, routines, and the current life chapter - and it is the pressure-release valve that keeps the rest of the profile timeless. A standing goal is a `Goals/` fact; this week's priority is a `Focus/` fact. When in doubt, ask: would this still be true in a year? If yes, it is stable; if no, it is Focus (or it belongs in Memory or Projects).

## Provenance and freshness

Profile entries carry their origin and stay fresh by use, not by schedule. The convention is deliberately lightweight - it puts the Rules' propose-first into practice without adding any frontmatter field:

- **Self-reported is the default.** Anything the user states needs no marker; a plain entry is a self-reported fact.
- **Mark what is inferred.** An entry inferred rather than stated by the user carries an inline HTML comment, which renders invisibly on GitHub and in any Markdown preview but stays in the source:
  `**Field:** value <!-- observed 2026-06-19 · confidence: low|medium|high · unconfirmed -->`
  On the user's confirmation, shorten it to `<!-- confirmed 2026-06-19 -->` or drop it (a confirmed fact is just a fact). An entry left `unconfirmed` is a proposal awaiting approval, never treated as established (Rules, above).
- **Refresh on use, not on a calendar.** A section that still holds when it is used is current; something stale is fixed then. A drift-prone section (occupation, current chapter) may carry `<!-- reviewed 2026-06-19 -->` at its end once it is confirmed.

**Standardized provenance vocabulary.** The marker tokens are fixed so they stay machine-filterable across the whole layer: a state token (`observed` | `confirmed` | `reviewed`) with an ISO date, an optional `confidence: low | medium | high`, and the proposal flag `unconfirmed`. The lifecycle is `observed` + `unconfirmed` (an inference, a proposal) -> `confirmed` (the user approved it) -> `reviewed` (re-verified later). Because the tokens are fixed, the profile is queryable: a search for `unconfirmed` lists every pending proposal, and one for `confidence: low` surfaces the weakest inferences to re-check. Self-reported facts stay unmarked, so a marker only ever appears on an exception.

## Sensitivity

The whole `Profile/` tree is **sensitive by default**, by its path (`.docs/technical/vault/Keywords.md`): no tag marks it, because the folder already does. Discretion is behavioral, enforced when surfacing, not by hiding files: do not surface this information unless directly relevant to the task (Rules, above). The most private facts - health, beliefs, relationships - are **isolated into their own entry files** so that a benign query never drags them in; the per-entry granularity is itself the privacy control. Keep the most sensitive entries terse and factual: record the minimum needed to be considerate, not a full record.

## Design: facet overview + entries

Facets come in two shapes, the same split as `Memory/`. A facet read as a whole is a single **flat file** at `Profile/` root (Biography, Personality, Preferences, Working Style, Focus). A facet that accretes many independent items is a **folder** whose `README.md` is the facet's overview, plus one **entry file per item** (Values holds belief entries; Goals, Skills, and Health hold one entry per goal, skill, or condition). A flat facet is promoted to a folder only if it later grows entries (for example, Biography gaining life-chapter entries) - never speculatively. Write each independently-answerable fact as its own `## H2` so it chunks cleanly for retrieval, restate the subject in the heading, and keep discrete facts in tables and lists. Discovery is by folder path plus `keywords`, never tags (`.docs/technical/vault/Keywords.md`).

## Filling These Files: The Profile Interview

The recommended way to fill or deepen these files is a structured interview rather than hand-editing, such as the profile interview the `human-resources` skill runs (installed with the home kit from tannergolden/intelligence, not kept in this vault). `python3 .github/scripts/profile-coverage.py --json` scores each facet and names the next one to ask about, starting with `Working Style.md`. The interview reads what each file holds, targets what is thin or unconfirmed, and asks structured questions drawn from validated frameworks: **Big Five** for Personality, **Schwartz's basic values** for Values, the **McAdams life-story** method for Biography, mixing direct questions for facts with indirect ones that surface traits the user would not think to state. What it writes follows the rules on this page: an inference is **marked, evidence-cited, confidence-rated and left unconfirmed until approved**, sensitive topics come with skip options, and each file's last state is committed before it is written. A new entry is copied from `.template/`, whose `README.md` says which scaffold makes what. Hand-editing is fine for a quick correction, but misses the inference layer and those safeguards.

## File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                    | Purpose                                                                                                                                                                                                                                                                                                      |
| :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`.template/`](.template/README.md)      | The Profile scaffolds: a facet overview, a generic entry, and the entries of the folder facets (a belief, a goal, a skill, a health condition, a life chapter). Each is copied on its own, never edited in place.                                                                                            |
| [`Goals/`](Goals/README.md)              | The user's enduring aspirations and direction: the stable, long-horizon goals that define what they are working toward, distinct from this week's priorities.                                                                                                                                                |
| [`Health/`](Health/README.md)            | Stable health attributes and accessibility needs that affect how to help. For awareness, not diagnostic use; surfaced only when directly relevant. Conditions are isolated as their own sensitive entries.                                                                                                   |
| [`Skills/`](Skills/README.md)            | The user's competencies and the per-domain expertise map that calibrates how much to explain: skip the basics where the user is expert, define terms where they are new.                                                                                                                                     |
| [`Values/`](Values/README.md)            | What the user cares about and how they decide what is right: core values, orientation axes, life philosophy, ethics, motivation, purpose, role models, and what they stand for and against, plus held beliefs as sensitive entries.                                                                          |
| [`Biography.md`](Biography.md)           | The user's life facts and life story: name, contact, location, work, education, family, formative years, key events, and the McAdams narrative themes that give the facts meaning.                                                                                                                           |
| [`Finances.md`](Finances.md)             | The user's stable personal financial picture and money-management self: financial situation, assets and liabilities, insurance, risk posture, money style, financial goals, and the existence and location of legal and estate documents. Sensitive; records the picture and pointers, never secret numbers. |
| [`Focus.md`](Focus.md)                   | The dynamic layer: the user's current priorities, how to help right now, routines, current life chapter, and what is on the horizon. Changes often; trust it over older notes and refresh it on use.                                                                                                         |
| [`Lifestyle.md`](Lifestyle.md)           | How the user lives day to day: the stable patterns of sleep, diet, exercise, substances, daily rhythm, rituals, living environment, and recreation. The enduring counterpart to the dynamic Focus layer.                                                                                                     |
| [`Personality.md`](Personality.md)       | How the user thinks, focuses, feels, works, learns, and behaves under pressure: personality typing, Big Five with BFI-2 facets, temperament, cognitive/working/learning style, emotional and social style, strengths, blind spots, and behavior under pressure.                                              |
| [`Preferences.md`](Preferences.md)       | The user's interests, tastes, media, food and lifestyle, tools, aesthetics, and dislikes: the topical likes that personalize suggestions, distinct from the AI-interaction rules in Working Style and competencies in Skills.                                                                                |
| [`README.md`](README.md)                 | This file.                                                                                                                                                                                                                                                                                                   |
| [`Relationships.md`](Relationships.md)   | The user's relational self and social world: family and household structure, the roles they hold, their social network, attachment and relational style, and key contacts. The individual people themselves live in Memory; this holds the relational self.                                                  |
| [`Working Style.md`](<Working Style.md>) | How the AI should respond to the user and how the user collaborates: how to address them, the do's, don'ts, tone, length, and format rules followed every reply, plus communication, terminology, feedback, and decision style. The facet the AI acts on most.                                               |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.
