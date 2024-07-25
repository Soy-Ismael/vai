@echo off
echo Automated Installer

title Actualizando pip
color 8
python.exe -m pip install --upgrade pip
echo TERMINADO
cls

title Instalando SpeechRecognition
color 5
pip install SpeechRecognition
echo TERMINADO
cls

title Instalando PyAudio
color 6
pip install PyAudio
echo TERMINADO
cls

title Instalando dotenv
color d
pip install python-dotenv
echo TERMINADO
cls

title Instalando setuptools py-3.12
color b
python -m pip install setuptools
echo TERMINADO
cls

title Instalando distutils644 (opt)
color c
pip install distutils644
echo TERMINADO
cls

title Instalando OpenAI
color 2
pip install --upgrade openai
echo TERMINADO
cls

title Instalando pyttsx3
color 9
pip install pyttsx3
echo TERMINADO
cls

title Instalando pywhatkit
color a
pip install pywhatkit
echo TERMINADO
cls

title Instalando spoty
color 2
pip install spoty
echo TERMINADO
cls

title Instalando pyjokes
color 5
pip3 install pyjokes
echo TERMINADO
cls

title Instalando pyfiglet
color c
pip3 install pyfiglet
echo TERMINADO
cls

title Instalando azure_speech
color 7
pip install azure-cognitiveservices-speech
echo TERMINADO
cls

title Instalando pandas
color 3
pip install pandas
echo TERMINADO
cls

title Instalando openpyxl
color 2
pip install openpyxl
echo TERMINADO
cls

title pydub
color 4
pip install pydub
echo TERMINADO
cls

title wake on lan
color c
pip install wakeonlan
echo TERMINADO
cls

title Instalando playsound
python -m pip install --upgrade pip setuptools wheel
color b
pip install playsound
echo TERMINADO
cls

@REM title matplotlib
@REM color 4
@REM pip install matplotlib
@REM echo TERMINADO
@REM cls

@REM title reportlab
@REM color c
@REM pip install reportlab
@REM echo TERMINADO
@REM cls

@REM text-to-speech de openAI
@REM title Instalando pathlib
@REM color c
@REM pip install pathlib
@REM echo TERMINADO
@REM cls

@REM https://platform.openai.com/docs/guides/text-to-speech

title Terminado
msg * "Instalacion de dependencias completada con exito"

