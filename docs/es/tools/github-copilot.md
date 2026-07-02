# GitHub Copilot

GitHub Copilot ocupa un lugar distinto dentro del harness: suele aparecer dentro del editor, cerca del archivo que se está modificando, y por eso necesita instrucciones duraderas que sean fáciles de descubrir desde el contexto del repositorio. En [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), Copilot consume una versión adaptada de las reglas compartidas mediante `.github/copilot-instructions.md`.

## Rol en el workflow

Copilot ayuda con sugerencias inline, chat dentro del editor, navegación conceptual y generación de fragmentos. El harness no debería asumir que Copilot ejecutará todo el ciclo de trabajo por sí solo; su fortaleza está en mantener las sugerencias alineadas con las reglas del repositorio mientras el desarrollador conserva el control.

El objetivo es que Copilot entienda:

- convenciones de arquitectura y estilo;
- límites entre `src/`, `tests/`, notebooks y datos;
- comandos de validación esperados;
- cuándo una sugerencia necesita tests, docs o revisión adicional.

## Qué lee Copilot

| Artefacto | Qué aporta | Fuente |
|---|---|---|
| [`.github/copilot-instructions.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/copilot-instructions.md) | Instrucciones persistentes del repositorio para Copilot. | Generado desde reglas compartidas |
| [`.github/architecture.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/architecture.md) | Capas, límites y criterios de diseño. | Fuente gobernada |
| [`.github/standards.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/standards.md) | Estándares de Python, `uv`, Ruff, mypy y checklist de validación. | Fuente gobernada |
| [`adapters/templates/copilot.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/copilot.md.j2) | Plantilla que empaqueta reglas compartidas para Copilot. | Adapter |

Copilot no necesita una carpeta de skills nativa como `.opencode/skills/` o `.codex/skills/`; su integración se apoya sobre instrucciones persistentes y contexto cercano al archivo.

## Archivos y carpetas que participan

La carpeta `.github/` cumple una doble función. Primero, contiene las fuentes humanas del harness: arquitectura, estándares, automatización, límites de dominio y orquestación. Segundo, aloja el archivo que Copilot descubre como instrucción persistente: `.github/copilot-instructions.md`.

El adapter `copilot.md.j2` evita copiar a mano las mismas políticas. Cuando cambian las reglas compartidas, `make sync-skills` puede regenerar la instrucción de Copilot y `make check-sync` puede detectar drift.

## Fuente de verdad vs generado

La fuente de verdad son las reglas gobernadas y los templates de adapters. `.github/copilot-instructions.md` es una salida preparada para Copilot. Si una regla aplica a todas las herramientas, debe cambiarse en la capa compartida, no solo en el archivo de Copilot.

Esta distinción importa porque Copilot opera muy cerca del código: una instrucción duplicada o vieja puede producir sugerencias que parecen correctas localmente pero contradicen el harness.

## Mini flujo de estudio

1. Lee [reglas](../reference-implementation/ml-python-base/rules.md) para ver las políticas compartidas.
2. Abre [`.github/copilot-instructions.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/copilot-instructions.md) y observa cómo se compactan para Copilot.
3. Revisa [adapters](../reference-implementation/ml-python-base/adapters.md) y ubica `copilot.md.j2`.
4. Cierra con [automatización](../reference-implementation/ml-python-base/automation.md) para entender qué comandos validan las sugerencias antes de integrarlas.

## Documentación oficial

- [GitHub Copilot Docs](https://docs.github.com/copilot): documentación principal de Copilot.
- [Repository custom instructions](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot): cómo agregar instrucciones persistentes al repositorio.
- [About customizing Copilot responses](https://docs.github.com/copilot/concepts/about-customizing-github-copilot-chat-responses): tipos de instrucciones y precedencia.
- [Copilot cloud agent](https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent): contexto para flujos agénticos delegados en GitHub.

## Referencias

- [`ml-python-base` en GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Reglas de la implementación de referencia](../reference-implementation/ml-python-base/rules.md)
- [Inventario de artefactos](../reference-implementation/ml-python-base/inventory.md)
- [Proyección de adaptadores](../reference-implementation/ml-python-base/adapters.md)
