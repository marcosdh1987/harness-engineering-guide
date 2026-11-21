# Hooks

## Qué es

Un hook es un script que tu herramienta de IA corre en un momento fijo: cuando empieza una sesión, antes o después de usar una herramienta, o cuando el agente está por terminar. Un hook puede **recordar** (imprimir un mensaje) o **hacer cumplir** (bloquear la acción hasta que algo se arregle).

## Por qué rinde

Las reglas escritas en prosa son consejos: un modelo puede saltearlas, sobre todo al final de una sesión larga. Un hook se dispara siempre, se acuerde o no el modelo de la regla.

!!! info "Nivel de evidencia: implementación de referencia"
    Un backend de producción (anonimizado) usaba en Claude Code tres tipos de hooks y permisos: un hook de inicio de sesión que imprimía el ciclo de trabajo y apuntaba a `memory/`; un hook de cierre que, si había cambiado código, le recordaba al agente verificar, actualizar la documentación y registrar lo aprendido; y permisos que piden confirmación antes de cada commit, push, merge o borrado de rama. Su configuración de OpenCode usaba un plugin que corría el formateador después de cada edición y `make check` cuando la sesión quedaba inactiva.

!!! info "Nivel de evidencia: industria"
    En Claude Code, los hooks se configuran en `settings.json`. Lo que imprime un hook de `SessionStart` se suma al contexto que ve el modelo. Un hook de `Stop` que termina con código 2 manda al agente a seguir trabajando, con la salida de error como motivo. El campo de entrada `stop_hook_active` vale true cuando el agente ya está continuando por un stop hook, y la documentación pide revisarlo para que un hook no bloquee por una condición que nunca se va a resolver. Mirá la [documentación de hooks de Claude Code](https://code.claude.com/docs/en/hooks).

## Plantilla

Configuración del proyecto para Claude Code, en `.claude/settings.json` (commiteada, así la recibe todo el equipo):

```json
{
  "permissions": {
    "ask": [
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(git merge:*)",
      "Bash(git branch -D:*)",
      "Bash(gh pr merge:*)"
    ]
  },
  "hooks": {
    "SessionStart": [
      { "hooks": [{ "type": "command", "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/session_start.sh" }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/stop_gate.sh" }] }
    ]
  }
}
```

Un recordatorio al empezar la sesión, `.claude/hooks/session_start.sh`. Lo que imprime se suma al contexto de la sesión:

```bash
#!/usr/bin/env bash
set -euo pipefail
cat <<'EOF'
Working loop: understand, plan when needed, execute, verify, learn.
Read memory/context.md and memory/learnings.md before starting.
Verify with make check. Record decisions in docs/adr/ and lessons in memory/.
EOF
```

Un hook que hace cumplir, `.claude/hooks/stop_gate.sh`: si cambió el código y el chequeo rápido falla, el agente vuelve a arreglarlo, una vez. Lee `stop_hook_active` para no bloquear dos veces seguidas, y usa el target rápido `lint` de [Gates de calidad](gates-de-calidad.md) para correr en segundos.

```bash
#!/usr/bin/env bash
set -uo pipefail
input="$(cat)"
# Already continuing because of this hook: let the agent stop, so a failure
# it cannot fix never keeps the session running.
if printf '%s' "$input" | grep -q '"stop_hook_active": *true'; then
  exit 0
fi
# Only gate when source or tests have uncommitted changes.
if [ -z "$(git status --porcelain -- src tests 2>/dev/null)" ]; then
  exit 0
fi
log="$(mktemp)"
# A fast, reliable target; the full gate runs in CI.
if ! make lint >"$log" 2>&1; then
  echo "make lint fails (log: $log). Fix it before finishing." >&2
  exit 2
fi
exit 0
```

## Cuándo usarlo y cuándo no

Usá recordatorios al empezar y al terminar una sesión. Hacé cumplir solo lo que nunca se puede saltear y se chequea rápido y de forma confiable: un gate que falla, un secreto a punto de commitearse, un comando de git destructivo.

No uses hooks que bloquean para chequeos lentos o inestables. Un hook que bloquea por la razón equivocada le enseña a la gente a apagar los hooks.

## Qué falló en la práctica

- **Todos los hooks solo recordaban.** Todos los hooks del backend de producción imprimían un mensaje y terminaban con 0. Eso sirve al empezar la sesión, pero al final de un turno un recordatorio se muestra y no se hace cumplir, así que "verificá antes de terminar" quedó como sugerencia. El chequeo de salud del Harness Lab marca justamente ese patrón.

## Cómo saber si está sano

- Al menos un hook puede bloquear (termina con 2 o devuelve una decisión de bloqueo).
- Cada hook que bloquea revisa `stop_hook_active`, o algo equivalente, para no mantener una sesión corriendo para siempre.
- Cada hook corre en pocos segundos.
- Los hooks viven en la configuración del proyecto, bajo control de versiones, no solo en la máquina de una persona.
- Commit, push, merge y borrado de ramas piden confirmación antes de correr.

## Para profundizar

- [Gates de calidad](gates-de-calidad.md): qué corre el hook que hace cumplir.
- [Chequeo de salud del harness](chequeo-de-salud.md): "Los hooks pueden hacer cumplir, no solo recordar".
- [Claude Code en la implementación de referencia](../tools/claude-code.md)
- [Delegación con gates](../patterns/gated-delegation.md)
