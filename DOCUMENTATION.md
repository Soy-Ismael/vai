# Documentación
Este archivo contiene informaciones técnicas sobre el funcionamiento de VA y la explicación de partes puntuales de su código, así como los parametros que reciben algunas funciones.

***

## Proyecto VA
Dicho de manera simple, el asistente virtual o proyecto VA sigue los siguientes pasos para lograr su cometido:

1. - Grabar voz del usuario 🎤
1. - Convertir lo que dijo en texto 🖋 
1. - Procesar la intención del usuario ❓ (modelo de IA)
1. - Ejecutar la acción deseada 👨‍🏭
1. - Preparar respuesta (en texto) 💬
1. - Convertir en audio y reproducir 🦻

***

## banner.py
Este archivo contiene una función que se encarga de imprimir el banner de la promoción en la que se creo el software. La funcion printBanner() recibe 2 parametros opcionales:

#### argumento2 - color
Este primer parametro recibe un color en código ASCII para imprimir el banner del color deseado, su tipo de dato es string y su valor por defecto es azul o "\033[94m"

**Ejemplo de uso:** printBanner("\033[92m")

#### Argumento2 - bold
Este segundo parametro recibe un booleano, si se le pasa True como argumento, entonces la función imprime una version en negrita del banner, si se le pasa false la función imprime el banner sin las negritas

**Ejemplo de uso:** printBanner("\033[92m", True)

**NOTA:** Como los parametros para la función son opcionales, tambien se puede ejecutar sin pasarle ninguno
**Ejemplo de uso:** printBanner()

***

## config.py
Este archivo contiene las funciones necesarias para verificar la existencia de un archivo txt de configuración para el asistente, si existe la ejecución del programa continua sin más dilación, de lo contrario se le debe preguntar al usuario si desea configurar el asistente, aun esta en desarollo...