# Mejora continua del harness

La **Mejora continua del harness** es la metodología operativa para traducir la evidencia obtenida en las evaluaciones en mejoras versionadas y verificadas mediante quality gates para el harness de ingeniería.

En lugar de modificar prompts o reglas de manera improvisada en múltiples repositorios, los equipos gestionan su harness de ingeniería con el mismo rigor que una librería compartida de nivel empresarial: mediante **evidencia, seguimiento de issues sanitizados, releases con SemVer y re-medición**.

---

## El ciclo de mejora continua de ciclo cerrado

El ciclo de mejora opera a través de dos fronteras sincronizadas: la **Plataforma de evaluación** y el **Template gobernado de repositorios**:

```mermaid
flowchart TB
    subgraph LAB["1. Plataforma de evaluación (ej. ai-agentic-harness-lab)"]
        RUN["Ejecutar caso de evaluación en Sandbox Docker"]
        ATTR["Capturar atribución estructurada y telemetría"]
        AUD["Generar auditoría de comportamiento con LLM"]
        ISSUE["Generar issue de mejora sanitizado"]
    end

    subgraph GOV["2. Repositorio gobernado (ej. ml-python-base)"]
        EDIT["Refinar skill / regla gobernada (.github/)"]
        GATE["Verificar gates de CI (make check && make check-sync)"]
        REL["Publicar release con SemVer (vX.Y.Z)"]
    end

    RUN --> ATTR --> AUD --> ISSUE
    ISSUE -->|"Issue público / rastreado"| EDIT
    EDIT --> GATE --> REL
    REL -->|"make harness-sync-preview / -branch"| RUN
```

---

## Los 4 pasos del ciclo de mejora

### 1. Evidencia (Observada en el Lab)
- Ejecuta un benchmark o caso de evaluación interna dentro de un contenedor Docker aislado.
- Revisa el **Panel de atribución** (qué reglas y skills fueron consultadas) y la **Auditoría de comportamiento** (¿el agente cayó en bucles de comandos, violó estándares de estilo o alucinó flags en CLI?).
- Aísla un **síntoma medible** (ej. *"el agente releyó el mismo archivo de configuración 8 veces sin actuar; los comandos repetidos equivalentes deben ser $\le 2$*").

### 2. Generación del issue sanitizado
- Genera un issue en Markdown sanitizado a partir de la ejecución de evaluación.
- **Protocolo de sanitización**: Elimina automáticamente rutas locales, nombres de hosts, tokens de API y variables de entorno privadas.
- El issue resultante define:
  - La **skill o regla objetivo** (`.github/skills/systematic_debugging.md`).
  - El **comportamiento fallido** observado en la corrida.
  - La **propuesta de corrección**.
  - El **criterio cuantitativo de éxito** (`repeated_equivalent_commands <= 2`).

### 3. Iteración y release (En el template gobernado)
- En el repositorio template gobernado, crea una rama de desarrollo.
- Actualiza la skill o regla bajo `.github/`.
- Ejecuta los quality gates locales (`make check`, `make check-sync`) para asegurar que los adaptadores multi-herramienta (`CLAUDE.md`, `AGENTS.md`, `OPENCODE.md`) se regeneren y sincronicen.
- Mergea el PR y crea un tag inmutable con SemVer (ej. `v1.4.0`).

### 4. Re-medición y validación (Cierre del ciclo)
- En la plataforma de evaluación, sincroniza la versión candidata en un worktree aislado de Git.
- Vuelve a ejecutar exactamente el mismo caso de evaluación con el mismo modelo, prompt y parámetros de sandbox.
- Compara la atribución, el consumo de tokens y las auditorías de comportamiento:
  - ¿Desapareció el síntoma medible?
  - ¿Aprobó la suite de tests objetivos?
  - ¿La corrida produjo **cero propuestas de mejora** (outcome gate limpio)?
- Si se valida, promueve el release del harness en todos los repositorios productivos de la organización.

---

## El gate determinista de resultados (Outcome Gate)

