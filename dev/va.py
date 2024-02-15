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
import random #Nuevo modulo
import wikipedia #Nuevo modulo
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
cian_color = "\033[96m"
blue_color = "\033[94m"
yellow_color = "\033[93m"
red_color = "\033[91m"
negrita = "\033[1m"
subrayado = "\033[4m"
normal_color = "\033[0m"

# Banner para la terminal al ejecutar

# print(f'''{negrita} {blue_color}
# ____________ ________  ___ _____  _____  _____  _____        _____  _____  _____   ___ 
# | ___ \ ___ \  _  |  \/  |/ __  \|  _  |/ __  \|____ |      / __  \|  _  |/ __  \ /   |
# | |_/ / |_/ / | | | .  . |`' / /'| |/' |`' / /'    / /______`' / /'| |/' |`' / /'/ /| |
# |  __/|    /| | | | |\/| |  / /  |  /| |  / /      \ \______| / /  |  /| |  / / / /_| |
# | |   | |\ \\\\ \_/ / |  | |./ /___\ |_/ /./ /___.___/ /      ./ /___\ |_/ /./ /__\___  |
# \_|   \_| \_|\___/\_|  |_/\_____/ \___/ \_____/\____/       \_____/ \___/ \_____/   |_/
# {normal_color}''')


name = 'jarvis' # Nombre por el que se llamara al asistente (para desarrollar más tarde)
lang = 'es-ES'
time_format = "%I:%M:%p"
user_template = f"{negrita}Usuario: {normal_color}"
va_template = f"{negrita}{name}: {normal_color}"
err_template = f"{red_color}{negrita}ERROR: {normal_color}"
wiki_lang = 'es'
# format24 = "%H:%M"
# format12 = "%I:%M"

# assistant_role: "Eres un asistente virtual que habla en verso y responde de manera cortez."
# prompt = "Dime de manera detallada como puedo crear una función en python."


# De texto a voz - Modulo 6
engine = pyttsx3.init()

try:
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
except IndexError:
    print("No existe la voz con el ID 3, asegurese de tener ingles, español de españa y español mexico instalado en su windows")
    talk("Error en configuración de idiomas")

# for voice in voices:
#     print(voice)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# talk("Hola, ¿como estas?")


# De voz a texto - Modulo 1 & 2
rec = sr.Recognizer()

# Acceder al microfono del dispositivo
try:
    with sr.Microphone() as source:
        try:
            print(f"{green_color}Escuchando... {normal_color}")
            audio = rec.listen(source,  timeout = 0.9, phrase_time_limit = 4)
            print(f"{blue_color}Analizando... {normal_color}")
            text = rec.recognize_google(audio, language = lang)
            # print("Texto: " + text)
            print(user_template + text)
            text = text.lower()

            if name in text:
                text = text.replace(name, '')
                print('Texto con nombre omitido: ' + text)

            prompt = text
            # talk(text)

        except sr.WaitTimeoutError:
            print(err_template + 'No se detecto entrada de audio.')
        except sr.UnknownValueError:
            print(err_template + 'Google Speech Recognition no pudo entender el audio.')
        except sr.RequestError as e:
            print(err_template + f"No se pudo solicitar resultados de Google Speech Recognition; {0}".format(e))
        except KeyboardInterrupt:
            print(err_template + 'Acción cancelada por el usuario.')
except KeyboardInterrupt:
    print(err_template + 'Acción cancelada por el usuario.')
except:
    print(err_template + 'No hay microfono seleccionado')
    talk('No se encontro microfono, por favor, configure el dispositivo de entrada')


#* =========================
#* PARTE DE Ismael Y Xaviel - con open AI
#* =========================
# Cargar las variables de entorno (variables contenidas en archivos .env)
#todo load_dotenv()

# Almanecar variable de entorno en una variable de python con dotenv
# open_ai_api = os.getenv('OPENAI_API_KEY')
# print(open_ai_api)

# Variables de entorno

#* Chat GPT
#todo client = OpenAI()
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

text = 'busca cual es la mejor manera de cocinar el pollo'
def run():
    if 'reproduce' in text:
        music = text.replace('reproduce', '')
        # print('Texto con nombre omitido: ' + text)
        pywhatkit.playonyt(music)
        talk('Reproduciendo ' + music)
        # print(f'{negrita}{name}: {normal_color}Reproduciendo ' + music)
        print(va_template + 'Reproduciendo ' + music)

