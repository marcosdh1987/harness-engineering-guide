# Chequeo de salud del harness

Ocho chequeos que te dicen si el harness de un repositorio puede hacer su trabajo de verdad. Los podés hacer todos leyendo tu repositorio; el Harness Lab también los puede correr por vos, de forma determinista y sin modelo.

!!! info "Nivel de evidencia: implementación de referencia"
    Son los chequeos de `make harness-check` del Harness Lab, los mismos que incluye su auditoría de repositorios. Los decide el código, no un modelo, así que el resultado es siempre el mismo.

## La checklist

| # | Chequeo | Cómo chequearlo leyendo | Por qué importa |
| --- | --- | --- | --- |
| 1 | **La verificación puede fallar** | Buscá el comando con el que se les pide verificar a los agentes. Rompé un test a propósito: ¿termina con error? | Si un test que falla igual termina con 0, cada "los tests pasan" que informa un agente no está verificado. |
| 2 | **La verificación no reescribe el árbol** | Leé ese target: ¿formatea o corrige solo mientras "testea"? | Un target que reescribe el código cambia lo que está chequeando, esconde fallas de lint y deja diffs sin explicación. |
| 3 | **Los hooks pueden hacer cumplir, no solo recordar** | Mirá tus hooks: ¿al menos uno puede bloquear (código de salida 2 o una decisión de bloqueo)? | Las reglas en prosa son consejos. Un hook que imprime un recordatorio y termina con 0 se muestra, no se hace cumplir. |
| 4 | **Las instrucciones que se cargan siempre siguen siendo un mapa** | Contá las líneas de `AGENTS.md`, `CLAUDE.md` o el archivo de reglas de tu herramienta. Presupuesto: unas 200 líneas o 2.500 tokens. | Cada sesión paga ese archivo antes de leer la tarea. Un mapa corto que apunta a la documentación y a las skills hace el mismo trabajo. |
| 5 | **Las skills se pueden descubrir** | Abrí cada `SKILL.md`: ¿tiene `name` y una `description` de una línea que diga cuándo usarla? | Un agente decide si carga una skill solo por su nombre y su descripción. Sin descripción, nunca la elige. |
| 6 | **Los servidores MCP están fijados** | Leé `.mcp.json`: ¿algún servidor usa `@latest` o no tiene versión? | Un servidor sin versión fija corre lo último que se publicó, con los permisos del agente. Fijarlo convierte cada actualización en un cambio revisado. |
| 7 | **CI corre el mismo gate que corre el agente** | Abrí `.github/workflows/`: ¿algún workflow corre el mismo target en cada cambio? | La verificación local solo cuenta si CI la hace cumplir; si no, los chequeos salteados llegan a main. |
| 8 | **La versión del harness está declarada** | ¿Hay un archivo `.template-version` o `.harness-version.yaml`? | Sin eso, nadie puede saber de qué harness salió un resultado ni si una actualización cambió algo. |

## Correrlo automáticamente

Cloná el Harness Lab una vez y apuntalo a cualquier repositorio local:

```bash
git clone https://github.com/marcosdh1987/ai-agentic-harness-lab
cd ai-agentic-harness-lab
make harness-check REPO=../tu-proyecto
```

Necesita `git`, `uv` y `make`. No necesita Docker, ni modelo, ni red una vez instalado, y cada corrida tarda unos 30 segundos. Lee el árbol commiteado (agregá `REF=<rama>` para otra referencia), imprime una línea por chequeo con un arreglo para cada falla y termina con 1 cuando algún chequeo falla, así que también puede ser un paso de CI.

## Después de la checklist

Una checklist en verde significa que el harness puede funcionar, no que ayude. Para saber si una skill, una regla o un cambio de modelo mejora los resultados de verdad, compará dos configuraciones en el mismo caso en el [Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md).

## Para profundizar

- [Gates de calidad](gates-de-calidad.md): chequeos 1, 2 y 7.
- [Hooks](hooks.md): chequeo 3.
- [Empezá con pocas skills](pocas-skills.md): chequeos 4 y 5.
- [El kit inicial](index.md): un harness que pasa la mayoría de los chequeos desde el primer día.
