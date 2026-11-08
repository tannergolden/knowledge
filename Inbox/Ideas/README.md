<!--
title: '💡 IDEAS'
description: 'The held idea pool: the living library of idea records that discovery work produces, kept by lifecycle status (raw, shortlisted, developed, promoted, parked, killed) and never sorted, the ideation counterpart to the Reports library. Read it to file an idea, or to check a new one against the whole pool, killed ideas included, and trace its lineage.'
type: 'index'
keywords: ["the idea pool", "idea backlog", "ideation pool", "idea pool", "idea records", "ideation", "discovery ideas", "ice elo"]
-->

<div align="center">

# 💡 IDEAS

<a name="top"></a>

**The held idea pool, where every idea is kept by its lifecycle status.**

_Killed ideas stay, so no dead end is walked twice._

</div>

---

## 💡 What This Folder Is For

The held idea pool. Idea records from discovery work land here, such as the `research-and-development` skill's, one idea per file, by the rules below. It is the ideation counterpart to the Reports library (`Inbox/Reports/`): Reports holds finished reports, and Ideas holds the living raw material that discovery generates and ranks.

---

## 📌 Held, not sorted

Idea records live here and stay here. The session-start sort skips this folder, as it skips the Reports and Visuals libraries (`Inbox/README.md`), so an idea record is never proposed for re-sorting, yet it stays fully linted and cataloged like any other vault file.

---

## 🔄 A living pool, governed by status not time

Unlike Reports (good for three months) and Visuals (archival snapshots), the idea pool is a living competitive selector. An idea persists with a lifecycle status: raw, shortlisted, developed, promoted, parked, or killed. Killed and parked ideas are kept on purpose: every new idea is checked against the whole pool, killed ones included, so a rejected dead end is never re-trodden. Most ideas end killed, by design; the pool is a competitive selector, not an archive of everything. A promoted idea is handed off to its venture or project, and the pool keeps the record and its lineage.

---

## ⚖️ What is filed here, and what goes elsewhere

The idea records, the raw material, are filed here. A finished discovery report, the ranked shortlist with the recommendation, is a deliverable: it goes to the held reports library at `Inbox/Reports/`, not here. A promoted idea's real home is its venture (`Ventures/`) or project (`Projects/`); the pool retains the record so the lineage and the dedup history never dangle.

---

## 🧾 One idea, one record

Each idea is one Markdown file, typed `record`, whose fields sit in the vault's hidden frontmatter: a stable `id`, a short `title`, a one-line `statement`, its `lifecycle`, the `ice` and `elo` scores, the generative `lens` that produced it, `parents` for lineage, and `serves`, in plain text, for the venture, project, or topic it is for. These are fields of the record's kind (`.docs/technical/vault/Note-Schema.md`). The full schema, the ICE, Elo and RICE scoring, the lifecycle gates, and the dedup-and-lineage rules are the discovery method's, defined with the `research-and-development` skill in tannergolden/intelligence rather than in this vault. This folder is the home where the records live; the method is how they are made and scored.

---

## 🍃 Idea files are leaves

An idea record links to nothing in the wikilink graph: `parents` are plain ids and `serves` is plain text. Lineage is reconstructed by querying `id` and `parents`, not by links, and the pool is found by searching this folder. So, unlike the Reports index, this README does not wikilink each idea: the pool can grow to many records, and linking them would clutter the graph, while the leaf design keeps it clean. The pool is browsable by search and by status.

---

<div align="center">

**Rank them all, keep them all.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
