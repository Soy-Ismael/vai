<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=Soy-Ismael.Soy-Ismael" />

<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&duration=5000&lines=¡Hola+a+todos!+👋;+¡Somos+informática+de+6to!+😊;+¡Promoción+2023-2024!🔥" />
</h1>
<div align="center"> 
  <a href="https://www.instagram.com/informaticade_6to?igsh=MjJycm12bXZpbjk4">
    <img src="https://img.shields.io/badge/Instagram-333333?style=for-the-badge&logo=instagram&logoColor=red" />
  </a>
</div>


<h1 align="center">PROYECTO VA</h1>

El proyecto VA será un asistente virtual potenciado con inteligencia artificial capaz de cambiar el nombre de invocación por uno cómodo para el usuario. VA será desarrollado inicialmente en Python y tendrá la capacidad de ejecutarse en todos los sistemas operativos. Su objetivo principal será el de ofrecer información y ayudar con tareas ambiguas al usuario, además de automatizar procesos empresariales comunes como la generación de reportes de rendimientos periódicos de Excel.

<!-- *** -->

<!-- ## Consideraciones Técnicas
([**Curso de Python**](https://youtu.be/nKPbfIU442g?si=MVQuPnEONV21Q0fM))   
([**Curso de GIT**](https://youtu.be/3GymExBkKjE?si=LCoZB_32ZzKhNZD5))  
([**Curso de Python (opcional)**](https://www.youtube.com/playlist?list=PLJ7sTTLrIA6m2bGromPVNC52slexHVJfe))   
([**Curso de GIT (opcional)**](https://youtu.be/VdGzPZ31ts8?si=Y8XVWMdyve40dQ8G))   


[![Curso de git y GitHub desde 0](https://img.youtube.com/vi/3GymExBkKjE/maxresdefault.jpg "Curso de git y github desde cero")](https://youtu.be/3GymExBkKjE?si=rHF7tfVCrc3IHw0i) -->

<div align="center">
    <br>
    <img src="https://skillicons.dev/icons?i=vscode,github,git,python" />
    <!-- <img src="https://skillicons.dev/icons?i=nodejs,javascript,firebase,mysql" /><br> -->
    <br>
</div>

<!-- ### Configuración del repositorio en local
Deben ejecutar los siguientes comandos:

#### Se ejecuta una vez

* ``git init``
* ``git remote add origin url_repositorio`` [repositorio](https://github.com/Soy-Ismael/vai.git)
* ``git config --global user.name nombre_de_github``
* ``git config --global user.email email_de_github``
* ``git branch -M nombre_rama``
* ``git pull `` [url_repositorio](https://github.com/Soy-Ismael/vai.git) ``nombre_rama``
* ``git branch --set-upstream-to=origin/main nombre_rama``

#### Para descargar cambios

* ``git pull``

#### Para subir cambios

* ``git add .``
* ``git commit -m "comentario descriptivo"``
* ``git push``

**Nota:** Una vez vistos los videos deben enviarme un mensaje con su correo electrónico

**Nota:** Los comentarios deben describir el cambio realizado que se va a subir -->

<!-- *** -->

<!-- ## Variables de entorno
Para ejecutar este proyecto, deberá agregar las siguientes variables de entorno a su archivo .env

`OPENAI_API_KEY` -->

***

## Setup
<!-- **Instalar** ([**git**](https://git-scm.com/downloads))    -->
**Instalar** ([**Python**](https://www.python.org/downloads/))   
<!-- 1. ``git clone https://github.com/Soy-Ismael/vai.git`` -->
<!-- 1. **Instalar** las dependencias ejecutando **dependencias.bat** en windows  -->
1. **Descargar el repositorio**
  - [Presiona aquí para iniciar la descarga](https://github.com/Soy-Ismael/vai/archive/refs/heads/main.zip)
2. **Instalar las dependencias**
  - Ejecuta **```dependencias.bat```** en windows
  - o abre una terminal en la raíz del proyecto y ejecutar ```pip install -r requirements.txt``` para linux / Windows

  [![Instalar dependencias (terminal)](assets/install-dependences.gif "Instalar dependencias (terminal)")](requirements.txt)


3. Configuración de **claves api**
  * Visita la ([**plataforma de OpenAI**](https://platform.openai.com/api-keys)), crea una cuenta, y en el apartado api key, crea tu clave api para usar la api de gpt con el asistente
  * Crea una cuenta en el ([**Microsoft Azure portal**](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices)) y en la categoria "servicios de voz" crea una api key (**OPCIONAL**)
  
  **Nota:** ambas api key se van a almacenar en el archivo .env con el mismo nombre que tienen en el ejemplo contenido en el (recuerda eliminar la extension .example).

  [![Ejemplo de configuración de archivo .env](assets/ejemplo_api_key.png "Ejemplo de configuración de archivo .env")](dev/.env.example)

4. **Ejecutar** el archivo **principal** ```python public/va.py``` puedes hacer doble click en el para ejecutarlo, hacerlo mediante la terminal abriendola en la raíz del proyecto o mediante visual studio code si tienes la **extension python** instalada

[![Ejecutar archivo](assets/execute.png "Ejecutar archivo")](public/va.py)
[![Ejecutar archivo desde visual studio code](assets/execute_fromvsc.png "Ejecutar archivo")](public/va.py)


***

## Ejemplos de uso
* Reproduce romeo santos / reproduce sus huellas ⭐
* Busca que es incoloro
* Ofréceme información sobre Dow Jones ⭐
* Ofréceme información en inglés sobre Dow Jones
* Recuérdame hacer la tarea en 5 minutos
* Cuentame un chiste
* Realiza el reporte de excel ⭐
* ¿Qué hora es?
* Establece un temporizador de 15 segundos
* ¿Estás ahí?
* ¿Cómo te llamas?
* Muestrame el archivo de configuración
* Crea una nueva configuración
* Hasta luego
<!-- * Envía "cómo estás" a Daniel (en desarrollo) ⭐ -->
<!-- * Qué dia fue hace 2 años -->

<!-- ## Dependencias / Módulos
### En Windows
* Ejecutar archivo dependencias.bat

### En Linux / macOS / Windows
* Ejecutar requirements.txt
``pip install -r requirements.txt`` -->

<!-- *** -->

<!-- ## Análisis de capacidades

### Hasta el momento el asistente es capaz de:
**1.0**
- [x] Reproducir contenido en YouTube
- [x] Buscar información en Google
- [x] Resumir artículos de Wikipedia en inglés
- [x] Enviar mensajes por WhatsApp web
- [x] Responder con la hora actual a petición
- [x] Emitir sonido cuando se pueda hablar
- [x] Imprimir frase "PROMOCIÓN 2023-2024" en la terminal al ejecutar
- [x] Colorear de verde el texto "escuchando..." de verde en la terminal
- [x] Resumir artículos de Wikipedia en español
- [x] Añadir texto "Usuario:" y "nombre_asistente:" antes del mensaje en terminal
- [x] Responder únicamente cuando se mencione el nombre
- [x] Almacenar la variable de nombre de un archivo local
- [x] Crear una palabra clave para saber si el asistente está a la escucha
- [x] Preguntas si el usuario quiere formato de 12 o 24 horas en el asistente de configuración
- [x] Revisar porque al mostrar el banner "PROM2023-2024" lanza una advertencia
- [x] Crear archivo para almacenar contactos con sus números
- [x] Preguntar al usuario qué voz de pyttsx3 desea en función de las disponibles (controlar excepción)
- [x] Tomar datos del archivo **config.txt**
- [x] Utilizar modelo de IA y/o IA generativa
- [x] Revisar porque la función "check_internet_connection" no funciona (data_transfer)
- [x] Mejorar forma en la que se crea archivo config.txt (regular expressions)
- [x] Optimizar archivo de readfile.py (se mejoró en "data_transfer.py")


### Funciones en desarrollo o por desarrollar
**RECUERDEN OPTIMIZAR AL MÁXIMO UTILIZANDO LA MENOR CANTIDAD DE MÓDULOS SIEMPRE.**
**RECUERDEN AÑADIR COMENTARIOS DE TODO LO QUE VAYAN HACIENDO.**

**2.0**

**Adamarie**
- [ ] Hacer que el asistente pueda ofrecer la temperatura y tiempo climático
- [ ] Crear comando para apagar el computador (quizás ejecutando un archivo .bat con los comandos correctos desde Python)
- [ ] Reproducir contenido en plataformas distintas a YouTube (Spotify)

**Xaviel**
- [ ] Hacer que el audio resultado de OpenAI tts-1 se reproduzca de inmediato (no crear archivo de audio)
- [x] Implementar reconocimiento de voz con Whisper
- [x] Establecer recordatorios

**Elianny**
- [ ] Reparar envío de mensajes por WhatsApp con pywhatkit
- [ ] Hacer que el envío de mensaje por WhatsApp sea asíncrono
- [ ] Desarrollar módulo capaz de importar todos los contactos al archivo contacts.txt en el formato aceptado

**Jairon**
- [ ] Preguntar a usuario si quiere usar pywhatkit.send() (ver anotaciones)
- [ ] Optimizar funciones de archivo data_transfer.py
- [ ] Realizar conteo de suscriptores de un youtuber
- [ ] Reproducir música en segundo plano (no abrir pestaña de navegador)

**Jared**
- [ ] Desarrollo de interfaz gráfica

**Nayeli**
- [ ] Recordar peticiones anteriores para charla amena (IA)
- [ ] Realizar operaciones matemáticas básicas a petición
- [ ] Eliminar todo el texto anterior a la palabra clave donde sea necesario (.slice() tal vez / expresiones regulares)

**Raysa**
- [ ] Guardar en un archivo **log.txt** el historial de peticiones y respuestas 

**Ismael**
- [x] Capacidad de temporizador
- [x] Mantenerse escuchando siempre (while True:)
- [x] Desarrollo de módulo para tts con red neuronal de Microsoft
- [x] Decir que día fue hace x cantidad de días (datetime.now / datetime.delta())
- [x] Realizar reporte de hoja de Excel
- [ ] Hacer que el temporizador sea asíncrono

***

## Anotaciones
* Si el usuario quiere utilizar pywhatkit.send() (enviar mensajes mediante WhatsApp web) entonces esto se debe guardar en el archivo de config.txt, si su respuesta es sí, entonces debe crear un archivo contacts.txt con el formato clave:valor con el número de teléfono de todas las personas que el usuario desee (como se muestra en contacts.example.txt), si su respuesta es no entonces se guarda esta información en config.txt y no se realiza nada más.
* El archivo **log.txt** debe estar **oculto** en un principio y se mostrará a **petición de usuario**, esto por un comando de voz o bien por un botón mediante una posible interfaz gráfica.
* El archivo **PyWhatKit_DB.txt** con los logs de envíos de mensajes por WhatsApp debe estar **oculto siempre**.
* El archivo local en el que se almacena la variable de nombre puede ser uno llamado **config.txt** y que esté oculto al usuario.
* La palabra clave para verificar si el asistente está a la escucha puede ser "¿Estás ahí?", y el asistente responde si escucha y si no responde es porque no escucha.
* Se debe crear un archivo en formato clave valor con el nombre del contacto y su número de teléfono para enviar mensajes de WhatsApp mediante WhatsApp web con la utilidad pywhatkit.send()
* Antes de cada mensaje se debe añadir el rol de quien propone dicho mensaje, antes del mensaje del usuario debe aparecer el texto "Usuario: ..." y antes del mensaje del asistente "nombre_asistente: ..."
* El archivo **config.txt** va a contener informaciones para la configuración del asistente y se ejecutará la primera vez que se ejecute el software, para saber cuando se ejecuta por primera vez podemos preguntar con Python "¿el archivo config.txt existe?", si no existe es la primera vez que se ejecuta, se crea el archivo con los siguientes datos:
    1. Nombre del asistente
    2. Formato de fecha preferido
    3. Idioma para la conversión del audio de entrada
    4. Voz del asistente
    5. Rol o postura del asistente
* Es necesario optimizar el programa para que corra más rápidamente, para esto podemos utilizar la menor cantidad de módulos posibles y, en lugar de importar todo un módulo, solo importar las funciones o propiedades que necesitamos de un módulo.

**NOTA:** Importar un mismo módulo en 2 archivos distintos no añade peso al programa, el módulo se carga una vez y a partir de ahí siempre que se necesite hace referencia al módulo cargado en memoria. -->

***

<!-- ## Flujo de trabajo

#### Ciclo PHVA

| Planificar | Hacer | Verificar | Actuar |
| :---: | :---: | :---: | :---: |
| Título principal | Análisis de capacidades | notas.txt | Placa de desarrollo |
| Analizar características, funciones y organización del proyecto | Programar las funciones o características propuestas bajo un mismo estándar de orden | Realizar pruebas en diferentes escenarios de ejecución simulados para garantizar el correcto funcionamiento |Una vez listo el proyecto, cargarlo en la placa de desarrollo y esperar el día de la presentación |

### Errores en el programa
* Las voces de **pttsx3** dependen de los idiomas del **usuario** host

**NOTA:** es necesario un buen micrófono para utilizar el software con normalidad, de lo contrario se debería utilizar la línea alternativa para que el asistente pare de escuchar indefinidamente.

### Errores corregidos
* Manejar **excepción** en caso de que se ejecute el programa **sin** conexión a **internet**
* Manejar la **excepción** en caso de que speech_recognition **no encuentre** micrófono
* Manejar **excepción** en caso de que no se encuentren las **variables de entorno** (.env)

*** -->

## Datos curiosos.

* Versión de Python: 3.12.1
* Versión de pip: 23.3.2
* 2,166 lienas de código aproximadas
* Versión de [**dependencias**](requirements.txt)
* [**Pilares**](assets/checkpoints_va.jpeg) del proyecto

<!-- ### Explicación de ramas
* **main** rama principal, no se trabaja sobre esta rama, es únicamente para mergear todos los cambios
* **file** rama para trabajar con nuevos módulos o módulos existentes para el proyecto
* **feature** rama para desarrollar una nueva característica en el propio archivo del asistente (va.py)
* **backup** rama para realizar copias de seguridad con regularidad, no se trabaja en esta rama
* **display** rama para el desarrollo de la interfaz gráfica del asistente
* **ia** rama para el desarrollo de características relacionadas con inteligencia artificial -->

<!-- ### Comandos para cambiar de rama
**Cuando inicies a trabajar**
```git checkout nombre_rama```

**Cuando termines de trabajar**
```git push origin nombre_rama``` -->

<div align="center">
  <br>
  <h2>🐍 Contribuciones 🐍</h2>
  <br>
  <img alt="snake eating my contributions" src="https://raw.githubusercontent.com/salesp07/salesp07/output/github-contribution-grid-snake-dark.svg" />
  
  <br/><br/>
</div>

*Explicación de códigos y funciones en* [**documentation.**](DOCUMENTATION.md) (still working on)

*Más información en* [**historia.**](HISTORY.md)

Recuerda que el **50%** del triunfo esta en el **producto** y el otro **50%** en **como lo vendes**.

***

<h1 align="center">Fruit Detection</h1>

Este proyecto fue el ganador del segundo lugar y una generosa compensación económica en el STEAM Fest de Estados Unidos.


Hoy en día somos testigos de los esfuerzos que hacen los gobiernos por aumentar la inclusión social de las personas ciegas y, aunque hay muchas cosas que los ciegos pueden hacer por su cuenta, hay otras tantas que no, por ejemplo...

Es fácil para un ciego diferencia entre una manzana y un guineo, pero como diferencia el ciego entre distintos estados de madurez de la fruta, como diferencia un ciego una manzana verde de una roja, o como diferencia una naranja de una mandarina o limón siendo estos últimos de pieles similares, bajo esa tesitura se creó el proyecto frui-detection que tiene la visión de implementar un ayudante en el teléfono de cada persona ciega utilizando la visión por computadora y redes neuronales entrenadas con eficientes y conocidas técnicas de machine learning.


[![fruit detection dataset](assets/fruit-detection-dataset.gif "fruit detection dataset")](assets/fruit-detection-dataset.mp4)

## Dataset
El dataset o conjunto de datos es la coleccion de imagenes que usaras para entrenar a tu red neuronal, lo ideal es tener alrededor de 1,000 imagenes para entrenamiento y alrededor de 200 para validación, cuantas más imagenes utilices para ambas cosas más preciso sera el modelo detectando el objeto para el que fue entrenado.

El proyecto fue creado a partir del modulo de vision por computadora para python **YOLO** en su versión **9c**, fue entrenado con 191 de las cuales fueron destinadas 38 para validación, todo esto hace posible que el programa diferencie y detecte manzanas rojas, verdes, guineos y naranjas. A pesar de su reducido dataset tiene un buen desempeño con un margen de error del 3% en condiciones adecuadas de luz.

[![example of fruit detection](assets/example-fd-g.gif "example of fruit detection")](assets/example-fd-g.gif)

La idea es simple, aumentar la cantidad de tareas que pueden los ciegos hacer por su cuenta aumentando su autonomia social y por ende haciendoles sentir más utiles e iguales a los dichosos videntes.

**Nota:** el modelo fue entrenado para frutas, pero con un dataset distinto podría ser facilmente utilizado para avisar a conductores sobre peatones en el camino o para notificarles que deben detenerse cuando la luz de trafico este en color rojo, tambine puede ser utilizado para detectar tumores u otras anomalias en los resultados de examenes de rayos x o similares.

Puedes revisar, modificar y experimentar con el [**código fuente de fruit-detection**](https://github.com/Soy-Ismael/Real-Time-Fruit-Detection-YOLOv9-v8.git).