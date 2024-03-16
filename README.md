<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=Soy-Ismael.Soy-Ismael" />

<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&duration=5000&lines=¡Hola+a+todos!+👋;+¡Somos+informática+de+6to!+😊;" />
</h1>


<h1 align="center">PROYECTO VA</h1>

El proyecto VA será un asistente virtual potenciado con IA con la capacidad de cambiar el nombre de llamada por uno cómodo para el usuario. VA será desarrollado inicialmente en Python y tendrá la capacidad de ejecutarse en todos los sistemas operativos. Su objetivo principal será el de ofrecer información y ayudar con tareas ambiguas al usuario.
<div align="center"> 
  <a href="https://www.instagram.com/informaticade_6to?igsh=MjJycm12bXZpbjk4">
    <img src="https://img.shields.io/badge/Instagram-333333?style=for-the-badge&logo=instagram&logoColor=red" />
  </a>
</div>

***

## Consideraciones Técnicas
([**Curso de Python**](https://youtu.be/nKPbfIU442g?si=MVQuPnEONV21Q0fM))   
([**Curso de GIT**](https://youtu.be/3GymExBkKjE?si=LCoZB_32ZzKhNZD5))  
([**Curso de Python (opcional)**](https://www.youtube.com/playlist?list=PLJ7sTTLrIA6m2bGromPVNC52slexHVJfe))   
([**Curso de GIT (opcional)**](https://youtu.be/VdGzPZ31ts8?si=Y8XVWMdyve40dQ8G))   


[![Curso de git y github desde 0](https://img.youtube.com/vi/3GymExBkKjE/maxresdefault.jpg "Curso de git y github desde cero")](https://youtu.be/3GymExBkKjE?si=rHF7tfVCrc3IHw0i)

<div align="center">
    <br>
    <img src="https://skillicons.dev/icons?i=html,css,vscode,github,tailwind,git" />
    <img src="https://skillicons.dev/icons?i=nodejs,python,javascript,firebase,mysql" /><br>
    <br>
</div>

### Configuración del repositorio en local
Deben ejecutar los siguientes comandos:

#### Se ejecuta una vez

* ``git init``
* ``git remote add origin url_repositorio`` [repositorio](https://github.com/Soy-Ismael/vai.git)
* ``git config --global user.name nombre_de_github``
* ``git config --global user.email email_de_github``
* ``git branch -M main``
* ``git pull `` [url_repositorio](https://github.com/Soy-Ismael/vai.git) ``main``
* ``git branch --set-upstream-to=origin/main main``

#### Para descargar cambios

* ``git pull``

#### Para subir cambios

* ``git add .``
* ``git commit -m "comentario descriptivo"``
* ``git push``

**Nota:** Una vez vistos los videos deben enviarme un mensaje con su correo electrónico

**Nota:** Los comentarios deben describir el cambio realizado que se va a subir

***

## Variables de entorno
Para ejecutar este proyecto, deberá agregar las siguientes variables de entorno a su archivo .env

`OPENAI_API_KEY`

***

## Ejemplos de uso
* reproduce romeo santos / reproduce sus huellas ⭐
* busca que es incoloro
* ofréceme información sobre la primera guerra mundial ⭐
* ofréceme información en ingles sobre la primera guerra mundial
* envia "como estas" a Daniel (en desarrollo) ⭐
* qué hora es
* ¿estás ahí?
* ¿cómo te llamas?
* hasta luego

## Dependencias / Módulos
### En Windows
* Ejecutar archivo dependencias.bat

### En Linux / macOS
* Ejecutar requirements.txt
``pip install -r requirements.txt``

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
- [x] Responder únicamente cuando se mencione el nombre
- [x] Almacenar la variable de nombre de un archivo local
- [x] Creaer una palabra clave para saber si el asistente esta a la escucha
- [x] Preguntas si el usuario quiere formato de 12 o 24 horas en el asistente de configuración
- [x] Revisar porque al mostrar el banner "PROM2023-2024" lanza una advertencia
- [x] Crear archivo para almacenar contactos con sus números
- [x] Preguntar al usurio que voz de pyttsx3 desea en función de las disponibles (controlar excepción)
- [x] Tomar datos del archivo **config.txt**

### Funciones en desarrollo o por desarrollar

- [ ] Mantenerse escuchando siempre (while True:)
- [ ] Hacer que el envio de mensaje por whatapp sea asincrono
- [ ] Reparar envio de mensajes por whatapp con pywhatkit
- [ ] Preguntar a usuario si quiere usar pywhatkit.send() (ver anotaciones)
- [ ] Mejorar forma en la que se crea archivo config.txt (regular expressions)
- [ ] Optimizar archivo de readfile.py
- [ ] Utilizar modelo de IA y/o IA generativa
- [ ] Recordar peticiones anteriores para charla amena
- [ ] Conteo de suscriptores de un youtuber
- [ ] Reproducir contenido en plataformas distintas a youtube
- [ ] Eliminar todo el texto anterior a la palabra clave donde sea necesario (utilidad de VA)
- [ ] Guardar en un **log.txt** el historial de peticiones 
- [ ] Compatibilidad con productos Govee
    
    El archivo log.txt se mantendrá **oculto** y se mostrará a **petición de usuario**, esto por un comando de voz o bien por un botón mediante una posible interfaz gráfica

***

## Anotaciones
* Si el usuario quiere utilizar pywhatkit.send() (enviar mensajes mediante whatapp web) entonces esto se debe guardar en el archivo de config.txt, si su respuesta es sí, entonces debe crear un archivo contacts.txt con el formato clave:valor con el número de telefono de todas las personas que el usuario desee (como se muestra en contacts.example.txt)
* El archivo **log.txt** debe estar oculto en un principio
* El archivo **PyWhatKit_DB.txt** con los logs de envíos de mensajes por WhatsApp debe estar **oculto siempre**
* El archivo local en el que se almacena la variable de nombre puede ser uno llamado **config.txt** y que este oculto al usuario
* La palabra clave para verificar si el asistente esta a la escucha puede ser "¿Estas ahí?" y el asistente responde si escucha y si no responde es porque no escucha.
* Se debe crear un archivo en formato clave valor con el nombre del contacto y su número de telefono para enviar mensajes de whatapp mediante whatapp web con la utilidad pywhatkit.send()
* Antes de cada mensaje se debe añadir el rol de quien propone dicho mensaje, antes del mensaje del usuario debe aparecer el texto "Usuario: ..." y antes del mensaje del asistente "nombre_asistente: ..."
* El archivo **config.txt** va a contener informaciones para la configuración del asistente y se ejecutara la primera vez que se ejecute el software, para saber cuando se ejecuta por primera vez podemos preguntar con Python "¿el archivo config.txt existe?", si no existe es la primera vez que se ejecuta, se crea el archivo con los siguientes datos:
    1. Nombre del asistente
    2. Formato de fecha preferido
    3. Idioma para la conversion del audio de entrada
    4. Voz del asistente
    5. Rol o postura del asistente
* Es necesario optimizar el programa para que corra más rapidamente, para esto podemos utilizar la menor cantidad de modulos posibles y en lugar de importa todo un modulo, solo importar las funciones o propiedades que necesitamos de un modulo.

**NOTA:** Importar un mismo modulo en 2 archivos distintos no añade peso al programa, el modulo se carga una vez y a partir de ahí siempre que se necesite hace referencia al modulo cargado en memoria.

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
* Manejar **excepción** en caso de que se ejecute el programa **sin** conexión a **internet**

**NOTA:** es necesario un buen microfono para utilizar el software con normalidad, de lo contrario se deberia utilizar la linea alternativa para que el asistente pare de escuchar indefinidamente.

### Errores corregidos
* Manejar la **excepción** en caso de que speech_recognition **no encuentre** microfono
* Manejar **excepción** en caso de que no se encuentren las **variables de entorno** (.env)

***

## Informaciones de interés para los desarrolladores.

* Versión de python: 3.12.1
* Versión de pip: 23.3.2
* Versión de [**dependencias:**](requirements.txt)
* [**Pilares**](assets/estructuras_de_control.jpeg) del proyecto

### Explicación de ramas
* **main** rama principal, no se trabaja sobre esta rama, es unicamente para mergear todos los cambios
* **file** rama para trabajar con nuevos modulos o modulos existentes para el proyecto
* **feature** rama para desarrollar una nueva caracteristica en el propio archivo del asistente (va.py)
* **backup** rama para realizar copias de seguridad con regularidad, no se trabaja en esta rama

### Comandos para cambiar de rama
**Cuando inicies a trabajar**
```git checkout nombre_rama```

**Cuando termines de trabajar**
```git push origin nombre_rama```

<div align="center">
  <br>
  <h2>🐍 Mis contribuciones 🐍</h2>
  <br>
  <img alt="snake eating my contributions" src="https://raw.githubusercontent.com/salesp07/salesp07/output/github-contribution-grid-snake-dark.svg" />
  
  <br/><br/>
</div>

### Informaciones adicionales
*Explicación de códigos y funciones en* [**documentation.**](DOCUMENTATION.md)

*Más información en* [**historia.**](HISTORY.md)