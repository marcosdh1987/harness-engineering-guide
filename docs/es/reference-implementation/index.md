# Implementaciones de referencia y el ecosistema de 3 repositorios

La metodología de **Harness Engineering** no es una abstracción teórica. Está completamente respaldada en un **ecosistema público de tres repositorios en funcionamiento** que conecta metodología, gobernanza técnica y evaluación empírica en un ciclo continuo de mejora:

---

```mermaid
flowchart LR
    GUIDE["<b>1. Teoría y Metodología</b><br/>harness-engineering-guide<br/><i>(Patrones, Principios, Evals)</i>"]
    MPB["<b>2. Harness Gobernado</b><br/>ml-python-base<br/><i>(Reglas, Skills, Adaptadores, Gates)</i>"]
    LAB["<b>3. Plataforma de Evaluación</b><br/>ai-agentic-harness-lab<br/><i>(Sandboxes, Atribución, Auditorías)</i>"]

    GUIDE -->|"Define la Arquitectura"| MPB
    MPB -->|"Se Mide En"| LAB
    LAB -->|"Propuestas HEP Sanitizadas"| MPB
    LAB -->|"Benchmarks Empíricos"| GUIDE
```

$$\mathbf{MÉTODO} \longrightarrow \mathbf{IMPLEMENTAR} \longrightarrow \mathbf{MEDIR} \longrightarrow \mathbf{APRENDER} \longrightarrow \mathbf{MEJORAR} \circlearrowleft$$

---

## Los tres repositorios

### 1. Guía de Harness Engineering (`harness-engineering-guide`)
*La base de conocimiento pública y la metodología.*
- **Rol**: Explica los conceptos, el Modelo de Madurez del Agentic SDLC, el ciclo Estandarizar-Medir-Mejorar, principios de sandboxing, ingeniería de evaluación y patrones de diseño.
- **Independencia**: **Autocontenida.** No necesitas clonar ni ejecutar los otros repositorios para aprender y aplicar esta metodología en tu propia organización.
- **Repositorio**: [`marcosdh1987/harness-engineering-guide`](https://github.com/marcosdh1987/harness-engineering-guide).

---

### 2. ML Python Base (`ml-python-base`)
*La implementación de referencia de un harness gobernado.*
- **Rol**: Funciona como un template listo para producción para repositorios de ingeniería.
- **Características clave**:
  - Capa centralizada de reglas bajo `.github/` (`standards.md`, `architecture.md`, `automation.md`).
  - Catálogo de skills gobernadas (`.github/skills/`) con procedimientos estructurados.
  - Motor de sincronización declarativo en Python que genera adaptadores nativos (`CLAUDE.md`, `AGENTS.md`, `OPENCODE.md`, `GEMINI.md`, `.github/copilot-instructions.md`).
  - Quality gates de CI de solo lectura (`make check`, `make check-sync`) que verifican la integridad de lockfiles y evitan el drift no comprometido.
- **Repositorio**: [`marcosdh1987/ml-python-base`](https://github.com/marcosdh1987/ml-python-base).
- **Documentación**: [Guía de referencia de ml-python-base](ml-python-base/index.md).

---

### 3. Agentic Harness Lab (`ai-agentic-harness-lab`)
*La implementación de referencia de una plataforma de evaluación, benchmarking y mejora continua.*
- **Rol**: Proporciona una aplicación web local y backend de ejecución para evaluar harnesses de agentes y retroalimentar las observaciones en los templates de gobernanza.
- **Características clave**:
  - Ejecución aislada en contenedores Docker por corrida con workers en Celery + Redis.
  - Soporte multi-harness (Claude Code, OpenCode, Codex, Antigravity).
  - Hash de condición (`condition_hash`) y fingerprinting de harness.
  - Atribución estructurada (skills usadas vs disponibles).
  - Auditorías de comportamiento mediante LLMs y scoring multidimensional.
  - Generador de propuestas sanitizadas de ciclo cerrado (`HEP-YYYY-NNN`).
- **Repositorio**: [`marcosdh1987/ai-agentic-harness-lab`](https://github.com/marcosdh1987/ai-agentic-harness-lab).
- **Documentación**: [Guía de referencia de ai-agentic-harness-lab](ai-agentic-harness-lab/index.md).

---

## Cómo se cierra el ciclo en la práctica

```mermaid
sequenceDiagram
    autonumber
    actor Engineer as Ingeniero / Lead
    participant Lab as ai-agentic-harness-lab
    participant MPB as ml-python-base
    
    Engineer->>Lab: Ejecuta caso de evaluación (ej. migración de BD)
    Lab->>Lab: Ejecuta en sandbox Docker y analiza logs de pasos
    Lab->>Engineer: Atribución + Auditoría muestran debilidad en una skill
    Engineer->>Lab: Clic en "Generar issue sanitizado" (HEP-YYYY-NNN)
    Engineer->>MPB: Abre issue sanitizado y mejora la skill en .github/skills/
    MPB->>MPB: Ejecuta quality gates locales (make check && make check-sync)
    MPB->>MPB: Publica release SemVer (v1.4.0)
    Engineer->>Lab: make harness-sync-branch REF=v1.4.0
    Engineer->>Lab: Re-ejecuta el mismo caso en todo el tier de modelos
    Lab->>Engineer: Verificación aprobada: 0 propuestas generadas (Ciclo Cerrado)
```

---

### Explorar las implementaciones
- **[ml-python-base: Harness gobernado](ml-python-base/index.md)**
- **[ai-agentic-harness-lab: Plataforma de evaluación](ai-agentic-harness-lab/index.md)**
- **[Flujos de evaluación en el Lab](ai-agentic-harness-lab/evaluation-workflow.md)**
