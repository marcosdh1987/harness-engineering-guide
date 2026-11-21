---
hide:
  - toc
---

# Guía de Harness Engineering

Trabajá con IA de una forma en la que puedas confiar, que puedas medir y mejorar, uses la herramienta o el modelo que uses este mes. Elegí la ruta que más se parece a vos: el mapa enciende las piezas que necesitás, en orden.

## ¿Por dónde empiezo?

<div id="route-map" class="route-map"></div>

<div class="route-map-fallback" markdown>

<div class="grid cards" markdown>

-   :material-code-braces: **[Programo con IA](rutas/programo-con-ia.md){ data-route="dev" }**

    ---

    Para developers.

    1. Entendé el ciclo y por qué alcanzan pocas skills (unos 10 min).
    2. Copiá el kit inicial en tu repo (unos 15 min, terminal).
    3. Usalo durante una semana, más o menos, en tareas reales.
    4. Revisá tu harness con la checklist de ocho puntos y después medí la skill que dudás.

-   :material-account-group: **[Lidero un equipo](rutas/lidero-un-equipo.md){ data-route="lead" }**

    ---

    Para tech leads y managers.

    1. Por qué el sistema importa más que el modelo (unos 10 min).
    2. Decisiones, fuentes y dueños en un solo lugar (sin código).
    3. Un piloto: un repo, un ciclo, decisiones de una página (unas 2 semanas).
    4. Medí la adopción sin medir personas.

-   :material-book-open-variant: **[Trabajo con documentos, no código](rutas/documentos-no-codigo.md){ data-route="docs" }**

    ---

    Para PMs, operaciones y análisis.

    1. El Knowledge Harness en unos 5 minutos.
    2. Una pregunta que se repite: sus fuentes y quién las mantiene (sin terminal).
    3. Usá la IA con ese contexto y anotá qué falló (sin terminal).

-   :material-flask-outline: **[Mejoro el sistema](rutas/mejoro-el-sistema.md){ data-route="champion" }**

    ---

    Para AI champions y Harness Engineers.

    1. Encontrá dónde duele: retrabajo, costo, fallas repetidas.
    2. Convertí la falla en un caso y compará v1 contra v2 (unos 45 min).
    3. Promové lo que ganó, una skill a la vez.
    4. Compartí lo aprendido.

</div>

**Las piezas del ecosistema**

- [Guía](patterns/working-loop.md){ data-node="guide" }: el método. Cómo trabajar con IA sin depender de una herramienta.
- [Template](harness-completo/index.md){ data-node="template" }: tu repo con IA. Reglas, skills y gates de calidad versionados en el repositorio.
- [Company Brain](start-here/company-brain-template.md){ data-node="brain" }: contexto compartido. Fuentes, decisiones, procedencia y dueños.
- [Trabajo real](harness-completo/index.md){ data-node="work" }: el ciclo y unas pocas skills, todos los días.
- [Observatorio](medir-y-mejorar/engineering-delivery-observatory.md){ data-node="observatory" }: qué pasa en el día a día, medido como proceso, nunca como personas.
- [Harness Lab](harness-completo/chequeo-de-salud.md){ data-node="lab" }: ¿esto ayuda de verdad? Dos configuraciones, el mismo caso, un veredicto.

</div>

<div class="hk-below" markdown>

<div class="hk-loop" markdown>

**El mismo ciclo, en cualquier ruta**

<span class="hk-chip">Understand</span> → <span class="hk-chip">Planificar o diseñar cuando haga falta</span> → <span class="hk-chip">Execute</span> → <span class="hk-chip">Testear</span> → <span class="hk-chip">Verify</span> → <span class="hk-chip">Review</span> → <span class="hk-chip">Learn</span>

Un cambio chico lo recorre rápido. Uno grande pide un diseño y un plan. La ceremonia sigue al riesgo. Mirá el [ciclo de trabajo](patterns/working-loop.md).

</div>

<div class="hk-honest" markdown>

**Qué te va a decir esta guía, y qué no**

- Te da un método estable, no la herramienta del mes.
- Separa la evidencia de la industria, las recomendaciones de la guía y los hechos sobre los repositorios de referencia.
- Mide sistemas y flujos de trabajo, nunca personas.
- No es un runtime ni un producto: los repositorios de referencia son implementaciones posibles.

</div>

</div>

