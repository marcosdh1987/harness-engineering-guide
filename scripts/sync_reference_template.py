#!/usr/bin/env python3
"""
scripts/sync_reference_template.py

Synchronizes documentation with the marcosdh1987/ml-python-base reference implementation.
This script is idempotent. It:
1. Locates the reference repository (local path or git clone).
2. Extracts Git metadata (commit SHA and default branch).
3. Inventories important harness artifacts.
4. Generates a machine-readable JSON snapshot.
5. Generates English and Spanish reference implementation markdown pages.
6. Generates English and Spanish evidence pages from evidence-sources.yml.
"""

import os
import sys
import json
import subprocess
import tempfile
import shutil
import argparse
from datetime import datetime

# Import yaml (which is available in the environment as MkDocs depends on it)
try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Please install it with 'pip install pyyaml'.")
    sys.exit(1)

# Configuration
REPO_URL = "https://github.com/marcosdh1987/ml-python-base"
DEFAULT_LOCAL_PATH = "/Users/marcossoto/Documents/example/ml-python-base"
SNAPSHOT_PATH = "docs/reference-data/ml-python-base-snapshot.json"
EVIDENCE_YAML_PATH = "docs/reference-data/evidence-sources.yml"

ARTIFACT_FAMILIES = [
    {
        "path": "README.md",
        "purpose": "Main entry point and documentation overview of the template repository.",
        "tool_target": "General Developers",
        "source_of_truth": "Yes",
    },
    {
        "path": "CLAUDE.md",
        "purpose": "Claude Code integration profile, tool guidelines, and command policies.",
        "tool_target": "Claude Code",
        "source_of_truth": "Yes",
    },
    {
        "path": "OPENCODE.md",
        "purpose": "OpenCode configuration profile, MCP tool usage instructions, and safety rules.",
        "tool_target": "OpenCode",
        "source_of_truth": "Yes",
    },
    {
        "path": "GEMINI.md",
        "purpose": "GEMINI rules mapping governed skills with @.github prefix reference syntax (if present in root).",
        "tool_target": "Gemini / Antigravity",
        "source_of_truth": "Generated",
    },
    {
        "path": "AGENTS.md",
        "purpose": "Codex subagent profile defining standard coding roles and coordination paths.",
        "tool_target": "Codex / OpenAI Agents",
        "source_of_truth": "Yes",
    },
    {
        "path": ".github/copilot-instructions.md",
        "purpose": "Repository-wide custom instructions for GitHub Copilot.",
        "tool_target": "GitHub Copilot",
        "source_of_truth": "Generated",
    },
    {
        "path": ".github/architecture.md",
        "purpose": "Core design, layering boundaries (Domain, Application, Infrastructure), and SRP guidance.",
        "tool_target": "All AI Tools",
        "source_of_truth": "Yes",
    },
    {
        "path": ".github/standards.md",
        "purpose": "Coding guidelines (Python, uv, Makefile, absolute imports, Ruff, Pydantic, mypy, validation checklist).",
        "tool_target": "All AI Tools",
        "source_of_truth": "Yes",
    },
    {
        "path": ".github/domain-boundaries.md",
        "purpose": "Workspace separation (src, tests, notebooks) and mutable/immutable data zones.",
        "tool_target": "All AI Tools",
        "source_of_truth": "Yes",
    },
    {
        "path": ".github/automation.md",
        "purpose": "Level 3 automation checks, read-only CI quality gates, and uv.lock drift guards.",
        "tool_target": "All AI Tools",
        "source_of_truth": "Yes",
    },
    {
        "path": ".github/orchestration.md",
        "purpose": "Level 4 orchestration, plan-first rules, diff reviews, and skill invocation gates.",
        "tool_target": "All AI Tools",
        "source_of_truth": "Yes",
    },
    {
        "path": ".github/skills/",
        "purpose": "Governed internal skills defining repeatable agent workflows.",
        "tool_target": "Skills Sync Engine",
        "source_of_truth": "Yes",
    },
    {
        "path": ".github/skills-external/",
        "purpose": "Imported external skills managed by the skills sync engine.",
        "tool_target": "Skills Sync Engine",
        "source_of_truth": "Yes (Synced source)",
    },
    {
        "path": ".github/agents/",
        "purpose": "Governed agent definitions mapping workspace roles (documenter, orchestrator, reviewer, tester, etc.).",
        "tool_target": "Skills Sync Engine",
        "source_of_truth": "Yes",
    },
    {
        "path": ".claude/",
        "purpose": "Claude Code workspace settings, commands, hooks, and native symlinked skills.",
        "tool_target": "Claude Code",
        "source_of_truth": "Generated (from settings/hooks)",
    },
    {
        "path": ".claude/skills/",
        "purpose": "Symlinks pointing to governed and external skills for Claude Code discovery.",
        "tool_target": "Claude Code",
        "source_of_truth": "Generated",
    },
    {
        "path": ".claude/hooks/",
        "purpose": "Claude session hooks like session_start.sh and stop_nudge.sh.",
        "tool_target": "Claude Code",
        "source_of_truth": "Yes",
    },
    {
        "path": ".opencode/",
        "purpose": "OpenCode workspace configuration, modules, and native adapter links.",
        "tool_target": "OpenCode",
        "source_of_truth": "Generated",
    },
    {
        "path": ".opencode/skills/",
        "purpose": "Symlinks pointing to governed skills for OpenCode discovery.",
        "tool_target": "OpenCode",
        "source_of_truth": "Generated",
    },
    {
        "path": ".codex/",
        "purpose": "Codex adapter configuration and local workspace hooks.",
        "tool_target": "Codex",
        "source_of_truth": "Generated",
    },
    {
        "path": ".codex/skills/",
        "purpose": "Symlinks pointing to governed skills for Codex discovery.",
        "tool_target": "Codex",
        "source_of_truth": "Generated",
    },
    {
        "path": ".agents/",
        "purpose": "Antigravity native adapter directory.",
        "tool_target": "Antigravity",
        "source_of_truth": "Generated",
    },
    {
        "path": ".agents/skills/",
        "purpose": "Copied native Antigravity skills with a generated manifest.",
        "tool_target": "Antigravity",
        "source_of_truth": "Generated",
    },
    {
        "path": ".agents/rules/",
        "purpose": "Antigravity rules directory containing GEMINI.md.",
        "tool_target": "Antigravity",
        "source_of_truth": "Generated",
    },
    {
        "path": "adapters/",
        "purpose": "Declarative registry (registry.toml) and templates for multi-tool adapter rendering.",
        "tool_target": "Skills Sync Engine",
        "source_of_truth": "Yes",
    },
    {
        "path": "src/ml_python_base/skills_sync/",
        "purpose": "Python-based declarative engine managing link projection, agent mapping, and hash-based drift checks.",
        "tool_target": "Skills Sync Engine",
        "source_of_truth": "Yes",
    },
    {
        "path": "skills-lock.json",
        "purpose": "Hash-locked catalog of synced external skills ensuring CI reproducibility.",
        "tool_target": "Skills Sync Engine",
        "source_of_truth": "Generated / Lock",
    },
    {
        "path": "Makefile",
        "purpose": "Standardized entry point for local and CI quality gates and skills synchronization.",
        "tool_target": "General Developers",
        "source_of_truth": "Yes",
    },
    {
        "path": "docs/skills-management.md",
        "purpose": "Explanatory guide on the skills sync engine, ideation routing, and adapter drift gates.",
        "tool_target": "General Developers",
        "source_of_truth": "Yes",
    }
]

