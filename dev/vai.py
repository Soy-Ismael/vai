# ESTRUCTURA Y REPARTICION DE TRABAJO DEL ASISTENTE
# *     Jared y Jairon
#todo 1 - Grabar voz del usuario 🎤
#todo 2 - Convertir lo que dijo en texto 🖋
# 
# *     Xaviel e Ismael
#todo 3 - Procesar la intención del usuario ❓ (modelo de IA)
#todo 4 - Ejecutar la acción deseada 👨‍🏭
# 
# ?      Proximamente
#todo 5 - Preparar respuesta (en texto) 💬
#todo 6 - Convertir en audio y reproducir 🦻

# Importaciones 
import speech_recognition as sr
from dotenv import load_dotenv
import datetime
import pyttsx3
import pywhatkit
import os
# Open AI - Chat Gpt
from openai import OpenAI
# Google - Gemini
# import pathlib
# import textwrap

# import google.generativeai as genai

# Used to securely store your API key
# from google.colab import userdata

# from IPython.display import display
# from IPython.display import Markdown


# def to_markdown(text):
#     text = text.replace('•', '  *')
#     return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# colors
# green_color = "\033[1;32;40m"
# red_color = "\033[1;31;40m"
# normal_color = "\033[0;37;40m"
green_color = "\033[92m"
cian = "\033[96m"
azul = "\033[94m"
amarillo = "\033[93m"
red_color = "\033[91m"
negrita = "\033[1m"
subrayado = "\033[4m"
normal_color = "\033[0m"

#* Módulo de wikipedia para resumen en español y capacidad para almacenar respuesta (pywhatkit.info()):
# import wikipedia

#* Establecer el idioma en español
# wikipedia.set_lang("es")

#* Obtener un resumen de un artículo de Wikipedia
# resumen = wikipedia.summary("Python (lenguaje de programación)")
# print(resumen)
#* Fin del codigo para resumen de wikipedia 

name = "jarvis" # Nombre por el que se llamara al asistente (para desarrollar más tarde)
lang = 'es-ES'

# assistant_role: "Eres un asistente virtual que habla en verso y responde de manera cortez."
# prompt = "Dime de manera detallada como puedo crear una función en python."


# De texto a voz - Modulo 6
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

# for voice in voices:
#     print(voice)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# talk("Hola, ¿como estas?")


# De voz a texto - Modulo 1 & 2
rec = sr.Recognizer()

# Acceder al microfono del dispositivo
with sr.Microphone() as source:
    try:
        print(f"{green_color} Escuchando... {normal_color}")
        audio = rec.listen(source,  timeout = 0.9, phrase_time_limit = 4)
        print("Analizando...")
        text = rec.recognize_google(audio, language = lang)
        # print("Texto: " + text)
        text = text.lower()

        if name in text:
            text = text.replace(name, '')
            print('Texto con nombre omitido: ' + text)

        prompt = text
        print("Texto: " + text)
        # talk(text)

    except sr.WaitTimeoutError:
        print("No se detecto entrada de audio.")
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio.")
    except sr.RequestError as e:
        print("No se pudo solicitar resultados de Google Speech Recognition; {0}".format(e))
    except KeyboardInterrupt:
        print("Acción cancelada por el usuario.")

#* =========================
#* PARTE DE Ismael Y Xaviel - con open AI
#* =========================
# Cargar las variables de entorno (variables contenidas en archivos .env)
load_dotenv()

# Almanecar variable de entorno en una variable de python con dotenv
# open_ai_api = os.getenv('OPENAI_API_KEY')
# print(open_ai_api)

# Variables de entorno

#* Chat GPT
client = OpenAI()
# print(client.api_key)

# *INICIO CHAT GPT - Modulo 3 & 4
#* Este primer bloque se utiliza para interacciones con usuario
# try:
#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "Eres un asistente virtual que habla en verso y responde de manera cortez."},
#         {"role": "user", "content": prompt}
#     ])
#     print(completion.choices[0].message)
# except Exception as err:
#     print(err)

#* Modulo 5
#* Este segundo bloque se utiliza para interpretación y ejecución de peticiones de usuario (se ejecuta por detras)

# try:
#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "Eres un asistente virtual que interpreta las intenciónes del usuario y las clasifica de manera objetiva sin aunar descripción para ser posteriormente procesado y ejecutado lo que el usuario quiere realizar"},
#         {"role": "user", "content": "¿Cuál es la intención del usuario segun este prompt?: " + prompt}
#     ])
#     intencion = completion.choices[0].message
#     print(intencion)
# except Exception as err:
#     print(err)
# *FINAL CHAT GPT

#* Ejecutar accion (funcion para escuchar musica en youtube)

