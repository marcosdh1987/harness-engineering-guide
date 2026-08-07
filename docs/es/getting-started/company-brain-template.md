# El template de Company Brain

La página [Del proyecto a la organización](proyecto-a-organizacion.md) introduce el
Company Brain como concepto: el contexto organizacional gobernado que puede
compartirse entre proyectos, equipos y agentes de IA. Esta página documenta su
**implementación concreta**: el repositorio
[`company-brain-template`](https://github.com/marcosdh1987/company-brain-template)
— un punto de partida materializado para esa capa de contexto organizacional.

!!! tip "Cuándo usar este template"
    No el día uno. Un engagement de un solo repo mantiene su contexto *adentro*
    del repo (`memory/`, `docs/adr/`, docs de dominio) — ese **project brain**
    in-repo alcanza. Este template se gana su lugar cuando un **segundo
    repositorio empieza a duplicar el contexto del primero**. La progresión
    completa está en
    [Adopción en un proyecto existente](adopt-existing-project.md).

## Qué es

`company-brain-template` es un template de repositorio solo-documentación que
instancia un **company brain** para una organización: la fuente de verdad canónica
y legible por agentes de su dominio, decisiones, vocabulario, convenciones, mapa de
sistemas y runbooks operativos. No contiene código de producto. Todo es Markdown
versionado, propiedad de la organización que lo instancia.

Completa deliberadamente el modelo de dos capas que describe esta guía:

```text
Harness de ingeniería compartido (releases de ml-python-base) → cómo se trabaja (ejecución)
        +
Company brain (una instancia por organización)                → qué sabe la organización (contexto)
        =
Contexto efectivo de cada repositorio (los adapters importan ambas capas)
```

El harness es reutilizable entre organizaciones y se actualiza por releases semver.
El brain es único por organización y evoluciona con su negocio. Los repos de código
importan ambas capas desde sus adapters (`CLAUDE.md`, `AGENTS.md`).

## Estructura

| Sección | Contenido |
|---|---|
| `brain/00-index.md` | Punto de entrada: mapea tareas a las secciones que vale la pena cargar (inyección selectiva) |
| `brain/ai-policy.md` | La postura de IA de la organización — herramientas aprobadas, reglas de datos, permisos de agentes |
| `brain/domain/` | Visión del negocio, entidades, reglas de negocio numeradas (BR-NNN), stakeholders |
| `brain/glossary.md` | Vocabulario canónico del negocio |
| `brain/decisions/` | ADRs a nivel organización (los de un solo repo quedan en ese repo) |
| `brain/conventions/` | Convenciones de ingeniería, git y comunicación transversales |
| `brain/architecture/` | Mapa de sistemas e inventario de integraciones externas |
| `brain/runbooks/` | Procedimientos operativos paso a paso, ejecutables por una persona nueva o un agente |
| `brain/team/ownership.md` | Toda sección compartida tiene un dueño humano explícito |
| `memory/` | Aprendizajes y patrones a nivel organización |

## Ciclo de vida

El template incluye skills gobernadas (mismo formato que las de la implementación
de referencia) que cubren el ciclo completo:

- **`bootstrap_company_brain`** — instancia y puebla el brain para una organización
  nueva: primero mina fuentes reales (repos, docs, configuraciones), entrevista a
  humanos solo para lo que el minado no responde, y nunca inventa hechos del
  dominio. Una marca `_PENDIENTE_` visible vale más que ficción plausible.
- **`update_domain_context`**, **`record_decision`**, **`add_runbook`** — absorben
  cambios del negocio de forma consistente en lugar de parchear un solo archivo.
- **`quarterly_context_review`** — el mecanismo anti-drift: cada ~90 días el brain
  se audita contra la realidad, el contenido viejo se marca y la deuda de marcas se
  reporta a los dueños de sección. El contexto desactualizado es peor que el
  faltante.

La validación es automática (`make validate`: estructura, links, deuda de marcas) y
la estructura de carpetas se trata como interfaz pública — los repos consumidores la
referencian desde sus adapters, así que reestructurar es un cambio `MAJOR`.

## Relación con el resto del ecosistema

- La **guía** (este sitio) explica los conceptos y los niveles de adopción.
- **`ml-python-base`** aporta la capa de ejecución y distribuye las skills del
  ciclo de vida del brain con sus releases.
- El **lab** puede medir qué secciones del brain consultan realmente los agentes,
  alimentando el review trimestral: lo nunca leído es candidato a fusionarse o
  borrarse.

!!! note "Frontera de propiedad"
    El template (estructura + skills) es un activo de ingeniería reutilizable. Cada
    brain instanciado pertenece a la organización que describe — incluso cuando una
    consultora opera el bootstrap. Esa separación es lo que mantiene el motor
    reutilizable y el conocimiento del cliente como propio.
