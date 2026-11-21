# I code with AI

<div class="hk-facts" markdown>
<div markdown>
**For**

Developers using Claude Code, Codex, OpenCode, or Copilot.
</div>
<div markdown>
**Time**

About 15 minutes to start, about a week to try it.
</div>
<div markdown>
**You take away**

A repository where AI follows your rules and checks its own work.
</div>
</div>

<div class="hk-onmap" markdown>
On the map: <span class="hk-chip">1 Guide</span> → <span class="hk-chip">2 Template</span> → <span class="hk-chip">3 Real work</span> → <span class="hk-chip">4 Harness Lab</span> <span class="hk-chip is-off">Company Brain</span> <span class="hk-chip is-off">Observatory</span>
</div>

<div class="hk-steps" markdown>

<div class="hk-step" markdown>

### 1. Understand the loop

<p class="hk-meta">Guide · about 10 minutes of reading</p>

Understand, plan or design when needed, execute, test, verify, review, learn. The ceremony follows the risk: a typo needs no design, a new subsystem does. Most of the value comes from a few habits, not from a long list of skills.

[The working loop](../patterns/working-loop.md)

</div>

<div class="hk-step" markdown>

### 2. Copy the starter kit into your repo

<p class="hk-meta">Template · about 15 minutes · works in a repository you already have</p>

Three kinds of things, nothing more: short rules, a small memory, and one command that can fail.

```text
your-repo/
├── AGENTS.md          short rules + "how big is the task?" table
├── CLAUDE.md          one line pointing to AGENTS.md
├── memory/            context · learnings · patterns
├── docs/adr/          one-page decision records
├── docs/plans/        approved plans
├── <tool>/skills/     the 7 starter skills
└── make check         or the command that already verifies your project
```

| If the task is... | Use |
| --- | --- |
| Small and clear | Direct change, then verify |
| Bounded | Quick brainstorm, then plan and execute |
| New or ambiguous | Approved design, then plan, then execution |

!!! info "Evidence level: reference implementation"
    In the Harness Lab every run carried 25 skills, and across 18 runs on six models the agents opened only 3. A production backend (anonymized) went from 27 flat skills to 9 entry points and cut its generated instructions by 19%. Small samples: read them as signals, not laws.

[Minimal setup](../start-here/minimal-setup.md)

</div>

<div class="hk-step" markdown>

### 3. Use it for about a week

<p class="hk-meta">Real work · your real tasks</p>

Work as usual, but route each task by its size. Every time the AI makes the same mistake twice, add one entry to `memory/learnings.md`: the fact, why it matters, and how to apply it next time. That list is your next harness change.

[State and continuity](../concepts/state-and-continuity.md)

</div>

<div class="hk-step" markdown>

### 4. Check your harness, then measure the skill you doubt

<p class="hk-meta">Harness Lab · start with the checklist</p>

Go through the eight-item health checklist by reading your repository. For the automated version, clone the lab and point it at your project:

```bash
git clone https://github.com/marcosdh1987/ai-agentic-harness-lab
cd ai-agentic-harness-lab
make harness-check REPO=../your-project
```

It needs `git`, `uv`, and `make`; no Docker and no model. Each run takes about 30 seconds. If you doubt a skill, the lab compares it against not having it, on the same case.

[Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md)

</div>

</div>

!!! success "You finished the route"
    If you are the one pushing this in your team, continue with [I lead a team](lead-a-team.md) or [I improve the system](improve-the-system.md).
