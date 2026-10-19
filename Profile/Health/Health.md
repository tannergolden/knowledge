<!--
title: "Health"
description: "Stable health attributes and accessibility needs that affect how the AI should help. For AI awareness, not diagnostic use; surfaced only when directly relevant. Conditions are isolated as their own sensitive entries."
type: "reference"
keywords: ["wellbeing", "accessibility", "conditions", "needs", "accommodations", "how to help"]
-->

# 🩺 Health

Stable health attributes and accessibility needs, kept only insofar as they change **how the AI should help**. This is for AI awareness, **not diagnostic use**, and is surfaced only when directly relevant to the task (`Profile/Profile.md`, Rules). It is not a medical record. Each specific condition is isolated in its own entry so that a benign query never drags in a diagnosis; this page holds only the always-useful summary.

## Snapshot

A terse, general line on health status, only if it bears on how to help. Fill last.

## Implications for How to Help

The part the AI actually uses: how to pace, format, or adapt help, and what to avoid. Keep it minimal and considerate.

## Conditions & Needs

One terse entry per condition or accessibility need, isolated for privacy. Add one by copying `Profile/.template/Health Condition.md` here as `<Title>.md`; `update-vault.py` keeps the list below.

<!-- brain:profile-entries (drawn by .github/scripts/update-vault.py - do not edit by hand) -->
_None recorded yet._
<!-- /brain:profile-entries -->

## Medical History

The durable medical background the AI should be aware of: allergies, significant past conditions and surgeries, current medications and supplements, immunizations, and relevant family medical history. Terse, for awareness, not a clinical record. Sensitive.

## Insurance & Advance Directives

Health insurance (carrier and coverage, by reference) and any advance directives - living will, healthcare proxy, DNR - their existence and location only (estate-side documents live in `Profile/Finances/`). Pointers, never contents.
