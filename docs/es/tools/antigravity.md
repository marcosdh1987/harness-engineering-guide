# Antigravity

Antigravity se puede estudiar como otro consumidor del mismo harness multi-herramienta. En [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), su integración muestra una diferencia importante frente a OpenCode o Codex: algunas capacidades se copian a una estructura nativa bajo `.agents/` en vez de exponerse solo como enlaces simbólicos.

## Rol en el workflow

Antigravity recibe políticas duraderas, reglas de workspace y skills adaptados para ejecutar trabajo guiado. El harness debe darle la misma intención que al resto de herramientas, pero empaquetada en la forma que su runtime espera.

Su rol en el sistema es:

- leer reglas compatibles con el ecosistema Gemini/Antigravity;
- descubrir skills en `.agents/skills/`;
- respetar límites de workspace definidos por las reglas compartidas;
- participar del mismo ciclo de sincronización y drift control.

## Qué lee Antigravity

| Artefacto | Qué aporta | Fuente |
|---|---|---|
| [`GEMINI.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/GEMINI.md) | Reglas raíz para Gemini/Antigravity cuando están presentes. En el snapshot actual aparece como ausente en raíz. | Generado |
| [`.agents/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.agents/) | Directorio nativo del adapter de Antigravity. | Generado |
| [`.agents/rules/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.agents/rules/) | Reglas nativas, incluyendo la variante de `GEMINI.md` usada por el adapter. | Generado |
| [`.agents/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.agents/skills/) | Skills copiados al formato nativo, junto con manifest de generación. | Generado |
| [`adapters/templates/gemini.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/gemini.md.j2) | Plantilla que renderiza las reglas para Gemini/Antigravity. | Adapter |

La página de inventario marca el `GEMINI.md` raíz como ausente en el snapshot actual, pero sí detecta `.agents/rules/` y `.agents/skills/` como salida generada para Antigravity.

## Archivos y carpetas que participan

Los skills nacen en `.github/skills/` y `.github/skills-external/`. Para Antigravity, el motor de sincronización no solo crea enlaces: copia skills a `.agents/skills/` y los distingue con un manifest generado. Esto hace que el entorno nativo pueda leerlos directamente, sin cambiar dónde se gobierna el contenido.

El adapter `gemini.md.j2` transforma las reglas compartidas en instrucciones compatibles con el formato esperado. `make sync-skills` regenera esta estructura y `make check-sync` valida que el resultado siga alineado.

## Fuente de verdad vs generado

La fuente de verdad no está en `.agents/skills/`; está en las reglas y skills gobernados. `.agents/` es una proyección operativa. Si se edita una copia generada, el cambio puede perderse en la siguiente sincronización y además quedar fuera del resto de herramientas.

La regla de estudio es simple: lee `.agents/` para entender cómo Antigravity consume el harness, pero edita `.github/` y `adapters/` para cambiar el harness.

## Mini flujo de estudio

1. Lee el [inventario](../reference-implementation/ml-python-base/inventory.md) y compara el estado de `GEMINI.md`, `.agents/`, `.agents/rules/` y `.agents/skills/`.
2. Lee [skills](../reference-implementation/ml-python-base/skills.md) y observa la diferencia entre enlaces simbólicos para otras herramientas y copias nativas para Antigravity.
3. Revisa [adapters](../reference-implementation/ml-python-base/adapters.md) para ubicar `gemini.md.j2`.
4. Cierra con [control de drift](../reference-implementation/ml-python-base/drift-control.md) para entender cómo se evita que las copias nativas se conviertan en políticas paralelas.

## Documentación oficial

- [Google Antigravity Documentation](https://antigravity.google/docs/home): documentación principal de Antigravity.
- [Agent Skills](https://antigravity.google/docs/skills): cómo Antigravity entiende skills basados en carpetas con `SKILL.md`.
- [Getting Started with Google Antigravity](https://codelabs.developers.google.com/getting-started-google-antigravity): codelab oficial para instalación y conceptos iniciales.

## Referencias

- [`ml-python-base` en GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Inventario de artefactos](../reference-implementation/ml-python-base/inventory.md)
- [Skills gobernados](../reference-implementation/ml-python-base/skills.md)
- [Proyección de adaptadores](../reference-implementation/ml-python-base/adapters.md)
