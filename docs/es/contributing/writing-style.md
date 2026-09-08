# Guía de estilo de redacción

Este documento establece las normas canónicas de redacción y puntuación para `harness-engineering-guide`. Toda la documentación, guías, implementaciones de referencia y textos generados por agentes en este repositorio deben cumplir con estas directrices.

## Estándares de puntuación y prosa

Para mantener una documentación humana, natural, creíble y precisa, este repositorio aplica una estricta regla de puntuación en inglés y español.

### Puntuación prohibida en prosa

No utilices los siguientes signos de puntuación en la prosa visible:

1. **Doble guion ASCII (`--`)**: no uses dos guiones consecutivos como raya informal.
2. **Raya o em dash Unicode (`—`)**: no uses rayas para separar cláusulas o pensamientos.
3. **Semirraya o en dash Unicode (`–`)**: no uses semirrayas como recurso de estilo.

### Alternativas permitidas

En lugar de rayas, utiliza estructuras gramaticales convencionales:

- **Comas**: para oraciones parentéticas y pausas naturales.
- **Paréntesis**: para aclaraciones, acrónimos o contexto secundario.
- **Dos puntos**: para introducir explicaciones, listas o definiciones.
- **Punto y coma**: para vincular oraciones independientes estrechamente relacionadas.
- **Puntos seguidos**: para dividir ideas compuestas en oraciones directas.
- **Guion simple (`-`)**: para palabras compuestas técnicas estándar.

#### Ejemplos

| A evitar | Preferido |
|---|---|
| `The harness -- not the model -- determines the workflow.` | The harness, not the model, determines the workflow. |
| `The model — even a frontier model — needs feedback.` | Even a frontier model needs feedback. |
| `Extremos — escribir el ticket, revisar el PR.` | Extremos: escribir el ticket y revisar el PR. |
| `Tres repositorios — guía, template y lab.` | Tres componentes: guía, template y lab. |

### Excepciones técnicas

Estas secuencias siguen estando permitidas únicamente cuando sean necesarias dentro de:

- Bloques de código (como sesiones de shell, Python o YAML).
- Código inline y flags de línea de comandos (como `--strict` o `--locked`).
- Delimitadores de frontmatter (`---`).
- Filas estructurales de tablas Markdown (`|---|---|`).
- Líneas horizontales de Markdown (`---`).
- URLs y destinos de hipervínculos.
- Listas de atributos de Markdown (como `{.md-button--primary}`).
- Diagramas Mermaid.

## Verificación automatizada

El cumplimiento se verifica automáticamente mediante `scripts/check_prose_style.py`. Ejecuta la comprobación localmente con:

```bash
make check-style
```
