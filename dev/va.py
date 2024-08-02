# Dato curioso a fecha de hoy 5/marzo/2024 3:27 hora dominicana hay un total de 529 lineas de código en va.py, hay 265 lineas de código y otras 264 de cómentarios aproximadamente (los espacios en blanco se contaron como lineas de código).
# ESTRUCTURA Y REPARTICION DE TRABAJO DEL ASISTENTE
# *     Jared y Jairon
#todo 1 - Grabar voz del usuario 🎤 ✔️
#todo 2 - Convertir lo que dijo en texto 🖋 ✔️
# 
# *     Xaviel e Ismael
#todo 3 - Procesar la intención del usuario ❓ (modelo de IA) ✔️
#todo 4 - Ejecutar la acción deseada 👨‍🏭 ✔️
#
# ?      Proximamente
#todo 5 - Preparar respuesta (en texto) 💬 ✔️
#todo 6 - Convertir en audio y reproducir 🦻 ✔️

#* Comprobar conectividad del usuario
from transfer_data import Transaction # Módulo local para sustituir a config y readfile, ademas, añade nuevos métodos
import os # Módulo para administrar cosas afines al sistema operativo (rutas, cierre de programas, etc.)
import sys

# Instanciar clase Transaction
Data_transfer = Transaction()

if Data_transfer.check_internet_connection():
    print(Data_transfer.green_color+'Conexión a internet ✔️'+Data_transfer.normal_color)
    # pass
else:
    print(Data_transfer.err_template+'No hay conexión a internet ✖️'+Data_transfer.normal_color)
    sys.exit(0)

# Importaciones 
import speech_recognition as sr # Módulo para reconocer audio y convertir a texto (STT)
import pyttsx3 # Módulo para convertir de texto a audio (TTS)
from dotenv import get_key # Módulo para cargar api-key en archivo .env
import datetime # Módulo para manejar la hora
import pywhatkit # Módulo para enviar mensajes de whatapp y abrir contenido en youtube (es un kit)
import random #Nuevo módulo para generar números aleatorios
import wikipedia #Nuevo modulo para resumir articulos de wikipedia
# import winsound #Nuevo modulo para reproducir sonido, (no es necesario instalar con pip - solo funciona con windows)
from playsound import playsound #Nuevo modulo para reproducir sonido, (funciona en todos los sistemas operativos y reproduce .mp3, .ogg, .wav)
# import urllib.request #Nuevo modulo para conteo de suscriptores
import pyjokes # Módulo para chistes
import time # Módulo para temporizador - importado solo en caso de que se necesite
start_time = time.time()
# import re # Módulo expresiones regulares - se importa cuando se necesita
import asyncio # Módulo para ejecutar código asíncrono
from voice_synthesizer import synthesize_to_speaker # Módulo local creado para tts de microsoft (más voces y calidad que pyttsx3, no depende de voces en el ordenador, es necesario crear cuentan de microsoft azure y crear api key para servicios de voz)
from days import getDaysAgo 
# import spoty # Módulo para reproducir contenido en spotify (no esta en uso actualmente)
# from sys import exit #Para trabajar con sys.exit() en caso de ser necesario
# from banner import figlet_banner # Nuevo módulo local para imprimir banner de los desarrolladores
from report import create_report # Módulo para crear reportes de excel a partir de un archivo con formato definido
# from whisperBeta import main # Módulo para reconocer el audio mediante whisper, recibe como parametro el modelo que va a utilizar para reconocer el audio (tiny, base, medium, large), el valor por defecto es base
#* Open AI - Chat Gpt
from openai import OpenAI # Módulo para inteligencia artificial
# from audio import tts
# Google - Gemini
# import pathlib
# import textwrap

config = Data_transfer.read_config_file()

# global name, lang, wiki_lang, time_format, voice

name = config['assistant']['name']
lang = config['assistant']['language']
time_format = config['assistant']['hourFormat']
voice = config['assistant']['voiceNumber']
wiki_lang = lang[slice(0,2)]
role = config['assistant']['role']
printBanner = config['modules']['printBanner']
voiceEngine = config['env']['voiceEngine']

# print('Nombre: ' + name)
# print('Idioma: ' + lang)
# print('Formato de hora: ' + time_format)
# print('Indice de voz: ' + voice)
# print('Idioma de wikipedia: ' + wiki_lang)

#* text templates
user_template = f"{Data_transfer.negrita}Usuario: {Data_transfer.normal_color}"
va_template = f"{Data_transfer.negrita}{name}: {Data_transfer.normal_color}" #Declarada más abajo
err_template = f"{Data_transfer.red_color}{Data_transfer.negrita}ERROR: {Data_transfer.normal_color}"
warning_template = f"{Data_transfer.yellow_color}{Data_transfer.negrita}ADVERTENCIA: {Data_transfer.normal_color}"

