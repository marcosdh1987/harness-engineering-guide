# Context Engineering

**Context Engineering** (Ingeniería de Contexto) es la práctica disciplinada de diseñar, estructurar, curar e inyectar información de forma selectiva en la ventana de contexto activa de un agente de IA.

La calidad del contexto —no su volumen— es el factor determinante más importante en el rendimiento de los agentes de programación. Aunque los LLMs modernos ofrecen ventanas de contexto que superan el millón de tokens, saturar indiscriminadamente el modelo con documentación provoca una degradación catastrófica en su capacidad de razonamiento, precisión y adhesión a reglas.

Una ingeniería de contexto eficaz trata la ventana de contexto como **memoria de trabajo finita y de alto coste**, reservando la gran mayoría de tokens para el código activo, árboles de sintaxis (AST), salida de tests y trazas de razonamiento.

---

## El peligro de la saturación de contexto (Context Flooding)

Un error recurrente en la ingeniería de software asistida por IA es el **context flooding** (saturación de contexto o inflado de prompts): concatenar bases de conocimiento enteras, toda la documentación del proyecto e historiales extensos en cada prompt del agente.

### Por qué fracasa el Context Flooding

1. **Degradación "Aguja en un Pajar" (Needle-in-a-Haystack)**: A medida que el número de tokens crece, disminuye la capacidad del modelo para recordar y priorizar restricciones críticas. Reglas de seguridad sutiles o requisitos de tipado estricto se pierden entre cientos de líneas de explicaciones secundarias.
2. **Confusión e instrucción drift**: Documentos históricos desactualizados o contradictorios hacen que el agente vacile entre convenciones obsoletas y estándares vigentes, llevando a decisiones arquitectónicas erróneas tomadas con falsa seguridad.
3. **Dilución de tokens y latencia**: Prompts de gran volumen ralentizan la velocidad de inferencia, disparan los costes operativos y agotan los límites de peticiones sin mejorar la calidad del resultado.
4. **Desplazamiento del estado de trabajo**: Llenar el prompt con contexto estático deja espacio insuficiente para el feedback dinámico en tiempo de ejecución —errores del compilador, salidas de tests y validación de diffs.

> **Regla fundamental**: Nunca transmitas conocimiento organizacional de forma indiscriminada. Una buena ingeniería de contexto se basa en la **curación de alta señal**, no en la ingesta exhaustiva.

---

## El patrón de Selective Context

Para dotar a los agentes exactamente de lo que necesitan sin saturar su contexto, los harnesses modernos implementan el **patrón de Selective Context**:

```text
┌──────────────────────────────────────────────┐
│ 1. START_HERE / Router Index                 │
│ Mapa compacto de dominios, reglas y entradas │
└──────────────────────┬───────────────────────┘
                       │ 1. Identificar intención y alcance
                       ▼
┌──────────────────────────────────────────────┐
│ 2. Task Routing Hub                          │
│ Catálogo específico del dominio o subsistema │
└──────────────────────┬───────────────────────┘
                       │ 2. Seleccionar referencias clave
                       ▼
┌──────────────────────────────────────────────┐
│ 3. Smallest Useful Read Set                  │
│ 1–3 archivos precisos (ADR, esquema, runbook)│
└──────────────────────────────────────────────┘
```

### 1. START_HERE / Router Index
Los archivos raíz de instrucciones (`CLAUDE.md`, `AGENTS.md` o `START_HERE.md`) nunca deben ser una enciclopedia exhaustiva. En su lugar, funcionan como una **tabla de enrutamiento ligera**:
- Restricciones no negociables globales (p. ej., "Ejecutar `make check` antes de concluir", "Prohibido el tipado `any` sin justificación").
- Mapa de alto nivel conciso con los dominios y subsistemas del repositorio.
- Punteros directos a hubs de documentación por dominio o índices generados.

### 2. Task Routing Hub
Ante una tarea concreta (p. ej., "Añadir autenticación al webhook de facturación"), el agente no rastrea el sistema de archivos completo. Consulta el enrutador para determinar qué dominio o capacidad corresponde:
- Si la tarea atañe a facturación, enruta hacia `docs/domains/billing/` o `billing-rules.md`.
- Si la tarea requiere migrar una base de datos, invoca la skill `db_migration` en vez de cargar todas las migraciones históricas.