#* Enviar mensajes de whatapp
# pywhatkit sirve para enviar mensajes de WhatsApp: Utilice la función pywhatkit.sendwhatmsg() para enviar mensajes de WhatsApp a cualquier número de WhatsApp en un momento determinado. La sintaxis es la siguiente: pywhatkit.sendwhatmsg("número de móvil del receptor", "mensaje", horas, minutos). Asegúrese de que el número de móvil del receptor esté en formato de cadena y el código del país se mencione antes del número de móvil. Las horas siguen el formato de 24 horas. Los minutos son los minutos de la hora programada para el mensaje (00-59). Por ejemplo, para enviar un mensaje a un número de WhatsApp a las 22:28, utilice la siguiente sintaxis: pywhatkit.sendwhatmsg("+91xxxxxxxxxx", "Hola desde Mi Diario Python", 22, 28)


def run():
    if 'reproduce' in text:
        music = text.replace('reproduce', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)

def search():
    if 'busca' in text:
        busqueda = text.replace('busca', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Buscando ' + busqueda)
        pywhatkit.search(busqueda)
        # Esta funcion busca en el motor de busqueda google.com, valga la redundancia

def info():
    if 'información sobre' in text:
        info = text.replace('información sobre', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Resumiendo informacion sobre ' + info + ' en wikipedia')
        talk(pywhatkit.info(info))
        # Esta funcion unicamente devuelve resumen en la consola (no puedo almacenar el resumen en variable), y lo devuelve en ingles, para almacenar el resumen y poder cambiar el idioma necesito utilizar el modulo de wikipedia (ejemplo mostrado arriba), que es el mismo modulo que utiliza pywhatkit internamente.

def send():
    if 'enviar' in text:
        msg = text.replace('enviar', '')
        # "Esto es un mensaje de prueba desde python"

        #* Modulo para obtener el tiempo actual y sumarle 10 segundos para la funcion de enviar mensaje por whatapp
        # Obtén la hora actual
        hora_actual = datetime.datetime.now()

        # Imprime la hora actual en formato de 24 horas
        # print("Hora actual: ", hora_actual)
        # print("Hora actual: ", hora_actual.strftime("%H:%M:%S"))

        # Suma 10 segundos a la hora actual
        nueva_hora = hora_actual + datetime.timedelta(minutes=1)

        # Imprime la nueva hora en formato de 24 horas
        # print("Nueva hora: ", nueva_hora.strftime("%H:%M:%S"))
        nueva_hora_formateada = nueva_hora.strftime(int(str("%H")) , int(str("%M")))
        # print("Nueva hora: ", nueva_hora.strftime("%H:%M"))

        # print("Nueva horaH: ", nueva_hora.strftime("%H"))
        # print("Nueva horaM: ", nueva_hora.strftime("%M"))
        # print("Nueva horaM: ", nueva_hora.strftime("%S"))
        # print("Nueva hora: ", nueva_hora.strftime(str("%H")+ ',' +str("%M") + ',' + str("%S")))

        print(nueva_hora_formateada)
        # pywhatkit.sendwhatmsg("+18094584686",msg, nueva_hora_formateada)
        # pywhatkit.sendwhatmsg("numero con prefijo","mensaje", 23,57)

# * Diferencia entre search e info
# search: La función pywhatkit.search("Palabra clave") abre tu navegador predeterminado y realiza una búsqueda en Google con la “Palabra clave” que proporcionaste. Te mostrará todos los resultados de búsqueda relacionados con esa palabra clave en Google.

# info: Por otro lado, la función pywhatkit.info("Tema") te proporciona una breve información sobre el “Tema” que proporcionaste. Esta función utiliza la biblioteca wikipedia para buscar el tema y devuelve un resumen del artículo de Wikipedia correspondiente.

# Por lo tanto, la principal diferencia es que search realiza una búsqueda en Google e info proporciona un resumen de un artículo de Wikipedia.

run()
search()
info()
send()

#* GEMINI Pro
# google_api_key = os.getenv('GOOGLE_API_KEY')

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# google_api_key = userdata.get('GOOGLE_API_KEY')

# print(google_api_key) 
# print(type(google_api_key))

# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])

# response = chat.send_message("Dime como puedo crear una funcion en python.")
# to_markdown(response.text)
# print(response.text)
# print(chat.history)

# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])
# print(model.count_tokens)
# print(chat.model)

# response = chat.send_message(
#     "Pretend you\'re a snowman and stay in character for each response.")
# # print(response.text)

# response = chat.send_message(
#     "What\'s your favorite season of the year?")
# # print(response.text)




# google_api_key = os.getenv('GOOGLE_API_KEY')
# genai.configure(api_key= google_api_key)

# model = genai.get_model("tunedModels/gemini-pro") # Elige el modelo gemini-pro
# prompt = "¿Qué es la inteligencia artificial?" # Define tu entrada de texto
# response = model.generateContent(prompt=prompt) # Genera una respuesta de texto
# print(response) # Imprime la respuesta