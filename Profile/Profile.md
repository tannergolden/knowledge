---
title: "Profile - Folder Information"
description: "Who the user is: the stable self (Biography, Personality, Values, Goals, Skills, Preferences, Working Style, Health) plus the dynamic Focus layer. The foundation for personalized, contextually appropriate responses, and how the AI reads and writes it with discretion."
status: "active"
tags: ["profile", "information", "timeless"]
aliases: ["Identity", "Self", "About Me"]
keywords: ["who the user is", "personal profile", "stable self", "personalization", "identity layer", "how ai uses profile", "user manual of me", "discretion"]
created: 2026-06-19
updated: 2026-10-19
type: "information"
folder: "profile"
layer: 1
policy: false
author: "Tanner Golden"
path: "BRAIN/Profile/Profile.md"
id: "id-profile"
---

# 🪪 Profile/

> [!abstract] What this folder is
> Everything the AI needs to understand **who the user is as a person**, and the foundation for personalized, contextually appropriate responses. These files are a **personal profile, not reference material.** Treat them with discretion: absorb them as context, never quote them back, and let them inform behavior rather than serve as a checklist to work through.

`Profile/` is the **stable self**: the durable, slowly-changing facts about who the user is. It is organized the way personality and identity are described in both psychology and modern AI personalization research - **by facet of the self** (background, traits, values, goals, skills, tastes, working style, health) - with one dynamic exception, [[Profile/Focus|Focus]], for what is true only right now.

## The `profile` Folder tag

Every file here carries `folder: "profile"` and the `profile` Folder tag (Constitution 7.1). The facet files describing the user carry the File Role `self` (`type: "self"`); the hub, index, and templates use their usual roles (`information`, `index`, `template`). Ids use the `id-` prefix.

## The facets

| Facet | Holds | When to read |
|-------|-------|--------------|
| [[Profile/Working Style\|Working Style]] | How the AI should respond and how the user collaborates: do's, don'ts, tone, length, format, feedback and decision style | Every session (`startup`) |
| [[Profile/Biography\|Biography]] | Life history and facts: name, location, work, education, family, formative years, life story | When biographical context helps |
| [[Profile/Personality\|Personality]] | Traits, temperament, cognitive and working style, character strengths, behavior under pressure | To calibrate tone, pacing, depth |
| [[Profile/Values/Values\|Values]] | Core values, ethics, purpose, life philosophy, and held beliefs (sensitive entries) | When helping with decisions |
| [[Profile/Goals/Goals\|Goals]] | Enduring aspirations and direction (the stable "what I am working toward") | When advising on direction |
| [[Profile/Relationships\|Relationships]] | The relational self: family and household structure, roles, social network, attachment and relational style (the people themselves are in Memory) | When relationships matter |
| [[Profile/Finances\|Finances]] | The personal financial picture: situation, assets and liabilities, money style, estate pointers (sensitive) | When money or planning is involved |
| [[Profile/Lifestyle\|Lifestyle]] | How the user lives: daily rhythm, sleep, diet, exercise, substances, environment, recreation | When daily life is relevant |
| [[Profile/Skills/Skills\|Skills]] | Competencies and the per-domain expertise map the AI uses to calibrate explanation depth | When calibrating how much to explain |
| [[Profile/Preferences\|Preferences]] | Interests, tastes, tools, lifestyle, likes and dislikes | When personalizing suggestions |
| [[Profile/Health/Health\|Health]] | Stable health attributes and accessibility needs that affect how to help (sensitive) | Only when directly relevant |
| [[Profile/Focus\|Focus]] | The **dynamic** layer: current priorities, routines, and current life chapter | When acting on current context |

## How to use Profile/

- **Read [[Profile/Working Style|Working Style]] first.** It carries direct instructions for how the AI should behave and is loaded at every session start.
- Use [[Profile/Focus|Focus]] for current priorities and situational context; it changes often, so trust it over older notes and refresh it when you use it.
- Calibrate with [[Profile/Personality|Personality]] (tone, pacing, depth) and [[Profile/Skills/Skills|Skills]] (explanation depth per domain).
- Weigh options with [[Profile/Values/Values|Values]] and [[Profile/Goals/Goals|Goals]].
- **Never treat these files as a checklist.** Absorb them as context and apply naturally.
- **Surface, do not silently write:** when you learn something new about the user, propose adding it (Article 4.2 below) rather than editing on your own.

## Profile vs. the other layers

`Profile/` is the **single home for who the user is** (Constitution 2.7): background, personality, values, preferences, skills, beliefs, goals, and health, whether the user stated it or the AI observed it. A fact about the user lives in exactly one place, and that place is `Profile/`.

- **Memory** holds only what Profile cannot: what happened (sessions, the Log, Events), who is around the user (Entities/People), what they decided (Decisions), and when things occur (Dates). When the AI learns something about the user *themselves*, it proposes a `Profile/` edit; it never stores a parallel copy in Memory.
- **Ventures** holds business context and business contacts; `Profile/` is the *personal* self.
- **Library** holds general and world knowledge; `Profile/` is never reference material (Article 6.1).
- **Projects** holds project execution and tasks; `Profile/` holds the person, not the work.

