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

## GitHub Pages deployment

GitHub Actions builds the site on every push to `main`, uploads the generated `site/` artifact, and deploys it with the official GitHub Pages actions.

## License

This repository includes the MIT License for an initial public `0.1` release. Review the license choice before accepting substantial outside contributions if project governance changes.
