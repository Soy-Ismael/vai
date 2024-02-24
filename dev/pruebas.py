# Importaciones 
import speech_recognition as sr
from dotenv import load_dotenv
import pyttsx3
import pywhatkit
import os
#Reproducir sonido
import winsound
#Buscar
import webbrowser
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


name = "jarvis" # Nombre por el que se llamara al asistente (para desarrollar más tarde)
lang ='es-ES'

# assistant_role: "Eres un asistente virtual que habla en verso y responde de manera cortez."
# prompt = "Dime de manera detallada como puedo crear una función en python."


# De texto a voz - Modulo 6
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

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
        print("Escuchando...")
        # Intentando reproducir un sonido
        winsound.PlaySound('sounds/Sonido_apertura.wav', winsound.SND_FILENAME)
        audio = rec.listen(source)
        print("Analizando...")
        text = rec.recognize_google(audio, language = lang)
        # print("Texto: " + text)
        text = text.lower()
        winsound.PlaySound('sounds/Sonido_Cierre.wav', winsound.SND_FILENAME)


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
# load_dotenv()

# Almanecar variable de entorno en una variable de python con dotenv
# open_ai_api = os.getenv('OPENAI_API_KEY')
# print(open_ai_api)

# Variables de entorno

#* Chat GPT
# client = OpenAI()
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

def run():
    if 'reproduce' in text:
        music = text.replace('reproduce', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'busca' in text:
        search_query = text.replace('busca', '')
        talk('Buscando en el navegador ' + search_query)
        webbrowser.open('https://www.google.com/search?q=' + search_query)

run() 

#* GEMINI Pro
# google_api_key = os.getenv('GOOGLE_API_KEY')

# Or use os.getenv('GOOGLE_API_KEY') to fetch an environment variable.
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