def search():
    if 'busca' in text:
        busqueda = text.replace('busca', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Buscando ' + busqueda)
        pywhatkit.search(busqueda)
        # Esta funcion busca en el motor de busqueda google.com, valga la redundancia
        print(f"{va_template}Buscando {busqueda}")

def info():
    if 'información sobre' in text and 'ingles' in text:
        info = text.replace('información sobre', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Resumiendo informacion sobre ' + info + ' en wikipedia')
        talk(pywhatkit.info(info))
        # Esta funcion unicamente devuelve resumen en la consola (no puedo almacenar el resumen en variable), y lo devuelve en ingles, para almacenar el resumen y poder cambiar el idioma necesito utilizar el modulo de wikipedia (ejemplo mostrado arriba), que es el mismo modulo que utiliza pywhatkit internamente.
        print(f"{va_template}resumiendo {info} en wikipedia en ingles")
    
    if 'información sobre' in text:
        # wikipedia.set_lang = 'es'
        wikipedia.set_lang(wiki_lang)
        info = text.replace('información sobre', '')

        resumen = wikipedia.summary(info)
        print(va_template + resumen)
        talk(resumen)

# * Diferencia entre search e info
# search: La función pywhatkit.search("Palabra clave") abre tu navegador predeterminado y realiza una búsqueda en Google con la “Palabra clave” que proporcionaste. Te mostrará todos los resultados de búsqueda relacionados con esa palabra clave en Google.

# info: Por otro lado, la función pywhatkit.info("Tema") te proporciona una breve información sobre el “Tema” que proporcionaste. Esta función utiliza la biblioteca wikipedia para buscar el tema y devuelve un resumen del artículo de Wikipedia correspondiente.

# Por lo tanto, la principal diferencia es que search realiza una búsqueda en Google e info proporciona un resumen de un artículo de Wikipedia.


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

        # Suma 1 minuto a la hora actual
        #* minuto_extra = datetime.timedelta(minutes=1)
        nueva_hora = hora_actual + datetime.timedelta(minutes=1)
        # nueva_hora = datetime.datetime.strftime(nueva_hora, "%H:%M")

        # print(nueva_hora.strftime("%I,%M")) Esto funciona
        # Imprime la nueva hora en formato de 24 horas
        # print("Nueva hora: ", nueva_hora.strftime("%H:%M:%S"))
        # nueva_hora_formateada = nueva_hora.strftime(str(int("%H")) , str(int("%M")+1))
        # print("Nueva hora: ", nueva_hora.strftime("%H:%M"))

        # print("Nueva horaH: ", nueva_hora.strftime("%H"))
        # print("Nueva horaM: ", nueva_hora.strftime("%M"))
        # print("Nueva horaM: ", nueva_hora.strftime("%S"))
        # print("Nueva hora: ", nueva_hora.strftime(str("%H")+ ',' +str("%M") + ',' + str("%S")))

        #* print(hora_actual.strftime("%I:%M"))
        #* print(nueva_hora.strftime("%I:%M"))
        # print(nueva_hora_formateada)
        try:
            pywhatkit.sendwhatmsg("+18094584686",msg, nueva_hora.hour, nueva_hora.minute, 15, True, 3)
            talk(f"Enviando mensaje al número seleccionado")
            print(va_template + "Enviando mensaje al número seleccionado")
        except:
            print(err_template + "en el envío de mensaje, por favor, vuelve a intentarlo.")
            talk("Error en el envío de mensaje, por favor, vuelve a intentarlo.")
        # pywhatkit.sendwhatmsg("numero con prefijo","mensaje", 23,57)

def time():
    if 'qué hora es' in text:
        # print(f"Son las {datetime.datetime.now().strftime("%I:%M")}")
        # talk(f"Son las {datetime.datetime.now().strftime("%I:%M")}")
        time = datetime.datetime.now().strftime("%I:%M")
        time_es = datetime.datetime.now().strftime("%I:%M:%p")
        
        # print(time)
        # print(time_es)
        #print(type(time)) es string

        changeShape = random.randint(0,2)
        # print(changeShape)

        if(changeShape == 0):
            print(va_template + f"Son las {time}")
            talk(va_template + f"Son las {time}")

        elif(changeShape == 1):
            if(datetime.datetime.now().strftime('%p') == 'PM'):
                print(va_template + f"Son las {time} de la tarde")
                talk(va_template + f"Son las {time} de la tarde")
            else:
                print(va_template + f"Son las {time} de la mañana")
                talk(va_template + f"Son las {time} de la mañana")
        else:
            print(va_template + f"Son las {time_es}")
            talk(va_template + f"Son las {time_es}")

try:
    run()
    search()
    info()
    send()
    time()
except NameError:
    print("Entrada de audio inválida, intentalo nuevamente")
    talk("Entrada de audio inválida, intentalo nuevamente")
except KeyboardInterrupt:
    print(err_template + 'Acción cancelada por el usuario.')

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