<script type="application/json" id="route-map-data">
{
  "ui": {
    "question": "¿Por dónde empiezo?",
    "routeFor": "Para",
    "openRoute": "Abrir la ruta completa",
    "tapHint": "Tocá una caja del mapa para ver qué es.",
    "what": "Qué es",
    "who": "Para quién",
    "first": "Primer paso",
    "learnTemplate": "lo que gana en el Lab vuelve al template",
    "learnGuide": "y a la guía",
    "signals": "señales",
    "mapLabel": "Mapa del ecosistema de Harness Engineering"
  },
  "nodes": {
    "guide": {
      "label": "Guía",
      "sub": "el método",
      "what": "Cómo trabajar con IA sin depender de una herramienta: contexto, reglas, pocas skills, verificación y aprendizaje.",
      "who": "Todos.",
      "first": "Leé el ciclo de trabajo (unos 10 minutos)."
    },
    "template": {
      "label": "Template",
      "sub": "tu repo con IA",
      "what": "ml-python-base: reglas, skills y gates de calidad versionados en tu repositorio y proyectados a Claude Code, Codex, OpenCode y Copilot. ¿Construís un producto con agentes? Mirá también ml-langchain-agent.",
      "who": "Developers y tech leads.",
      "first": "Copiá el kit inicial: un AGENTS.md corto, siete skills y un comando de verificación."
    },
    "brain": {
      "label": "Company Brain",
      "sub": "contexto compartido",
      "what": "company-brain-template: fuentes, decisiones, procedencia y dueños, en un lugar que pueden leer las personas y la IA.",
      "who": "Managers, PMs y equipos. No hace falta programar para empezar.",
      "first": "Elegí una pregunta que tu equipo repite y anotá sus fuentes."
    },
    "work": {
      "label": "Trabajo real",
      "sub": "ciclo + pocas skills",
      "what": "El trabajo de todos los días con IA: una tabla te dice cuándo alcanza con un cambio directo y cuándo conviene diseñar primero.",
      "who": "Quien hace el trabajo, con o sin código.",
      "first": "Usá el ciclo en tareas reales durante una semana, más o menos."
    },
    "observatory": {
      "label": "Observatorio",
      "sub": "qué pasa en el día a día",
      "what": "Señales de flujo, calidad y uso de IA. Mide el proceso, nunca el contenido y nunca a las personas.",
      "who": "Managers y AI champions.",
      "first": "Empezá por el modelo de madurez y las seis dimensiones."
    },
    "lab": {
      "label": "Harness Lab",
      "sub": "¿esto ayuda de verdad?",
      "what": "Compara dos configuraciones en el mismo caso (una skill, un modelo o una regla) y te dice qué ganó y con cuánta confianza.",
      "who": "Tech leads y AI champions.",
      "first": "Revisá tu repo con la checklist de salud de ocho puntos, o cloná el lab y corré make harness-check (unos 30 segundos por corrida, sin Docker, sin modelo)."
    }
  },
  "routes": [
    {
      "id": "dev",
      "label": "Programo con IA",
      "audience": "Developers",
      "steps": [
        {"node": "guide", "text": "Entendé el ciclo y por qué alcanzan pocas skills", "tags": [{"text": "unos 10 min", "easy": true}]},
        {"node": "template", "text": "Copiá el kit inicial en tu repo", "tags": [{"text": "unos 15 min", "easy": true}, {"text": "terminal", "easy": false}]},
        {"node": "work", "text": "Usalo en tareas reales", "tags": [{"text": "una semana, más o menos", "easy": false}]},
        {"node": "lab", "text": "Revisá tu harness con la checklist de ocho puntos y después medí la skill que dudás", "tags": [{"text": "primero la checklist", "easy": true}]}
      ]
    },
    {
      "id": "lead",
      "label": "Lidero un equipo",
      "audience": "Tech leads y managers",
      "steps": [
        {"node": "guide", "text": "Por qué el sistema importa más que el modelo", "tags": [{"text": "unos 10 min", "easy": true}]},
        {"node": "brain", "text": "Decisiones, fuentes y dueños en un solo lugar", "tags": [{"text": "sin código", "easy": true}]},
        {"node": "work", "text": "Un piloto: un repo, un ciclo, decisiones de una página", "tags": [{"text": "unas 2 semanas", "easy": false}]},
        {"node": "observatory", "text": "Medí la adopción sin medir personas", "tags": []}
      ]
    },
    {
      "id": "docs",
      "label": "Trabajo con documentos, no código",
      "audience": "PMs, operaciones y análisis",
      "steps": [
        {"node": "guide", "text": "El Knowledge Harness en pocos minutos", "tags": [{"text": "unos 5 min", "easy": true}]},
        {"node": "brain", "text": "Una pregunta que se repite: sus fuentes y quién las mantiene", "tags": [{"text": "sin terminal", "easy": true}]},
        {"node": "work", "text": "Usá la IA con ese contexto y anotá qué falló", "tags": [{"text": "sin terminal", "easy": true}]}
      ]
    },
    {
      "id": "champion",
      "label": "Mejoro el sistema",
      "audience": "AI champions y Harness Engineers",
      "steps": [
        {"node": "observatory", "text": "Encontrá dónde duele: retrabajo, costo, fallas repetidas", "tags": []},
        {"node": "lab", "text": "Convertí la falla en un caso y compará v1 contra v2", "tags": [{"text": "unos 45 min", "easy": false}]},
        {"node": "template", "text": "Promové lo que ganó, una skill a la vez", "tags": []},
        {"node": "guide", "text": "Compartí lo aprendido", "tags": []}
      ]
    }
  ]
}
</script>
