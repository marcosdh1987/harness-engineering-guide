# Memoria del proyecto

## Qué es

Unos pocos archivos de texto en el repositorio que las personas y los agentes leen al empezar a trabajar y completan cuando aprenden algo que vale la pena guardar. La memoria guarda lo que el código y el historial de git no dicen: por qué algo es como es, la trampa en la que alguien ya cayó, la convención que nadie escribió.

## Por qué rinde

Un agente empieza cada sesión sin recordar la anterior. Sin una memoria escrita, los mismos datos se redescubren cada vez, despacio y a veces mal. Una memoria chica y cuidada convierte los descubrimientos aislados en algo que puede usar todo el equipo y cualquier herramienta.

!!! info "Nivel de evidencia: implementación de referencia"
    Un backend de producción (anonimizado) acumuló 29 aprendizajes con fecha en unos dos meses. Sus instrucciones y un hook de inicio de sesión le pedían al agente leer `memory/context.md` y `memory/learnings.md` antes de empezar, y un comando `/retro` agregaba entradas nuevas al final. El Harness Lab y `ml-python-base` usan los mismos tres archivos.

## Plantilla

| Archivo | Guarda | Actualizalo cuando |
| --- | --- | --- |
| `context.md` | Dónde está el proyecto hoy: qué está en curso, objetivos activos, restricciones, temas abiertos | Empieza o termina una sesión de trabajo, o cambia el foco |
| `learnings.md` | Hechos no obvios: trampas, por qué algo es así, callejones sin salida | Aprendés algo que te habría ahorrado tiempo |
| `patterns.md` | Convenciones propias de este código: nombres, capas, estilo de tests | Notás o establecés un patrón que otros deberían seguir |

Cada entrada tiene la misma forma:

```markdown
## <título corto>: <AAAA-MM-DD>

<Una o dos oraciones con el hecho.>

**Por qué importa:** <la consecuencia>
**Cómo aplicarlo:** <qué hacer la próxima vez>
```

Reglas para poner en `memory/README.md`:

```markdown
- Un hecho por entrada. Si crece, partila.
- Fechas absolutas (2026-11-21), nunca "ayer".
- Borrá una entrada que resulta estar mal; no la dejes para que confunda.
- No repitas lo que ya dicen el código, el README o un mensaje de commit.
- Linkeá el registro de decisión cuando una entrada explica una decisión.
```

## Cuándo usarlo y cuándo no

Escribí una entrada en el momento en que aprendés algo que te habría ahorrado tiempo, cuando cambia el foco del proyecto o cuando aparece una convención que otros deberían seguir.

No la escribas para lo que ya dicen el código, la documentación o el mensaje de commit, para cambios chicos donde no pasó nada sorprendente, ni para notas temporales de debugging. Esas notas son estado de trabajo: pertenecen a la tarea y desaparecen con ella.

## Qué falló en la práctica

- **La memoria creció sin límite.** En un repositorio de referencia `learnings.md` pasó las 3.500 líneas. Nadie, ni persona ni agente, recorre eso al empezar una sesión, así que la memoria dejó de cumplir su función.
- **Las entradas sobrevivieron a los hechos.** Un archivo de convenciones citaba un workflow de CI que ya no existía. El agente confiaba en una regla que nada hacía cumplir.

!!! tip "Nivel de evidencia: recomendación de la guía"
    Dale a la memoria un presupuesto de tamaño: `learnings.md` se tiene que poder recorrer en unos dos minutos. Cuando lo supere, pasá los hechos asentados a `patterns.md` o a la documentación, y borrá lo que ya no es cierto. Podar es parte del trabajo, no un proyecto de limpieza.

## Cómo saber si está sano

- `context.md` cambió durante la última semana de trabajo activo.
- `learnings.md` sigue dentro del presupuesto de tamaño.
- Cada ruta, comando o workflow que nombra una entrada todavía existe.
- Las entradas equivocadas se borraron, no quedaron con una nota.

## Para profundizar

- [Estado y continuidad](../concepts/state-and-continuity.md): la diferencia entre estado de trabajo, memoria del proyecto y conocimiento organizacional.
- [Registros de decisión](registros-de-decision.md): adónde van las decisiones difíciles de revertir.
- [El kit inicial](index.md): la carpeta `memory/` en contexto.
