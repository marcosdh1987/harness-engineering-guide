# Planes y specs

## Qué es

Una spec (un diseño) dice qué vas a construir y por qué. Un plan dice cómo, paso a paso: los archivos que toca cada paso y cómo se verifica cada uno. El orden es fijo: se aprueba el diseño, después se escribe el plan, y la ejecución sigue el plan sin reabrir el diseño.

## Por qué rinde

Separar las decisiones de la ejecución permite que un agente haga una tarea larga sin desviarse, que una persona revise el diseño una vez en lugar de cada diff, y que el trabajo se pueda retomar cuando una sesión se corta a la mitad. Cuando el plan lleva las decisiones, la ejecución puede correr en un modelo más barato o repartirse entre agentes.

!!! info "Nivel de evidencia: implementación de referencia"
    Un backend de producción (anonimizado) guardó más de dos docenas de planes en `docs/plans/` en dos meses. Su skill de planificación (`plan_and_execute_feature`, también en `ml-python-base`) tiene un modo `execute_only`: con un plan aprobado, saltea las fases de planificación y va directo a ejecutar, así el diseño no se reabre.

## Plantilla

Una spec, en `docs/specs/AAAA-MM-DD-<tema>-design.md`:

```markdown
# Diseño: <tema>

## Intención
Por qué existe y para quién es.

## Objetivos, no objetivos y anti-objetivos
Lo que tiene que hacer, lo que no va a hacer y lo que lo haría un fracaso aunque funcione.

## Restricciones
Reglas, dependencias, plazos, privacidad.

## Enfoques considerados
Dos o tres opciones, qué resigna cada una, cuál se eligió y por qué.

## Diseño decidido
Lo que ya está resuelto.

## Lo que queda a quien construye
Lo que puede decidir la persona o el agente que lo implementa.
```

Un plan, en `docs/plans/AAAA-MM-DD-<tema>.md`:

```markdown
# Plan: <tema>

Spec: docs/specs/AAAA-MM-DD-<tema>-design.md

## Tarea 1: <entregable>
Archivos: <archivos a crear o cambiar>
- [ ] Escribí el test que falla (o el chequeo que lo prueba).
- [ ] Hacé el cambio.
- [ ] Corré <comando>. Esperado: <salida>.
- [ ] Commit.

## Tarea 2: ...
```

## Cuándo usarlo y cuándo no

Usá los dos para trabajo nuevo o ambiguo, para cambios que cruzan módulos y para todo lo riesgoso o difícil de revertir.

No los uses para tareas chicas y claras: un typo no necesita ninguno. Una tarea acotada lleva un plan corto en la misma sesión, no un archivo. La tabla de ruteo de `AGENTS.md` hace esa elección por vos.

## Qué falló en la práctica

- **El gate de diseño se nombraba más de lo que se usaba.** En el backend de producción, la skill de brainstorming (que bloquea el código hasta que se aprueba un diseño) aparecía en todos los archivos de instrucciones, pero solo se escribieron 7 specs de diseño en el mismo período en que se escribieron más de 100 registros de decisión y más de dos docenas de planes. La mayor parte del trabajo fue por el camino barato, y eso estuvo bien; el error sería creer que el gate protegía trabajo que nunca vio.
- **Los planes que reabren el diseño a mitad de camino** convierten la ejecución en una sesión de diseño nueva, sin la revisión que tuvo la primera.

!!! tip "Nivel de evidencia: recomendación de la guía"
    Dejá el gate de diseño solo para trabajo nuevo o ambiguo, y que la tabla de ruteo mande todo lo demás por el camino barato. Contá los diseños escritos, no las menciones del gate.

## Cómo saber si está sano

- Cada cambio no trivial que se mergeó puede señalar un plan, o una razón por la que no lo necesitó.
- Cada paso de un plan dice cómo se verifica.
- Cada spec registra los enfoques que consideró.
- Ningún plan cambió el diseño sin una aprobación nueva.

## Para profundizar

- [Trabajo guiado por specs](../patterns/spec-driven-agentic-work.md)
- [Delegación con gates](../patterns/gated-delegation.md)
- [El ciclo de trabajo](../patterns/working-loop.md)
- [Registros de decisión](registros-de-decision.md)
