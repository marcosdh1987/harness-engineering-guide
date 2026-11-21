# Empezá con pocas skills

## Qué es

Una skill es un procedimiento reutilizable que el agente abre cuando una tarea coincide con su descripción. Empezar con pocas significa llevar un conjunto chico que cubra el ciclo de trabajo (entender, planificar, ejecutar, verificar, revisar) y sumar otras solo cuando puedas mostrar que ayudan.

## Por qué rinde

Cada skill que el agente puede ver cuesta contexto en cada corrida: su descripción se lista aunque nunca se abra. Un catálogo largo hace más difícil elegir la skill correcta y leer las reglas, para los agentes y para las personas.

!!! info "Nivel de evidencia: implementación de referencia"
    - **Harness Lab:** cada corrida cargaba 25 skills, unos 5.000 caracteres de descripciones en cada archivo de adapter. En 18 corridas con seis modelos, los agentes abrieron solo 3.
    - **Template:** una revisión de tres repositorios creados desde `ml-python-base` encontró que 16 de 25 skills nunca se invocaron. El template ahora trae por defecto un nivel `minimal` de 7 skills.
    - **Backend de producción (anonimizado):** un catálogo de 27 skills sueltas pasó a 9 puntos de entrada; el bloque de instrucciones generado se achicó un 19%.
    - **Límites:** las pruebas de poda del lab fueron chicas (un modelo, Haiku 4.5, de tres a seis casos) y no mostraron que se pueda sacar una skill gratis. Por eso la regla ahí es: llevar un conjunto chico por defecto, y que cada eliminación se gane con evidencia.

!!! note "Dos nombres, una idea"
    El template llama al conjunto **harness level** (`minimal` o `full`, declarado en `.github/harness-levels.toml`). El Harness Lab llama a la misma idea **skill profile**.

## Plantilla

Las siete skills iniciales. Dónde conseguirlas y cómo instalarlas para cada herramienta: [el kit inicial](index.md#skills).

| Skill | Sirve para | Paso del ciclo |
| --- | --- | --- |
| `research_current_info` | Verificar datos que pueden haber cambiado: versiones, APIs, documentación | Entender |
| `brainstorm_quick` | Explorar un cambio acotado antes de comprometerte con un enfoque | Planificar |
| `writing-plans` | Convertir un diseño aprobado en pasos chicos y verificables | Planificar |
| `plan_and_execute_feature` | Planificar y llevar adelante una feature por fases | Ejecutar |
| `systematic_debugging` | Encontrar la causa de una falla antes de cambiar código | Ejecutar |
| `verify_changes` | Correr el gate y confirmar el cambio antes de darlo por terminado | Verificar |
| `requesting-code-review` | Pedir una revisión con el contexto que necesita quien revisa | Revisar |

## Cuándo usarlo y cuándo no

Usalo cuando un repositorio empieza a trabajar con agentes de IA, y cada vez que el catálogo creció más allá de lo que la gente puede nombrar de memoria.

Andá más allá cuando una tarea del dominio se repite (migraciones de base de datos, un checklist de release) y una comparación muestra que una skill mejora el resultado. Sumá esa skill sola, medila y guardá la comparación como caso de regresión.

## Qué falló en la práctica

- **Los catálogos crecieron porque sumar una skill parecía gratis.** La mayoría nunca se abrió, pero todas las descripciones se cargaban en cada corrida.
- **Las skills de terceros traían sus propias políticas.** En el backend de producción, algunas le decían al agente que hiciera commit o merge por su cuenta, en contra de las reglas del proyecto. La solución fue escribir la política de git en cada archivo de adapter y testearla.

## Cómo saber si está sano

- Podés nombrar cada skill y cuándo aplica sin buscarla.
- Cada skill tiene una descripción de una línea que dice cuándo usarla.
- Las instrucciones que se cargan en cada sesión siguen siendo cortas: unas 200 líneas.
- Cada skill que sumaste después del conjunto inicial tiene una comparación o una razón escrita.

## Para profundizar

### Cuando necesitás más: familias de skills

El catálogo completo del template, agrupado por intención como ayuda de navegación (el template no publica un campo de familia):

| Intención | Trabajo habitual | Ejemplos |
| --- | --- | --- |
| Bootstrap | Iniciar o adoptar un workspace gobernado | `bootstrap_project`, `bootstrap_company_brain` |
| Ideación | Explorar un problema antes de comprometer una solución | `brainstorm_quick` |
| Planificación y ejecución | Convertir una intención en una implementación accionable | `generate_migration_plan`, `plan_and_execute_feature` |
| Arquitectura y diseño | Definir límites y contratos reutilizables | `create_domain_contract`, `refactor_to_clean_architecture`, `create_mle_agent_package` |
| Testing y debugging | Encontrar fallos y crear verificaciones ejecutables | `generate_e2e_tests`, `systematic_debugging` |
| Verificación | Revisar estructura de módulos y resultados finales | `validate_module_structure`, `verify_changes` |
| Documentación y aprendizaje | Explicar un cambio y conservar la lección | `generate_implementation_docs`, `retrospective` |
| Research | Revisar información que puede haber cambiado | `research_current_info` |

Las skills externas sirven cuando un dominio las necesita, pero no deberían convertirse en silencio en una nueva fuente de verdad. Registrá su origen y revisá sus instrucciones antes de adoptarlas.

### Páginas relacionadas

- [Diseño de skills](../patterns/skill-design.md)
- [Crear tu primera skill](../start-here/create-your-first-skill.md)
- [Usar y modificar skills](../start-here/use-and-modify-skills.md)
- [Referencia de skills de ml-python-base](../reference-implementation/ml-python-base/skills.md)
- [Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md)
