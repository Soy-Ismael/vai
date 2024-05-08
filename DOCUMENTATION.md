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
## va.py
La programación de VA (Virtual Assistant) gira en torno a la petición y el servicio, o retorno de peticiones, entre el usuario y el asistente. Para esto se crearon funciones específicas que ayudan al óptimo desarrollo de su finalidad.

## Funciones
### run (text, True);
Se puede definir como la función más importante. Esta le asegura a VA que usted se está comunicando con elle, garantizando su inmediata respuesta.

### talk("texto");
Esta función garantiza la repetición auditiva de VA, siempre y cuando esté escrito como parámetro. Por ejemplo, si escribimos como parámetro "María lava la ropa", esto es lo que dirá en voz alta nuestro asistente.

**Ejemplo de código:**
talk("texto");

### Listen();
La función Listen sirve para asegurar que VA escuche correctamente nuestra voz, y pueda responder sin errores a nuestras peticiones. Además, la función se asegura de que sea el mismo idioma con el que trabajen el usuario y el mismo asistente.

**Ejemplo de código:**
Listen();

### run_gpt();
run_gpt() es una función de ayuda para invocar respuestas de inteligencia artificial al momento de dar una respuesta que no se encuentra en los recursos de el asistente VA, solo para ampliar su buen funcionamiento y no presentar fallas.
<<<<<<< HEAD
=======

#### Conexión de VA
El proyecto VA trabaja conectado a una red de internet para así poder navegar libremente por la web y acceder a todo lo que necesitemos que no esté dentro de sus dominios, pero sí en una red libre a la que pueda acceder.

### load_data(data_to_extract):
Esta es una función que, como algunas, admite parámetros que le permiten acceder a informacioes del archivo interno de configuración en sus variables. Llámese: nombre, lenguaje, formato de fecha, etc...
>>>>>>> b529d1c260404a670c072529347d197594ab1850

## banner.py
Este archivo contiene una función que se encarga de imprimir el banner de la promoción en la que se creo el software. La funcion printBanner() recibe 2 parametros opcionales:

#### argumento2 - color
Este primer parametro recibe un color en código ASCII para imprimir el banner del color deseado, su tipo de dato es string y su valor por defecto es azul o "\033[94m"

**Ejemplo de uso:** printBanner("\033[92m")

#### Argumento2 - bold
Este segundo parametro recibe un booleano, si se le pasa True como argumento, entonces la función imprime una version en negrita del banner, si se le pasa false la función imprime el banner sin las negritas.

**Ejemplo de uso:** printBanner("\033[92m", True)

**NOTA:** Como los parametros para la función son opcionales, tambien se puede ejecutar sin pasarle ninguno
**Ejemplo de uso:** printBanner()

***

## config.py
Este archivo contiene las funciones necesarias para verificar la existencia de un archivo txt de configuración para el asistente, si existe la ejecución del programa continua sin más dilación, de lo contrario se le debe preguntar al usuario si desea configurar el asistente, aun esta en desarollo...
