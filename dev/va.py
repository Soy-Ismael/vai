# Dato curioso a fecha de hoy 5/marzo/2024 3:27 hora dominicana hay un total de 529 lineas de código en va.py, hay 265 lineas de código y otras 264 de cómentarios aproximadamente (los espacios en blanco se contaron como lineas de código).
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
import pyttsx3
from dotenv import load_dotenv
import datetime
import pywhatkit
import os
import random #Nuevo modulo para generar números aleatorios
import wikipedia #Nuevo modulo para resumir articulos de wikipedia
import winsound #Nuevo modulo para reproducir sonido, (no es necesario instalar con pip)
# import urllib.request #Nuevo modulo para conteo de suscriptores
import pyjokes
import spoty
# from sys import exit #Para trabajar con sys.exit() en caso de ser necesario
from banner import printBanner #Nuevo modulo para banner
from config import check_config, create_config_file, initial_config #Nuevo modulo para configuracion de asistente
from readfile import check_file_integrity, readfile
from transfer_data import Transaction
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

#* Default const
# name = 'jarvis' # Nombre por el que se llamara al asistente (para desarrollar más tarde)
# lang = 'es-ES'
# time_format = "%I:%M:%p"
# wiki_lang = 'es'

#* Obtener constantes del archivo config.text
# Esto se hace mas adelante en el códgio

#* Default const - open AI mode#
#  assistant_role: "Eres un asistente virtual que habla en verso y responde de manera cortez."
# prompt = "Dime de manera detallada como puedo crear una función en python."

# Instanciar clase Transaction
Data_transfer = Transaction()

#* Colors
green_color = "\033[92m"
cian_color = "\033[96m"
blue_color = "\033[94m"
yellow_color = "\033[93m"
red_color = "\033[91m"
negrita = "\033[1m"
subrayado = "\033[4m"
normal_color = "\033[0m"

#* Templates
user_template = f"{negrita}Usuario: {normal_color}"
# va_template = f"{negrita}{name}: {normal_color}" #Declarada más abajo
err_template = f"{red_color}{negrita}ERROR: {normal_color}"
warning_template = f"{yellow_color}{negrita}ADVERTENCIA: {normal_color}"


# De texto a voz - Modulo 6
engine = pyttsx3.init()

try:
    # global voice
    voice_id = 0

    # if voice != None:
    #     voice_id = voice

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
except IndexError:
    print(f"No existe la voz con el ID {voice_id}, asegurese de tener ingles, español de españa y español de mexico instalado en su windows")
    print(f"{err_template}en configuración de idiomas")

    for voice in voices:
        print(f'{yellow_color} = = = = = = = =  = = = = = = {normal_color}')
        print(f'ID:{cian_color} {voice.id} {normal_color}')
        print(f'Name:{cian_color} {voice.name} {normal_color}')
        # print(f'Languages:{cian_color} {voice.languages} {normal_color}')
        # print(f'Age:{cian_color} {voice.age} {normal_color}')
        # print(f'Gender:{cian_color} {voice.gender} {normal_color}')

    #! No utilizar el exit() para programas reales, lo mejor seria utilizar el sys.exit()
    exit()
    # sys.exit()

# for voice in voices:
#     print(voice)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def no_talk():
    engine.stop()
# talk("Hola, ¿como estas?")


# De voz a texto - Modulo 1 & 2
rec = sr.Recognizer()

# Ajuste del umbral de audio (En términos simples, si la energía (volumen) de la señal de audio es mayor que el umbral, el sistema considera que está recibiendo voz. Si la energía es menor que el umbral, el sistema considera que no hay voz y que cualquier sonido que esté recibiendo es simplemente ruido)

# 2300 tiene problemas para entender
# rec.energy_threshold = 2900

