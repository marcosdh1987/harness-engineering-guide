# Adopción del harness en un proyecto existente

La mayoría de los engagements reales no arrancan de un template limpio. El caso
típico es un **proyecto existente** — un repositorio, o unos pocos servicios que
comparten dominio — que ya tiene código, historia y costumbres. Esta página
describe cómo adoptar el harness ahí de forma segura, cómo el contexto del
proyecto crece hasta ser un **project brain**, y cuándo (y solo cuándo) ese brain
debería extraerse a un repositorio compartido.

La regla que gobierna todo esto viene de
[Del proyecto a la organización](proyecto-a-organizacion.md): **no saltear
niveles.** Adoptar en el alcance más chico que resuelva el problema observable.

## La progresión

```text
Nivel 0 — Repo existente, sin harness
    El uso de IA es ad-hoc; el contexto se re-explica en cada sesión.

Nivel 1 — Retrofit
    El repo adopta la capa de gobernanza del template
    (rules, skills, adapters, gates) vía sync selectivo. El código no se toca.

Nivel 2 — Project brain (adentro del repo)
    El contexto del proyecto se acumula en los contenedores que el template
    ya trae: memory/, docs/adr/, .github/domain-boundaries.md y docs de dominio.
    No se crea ningún repositorio nuevo.

Nivel 3 — Brain compartido (solo con 2+ repos)
    En el momento en que un segundo repo del mismo proyecto/cliente empieza a
    duplicar contexto, la parte común se extrae a un repositorio de contexto
    (ver El template de Company Brain) y ambos repos lo apuntan.
```

La mayoría de los engagements viven toda su vida en los niveles 1–2. Eso es
éxito, no un estado intermedio.

## Qué significa "project brain"

Un project brain no es un producto ni un repositorio nuevo. Es la **capa de
contexto in-repo** para la que `ml-python-base` ya trae contenedores:

| Contenedor | Qué se acumula ahí |
|---|---|
| `memory/context.md` | Dónde está el proyecto ahora — se actualiza al abrir/cerrar sesión |
| `memory/learnings.md`, `memory/patterns.md` | Lecciones durables y soluciones recurrentes |
| `docs/adr/` | Decisiones y su racional — el "por qué" durable |
| `.github/domain-boundaries.md` | Reglas y límites del dominio del proyecto |
| `docs/` (glosario, runbooks según necesidad) | Vocabulario y procedimientos, cuando se ganan su lugar |

El brain crece por uso, no por ceremonia: la primera sesión de trabajo llena
`context.md`; la primera decisión no obvia produce un ADR; un término que hubo
que explicar dos veces entra al glosario; un procedimiento explicado dos veces se
vuelve runbook. Nada se escribe "por las dudas".

## Dos rutas de adopción seguras

### Ruta A — Retrofit en el lugar

Para un repo que va a seguir evolucionando donde está. El sync selectivo de
gobernanza trae rules, skills, agents y adapters desde una release tagueada del
template **sin tocar código, datos ni el Makefile del proyecto**:

```bash
make template-remote-setup                 # una vez
make template-sync PREVIEW=1 REF=vX.Y.Z    # diff read-only — mirar siempre primero
make template-sync REF=vX.Y.Z              # adoptar
```

Propiedades de seguridad que lo hacen de baja fricción:

- **Primero read-only.** El preview muestra cada archivo que el sync escribiría
  antes de escribir nada.
- **Aditivo por defecto.** Los archivos de gobernanza aterrizan junto al
  proyecto; el CI y los scripts existentes no se modifican. Los gates se adoptan
  de forma incremental — primero los read-only (`lint`, `test`) y recién después
  se vuelven obligatorios.
- **Reversible.** Todo llega en un rango de commits; revertir la adopción es un
  `git revert`, no una migración de vuelta.

### Ruta B — Expansión estranguladora (repo nuevo junto al legacy)

Para proyectos donde retrofitear el repo legacy no vale la fricción (toolchains
muy viejos, CI congelado, builds hostiles) — o donde el trabajo nuevo se puede
separar limpio. En lugar de migrar el repo legacy, **el próximo módulo/servicio
arranca como repo nuevo desde el template** (`make init`) y conviven:

```text
repo-legacy/          retrofit mínimo: solo adapters + gates read-only
servicio-nuevo/       harness completo desde el día 1 (make init)
```

- El repo legacy recibe lo *mínimo*: adapters de instrucciones (`CLAUDE.md`,
  `AGENTS.md`) y checks read-only, para que la asistencia con IA también esté
  gobernada ahí — pero nadie reescribe su build.
- El trabajo nuevo pasa en el repo nuevo con el working loop completo.
- La migración avanza módulo a módulo, **tirada por tareas reales** ("esta
  feature toca el módulo X → X se muda"), nunca como reescritura big-bang.

Es el patrón strangler-fig clásico aplicado a la adopción del harness: la
fricción de la migración completa se evita porque la migración completa nunca se
agenda.

!!! warning "En cuanto la Ruta B crea dos repos, vigilar la duplicación de contexto"
    El repo legacy y el nuevo comparten dominio. El día que copiás el glosario o
    una regla de negocio de uno al otro es el día en que el brain compartido se
    gana su existencia — ver abajo.

## Cuándo extraer un brain compartido

El disparador es concreto y observable: **un segundo repo empieza a duplicar el
contexto del primero.** No antes. La extracción en sí es barata — es mover
archivos Markdown, no migrar código:

1. Instanciar el template de contexto
   ([company-brain-template](company-brain-template.md)) al alcance del
   engagement — la "organización" puede ser simplemente *la plataforma de este
   cliente*.
2. Mover (no copiar) las partes compartidas: glosario, reglas de dominio,
   decisiones cross-repo, convenciones comunes. Los ADRs y la memoria
   específicos de cada proyecto se quedan en su repo.
3. Apuntar los adapters de ambos repos al brain compartido (el snippet listo
   para pegar está en `examples/` del template).

Anti-patrón, dicho sin vueltas: **crear un company/shared brain el día uno de un
engagement de un solo repo es overkill.** Agrega un segundo repositorio a
mantener antes de que exista duplicación alguna. El project brain in-repo es la
herramienta correcta hasta que aparece el segundo repo.

## Medir la adopción

Una adopción sin baseline no puede demostrar valor. Medición mínima viable, en
orden de esfuerzo:

1. Rutear el uso de IA por un gateway desde el día uno — costo y adopción por
   developer pasan a ser datos, no anécdota.
2. Registrar el "antes": estado de los gates, tiempo de onboarding, dónde las
   sesiones pierden tiempo re-explicando contexto.
3. Re-medir a las 4–6 semanas; el delta es la evidencia del engagement.

## Checklist

- [ ] Preview corrido y revisado antes de cualquier sync (`PREVIEW=1`)
- [ ] Gates adoptados primero en read-only; nada existente se debilitó ni reemplazó
- [ ] `memory/context.md` completado en la primera sesión de trabajo
- [ ] Primer ADR registrado cuando apareció la primera decisión no obvia
- [ ] Ningún brain compartido creado mientras el engagement tiene un solo repo
- [ ] Con el segundo repo: duplicación vigilada, extracción hecha cuando aparece
