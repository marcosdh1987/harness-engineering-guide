# Control de drift y motor de sincronización

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [587ac29](https://github.com/marcosdh1987/ml-python-base/commit/587ac29d30cb50d5c307f41e942c14d3f0bba298) en la rama `main`
> - **Última sincronización**: `2026-06-28T00:52:06.059621Z`
> - **Artefactos de referencia**:
>   - [skills-lock.json](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/skills-lock.json)
>   - [src/ml_python_base/skills_sync/](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/src/ml_python_base/skills_sync/)
>   - [docs/skills-management.md](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/docs/skills-management.md)
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
