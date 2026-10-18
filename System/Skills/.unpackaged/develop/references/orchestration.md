# Orchestration - dispatching the Development

How develop dispatches the Development team, the BRAIN's engineering team, without misfires. Develop briefs the Development team's Software Architect, Full-Stack Engineer, QA Engineer, and Application Security Engineer as fresh-context subagents per build. Dispatch scaling (who runs at which complexity) is in SKILL.md; this is the contract for how each dispatch is shaped. Read it before the first dispatch of a build.

## The self-contained brief

A subagent sees none of this conversation. Every dispatch brief restates, in full: the **objective** (the one job and the success test), the **output contract** (the exact artifact shape and the absolute path to write it to), the **inputs** (every path to read), the **tools and sources** to use, and the **boundaries** (what not to do, what to flag and stop on). An incomplete brief is the single most common dispatch failure: the worker improvises the gap.

Fill every field on every dispatch; an omitted field is precisely the gap that gets improvised:

```
ROLE: read <agent spec path>. You are the <role>.
OBJECTIVE: <the one job> - you are done when <success test>.
INPUTS: read <absolute paths>. Assume <X>; flag and stop if <Y> is missing.
OUTPUT: write <artifact> to <absolute path>; return a summary of at most <N> lines.
TOOLS / SOURCES: <what to use, what to prefer>.
BOUNDARIES: never <forbidden action>. Write-scope: <what it may write>.
```

## Only the orchestrator spawns

Develop is the only one that dispatches. Subagents never spawn subagents; all fan-out happens at the top, where the full picture lives. A worker that needs more work done returns a flag, and develop dispatches the follow-up.

## The filesystem is the artifact bus

Each phase writes its artifact to the run workspace; the next phase reads it from disk. Workers return a short summary (status, artifact path, key decisions, flags), never a file dump. Passing artifacts inside chat messages loses detail in transit; the file is the source of truth.

## Scale the dispatch, and parallelize only the independent

A multi-agent run costs about 15x a single agent, so dispatch is scaled to the build, not reflexive. Parallelize genuinely independent work (separate finders, separate dimension reviews); keep interdependent authoring sequential, because parallel generation does not suit work where each part depends on the others.

## The fix loop

A validator error or a NEEDS-FIX audit resumes the builder on the cited issues only. Re-run `brain.command skill validate` always; re-audit only the cited items with a fresh reviewer. If the same error survives two rounds, stop and surface a likely requirement-level conflict rather than looping.

## Independence is structural, not requested

The QA Engineer and the Application Security Engineer are fresh-context reviewers who never touch the build (the QA Engineer runs the validator and tests via Bash; neither holds Write) and never read the builder's notes, so a reviewer cannot fix-and-rubber-stamp its own work. Never "now check your work"; always a separate, fresh-context invocation. That separation is the main quality lever and must not be collapsed for speed.

## When the Agent tool is unavailable

Where the Agent tool is unavailable, run the same role specs sequentially in this one context with role headers, and tell the user the independent-review guarantee is weakened: a single context cannot give the auditor fresh eyes. This single-context mode is the fallback, never the default. Running inline without a standing crew is still the default, because the fresh-context reviewer is the main quality lever and a separate subagent is what makes it fresh.
