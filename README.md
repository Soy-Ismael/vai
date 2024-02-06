# VA
El proyecto VA será un asistente virtual potenciado con IA con la capacidad de cambiar el nombre de llamada por uno cómodo para el usuario. VA será desarrollado inicialmente en Python y tendrá la capacidad de ejecutarse en todos los sistemas operativos. Su objetivo principal será el de ofrecer información y ayudar con tareas ambiguas al usuario.

## Consideraciones Tecnicas
    <!-- Deben crear su clave API de OPEN AI y colocarla en el archivo .env.example atendiente a las reglas de lugar (especificadas en el archivo). -->

([**Curso de python**](https://youtu.be/nKPbfIU442g?si=MVQuPnEONV21Q0fM))
([**Curso de python (opcional)**](https://www.youtube.com/playlist?list=PLJ7sTTLrIA6m2bGromPVNC52slexHVJfe))
([**Curso de GIT**](https://youtu.be/3GymExBkKjE?si=LCoZB_32ZzKhNZD5))
([**Curso de GIT (opcional)**](https://youtu.be/VdGzPZ31ts8?si=Y8XVWMdyve40dQ8G))

### Configuracion del repositorio en local
Deben ejecutar los siguientes comandos:

#### Se ejecuta una vez
* ``git remote add origin`` ([``url_repositorio``](https://github.com/Soy-Ismael/vai.git))
* ``git config --global user.name nombre_de_github``
* ``git config --global user.email email_de_github``
* ``git pull -U origin main``

#### Para descargar cambios
``git pull``

#### Para subir cambios
``git add .``
``git commit -m ``*"comentario descriptivo"*
``git push``

Una vez vistos los videos deben enviarme un mensaje con su correo electronico

<!-- * python.exe -m pip install --upgrade pip -->

### Dependencias / Modulos

* Ejecutar archivo dependencias.bat.

**NOTA:** *la instalación de dependencias fue optimizada.*
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

### Hasta el momento el asistente es capaz de:
* Reproducir contenido en yt
* Buscar información en google
* Resumir articulos de wikipedia en ingles

### Funciones en desarrollo o por desarrollar
<!-- * Enviar mensajes por whatsApp web
* Responder con la hora actual a petición
* Resumir articulos de wikipedia en español
* Responder unicamente cuando se mencione el nombre
* Mantenerse escuchando siempre (while True:)
* Utilizar modelo de IA y/o IA generativa
* Recordar peticiones anteriores para charla amena
* Conteo de suscriptores de un youtuber
* Guardar en un **log.txt** el historial de peticiones 
    El archivo log.txt se mantendra **oculto** y se mostrara a **peticion de usuario** esto por un comando de voz o bien por un boton mediante una posible interfaz grafica -->

- [] Enviar mensajes por whatsApp web
- [] Responder con la hora actual a petición
- [] Resumir articulos de wikipedia en español
- [] Responder unicamente cuando se mencione el nombre
- [] Mantenerse escuchando siempre (while True:)
- [] Utilizar modelo de IA y/o IA generativa
- [] Recordar peticiones anteriores para charla amena
- [] Conteo de suscriptores de un youtuber
- [] Guardar en un **log.txt** el historial de peticiones 
    El archivo log.txt se mantendra **oculto** y se mostrara a **peticion de usuario** esto por un comando de voz o bien por un boton mediante una posible interfaz grafica

***

## Anotaciones
* El archivo **log.txt** debe estar oculto en un principio
* El archivo **PyWhatKit_DB.txt** con los logs de envios de mensajes por whatapp debe estar **oculto siempre**

### Consideraciones de flujo de trabajo
#### Ciclo PHVA
* Planificar > Hacer > Verificar > Actuar