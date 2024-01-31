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


name = "Jarvis" # Nombre por el que se llamara al asistente (para desarrollar más tarde)
lang ='es-ES'

# assistant_role: "Eres un asistente virtual que habla en verso y responde de manera cortez."
prompt = "Dime de manera detallada como puedo crear una función en python."


# Audio - Modulo 1
rec = sr.Recognizer()

# Acceder al microfono del dispositivo
with sr.Microphone() as source:
    try:
        print("Escuchando...")
        audio = rec.listen(source, timeout=1)

        text = rec.recognize_google(audio, language = lang)
        print("Texto: " + text)
        prompt = text
    except sr.WaitTimeoutError:
        print("No se detecto entrada de audio.")
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio")
    except sr.RequestError as e:
        print("No se pudo solicitar resultados de Google Speech Recognition; {0}".format(e))

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

try:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente virtual que habla en verso y responde de manera cortez."},
        {"role": "user", "content": prompt}
    ])
    print(completion.choices[0].message)
except Exception as err:
    print(err)


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