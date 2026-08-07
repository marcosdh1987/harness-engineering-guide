# Delegación con gates: un pipeline de ticket a PR

Este patrón describe la forma más autónoma que un harness puede tomar de manera
segura: un agente recibe un ticket y produce un pull request listo para revisión
humana, con humanos solo en los dos extremos — escribir el ticket, revisar el PR.
Está probado internamente sobre una base de código real en producción; esta
página documenta el patrón en términos agnósticos de herramienta y cómo
implementarlo sobre el template de referencia.

## La idea central

La mayoría de los setups de agentes dejan que el modelo reporte su propio éxito.
Este patrón lo prohíbe estructuralmente, dividiendo el pipeline en dos capas con
una línea dura entre ellas:

- **El juicio es del modelo.** Leer el ticket, escribir la spec, proponer un
  diseño, editar código — todo lo que requiere interpretación.
- **La certificación es del código.** Si los gates pasaron, si el bug se
  reprodujo y dejó de existir, cuál es el veredicto final — todo lo que un
  revisor va a confiar debe derivarse de scripts deterministas que el modelo
  puede *invocar* pero cuyos resultados nunca puede *autorar*.

```text
juicio (modelo)                        certificación (código determinista)
  lee el ticket                          ¿pasó cada gate requerido?
  escribe la spec        ── invoca ──▶   ¿los gates notarían una rotura?
  propone el plan                        ¿el bug existió, y dejó de existir?
  edita código                           una única derivación del veredicto
                                                      │
                                        veredicto + artefactos → revisión humana
```

Todo lo demás del patrón es consecuencia de esa línea.

## El pipeline y sus dietas

Cada fase corre con un **contexto deliberadamente restringido** — una "dieta".
Las dietas son el mecanismo, no ceremonia:

| Fase | Dieta | Por qué |
|---|---|---|
| **Spec** | Solo el ticket — el repositorio *no* se carga | Una spec escrita con el código abierto empieza a describir lo que el código ya hace |
| **Diseño** | Repositorio abierto; no puede cambiar requisitos | Las decisiones de diseño necesitan el código; los requisitos se fijaron antes |
| **Revisión adversarial** | Contexto fresco; solo documentos, sin código | Un revisor que lee el código empieza a estar de acuerdo con él. Revisar con los mismos insumos de la spec le permite juzgar en vez de creer |
| **Plan** | Spec + diseño aprobados | Tareas, archivos, orden |
| **Implementación** | Una tarea, un commit | Los lotes chicos mantienen la verificación con sentido |
| **Verificación** | Solo determinista | Gates corridos por script, por tarea |
| **Clasificación** | Solo determinista | Una derivación del veredicto; una corrida que dispara un tope es `partial`, nunca `success` |

Un "no-go" adversarial devuelve el trabajo a una persona. No loopea para siempre.

## Qué puede significar "verificado"

Cuatro preguntas independientes, cuatro mecanismos — y una corrida que no puede
responder una lo dice, en vez de responder otra distinta:

| Pregunta | Mecanismo | Modo de falla honesto |
|---|---|---|
| ¿Pasaron los checks del propio proyecto? | Un runner ejecuta los gates **que el proyecto declara** | Ausencia, error y "no reconocido" son fallas — nunca "n/a" |
| ¿Esos checks notarían una rotura? | Un **chequeo de mutación**: revertir el diff no-test y re-correr los gates | Un gate que sigue pasando es decorativo — y se reporta como tal |
| ¿El bug descripto existió, y dejó de existir? | Una reproducción congelada, corrida en el commit base pineado y de nuevo en HEAD | Una repro que pasa en el pin no probó nada — se marca inválida |
| ¿Cuál es el veredicto? | Un único script de clasificación | Cualquier tope dispara → `partial`, nunca `success` |

El chequeo de mutación es el que los equipos subestiman: gates verdes prueban que
los gates *corrieron*, no que puedan *detectar* algo. Romper el código a
propósito y exigir que los gates lo noten es lo que hace que una corrida verde
signifique algo.

## Reglas permanentes

Cuatro reglas, cada una típicamente ganada por un bug que llegó a producción:

1. **Nada del repositorio se auto-certifica.** Todo lo confiable deriva de un
   commit base pineado *antes* de que un modelo tocara el árbol, guardado fuera
   del repositorio.
2. **La ausencia no es un pass.** Un artefacto faltante, un servicio que nunca
   levantó, un check que no cargó — cada uno tiene un estado propio y ruidoso.
3. **Las categorías no deben favorecer.** Ninguna taxonomía donde la rotura de
   entorno caiga en el bin que habilita el éxito.
4. **Las afirmaciones deben coincidir con los mecanismos.** "Determinista" se
   reserva para código. Un comentario que promete una garantía que el código no
   aplica es peor que el silencio.

## Implementación sobre `ml-python-base`

El template ya provee la mayor parte de la materia prima; el patrón es una forma
de ordenarla:

| Elemento del patrón | Contraparte en el template |
|---|---|
| Fases como procedimientos gobernados | Una skill por fase en `.github/skills/` (spec, diseño, adversarial, plan, implementación) — mismo formato que las skills existentes |
| Dietas por fase | Subagentes con contexto restringido (`.claude/agents/`, uno por fase; contexto fresco para el revisor adversarial) — los roles existentes `planner`/`reviewer`/`implementer` son el punto de partida |
| Capa de certificación | Gates de `make` más scripts deterministas chicos bajo `scripts/` — tooling nivel bash/`jq`, versionado y testeado como cualquier código. El modelo llama `make verify`; nunca escribe el reporte |
| Declaración por proyecto | Un archivo de config en el proyecto objetivo que declara *qué* gates existen y cómo correrlos — solo el proyecto sabe qué significa verificarlo; el pipeline solo sabe que la verificación debe ser demostrable |
| Artefactos por corrida | Un directorio por run (spec, plan, diffs y logs de gates por tarea, clasificación) — provenance que un revisor y el lab pueden auditar |
| La pared | Branch protection en la rama default, más dry-run como default de toda operación mutante. Un guard a nivel comando es cinturón de seguridad, no contención |

Lo que el template **no** te da y este patrón agrega: el orden de fases con sus
dietas, el chequeo de mutación, el flujo de evidencia red→green, y el
clasificador de derivación única. Cada uno es código chico y determinista — el
tipo de cosa que el paso *Verify* del working loop ya defiende, llevado a su fin
lógico.

## Dónde encaja

- **Orden de adopción:** esto es un estado final, no una puerta de entrada. Un
  equipo debería estar cómodo con el working loop asistido (Ground → Plan →
  Delegate → Verify → Compound) antes de delegar tickets completos.
- **Medición:** un lab de benchmarking puede correr el pipeline como una
  condición más (pipeline vs. sesión asistida, mismos tickets) y comparar pass
  rate, costo y cantidad de intervenciones — los artefactos del patrón están
  diseñados para auditarse.
- **Contexto:** la fase de spec lee el ticket *y las convenciones del proyecto* —
  reglas de ticketing, definition of ready, glosario del dominio — que es
  exactamente lo que provee el project brain (y, a escala multi-repo, un brain
  compartido). Ver
  [Adopción del harness en un proyecto existente](../getting-started/adopt-existing-project.md).