def run_cmd(args, cwd=None):
    try:
        return subprocess.check_output(args, cwd=cwd, stderr=subprocess.DEVNULL).decode("utf-8").strip()
    except Exception:
        return ""

def locate_repository(local_path_arg=None):
    """
    Finds the reference repository. Checks:
    1. CLI Argument
    2. Environment variable REF_REPO_PATH
    3. Default local path
    4. Otherwise, clones to a temporary directory in workspace.
    """
    path = local_path_arg or os.environ.get("REF_REPO_PATH") or DEFAULT_LOCAL_PATH
    if os.path.isdir(path) and os.path.exists(os.path.join(path, ".git")):
        print(f"✅ Using reference repository from local path: {path}")
        return path, False

    # Clone fallback
    temp_dir = os.path.join(os.getcwd(), "docs", "reference-data", "temp_clone_repo")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    print(f"🔄 Reference repository not found locally. Cloning {REPO_URL} into temporary path...")
    subprocess.check_call(["git", "clone", REPO_URL, temp_dir])
    return temp_dir, True

def scan_repository(repo_path):
    # Get Git metadata
    commit_sha = run_cmd(["git", "rev-parse", "HEAD"], cwd=repo_path)
    if not commit_sha:
        commit_sha = "unknown"
    
    branch = run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_path)
    if not branch:
        branch = "main"

    # Inventory scanning
    inventory = []
    for item in ARTIFACT_FAMILIES:
        rel_path = item["path"]
        full_path = os.path.join(repo_path, rel_path)
        exists = os.path.exists(full_path)
        is_dir = os.path.isdir(full_path) if exists else False
        
        size_or_children = "Not present in current snapshot"
        if exists:
            if is_dir:
                try:
                    children = os.listdir(full_path)
                    size_or_children = f"{len(children)} items"
                except Exception:
                    size_or_children = "Error listing"
            else:
                try:
                    size_bytes = os.path.getsize(full_path)
                    size_or_children = f"{size_bytes} bytes"
                except Exception:
                    size_or_children = "Error size"
                    
        inventory.append({
            "path": rel_path,
            "exists": exists,
            "is_dir": is_dir,
            "size_or_children": size_or_children,
            "purpose": item["purpose"],
            "tool_target": item["tool_target"],
            "source_of_truth": item["source_of_truth"]
        })

    # Detailed Skills scan
    skills = []
    for skill_type, dir_path in [("internal", ".github/skills"), ("external", ".github/skills-external")]:
        full_dir = os.path.join(repo_path, dir_path)
        if os.path.exists(full_dir):
            for child in os.listdir(full_dir):
                child_path = os.path.join(full_dir, child)
                if skill_type == "internal" and child.endswith(".md") and child != "README.md":
                    skill_name = child[:-3]
                    skills.append({
                        "name": skill_name,
                        "type": "internal",
                        "path": f"{dir_path}/{child}",
                        "source_link": f"{REPO_URL}/blob/{commit_sha}/{dir_path}/{child}"
                    })
                elif skill_type == "external" and os.path.isdir(child_path):
                    skill_file = os.path.join(child_path, "SKILL.md")
                    if os.path.exists(skill_file):
                        skills.append({
                            "name": child,
                            "type": "external",
                            "path": f"{dir_path}/{child}/SKILL.md",
                            "source_link": f"{REPO_URL}/blob/{commit_sha}/{dir_path}/{child}/SKILL.md"
                        })

    # Detailed Agents scan
    agents = []
    agents_dir = os.path.join(repo_path, ".github/agents")
    if os.path.exists(agents_dir):
        for child in os.listdir(agents_dir):
            if child.endswith(".md") and child != "README.md":
                agent_name = child[:-3]
                agents.append({
                    "name": agent_name,
                    "path": f".github/agents/{child}",
                    "source_link": f"{REPO_URL}/blob/{commit_sha}/.github/agents/{child}"
                })

    # Detailed Hooks scan
    hooks = []
    hooks_dir = os.path.join(repo_path, ".claude/hooks")
    if os.path.exists(hooks_dir):
        for child in os.listdir(hooks_dir):
            if child.endswith(".sh"):
                hooks.append({
                    "name": child,
                    "path": f".claude/hooks/{child}",
                    "source_link": f"{REPO_URL}/blob/{commit_sha}/.claude/hooks/{child}"
                })

    # Detailed Adapters scan
    adapters = []
    registry_path = os.path.join(repo_path, "adapters/registry.toml")
    if os.path.exists(registry_path):
        adapters.append({
            "name": "registry.toml",
            "path": "adapters/registry.toml",
            "source_link": f"{REPO_URL}/blob/{commit_sha}/adapters/registry.toml"
        })
    templates_dir = os.path.join(repo_path, "adapters/templates")
    if os.path.exists(templates_dir):
        for child in os.listdir(templates_dir):
            adapters.append({
                "name": f"template: {child}",
                "path": f"adapters/templates/{child}",
                "source_link": f"{REPO_URL}/blob/{commit_sha}/adapters/templates/{child}"
            })

    return {
        "repo_url": REPO_URL,
        "commit_sha": commit_sha,
        "branch": branch,
        "last_sync": datetime.utcnow().isoformat() + "Z",
        "inventory": inventory,
        "skills": skills,
        "agents": agents,
        "hooks": hooks,
        "adapters": adapters
    }

def save_snapshot(data):
    os.makedirs(os.path.dirname(SNAPSHOT_PATH), exist_ok=True)
    with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"💾 Snapshot saved to {SNAPSHOT_PATH}")

