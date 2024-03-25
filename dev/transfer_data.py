import re #Expresión regular
from socket import gethostbyname, create_connection, error
import pyttsx3

# Este fichero contendra una clase con todos los métodos y propiedades necesarios para la transferencia de informaciónes entre disitntos archivos, esto con el fin de tener un código más modularizado y limpio.

# Revisar archivo de notas.txt
import os
nombre_archivo = 'config.txt'

class Transaction:
    def __init__(self):
        self.white_color                = "\033[97m"
        self.negrita                    = "\033[1m"
        self.normal_color               = "\033[0m"
        self.blinking_text              = "\033[5m"
        self.cian_color                 = "\033[96m"
        self.bright_cyan_color          = "\033[96;1m"
        self.blue_color                 = "\033[94m"
        self.magenta_color              = "\033[95m"
        self.red_color                  = "\033[91m"
        self.yellow_color               = "\033[93m"
        self.bright_yellow_color        = "\033[93;1m"
        self.light_green_color          = "\033[92m"
        self.green_color                = "\033[92m"
        self.bright_blinking_yellow     = "\033[93;5m"
        self.bold_underlined_text       = "\033[1;4m"
        self.black_on_white_color       = "\033[97;40m"
        self.inverted_text              = "\033[7m"
        self.bold_white_background      = "\033[1;47m"
        self.bold_cyan_background       = "\033[1;46m"
        self.bold_blue_background       = "\033[1;44m"
        self.bold_magenta_background    = "\033[1;45m"
        self.bold_red_background        = "\033[1;41m"
        self.inverted_yellow_text       = "\033[7;93m"
        self.bold_yellow_background     = "\033[1;43m"
        self.bold_green_background      = "\033[1;42m"
        self.subrayado                  = "\033[4m"
        self.warning_template = f"{self.yellow_color}{self.negrita}ADVERTENCIA: {self.normal_color}"
        self.err_template = f"{self.red_color}{self.negrita}ERROR: {self.normal_color}"

    #* Función para probar que todos los códigos de color funcionan correctamente
    def test_colors(self):
        print(self.white_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.negrita + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.normal_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.blinking_text + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.cian_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bright_cyan_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.blue_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.magenta_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.red_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.yellow_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bright_yellow_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.light_green_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.green_color + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bright_blinking_yellow + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_underlined_text + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.black_on_white_color + ' Hola ¿Cómo esdIStás? ' + color.normal_color)
        print(self.inverted_text + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_white_background + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_cyan_background + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_blue_background + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_magenta_background + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_red_background + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.inverted_yellow_text + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_yellow_background + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.bold_green_background + ' Hola ¿Cómo estás? ' + color.normal_color)
        print(self.subrayado + ' Hola ¿Cómo estás? ' + color.normal_color)

    #* Función de config file optimizada para crear archivo de configuración
    def create_config_file(self):
        with open('dev\\'+nombre_archivo, 'w') as archivo:
            return True
        return False

    #* Rellenar archivo de configuración con datos ingresados por usuario
    def initial_config(self):
        try:
            text_plain_enter = '\n'
            print(self.black_on_white_color + 'Inicializando configuración...' + self.normal_color + '\n')

            name = input('Nombre del asistente: ')
            while(len(name) < 1):
                # print(f"{self.err_template} {self.red_color} {self.negrita}DATO INVALIDO. {self.normal_color}")
                print(f"{self.err_template} {self.red_color} {self.negrita}El nombre debe contener algún carácter.{self.normal_color}")
                name = input('Nombre del asistente: ')
            name = f"name: {name}"
                

            # lang = input('Idioma preferido (es-ES / en-US): ')
            #* Expresión regular para idioma
            def validate_lang(text_input:str):
                text_input.strip()
                regEx = re.search(r"^[a-z]{2}-[A-Z]{2}$", text_input)
                return regEx.group() if regEx else False

            lang = validate_lang(input('Idioma preferido (es-ES / en-US): '))
            while lang == False:
                lang = validate_lang(input('Idioma preferido (es-ES / en-US): '))

            lang = f"language: {lang}"

            #* User re.sub para remplazar en expresión regular para formato de hora
            def validate_hour(hour):
                if re.match(r"^12$", hour):
                    return "%H:%M %p"
                elif re.match(r"^24$", hour):
                    return "%H:%M %p"
                else:
                    return False

            hour_format = validate_hour(input('Formato de hora (12 / 24): ').strip().replace(' ', ''))
            while hour_format == False:
                print(self.warning_template+'Entrada invalida, intentalo nuevamente')
                hour_format = validate_hour(input('Formato de hora (12 / 24): ').strip().replace(' ', ''))

            hour_format = f"hour_format: {hour_format}"

            #* Seleccionar voz
            def validate_voice(index:int, max_lengh:int):
                return index if type(index) == int and index in range(max_lengh+1) else False


            try:
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                print(f"{self.yellow_color}Las voces disponibles son proporcionales a la cantidad de idiomas instalados{self.normal_color} {text_plain_enter}")

                index = 0
                for voice in voices:
                    voice_name = voice.name
                    voice_name = voice_name.replace('Microsoft', '')
                    voice_name = voice_name.replace('Desktop', '')
                    # ϟ ↦ ↯ ↪ ⇆ ⇢ ⇉ ⇨ ➜ ➠ ➸ ➵ ⤨ ⟼ ☠ ✘ ッ ヅ ツ 
                    print(f'{self.red_color} {self.negrita} ID: {self.green_color} {index}  {self.red_color} ヅ {self.normal_color}{self.cian_color}{voice_name} {self.normal_color}')
                    print(f'{self.yellow_color} - - - - - - - - - - - - {self.normal_color}')
                    index = index + 1

                print(f"{self.yellow_color}{self.negrita}= = Escoge una voz escribiendo su ID = ={self.normal_color} {text_plain_enter}")

                voice_number = validate_voice(int(input('Voz preferida (0, 1, 2...)(int): ')), len(voices))
                # is para comprobar que sea exactamente igual a False y que el '0' no se interprete como False
                while voice_number is False:
                    voice_number = validate_voice(int(input('Voz preferida (0, 1, 2...)(int): ')), len(voices))
                engine.setProperty('voice', voices[voice_number].id)

            except IndexError as err:
                print(f"{self.err_template} {err}")
                print(f"{self.warning_template}Aplicando configuración por defecto...")
                voice_number = 0
                engine.setProperty('voice', voices[voice_number].id)
            except ValueError as err:
                print(f"{self.err_template} {err}")
                print(f"{self.warning_template}Aplicando configuración por defecto...")
                voice_number = 0
                engine.setProperty('voice', voices[voice_number].id)

            voice = f"voice_number: {voice_number}"

            def summary():
                # print(f"{self.green_color}= = Configuración finalizada. = ={self.normal_color}")
                print(f"{self.green_color}{self.negrita}= = Resumen de configuración: = ={self.normal_color} {text_plain_enter}")

                print(f"{self.yellow_color} {name} {self.normal_color}")
                print(f"{self.yellow_color} {lang} {self.normal_color}")
                print(f"{self.yellow_color} {hour_format} {self.normal_color}")
                print(f"{self.yellow_color} {voice} {self.normal_color}")

            data_dictionary = [name+text_plain_enter, lang+text_plain_enter, hour_format+text_plain_enter, voice]

            def fill_file(data:dict):
                with open('dev\\'+nombre_archivo, 'w') as archivo:
                    archivo.writelines(data_dictionary)
                    return True

            return fill_file(data_dictionary)
        except KeyboardInterrupt:
            print(f'\n{self.warning_template}Acción cancelada por el usuario.')


    #* Comprobar si el archivo de configuración está correcto (comprueba si existe y si tiene todo el contenido)
    def check_file_integrity(self, ruta:str = 'dev\\'+nombre_archivo, lines:int = 3):
        if(os.path.isfile(ruta)):
            with open(ruta, 'r') as archivo:
                if(len(archivo.readlines()) <= lines):
                    return False
                else:
                    return True
        else:
            return False


    #* Leer archivo de configuración y devolver diccionario con los resultados obtenidos
    def readfile(self):
        try:
            with open('dev\\'+nombre_archivo, 'r') as archivo:
                data = {}

                for line in archivo:
                    line = line.replace("\n", '')
                    
                    key , value  = line.strip().split(': ')
                    data[key] = value

                if(len(data) <= 0):
                    return False
                else:
                    return data
        except ValueError:
            print(self.err_template+'en archivo de configuración')
        except Exception as e:
            print(self.err_template+f"Ocurrio un error al leer el archivo de configuración: {e}")
            return False


    #* Función para leer archivo de números telefonico
    def read_phone_numbers(self, name:str):
        #! ESTA FUNCIÓN NO CONTROLA ACENTOS HASTA AHORA.
        if(self.check_file_integrity('dev\\contacts.txt', 3)):
            with open('dev\\contacts.txt', 'r') as archivo:
                for line in archivo.readlines():
                    line = line.replace('\n', '')
                    name_in_db,number = line.replace(' ', '').split(':')                    

                    if name.lower() == name_in_db.lower():
                        return number
                return False
        else:
            return 'Archivo no encontrado'

    #* Función para revisar si el usuario tiene conección a internet (para ejecutar módulo de gpt) (Aun no esta lista la función)
    def check_internet_connection(self):
        try:
            gethostbyname("google.com")
            conexion = create_connection(("google.com", 80), 1)
            conexion.close()
            return True
            # return "Hay conexión a internet..."
        except error:
            return False
            # return "No hay conexión a internet..."
        


if __name__ == '__main__':
    transactions = Transaction()
    # color = Transaction()
    # color.test_colors()
    # transactions.initial_config()
    print(transactions.check_internet_connection())
    # transactions.check_internet_connection()
    
    # if(os.path.isfile('dev\\contacts.txt')):
    #     print('en ruta')
    #     with open('dev\\contacts.txt', 'r') as archivo:
    #         if(len(archivo.readlines()) <= 3):
    #             print(False)
    #         else:
    #             print(True)
    # else:
        # print(False)
    
    # number = transactions.read_phone_numbers('raylin')
    # print(number)

    # print(transactions.read_phone_numbers())