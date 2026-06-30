# Arquitecturas de Agentes y Mejores Prácticas

Este documento reúne los conceptos fundamentales, la terminología técnica y los patrones de diseño recomendados por Anthropic para construir sistemas agénticos robustos y de grado de producción con **Claude**.

---

## 1. Control de Flujo del Bucle Agéntico (Agentic Loop)

El ciclo de vida de un agente se basa en la **toma de decisiones impulsada por el modelo (model-driven decision-making)** en lugar de árboles de decisión estructurados de forma rígida y predecible. El modelo evalúa el contexto en cada turno para decidir qué herramienta llamar a continuación.

### El parámetro `stop_reason`
El control del bucle agéntico debe gestionarse de forma limpia y directa inspeccionando el campo `stop_reason` en la respuesta de la API:
- **`tool_use`**: Indica que el modelo ha decidido llamar a una herramienta. El orquestador local debe ejecutar la herramienta, dar formato al resultado y adjuntarlo al historial de la conversación antes de volver a llamar a Claude.
- **`end_turn`**: El modelo ha completado su razonamiento y devuelve la respuesta definitiva al desarrollador/usuario.

### Antipatrones críticos
- **Terminaciones heurísticas**: Nunca se debe intentar controlar el bucle analizando expresiones en texto plano (ej. buscar "tarea finalizada" o "OK") ya que es un método probabilístico y propenso a fallos.
- **Topes de iteración arbitrarios**: Establecer límites de turnos (ej. máx. 5 llamadas) como *único* mecanismo de parada oculta errores de bucles infinitos en lugar de manejarlos de forma limpia.
- **Asumir fin de turno por primer bloque de texto**: Claude puede emitir explicaciones en texto seguidas de llamadas a herramientas en una sola respuesta. El bucle debe continuar si existe una petición de herramienta, sin importar si vino acompañada de texto explicativo.

---

## 2. Orquestación Multi-Agente (Patrón Coordinador-Subagentes)

Para flujos complejos y no estructurados, se recomienda la arquitectura **Hub-and-Spoke** (Concentrador y Radios). En este patrón, un agente coordinador (Hub) gestiona la descomposición del problema, el enrutamiento de información y el control de errores, delegando tareas específicas a subagentes especializados (Spokes).

### Reglas de Diseño de Orquestación
- **Aislamiento de contexto (Regla de Oro)**: Los subagentes operan con un contexto estrictamente aislado. **No heredan** automáticamente el historial de conversación del coordinador. El coordinador debe transferir de forma explícita los hechos descubiertos, resultados previos y la meta exacta de investigación en el prompt de invocación del subagente.
- **La herramienta `Task`**: Es el mecanismo estándar para que un coordinador genere (spawnee) subagentes. El coordinador puede invocar la herramienta `Task` múltiples veces en una sola respuesta para lanzar ejecuciones en paralelo de subagentes y reducir la latencia general.
- **Riesgo de descomposición estrecha**: Un error común en coordinadores es fragmentar el objetivo de manera tan limitada que se pierde la cobertura del tema (ej. descomponer una consulta sobre "impacto en industrias creativas" analizando solo "diseño digital" y omitiendo "música" y "cine"). El coordinador debe asegurar una cobertura completa y transversal en sus planes.

---

## 3. Garantías Deterministas frente a Cumplimiento Probabilístico

Al diseñar sistemas de gobernanza para agentes de IA, se debe distinguir entre guías probabilísticas e imposiciones deterministas:

- **Instrucciones en Prompt (Probabilístico)**: Escribir restricciones en el prompt del sistema (ej. "no borres archivos" o "siempre verifica los IDs antes de reembolsar") ofrece un comportamiento probabilístico. Tiene una tasa de fallo no nula en condiciones complejas.
- **Hooks programáticos (Deterministas)**: El uso de interceptores de código es la única forma de asegurar el cumplimiento absoluto de reglas de negocio críticas o de seguridad:
  - **`PreToolUse` / Interceptación de salida**: Bloquea llamadas a herramientas salientes que violen una regla dura (ej. bloquear un reembolso de dinero de más de $500 y forzar la escalación a un humano).
  - **`PostToolUse` / Normalización**: Intercepta los resultados de una herramienta externa antes de que lleguen a Claude para normalizar formatos heterogéneos (ej. convertir marcas de tiempo UNIX provenientes de distintas APIs a un estándar ISO 8601), evitando que el modelo deba deducir formatos inconsistentes.
  - **Protocolo de Handoff (Escalamiento)**: Cuando el agente deriva el control a un humano, debe generar un **resumen estructurado** (ID de cliente, causa de escalación y acción sugerida), dado que los operadores humanos típicamente no tienen el presupuesto de tiempo o acceso para leer toda la transcripción del chat del agente.

---

## 4. Estrategias de Descomposición de Tareas

El diseño arquitectónico de los flujos debe adaptarse al tipo de tarea:

### Encadenamiento de Prompts (Prompt Chaining)
Es una canalización secuencial fija y predecible. Es ideal para tareas estructuradas con múltiples aspectos. 
- *Ejemplo en código*: En una revisión de código transversal a 15 archivos, un pase único de Claude tiende a diluir la atención del modelo, ignorando errores obvios. La arquitectura correcta consiste en un paso secuencial individual por archivo (análisis local) y un pase de integración final transversal.

### Descomposición Adaptativa
Consiste en la creación dinámica de tareas donde el agente genera nuevos pasos en función de los hallazgos intermedios. Es el enfoque preferido para exploraciones libres o investigaciones no estructuradas del repositorio.

---

## 5. Gestión del Estado de la Sesión y Bifurcaciones

A medida que las interacciones con el repositorio crecen, mantener el contexto libre de ruido y actualizado es indispensable para evitar la degradación del rendimiento de Claude.

- **Resumen y reinicio de sesión (`--resume <session-name>`)**: Reanudar una sesión larga mantiene el historial. Sin embargo, si el entorno local o los archivos del código cambiaron sustancialmente, es mucho más confiable iniciar una **sesión limpia** e inyectar un resumen estructurado del estado actual. Esto evita que Claude tome decisiones basadas en resultados de herramientas caducados o estados de variables obsoletos.
- **Bifurcaciones de contexto (`fork_session` o `context: fork`)**: Permiten crear ramas de análisis paralelas e independientes a partir de un estado base compartido (ej. probar dos enfoques de refactorización diferentes). Esto evita la contaminación de contexto cruzada y mantiene la sesión limpia de discusiones redundantes.
