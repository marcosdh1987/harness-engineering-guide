---
hide:
  - toc
---

# Harness Engineering Guide

Work with AI in a way you can trust, measure, and improve, whatever tool or model you use this month. Pick the route that sounds like you: the map lights up the pieces you need, in order.

## Where do I start?

<div id="route-map" class="route-map"></div>

<div class="route-map-fallback" markdown>

<div class="grid cards" markdown>

-   :material-code-braces: **[I code with AI](routes/build-with-ai.md){ data-route="dev" }**

    ---

    For developers.

    1. Understand the loop and why a few skills are enough (about 10 min).
    2. Copy the starter kit into your repo (about 15 min, terminal).
    3. Use it for about a week on real tasks.
    4. Check your harness with the eight-item checklist, then measure the skill you doubt.

-   :material-account-group: **[I lead a team](routes/lead-a-team.md){ data-route="lead" }**

    ---

    For tech leads and managers.

    1. Why the system matters more than the model (about 10 min).
    2. Put decisions, sources, and owners in one place (no code).
    3. Run a pilot: one repo, one loop, one-page decisions (about 2 weeks).
    4. Measure adoption without measuring people.

-   :material-book-open-variant: **[I work with documents, not code](routes/documents-not-code.md){ data-route="docs" }**

    ---

    For PMs, operations, and analysts.

    1. The Knowledge Harness in about 5 minutes.
    2. One recurring question: its sources and who maintains them (no terminal).
    3. Use AI with that context and note what failed (no terminal).

-   :material-flask-outline: **[I improve the system](routes/improve-the-system.md){ data-route="champion" }**

    ---

    For AI champions and Harness Engineers.

    1. Find where it hurts: rework, cost, repeated failures.
    2. Turn the failure into a case and compare v1 against v2 (about 45 min).
    3. Promote what won, one skill at a time.
    4. Share what you learned.

</div>

**The pieces of the ecosystem**

- [Guide](patterns/working-loop.md){ data-node="guide" }: the method. How to work with AI without depending on one tool.
- [Template](start-here/minimal-setup.md){ data-node="template" }: your repo with AI. Rules, skills, and quality gates versioned in the repository.
- [Company Brain](start-here/company-brain-template.md){ data-node="brain" }: shared context. Sources, decisions, provenance, and owners.
- [Real work](patterns/working-loop.md){ data-node="work" }: the loop plus a few skills, every day.
- [Observatory](measure-and-improve/engineering-delivery-observatory.md){ data-node="observatory" }: what happens day to day, measured as a process, never as people.
- [Harness Lab](reference-implementation/ai-agentic-harness-lab/index.md){ data-node="lab" }: does this really help? Two configurations, same case, one verdict.

</div>

<div class="hk-below" markdown>

<div class="hk-loop" markdown>

**The same loop, on every route**

<span class="hk-chip">Understand</span> → <span class="hk-chip">Plan or Design when needed</span> → <span class="hk-chip">Execute</span> → <span class="hk-chip">Test</span> → <span class="hk-chip">Verify</span> → <span class="hk-chip">Review</span> → <span class="hk-chip">Learn</span>

A small change moves through it quickly. A large one asks for a design and a plan. The ceremony follows the risk. See the [working loop](patterns/working-loop.md).

</div>

<div class="hk-honest" markdown>

**What this guide will and will not tell you**

- It gives you a stable method, not the tool of the month.
- It keeps industry evidence, guide recommendations, and facts about the reference repositories apart.
- It measures systems and workflows, never people.
- It is not a runtime or a product: the reference repositories are possible implementations.

</div>

</div>

