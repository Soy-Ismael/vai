import openai
import os
import winsound
import dotenv

# Initialize the OpenAI client
dotenv.load_dotenv()
client = openai.OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))
print(client.api_key)

# Set the audio file path
def listen():
    # Acceder al microfono del dispositivo
    try:
        # print(text)
        with sr.Microphone() as source:
            status = False

            print(f"{green_color}Escuchando... {normal_color}")

            winsound.PlaySound('sounds/sonido_apertura.wav', winsound.SND_FILENAME)
            # rec.adjust_for_ambient_noise(source,duration=1) #Ajustar para ruido de fondo, toma una muestra de 1 segundo para el ruido de fondo
            audio = rec.listen(source)
            print(f"{blue_color}Analizando... {normal_color}")

            winsound.PlaySound('sounds/sonido_cierre.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            return {'sound': audio, 'status': True}
            

    except KeyboardInterrupt:
        print('Acción cancelada por el usuario.')
    except TypeError:
        print('Variable aun sin datos')
    except sr.WaitTimeoutError:
        print('No se detecto entrada de audio.')
    except sr.UnknownValueError:
        print('Google Speech Recognition no pudo entender el audio.')
    except sr.RequestError as e:
        print(f"No se pudo solicitar resultados de Google Speech Recognition; {0}".format(e))
    except:
        print('No hay microfono seleccionado')
        winsound.PlaySound('sounds/Sonido_Cierre.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        return {'sound': None, 'status': False}

#! WHISPER - WHISPER
#! WHISPER
def whisper():
    audio_file_path = "dev/output-n.mp3"

    # Transcribe the audio
    response = client.audio.whisper.create(
        model="whisper-1",
        audio= audio_file_path
    )

    # print(listen()['sound'])

    # Print the transcribed text
    print(response.transcript)

#! TTS - TTS
#! TTS
def get_voices():
    print('alloy')
    print('echo')
    print('fable')
    print('onyx')
    print('nova')
    print('shimmer')

def tts(input_text:str = "Hola, esto es una prueba", voice:str = "nova", openai_model:str = 'tts-1'):
    # Generate the audio
    response = client.audio.speech.create(
        model=openai_model,
        voice=voice,
        input=input_text,
    )

    # Save the audio to a file
    response.stream_to_file("sounds/output.mp3")
    # winsound.PlaySound('dev\output.mp3', winsound.SND_FILENAME)
    # with open("dev/output.mp3", "wb") as f:
        # f.write(response.stream_to_file())

tts('Dos elefantes se balanceaban sobre la tela de una araña')
# winsound.PlaySound('sounds/output.mp3', winsound.SND_FILENAME)

# whisper() tiene problemas