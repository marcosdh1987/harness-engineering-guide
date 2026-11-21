# Comandos

## Qué es

Un comando es un atajo corto con nombre que escribe una persona, como `/plan`, `/adr`, `/retro` o `/verify`, y que le dice al agente qué procedimiento seguir en un momento clave del ciclo. Un buen comando es delgado: apunta a las skills, a la memoria y al gate en lugar de repetirlos.

## Por qué rinde

Los comandos ponen los momentos importantes del ciclo a una tecla de distancia y hacen que un equipo trabaje de la misma forma sin memorizar procedimientos. Como cada uno es un archivo chico en el repositorio, se revisa y se versiona como código.

!!! info "Nivel de evidencia: implementación de referencia"
    Un backend de producción (anonimizado) tenía un puñado de comandos, de unas 20 líneas cada uno. Los que acompañaban un hábito que ya existía fueron los más mencionados: el comando de registros de decisión aparece varias veces más en sus documentos e historial que el de correr agentes en paralelo. Son menciones, no invocaciones medidas. El Harness Lab y `ml-python-base` traen el mismo núcleo: `/plan`, `/adr`, `/retro`, `/verify`.

## Plantilla

Los cuatro centrales y a qué apunta cada uno:

| Comando | Qué hace | Apunta a |
| --- | --- | --- |
| `/plan <objetivo>` | Lee primero el código y la memoria, elige la skill de ideación, escribe un plan por fases y no escribe código | `memory/`, `brainstorm_quick`, `writing-plans` |
| `/adr <decisión>` | Arma un registro de decisión desde la plantilla, lo agrega al índice y pregunta lo que tuvo que suponer | `docs/adr/` |
| `/retro` | Revisa el diff, agrega entradas cortas a la memoria y sugiere `/adr` si se tomó una decisión | `memory/`, `docs/adr/` |
| `/verify` | Corre el gate e informa con honestidad si pasó o falló | `make check`, `verify_changes` |

En Claude Code, un comando es un archivo Markdown en `.claude/commands/`; `$ARGUMENTS` se reemplaza por lo que escribís después del nombre del comando. Por ejemplo, `.claude/commands/retro.md` (en inglés, porque los agentes lo leen bien así; podés traducirlo):

```markdown
---
description: Close out work with a short retrospective and update project memory.
allowed-tools: Read, Edit, Write, Bash(git diff:*), Bash(git log:*)
---

Run a brief retrospective on the work done in this session.

1. Review what changed: `git diff`, `git log` for this branch, and the conversation.
2. Keep only durable, non-obvious knowledge: gotchas, why a choice was made,
   dead ends, new conventions. Skip what the code or commit messages already say.
3. Append short entries, one fact each, using the format in `memory/README.md`:
   facts to `memory/learnings.md`, conventions to `memory/patterns.md`,
   current focus to `memory/context.md`.
4. If a decision that is hard to reverse was made, suggest running `/adr`.
5. Summarize what you recorded in three to five bullets.
```

Otras herramientas tienen su propio mecanismo para prompts reutilizables; mantené los mismos nombres para que la gente pueda pasar de una herramienta a otra.

## Cuándo usarlo y cuándo no

Creá un comando para un momento que se repite varias veces por semana: empezar un plan, registrar una decisión, cerrar una sesión, verificar. No lo crees para procedimientos que corrés de vez en cuando; alcanza con una skill o una nota. Nunca copies el cuerpo de una skill en un comando: apuntá a la skill.

## Qué falló en la práctica

- **Los comandos para hábitos que el equipo todavía no tenía fueron los menos mencionados.** El comando de decisiones prosperó porque el equipo ya escribía decisiones; el de agentes en paralelo casi no aparece. Un comando facilita un hábito; no lo crea.

!!! tip "Nivel de evidencia: recomendación de la guía"
    Mantené entre cuatro y seis comandos. Si un comando ocupa más de una pantalla, una parte pertenece a una skill o a `AGENTS.md`.

## Cómo saber si está sano

- Cada archivo de comando entra en una pantalla.
- Cada comando nombra la skill, la carpeta o el target del que depende.
- Cada comando se usó en el último mes; sacá los que no.
- Los nombres de los comandos son los mismos en todas las herramientas que usa tu equipo.

## Para profundizar

- [Fundamentos de Claude Code](../start-here/claude-code-basics.md): cómo encajan comandos, skills y `CLAUDE.md`.
- [Registros de decisión](registros-de-decision.md) y [memoria del proyecto](memoria-del-proyecto.md): dónde escriben `/adr` y `/retro`.
- [Gates de calidad](gates-de-calidad.md): qué corre `/verify`.