#* Función para escuchar la petición del usuario, se puede invocar durante la ejecución del programa, lo que permite que el asistente pueda volver a escuchar en cualquier punto del programa con solo invocar la función
def listen():
    # Acceder al microfono del dispositivo
    try:
        # print(text)
        with sr.Microphone() as source:
            try:
                text = ''
                status = False

                print(f"{green_color}Escuchando... {normal_color}")

                winsound.PlaySound('sounds/sonido_apertura.wav', winsound.SND_FILENAME)
                # rec.adjust_for_ambient_noise(source,duration=1) #Ajustar para ruido de fondo, toma una muestra de 1 segundo para el ruido de fondo
                audio = rec.listen(source)

                #? Linea alternativa si el asistente escucha indefinidamente
                # audio = rec.listen(source, timeout = 2, phrase_time_limit = 4)

                print(f"{blue_color}Analizando... {normal_color}")
                text = rec.recognize_google(audio, language = lang).lower()
                # print("Texto: " + text)

                winsound.PlaySound('sounds/sonido_cierre.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                print(user_template + text)

                if name in text:
                    text = text.replace(name, '')
                    # print('Texto con nombre omitido: ' + text)
                    status = True

                # prompt = text
                # talk(text)
                # return text
                return {'text': text, 'status': status}
                
            except sr.WaitTimeoutError:
                print(err_template + 'No se detecto entrada de audio.')
                # return False
            except sr.UnknownValueError:
                print(err_template + 'Google Speech Recognition no pudo entender el audio.')
                talk('No he podido entender eso, intentemoslo nuevamente')
                listen()
            except sr.RequestError as e:
                print(err_template + f"No se pudo solicitar resultados de Google Speech Recognition; {0}".format(e))
                # return False
            except TypeError:
                print(err_template + 'Variable aun sin datos')
                # return False
            except KeyboardInterrupt:
                print(err_template + 'Acción cancelada por el usuario.')
                # return False
            winsound.PlaySound('sounds/Sonido_Cierre.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

    except KeyboardInterrupt:
        print(err_template + 'Acción cancelada por el usuario.')
        # return False
    except TypeError:
        print(err_template + 'Variable aun sin datos')
        # return False
    except:
        print(err_template + 'No hay microfono seleccionado')
        talk('No se encontro microfono, por favor, configure el dispositivo de entrada')
        # return False


#* IMPORTACIÓN DE FUNCIONES DE ARCHIVOS EXTERNOS
# La funcion printBanner se importa del archivo banner.py y recibe el color del banner como primer parametro opcional y un segundo parametro opcional booleano que define si el banner se imprime en negrita o no

# printBanner()
# check_config()

# print('Check config', check_config())
try:
    def load_data(data_to_extract):
        global name, lang, wiki_lang, time_format, voice
        # config_name, config_lang, time_format, voice = data_to_extract

        # name = config_name
        # lang = config_lang
        # wiki_lang = config_lang[slice(0,2)]

        # print('Nombre: ' + name)
        # print('Idioma: ' + lang)
        # print('Idioma de wikipedia: ' + wiki_lang)
        # print('Formato de hora: ' + time_format)
        # print('Indice de voz: ' + voice)

        # print('===========================')
        name, lang, time_format, voice = data_to_extract
        wiki_lang = lang[slice(0,2)]

        # print('Nombre: ' + name)
        # print('Idioma: ' + lang)
        # print('Idioma de wikipedia: ' + wiki_lang)
        # print('Formato de hora: ' + time_format)
        # print('Indice de voz: ' + voice)


    data = readfile()
    if type(data) != dict or not check_file_integrity():
        # print(err_template+'Archivos de configuración corruptos')
        (err_template+'Datos de configuración corruptos o inexistentes')
        talk('Error en datos de configuración, por favor restablezca el archivo.')
        initial_config()

        data = readfile()
        load_data(data.values())
    else:
        load_data(data.values())
except KeyboardInterrupt:
    print(f'\n{warning_template}Acción cancelada por el usuario.')


def init_configuration():
    try:
        response:str = listen()

        if('sí' in response or 'si' in response):
            print('Entro en si en respuesta')
            create_config_file()
            initial_config()

        else:
            print('Entro en no en respuesta')
            print('Archivo de configuración no creado a petición de usuario, continuando con ejecución')
            print('Cargando valores por defecto...')

            name = 'va'
            lang = 'es-ES'
            time_format = "%I:%M %p"
            wiki_lang = 'es'
            voice_number = 0

            talk('Esta bien, continuando con la ejecución')
    except:
        print('Audio no reconocido')
        talk('No pude entender lo que has dicho, ¿Te importaria repetirlo?')
        init_configuration()

# init_configuration()

#* Templates 2
va_template = f"{negrita}{name}: {normal_color}"

#* Ejecutar la función para escuchar al usuario
text = listen()
# text = {'text' : 'envía Hola ¿cómo estas? a raylin', 'status': True}

# print(Transaction)
# print(type(Transaction))

# listen()
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
# try:
#     client = OpenAI()
#    # print(client.api_key)
# except:
#     print(err_template+'No se pudo obtener el api de OPEN AI')
#     talk('No se pudo obtener el api de OPEN AI, por favor revise el archivo .env')

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

# print(text)
# print(text['text'])
# print(text['status'])

def run():
    global text
    if 'reproduce' in text['text']:
        if 'spotify' in text['text']:
            music = text['text'].replace('reproduce', '')
            music = music.replace('jarvis', '')
            music = music.replace('spotify', '')
            talk('Reproduciendo ' + music)
            spoty.play(keys["spoty_client_id"], keys["spoty_client_secret"], music)
        else:
            music = text['text'].replace('reproduce', '')
            music = music.replace('jarvis', '')
            pywhatkit.playonyt(music)
            talk('Reproduciendo ' + music)
            # print(f'{negrita}{name}: {normal_color}Reproduciendo ' + music)
            print(va_template + 'Reproduciendo' + music)

    elif 'busca' in text['text']:
        busqueda = text['text'].replace('busca', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Buscando ' + busqueda)
        pywhatkit.search(busqueda)
        # Esta funcion busca en el motor de busqueda google.com, valga la redundancia
        print(f"{va_template}Buscando {busqueda}")

    elif 'información sobre' in text['text'] and 'ingles' in text['text']:

        info = text['text'].replace('información sobre', '')
        info = text['text'].replace('en', '')
        info = text['text'].replace('dame', '')
        info = text['text'].replace('dime', '')
        info = text['text'].replace('ofreceme', '')
        info = text['text'].replace('ofréceme', '')

        # print('Texto con nombre omitido: ' + text)
        talk('Resumiendo informacion sobre ' + info + ' en wikipedia')
        talk(pywhatkit.info(info))
        # Esta funcion unicamente devuelve resumen en la consola (no puedo almacenar el resumen en variable), y lo devuelve en ingles, para almacenar el resumen y poder cambiar el idioma necesito utilizar el modulo de wikipedia (ejemplo mostrado arriba), que es el mismo modulo que utiliza pywhatkit internamente.
        print(f"{va_template}resumiendo {info} en wikipedia en ingles")
    
    elif 'información sobre' in text['text']:
        # wikipedia.set_lang = 'es'
        wikipedia.set_lang(wiki_lang)
        
        info = text['text'].replace('información sobre', '')
        info = text['text'].replace('dame', '')
        info = text['text'].replace('dime', '')
        info = text['text'].replace('ofreceme', '')
        info = text['text'].replace('ofréceme', '')

        resumen = wikipedia.summary(info)
        print(va_template + resumen)
        talk(resumen)

# * Diferencia entre search e info
# search: La función pywhatkit.search("Palabra clave") abre tu navegador predeterminado y realiza una búsqueda en Google con la “Palabra clave” que proporcionaste. Te mostrará todos los resultados de búsqueda relacionados con esa palabra clave en Google.

# info: Por otro lado, la función pywhatkit.info("Tema") te proporciona una breve información sobre el “Tema” que proporcionaste. Esta función utiliza la biblioteca wikipedia para buscar el tema y devuelve un resumen del artículo de Wikipedia correspondiente.

# Por lo tanto, la principal diferencia es que search realiza una búsqueda en Google e info proporciona un resumen de un artículo de Wikipedia.

    elif 'chiste' in text['text']:
        chiste = pyjokes.get_joke(wiki_lang)
        print(va_template + chiste)
        talk(chiste)
        winsound.PlaySound('sounds/redoble_de_tambores.wav', winsound.SND_FILENAME)


    elif 'envía' in text['text']:
        text = text['text'].replace('envía', '')

        #! EJEMPLO DE LO QUE SE ESPERA COMO ENTRADA "ENVIAR MENSAJE A DANIEL", ELIMINAR LA FRASE ENVIAR O ENVIA Y TOMAR LA VOCAL "A" COMO SEPARADOR, LO QUE ESTA DESPUES DE LA "A" SERA EL CONTACTO A QUIEN SE LE ENVIARA QUE SE DEBERA BUSCAR EN EL ARCHIVO CONTACTS.TXT Y LO QUE ESTA ANTES DE "A" Y DESPUES DE "ENVIA" O "ENVIAR" SERA EL MENSAJE.

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
            msg, contact = text.split(' a ')
            # print('Mensaje ' + msg)
            # print('contacto ' + contact)

            contact = Data_transfer.read_phone_numbers(contact)

            #? talk(f"El mensaje se enviara en unos segundos")
            talk(f"El mensaje se enviara en unos segundos")
            # print(contact, msg, nueva_hora.hour, nueva_hora.minute, 15, True, 3)

            # pywhatkit.sendwhatmsg(contact, msg, nueva_hora.hour, nueva_hora.minute, 15, True, 3)
            pywhatkit.sendwhatmsg('+18574928689', msg, nueva_hora.hour, nueva_hora.minute, 3, True, 5)
            talk(f"Mensaje enviado al número seleccionado")
            print(va_template + "Mensaje enviado al número seleccionado")
        except:
            print(err_template + "en el envío de mensaje, por favor, vuelve a intentarlo.")
            talk("Error en el envío de mensaje, por favor, vuelve a intentarlo.")
        # pywhatkit.sendwhatmsg("numero con prefijo","mensaje", 23,57)


    elif 'qué hora es' in text['text']:
        # print(f"Son las {datetime.datetime.now().strftime("%I:%M")}")
        # talk(f"Son las {datetime.datetime.now().strftime("%I:%M")}")

        # time = datetime.datetime.now().strftime("%I:%M")
        time = datetime.datetime.now().strftime(time_format[slice(0,5)])
        # time_es = datetime.datetime.now().strftime("%I:%M:%p")
        time_es = datetime.datetime.now().strftime(time_format)
        
        # print(time)
        # print(time_es)

        if(time.startswith('0')):
            time = time[slice(1,(time.__len__()+1))]
            time_es = time_es[slice(1,(time.__len__()+1))]
            # print('Ajustado: '+ time)
            # print('Ajustado: '+ time_es)

        changeShape = random.randint(0,2)
        # print(changeShape)

        if(changeShape == 0):
            print(va_template + f"Son las {time}")
            talk(f"Son las {time}")

        elif(changeShape == 1):
            if(datetime.datetime.now().strftime('%p') == 'PM'):
                print(va_template + f"Son las {time} de la tarde")
                talk(f"Son las {time} de la tarde")
            else:
                print(va_template + f"Son las {time} de la mañana")
                talk(f"Son las {time} de la mañana")
        else:
            print(va_template + f"Son las {time_es}")
            talk(f"Son las {time_es}")


    #! IMPORTANTE
    #* Con global le indico que la variable text sera global en lugar de local, como la variable text existe, entonces estoy indicando que quiero utilizar la variable global y no crear una variable nueva dentro de la función, esto deberia solucionar el error de "UnboundLocalError" 
    # global text
    elif 'estás ahí' in text['text']:
        print(True)
        print(va_template + 'Sí, ¿En qué te puedo ayudar?')
        talk('Sí, ¿En qué te puedo ayudar?')
        text = name + ' ' + listen()


    # global text
    elif 'cómo te llamas' in text['text']:
        print(name)
        talk('Soy' + name + '¿Cómo te puedo ayudar?')
        # text = listen()

    elif 'muestrame el archivo de configuración' in text['text'] or 'muéstrame el archivo de configuración' in text['text']:
        print('Mostrando el contenido del archivo de configuración')
        talk('Mostrando el contenido del archivo de configuración')

        print('Nombre del asistente: ' + name)
        print('Idioma: ' + lang)
        print('Idioma de wikipedia: ' + wiki_lang)
        print('Formato de hora: ' + '12' if time_format.startswith('%I') else '24' + 'horas')
        print('Indice de voz: ' + voice)

        talk('Nombre del asistente: ' + name)
        talk('Idioma: ' + lang)
        talk('Idioma de wikipedia: ' + wiki_lang)
        talk('Formato de hora: ' + '12' if time_format.startswith('%I') else '24' + 'horas')
        talk('Indice de voz: ' + voice)
        
    
    elif 'crea una nueva configuración' in text['text'] :
        talk('Creando archivo de configuración nuevamente')
        initial_config()
        load_data(readfile().values())


    elif 'hasta luego' in text['text']:
        talk(f'Hasta pronto')
        os._exit(0)


    # elif 'cuántos suscriptores tiene' in text or 'cuantos suscriptores tiene' in text:
    #     key = os.getenv('GOOGLE_API_KEY_YOUTUBE')
    #     name_subs = text.replace('cuantos suscriptores tiene', '')
    #     data = urllib.request.urlopen(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={name_subs.strip()}&key={key}').read()
    #     subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    #     talk(name_subs + " tiene +{:,d}".format(int(subs)) + "suscriptores!")


# print('Nombre asistente: '+name)
# print('Texto: '+text)}# print(name in text)
#* Ejecutar funciones que ejecutan acciones a peticion
# try:
#     if(name in text):
#         try:
#             finish()
#             run()
#             search()
#             info()
#             send()
#             time()
#             disponibilidad()
#             who_i_am()
#         except NameError as err:
#             print("Entrada de audio inválida, intentalo nuevamente")
#             talk("Entrada de audio inválida, intentalo nuevamente")
#             print(err)
#         except KeyboardInterrupt:
#             print(err_template + 'Acción cancelada por el usuario.')
# except TypeError:
#     pass

#* NUEVO MODULO PARA EJECUCIÓN DE ACCIONES
try:
    run()
except NameError as err:
    print("Entrada de audio inválida, intentalo nuevamente")
    talk("Entrada de audio inválida, intentalo nuevamente")
    print(err)
except KeyboardInterrupt:
    print(err_template + 'Acción cancelada por el usuario.')


#! LINEA TEMPORAL
# run()

#* Ejecutar acción sin decir jarvis antes
# def justRun():
#     finish()
#     run()
#     search()
#     info()
#     send()
#     time()
#     disponibilidad()
#     who_i_am()

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