<script type="application/json" id="route-map-data">
{
  "ui": {
    "question": "Where do I start?",
    "routeFor": "For",
    "openRoute": "Open the full route",
    "tapHint": "Tap a box on the map to see what it is.",
    "what": "What it is",
    "who": "Who it is for",
    "first": "First step",
    "learnTemplate": "what wins in the Lab goes back to the template",
    "learnGuide": "and to the guide",
    "signals": "signals",
    "mapLabel": "Map of the Harness Engineering ecosystem"
  },
  "nodes": {
    "guide": {
      "label": "Guide",
      "sub": "the method",
      "what": "How to work with AI without depending on one tool: context, rules, a few skills, verification, and learning.",
      "who": "Everyone.",
      "first": "Read the working loop (about 10 minutes)."
    },
    "template": {
      "label": "Template",
      "sub": "your repo with AI",
      "what": "ml-python-base: rules, skills, and quality gates versioned in your repository and projected to Claude Code, Codex, OpenCode, and Copilot. Building an agent product? Look at ml-langchain-agent too.",
      "who": "Developers and tech leads.",
      "first": "Copy the starter kit: a short AGENTS.md, seven skills, and one verification command."
    },
    "brain": {
      "label": "Company Brain",
      "sub": "shared context",
      "what": "company-brain-template: sources, decisions, provenance, and owners, in one place that people and AI can read.",
      "who": "Managers, PMs, and teams. You do not need to code to start.",
      "first": "Pick a question your team keeps asking and write down its sources."
    },
    "work": {
      "label": "Real work",
      "sub": "loop + few skills",
      "what": "Everyday work with AI: a routing table tells you when a direct change is enough and when to design first.",
      "who": "Whoever does the work, with or without code.",
      "first": "Use the loop on real tasks for about a week."
    },
    "observatory": {
      "label": "Observatory",
      "sub": "what happens day to day",
      "what": "Signals about flow, quality, and AI usage. It measures the process, never the content and never people.",
      "who": "Managers and AI champions.",
      "first": "Start with the maturity model and the six dimensions."
    },
    "lab": {
      "label": "Harness Lab",
      "sub": "does this really help?",
      "what": "Compares two configurations on the same case (a skill, a model, or a rule) and tells you what won and how confident you can be.",
      "who": "Tech leads and AI champions.",
      "first": "Read the eight-item health checklist against your repo, or clone the lab and run make harness-check (about 30 seconds per run, no Docker, no model)."
    }
  },
  "routes": [
    {
      "id": "dev",
      "label": "I code with AI",
      "audience": "Developers",
      "steps": [
        {"node": "guide", "text": "Understand the loop and why a few skills are enough", "tags": [{"text": "about 10 min", "easy": true}]},
        {"node": "template", "text": "Copy the starter kit into your repo", "tags": [{"text": "about 15 min", "easy": true}, {"text": "terminal", "easy": false}]},
        {"node": "work", "text": "Use it on real tasks", "tags": [{"text": "about 1 week", "easy": false}]},
        {"node": "lab", "text": "Check your harness with the eight-item checklist, then measure the skill you doubt", "tags": [{"text": "checklist first", "easy": true}]}
      ]
    },
    {
      "id": "lead",
      "label": "I lead a team",
      "audience": "Tech leads and managers",
      "steps": [
        {"node": "guide", "text": "Why the system matters more than the model", "tags": [{"text": "about 10 min", "easy": true}]},
        {"node": "brain", "text": "Put decisions, sources, and owners in one place", "tags": [{"text": "no code", "easy": true}]},
        {"node": "work", "text": "Run a pilot: one repo, one loop, one-page decisions", "tags": [{"text": "about 2 weeks", "easy": false}]},
        {"node": "observatory", "text": "Measure adoption without measuring people", "tags": []}
      ]
    },
    {
      "id": "docs",
      "label": "I work with documents, not code",
      "audience": "PMs, operations, and analysts",
      "steps": [
        {"node": "guide", "text": "The Knowledge Harness in a few minutes", "tags": [{"text": "about 5 min", "easy": true}]},
        {"node": "brain", "text": "One recurring question: its sources and who maintains them", "tags": [{"text": "no terminal", "easy": true}]},
        {"node": "work", "text": "Use AI with that context and note what failed", "tags": [{"text": "no terminal", "easy": true}]}
      ]
    },
    {
      "id": "champion",
      "label": "I improve the system",
      "audience": "AI champions and Harness Engineers",
      "steps": [
        {"node": "observatory", "text": "Find where it hurts: rework, cost, repeated failures", "tags": []},
        {"node": "lab", "text": "Turn the failure into a case and compare v1 against v2", "tags": [{"text": "about 45 min", "easy": false}]},
        {"node": "template", "text": "Promote what won, one skill at a time", "tags": []},
        {"node": "guide", "text": "Share what you learned", "tags": []}
      ]
    }
  ]
}
</script>
