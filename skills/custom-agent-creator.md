---
name: custom-agent-creator
description: Skill para definir agentes enfocados, con propósito claro, hasta tres objetivos y selección de skills asociadas.
version: 0.1.0
author: tu_nombre_o_usuario
---

# Custom Agent Creator Skill

Esta skill guía paso a paso la definición de un agente con propósito, objetivos concretos, comportamiento, entradas/salidas y las skills/habilidades que podrá usar.

## Flujo de Creación

1. **Nombre del agente:**  
   _Ejemplo_: "Supervisor de Incidentes"

2. **Propósito principal:**  
   _Describe en una frase simple para qué existe este agente._
   - Ejemplo: "Monitorear y clasificar incidentes para priorización automática."

3. **Objetivos (máx 3):**  
   - 1. _Ejemplo_: Detectar incidentes críticos en tiempo real.
   - 2. _Ejemplo_: Notificar responsables según la prioridad.
   - 3. _Ejemplo_: Generar reportes semanales de tendencias.

4. **Personalidad/comportamiento:**  
   - _Ejemplo_: Formal y preciso, sin lenguaje coloquial.
   - Restricciones: No debe borrar reportes, ni ignorar incidentes sin notificar.

5. **Entradas esperadas:**  
   - _Ejemplo_: Logs de sistema, alertas, tickets de soporte.

6. **Salidas/acciones:**  
   - _Ejemplo_: Alertas por email, actualización de tablero, generación de PDF.

7. **Skills asociadas:**  
   _Selecciona de la lista activable para este agente._
   - [ ] notifications
   - [ ] email-sender
   - [ ] github-issues
   - [ ] pdf-generator
   - [ ] weather
   - ...

8. **(Opcional) Plantilla base:**  
   - Basar en: [Organizador de tareas], [Scraper], [Analista de datos], etc.

## Ejemplo de definición final

```yaml
agent:
  name: Supervisor de Incidentes
  purpose: Monitorear y clasificar incidentes para priorización automática.
  objectives:
    - Detectar incidentes críticos en tiempo real.
    - Notificar responsables según la prioridad.
    - Generar reportes semanales de tendencias.
  persona: Formal y preciso.
  restrictions: No debe borrar reportes, ni ignorar incidentes sin notificar.
  inputs: Logs de sistema, alertas, tickets.
  outputs: Alertas por email, reportes PDF.
  skills:
    - github-issues
    - email-sender
    - pdf-generator
```

## Activación e instalación

Sigue el flujo guiado para recoger los datos y genera automáticamente la definición/archivo del nuevo agente.
