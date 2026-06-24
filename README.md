# Harness Engineering Guide

Harness Engineering Guide is a public, bilingual documentation site about building durable systems around AI coding tools.

## What this repository is

This repository is a study guide and reference for AI-assisted software development. It is documentation-first, static, and safe for open-source sharing.

## What Harness Engineering means

Harness Engineering is the practice of designing the durable system around AI tools: rules, context, skills, agents, adapters, workflows, validation gates, drift control, and documentation.

## Why the guide is bilingual

English is the canonical language for the guide. Spanish is a first-class translation so that the same ideas are accessible to a broader audience without mixing both languages on the same study page.

## Reference implementation

The guide uses [`marcosdh1987/ml-python-base`](https://github.com/marcosdh1987/ml-python-base) as a public reference implementation. It is referenced for patterns and structure only. This repository does not modify or copy private content from it.

## Local installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run locally

```bash
mkdocs serve
```

## Build the site

```bash
mkdocs build --strict
```

This is the same strict validation path used in CI before deployment.

## GitHub Pages deployment

The site is deployed to GitHub Pages with the official GitHub Pages Actions workflow.

### One-time repository setup

Enable GitHub Pages in **Settings → Pages** and set the source to:

- **Build and deployment source**: **GitHub Actions**

This only needs to be done once. The `Deploy GitHub Pages` workflow uploads the built `site/` artifact and publishes it through the `github-pages` environment on pushes to `main` or manual runs.

### Workflows

| Workflow | Trigger | What it does |
|---|---|---|
| `docs-check.yml` | Every PR and push to `main` | Validates the build with `mkdocs build --strict` |
| `pages.yml` | Push to `main`, manual run | Builds the site, uploads the Pages artifact, and deploys with the official GitHub Pages Actions flow |
| `pr-preview.yml` | PR opened / updated | Deploys a live preview to `pr-preview/pr-<N>/` and posts the URL as a PR comment |
| `pr-preview-cleanup.yml` | PR closed | Removes the preview directory and its PR comment |

PR preview URLs follow the pattern:
```
https://marcosdh1987.github.io/harness-engineering-guide/pr-preview/pr-<N>/
```

## Open-source safety

This repository is intended for public use and does not include credentials, tokens, private URLs, client names, budgets, contractual details, copied private documentation, or sensitive prompts.

## License

This repository includes the MIT License for an initial public `0.1` release. Review the license choice before accepting substantial outside contributions if project governance changes.
