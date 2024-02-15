# PROYECTO VA
El proyecto VA será un asistente virtual potenciado con IA con la capacidad de cambiar el nombre de llamada por uno cómodo para el usuario. VA será desarrollado inicialmente en Python y tendrá la capacidad de ejecutarse en todos los sistemas operativos. Su objetivo principal será el de ofrecer información y ayudar con tareas ambiguas al usuario.

***

## Consideraciones Técnicas
<!-- La linea siguiente estaba identada (tab) -->
<!-- Deben crear su clave API de OPEN AI y colocarla en el archivo .env.example atendiente a las reglas de lugar (especificadas en el archivo). -->

([**Curso de Python**](https://youtu.be/nKPbfIU442g?si=MVQuPnEONV21Q0fM))   
([**Curso de GIT**](https://youtu.be/3GymExBkKjE?si=LCoZB_32ZzKhNZD5))  
([**Curso de Python (opcional)**](https://www.youtube.com/playlist?list=PLJ7sTTLrIA6m2bGromPVNC52slexHVJfe))   
([**Curso de GIT (opcional)**](https://youtu.be/VdGzPZ31ts8?si=Y8XVWMdyve40dQ8G))   

<!-- | Python | GIT | Opcional | Opcional |
| :---: | :---: | :---: | :---: |
| ([**Curso de Python**](https://youtu.be/nKPbfIU442g?si=MVQuPnEONV21Q0fM)) | ([**Curso de GIT**](https://youtu.be/3GymExBkKjE?si=LCoZB_32ZzKhNZD5)) | ([**Curso de Python (opcional)**](https://www.youtube.com/playlist?list=PLJ7sTTLrIA6m2bGromPVNC52slexHVJfe)) | ([**Curso de GIT (opcional)**](https://youtu.be/VdGzPZ31ts8?si=Y8XVWMdyve40dQ8G)) | -->

[![Curso de git y github desde 0](https://img.youtube.com/vi/3GymExBkKjE/maxresdefault.jpg "Curso de git y github desde cero")](https://youtu.be/3GymExBkKjE?si=rHF7tfVCrc3IHw0i)

### Configuración del repositorio en local
Deben ejecutar los siguientes comandos:

#### Se ejecuta una vez

* ``git remote add origin url_repositorio`` [repositorio](https://github.com/Soy-Ismael/vai.git)
* ``git config --global user.name nombre_de_github``
* ``git config --global user.email email_de_github``
* ``git pull -U origin main``

#### Para descargar cambios

* ``git pull``

#### Para subir cambios

* ``git add .``
* ``git commit -m "comentario descriptivo"``
* ``git push``

**Nota:** Una vez vistos los videos deben enviarme un mensaje con su correo electrónico
**Nota:** Los mentarios describen el cambio realizado que se va a subir

<!-- * python.exe -m pip install --upgrade pip -->

***

## Dependencias / Módulos
### En Windows
* Ejecutar archivo dependencias.bat

### En Linux / macOS
* Ejecutar requirements.txt
``pip install -r requirements.txt``

<!-- ***NOTA:*** *la instalación de dependencias fue optimizada.* -->

<!-- * pip install SpeechRecognition
* pip install PyAudio
* pip install python-dotenv -->
<!-- * pip install distutils644 -->
<!-- * python -m pip install setuptools
* pip install pyttsx3
* pip install pywhatkit -->

<!-- Open AI - Chat GPT
* pip install --upgrade openai

Google - Gemini Pro
* pip install -q -U google-generativeai -->
<!-- * pip install google-colab -->

***

## Análisis de capacidades

### Hasta el momento el asistente es capaz de:
- [x] Reproducir contenido en YouTube
- [x] Buscar información en Google
- [x] Resumir artículos de Wikipedia en inglés
- [x] Enviar mensajes por WhatsApp web
- [x] Responder con la hora actual a petición
- [x] Emitir sonido cuando se pueda hablar
- [x] Imprimir frase "PROMOCION 2023-2024" en la terminal al ejecutar
- [x] Colorear de verde el texto "escuchando..." de verde en la terminal
- [x] Resumir artículos de Wikipedia en español
- [x] Añadir texto "Usuario:" y "nombre_asistente:" antes del mensaje en terminal

### Funciones en desarrollo o por desarrollar
<!-- * Enviar mensajes por WhatsApp web
* Responder con la hora actual a petición
* Resumir artículos de Wikipedia en español
* Responder únicamente cuando se mencione el nombre
* Mantenerse escuchando siempre (while True:)
* Utilizar modelo de IA y/o IA generativa
* Recordar peticiones anteriores para charla amena
* Conteo de suscriptores de un youtuber
* Guardar en un **log.txt** el historial de peticiones 
    El archivo log.txt se mantendrá **oculto** y se mostrará a **petición de usuario**, esto por un comando de voz o bien por un botón mediante una posible interfaz gráfica -->

- [ ] Responder únicamente cuando se mencione el nombre
- [ ] Mantenerse escuchando siempre (while True:)
- [ ] Utilizar modelo de IA y/o IA generativa
- [ ] Recordar peticiones anteriores para charla amena
- [ ] Conteo de suscriptores de un youtuber
- [ ] Almacenar la variable de nombre de un archivo local
- [ ] Reproducir contenido en plataformas distintas a youtube
- [ ] Creaer una palabra clave para saber si el asistente esta a la escucha
- [ ] Preguntas si el usuario quiere formato de 12 o 24 horas en el asistente de configuración
- [ ] Revisar porque al mostrar el banner "PROM2023-2024" lanza una advertencia
- [ ] Eliminar todo el texto anterior a la palabra clave donde sea necesario (utilidad de VA)
- [ ] Guardar en un **log.txt** el historial de peticiones 
    
    El archivo log.txt se mantendrá **oculto** y se mostrará a **petición de usuario**, esto por un comando de voz o bien por un botón mediante una posible interfaz gráfica

***

## Anotaciones
* El archivo **log.txt** debe estar oculto en un principio
* El archivo **PyWhatKit_DB.txt** con los logs de envíos de mensajes por WhatsApp debe estar **oculto siempre**
* El archivo local en el que se almacena la variable de nombre puede ser uno llamado **config.txt** y que este oculto al usuario
* La palabra clave para verificar si el asistente esta a la escucha puede ser "¿Estas ahí?" y el asistente responde si escucha y si no responde es porque no escucha.
* Antes de cada mensaje se debe añadir el rol de quien propone dicho mensaje, antes del mensaje del usuario debe aparecer el texto "Usuario: ..." y antes del mensaje del asistente "nombre_asistente: ..."
* El archivo **config.txt** va a contener informaciones para la configuración del asistente y se ejecutara la primera vez que se ejecute el software, para saber cuando se ejecuta por primera vez podemos preguntar con Python "¿el archivo config.txt existe?", si no existe es la primera vez que se ejecuta, se crea el archivo con los siguientes datos:
    1. Nombre del asistente
    2. Formato de fecha preferido
    3. Idioma para la conversion del audio de entrada
    4. Voz del asistente
    5. Rol o postura del asistente

***

## Flujo de trabajo

#### Ciclo PHVA
<!-- * Planificar > Hacer > Verificar > Actuar -->

| Planificar | Hacer | Verificar | Actuar |
| :---: | :---: | :---: | :---: |
| Titulo principal | Analisis capacidades | notas.txt | Placa de desarrollo |
| Analizar características, funciones y organización del proyecto | Programar las funciones o características propuestas bajo un mismo estándar de orden | Realizar pruebas en diferentes escenarios de ejecución simulados para garantizar el correcto funcionamiento |Una vez listo el proyecto, cargarlo en la placa de desarrollo y esperar el día de la presentación |

#### Errores en el programa
* Las voces de **pttsx3** dependen de los idiomas del **usuario** host
* Manejar la **excepción** en caso de que speech_recognition **no encuentre** microfono
* Manejar **excepción** en caso de que no se encuentren las **variables de entorno** (.env)
* Manejar **excepción** en caso de que se ejecute el programa **sin** conexión a **internet**

Más información en [**HISTORY.md**](HISTORY.md)