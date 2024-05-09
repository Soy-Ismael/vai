import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from dotenv import get_key
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

# función para sintetizar el texto y convertirlo a voz, recibe como parametros: el texto a sintetizar, el idioma y acento con el que va a hablar, el idioma que va a reconocer, la clave api de azure y la región de esa clave api, (tiene valores por defecto cada parametro para una ejecución más limpia de la función)

def synthesize_to_speaker(text:str='Hola mundo', voice:str='es-MX-DaliaNeural', recognition_language:str='es-MX', azure_api_key:str=get_key('public/.env',"AZURE_API_KEY"), region:str='eastus'):
    speech_config = speechsdk.SpeechConfig(subscription=azure_api_key, region=region,speech_recognition_language = recognition_language)
    audio_config = AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_language = voice[0:5]
    speech_config.speech_synthesis_voice_name = voice
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    synthesizer.speak_text(text)

if __name__ == "__main__":
    #* Ejemplo de uso
    # synthesize_to_speaker("Hola, ¿como estas? Esta es la voz del sintetizador de Microsoft", azure_api_key='<API_KEY>', region='<API_KEY_REGION>')

    # talk(text='Uy parce, ¡dígame cómo puedo ayudarle el día de hoy pues!')
    # synthesize_to_speaker(text="Hola, ¿como estas? Esta es la voz del sintetizador de Microsoft")
    pass
