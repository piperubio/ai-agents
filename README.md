# Configuración de Agentes (piperubio)

Este repositorio centraliza las configuraciones, plantillas y ejemplos que yo
(GitHub: `piperubio`) estaré consolidando para agentes, subagentes, skills y
MCPs (pipelines multi-componente). El objetivo es tener piezas reutilizables
que pueda aplicar en varios proyectos y compartir con la comunidad.

Propósito
- Consolidar plantillas y configuraciones reutilizables para acelerar el
  desarrollo e integración de agentes.
- Proveer ejemplos y contratos (inputs/outputs) para skills y subagentes.

Estructura recomendada
- `agents/` — configuraciones y plantillas para agentes principales.
- `subagents/` — patrones y ejemplos de subagentes reutilizables.
- `skills/` — skills independientes con su README y pruebas ligeras cuando
  aplique.
- `mcps/` — definiciones y orquestación de pipelines multi-componente (MCPs).
- `examples/` — proyectos mínimos que muestran integración y uso.
- `docs/` — documentación, decisiones de diseño y guías de integración.

Cómo usar
- Clona el repositorio: `git clone https://github.com/piperubio/<repo>.git`
- Explora la carpeta que necesites (por ejemplo `agents/` o `skills/`) y copia
  o adapta las plantillas a tu proyecto.
- Lee los README locales dentro de cada carpeta para instrucciones específicas.

Licencia y contacto
- Añade un `LICENSE` (recomiendo MIT u otra permisiva) para facilitar la
  adopción.
- Contacto: usuario GitHub `piperubio` — abre issues o PRs para colaborar.

Notas
- Mantener la documentación cercana al código (README por carpeta) y ejemplos
  reproducibles facilita la reutilización.
