@echo off
echo Automated Installer

title Instalando dependencias
pip install -r requirements.txt

title Terminado
msg * "Instalación de dependencias completada con éxito."