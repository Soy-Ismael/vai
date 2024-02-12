@echo off
echo Automated Installer

title Instalando dependencias
pip install -r requirements.txt

title Terminado
msg * "Instalacion de dependencias completada con exito"