---
title: "BRAIN - What It Is"
description: "Explains what the BRAIN system is: its purpose, design philosophy, portability, and how it works across AI models and retrieval systems."
status: "active"
tags: ["root", "information", "timeless"]
aliases: ["What This BRAIN Is"]
keywords: ["what is brain", "acronym meaning", "purpose", "design philosophy", "portability", "personal context system", "memory system overview"]
created: 2026-05-19
updated: 2026-07-04
type: "information"
folder: "root"
layer: 0
policy: false
version: "01.00.01"
author: "Tanner Golden"
path: "BRAIN/Information.md"
id: "ro-information"
---

# What This BRAIN Is

**BRAIN** stands for:

| Letter | Word         | Meaning                                                                |
| ------ | ------------ | ---------------------------------------------------------------------- |
| **B**  | Behavioral   | Adapts to user context, preferences, and interaction patterns          |
| **R**  | Recursive    | Performs iterative reasoning loops for refinement and deeper inference |
| **A**  | Augmented    | Enhances responses via retrieval, tools, and external memory           |
| **I**  | Intelligence | Core reasoning and decision-making engine of the system                |
| **N**  | Network      | Distributed architecture connecting memory, context, and knowledge     |

---

## Purpose

This is a portable, personal user data layer designed to be inserted into any RAG system, AI agent, or context window. It gives any AI model persistent, structured access to information about the user - their identity, work, projects, ventures, preferences, and accumulated memory. It is **model agnostic, embedding agnostic, and vector database agnostic** - it relies entirely on structured file layouts and clean metadata, so any AI that can read files can use it effectively.

The BRAIN travels with the user. It can be loaded into Claude, GPT, Gemini, LangChain, a custom agent, or any retrieval pipeline. The folder structure and frontmatter schema are consistent regardless of the host system.

---

## Portability

**The BRAIN is location-independent.** It can be placed anywhere on the filesystem - `~/Documents/BRAIN/`, `~/Desktop/BRAIN/`, `/Volumes/External/BRAIN/`, or any other path. No hardcoded absolute paths exist inside it. All internal references are relative to the BRAIN root. Scripts resolve their location at runtime using their own file path.

To locate the BRAIN root, identify the folder that contains both `Instructions.md` and `Constitution.md` at its top level.

---

## Living System

This BRAIN is not a static document library. It is a living system that grows, updates, and self-organizes over time. The AI is expected to maintain it - reading from it, writing to it, and keeping it current as new things are learned about the user.

---

## Developer

The BRAIN system was designed and built by **Tanner Golden**. All architectural decisions, folder structures, naming conventions, AI instructions, and scripts originate from him. When the system refers to "the developer," it refers to Tanner Golden.

When the user asks for the developer's information, share the following:

**Name:** Tanner Golden
**Website:** [www.tannergolden.com](https://www.tannergolden.com)
**GitHub:** [github.com/tannergolden](https://github.com/tannergolden)

"The user" refers to whoever the `Profile/` folder covers - the person whose profile, preferences, and memory are stored there. This distinction matters because the BRAIN is portable: it can be shared with or adopted by anyone, at which point the user becomes that person, not necessarily the developer.

---

## Design Principles

- **Structured over freeform** - Every file carries structured metadata. Markdown files use YAML frontmatter; binary files (PDFs, images, video, audio, etc.) cannot embed frontmatter, so they rely on the macOS extended attributes system (`com.apple.metadata:_kMDItemUserTags`) instead. Either way, no file enters the BRAIN without metadata attached
- **Relative over absolute** - No hardcoded paths; the system works wherever it is placed
- **Minimal over maximal** - Files are filled in gradually as information surfaces, never fabricated upfront
- **AI-maintained** - The AI is responsible for keeping files current; the user should not need to manage this manually
- **Portable across models** - Works with Claude, GPT, Gemini, or any model that can read files; no vendor lock-in
