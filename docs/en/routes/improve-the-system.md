# I improve the system

<div class="hk-facts" markdown>
<div markdown>
**For**

AI champions and Harness Engineers.
</div>
<div markdown>
**Time**

About 45 minutes for a first comparison.
</div>
<div markdown>
**You take away**

A harness change backed by a measured comparison, kept as a regression case.
</div>
</div>

<div class="hk-onmap" markdown>
On the map: <span class="hk-chip">1 Observatory</span> → <span class="hk-chip">2 Harness Lab</span> → <span class="hk-chip">3 Template</span> → <span class="hk-chip">4 Guide</span> <span class="hk-chip is-off">Company Brain</span> <span class="hk-chip is-off">Real work</span>
</div>

<div class="hk-steps" markdown>

<div class="hk-step" markdown>

### 1. Find where it hurts

<p class="hk-meta">Observatory · process signals</p>

Look for rework, repeated review comments, cost spikes, and failures that keep coming back. Process signals tell you where to look; they do not prove what caused the problem.

[Engineering Delivery Observatory](../measure-and-improve/engineering-delivery-observatory.md)

</div>

<div class="hk-step" markdown>

### 2. Turn the failure into a case and compare v1 against v2

<p class="hk-meta">Harness Lab · about 45 minutes</p>

Sanitize the failure into a reproducible case. Run the current harness and your change on the same case and the same model, several times each. One run is exploratory; read a difference only from about five runs per arm.

[Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md) · [Failure to regression](../patterns/failure-to-regression.md)

</div>

<div class="hk-step" markdown>

### 3. Promote what won, one skill at a time

<p class="hk-meta">Template · only what the comparison supports</p>

Change the template only with what the comparison supports. Add skills one at a time and keep the case as a regression check, so a later model or tool change cannot quietly undo the gain.

[Start with few skills](../harness-kit/few-skills.md) · [Use and modify skills](../start-here/use-and-modify-skills.md)

</div>

<div class="hk-step" markdown>

### 4. Share what you learned

<p class="hk-meta">Guide · where others will look</p>

Write the finding down where others will find it: a decision record, a learning entry, or a contribution to this guide.

[Continuous harness improvement](../adoption/continuous-harness-improvement.md)

</div>

</div>

!!! success "You finished the route"
    Bring the change back to daily work with [I code with AI](build-with-ai.md).
