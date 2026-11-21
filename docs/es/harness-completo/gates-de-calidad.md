# Gates de calidad

## Qué es

Un gate de calidad es un comando que responde "¿este cambio es aceptable?" con un sí o un no: por ejemplo `make check`. Lo corren las personas, lo corren los agentes antes de decir que terminaron, lo pueden correr los hooks, y CI corre el mismo comando en cada cambio.

## Por qué rinde

El "todos los tests pasan" de un agente vale lo que vale el comando que hay detrás. Un único gate, usado por todos y por todo, convierte la verificación de una afirmación en evidencia, y te deja agregar una regla una sola vez (un lint, un test que hace cumplir la arquitectura) para que todas las herramientas la respeten.

!!! info "Nivel de evidencia: implementación de referencia"
    Un backend de producción (anonimizado) agrupaba su gate en `make check`: búsqueda de secretos, chequeo de prosa, chequeo de formato, lint, lint de seguridad, chequeo de tipos y tests con cobertura. Un `make ci` más amplio sumaba dos chequeos que vale la pena copiar: un test que lee los imports y falla cuando un módulo cruza una capa de la arquitectura, y un chequeo que falla cuando cambian el código o los tests sin un cambio en la documentación. `ml-python-base` v2.2.0 corrigió un gate que formateaba el código y después informaba éxito aunque fallara un test.

## Plantilla

Un gate mínimo en un `Makefile`, de solo lectura por diseño:

```make
# Fixes are a separate, explicit step.
fix:
	ruff check --fix src tests
	ruff format src tests

# The gate never writes. It fails when anything fails.
check:
	ruff format --check src tests
	ruff check src tests
	mypy src
	pytest
```

Usá el equivalente de tu stack (`npm run check`, `./gradlew check`). Después hacé que CI corra exactamente el mismo target:

```yaml
# .github/workflows/ci.yml
name: ci
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: make install
      - run: make check
```

Dos extras que rinden una vez que lo básico está en su lugar:

- **Un test de arquitectura:** un test unitario que lee los imports de cada módulo y falla si, por ejemplo, la capa de dominio importa la de infraestructura. La regla deja de depender de la revisión.
- **La documentación acompaña al código:** un chequeo de CI que falla cuando cambian archivos en `src/` o `tests/` y nada en `docs/`. Evita que se vuelva viejo el contexto que leen los agentes.

## Cuándo usarlo y cuándo no

Todo repositorio que tocan los agentes necesita un gate, aunque sea chico. Hacelo crecer a medida que encontrás fallas: un error que un agente cometió dos veces es candidato a un chequeo.

No pongas pasos lentos, inestables o que dependen de la red en el gate que los agentes corren en cada cambio; dejalos en un job aparte de CI.

## Qué falló en la práctica

- **Un gate que no podía fallar.** El `make test` anterior del template corría primero el formateador y el auto-fixer, y terminaba con una alternativa que imprimía "No tests found to run", así que una suite que fallaba salía con 0. Cada "los tests pasan" que dependía de él no estaba verificado. La versión 2.2.0 hizo que solo corra los tests y propague la falla.
- **Un gate que reescribe el árbol** esconde fallas de lint y deja diffs que nadie puede explicar, porque el código que se chequea cambia mientras se chequea.

## Cómo saber si está sano

- Rompé un test a propósito: el gate tiene que terminar con error.
- Corré el gate dos veces sobre un árbol limpio: `git status` sigue limpio.
- CI corre el mismo target en cada pull request.
- El gate termina lo bastante rápido como para que la gente lo corra antes de cada commit.

## Para profundizar

- [Chequeo de salud del harness](chequeo-de-salud.md): "La verificación puede fallar", "La verificación no reescribe el árbol", "CI corre el mismo gate que corre el agente".
- [Hooks](hooks.md): bloquear el final de un turno si el gate falla.
- [Validar un cambio](../labs/validate-a-change.md)
- [Referencia de automatización de ml-python-base](../reference-implementation/ml-python-base/automation.md)
