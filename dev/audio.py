# Archivo para probar distintos motores de texto a voz (en este caso el modulo gratuito de python pyttsx3 y el de openAI Whisper)

from pathlib import Path
from openai import OpenAI
import pyttsx3
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

def openaitalk():
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    # input="Today is a wonderful day to build something people love!"
    input="Hola, como estas, espero que bien, si es así, me alegro de que lo estes"
    )
    response.stream_to_file(speech_file_path)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# for voice in voices:
#     print(voice)

def normaltalk(text):
    engine.say(text)
    engine.runAndWait()

normaltalk("Today is a wonderful day to build something people love!")
# openaitalk()