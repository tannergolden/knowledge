---
title: "Visualize - Skill Information"
description: "BRAIN documentation node for the visualize skill: dispatches the Design team to turn data, structure, and ideas into honest, legible visuals, rendered inline. Use when the user wants a chart, diagram, dashboard, interactive widget, or explanatory illustration."
status: "active"
tags: ["system", "information", "timeless"]
aliases: ["/visualize"]
keywords: ["visualization skill", "charts", "diagrams", "dashboards", "data visualization", "graphical integrity", "design team"]
created: 2026-06-28
updated: 2026-06-28
type: "information"
folder: "system"
layer: 4
policy: false
author: "Tanner Golden"
path: "BRAIN/System/Skills/.unpackaged/visualize/Visualize.md"
id: "sy-skill-visualize"
---

# 📊 Visualize - Information Guide

## What this skill does

Visualize turns data, structure, and ideas into finished visuals: statistical charts, diagrams, interactive widgets, and explanatory illustration, rendered inline and saved only when the owner asks to keep one, into a named home or the held visuals library at `Inbox/Visuals/`. It holds one overriding standard, graphical integrity: the visual never distorts what is true, and a beautiful chart that lies fails. Legibility and accessibility are the craft rule beneath it.

## How it fits the architecture

The skill composes the standing **Design team** (`metadata.team: Design`, at `Inbox/Faculties/Design/`): the Design Lead (Margot) frames the request and picks the visual form, the Visualization Designer (Otto) makes the artifact, and the Design Critic (Vera) is the independent reviewer and blocking accessibility gate. It is the fifth BRAIN faculty, "show," alongside Research (find), Discovery (ideate), Development (build), and Editorial (write). The skill carries no agents of its own; it references the team by name and vendors the agents in only at Publish.

## Design basis

Built fresh on the federated-team architecture (the deprecated pre-team `visualize` left no source to restore). Grounded in a research pass over the established visualization authorities, Tufte (graphical integrity, the lie factor, the data-ink ratio, chartjunk), Cleveland and McGill (the perceptual-accuracy ranking), Munzner, Bertin, Few (dashboards), Shneiderman (the visual information-seeking mantra), and WCAG 2.2 (contrast and color-independence thresholds), plus an adversarial design review that replaced an initial "truthful at a glance" standard with graphical integrity and collapsed a six-role roster to a lead plus two. The durable synthesis lives in `references/principles.md`. Format and inline-craft research (the renderable formats, hand-authored SVG, interactive HTML and charting libraries, and cross-cutting inline aesthetics) lives in `references/formats.md`, `references/svg-craft.md`, `references/interactive.md`, and `references/inline-aesthetics.md`. A curated library of about 87 established data-visualization palettes (ColorBrewer, viridis, Tableau, Plotly, CARTOColors, Paul Tol, Okabe-Ito), with picking doctrine, is in `assets/palettes.json` and `references/palette.md`.
