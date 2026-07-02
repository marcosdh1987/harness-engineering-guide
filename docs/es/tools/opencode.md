# OpenCode

OpenCode es un buen ejemplo para estudiar cómo un harness separa la intención estable del repositorio de la forma nativa en que cada herramienta espera recibir instrucciones. En [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), OpenCode no se trata como una isla: consume reglas compartidas, skills gobernados y adapters generados desde el mismo sistema que alimenta al resto de herramientas.

## Rol en el workflow

OpenCode actúa como una herramienta de exploración, edición y ejecución guiada. Su valor aumenta cuando el repositorio ya explica qué arquitectura debe respetar, qué comandos validan el cambio y qué workflows repetibles conviene invocar como skills.

En el harness, OpenCode cumple tres funciones:

- leer instrucciones persistentes del repositorio antes de improvisar;
- descubrir skills proyectados en su estructura nativa;
- ejecutar cambios contra gates compartidos, como `make check` y `make check-sync`.

## Qué lee OpenCode

En la implementación de referencia, los artefactos principales son:

| Artefacto | Qué aporta | Fuente |
|---|---|---|
| [`OPENCODE.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/OPENCODE.md) | Perfil de integración, reglas de uso de herramientas, MCP y políticas de seguridad. | Fuente de verdad renderizada para OpenCode |
| [`.opencode/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.opencode/) | Configuración del workspace, módulos y enlaces nativos del adapter. | Generado |
| [`.opencode/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.opencode/skills/) | Skills gobernados expuestos en el formato que OpenCode puede descubrir. | Generado desde `.github/skills/` |
| [`adapters/templates/opencode.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/opencode.md.j2) | Plantilla que transforma reglas compartidas en instrucciones específicas para OpenCode. | Adapter |

La clave didáctica es que OpenCode lee una capa ya compilada para su experiencia, pero esa capa no debería convertirse en una segunda política independiente.

## Archivos y carpetas que participan

El contenido estable vive en `.github/`: arquitectura, estándares, límites de dominio, automatización, orquestación, skills internos y skills externos bloqueados. El motor [`src/ml_python_base/skills_sync/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/src/ml_python_base/skills_sync/) toma esa intención y la proyecta hacia `.opencode/`.

`make sync-skills` actualiza los enlaces, los bloques generados y los manifests. `make check-sync` verifica que nadie haya editado a mano lo que pertenece al output generado. Así, OpenCode puede tener una forma propia sin crear drift respecto del harness común.

## Fuente de verdad vs generado

Edita las reglas y skills en las fuentes gobernadas: `.github/*.md`, `.github/skills/`, `.github/skills-external/`, `adapters/` y el registro de sincronización. No edites como fuente primaria los archivos bajo `.opencode/skills/`, porque el motor puede sobrescribirlos.

Esta separación permite estudiar dos planos:

- **Intención**: qué quiere el repositorio que haga cualquier asistente.
- **Adapter**: cómo se empaqueta esa intención para que OpenCode la descubra y la ejecute.

## Mini flujo de estudio

1. Lee el [inventario de `ml-python-base`](../reference-implementation/ml-python-base/inventory.md) y ubica `OPENCODE.md`, `.opencode/` y `.opencode/skills/`.
2. Lee la página de [adapters](../reference-implementation/ml-python-base/adapters.md) para entender cómo `opencode.md.j2` participa en la proyección.
3. Lee [skills](../reference-implementation/ml-python-base/skills.md) y compara un skill en `.github/skills/` con su enlace en `.opencode/skills/`.
4. Cierra el recorrido con [automatización](../reference-implementation/ml-python-base/automation.md) y [control de drift](../reference-implementation/ml-python-base/drift-control.md) para ver cómo se valida que la copia nativa no diverja.

## Documentación oficial

- [OpenCode Docs](https://opencode.ai/docs/): introducción, instalación, configuración y uso general.
- [OpenCode Config](https://opencode.ai/docs/config/): formato de configuración JSON/JSONC y opciones del archivo `opencode.jsonc`.

## Referencias

- [`ml-python-base` en GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Inventario de artefactos](../reference-implementation/ml-python-base/inventory.md)
- [Proyección de adaptadores](../reference-implementation/ml-python-base/adapters.md)
- [Skills gobernados](../reference-implementation/ml-python-base/skills.md)
