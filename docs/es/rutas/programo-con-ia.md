# Programo con IA

<div class="hk-facts" markdown>
<div markdown>
**Para**

Developers que usan Claude Code, Codex, OpenCode o Copilot.
</div>
<div markdown>
**Tiempo**

Unos 15 minutos para arrancar, una semana más o menos para probarlo.
</div>
<div markdown>
**Te llevás**

Un repositorio donde la IA sigue tus reglas y verifica su propio trabajo.
</div>
</div>

<div class="hk-onmap" markdown>
En el mapa: <span class="hk-chip">1 Guía</span> → <span class="hk-chip">2 Template</span> → <span class="hk-chip">3 Trabajo real</span> → <span class="hk-chip">4 Harness Lab</span> <span class="hk-chip is-off">Company Brain</span> <span class="hk-chip is-off">Observatorio</span>
</div>

<div class="hk-steps" markdown>

<div class="hk-step" markdown>

### 1. Entendé el ciclo

<p class="hk-meta">Guía · unos 10 minutos de lectura</p>

Entender, planificar o diseñar cuando haga falta, ejecutar, testear, verificar, revisar, aprender. La ceremonia sigue al riesgo: un typo no necesita diseño, un subsistema nuevo sí. La mayor parte del valor viene de unos pocos hábitos, no de una lista larga de skills.

[El ciclo de trabajo](../patterns/working-loop.md)

</div>

<div class="hk-step" markdown>

### 2. Copiá el kit inicial en tu repo

<p class="hk-meta">Template · unos 15 minutos · sirve en un repositorio que ya tenés</p>

Tres tipos de cosas, nada más: reglas cortas, una memoria chica y un comando que puede fallar.

```text
tu-repo/
├── AGENTS.md          reglas cortas + tabla "¿qué tamaño tiene la tarea?"
├── CLAUDE.md          una línea que apunta a AGENTS.md
├── memory/            context · learnings · patterns
├── docs/adr/          decisiones de una página
├── docs/plans/        planes aprobados
├── <herramienta>/skills/   las 7 skills iniciales
└── make check         o el comando que ya verifica tu proyecto
```

| Si la tarea es... | Usá |
| --- | --- |
| Chica y clara | Cambio directo, después verificar |
| Acotada | Brainstorm rápido, después plan y ejecución |
| Nueva o ambigua | Diseño aprobado, después plan, después ejecución |

!!! info "Nivel de evidencia: implementación de referencia"
    En el Harness Lab cada corrida cargaba 25 skills, y en 18 corridas con seis modelos los agentes abrieron solo 3. Un backend de producción (anonimizado) pasó de 27 skills sueltas a 9 puntos de entrada y achicó un 19% sus instrucciones generadas. Son muestras chicas: leelas como señales, no como leyes.

[El kit inicial](../harness-completo/index.md)

</div>

<div class="hk-step" markdown>

### 3. Usalo durante una semana, más o menos

<p class="hk-meta">Trabajo real · tus tareas de verdad</p>

Trabajá como siempre, pero elegí el camino de cada tarea según su tamaño. Cada vez que la IA cometa el mismo error dos veces, agregá una entrada en `memory/learnings.md`: el hecho, por qué importa y cómo aplicarlo la próxima vez. Esa lista es tu próximo cambio al harness.

[Memoria del proyecto](../harness-completo/memoria-del-proyecto.md)

</div>

<div class="hk-step" markdown>

### 4. Revisá tu harness y después medí la skill que dudás

<p class="hk-meta">Harness Lab · primero la checklist</p>

Recorré la checklist de salud de ocho puntos leyendo tu repositorio. Para la versión automática, cloná el lab y apuntalo a tu proyecto:

```bash
git clone https://github.com/marcosdh1987/ai-agentic-harness-lab
cd ai-agentic-harness-lab
make harness-check REPO=../tu-proyecto
```

Necesita `git`, `uv` y `make`; no necesita Docker ni modelo. Cada corrida tarda unos 30 segundos. Si dudás de una skill, el lab la compara contra no tenerla, en el mismo caso.

[Chequeo de salud del harness](../harness-completo/chequeo-de-salud.md) · [Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md)

</div>

</div>

!!! success "Terminaste la ruta"
    Si sos quien empuja esto en tu equipo, seguí con [Lidero un equipo](lidero-un-equipo.md) o [Mejoro el sistema](mejoro-el-sistema.md).
