# Harness Engineering

!!! info "Sobre esta página"
    **Qué vas a aprender:** los principios estables detrás de contexto, reglas, skills, herramientas, verificación y evaluación.

    **Para quién:** todos, con profundidad adicional para practitioners técnicos.

    **Leela cuando:** quieras la base conceptual antes de explorar implementaciones.

**Harness Engineering** es la práctica de diseñar, gobernar, observar, evaluar y mejorar de forma continua el sistema completo alrededor de agentes de inteligencia artificial aplicados al software y al trabajo de conocimiento.

En lugar de concebir el trabajo con IA como una conversación efímera, Harness Engineering estructura el sistema operativo que lo rodea: contexto confiable, reglas persistentes, skills modulares, adaptadores de herramientas, verificación, gates de calidad, observabilidad y evaluación. Los mismos principios pueden sostener un Engineering Harness o un Knowledge Harness.

---

```mermaid
flowchart TD
    DEV["Desarrollador / Flujo autónomo"] --> AGENT["Coding Agent (Claude, Codex, OpenCode, Antigravity)"]
    
    subgraph HARNESS["El Engineering Harness"]
        direction TB
        
        subgraph L1["1. Capa de Gobernanza"]
            R["Arquitectura de Reglas (.github/standards.md, architecture.md)"]
            C["Context Engineering y Esquemas de Límites de Dominio"]
        end
        
        subgraph L2["2. Capa de Ejecución y Adaptación"]
            S["Skills Gobernadas (.github/skills/)"]
            T["Herramientas y MCP Servers (Linters, AST, Tests)"]
            A["Adaptadores Multi-Herramienta (CLAUDE.md, AGENTS.md, OPENCODE.md)"]
        end
        
        subgraph L3["3. Capa de Verificación y Seguridad"]
            G["Quality Gates (make check, detección de drift en lockfiles)"]
            SB["Sandbox en Docker Controlado y Watchdogs de Procesos"]
        end

        subgraph L4["4. Capa de Medición y Mejora"]
            TEL["Telemetría y Atribución Estructurada (Langfuse, Trazas)"]
            EVAL["Suites de Evaluación y Matriz de Regresión Permanente"]
        end
    end

    HARNESS --> REPO["Repositorio de Destino y Código Productivo"]
    EVAL -.->|"Ciclo de Retroalimentación Continua"| HARNESS
```

---

## Los 4 pilares de la arquitectura de un harness

### 1. Gobernanza y restricciones
Establece las reglas de juego para el agente:
- **Límites de capas**: Separación estricta de responsabilidades (ej. Dominio, Aplicación, Infraestructura).
- **Estándares y convenciones**: Tipado, importaciones absolutas, nomenclatura y patrones prohibidos.
- **Límites de contexto**: Gestión del presupuesto de tokens y curación de la memoria del proyecto para maximizar la señal y evitar la dilución de contexto.

### 2. Capacidades y adaptadores de herramientas
Equipa al agente con procedimientos estructurados y repetibles:
- **Skills gobernadas**: Instrucciones ejecutables en Markdown con validación de entradas y pasos lógicos.
- **Servidores MCP y herramientas**: Interfaces controladas para consultar ASTs, esquemas de bases de datos o correr tests.
- **Adaptadores declarativos**: Generación automática de archivos de configuración (`CLAUDE.md`, `AGENTS.md`, `OPENCODE.md`, `GEMINI.md`, `copilot-instructions.md`) a partir de la fuente de verdad en `.github/`.

### 3. Verificación y seguridad en sandboxes
Evita la ejecución descontrolada y las regresiones silenciosas:
- **Quality Gates**: Verificaciones de pre-commit y CI de solo lectura que fallan de inmediato ante desincronizaciones o violaciones de reglas.
- **Sandboxes aislados**: Ejecución de agentes en contenedores Docker dedicados para garantizar reproducibilidad y evitar alteraciones en la máquina host.

### 4. Medición y mejora continua
Reemplaza la intuición por ciencia empírica:
- **Atribución estructurada**: Medición de qué partes del harness consultó efectivamente el agente durante su ejecución multi-paso.
- **Ingeniería de evaluación**: Experimentos A/B multi-corrida, ablaciones de skills y suites de regresión permanentes.
- **Propuestas de ciclo cerrado**: Transformación de errores observados en issues sanitizados que actualizan el harness de forma continua.

---

### Recursos relacionados
- **[¿Qué es Harness Engineering? (Empieza aquí)](../start-here/what-is-harness-engineering.md)**
- **[Estandarizar → Medir → Mejorar](../start-here/standardize-measure-improve.md)**
- **[Modelo de madurez del Agentic SDLC](../adoption/maturity-model.md)**
- **[Observabilidad vs Evaluación](observability-vs-evaluation.md)**
