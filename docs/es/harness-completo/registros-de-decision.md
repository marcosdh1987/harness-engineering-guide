# Registros de decisión (ADRs)

## Qué es

Un Architecture Decision Record (ADR) es una página sobre una decisión difícil de revertir: el contexto que obligó a elegir, la elección, sus consecuencias y las alternativas descartadas. El código muestra qué hace el sistema; el registro dice por qué.

## Por qué rinde

Los registros de decisión evitan que los equipos vuelvan a discutir lo que ya está resuelto, hacen más rápidas las revisiones y les dan a los agentes el razonamiento que necesitan para extender el sistema como se pensó. Un agente que lee "guardamos las fechas en UTC y las convertimos solo en los bordes, porque..." no va a agregar horas locales en el próximo cambio.

!!! info "Nivel de evidencia: implementación de referencia"
    Un backend de producción (anonimizado) escribió más de 100 registros de decisión en unos dos meses (alrededor de 1.000 commits). Muchos registraban decisiones de comportamiento (cómo se comporta un paso, qué componente es dueño de un valor), no solo de arquitectura. Cada título era la decisión escrita como una oración, así que el índice se leía como la lista de reglas vigentes.

## Plantilla

Copiá el registro desde [el kit inicial](index.md). Poné estas reglas en `docs/adr/README.md`:

```markdown
# Registros de decisión

Escribí uno cuando una decisión es difícil de revertir, o cuando alguien (una
persona o un agente) tendría que adivinarla de otra forma.

1. Copiá 0000-template.md como NNNN-titulo-corto.md (número siguiente, cuatro dígitos).
2. El título es la decisión como oración: "Guardar fechas en UTC y convertir en los bordes".
3. Completá Contexto, Decisión, Consecuencias y Alternativas. Una página alcanza.
4. El estado empieza como Propuesto. Pasa a Aceptado en el mismo pull request
   que lo implementa.
5. Un registro aceptado no se edita. Una decisión nueva lo reemplaza, y el
   viejo dice "Reemplazado por ADR-XXXX".
6. Agregá el registro al índice al final de este archivo.
```

Un comando `/adr` puede armar un registro nuevo desde la plantilla, agregarlo al índice y preguntarte lo que tuvo que suponer. Mirá [Comandos](comandos.md) para los otros atajos.

## Cuándo usarlo y cuándo no

Escribí uno cuando elegís un framework, una base de datos o un servicio externo; cuando definís o cambiás un límite entre módulos; cuando aceptás un trade-off que no es obvio; cuando fijás una convención que todos tienen que seguir; o cuando un agente tendría que adivinar por qué existe un comportamiento.

No lo escribas para cambios de rutina que se revierten fácil. Un typo no necesita un registro de decisión; las lecciones chicas van a la [memoria del proyecto](memoria-del-proyecto.md) o al mensaje de commit.

## Qué falló en la práctica

- **El estado se desactualizó.** En el backend de producción, más de la mitad de los registros seguían en "Propuesto" después de que su trabajo ya estaba en producción. Ni las personas ni los agentes podían saber qué decisiones estaban vigentes.
- **Editar la historia.** Cambiar un registro aceptado esconde cómo llegó el sistema adonde está. Reemplazarlo conserva la razón vieja y la nueva.

!!! tip "Nivel de evidencia: recomendación de la guía"
    Hacé que aceptar el registro sea parte del merge: el pull request que implementa una decisión cambia su estado a Aceptado, y quien revisa chequea esa línea como cualquier otra.

## Cómo saber si está sano

- Todos los registros aparecen en el índice.
- Ningún registro está en "Propuesto" si su cambio ya se mergeó.
- Todo registro reemplazado nombra a su reemplazo.
- Cada registro sigue entrando en una página.

## Para profundizar

- [Memoria del proyecto](memoria-del-proyecto.md): para las lecciones que no son decisiones.
- [Planes y specs](planes-y-specs.md): donde muchas veces empieza una decisión.
- [Estado y continuidad](../concepts/state-and-continuity.md): cómo encajan las decisiones en la memoria del proyecto y en el conocimiento organizacional.
