import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import tempfile
import os
import pyttsx3
import pywhatkit

temp_file = tempfile.mkdtemp()
save_path = 'dev/temp.wav'

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 145)
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            data = io.BytesIO(audio.get_wav_data())
            audio_clip = AudioSegment.from_file(data)
            audio_clip.export(save_path, format ='wav')
    except Exception as e:
        print('Error: ' + str(e))
    return save_path

def recognize_audio(save_path, model):
    audio_model = whisper.load_model(model)
    transcription = audio_model.transcribe(save_path, language='spanish', fp16=False)
    return transcription['text']

def main(model:str = 'base'):
        return recognize_audio(listen(), model)

    
if __name__ == "__main__":
    text_by_whisper = main()
    print(text_by_whisper)
    talk(text_by_whisper)
