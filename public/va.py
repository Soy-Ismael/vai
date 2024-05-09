#* Comprobar conectividad del usuario
from transfer_data import Transaction # Módulo local para sustituir a config y readfile, ademas, añade nuevos métodos
import os # Módulo para administrar cosas afines al sistema operativo (rutas, cierre de programas, etc.)

# Instanciar clase Transaction
Data_transfer = Transaction()

if Data_transfer.check_internet_connection():
    print(Transaction().green_color+'Conexión a internet ✔️'+Transaction().normal_color)
    pass
else:
    print(Transaction().err_template+'Conección a internet ✖️'+Transaction().normal_color)
    os._exit()

# Importaciones 
import speech_recognition as sr # Módulo para reconocer audio y convertir a texto (STT)
import pyttsx3 # Módulo para convertir de texto a audio (TTS)
from dotenv import get_key # Módulo para cargar api-key en archivo .env
import datetime # Módulo para manejar la hora
import pywhatkit # Módulo para enviar mensajes de whatapp y abrir contenido en youtube (es un kit)
import random #Nuevo módulo para generar números aleatorios
import wikipedia #Nuevo modulo para resumir articulos de wikipedia
import winsound #Nuevo modulo para reproducir sonido, (no es necesario instalar con pip)
# import urllib.request #Nuevo modulo para conteo de suscriptores
import pyjokes # Módulo para chistes
import time # Módulo para temporizador - importado solo en caso de que se necesite
start_time = time.time()
import re # Módulo expresiones regulares
import asyncio # Módulo para ejecutar código asíncrono
from voice_synthesizer import synthesize_to_speaker # Módulo local creado para tts de microsoft (más voces y calidad que pyttsx3, no depende de voces en el ordenador, es necesario crear cuentan de microsoft azure y crear api key para servicios de voz)
# from days import getDaysAgo 
# import spoty # Módulo para reproducir contenido en spotify (no esta en uso actualmente)
# from sys import exit #Para trabajar con sys.exit() en caso de ser necesario
from banner import figlet_banner # Nuevo módulo local para imprimir banner de los desarrolladores
from report import create_report # Módulo para crear reportes de excel a partir de un archivo con formato definido
# from whisperBeta import main # Módulo para reconocer el audio mediante whisper, recibe como parametro el modelo que va a utilizar para reconocer el audio (tiny, base, medium, large), el valor por defecto es base
#* Open AI - Chat Gpt
from openai import OpenAI # Módulo para inteligencia artificial
from whisperBeta import main # Módulo para reconocer el audio mediante whisper, recibe como parametro el modelo que va a utilizar para reconocer el audio (tiny, base, medium, large), el valor por defecto es base
# from audio import tts
# Google - Gemini
# import pathlib
# import textwrap

# def to_markdown(text):
#     text = text.replace('•', '  *')
#     return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#* Default const
# name = 'jarvis' # Nombre por el que se llamara al asistente (para desarrollar más tarde)
# lang = 'es-ES'
# time_format = "%I:%M:%p"
# wiki_lang = 'es'

#* Default const - open AI mode#
#  assistant_role: "Eres un asistente virtual que habla en verso y responde de manera cortez."
# prompt = "Dime de manera detallada como puedo crear una función en python."

#* Color templates
green_color = Data_transfer.green_color
cian_color = Data_transfer.cian_color
blue_color = Data_transfer.blue_color
yellow_color = Data_transfer.yellow_color
red_color = Data_transfer.red_color
negrita = Data_transfer.negrita
subrayado = Data_transfer.subrayado
normal_color = Data_transfer.normal_color

#* text templates
user_template = f"{negrita}Usuario: {normal_color}"
# va_template = f"{negrita}{name}: {normal_color}" #Declarada más abajo
err_template = f"{red_color}{negrita}ERROR: {normal_color}"
warning_template = f"{yellow_color}{negrita}ADVERTENCIA: {normal_color}"

#* De texto a voz - Modulo 6
engine = pyttsx3.init()