Una innovación clave en la gestión del ciclo de vida del harness es el **gate determinista de resultados**:

```mermaid
flowchart LR
    EVAL["Re-ejecutar caso bajo vX.Y.Z"] --> CHK{"Outcome Gate:<br/>1. Tests objetivos: PASS<br/>2. Score >= 8.0<br/>3. Intervenciones humanas: 0<br/>4. Auditoría: 0 ítems 'improve'"}
    CHK -->|"Todo Verdadero"| CLEAN["Corrida limpia:<br/>0 Propuestas generadas<br/>(Ciclo validado y cerrado)"]
    CHK -->|"Algún Falso"| ITER["Propuesta generada:<br/>Requiere iteración adicional"]
```

Una corrida que cumple limpiamente con todos los criterios objetivos y de comportamiento genera automáticamente **cero propuestas**. Cuando re-ejecutar el mismo caso en todo tu tier de modelos (ej. Claude Haiku, Sonnet, Opus) arroja cero propuestas en cada combinación, el ciclo de mejora queda objetivamente cerrado.

---

## Estrategias de sincronización del harness

Al distribuir las mejoras del harness a los repositorios de desarrollo, los equipos emplean tres estrategias controladas:

| Estrategia | Mecanismo | Uso recomendado |
|---|---|---|
| **Preview Dry-Run** | `make harness-sync-preview REF=vX.Y.Z` | Inspección de diffs en modo solo lectura antes de modificar archivos del workspace. |
| **Candidate Worktree** | `make harness-sync-branch REF=vX.Y.Z` | Prepara los cambios en un Git worktree aislado (`.worktrees/candidate-vX.Y.Z`) para verificar gates antes de mergear a `main`. |
| **Sincronización directa** | `make template-sync REF=vX.Y.Z` | Actualización directa para cambios menores no disruptivos en repositorios en desarrollo activo. |

---

## Hallazgos: las máquinas sugieren, las personas firman

El análisis automático es excelente para *notar* (un caso que regresionó, una skill que nadie consulta, una falla que se repite. Nunca debe tener permitido *concluir*. En un ciclo de mejora maduro, los patrones autogenerados llegan etiquetados como **sugeridos** y se vuelven hallazgos de registro solo cuando una persona los revisa, opcionalmente los edita y los firma; los rechazos también se registran, para que el mismo patrón no se re-proponga cada semana. Un hallazgo sin dueño es una afirmación que nadie tiene que defender) y un reporte para un cliente construido sobre hallazgos sin firma es marketing, no evidencia.

## Auditar un repositorio que nunca viste

El mismo ciclo escala a la consultoría: auditar el repositorio de un cliente con transparencia. La mecánica que lo hace creíble:

- **Derivar el benchmark de su propia historia**: los commits que cambiaron código y tests juntos se vuelven casos reproducibles, así la evaluación mide *su* trabajo, no un rompecabezas sintético.
- **Inferir su quality gate desde sus propios archivos** (targets del Makefile, lockfiles, configs de test) y adoptarlo explícitamente, nunca adivinarlo en silencio.
- **Juzgar cada corrida contra la gobernanza que esa corrida realmente tuvo.** Un brazo de control "nativo" auditado contra *tus* reglas se vería peor por construcción; la comparación nativo-vs-inyectado solo es honesta cuando cada brazo se mide contra su propia superficie.
- **Reportar solo lo que la evidencia sostiene.** Sin corridas, el reporte dice "lectura, no medición"; con repeticiones exploratorias, dice exploratorio.

La jugada de cierre de toda auditoría es el mismo experimento: *su repo tal cual está* versus *su repo con tu harness inyectado*, mismos casos, cinco o más repeticiones por brazo, la pregunta del engagement, respondida como medición.

---

### Recursos relacionados
- **[Construir una suite interna de evaluación](internal-evaluation-suite.md)**
- **[De fallos de agentes a casos de regresión](failures-to-regression-cases.md)**
- **[Gobernanza y ownership del equipo](team-governance.md)**
