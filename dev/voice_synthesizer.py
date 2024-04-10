import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from dotenv import get_key

# función para sintetizar el texto y convertirlo a voz, recibe como parametros: el texto a sintetizar, el idioma y acento con el que va a hablar, el idioma que va a reconocer, la clave api de azure y la región de esa clave api, (tiene valores por defecto cada parametro para una ejecución más limpia de la función)
def synthesize_to_speaker(text:str, voice:str='es-MX-DaliaNeural', speech_language:str='es-MX', recognition_language:str='es-MX', azure_api_key:str=get_key('AZURE_API_KEY'), region:str='northAmerica'):
    #Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
    # speech_config = speechsdk.SpeechConfig(subscription="<YOUR_ID_SUBSCRIPTION>", region="<YOUR_REGION>",speech_recognition_language="es-MX")
    speech_config = speechsdk.SpeechConfig(subscription=azure_api_key, region=region,speech_recognition_language = recognition_language)

    #Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
    audio_config = AudioOutputConfig(use_default_speaker=True)

    # Note: if only language is set, the default voice of that language is chosen.
    # speech_config.speech_synthesis_çlanguage = "es-MX"
    speech_config.speech_synthesis_language = speech_language

    # The voice setting will overwrite language setting.
    # The voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = "es-MX-DaliaNeural"
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    synthesizer.speak_text_async(text)

if __name__ == "__main__":
    synthesize_to_speaker("Hola, ¿como estas? Esta es la voz del sintetizador de Microsoft", azure_api_key='<API_KEY>', region='<API_KEY_REGION>')