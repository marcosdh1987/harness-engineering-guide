# Mejoro el sistema

<div class="hk-facts" markdown>
<div markdown>
**Para**

AI champions y Harness Engineers.
</div>
<div markdown>
**Tiempo**

Unos 45 minutos para una primera comparación.
</div>
<div markdown>
**Te llevás**

Un cambio al harness respaldado por una comparación medida, guardada como caso de regresión.
</div>
</div>

<div class="hk-onmap" markdown>
En el mapa: <span class="hk-chip">1 Observatorio</span> → <span class="hk-chip">2 Harness Lab</span> → <span class="hk-chip">3 Template</span> → <span class="hk-chip">4 Guía</span> <span class="hk-chip is-off">Company Brain</span> <span class="hk-chip is-off">Trabajo real</span>
</div>

<div class="hk-steps" markdown>

<div class="hk-step" markdown>

### 1. Encontrá dónde duele

<p class="hk-meta">Observatorio · señales del proceso</p>

Buscá retrabajo, comentarios que se repiten en las revisiones, picos de costo y fallas que vuelven. Las señales del proceso te dicen dónde mirar; no prueban qué causó el problema.

[Engineering Delivery Observatory](../medir-y-mejorar/engineering-delivery-observatory.md)

</div>

<div class="hk-step" markdown>

### 2. Convertí la falla en un caso y compará v1 contra v2

<p class="hk-meta">Harness Lab · unos 45 minutos</p>

Limpiá la falla hasta tener un caso reproducible. Corré el harness actual y tu cambio sobre el mismo caso y el mismo modelo, varias veces cada uno. Una corrida es exploratoria; leé una diferencia recién con unas cinco corridas por brazo.

[Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md) · [De fallo a regresión](../patterns/failure-to-regression.md)

</div>

<div class="hk-step" markdown>

### 3. Promové lo que ganó, una skill a la vez

<p class="hk-meta">Template · solo lo que respalda la comparación</p>

Cambiá el template solo con lo que respalda la comparación. Agregá skills de a una y guardá el caso como chequeo de regresión, así un cambio posterior de modelo o de herramienta no deshace la mejora sin que nadie lo note.

[Empezá con pocas skills](../harness-completo/pocas-skills.md) · [Usar y modificar skills](../start-here/use-and-modify-skills.md)

</div>

<div class="hk-step" markdown>

### 4. Compartí lo aprendido

<p class="hk-meta">Guía · donde otros van a mirar</p>

Escribí el hallazgo donde otros lo van a encontrar: un registro de decisión, una entrada de aprendizaje o un aporte a esta guía.

[Mejora continua del harness](../adoption/continuous-harness-improvement.md)

</div>

</div>

!!! success "Terminaste la ruta"
    Llevá el cambio al trabajo de todos los días con [Programo con IA](programo-con-ia.md).
