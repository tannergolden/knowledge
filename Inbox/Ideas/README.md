<!--
title: "Ideas"
description: "The held idea pool: the living library of idea records that discovery work produces. Ideas persist here by lifecycle status (raw, shortlisted, developed, promoted, parked, killed), held and never sorted, so each new idea is checked against the whole pool, killed ideas included, and its lineage traced. The ideation counterpart to the Reports library."
type: "index"
keywords: ["the idea pool", "idea backlog", "ideation pool", "idea pool", "idea records", "ideation", "discovery ideas", "ice elo"]
-->

# 💡 Ideas

The held idea pool. Idea records from discovery work land here, such as the `research-and-development` skill's, one idea per file, by the rules below. It is the ideation counterpart to the Reports library (`Inbox/Reports/`), where Reports holds finished reports and Ideas holds the living raw material that discovery generates and ranks.

## Held, not sorted

Like the Reports library and the Visuals library, the session-start card leaves Ideas out of the sort sweep, so an idea record is never proposed for re-sorting. It stays fully linted and cataloged like any other vault content. Only the loose files at the `Inbox/` root are sorted.

## A living pool, governed by status not time

Unlike Reports (good for three months) and Visuals (archival snapshots), the idea pool is a living competitive selector. An idea persists with a lifecycle status: raw, shortlisted, developed, promoted, parked, or killed. Killed and parked ideas are kept on purpose: every new idea is checked against the whole pool, killed ones included, so a rejected dead end is never re-trodden. Most ideas end killed, by design; the pool is a competitive selector, not an archive of everything. A promoted idea is handed off to its venture or project, and the pool keeps the record and its lineage.

## One idea, one record (the schema lives with the method)

Each idea is one Markdown file, `type: record`, carrying a stable `id`, a short `title`, a one-line `statement`, its `lifecycle`, the `ice` and `elo` scores, the generative `lens` that produced it, `parents` for lineage, and the `serves` path for the venture, project, or topic it is for. The full schema, the ICE and Elo and RICE scoring, the lifecycle gates, and the dedup-and-lineage rules are the discovery method's, defined with the `research-and-development` skill in tannergolden/intelligence rather than in this vault. This folder is the home where the records live; the method is how they are made and scored.

## Idea files are leaves

An idea record links to nothing in the wikilink graph: `parents` are plain ids and `serves` is a plain path. Lineage is reconstructed by querying `id` and `parents`, not by links, and the pool is found by searching this folder. So, unlike the Reports index, this README does not wikilink each idea: the pool can grow to many records, and linking them would clutter the graph, while the leaf design keeps it clean. The pool is browsable by search and by status.

## What goes elsewhere

A finished discovery report, the ranked shortlist with the recommendation, is a deliverable: it goes to the held reports library at `Inbox/Reports/`, not here. This folder holds the idea records, the raw material; the report is the synthesized result. A promoted idea's real home is its venture (`Ventures/`) or project (`Projects/`); the pool retains the record so the lineage and the dedup history never dangle.
