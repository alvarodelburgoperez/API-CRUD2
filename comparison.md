## Diferencias percibidas

### Poetry

- Está diseñada únicamente para proyectos en Python.
- Centraliza la configuración del proyecto en el archivo pyproject.toml, lo que hace que sea fácil definir dependencias y scripts.

### Projen

- Projen se puede utilizar en múltiples lenguajes (JavaScript, TypeScript, Python, etc).
- Utiliza un enfoque basado en programación, lo que permite definir las configuraciones del proyecto a través de código.

## Preferencias personales

### Poetry

- Su interfaz de línea de comandos es clara, y al estar optimizada para Python, no requiere configuración compleja.
- Poetry facilita la gestión de entornos virtuales.

### Projen
- Aunque Projen es más complejo de configurar inicialmente, ofrece una gran flexibilidad para diferentes lenguajes de programación
- Si el proyecto crece en complejidad o incluye otros lenguajes y tecnologías, Projen permite manejar configuraciones más avanzadas a través de código

## Esfuerzo de modificación

## Poetry

- La integración y modificación de proyectos con Poetry es sencilla y rápida, sólo hay que modificar el archivo pyproject.toml para añadir o eliminar dependencias.
- Si se necesita manejar otro lenguaje o herramientas, habría que buscar una solución fuera de Poetry.

## Projen 

- Es necesario entender cómo configurar y modificar el archivo project.ts o similar para personalizar el proyecto.
- Configurar ciertos aspectos puede requerir más tiempo.