### 3. Smallest Useful Read Set (Conjunto Mínimo Útil de Lectura)
Una vez delimitado el alcance de la tarea, el agente lee **únicamente el conjunto mínimo de archivos necesarios para cumplir la solicitud**:
- Típicamente entre 1 y 3 archivos concretos: el ADR del dominio activo, el esquema de la API objetivo y la fixture de test correspondiente.
- El 90%+ restante de la ventana de contexto se conserva limpio, permitiendo al agente razonar con profundidad, analizar diffs e inspeccionar salidas de ejecución de tests.

---

## Gobernanza estática vs. Contexto dinámico

En un harness bien diseñado, el contexto se divide en dos categorías operativas:

| Dimensión | Gobernanza Estática (Proyectada) | Contexto Dinámico (Selectivo) |
|---|---|---|
| **Qué es** | Restricciones no negociables, linters, tipado, compuertas de seguridad | Contexto del dominio, decisiones históricas, esquemas de APIs |
| **Dónde reside** | `.github/rules/`, adaptadores (`CLAUDE.md`), `Makefile` | Documentos de arquitectura, ADRs, runbooks, Company Brain |
| **Cómo llega al agente** | Proyectado automáticamente en cada sesión | Descubierto y leído bajo demanda mediante enrutamiento de tareas |
| **Ciclo de vida** | Cumplimiento estricto mediante compuertas de CI (`make check`) | Mantenido como documentación canónica de referencia |
| **Coste en tokens** | Fijo y mínimo (< 1.000 tokens) | Variable; cargado únicamente cuando la tarea activa lo exige |

---

## La capa de compilación en la práctica

El patrón de Selective Context conecta directamente con la **arquitectura de tres capas** detallada en [Del proyecto a la organización](../start-here/proyecto-a-organizacion.md#la-arquitectura-de-tres-capas):

```text
Sistemas de Registro Corporativos (Jira, GitHub, Notion)
       │ (evidencia / procedencia)
       ▼
Company Brain (Canon gobernado, ADRs, capacidades)
       │
       │  [ Capa de Compilación y Selección ]
       ▼
Engineering Harness (Enrutamiento START_HERE → Smallest Useful Read Set)
       │ (ejecución y validación)
       ▼
Código del Repositorio y Compuerta de Verificación (make check)
```

El Engineering Harness funciona como la **capa de compilación**: traduce el amplio volumen de conocimiento organizacional gobernado del Company Brain en contextos de trabajo compactos, accionables y recuperados selectivamente.

---

## Reglas prácticas de Context Engineering

1. **Mantén la documentación cerca del código**: Colocaliza los Architecture Decision Records (ADRs), definiciones de dominio y contratos de API junto a los módulos que describen.
2. **Usa frontmatter estructurado e índices generados**: Mantén metadatos legibles por máquinas (`type`, `status`, `domain`) y genera catálogos indexados compactos (`make index`) para que los agentes puedan realizar búsquedas sin escaneos recursivos costosos.
3. **Prefiere ejemplos ejecutables frente a prosa extensa**: Un test unitario claro y en verde enseña al agente más sobre el comportamiento esperado que cinco páginas de descripción narrativa.
4. **Poda y archiva activamente**: La documentación desactualizada es más perjudicial que la ausencia de documentación. Mueve patrones obsoletos a un archivo histórico o elimínalos.
5. **Mide la atribución de contexto**: Audita con regularidad qué documentación y skills consultan realmente los agentes durante las evaluaciones (ver [Flujo de evaluación](../reference-implementation/ai-agentic-harness-lab/evaluation-workflow.md)) para detectar archivos de contexto ruidosos o ignorados.

---

## Recursos relacionados

- **[¿Qué es Harness Engineering?](../start-here/what-is-harness-engineering.md)**
- **[Del proyecto a la organización](../start-here/proyecto-a-organizacion.md)**
- **[El template de Company Brain](../start-here/company-brain-template.md)**
- **[Arquitectura de reglas de IA](ai-rules-architecture.md)**
- **[Skills vs prompts](skills-vs-prompts.md)**
