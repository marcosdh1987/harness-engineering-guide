# Adapter Design

Adapters are needed because AI coding tools expect instructions in different shapes.

## Why adapters matter

- One tool may prefer repository files.
- Another may prefer structured task inputs.
- Another may depend on generated configuration or command wrappers.

## Good adapter practice

Generate or sync adapters from a source of truth when possible. Avoid manually maintaining divergent policy copies across tools.
