# Start with few skills

## What it is

A skill is a reusable procedure the agent opens when a task matches its description. Starting with few means carrying a small set that covers the working loop (understand, plan, execute, verify, review) and adding others only when you can show they help.

## Why it pays off

Every skill an agent can see costs context on every run: its description is listed whether or not the skill is ever opened. A long catalog makes the right skill harder to pick and the rules harder to read, for agents and for people.

!!! info "Evidence level: reference implementation"
    - **Harness Lab:** every run carried 25 skills, about 5,000 characters of descriptions in each adapter file. Across 18 runs on six models, agents opened only 3 of them.
    - **Template:** a review of three repositories built from `ml-python-base` found 16 of 25 skills never invoked. The template now carries a `minimal` level of 7 skills by default.
    - **Production backend (anonymized):** a flat catalog of 27 skills became 9 entry points; the generated instruction block shrank 19%.
    - **Limits:** the lab's pruning trials were small (one model, Haiku 4.5, three to six cases) and did not show that any skill can be removed for free. So the rule there is: carry a small set by default, and make every removal earn its evidence.

!!! note "Two names, one idea"
    The template calls the set a **harness level** (`minimal` or `full`, declared in `.github/harness-levels.toml`). The Harness Lab calls the same idea a **skill profile**.

## Template

The seven starter skills. Where to get them and how to install them per tool: [the starter kit](index.md#skills).

| Skill | Use it to | Loop step |
| --- | --- | --- |
| `research_current_info` | Check facts that may have changed: versions, APIs, documentation | Understand |
| `brainstorm_quick` | Explore a bounded change before committing to one approach | Plan |
| `writing-plans` | Turn an approved design into small, verifiable steps | Plan |
| `plan_and_execute_feature` | Plan and carry out a feature in phases | Execute |
| `systematic_debugging` | Find the cause of a failure before changing code | Execute |
| `verify_changes` | Run the gate and confirm the change before calling it done | Verify |
| `requesting-code-review` | Ask for a review with the context a reviewer needs | Review |

## When to use it and when to skip it

Use it when a repository starts working with AI agents, and whenever the catalog has grown past what people can name from memory.

Go beyond it when a domain task repeats (database migrations, a release checklist) and a comparison shows a skill makes the outcome better. Add that skill alone, measure it, and keep the comparison as a regression case.

## What failed in practice

- **Catalogs grew because adding a skill felt free.** Most were never opened, yet every description was loaded on every run.
- **Vendored skills brought their own policies.** In the production backend, some third-party skills told the agent to commit or merge on its own, against the project's rules. The fix was to state the git policy in every adapter file and test it.

## How to check it is healthy

- You can name every skill and when it applies without looking it up.
- Every skill has a one-line description that says when to use it.
- The instructions loaded on every session stay short: about 200 lines.
- Every skill added after the starter set has a comparison or a written reason.

## Go deeper

### When you need more: skill families

The full template catalog, grouped by intention as a navigation aid (the template does not publish a family field):

| Intention | Typical work | Examples |
| --- | --- | --- |
| Bootstrap | Start or adopt a governed workspace | `bootstrap_project`, `bootstrap_company_brain` |
| Ideation | Explore a problem before committing to a solution | `brainstorm_quick` |
| Planning and execution | Turn intent into an actionable implementation | `generate_migration_plan`, `plan_and_execute_feature` |
| Architecture and design | Establish boundaries and reusable contracts | `create_domain_contract`, `refactor_to_clean_architecture`, `create_mle_agent_package` |
| Testing and debugging | Find failures and create executable checks | `generate_e2e_tests`, `systematic_debugging` |
| Verification | Check module structure and final outcomes | `validate_module_structure`, `verify_changes` |
| Documentation and learning | Explain a change and retain the lesson | `generate_implementation_docs`, `retrospective` |
| Research | Check information that may have changed | `research_current_info` |

External skills are useful when a domain needs them, but they should not silently become a new source of truth. Record their origin and review their instructions before adopting them.

### Related pages

- [Skill design](../patterns/skill-design.md)
- [Create your first skill](../start-here/create-your-first-skill.md)
- [Use and modify skills](../start-here/use-and-modify-skills.md)
- [ml-python-base skills reference](../reference-implementation/ml-python-base/skills.md)
- [Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md)
