@echo off
echo Automated Installer

title Instalando dependencias
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

title Terminado
msg * "Instalación de dependencias completada con éxito."