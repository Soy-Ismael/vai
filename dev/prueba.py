import speech_recognition as sr, os 
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI()
try:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente virtual que habla en prosa y responde de manera cortez."},
        {"role": "user", "content": "Dime de manera detallada como puedo crear una función en python."}
    ])
    print(completion.choices[0].message)
except Exception as err:
    print(err)