try:
    voice_id = 0
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
except IndexError:
    print(f"No existe la voz con el ID {voice_id}, asegurese de tener ingles, español de españa y español de mexico instalado en su windows")
    print(f"{err_template}en configuración de idiomas")

    for voice in voices:
        print(f'{yellow_color} = = = = = = = =  = = = = = = {normal_color}')
        print(f'ID:{cian_color} {voice.id} {normal_color}')
        print(f'Name:{cian_color} {voice.name} {normal_color}')
    os._exit()

#* Función para hablar, recibe el texto a reproducir como parametro
def talk(text):
    # engine.say(text)
    # engine.runAndWait()
    synthesize_to_speaker(text, 'es-MX-DaliaNeural')

#* Función para detener el habla en caso de ser necesario
def no_talk():
    engine.stop()
# talk("Hola, ¿como estas?")


#* De voz a texto - Modulo 1 & 2
rec = sr.Recognizer()

def listen():
    try:
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

                winsound.PlaySound('sounds/sonido_cierre.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                print(user_template + text)

                if name in text:
                    text = text.replace(name, '')
                    status = True

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
figlet_banner()

try:
    #* Función para cargar los datos de archivo de configuración en las variables de asistente
    def load_data(data_to_extract):
        global name, lang, wiki_lang, time_format, voice

        name, lang, time_format, voice = data_to_extract
        wiki_lang = lang[slice(0,2)]

    #* Ejecutar función que lee archivo de configuración
    data = Data_transfer.readfile()
    if type(data) != dict or not Data_transfer.check_file_integrity():
        print(err_template+'Datos de configuración corruptos o inexistentes')
        talk('Error en datos de configuración, por favor restablezca el archivo.')
        Data_transfer.initial_config()

        data = Data_transfer.readfile()
        load_data(data.values())
    else:
        load_data(data.values())
except KeyboardInterrupt:
    print(f'\n{warning_template}Acción cancelada por el usuario.')


#* Función para crear archivo de configuración (config.txt) mediante la voz (no se usa aun)
def init_configuration():
    try:
        response:str = listen()

        if('sí' in response or 'si' in response):
            print('Entro en si en respuesta')
            Data_transfer.create_config_file()
            Data_transfer.initial_config()

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

#* Templates 2 - variable faltante, es necesario colocarla aquí luego de que se tiene el valor de "name"
va_template = f"{negrita}{name}: {normal_color}"

#* Inteligencia Artificial
def run_gpt(prompt:str):
    try:
        client = OpenAI(
            api_key=get_key('public/.env',"OPENAI_API_KEY"),
        )

        response = client.chat.completions.create(
            # model="gpt-3.5-turbo-0125",
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente virtual que responde de manera cortez y esta dispuesto a ayudar a los usuarios con cada petición de manera objetiva y precisa."},
                {"role": "user", "content": prompt}
                # "role": "user", "content": prompt,
            ]
        )
        return response.choices[0].message.content
    except Exception as err:
        print(err_template+str(err))