#* De texto a voz - Modulo 6
engine = pyttsx3.init()
try:
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[int(voice)].id)
except IndexError:
    print(f"No existe la voz con el ID {voice}")
    print(f"{err_template}en configuración de idiomas")

    for voice in voices:
        print(f'{Data_transfer.yellow_color} = = = = = = = =  = = = = = = {Data_transfer.normal_color}')
        print(f'ID:{Data_transfer.cian_color} {voice.id} {Data_transfer.normal_color}')
        print(f'Name:{Data_transfer.cian_color} {voice.name} {Data_transfer.normal_color}')
        # print(f'Languages:{Data_transfer.cian_color} {voice.languages} {Data_transfer.normal_color}')
        # print(f'Age:{Data_transfer.cian_color} {voice.age} {Data_transfer.normal_color}')
        # print(f'Gender:{Data_transfer.cian_color} {voice.gender} {Data_transfer.normal_color}')

    #! No utilizar el exit() para programas reales, lo mejor seria utilizar el sys.exit()
    # os._exit(0)
    # exit()
    sys.exit(0)
# for voice in voices:
#     print(voice)

# figlet_banner(text='USAR API CON PRUDENCIA', banner_index=5)
if printBanner:
    from banner import figlet_banner
    figlet_banner(banner_index=5)


#* Función para hablar, recibe el texto a reproducir como parametro
def talk(text):
    if voiceEngine == 'azure':
        synthesize_to_speaker(text, 'es-MX-DaliaNeural', 'es-MX', config['env']['azureApiKey'])
    else:
        engine.say(text)
        engine.runAndWait()

#* Función para detener el habla en caso de ser necesario
# def no_talk():
#     engine.stop()


#* De voz a texto - Modulo 1 & 2
rec = sr.Recognizer()

# Ajuste del umbral de audio (En términos simples, si la energía (volumen) de la señal de audio es mayor que el umbral, el sistema considera que está recibiendo voz. Si la energía es menor que el umbral, el sistema considera que no hay voz y que cualquier sonido que esté recibiendo es simplemente ruido)

# 2300 tiene problemas para entender
# rec.energy_threshold = 2900
#* Función para escuchar la petición del usuario, se puede invocar durante la ejecución del programa, lo que permite que el asistente pueda volver a escuchar en cualquier punto del programa con solo invocar la función
def listen():
    # Acceder al microfono del dispositivo
    try:
        with sr.Microphone() as source:
            try:
                text = ''
                status = False

                print(f"{Data_transfer.green_color}Escuchando... {Data_transfer.normal_color}")

                # winsound.PlaySound('sounds/sonido_apertura.wav', winsound.SND_FILENAME)
                # playsound('sounds/sonido_apertura.wav')
                # os.system("aplay sounds/sonido_apertura.wav")
                # rec.adjust_for_ambient_noise(source,duration=1) #Ajustar para ruido de fondo, toma una muestra de 1 segundo para el ruido de fondo
                audio = rec.listen(source)

                #? Linea alternativa si el asistente escucha indefinidamente
                # audio = rec.listen(source, timeout = 2, phrase_time_limit = 4)

                print(f"{Data_transfer.blue_color}Analizando... {Data_transfer.normal_color}")
                text = rec.recognize_google(audio, language = lang).lower()
                # print("Texto: " + text)

                # winsound.PlaySound('sounds/sonido_cierre.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                # playsound('sounds/sonido_cierre.wav')
                # os.system("aplay sounds/sonido_cierre.wav")
                print(user_template + text)

                if name in text:
                    text = text.replace(name, '')
                    # print('Texto con nombre omitido: ' + text)
                    status = True

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
            playsound('sounds/sonido_cierre.wav')
            # os.system("aplay sounds/Sonido_Cierre.wav")

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


#* Ejecutar la función para escuchar al usuario y almacenar resultado en variable text para su futura evaluación
# text = listen() - Ahora se ejecuta dentro de la función run, de modo que run se hace más autosuficiente
# text = {'text' : 'envía Hola ¿cómo estas? a raylin', 'status': True}

