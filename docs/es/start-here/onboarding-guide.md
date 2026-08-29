# Primeros pasos con Claude Code

Esta es la rampa de entrada. **No** necesitás leer todo
[`ml-python-base`](https://github.com/marcosdh1987/ml-python-base) para ser productivo con
Claude Code. Esta sección te lleva desde "chat y un `CLAUDE.md` copiado" a usar y crear
skills con confianza — apoyada en la documentación oficial de Anthropic y en los conceptos
de la certificación Architect, y honesta sobre qué hace Claude Code de forma *nativa* frente
a lo que la referencia `ml-python-base` realmente hace.

## Para quién es esto

Ingenieros que hoy están en alguna de estas situaciones:

- usan Claude en chat crudo, reexplicando el proyecto en cada sesión;
- copian un `CLAUDE.md` extenso desde algún lado sin entenderlo;
- no usan skills, plan mode ni otras funciones — haciendo a mano lo que Claude podría asumir.

## Tres antipatrones que esta sección corrige

| Antipatrón | Por qué duele | Dónde lo corregimos |
|---|---|---|
| Solo chat — nada persiste | Sin contexto duradero; reexplicás el proyecto cada vez | [Fundamentos](claude-code-basics.md) + [Configuración mínima](minimal-setup.md) |
| Copiar un `CLAUDE.md` enorme que no entendés | Frágil, sin dueño, se desincroniza, difícil de confiar | [Configuración mínima](minimal-setup.md) — pequeño y comprendido |
| Ignorar skills / funciones nativas | Repetir trabajo manual que Claude podría automatizar | [Usar y modificar skills](use-and-modify-skills.md) → [Aprovechá más](leverage-more.md) |

## El recorrido

Leé estas páginas en orden — cada una es corta y se apoya en la anterior:

1. **[Fundamentos de Claude Code](claude-code-basics.md)** — el modelo mental: contexto duradero, qué lee Claude, plan vs. ejecución directa, sesiones.
2. **[Configuración mínima](minimal-setup.md)** — copiá un `CLAUDE.md` y un `SKILL.md` pequeños que puedas defender línea por línea.
3. **[Usar y modificar skills](use-and-modify-skills.md)** — ejecutá skills existentes y modificalas de forma segura.
4. **[Creá tu primera skill](create-your-first-skill.md)** — una skill nueva en tres pasos.
5. **[Aprovechá más funciones](leverage-more.md)** — las funciones nativas que probablemente todavía no usás, y cuáles usa realmente este template.
6. **[Del proyecto a la organización](proyecto-a-organizacion.md)** — cómo los principios de harness engineering evolucionan desde un repositorio individual hacia harnesses compartidos, equipos y conocimiento organizacional gobernado ([ver sección Company Brain](proyecto-a-organizacion.md#company-brain-como-termino-emergente-de-la-industria)).

## ¿Usás Codex u OpenCode?

El harness es agnóstico de la herramienta: la documentación de gobernanza y las skills son
compartidas, y solo cambia el archivo adapter que cada herramienta lee. Seguí el mismo
recorrido de arriba y después aplicá el delta corto por herramienta:

- **[Primeros pasos con Codex](codex.md)** — adapter `AGENTS.md`.
- **[Primeros pasos con OpenCode](opencode.md)** — adapter `OPENCODE.md`.

## Cómo se relaciona con `ml-python-base`

Cada idea de abajo se explica primero como una capacidad general de Claude Code, y luego se
aterriza en lo que hace el repo de referencia. Donde ambos difieren, lo decimos — así
aprendés la herramienta *y* una forma real y con criterio de aplicarla. Cuando quieras la
profundidad completa, las páginas de
[Implementación de referencia](../reference-implementation/ml-python-base/index.md) y la guía
de estudio [Herramientas › Claude Code](../tools/claude-code.md) van más a fondo de lo que
esta rampa de entrada busca intencionalmente.

## Documentación oficial

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code Memory (`CLAUDE.md`)](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)

## Referencias

- [Ruta de aprendizaje](../learning-path.md) — la secuencia de estudio completa una vez que hiciste el onboarding.
- [Herramientas › Claude Code](../tools/claude-code.md) — cómo el repo de referencia conecta Claude Code.
- [Implementación de referencia › ml-python-base](../reference-implementation/ml-python-base/index.md)
