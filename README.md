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

Pull requests run a docs validation workflow that builds the site with `mkdocs build --strict` and uploads the generated `site/` directory as an artifact for inspection.

Pushes to `main` run the GitHub Pages deployment workflow, which builds the site, uploads the generated `site/` artifact for Pages, and deploys it with the official GitHub Pages actions.

## Open-source safety

This repository is intended for public use and does not include credentials, tokens, private URLs, client names, budgets, contractual details, copied private documentation, or sensitive prompts.

## License

This repository includes the MIT License for an initial public `0.1` release. Review the license choice before accepting substantial outside contributions if project governance changes.
