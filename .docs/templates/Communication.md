<!--
title: '💬 COMMUNICATION FORMATS'
description: 'The formats for meeting notes and status updates written in this repository''s issues, discussions and pull requests, and where each kind of message goes. A meeting in the owner''s own life is a Memory event, and a project''s progress goes in its Log, never these.'
type: 'template'
keywords: ['meeting notes', 'status update', 'issues', 'discussions', 'pull requests', 'template']
-->

<!-- On copying: paste the format you need into the issue, the discussion or the pull request it belongs to, and replace every [bracketed] placeholder; none of these is copied to a file. A meeting or an event in the owner's own life is a Memory event, made from Memory/.template/Event.md; a project's progress goes in its Log.md, and a venture's in its own Log.md; a decision about the vault is an ADR in .docs/adrs/. Keep the owner's personal context out of an issue or a discussion on a public repository. Delete this note from the copy. -->

<div align="center">

# 💬 COMMUNICATION FORMATS

<a name="top"></a>

**Short formats for the notes and updates written in issues, discussions and pull requests.**

_Say what changed, what comes next and what is in the way._

</div>

---

## 📅 Meeting Notes

For a call about the repository's work, posted to the issue or the discussion it concerns:

```markdown
### [Meeting name] - [YYYY-MM-DD]

- **Participants**: [@handle, @handle]
- **Objective**: [What the meeting was for]
- **Decisions**:
  - [Decision]
- **Action items**:
  - [ ] [@handle]: [Task]
```

---

## 💓 Status Update

For a change that takes more than a day, posted to its issue or its draft pull request:

```markdown
### Status: [The change] - [YYYY-MM-DD]

- **State**: [On track / At risk / Blocked]
- **Done**: [What landed since the last update]
- **Next**: [What comes next]
- **Blocked by**: [What is in the way, or nothing]
```

---

## 📣 Who Hears About A Change

- **The owner** is told which files changed and what is not yet committed, at the end of every
  task, as the root [`README.md`](/README.md) says under What Done Means.
- **Everyone who uses the template** reads each version's release notes; a change that asks them to
  act is also announced in Discussions, under Announcements, where Discussions are switched on.
- **A decision about the vault** is recorded as an ADR in `.docs/adrs/`, made from the
  [ADR form](/.docs/templates/ADR.md), and linked from the pull request that carries it.

---

## 🧰 Where Each Conversation Goes

- **Issues**: a problem or a request, opened from one of the forms.
- **Discussions**: questions and ideas, where they are switched on.
- **Pull requests**: every change, with a summary of what changed and why.
- **Memory and the Log**: in a vault, what happened in the owner's own world, never an issue.

### 🔗 See also

> [!TIP]
> [`SUPPORT.md`](/.github/SUPPORT.md) says which channel answers which question. Every canonical
> guide is indexed in the
> [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**Written once, where the next reader will look.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