## Stable vs. dynamic

Every facet except [[Profile/Focus|Focus]] is **stable**: traits, values, and background that hold over months and years. `Focus/` is the deliberate **dynamic** layer - current priorities, routines, and the current life chapter - and it is the pressure-release valve that keeps the rest of the profile timeless. A standing goal is a `Goals/` fact; this week's priority is a `Focus/` fact. When in doubt, ask: would this still be true in a year? If yes, it is stable; if no, it is Focus (or it belongs in Memory or Projects).

## Provenance and freshness

Profile entries carry their origin and stay fresh by use, not by schedule. The convention is deliberately lightweight - it operationalizes Article 4.2 without adding any frontmatter field:

- **Self-reported is the default.** Anything the user states needs no marker; a plain entry is a self-reported fact.
- **Mark what the AI infers.** When the AI writes an entry it inferred rather than one the user stated, it appends an inline HTML comment, which renders invisibly in Obsidian reading view but stays in the source:
  `**Field:** value <!-- observed 2026-06-19 · confidence: low|medium|high · unconfirmed -->`
  On the user's confirmation, shorten it to `<!-- confirmed 2026-06-19 -->` or drop it (a confirmed fact is just a fact). An entry left `unconfirmed` is a proposal awaiting approval, never treated as established (Articles 4.1, 4.3).
- **Refresh on use, not on a calendar.** When you use a section and it still holds, it is current; when something is stale, fix it then. For a drift-prone section (occupation, current chapter), you may stamp `<!-- reviewed 2026-06-19 -->` at its end when you confirm it.

**Standardized provenance vocabulary.** The marker tokens are fixed so they stay machine-filterable across the whole layer: a state token (`observed` | `confirmed` | `reviewed`) with an ISO date, an optional `confidence: low | medium | high`, and the proposal flag `unconfirmed`. The lifecycle is `observed` + `unconfirmed` (an AI inference, a proposal) -> `confirmed` (the user approved it) -> `reviewed` (re-verified later). Because the tokens are fixed, the profile is queryable: a search for `unconfirmed` lists every pending proposal, and one for `confidence: low` surfaces the weakest inferences to re-check. Self-reported facts stay unmarked, so a marker only ever appears on an exception.

## Sensitivity

The whole `Profile/` tree is **sensitive by default** (Article 7.5): every content file carries the `sensitive` tag (the structural hub, index, and templates do not, as they hold no personal data). Discretion is behavioral, enforced when surfacing, not by hiding files: do not surface this information unless directly relevant to the task (Article 4.4). The most private facts - health, beliefs, relationships - are **isolated into their own entry files** so that a benign query never drags them in; the per-entry granularity is itself the privacy control. Keep the most sensitive entries terse and factual: record the minimum the AI needs to be considerate, not a full record.

## Design: facet overview + entries

Facets come in two shapes, the same split as `Memory/`. A facet read as a whole is a single **flat file** at `Profile/` root (Biography, Personality, Preferences, Working Style, Focus). A facet that accretes many independent items is a **folder** with a namesake overview doc plus one **entry file per item** (Values holds belief entries; Goals, Skills, and Health hold one entry per goal, skill, or condition). A flat facet is promoted to a folder only if it later grows entries (for example, Biography gaining life-chapter entries) - never speculatively (Constitution 1.3). Write each independently-answerable fact as its own `## H2` so it chunks cleanly for retrieval, restate the subject in the heading, and keep discrete facts in tables and lists. Discovery is by folder path plus `keywords`, never per-file content tags (Article VII).

## Filling these files: the `/identify` skill

The recommended way to populate or deepen these files is the **`/identify`** skill, not hand-editing. It reads what each file currently holds, targets what is thin or unconfirmed, and interviews the user with structured questions drawn from validated frameworks - **Big Five** for Personality, **Schwartz's basic values** for Values, the **McAdams life-story** method for Biography - mixing direct questions for facts with indirect ones that surface traits the user would not think to state. It writes inferences **marked, evidence-cited, confidence-rated, and left unconfirmed until approved**, covers sensitive topics with skip options and the `sensitive` tag, and commits each file's last state before writing to it. Hand-editing is fine for a quick correction but misses the inference layer and those safeguards.

## Article IV (Delegated) - Identity & Privacy Rules

Hosted here from the Constitution with full constitutional force (Constitution Article IV; amendments only per Article VIII). These rules govern every write to `Profile/` and to `Memory/`.

**4.1 Profile Files Are Read-Only by Default**
The AI should treat files in `Profile/` as read-only unless the user explicitly asks it to update them. These files represent the user's own self-description and should not be modified based on the AI's inferences alone.

**4.2 Inferences Must Be Flagged**
If the AI learns something about the user through conversation that it believes belongs in a Memory or Profile file, it should surface the observation explicitly rather than writing it silently:
> *"I noticed [X] - want me to add that to [file]?"*

**4.3 No Cross-Session Speculation**
The AI must not speculate about or record assumptions about the user that are not grounded in direct observation or explicit statement. Profile and Memory files must contain facts, not inferences presented as facts.

**4.4** remains in the root Constitution - sensitive-category discretion is universal law, not folder law.