#* PARTE DE Ismael Y Xaviel - con open AI - módulo 3
# *INICIO CHAT GPT - Modulo 3, 4 & 5
def run_gpt(prompt:str):
    try:
        client = OpenAI(
            api_key=get_key('dev/.env',"OPENAI_API_KEY"),
            # api_key=config['env']['openaiApiKey']
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", 
                # Manera original
                # "content": f"Eres un asistente virtual llamado {name} que habla en verso y responde de manera cortez, clara y objetiva, es decir, resumes la información solicitada por el usuario."},
                # Manera con archivo de configuración (los f-string deberian seguir funcionando)
                "content": f"{role}"},
                {"role": "user", 
                "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as err:
        print(err_template+str(err))
# *FINAL CHAT GPT

#* Enviar mensajes de whatapp
# pywhatkit sirve para enviar mensajes de WhatsApp: Utilice la función pywhatkit.sendwhatmsg() para enviar mensajes de WhatsApp a cualquier número de WhatsApp en un momento determinado. La sintaxis es la siguiente: pywhatkit.sendwhatmsg("número de móvil del receptor", "mensaje", horas, minutos). Asegúrese de que el número de móvil del receptor esté en formato de cadena y el código del país se mencione antes del número de móvil. Las horas siguen el formato de 24 horas. Los minutos son los minutos de la hora programada para el mensaje (00-59). Por ejemplo, para enviar un mensaje a un número de WhatsApp a las 22:28, utilice la siguiente sintaxis: pywhatkit.sendwhatmsg("+91xxxxxxxxxx", "Hola desde Python", 22, 28)

#* Módulo 4 - realización de acciones según palabras claves de activación
def run(text:str = '', status=True):
    if text == '':
        text = listen()
        if text['status'] == False:
            # print('no hay nombre de asistente')
            return {'text':text, 'status':status}
    else:
        text = {'text':text, 'status':status}

    # text = {'text': 'Hola, ¿cómo estás?'}

    # Utilizamos match para evaluar el texto
    match text['text']:
        case _ if 'reproduce' in text['text'] and config['modules']['playYtContent']:
            # print('REPRODUCE')
            music = text['text'].replace('reproduce', '')
            music = music.replace(name, '')
            pywhatkit.playonyt(music)
            print(va_template + 'Reproduciendo' + music)
            # print(f'{Data_transfer.negrita}{name}: {Data_transfer.normal_color}Reproduciendo ' + music)
            talk('Reproduciendo ' + music)
            return {'text' : text['text'], 'status' : True}
        case _ if 'busca' in text['text'] and config['modules']['searchInWeb']:
            busqueda = text['text'].replace('busca', '')
            # print('Texto con nombre omitido: ' + text)
            talk('Buscando ' + busqueda)
            pywhatkit.search(busqueda)
            # Esta funcion busca en el motor de busqueda google.com, valga la redundancia
            print(f"{va_template}Buscando {busqueda}")
            return {'text' : text['text'], 'status' : True}
        case _ if 'información sobre' in text['text'] and config['modules']['infoInWeb']:
            # print('INFORMACION SOBRE')
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
        case _ if 'recuérdame' in text['text'] and config['modules']['reminders']:
            import time
            import re

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
        case _ if 'chiste' in text['text'] and config['modules']['jokes']:
            chiste = pyjokes.get_joke(wiki_lang)
            print(va_template + chiste)
            talk(chiste)
            # tts(chiste)
            # windound no soporta formato mp3
            playsound('sounds/redoble_de_tambores.wav')
            # os.system("aplay sounds/redoble_de_tambores.wav")
            return {'text' : text['text'], 'status' : True}
        case _ if 'realiza' in text['text'] and 'reporte' in text['text'] and config['modules']['excelReport']:
            print('Creando reporte')
            talk('Creando reporte')
            create_report()
            return {'text' : text['text'], 'status' : True}
        case _ if 'qué hora es' in text['text'] and config['modules']['sayHour']:
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
        case _ if 'temporizador' in text['text'] and config['modules']['timer']:
            import time
            import re

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
                    # winsound.PlaySound('sounds/redoble_de_tambores.wav', winsound.SND_FILENAME)
                    playsound('sounds/redoble_de_tambores.wav')
            
            print('Antes de invocación de funcion asíncrona')        
            asyncio.run(async_sleep(wait))
            print('despues de invocación de funcion asíncrona')        
            return {'text' : text['text'], 'status' : True}
        case _ if ('que dia fue' in text['text'] or 'qué día fue' in text['text']) and config['modules']['whatDayWas']:
            # print('QUE DIA FUE')
            date = getDaysAgo(text['text'])
            print(date)
            talk(date)
            return {'text' : text['text'], 'status' : True}
        case _ if 'estás ahí' in text['text'] and config['modules']['checkAvailability']:
            print(va_template + 'Sí, ¿En qué te puedo ayudar?')
            talk('Sí, ¿En qué te puedo ayudar?')
            text = name + ' ' + listen()
            return {'text' : text['text'], 'status' : True}
        case _ if 'cómo te llamas' in text['text'] and config['modules']['sayName']:
            print(name)
            talk('Soy' + name + '¿Cómo te puedo ayudar?')
            # text = listen()
            return {'text' : text['text'], 'status' : True}
        case _ if ('muéstrame el archivo de configuración' in text['text'] or 'muestrame el archivo de configuración' in text['text']) and config['modules']['requestConfigFile']:
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
        case _ if 'hasta luego' in text['text'] and config['modules']['closingPhrase']:
            talk(f'Hasta pronto')
            sys.exit(0)
            return {'text' : text['text'], 'status' : True}
            # Aquí deberia ir un código para poner el asistente en modo de siempre escucha y contestar si se menciona el nombre del asistente
        case _ if 'enciende' in text['text'] and config['modules']['wakeOnLan']:
            from wakeonlan import send_magic_packet
            machine = text['text'].replace('enciende ', '').replace('la ', '').replace('ps', 'pc').replace('computadora ', 'pc').replace('de ', '')

            # class MacNotFoundError(Exception):
            #     # """Excepción personalizada para indicar que no se encontró la dirección MAC."""
            #     pass

            # Enviar un paquete mágico a una dirección MAC específica
            # send_magic_packet('00:11:22:33:44:55')
            # send_magic_packet('00:11:22:33:44:55', '66:77:88:99:AA:BB')
            # send_magic_packet('00:11:22:33:44:55', ip_address='192.168.1.255', port=7)
            try:
                if 'todas' in machine:
                    for pc, details in config['wakeonlan']['mac'].items():
                        if details['mac'] != "":
                            send_magic_packet(details['mac'])
                else:
                    if machine.split()[1].isdigit():
                        machine = machine.split()[0]+str(machine.split()[1])
                        # machine = machine.replace(' ', '')
                        send_magic_packet(config['wakeonlan']['mac'][machine]['mac'])
                        # print(machine)
                    else:
                        # tres, dos, veinte o un nombre "juan, pedro, asiento"
                        index = Data_transfer.letras_a_numero(machine.split()[1])
                        # Para el caso particular de interes, si index es False entonces se trata de un nombre
                        if index == False:
                            # raise MacNotFoundError(f"No se encontró la dirección MAC para {machine.strip()}.")
                            for pc, details in config['wakeonlan']['mac'].items():
                                if details['name'] == machine.split()[1] and details['mac'] != "":
                                    print(machine)
                                    send_magic_packet(details['mac'])
                        else:
                            machine = machine.split()[0]+str(index)
                            # print(config['wakeonlan']['mac'][machine]['mac'])
                            # print(machine)
                            # Lo envia por el nombre de index y no por el nombre de equipo
                            send_magic_packet(config['wakeonlan']['mac'][machine]['mac'])

                    # print('Mac: ' + Data_transfer.read_config_file_line(machine, txt_path+'/wol.txt'))
                    # send_magic_packet(Data_transfer.read_config_file_line(machine, txt_path+'/wol.txt'))
                print(va_template + "Echo ✅")
                talk('Listo')
            except ValueError as err:
                print(f"{err_template}{err}")
            except MacNotFoundError as err:
                print(err_template + str(err))
                talk(str(err))
        case _:
            return {'text' : text['text'], 'status' : False}

#* EJECUCIÓN DE ACCIONES - con control de excepciones
try:
    #* Implementando funcionalidad para que el asistente se mantenga escuchando
    # run('texto de prueba escrito')
    # muéstrame el archivo de configuración' in text['text'] or 'muestrame el archivo de configuración
    run('Que dia es hoy')
    # run()

    # while True:
    #     # result = run('Que dia es hoy')

    #     if not result['status'] and config['modules']['aiModule']:
    #         ia = run_gpt(result['text'])
    #         print(va_template + str(ia))
    #         talk(ia)
    #     else:
    #         print('Acción no programada')
    #         talk('Temo que lo que has pedido excede mis capacidades')

except KeyboardInterrupt:
    # no_talk()
    print(err_template + 'Acción cancelada por el usuario.')
except NameError as err:
    print(err)
    # print("Entrada de audio inválida, intentalo nuevamente")
    # talk("Entrada de audio inválida, intentalo nuevamente")
    pass
except TypeError as err:
    print(err)
    # talk("Entrada de audio inválida, intentalo nuevamente")
    # print("Entrada de audio inválida, intentalo nuevamente")
    pass


if config['modules']['countExecutionTime']:
    print(f'{Data_transfer.yellow_color}PROGRAMA FINALIZADO CON UNA DURACIÓN DE:{Data_transfer.bright_cyan_color}{Data_transfer.negrita} {int(time.time() - start_time)} segundos {Data_transfer.normal_color}')