# Del harness de proyecto al uso organizacional

Harness Engineering suele comenzar en un único repositorio. Desarrolladores y desarrolladoras configuran reglas persistentes, skills personalizadas y gates de validación para que herramientas de IA como Claude Code, Codex u OpenCode resulten efectivas a nivel local. Sin embargo, a medida que las organizaciones adoptan el desarrollo asistido por IA en múltiples equipos, surge una pregunta crítica: ¿cómo evolucionan estas prácticas desde proyectos individuales sin generar desalineación, reglas contradictorias o gobernanza centralizada excesiva?

Esta página explica cómo los harnesses a nivel de proyecto evolucionan hacia activos de ingeniería compartidos y cómo encajan dentro de sistemas más amplios de gestión del conocimiento y gobernanza organizacional.

> 💡 **Acceso rápido**: [Ir directamente a la sección Company Brain](#company-brain-como-termino-emergente-de-la-industria)

## Empezar con un solo proyecto

La base de Harness Engineering es siempre un repositorio individual. Dentro de un único código fuente, el harness del proyecto establece el entorno operativo duradero para los asistentes de IA. En lugar de depender de prompts improvisados o pedir a los equipos que reexpliquen decisiones de arquitectura en cada sesión de chat, el harness de proyecto encapsula:

- **Instrucciones persistentes y límites de arquitectura**: Restricciones obligatorias sobre estructura de código, dependencias y estilo.
- **Skills operativas**: Procedimientos reutilizables para ejecutar pruebas, refactorizar o generar documentación.
- **Adapters para herramientas**: Puntos de entrada específicos de instrucciones (`CLAUDE.md`, `AGENTS.md`, `OPENCODE.md`) que exponen la guía del proyecto a distintas herramientas de desarrollo asistido.
- **Comandos de validación y suites de prueba**: Scripts de verificación local (`make check`) que aseguran la validez del código antes de integrar cambios.
- **Artefactos contextuales**: Registros de decisiones de arquitectura (ADRs), descripciones del dominio, runbooks y controles locales de drift.

Al integrar estas capacidades directamente en el repositorio, el agente opera como un colaborador disciplinado alineado con la historia y estándares reales del proyecto.

## Qué proporciona `ml-python-base`

El repositorio [`ml-python-base`](../reference-implementation/ml-python-base/index.md) funciona como una implementación de referencia de un harness de ingeniería a nivel de proyecto. Demuestra cómo estructurar, versionar y validar capacidades para agentes en proyectos de Python.

Los elementos compartibles clave que aporta `ml-python-base` incluyen:

- **Gobernanza y reglas centralizadas**: Definiciones de reglas independientes de la herramienta mantenidas bajo `.github/rules/` (ver [Reglas](../reference-implementation/ml-python-base/rules.md)).
- **Skills operativas personalizadas**: Definiciones declarativas de skills ubicadas en `.github/skills/` (ver [Skills](../reference-implementation/ml-python-base/skills.md)).
- **Adapters para múltiples herramientas**: Generación automática de archivos adaptadores como `CLAUDE.md` y `AGENTS.md` (ver [Adaptadores](../reference-implementation/ml-python-base/adapters.md)).
- **Motor de sincronización y control de drift**: Herramientas (`scripts/sync_skills.py`, `make check-sync`) que detectan cuando los adaptadores o skills generados se desvían de las fuentes canónicas (ver [Control de drift](../reference-implementation/ml-python-base/drift-control.md)).
- **Ciclo de trabajo estandarizado**: Un patrón de interacción disciplinado `Ground → Plan → Delegate → Verify → Compound` (ver [Ciclo de trabajo](../reference-implementation/ml-python-base/working-loop.md)).

En lugar de reinventar estas estructuras en cada proyecto, los equipos pueden adoptar `ml-python-base` como una arquitectura de referencia base.

## Qué sigue siendo específico del proyecto

Aunque las estructuras de templates se pueden compartir, cada repositorio posee un contexto de dominio único que no puede—ni debe—estandarizarse globalmente.

Los elementos específicos del proyecto incluyen:

- **Propósito del producto y reglas de negocio**: La lógica de negocio explícita y las entidades del dominio únicas de la aplicación.
- **Arquitectura concreta y dependencias**: Elecciones específicas de frameworks, esquemas de bases de datos e integraciones con APIs externas.
- **Contexto histórico y ADRs**: Decisiones que explican por qué se tomaron compromisos de diseño específicos en este código en particular.
- **Runbooks operativos y scripts de despliegue**: Pipelines de CI/CD específicos del proyecto, configuraciones de entorno y pasos de entrega.
- **Tests locales y excepciones**: Pruebas unitarias/de integración del dominio y sobreescrituras locales a guías globales.

!!! warning "Aislamiento de contexto"
    > Un template compartido no debe eliminar ni reemplazar el contexto específico del proyecto.

Intentar reemplazar el conocimiento del dominio local con un template global genérico priva a los asistentes de IA del contexto preciso requerido para tomar decisiones locales correctas.

## Compartir el harness entre repositorios

Cuando una organización gestiona decenas o cientos de repositorios, copiar archivos de harness manualmente produce fragmentación. Para solucionar esto, las organizaciones establecen una capa base versionada entre repositorios.

Definimos un **Shared Engineering Harness** como:

> Un conjunto versionado de reglas de ingeniería, skills, adapters y prácticas de validación compartido por múltiples proyectos.

En este modelo, los harnesses de los repositorios se componen dinámicamente:

```text
Shared engineering harness
        +
Contexto local del proyecto
        =
Harness de proyecto efectivo
```

Los componentes compartibles entre repositorios incluyen típicamente:

- **Estándares de ingeniería y seguridad**: Reglas comunes de linter, límites de seguridad y políticas de vulnerabilidades.
- **Skills operativas aprobadas**: Procedimientos probados para tareas estándar como actualización de dependencias o revisión de contratos de API.
- **Gates de calidad y validación**: Verificaciones pre-commit estandarizadas y patrones de validación en CI.
- **Plantillas de documentación**: Formatos unificados para ADRs, pull requests y especificaciones técnicas.

## Escalar a equipos u organizaciones

Al pasar de varios repositorios a unidades de negocio complejas u organizaciones enteras, compartir archivos mediante Git resulta insuficiente. El despliegue empresarial introduce desafíos organizacionales que requieren infraestructura y gobernanza formal:

- **Control de acceso y límites de seguridad**: Control de acceso basado en roles (RBAC) para determinar qué equipos o agentes pueden consultar conocimiento sensible o ejecutar herramientas específicas.
- **Clasificación de datos y cumplimiento**: Garantizar que el código propietario o los datos personales (PII) nunca se inyecten inadvertidamente en contextos de modelos externos no aprobados.
- **Fuentes autoritativas y procedencia**: Establecer ownership claro y trazas de auditoría para las políticas organizacionales y estándares técnicos.
- **Búsqueda de conocimiento y registro de agentes**: Catalogar servicios empresariales, APIs y herramientas de agentes aprobadas entre equipos.
- **Gestión del ciclo de vida**: Mecanismos para actualizar, deponer y retirar guías o skills obsoletas a nivel corporativo.

Para respaldar la escala sin caer en una centralización monolítica, las organizaciones adoptan una estructura federada:

```text
Organización
├── Gobernanza compartida
├── Shared engineering harness
├── Conocimiento del dominio
├── Convenciones de equipo
└── Harnesses locales de proyecto
```

## Company Brain como término emergente de la industria

A medida que las empresas integran agentes de IA en múltiples dominios operativos, han surgido nuevos términos para describir estas arquitecturas de conocimiento multiproyecto.

> “Company Brain” es un término emergente de la industria para describir la aplicación de gestión del conocimiento organizacional, ingeniería de contexto, gobernanza e infraestructura de agentes entre múltiples equipos y proyectos.

Más que un estándar técnico formal o una disciplina académica, se trata de una etiqueta emergente utilizada para agrupar prácticas e infraestructuras ya existentes.

Conceptualmente, se apoya en áreas de investigación maduras como la gestión del conocimiento organizacional ([ISO 30401:2018](../evidence/research.md#iso-304012018-knowledge-management-systems-requirements)), la gobernanza de IA ([NIST AI RMF](../evidence/security.md#nist-artificial-intelligence-risk-management-framework-ai-rmf-10)), la ingeniería de contexto y la arquitectura de software empresarial. No debe presentarse como un producto comercial único, un binario ejecutable o una base de datos monolítica.

> En esta guía utilizamos “Company Brain” como una etiqueta práctica para referirnos al contexto organizacional gobernado que puede compartirse entre proyectos, equipos y agentes de IA.

### Relación con Harness Engineering

Es fundamental diferenciar la gobernanza del conocimiento organizacional de la ejecución técnica:

```text
Company Brain
    describe qué sabe la organización
    y cómo se gobierna ese conocimiento.

Harness Engineering
    vuelve ejecutable una parte seleccionada
    de ese conocimiento mediante reglas, skills,
    herramientas, workflows, contexto y validación.
```

En este modelo, **Harness Engineering puede funcionar como una capa de compilación entre el conocimiento organizacional y el comportamiento de los agentes.** La organización gobierna sus políticas y hallazgos del dominio, mientras que Harness Engineering proyecta subconjuntos relevantes de ese conocimiento en entornos de agentes accionables y validados.

## Qué no proporciona el template

Para mantener la claridad conceptual, es indispensable remarcar la frontera entre los templates a nivel de proyecto y los sistemas de conocimiento empresarial.

> `ml-python-base` puede aportar la capa de harness de ingeniería compartida dentro de un sistema más amplio de conocimiento y gobernanza organizacional. Por sí solo, no constituye un Company Brain.

Específicamente, `ml-python-base` **no** proporciona de manera nativa:

- Motores de búsqueda empresarial o pipelines de RAG corporativos.
- Gestión de identidades y accesos (IAM, RBAC, ABAC).
- Clasificación automática de datos o filtros DLP empresariales.
- Bases de datos de grafos de conocimiento empresarial.
- Auditoría centralizada y registro de logs entre múltiples repositorios.
- Motores de políticas legales o regulatorias corporativas.
- Catálogos corporativos de agentes o gateways para servidores MCP.

Reconocer estos límites evita que los equipos intenten forzar un template de repositorio para resolver problemas de infraestructura y gobernanza de nivel empresarial.

## Un camino incremental de adopción

La adopción de Harness Engineering debe realizarse de forma progresiva. Se debe evitar construir infraestructura organizacional compleja antes de consolidar harnesses funcionales a nivel de proyecto.

```text
Nivel 1 — Proyecto individual
Usar un harness pequeño y comprendido en un repositorio.

Nivel 2 — Implementación de referencia
Adoptar reglas, skills, adaptadores y patrones de validación reutilizables.

Nivel 3 — Shared engineering harness
Versionar y sincronizar componentes seleccionados entre repositorios.

Nivel 4 — Capa de equipo o dominio
Agregar terminología compartida, workflows, reglas de dominio y ownership.

Nivel 5 — Capa organizacional
Agregar controles de acceso, procedencia, gobernanza de políticas, descubrimiento, evaluación y auditabilidad.
```

### Principios de adopción

1. **No saltar niveles**: Intentar implementar gobernanza de Nivel 5 antes de dominar los fundamentos de Nivel 1 y Nivel 2 genera burocracia sin aportar utilidad real a la ingeniería.
2. **Resolver problemas reales**: Avanzar de nivel únicamente cuando el drift o las necesidades de gobernanza generen fricción observable.
3. **Preservar el ownership**: Cada regla compartida o skill del dominio debe contar con una persona o equipo responsable claro.
4. **Evitar la saturación de contexto**: No transmitir todo el conocimiento organizacional a cada sesión del agente. Inyectar únicamente lo relevante para la tarea activa.

## Distinciones clave

Para evitar confusiones habituales al escalar Harness Engineering, conviene tener presentes estas distinciones principales:

| Concepto | Propósito |
|---|---|
| Prompt | Instrucción para una interacción específica y transitoria |
| Contexto de proyecto | Conocimiento necesario para comprender un único repositorio |
| Harness de proyecto | Reglas duraderas, skills, herramientas, workflows y validación para un proyecto |
| Shared engineering harness | Capacidades versionadas y estándares compartidos entre varios proyectos |
| Conocimiento organizacional | Políticas, definiciones, decisiones de arquitectura e información del dominio |
| Company Brain | Etiqueta emergente para gobernar y aplicar el conocimiento organizacional entre equipos y agentes |

### No equivalencias

- **Conocimiento organizacional ≠ instrucciones para agentes**: La documentación cruda debe ser curada y estructurada en instrucciones accionables antes de que los agentes puedan ejecutarla eficazmente.
- **RAG ≠ gobernanza**: La generación aumentada por recuperación (RAG) provee mecanismos de búsqueda de datos; no define ni aplica políticas de seguridad, controles de acceso ni reglas de arquitectura.
- **Memoria ≠ fuente de verdad**: La memoria del agente guarda el historial de sesión y preferencias temporales; no reemplaza el código fuente canónico, la documentación versionada ni los esquemas de bases de datos.
- **Template compartido ≠ contexto completo del proyecto**: Un template base provee patrones de ingeniería estándar, pero el contexto del dominio local del repositorio sigue siendo indispensable.
- **Fuente independiente de la herramienta ≠ comportamiento idéntico en ejecución**: Las reglas centralizadas en Markdown ofrecen una guía unificada, pero cada herramienta de IA las procesa y ejecuta según sus capacidades nativas.

## Referencias

- [Conceptos › Harness Engineering](../concepts/harness-engineering.md)
- [Conceptos › Context Engineering](../concepts/context-engineering.md)
- [Conceptos › Arquitectura de reglas de IA](../concepts/ai-rules-architecture.md)
- [Implementación de referencia › ml-python-base Visión general](../reference-implementation/ml-python-base/index.md)
- [Implementación de referencia › Control de drift](../reference-implementation/ml-python-base/drift-control.md)
- [Implementación de referencia › Ciclo de trabajo](../reference-implementation/ml-python-base/working-loop.md)
- [Evidencia › Literatura de investigación (ISO 30401:2018)](../evidence/research.md#iso-304012018-knowledge-management-systems-requirements)
- [Evidencia › Avisos de seguridad (NIST AI RMF 1.0)](../evidence/security.md#nist-artificial-intelligence-risk-management-framework-ai-rmf-10)
- [Evidencia › Documentación de proveedores](../evidence/vendor-docs.md)
