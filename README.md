# Harness Engineering Guide

Harness Engineering Guide is a public, bilingual documentation site about building durable systems around AI coding tools.

## What this repository is

This repository is a study guide and reference for AI-assisted software development. It is documentation-first, static, and safe for open-source sharing.

## What Harness Engineering means

Harness Engineering is the practice of designing the durable system around AI tools: rules, context, skills, agents, adapters, workflows, validation gates, drift control, and documentation.

## Why the guide is bilingual

English is the canonical language for the guide. Spanish is a first-class translation so that the same ideas are accessible to a broader audience without mixing both languages on the same study page.

## Reference implementation

The guide uses [`marcosdh1987/ml-python-base`](https://github.com/marcosdh1987/ml-python-base) as a public reference implementation. This guide features auto-generated reference implementation sections and evidence libraries.

`ml-python-base` remains the authoritative source of truth for implementation patterns.

## Local installation

Create a local virtual environment and install the package dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Local commands (Makefile)

A helper `Makefile` is provided to run common operations locally:

- **Serve the site**:
  ```bash
  make docs-serve
  ```
  Launches a local development server at `http://localhost:8000`.

- **Build and validate the site**:
  ```bash
  make docs-build
  ```
  Performs a strict build validation (`mkdocs build --strict`). This is the same validation executed in CI.

- **Sync reference implementation**:
  ```bash
  make sync-reference
  ```
  Runs `scripts/sync_reference_template.py` to scan the local/remote `ml-python-base` template, generate the machine-readable snapshot JSON, and compile English and Spanish reference pages along with the evidence bibliography.

### Local sync folder configuration
By default, the sync script checks `/Users/marcossoto/Documents/example/ml-python-base` for a local clone. If that folder is not present, it will automatically clone `ml-python-base` into a temporary folder to perform the synchronization. You can override the target folder path using the `REF_REPO_PATH` environment variable:

```bash
REF_REPO_PATH=/path/to/my/ml-python-base make sync-reference
```

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

## Open-source safety

This repository is intended for public use and does not include credentials, tokens, private URLs, client names, budgets, contractual details, copied private documentation, or sensitive prompts.

## License

This repository includes the MIT License for an initial public `0.1` release. Review the license choice before accepting substantial outside contributions if project governance changes.
