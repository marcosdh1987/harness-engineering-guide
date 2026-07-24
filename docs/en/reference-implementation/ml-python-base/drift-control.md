# Drift Control & Sync Engine

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [422e35c](https://github.com/marcosdh1987/ml-python-base/commit/422e35ca5e27c50ab3007d7b2e7756bbcae65843) on branch `main`
> - **Last Synced**: `2026-07-24T15:35:41.166285Z`
> - **Reference Artifacts**:
>   - [skills-lock.json](https://github.com/marcosdh1987/ml-python-base/blob/422e35ca5e27c50ab3007d7b2e7756bbcae65843/skills-lock.json)
>   - [src/ml_python_base/skills_sync/](https://github.com/marcosdh1987/ml-python-base/blob/422e35ca5e27c50ab3007d7b2e7756bbcae65843/src/ml_python_base/skills_sync/)
>   - [docs/skills-management.md](https://github.com/marcosdh1987/ml-python-base/blob/422e35ca5e27c50ab3007d7b2e7756bbcae65843/docs/skills-management.md)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Preventing Configuration Drift

With multiple development tools interacting with the repository, configuration and instruction file drift is a major challenge. The template solves this with a centralized declarative engine: `src/ml_python_base/skills_sync/`.

### Configuration and Instruction Synchronization

```
+------------------+         +------------------+
| Governed Skills  |  ---->  |   Tool-Specific  |
| .github/skills/  |         |  Adapters / Views|
+------------------+         +------------------+
         |                            |
         | (Saves Hash)               | (make check-sync)
         v                            v
+------------------+         +------------------+
| skills-lock.json |  <====  | CI Drift Check   |
| (Source of Truth)|         |  (Asserts Hash)  |
+------------------+         +------------------+
```

### Role of `skills-lock.json`
Acts as a cryptographic lock catalog for external skills. When `make sync-skills` is executed:
1. External skills are copied to `.github/skills-external/<skill-name>/`.
2. A cryptographic hash (SHA256) and import timestamp are calculated for each external skill.
3. These metadata records are saved to `skills-lock.json`.
4. During CI, `make check-sync` recalculates the hashes and compares them to `skills-lock.json` and adapter files. If any manual local edits were made to tool-specific skill targets, the hashes mismatch and the pipeline fails.
