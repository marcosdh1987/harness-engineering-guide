# El rol de Harness Engineer / AI Champion

A medida que las organizaciones de ingeniería adoptan herramientas de IA para programar, surge una brecha evidente: desarrolladores individuales reportan aceleraciones en tareas aisladas, pero la velocidad de entrega del equipo y la calidad global del software no mejoran. La destreza individual con herramientas de IA no genera automáticamente apalancamiento organizacional.

El **Harness Engineer** (o **AI Champion**) es el rol o capacidad organizacional responsable de transformar la productividad personal con IA en capacidad predecible y compartida para todo el equipo.

---

## 1. Definición: Responsabilidad antes que título formal

Dependiendo de la madurez y el tamaño de la organización, esta función puede manifestarse como:

- **Una responsabilidad de equipo**: distribuida entre ingenieros senior dentro de una squad de producto.
- **Un rol staff dedicado**: un staff engineer enfocado en productividad y flujos de trabajo con agentes.
- **Una capacidad del equipo de plataforma**: un equipo de plataforma interna (IDP) que provee gobernanza compartida, devcontainers e infraestructura de evaluación.

El título formal importa mucho menos que el mandato: **diseñar, mantener y simplificar el sistema alrededor del modelo.**

---

## 2. Contraste de perfiles

Comprender este rol exige separar la destreza individual del diseño de sistemas:

| Dimensión | Desarrollador diestro con IA | Harness Engineer / AI Champion |
|---|---|---|
| **Enfoque principal** | Terminar su ticket asignado más rápido | Diseñar el sistema que hace fiable a todo el equipo |
| **Uso de herramientas** | Escribir prompts individuales efectivos en el chat | Codificar restricciones en reglas, skills y gates reutilizables |
| **Estrategia de contexto** | Pegar fragmentos en la ventana de contexto | Estructurar el repositorio y los registros del Company Brain |
| **Verificación** | Revisar visualmente el código o correr checks locales | Construir suites de evaluación y casos de regresión |
| **Visión del ciclo** | Sesiones individuales de programación | Ciclo continuo: Estandarizar → Medir → Aprender → Mejorar |
| **Mantenimiento** | Adoptar cada nuevo truco o prompt de moda | Podar reglas obsoletas y retirar scaffolding redundante |

---

## 3. Responsabilidades centrales

El Harness Engineer opera sobre las **Cinco Superficies Operativas**:

### 1. Dirección e instrucciones
- Gobierna las reglas compartidas del repositorio (`.github/standards.md`, `AGENTS.md`, `CLAUDE.md`).
- Cura el catálogo de skills operacionales, asegurando que cada skill tenga disparadores claros y pasos de verificación.
- Establece pautas spec-driven que evitan que los agentes programen sin requerimientos claros.

### 2. Arquitectura de contexto
- Estructura el mapa del repositorio para que los agentes naveguen proyectos grandes con eficiencia.
- Conecta la memoria del proyecto (`memory/`, ADRs) con el Company Brain organizacional.
- Diseña mecanismos de recuperación selectiva para no saturar la ventana de contexto.

### 3. Entorno y legibilidad para agentes
- Garantiza entornos locales y de CI reproducibles (archivos de lock, contenedores, makefiles).
- Optimiza las herramientas internas para emitir salidas legibles por máquinas (JSON estructurado, códigos de salida estándar).
- Configura sandboxes aislados y worktrees de Git para ejecución paralela de agentes.

### 4. Validación y evaluación
- Construye suites de evaluación internas y casos de regresión derivados de bugs de producción.
- Opera la plataforma de evaluación para medir el impacto de cambios en el harness antes de lanzarlos.
- Aplica gates de calidad en varios niveles (`make check`) que impiden regresiones antes de integrar código.

### 5. Mantenimiento adaptativo y desmantelamiento de scaffolding
- Audita el uso de skills y reglas mediante logs de atribución.
- Detecta scaffolding que se volvió obsoleto por mejoras en los modelos de frontera.
- Simplifica el harness para reducir el consumo de tokens y la carga de mantenimiento.

---

## 4. Facilitar la adopción en el equipo

El Harness Engineer no actúa como un policía aislado. Su meta primordial es la educación y la transferencia de capacidades:

1. **Pairing y mentoría**: enseñar a los ingenieros a dirigir agentes eficazmente con el ciclo de trabajo.
2. **Estandarización de aprendizajes**: convertir lecciones de depuración en reglas del repositorio o tests de regresión.
3. **Eliminación de fricción**: lograr que usar el harness sea más rápido y confiable que trabajar sin él.
