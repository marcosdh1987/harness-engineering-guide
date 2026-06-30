# Control de drift y motor de sincronización

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) en la rama `main`
> - **Última sincronización**: `2026-06-30T13:26:01.964630Z`
> - **Artefactos de referencia**:
>   - [skills-lock.json](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/skills-lock.json)
>   - [src/ml_python_base/skills_sync/](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/src/ml_python_base/skills_sync/)
>   - [docs/skills-management.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/docs/skills-management.md)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Prevención de desviaciones de configuración

Con múltiples herramientas de desarrollo interactuando con el repositorio, la desviación (drift) de archivos de configuración e instrucciones es un desafío importante. La plantilla resuelve esto con un motor declarativo centralizado: `src/ml_python_base/skills_sync/`.

### Sincronización de configuración e instrucciones

```
+------------------+         +------------------+
| Governed Skills  |  ---->  |   Tool-Specific  |
| .github/skills/  |         |  Adapters / Views|
+------------------+         +------------------+
         |                            |
         | (Guarda Hash)              | (make check-sync)
         v                            v
+------------------+         +------------------+
| skills-lock.json |  <====  | CI Drift Check   |
| (Source of Truth)|         |  (Valida Hash)   |
+------------------+         +------------------+
```

### Rol de `skills-lock.json`
Actúa como un catálogo de bloqueo criptográfico para los skills externos. Cuando se ejecuta `make sync-skills`:
1. Los skills externos se copian en `.github/skills-external/<skill-name>/`.
2. Se calcula un hash criptográfico (SHA256) y una marca de tiempo de importación para cada skill externo.
3. Estos registros de metadatos se guardan en `skills-lock.json`.
4. Durante la CI, `make check-sync` recalcula los hashes y los compara con `skills-lock.json` y los archivos de adaptadores. Si se realizaron ediciones locales manuales en los targets de los skills específicos de la herramienta, los hashes no coincidirán y el pipeline fallará.
