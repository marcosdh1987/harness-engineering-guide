# Creá tu primera skill en 3 pasos

Ya tenés la [plantilla mínima de `SKILL.md`](minimal-setup.md). Acá
está todo el flujo para convertirla en una skill que Claude pueda descubrir.

## Antes de empezar

Reutilizá la plantilla mínima. El único frontmatter requerido es:

```markdown
---
name: <skill_name>
description: <one line — when Claude should use this>
---
```

`name` debe ser igual al nombre del archivo sin `.md`. El `description` es el disparador
semántico — escribilo como "Use when …" para que Claude sepa cuándo recurrir a la skill.

## El flujo de 3 pasos

1. **Escribí** el archivo fuente `.github/skills/<name>.md` usando la plantilla mínima
   (frontmatter + `# Skill: <name>` + Purpose / Required Input / Output Format / Execution
   Rules, terminando con una línea de cumplimiento de gobernanza).
2. **Sincronizá** al layout nativo:
   ```bash
   make sync-skills          # full: ingest + link + regenerate adapter regions
   # or, just the Claude symlink:
   make setup-claude-skills
   ```
3. **Verificá** que no haya drift (este es el gate de CI):
   ```bash
   make check-sync
   ```

## Qué hace el motor por vos

`make sync-skills` no solo copia un archivo — conecta la skill en cada adapter de herramienta:

- crea el symlink `.claude/skills/<name>/SKILL.md → ../../../.github/skills/<name>.md`;
- regenera la región gestionada **entre los sentinelas** en `CLAUDE.md`, para que tu nueva
  skill aparezca en la lista "Internal skills";
- refresca los otros adapters (OpenCode, Codex, Copilot, Antigravity) desde la misma
  fuente, para que la skill esté disponible en todos lados sin copiar a mano.

Ver [Referencia › Adapters](../reference-implementation/ml-python-base/adapters.md) y
[Referencia › Control de drift](../reference-implementation/ml-python-base/drift-control.md).

## Un ejemplo trabajado

Una skill diminuta y realista — resumir un pull request:

```markdown
---
name: summarize_pr
description: Use to produce a concise, reviewer-facing summary of a pull request's diff.
---

# Skill: summarize_pr

## Purpose
Turn a PR diff into a short summary a reviewer can read in under a minute.

## Required Input
- The PR number or the diff to summarize.

## Output Format
- A 3–5 bullet summary: what changed, why, and any risk to review.

## Execution Rules
1. Read the diff (`gh pr diff <n>` or the provided patch).
2. Group changes by intent, not by file.
3. Flag anything that touches public APIs or data.
4. Comply with `.github/architecture.md`, `.github/standards.md`.
```

Guardala como `.github/skills/summarize_pr.md`, ejecutá `make sync-skills`, después `make
check-sync`. Ahora aparece en `.claude/skills/` y en la región de skills de `CLAUDE.md`.

## Profundizá más

Esta página es el inicio rápido. Para la disciplina completa de autoría — encuadre de
escenarios, validación, modos de falla y reflexión — hacé el lab:

- [Lab: Crear una skill](../labs/create-a-skill.md)
- [Patrones › Diseño de skills](../patterns/skill-design.md)

## Documentación oficial

- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)

## Referencias

- [Referencia › Adapters](../reference-implementation/ml-python-base/adapters.md)
- [Referencia › Control de drift](../reference-implementation/ml-python-base/drift-control.md)
- [Lab: Validar un cambio](../labs/validate-a-change.md)
