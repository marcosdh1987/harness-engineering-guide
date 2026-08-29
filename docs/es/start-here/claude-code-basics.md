# Fundamentos de Claude Code: tu primera sesión

Antes de cualquier configuración, ajustá bien el modelo mental. Claude Code no es un chat más
inteligente — es un agente semi-autónomo que lee, edita y ejecuta código, guiado por una
**capa operativa duradera** que vos controlás.

## Chat vs. una capa operativa duradera

En chat crudo reexplicás tu proyecto, tus convenciones y tus restricciones en cada sesión, y
nada de eso persiste. Un harness da vuelta esa lógica: las reglas, skills y contexto viven en
el repositorio, así que cada compañero de equipo — y cada sesión — arranca desde la misma
base. Esta es la diferencia entre un *prompt* de una sola vez y una *skill* reutilizable; ver
[Skills vs prompts](../concepts/skills-vs-prompts.md).

## Qué lee Claude Code

A grandes rasgos, Claude Code toma contexto de unos pocos lugares bien conocidos:

| Artefacto | Qué aporta |
|---|---|
| `CLAUDE.md` | Memoria del proyecto: punteros de gobernanza, ciclo de trabajo, política de comandos |
| `.claude/skills/` | Skills que Claude puede descubrir e invocar |
| `.claude/hooks/` | Recordatorios de sesión / nudges no bloqueantes |
| `.claude/settings.json` | Configuración del workspace |

Para el desglose completo de cómo el repo de referencia conecta esto, leé
[Herramientas › Claude Code](../tools/claude-code.md) — esta página se mantiene breve a
propósito.

## Memoria del proyecto: la idea de `CLAUDE.md`

`CLAUDE.md` es la memoria de tu proyecto — instrucciones persistentes que Claude lee al inicio
del trabajo.

!!! note "Capacidad nativa de Claude Code"
    Según la [documentación de Memory](https://docs.anthropic.com/en/docs/claude-code/memory), un
    `CLAUDE.md` a nivel de proyecto tiene precedencia sobre el personal/global, y podés
    dividir una memoria grande en módulos con imports `@path` para no inflar el contexto.

!!! tip "Cómo lo aplica ml-python-base"
    El repo de referencia usa un **único adapter `CLAUDE.md` gobernado** con una
    región de skills autogenerada. **No** usa imports `@path` — dirige el contexto
    por instrucción (una sección corta `## Governance` que apunta a los documentos de gobernanza).
    El mapa completo de nativo-vs-aplicado está en [Aprovechá más](leverage-more.md).

Construís la versión mínima y comprendida de este archivo en la página siguiente.

## Plan Mode vs. ejecución directa

Ajustá el modo al cambio:

- **Plan Mode** — para trabajo grande o estructural (un refactor a través de muchos archivos, una
  migración). Claude explora y propone una estrategia que vos validás *antes* de que edite
  nada. Esto refleja el ciclo de trabajo del harness **Ground → Plan → Delegate → Verify →
  Compound**; ver [Patrones › Ciclo de trabajo](../patterns/working-loop.md) y el
  [ciclo de trabajo](../reference-implementation/ml-python-base/working-loop.md) de referencia.
- **Ejecución directa** — para arreglos pequeños y bien acotados donde el error es obvio y no
  se necesita rediseño.

!!! tip "Regla práctica"
    Si no podés tener todo el cambio en la cabeza, planificá primero. Si el diff es pequeño y
    la causa es clara, hacelo directamente.

## Sesiones: retomar y contarle a Claude qué cambió

El trabajo largo abarca varias sesiones. Importan dos hábitos:

- **Retomá** (`--resume`) una sesión existente en lugar de arrancar en frío, para que Claude
  conserve el contexto previo.
- Cuando **una persona edita archivos** fuera de la sesión, decíselo a Claude explícitamente —
  necesita releer el estado modificado en lugar de asumir que lo va a notar por su cuenta.

!!! note "Capacidad nativa de Claude Code"
    Claude Code permite retomar sesiones y bifurcar (fork) una sesión para explorar enfoques
    divergentes desde un estado común.

## Mini flujo de estudio

1. Abrí un repo que tenga un `CLAUDE.md` y hojeá su sección `## Governance`.
2. Pedile a Claude que te explique de vuelta el ciclo de trabajo del proyecto.
3. Probá un arreglo pequeño en ejecución directa; probá un pedido más grande en Plan Mode.
4. Siguiente: construí tu propia [Configuración mínima](minimal-setup.md).

## Documentación oficial

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)

## Referencias

- [Skills vs prompts](../concepts/skills-vs-prompts.md)
- [Herramientas › Claude Code](../tools/claude-code.md)
- [Patrones › Ciclo de trabajo](../patterns/working-loop.md)