def load_evidence_sources():
    if not os.path.exists(EVIDENCE_YAML_PATH):
        print(f"⚠️ Evidence YAML path {EVIDENCE_YAML_PATH} not found!")
        return []
    with open(EVIDENCE_YAML_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Markdown rendering helpers
def render_header(lang, title, data, file_paths=None):
    sha = data["commit_sha"]
    short_sha = sha[:7]
    ts = data["last_sync"]
    
    if lang == "en":
        lines = [
            f"# {title}",
            "",
            "> [!NOTE]",
            f"> **Generated content**: This page is automatically generated from the template snapshot.",
            f"> - **Reference Commit**: [{short_sha}]({REPO_URL}/commit/{sha}) on branch `{data['branch']}`",
            f"> - **Last Synced**: `{ts}`",
        ]
        if file_paths:
            lines.append("> - **Reference Artifacts**:")
            for p in file_paths:
                lines.append(f">   - [{p}]({REPO_URL}/blob/{sha}/{p})")
        lines.append("> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*")
    else:
        lines = [
            f"# {title}",
            "",
            "> [!NOTE]",
            f"> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.",
            f"> - **Commit de referencia**: [{short_sha}]({REPO_URL}/commit/{sha}) en la rama `{data['branch']}`",
            f"> - **Última sincronización**: `{ts}`",
        ]
        if file_paths:
            lines.append("> - **Artefactos de referencia**:")
            for p in file_paths:
                lines.append(f">   - [{p}]({REPO_URL}/blob/{sha}/{p})")
        lines.append("> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*")
    
    lines.append("")
    return "\n".join(lines)

def render_inventory_page(lang, data):
    title = "Template Artifacts Inventory" if lang == "en" else "Inventario de artefactos de plantilla"
    content = render_header(lang, title, data)
    
    if lang == "en":
        content += """## Artifact Catalog

This catalog outlines all structural, governance, and adaptation artifacts found in the template. It lists their location, purpose, and role in Harness Engineering.

| Artifact Path | Status | Size / Children | Purpose / Description | Tool Target | Source of Truth | Source Link |
|---|---|---|---|---|---|---|
"""
    else:
        content += """## Catálogo de artefactos

Este catálogo detalla todos los artefactos estructurales, de gobernanza y de adaptación que se encuentran en la plantilla. Lista su ubicación, propósito y rol en Harness Engineering.

| Artifact Path | Estado | Tamaño / Hijos | Propósito / Descripción | Tool Target | Source of Truth | Enlace de origen |
|---|---|---|---|---|---|---|
"""

    for item in data["inventory"]:
        status = "Present" if item["exists"] else "Absent"
        if lang != "en":
            status = "Presente" if item["exists"] else "Ausente"
            
        git_link = f"[Source]({REPO_URL}/blob/{data['commit_sha']}/{item['path']})"
        if item["is_dir"]:
            git_link = f"[Source]({REPO_URL}/tree/{data['commit_sha']}/{item['path']})"
            
        content += f"| `{item['path']}` | {status} | `{item['size_or_children']}` | {item['purpose']} | `{item['tool_target']}` | {item['source_of_truth']} | {git_link} |\n"
        
    return content

def render_rules_page(lang, data):
    title = "Governance & Rules System" if lang == "en" else "Sistema de reglas y gobernanza"
    rules_files = [
        ".github/architecture.md",
        ".github/standards.md",
        ".github/domain-boundaries.md",
        ".github/automation.md",
        ".github/orchestration.md"
    ]
    content = render_header(lang, title, data, rules_files)
    
    if lang == "en":
        content += """## Structured Governance

The reference implementation structures governance into five dedicated rule files located under `.github/`. They establish Level 3 (Automation) and Level 4 (Orchestration) quality gates that AI coding tools must conform to.

### 1. Architecture Governance (`.github/architecture.md`)
Defines the architectural layout and module boundaries to prevent design drift.
- **Key Principle**: Enforces Single Responsibility Principle (SRP) and separation of business logic from infrastructure.
- **Preferred Layering**: Enforces a Clean Architecture layout:
  1. **Domain layer**: entities, value objects, core rules (must not depend on infrastructure).
  2. **Application layer**: use cases and orchestration.
  3. **Infrastructure layer**: frameworks, database adapters, external providers, APIs.

### 2. Engineering Standards (`.github/standards.md`)
Details development guidelines, language policies, tool execution pathways, and pre-finalization checklists.
- **Language Policy**: Interaction language follows user language, but all code artifacts (identifiers, docstrings, comments, generated documentation) **must remain in English**.
- **Tool Command Policy**: Prioritizes `Makefile` targets. Never execute `pip install` directly; use `uv` workflows.
- **Validation Checklist**:
  1. Code artifacts are in English.
  2. Relevant quality checks ran (`make check` or targeted tests).
  3. Data flows respect boundaries.
  4. Changes include updating documentation under `docs/`.

### 3. Domain Boundaries (`.github/domain-boundaries.md`)
Defines repository zones and data isolation boundaries to limit model generation scopes.
- **Repository Zones**: `src/` (production code), `tests/` (testing), `notebooks/` (prototyping).
- **Data Zones**: Enforces read-only immutable raw data under `data/raw/` and transform-only features under `data/processed/`.

### 4. Automation Policy (`.github/automation.md`)
Defines Level 3 enforcement so quality is verified programmatically and does not depend on model compliance.
- **CI is Read-Only**: CI only verifies and never mutates the working tree. Targets like `make format` are strictly local.
- **Drift Guard**: `make check` executes `uv sync --locked --exact` to align the environment exactly with the lockfile, preventing undeclared dependency leaks.

### 5. Orchestration Policy (`.github/orchestration.md`)
Establishes Level 4 workflow execution guidelines for complex programming tasks.
- **Plan-First**: Requires drawing an explicit implementation plan before writing code.
- **Diff Review**: Mandates model and developer reviews of Git diffs before finalizing to prune boundary violations.
- **Orchestration Route**: Prioritizes internal skill execution over generic model generation.
"""
    else:
        content += """## Gobernanza estructurada

La implementación de referencia estructura la gobernanza en cinco archivos de reglas dedicados ubicados en `.github/`. Estos establecen los quality gates de Nivel 3 (Automatización) y Nivel 4 (Orquestación) que las herramientas de codificación de IA deben cumplir.

### 1. Gobernanza de arquitectura (`.github/architecture.md`)
Define el esquema arquitectónico y los límites de los módulos para evitar desviaciones en el diseño.
- **Principio clave**: Aplica el Principio de Responsabilidad Única (SRP) y separa la lógica de negocio de la infraestructura.
- **Capas preferidas**: Impone un esquema de Arquitectura Limpia (Clean Architecture):
  1. **Domain layer**: entidades, objetos de valor y reglas principales (no debe depender de la infraestructura).
  2. **Application layer**: casos de uso y orquestación.
  3. **Infrastructure layer**: frameworks, adaptadores de base de datos, proveedores externos, APIs.

### 2. Estándares de ingeniería (`.github/standards.md`)
Detalla pautas de desarrollo, políticas de idioma, rutas de ejecución de herramientas y checklists previas a la finalización.
- **Política de idioma**: El idioma de interacción se adapta al usuario, pero todos los artefactos de código (identificadores, docstrings, comentarios, documentación técnica generada) **deben permanecer en inglés**.
- **Política de comandos de herramientas**: Prioriza los targets del `Makefile`. Nunca ejecute `pip install` directamente; use los flujos de `uv`.
- **Checklist de validación**:
  1. Los artefactos de código están en inglés.
  2. Se ejecutaron los controles de calidad correspondientes (`make check` o pruebas específicas).
  3. Los flujos de datos respetan los límites de zona.
  4. Los cambios en la implementación incluyen la actualización de la documentación en `docs/`.

### 3. Límites de dominio (`.github/domain-boundaries.md`)
Define las zonas del repositorio y los límites de aislamiento de datos para restringir el alcance de generación de los modelos.
- **Zonas del repositorio**: `src/` (código de producción), `tests/` (pruebas), `notebooks/` (prototipos).
- **Zonas de datos**: Impone datos de origen inmutables de solo lectura en `data/raw/` y transformaciones solo en `data/processed/`.

### 4. Política de automatización (`.github/automation.md`)
Define el cumplimiento de Nivel 3 para que la calidad se verifique mediante programación y no dependa del comportamiento del modelo.
- **La CI es de solo lectura**: La CI solo verifica y nunca modifica el árbol de trabajo. Comandos como `make format` son estrictamente locales.
- **Guardia de drift**: `make check` ejecuta `uv sync --locked --exact` para alinear el entorno exactamente con el archivo de bloqueo, evitando fugas de dependencias no declaradas.

### 5. Política de orquestación (`.github/orchestration.md`)
Establece pautas de ejecución de flujos de trabajo de Nivel 4 para tareas de programación complejas.
- **Planificar primero**: Requiere elaborar un plan de implementación explícito antes de escribir código.
- **Revisión de diffs**: Exige revisiones del diff de Git por parte del modelo y del desarrollador antes de finalizar para eliminar violaciones de límites.
- **Ruta de orquestación**: Prioriza la ejecución de skills internos sobre la generación genérica por parte de los modelos.
"""
    return content

def render_skills_page(lang, data):
    title = "Governed Skills" if lang == "en" else "Skills gobernados"
    content = render_header(lang, title, data, [".github/skills/", ".github/skills-external/", "skills-lock.json"])
    
    if lang == "en":
        content += """## Skills vs Prompts

In Harness Engineering, a **Skill** represents a structured, versioned, and executable procedure (typically a `SKILL.md` markdown file containing metadata, instructions, and rules) that handles a repeatable software development lifecycle task. 
Unlike ad-hoc or interactive chat prompts, a skill is a **durable system asset** that is link-projected to native tools.

### Discovered Skills Inventory

The template contains both internal skills (curated by the template) and external skills (synced and hash-locked).

| Skill Name | Type | Path | GitHub Link |
|---|---|---|---|
"""
    else:
        content += """## Skills vs Prompts

En Harness Engineering, un **Skill** representa un procedimiento estructurado, versionado y ejecutable (generalmente un archivo markdown `SKILL.md` que contiene metadatos, instrucciones y reglas) que maneja una tarea repetible del ciclo de vida del desarrollo de software.
A diferencia de los prompts de chat interactivos o ad-hoc, un skill es un **activo duradero del sistema** que se proyecta mediante enlaces a herramientas nativas.

### Inventario de skills detectados

La plantilla contiene tanto skills internos (curados por la plantilla) como externos (sincronizados y bloqueados mediante hash).

| Nombre de la Skill | Tipo | Ruta | Enlace de GitHub |
|---|---|---|---|
"""

    for s in data["skills"]:
        content += f"| `{s['name']}` | {s['type']} | `{s['path']}` | [Link]({s['source_link']}) |\n"

    if lang == "en":
        content += """
### Skill Duplicate Detection and Resolution

Because different tool adapters (Claude Code, OpenCode, Antigravity, Codex) have different native search folders, the sync engine projects these skills via:
- **Claude Code**: Symlinked to `.claude/skills/<skill-name>/SKILL.md`
- **OpenCode**: Symlinked to `.opencode/skills/<skill-name>/SKILL.md`
- **Antigravity**: Copied directly to `.agents/skills/<skill-name>/SKILL.md` (distinguished via a `.generated-manifest.tsv`).

**Resolution of duplicates**: The central engine (`skills_sync`) acts as the single compiler. Skills must only be edited under `.github/skills/` or external packages. The sync engine automatically overwrites any edits inside the adapter folders during `make sync-skills`, preventing duplicate conflicts or local modifications from diverging.
"""
    else:
        content += """
### Detección y resolución de duplicados de skills

Debido a que diferentes adaptadores de herramientas (Claude Code, OpenCode, Antigravity, Codex) tienen diferentes carpetas de búsqueda nativas, el motor de sincronización proyecta estos skills a través de:
- **Claude Code**: Enlazado simbólicamente a `.claude/skills/<skill-name>/SKILL.md`
- **OpenCode**: Enlazado simbólicamente a `.opencode/skills/<skill-name>/SKILL.md`
- **Antigravity**: Copiado directamente a `.agents/skills/<skill-name>/SKILL.md` (identificado mediante un archivo `.generated-manifest.tsv`).

**Resolución de duplicados**: El motor central (`skills_sync`) actúa como el único compilador. Los skills solo deben editarse bajo `.github/skills/` o en paquetes externos. El motor de sincronización sobrescribe automáticamente cualquier edición dentro de las carpetas de adaptadores durante `make sync-skills`, evitando conflictos de duplicados o divergencias de modificaciones locales.
"""
    return content

def render_agents_page(lang, data):
    title = "Autonomous Agents & Roles" if lang == "en" else "Agentes autónomos y roles"
    content = render_header(lang, title, data, [".github/agents/"])
    
    if lang == "en":
        content += """## Governed Agent Roles

The reference implementation defines specialized agent personas under `.github/agents/`. The sync engine compiles and projects these definitions into the target subagent configurations (e.g. Claude Code Markdown subagents, Codex TOML config files, etc.).

### Discovered Agent Personas

| Agent Persona | Configuration Path | GitHub Link |
|---|---|---|
"""
    else:
        content += """## Roles de agentes gobernados

La implementación de referencia define personas de agentes especializados bajo `.github/agents/`. El motor de sincronización compila y proyecta estas definiciones en las configuraciones de subagentes objetivo (por ejemplo, subagentes Markdown de Claude Code, archivos de configuración TOML de Codex, etc.).

### Personas de agentes detectadas

| Persona del agente | Ruta de configuración | Enlace de GitHub |
|---|---|---|
"""

    for a in data["agents"]:
        content += f"| `{a['name']}` | `{a['path']}` | [Link]({a['source_link']}) |\n"

    if lang == "en":
        content += """
### Agent Roles and Capabilities

Based on the metadata, the template maps the following roles:
- **orchestrator**: Coordinates tasks across specialized subagents and tracks implementation checklists.
- **planner**: Analyzes repository structure, parses requirements, and drafts implementation plans.
- **documenter**: Manages the generated documentation sites and ensures compliance with readability standards.
- **reviewer**: Conducts strict code quality reviews against architecture and domain boundaries.
- **tester**: Generates unit, integration, and E2E test suites based on changes.
- **implementer**: Handles actual code modifications and applies clean code patterns.
"""
    else:
        content += """
### Roles y capacidades de los agentes

Según los metadatos de la plantilla, se asignan los siguientes roles:
- **orchestrator**: Coordina tareas entre subagentes especializados y realiza el seguimiento de checklists de implementación.
- **planner**: Analiza la estructura del repositorio, interpreta requisitos y elabora planes de implementación.
- **documenter**: Gestiona los sitios de documentación generados y garantiza el cumplimiento de los estándares de legibilidad.
- **reviewer**: Realiza revisiones estrictas de calidad de código frente a los límites de arquitectura y dominio.
- **tester**: Genera suites de pruebas unitarias, de integración y E2E basadas en los cambios.
- **implementer**: Se encarga de las modificaciones de código reales y aplica patrones de código limpio.
"""
    return content

def render_hooks_page(lang, data):
    title = "Session Hooks & Guardrails" if lang == "en" else "Hooks de sesión y guardrails"
    content = render_header(lang, title, data, [".claude/hooks/"])
    
    if lang == "en":
        content += """## Hooks as Quality Guardrails

Hooks are executable scripts triggered automatically at key interaction boundaries. They integrate external validation checks, state diagnostics, and environment compliance checks directly into the agent session loop.

### Discovered Hook Files

| Hook Name | Target Path | Purpose | Link |
|---|---|---|---|
"""
    else:
        content += """## Hooks como guardrails de calidad

Los hooks son scripts ejecutables que se activan automáticamente en puntos clave de la interacción. Integran verificaciones de validación externas, diagnósticos de estado y controles de conformidad del entorno directamente en el ciclo de sesión del agente.

### Archivos de hooks detectados

| Nombre del Hook | Ruta de destino | Propósito | Enlace |
|---|---|---|---|
"""

    for h in data["hooks"]:
        purpose = "Cleans up session leftovers, warns about untracked files"
        if "start" in h["name"]:
            purpose = "Runs checks on environment setup, local lock state, and checks for uncommitted drift"
        elif "nudge" in h["name"]:
            purpose = "Warns developer of drift or uncommitted changes when the session remains idle"
            
        content += f"| `{h['name']}` | `{h['path']}` | {purpose} | [Link]({h['source_link']}) |\n"

    if not data["hooks"]:
        if lang == "en":
            content += "| *No explicit hooks found* | | Not present in current snapshot | |\n"
        else:
            content += "| *No se encontraron hooks explícitos* | | No presente en el snapshot actual | |\n"

    if lang == "en":
        content += """
### Configuration Settings and Integrations

If explicit shell hooks are not utilized, the integration points are defined in the tool configuration files:
- **Claude Code**: `.claude/settings.json` controls command execution approvals, system prompt modifiers, and tool paths.
- **OpenCode**: `opencode.json` defines tool permissions, network rules, and workspace directory mappings.
- **Antigravity**: `.agents/rules/GEMINI.md` binds workspace permissions and orchestrates agent execution.
"""
    else:
        content += """
### Ajustes de configuración e integraciones

Si no se utilizan hooks de shell explícitos, los puntos de integración se definen en los archivos de configuración de las herramientas:
- **Claude Code**: `.claude/settings.json` controla las aprobaciones de ejecución de comandos, modificadores de prompt de sistema y rutas de herramientas.
- **OpenCode**: `opencode.json` define los permisos de herramientas, reglas de red y asignaciones de directorios de espacio de trabajo.
- **Antigravity**: `.agents/rules/GEMINI.md` vincula permisos de espacio de trabajo y orquesta la ejecución de agentes.
"""
    return content

def render_adapters_page(lang, data):
    title = "Tool Adapters Projection" if lang == "en" else "Proyección de adaptadores de herramientas"
    content = render_header(lang, title, data, ["adapters/", "CLAUDE.md", "OPENCODE.md", "AGENTS.md", ".github/copilot-instructions.md"])
    
    if lang == "en":
        content += """## Adapters Composition

An **Adapter** acts as the glue layer between governed central rules and the tool-specific configuration formats.
Each adapter is composed of two distinct regions:
1. **Hand-written Governance Prose**: Explains project structure, rules, and general policies.
2. **Machine-Managed Skills Region**: Written dynamically by the synchronization engine between two unique markdown comments:
   ```markdown
   <!-- BEGIN GENERATED SKILLS (managed by skills_sync; do not edit) -->
   ...
   <!-- END GENERATED SKILLS -->
   ```

### Discovered Adapter Configurations

| Adapter / Template Name | Path | Target Tool | Link |
|---|---|---|---|
"""
    else:
        content += """## Composición de adaptadores

Un **Adapter** actúa como la capa de unión entre las reglas centrales gobernadas y los formatos de configuración específicos de cada herramienta.
Cada adaptador se compone de dos regiones distintas:
1. **Gobernanza escrita a mano**: Explica la estructura del proyecto, las reglas y las políticas generales.
2. **Región de skills gestionada por máquina**: Escrita dinámicamente por el motor de sincronización entre dos comentarios markdown únicos:
   ```markdown
   <!-- BEGIN GENERATED SKILLS (managed by skills_sync; do not edit) -->
   ...
   <!-- END GENERATED SKILLS -->
   ```

### Configuraciones de adaptadores detectadas

| Nombre del adaptador / plantilla | Ruta | Herramienta de destino | Enlace |
|---|---|---|---|
"""

    for ad in data["adapters"]:
        tool = "Multiple"
        if "claude" in ad["name"]:
            tool = "Claude Code"
        elif "opencode" in ad["name"]:
            tool = "OpenCode"
        elif "gemini" in ad["name"] or "antigravity" in ad["name"]:
            tool = "Antigravity"
        elif "copilot" in ad["name"]:
            tool = "GitHub Copilot"
        elif "agents" in ad["name"] or "codex" in ad["name"]:
            tool = "Codex"
            
        content += f"| `{ad['name']}` | `{ad['path']}` | {tool} | [Link]({ad['source_link']}) |\n"

    return content

def render_automation_page(lang, data):
    title = "Makefile Automation Workflows" if lang == "en" else "Flujos de automatización del Makefile"
    content = render_header(lang, title, data, ["Makefile"])
    
    if lang == "en":
        content += """## Command Automation Matrix

The template repository centralizes all local development commands and quality gates in a single `Makefile` utilizing `uv` for environment management.

### Key Makefile Targets

| Target Command | Execution Nature | Core Purpose / Actions |
|---|---|---|
| `make install` | Local-Mutating | Installs `uv`, pins Python version, and builds the local `.venv` exactly according to `uv.lock`. |
| `make format` | Local-Mutating | Automatically runs Ruff formatting and import sorting across `src/`, `tests/`, and `scripts/`. |
| `make fix` | Local-Mutating | Applies safe linter autofixes and formatting. |
| `make check` | CI-Safe (Read-Only) | **CI Quality Gate**: Lock-syncs `.venv` with `uv sync --locked --exact`, checks Ruff formatting/linting, executes security checks (Bandit), runs Mypy type-checking, and executes tests with coverage. |
| `make sync-skills` | Local-Mutating | Triggers the centralized sync engine to link skills, project agents, and rewrite generated adapter skill regions. |
| `make check-sync` | CI-Safe (Read-Only) | **CI Drift Gate**: Validates that no local adapter files, native skill links, or manifests have drifted from the governed sources. |
| `make ci` | CI-Safe (Read-Only) | Runs the complete CI pipeline: `make check` followed by `make check-sync`. |

### Local-Mutating vs CI-Safe (Read-Only) Workflows

- **CI-Safe (Read-Only)** targets never modify files in the working directory (besides environment sync inside `.venv`). They assert state and fail fast if checks fail.
- **Local-Mutating** targets write changes, formats, or refactors back to the disk. These should only be run by developers locally.
"""
    else:
        content += """## Matriz de automatización de comandos

El repositorio de plantilla centraliza todos los comandos de desarrollo local y quality gates en un único `Makefile` utilizando `uv` para la gestión del entorno.

### Targets clave del Makefile

| Comando Target | Naturaleza de ejecución | Propósito principal / Acciones |
|---|---|---|
| `make install` | Local-Modificador | Instala `uv`, fija la versión de Python y construye el `.venv` local exactamente de acuerdo con `uv.lock`. |
| `make format` | Local-Modificador | Ejecuta automáticamente el formateo de Ruff y la ordenación de imports en `src/`, `tests/` y `scripts/`. |
| `make fix` | Local-Modificador | Aplica correcciones automáticas seguras del linter y formateo. |
| `make check` | Seguro para CI (Lectura) | **Gate de calidad de CI**: Sincroniza el `.venv` con `uv sync --locked --exact`, verifica el formato/lint de Ruff, ejecuta controles de seguridad (Bandit), realiza la comprobación de tipos de Mypy y ejecuta pruebas con cobertura. |
| `make sync-skills` | Local-Modificador | Activa el motor de sincronización centralizado para enlazar skills, proyectar agentes y reescribir las regiones de skills generadas. |
| `make check-sync` | Seguro para CI (Lectura) | **Gate de drift de CI**: Valida que ningún adaptador local, enlace de skill nativo o manifiesto se haya desviado de las fuentes gobernadas. |
| `make ci` | Seguro para CI (Lectura) | Ejecuta el pipeline completo de CI: `make check` seguido de `make check-sync`. |

### Flujos de trabajo locales modificadores vs seguros para CI (solo lectura)

- Los targets **Seguros para CI (solo lectura)** nunca modifican archivos en el directorio de trabajo (excepto la sincronización del entorno dentro de `.venv`). Verifican el estado y fallan rápidamente si fallan los controles.
- Los targets **Locales modificadores** escriben cambios, formateos o refactorizaciones en el disco. Solo deben ser ejecutados por desarrolladores de forma local.
"""
    return content

def render_drift_control_page(lang, data):
    title = "Drift Control & Sync Engine" if lang == "en" else "Control de drift y motor de sincronización"
    content = render_header(lang, title, data, ["skills-lock.json", "src/ml_python_base/skills_sync/", "docs/skills-management.md"])
    
    if lang == "en":
        content += """## Preventing Configuration Drift

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
"""
    else:
        content += """## Prevención de desviaciones de configuración

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
"""
    return content

def render_working_loop_page(lang, data):
    title = "Harness Working Loop" if lang == "en" else "Ciclo de trabajo del Harness"
    content = render_header(lang, title, data)
    
    if lang == "en":
        content += """## Development Cycle Steps

The reference implementation enforces a highly structured, repeatable software development loop. This cycle ensures all modifications undergo rigorous verification before merge.

```mermaid
graph TD
    A[1. Plan: Write implementation plan] --> B[2. Apply Rules & Skills]
    B --> C[3. Modify Code: Execute changes]
    C --> D[4. Validate Locally: make check]
    D --> E[5. Sync Adapters: make sync-skills]
    E --> F[6. Review Diff: Check boundaries]
    F --> G[7. Update Documentation]
    G --> H[8. Merge: Submit PR & run CI]
```

### Step Breakdown

1. **Plan**: Never write code directly. Draft an `implementation_plan.md` first, listing affected components and verification commands.
2. **Apply Rules & Skills**: Verify if an existing internal skill covers the change scope (e.g. `create_domain_contract`).
3. **Modify Code**: Execute the code modifications inside your local directory.
4. **Validate Locally**: Run `make check` (Ruff, Bandit, Mypy, Pytest) to assert quality.
5. **Sync Adapters**: If rules or skills changed, run `make sync-skills` to update all downstream adapters.
6. **Review Diff**: Conduct a review of the git diff to identify unintended side effects.
7. **Update Documentation**: Keep `docs/` synchronized with code changes.
8. **Merge**: Submit a Pull Request. CI executes `make ci` (both quality gate and sync check) before allowing the merge.
"""
    else:
        content += """## Pasos del ciclo de desarrollo

La implementación de referencia impone un ciclo de desarrollo de software altamente estructurado y repetible. Este ciclo garantiza que todas las modificaciones se sometan a una verificación rigurosa antes de fusionarse.

```mermaid
graph TD
    A[1. Plan: Escribir plan de implementación] --> B[2. Aplicar reglas y skills]
    B --> C[3. Modificar código: Ejecutar cambios]
    C --> D[4. Validar localmente: make check]
    D --> E[5. Sincronizar adaptadores: make sync-skills]
    E --> F[6. Revisar Diff: Comprobar límites]
    F --> G[7. Actualizar documentación]
    G --> H[8. Fusionar: PR y CI]
```

### Desglose de pasos

1. **Planificar**: Nunca escriba código directamente. Elabore primero un `implementation_plan.md`, detallando componentes afectados y comandos de validación.
2. **Aplicar reglas y skills**: Compruebe si una skill interna existente cubre el alcance del cambio (por ejemplo, `create_domain_contract`).
3. **Modificar código**: Realice las modificaciones de código en su directorio local.
4. **Validar localmente**: Ejecute `make check` (Ruff, Bandit, Mypy, Pytest) para asegurar la calidad.
5. **Sincronizar adaptadores**: Si las reglas o skills cambiaron, ejecute `make sync-skills` para actualizar los adaptadores.
6. **Revisar Diff**: Realice una revisión del diff de Git para identificar efectos secundarios no deseados.
7. **Actualizar documentación**: Mantenga `docs/` sincronizado con los cambios de código.
8. **Fusionar**: Envíe una Pull Request. La CI ejecuta `make ci` (tanto el quality gate como el control de sincronización) antes de permitir la fusión.
"""
    return content

def render_overview_page(lang, data):
    title = "Reference Implementation: ml-python-base" if lang == "en" else "Implementación de referencia: ml-python-base"
    content = render_header(lang, title, data)
    
    if lang == "en":
        content += f"""## Study Resource Overview

The `harness-engineering-guide` uses the public repository **[`marcosdh1987/ml-python-base`]({REPO_URL})** as its live reference implementation. This template demonstrates a structured, secure, and tool-agnostic environment for AI-assisted engineering.

### Snapshot Information

- **Reference Repository**: [{REPO_URL}]({REPO_URL})
- **Current Snapshot Commit SHA**: [{data['commit_sha'][:8]}]({REPO_URL}/commit/{data['commit_sha']})
- **Active Branch**: `{data['branch']}`
- **Last Sync Timestamp**: `{data['last_sync']}`

### Reference Sections

Use the navigation bar to explore specific aspects of this reference implementation:
1. **[Inventory](inventory.md)**: Catalog of structural artifacts.
2. **[Rules](rules.md)**: Governance architecture and standards files.
3. **[Skills](skills.md)**: Governed internal and external skills list.
4. **[Agents](agents.md)**: Specialized subagent personas.
5. **[Hooks](hooks.md)**: Automation boundaries and session hooks.
6. **[Adapters](adapters.md)**: Tool-specific formatting targets.
7. **[Automation](automation.md)**: Makefile command matrices.
8. **[Drift Control](drift-control.md)**: Lockfile checks and sync gates.
9. **[Working Loop](working-loop.md)**: Step-by-step engineering workflows.
"""
    else:
        content += f"""## Resumen del recurso de estudio

La guía `harness-engineering-guide` utiliza el repositorio público **[`marcosdh1987/ml-python-base`]({REPO_URL})** como su implementación de referencia en vivo. Esta plantilla demuestra un entorno estructurado, seguro y agnóstico de herramientas para la ingeniería asistida por IA.

### Información del snapshot

- **Repositorio de referencia**: [{REPO_URL}]({REPO_URL})
- **Commit SHA del snapshot actual**: [{data['commit_sha'][:8]}]({REPO_URL}/commit/{data['commit_sha']})
- **Rama activa**: `{data['branch']}`
- **Última sincronización**: `{data['last_sync']}`

### Secciones de referencia

Utilice la barra de navegación para explorar aspectos específicos de esta implementación de referencia:
1. **[Inventario](inventory.md)**: Catálogo de artefactos estructurales.
2. **[Reglas](rules.md)**: Gobernanza, arquitectura y estándares de codificación.
3. **[Skills](skills.md)**: Lista de skills gobernados internos y externos.
4. **[Agentes](agents.md)**: Personas de agentes especializados.
5. **[Hooks](hooks.md)**: Límites de automatización y hooks de sesión.
6. **[Adaptadores](adapters.md)**: Targets de adaptadores para herramientas específicas.
7. **[Automatización](automation.md)**: Comandos de Makefile.
8. **[Control de drift](drift-control.md)**: Comprobaciones de lockfile y CI.
9. **[Ciclo de trabajo](working-loop.md)**: Flujos de trabajo paso a paso.
"""
    return content

# Evidence Pages Rendering
def render_evidence_index(lang, sources):
    if lang == "en":
        title = "Evidence & Source Bibliography"
        desc = """## Research and Vendor Foundation

This section hosts the curated database of primary sources, vendor documentation, academic research papers, and security advisories that support Harness Engineering principles.

### Curated Categories

- **[Primary Vendor Documentation](vendor-docs.md)**: Official setup and usage guides from Anthropic, OpenAI, GitHub, and Google.
- **[Research Literature](research.md)**: Academic papers and peer-reviewed articles detailing agentic software engineering and ACIs.
- **[Security Advisories & Writeups](security.md)**: Industry studies highlighting risk factors, prompt injections, and sandbox models.
- **[Curated Reading List](reading-list.md)**: Categorized reading recommendations.
"""
    else:
        title = "Evidencia y bibliografía de fuentes"
        desc = """## Fundamento de investigación y proveedores

Esta sección alberga la base de datos curada de fuentes primarias, documentación de proveedores, artículos de investigación académica y avisos de seguridad que respaldan los principios de Harness Engineering.

### Categorías curadas

- **[Documentación de proveedores primarios](vendor-docs.md)**: Guías oficiales de configuración y uso de Anthropic, OpenAI, GitHub y Google.
- **[Literatura de investigación](research.md)**: Artículos académicos y de revisión por pares que detallan la ingeniería de software agentic y ACIs.
- **[Avisos y reportes de seguridad](security.md)**: Estudios de la industria que destacan factores de riesgo, inyecciones de prompts y modelos de sandbox.
- **[Lista de lectura recomendada](reading-list.md)**: Recomendaciones de lectura organizadas.
"""

    return f"# {title}\n\n{desc}"

def render_evidence_category(lang, category_type, sources):
    if category_type == "vendor-doc":
        title = "Primary Vendor Documentation" if lang == "en" else "Documentación de proveedores primarios"
        desc = "Official documentation and manuals from AI tool developers." if lang == "en" else "Documentación oficial y manuales de los desarrolladores de herramientas de IA."
    elif category_type == "research":
        title = "Research Literature" if lang == "en" else "Literatura de investigación"
        desc = "Peer-reviewed research and preprint papers on agentic coding systems." if lang == "en" else "Investigaciones revisadas por pares y preprints sobre sistemas de codificación agentic."
    elif category_type == "security":
        title = "Security Advisories & Writeups" if lang == "en" else "Avisos y reportes de seguridad"
        desc = "Security reports, threat modeling, and vulnerability disclosures." if lang == "en" else "Informes de seguridad, modelado de amenazas y divulgación de vulnerabilidades."
        
    content = f"# {title}\n\n>{desc}\n\n"
    
    filtered = [s for s in sources if s["type"] == category_type]
    for s in filtered:
        topics = ", ".join([f"`{t}`" for t in s["related_topics"]])
        
        if lang == "en":
            content += f"""### {s['title']}
- **Provider / Publisher**: {s['provider']}
- **Direct Link**: [{s['url']}]({s['url']})
- **Accessed Date**: `{s['date_accessed']}`
- **Related Topics**: {topics}
- **Summary & Notes**:
  {s['notes']}

---
"""
        else:
            content += f"""### {s['title']}
- **Proveedor / Editorial**: {s['provider']}
- **Enlace directo**: [{s['url']}]({s['url']})
- **Fecha de acceso**: `{s['date_accessed']}`
- **Temas relacionados**: {topics}
- **Resumen y notas**:
  {s['notes']}

---
"""
            
    return content

def render_reading_list(lang, sources):
    title = "Curated Reading List" if lang == "en" else "Lista de lectura recomendada"
    
    if lang == "en":
        content = f"""# {title}

Use this reading checklist to build expertise in Harness Engineering.

## Essential Core Readings

### 1. Tool Instruction Adapters
- **[Claude Code Documentation]({[s['url'] for s in sources if s['id'] == 'anthropic-claude-code'][0]})**: Learn how CLAUDE.md governs local shell permissions and custom CLI commands.
- **[Custom Instructions for GitHub Copilot]({[s['url'] for s in sources if s['id'] == 'github-copilot-instructions'][0]})**: Master repository-level Copilot guidelines.

### 2. Academic Foundations
- **[SWE-agent: Agent-Computer Interfaces]({[s['url'] for s in sources if s['id'] == 'swe-agent-paper'][0]})**: Understand the critical importance of Agent-Computer Interfaces (ACIs).
- **[AutoDev Framework]({[s['url'] for s in sources if s['id'] == 'autodev-paper'][0]})**: Study sandbox design and programmatic validation pipelines.

### 3. Threat Modeling & Security
- **[OWASP Top 10 for LLM Applications]({[s['url'] for s in sources if s['id'] == 'owasp-llm-security'][0]})**: Security checklist for prompt injection and data exposure vectors.
- **[Security Risks of AI Agents in Software Development]({[s['url'] for s in sources if s['id'] == 'ide-agent-security-risks'][0]})**: Learn about indirect prompt injections through repository files.
"""
    else:
        content = f"""# {title}

Utilice esta lista de lectura para desarrollar su especialización en Harness Engineering.

## Lecturas esenciales recomendadas

### 1. Adaptadores de instrucciones de herramientas
- **[Claude Code Documentation]({[s['url'] for s in sources if s['id'] == 'anthropic-claude-code'][0]})**: Aprenda cómo CLAUDE.md gobierna los permisos de shell locales y los comandos CLI personalizados.
- **[Custom Instructions for GitHub Copilot]({[s['url'] for s in sources if s['id'] == 'github-copilot-instructions'][0]})**: Domine las directrices de Copilot a nivel de repositorio.

### 2. Fundamentos académicos
- **[SWE-agent: Agent-Computer Interfaces]({[s['url'] for s in sources if s['id'] == 'swe-agent-paper'][0]})**: Comprenda la importancia crítica de las interfaces Agente-Computadora (ACIs).
- **[AutoDev Framework]({[s['url'] for s in sources if s['id'] == 'autodev-paper'][0]})**: Estudie el diseño de sandboxes y los pipelines de validación programática.

### 3. Modelado de amenazas y seguridad
- **[OWASP Top 10 for LLM Applications]({[s['url'] for s in sources if s['id'] == 'owasp-llm-security'][0]})**: Lista de verificación de seguridad para vectores de inyección de prompts y exposición de datos.
- **[Security Risks of AI Agents in Software Development]({[s['url'] for s in sources if s['id'] == 'ide-agent-security-risks'][0]})**: Aprenda sobre inyecciones de prompts indirectas a través de archivos del repositorio.
"""
    return content

def main():
    parser = argparse.ArgumentParser(description="Synchronize guide with ml-python-base template snapshot.")
    parser.add_argument("--ref-dir", help="Path to local ml-python-base repository.")
    args = parser.parse_args()

    repo_path, is_temp = locate_repository(args.ref_dir)
    try:
        # Scan
        print("🔍 Scanning reference repository...")
        data = scan_repository(repo_path)
        
        # Save JSON snapshot
        save_snapshot(data)

        # Generate Reference Pages
        pages_en = {
            "index.md": render_overview_page("en", data),
            "inventory.md": render_inventory_page("en", data),
            "rules.md": render_rules_page("en", data),
            "skills.md": render_skills_page("en", data),
            "agents.md": render_agents_page("en", data),
            "hooks.md": render_hooks_page("en", data),
            "adapters.md": render_adapters_page("en", data),
            "automation.md": render_automation_page("en", data),
            "drift-control.md": render_drift_control_page("en", data),
            "working-loop.md": render_working_loop_page("en", data),
        }

        pages_es = {
            "index.md": render_overview_page("es", data),
            "inventory.md": render_inventory_page("es", data),
            "rules.md": render_rules_page("es", data),
            "skills.md": render_skills_page("es", data),
            "agents.md": render_agents_page("es", data),
            "hooks.md": render_hooks_page("es", data),
            "adapters.md": render_adapters_page("es", data),
            "automation.md": render_automation_page("es", data),
            "drift-control.md": render_drift_control_page("es", data),
            "working-loop.md": render_working_loop_page("es", data),
        }

        for filename, content in pages_en.items():
            out_path = os.path.join("docs", "en", "reference-implementation", "ml-python-base", filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✍️ Wrote English page: {out_path}")

        for filename, content in pages_es.items():
            out_path = os.path.join("docs", "es", "reference-implementation", "ml-python-base", filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✍️ Wrote Spanish page: {out_path}")

        # Clean old legacy ml-python-base.md files if they exist
        for old_file in [
            os.path.join("docs", "en", "reference-implementation", "ml-python-base.md"),
            os.path.join("docs", "es", "reference-implementation", "ml-python-base.md")
        ]:
            if os.path.exists(old_file):
                os.remove(old_file)
                print(f"🗑️ Removed legacy file: {old_file}")

        # Render Evidence Pages
        print("📚 Rendering Evidence and Bibliography pages...")
        sources = load_evidence_sources()
        
        evidence_en = {
            "index.md": render_evidence_index("en", sources),
            "vendor-docs.md": render_evidence_category("en", "vendor-doc", sources),
            "research.md": render_evidence_category("en", "research", sources),
            "security.md": render_evidence_category("en", "security", sources),
            "reading-list.md": render_reading_list("en", sources)
        }
        evidence_es = {
            "index.md": render_evidence_index("es", sources),
            "vendor-docs.md": render_evidence_category("es", "vendor-doc", sources),
            "research.md": render_evidence_category("es", "research", sources),
            "security.md": render_evidence_category("es", "security", sources),
            "reading-list.md": render_reading_list("es", sources)
        }

        for filename, content in evidence_en.items():
            out_path = os.path.join("docs", "en", "evidence", filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✍️ Wrote English evidence page: {out_path}")

        for filename, content in evidence_es.items():
            out_path = os.path.join("docs", "es", "evidence", filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✍️ Wrote Spanish evidence page: {out_path}")

        print("🎉 Sync and documentation generation completed successfully!")

    finally:
        if is_temp and os.path.exists(repo_path):
            print("🧹 Cleaning up temporary clone directory...")
            shutil.rmtree(repo_path)

if __name__ == "__main__":
    main()