#* Módulo 4 - realización de acciones según palabras claves de activación
def run(text:str = '', status=True):
    if text == '':
        text = listen()
    else:
        text = {'text':text, 'status':status}

    if 'reproduce' in text['text']:
        if 'spotify' in text['text']:
            music = text['text'].replace('reproduce', '')
            music = music.replace(name, '')
            music = music.replace('spotify', '')
            talk('Reproduciendo ' + music)
            spoty.play(keys["spoty_client_id"], keys["spoty_client_secret"], music)
        else:
            music = text['text'].replace('reproduce', '')
            music = music.replace(name, '')
            pywhatkit.playonyt(music)
            print(va_template + 'Reproduciendo' + music)
            # print(f'{negrita}{name}: {normal_color}Reproduciendo ' + music)
            talk('Reproduciendo ' + music)
        return {'text' : text['text'], 'status' : True}

    elif 'busca' in text['text']:
        busqueda = text['text'].replace('busca', '')
        # print('Texto con nombre omitido: ' + text)
        talk('Buscando ' + busqueda)
        pywhatkit.search(busqueda)
        # Esta funcion busca en el motor de busqueda google.com, valga la redundancia
        print(f"{va_template}Buscando {busqueda}")
        return {'text' : text['text'], 'status' : True}

    elif 'información sobre' in text['text'] and 'ingles' in text['text']:

        info = text['text'].replace('información sobre', '')
        info = text['text'].replace('en', '')
        info = text['text'].replace('dame', '')
        info = text['text'].replace('dime', '')
        info = text['text'].replace('ofreceme', '')
        info = text['text'].replace('ofréceme', '')

        talk('Resumiendo informacion sobre ' + info + ' en wikipedia')
        talk(pywhatkit.info(info))
        print(f"{va_template}resumiendo {info} en wikipedia en ingles")
        return {'text' : text['text'], 'status' : True}
    
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
        return {'text' : text['text'], 'status' : True}
    
    elif 'recuérdame' in text['text']:
        import time
        tarea_inicio = text['text'].find("Recuérdame") + len("Recuérdame")
        match = re.search(r'\b(en|después de)\b', text['text'])
        if match:
            tarea_fin = match.start()            
            tarea = text['text'][tarea_inicio:tarea_fin].strip()
            tiempo_inicio = match.end()
            tiempo_texto = text['text'][tiempo_inicio:].strip().split()[0]
            comando = int(tiempo_texto)
            if "segundo" or "segundos" in tiempo_texto:
                comando = comando
            elif "minuto" or "minutos" in tiempo_texto:
                comando = comando * 60
            elif "hora" or "horas" in tiempo_texto:
                comando = comando * 3600
            elif "día" or "días" in tiempo_texto:
                comando = comando * 86400
            talk(f"¡Tarea programada! Te recordaré que debes {tarea} en el tiempo estimado")
            time.sleep(comando)
            print(f"Recuerda que {tarea}")
            talk(f"Recuerda que {tarea}")
        else:
            talk("No se encontró la unidad de tiempo. Por favor intente de nuevo")
        # return True
        return {'text' : text['text'], 'status' : True}


    elif 'chiste' in text['text']:
        chiste = pyjokes.get_joke(wiki_lang)
        print(va_template + chiste)
        talk(chiste)
        winsound.PlaySound('sounds/redoble_de_tambores.wav', winsound.SND_FILENAME)
        return {'text' : text['text'], 'status' : True}


    elif 'realiza' in text['text'] and 'reporte' in text['text']:
        print('Creando reporte')
        talk('Creando reporte')
        create_report()
        return {'text' : text['text'], 'status' : True}



    elif 'envía' in text['text']:
        text = text['text'].replace('envía', '')
        hora_actual = datetime.datetime.now()
        nueva_hora = hora_actual + datetime.timedelta(minutes=1)
        import pywhatkit as kit
        import speech_recognition as sr
        
        try:
            msg, contact = text.split(' a ')

            contact = Data_transfer.read_phone_numbers(contact)
            def transcribir_audio():
                recognizer = sr.Recognizer()
                with sr.Microphone() as source:
                    talk(f"Di el mensaje que deseas enviar por WhatsApp:")
                    recognizer.adjust_for_ambient_noise(source)  
                    audio = recognizer.listen(source)
            talk(f"El mensaje se enviara en unos segundos")
            kit.sendwhatmsg_instantly("Ismael", msg)
            contact = "Ismael"
            talk(f"Mensaje enviado al número seleccionado")
            print(va_template + "Mensaje enviado al número seleccionado")
        except:
            print(err_template + "en el envío de mensaje, por favor, vuelve a intentarlo.")
            talk("Error en el envío de mensaje, por favor, vuelve a intentarlo.")
        # pywhatkit.sendwhatmsg("numero con prefijo","mensaje", 23,57)
        return {'text' : text['text'], 'status' : True}


    elif 'qué hora es' in text['text']:
        time = datetime.datetime.now().strftime(time_format[slice(0,5)])
        time_es = datetime.datetime.now().strftime(time_format)

        if(time.startswith('0')):
            time = time[slice(1,(time.__len__()+1))]
            time_es = time_es[slice(1,(time.__len__()+1))]

        changeShape = random.randint(0,2)

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
        return {'text' : text['text'], 'status' : True}


    elif 'temporizador' in text['text'] :
        import time
        wait = 0
        _, timer = text['text'].split('de')

        hour = re.findall(r"\d+\s*[h]{1,5}",timer)
        minute = re.findall(r"\d+\s*[m]{1,7}",timer)
        seconds = re.findall(r"\d+\s*[s]{1,8}",timer)

        hour = int(hour[0].replace('h','')) if len(hour) > 0 else 0
        minute = int(minute[0].replace('m','')) if len(minute) > 0 else 0
        seconds = int(seconds[0].replace('s','')) if len(seconds) > 0 else 0

        wait = (hour*3600) + (minute*60) + seconds

        print(f'Temporizador fijado para {wait} segundos...')
        talk(f'Temporizador fijado para {wait} segundos...')
        
        async def async_sleep(time_to_wait:int) -> None:
            await asyncio.sleep(time_to_wait)

            print(f'Terminado!')
            talk(f'Terminado!')

            for i in range(2):
                winsound.PlaySound('sounds/redoble_de_tambores.wav', winsound.SND_FILENAME)
        
        print('Antes de invocación de funcion asíncrona')        
        asyncio.run(async_sleep(wait))
        print('despues de invocación de funcion asíncrona')        
        return {'text' : text['text'], 'status' : True}

    
    elif 'que dia fue' in text['text'] or 'qué día fue' in text['text']:
        date = getDaysAgo(text['text'])
        print(date)
        talk(date)
        return {'text' : text['text'], 'status' : True}

    elif 'estás ahí' in text['text']:
        print(True)
        print(va_template + 'Sí, ¿En qué te puedo ayudar?')
        talk('Sí, ¿En qué te puedo ayudar?')
        text = name + ' ' + listen()
        return {'text' : text['text'], 'status' : True}


    elif 'cómo te llamas' in text['text']:
        print(name)
        talk('Soy' + name + '¿Cómo te puedo ayudar?')
        return {'text' : text['text'], 'status' : True}

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
        return {'text' : text['text'], 'status' : True}
        
    
    elif 'crea una nueva configuración' in text['text'] :
        talk('Creando archivo de configuración nuevamente')
        Data_transfer.initial_config()
        load_data(Data_transfer.readfile().values())
        return {'text' : text['text'], 'status' : True}


    elif 'hasta luego' in text['text']:
        talk(f'Hasta pronto')
        os._exit(0)
        return {'text' : text['text'], 'status' : True}

    return {'text' : text['text'], 'status' : False}


#* EJECUCIÓN DE ACCIONES - con control de excepciones
try:
    import time
    #* Escuchar una vez
    # result = run('Porque le decimos pantalones a los pantalones?')

    # if not result['status']:
    #     ia = run_gpt(result['text'])
    #     print(va_template + str(ia))
    #     talk(ia)

    #* Mantenerse escuchando
    while True:
        result = run()

        if not result['status']:
            ia = run_gpt(result['text'])
            print(va_template + str(ia))
            talk(ia)
            time.sleep(2) # Tiempo de espera antes de volver a estar disponible para escuchar

except KeyboardInterrupt:
    no_talk()
    print(err_template + 'Acción cancelada por el usuario.')
except NameError as err:
    print(err)
    print("Entrada de audio inválida, intentalo nuevamente")
    talk("Entrada de audio inválida, intentalo nuevamente")
except TypeError as err:
    print(err)
    talk("Entrada de audio inválida, intentalo nuevamente")
    print("Entrada de audio inválida, intentalo nuevamente")


print(f'{Transaction().yellow_color}PROGRAMA FINALIZADO CON UNA DURACIÓN DE:{Transaction().bright_cyan_color}{Transaction().negrita} {int(time.time() - start_time)} segundos {Transaction().normal_color}')