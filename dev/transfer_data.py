import re #Expresión regular

# Este fichero contendra una clase con todos los métodos y propiedades necesarios para la transferencia de informaciónes entre disitntos archivos, esto con el fin de tener un código más modularizado y limpio.

# Revisar archivo de notas.txt
import os

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

    def create_config_file(self):
        with open('dev\\'+nombre_archivo, 'w') as archivo:
            return True


    def initial_config(self):
        try:
            text_plain_enter = '\n'

            name = input('Nombre del asistente: ')
            while(len(name) < 1):
                print(f"{err_template} {red_color} {negrita}DATO INVALIDO. {normal_color}")
                print(f"{err_template} {red_color} {negrita}El nombre debe tener algún carácter.{normal_color}")
                name = input('Nombre del asistente: ')
                
            name = f"name: {name}"
            lang = input('Idioma preferido (es-ES / en-US): ')

            #* Expresión regular para idioma
            def request_lang(text_input):
                regEx = re.search(r"\w{2}-\w{2}", text_input)

                if regEx:
                    return regEx.group()
                else:
                    return False

            lang = False
            while lang == False:
                lang = request_lang(input('Idioma preferido (es-ES / en-US): '))
                
            # lang = request_lang(input('Idioma preferido (es-ES / en-US): '))

            while lang != 'es-ES':
                if lang == 'en-US':
                    break
                print(warning_template+'Entrada invalida, intentalo nuevamente')
                lang = input('Idioma preferido (es-ES / en-US): ')

            lang = f"language: {lang}"

            #* User re.sub para remplazar en expresión regular para formato de hora
            hour_format = int(input('Formato de hora (12 / 24): '))
            regEx = re.findall(r'\d{2,2}')
            while hour_format != 12:
                if hour_format == 24:
                    break
                print(warning_template+'Entrada invalida, intentalo nuevamente')
                hour_format = int(input('Formato de hora (12 / 24): '))

            if hour_format == 12:
                hour_format = "%I:%M %p"
            else:
                hour_format = "%H:%M %p"

            hour_format = f"hour_format: {hour_format}"

            #* Seleccionar voz
            engine = pyttsx3.init()
            try:
                voices = engine.getProperty('voices')
                print(f"{yellow_color}Las voces disponibles son proporcionales a la cantidad de idiomas instalados{normal_color} {text_plain_enter}")

                index = 0
                for voice in voices:
                    voice_name = voice.name
                    voice_name = voice_name.replace('Microsoft', '')
                    voice_name = voice_name.replace('Desktop', '')
                    # ϟ ↦ ↯ ↪ ⇆ ⇢ ⇉ ⇨ ➜ ➠ ➸ ➵ ⤨ ⟼ ☠ ✘ ッ ヅ ツ 
                    print(f'{red_color} {negrita} ID: {green_color} {index}  {red_color} ヅ {normal_color}{cian_color} {voice_name} {normal_color}')
                    print(f'{yellow_color} - - - - - - - - - - - - {normal_color}')
                    index = index + 1

                print(f"{yellow_color}{negrita}= = Escoge una voz escribiendo su ID = = {normal_color} {text_plain_enter}")
                voice_number = int(input('Voz preferida (0, 1, 2...)(int): '))

                while(voice_number < 0 or voice_number > len(voices)):
                    voice_number = 0
                    print(f"{err_template} {red_color} {negrita}DATO INVALIDO. {normal_color}")
                    voice_number = int(input('Voz preferida (0, 1, 2...): '))

                engine.setProperty('voice', voices[voice_number].id)
            except IndexError as err:
                print(f"{err_template} {err}")
                print(f"{warning_template}Aplicando configuración por defecto...")
                voice_number = 0
                engine.setProperty('voice', voices[voice_number].id)
            except ValueError as err:
                print(f"{err_template} {err}")
                print(f"{warning_template}Aplicando configuración por defecto...")
                voice_number = 0
                engine.setProperty('voice', voices[voice_number].id)

            voice = f"voice_number: {voice_number}"

            print(f"{green_color}= = Configuración finalizada. = ={normal_color}")
            print(f"{green_color}{negrita}= = Resumen de configuración: = ={normal_color} {text_plain_enter}")

            print(f"{yellow_color} {name} {normal_color}")
            print(f"{yellow_color} {lang} {normal_color}")
            print(f"{yellow_color} {hour_format} {normal_color}")
            print(f"{yellow_color} {voice} {normal_color}")

            data_dictionary = [name+text_plain_enter, lang+text_plain_enter, hour_format+text_plain_enter, voice]

            with open('dev\\'+nombre_archivo, 'w') as archivo:
                archivo.writelines(data_dictionary)
                return True
        except KeyboardInterrupt:
            print(f'\n{warning_template}Acción cancelada por el usuario.')



    def check_file_integrity(self, ruta:str = 'dev\\config.txt', lines:int = 3):
        if(os.path.isfile(ruta)):
            with open(ruta, 'r') as archivo:
                if(len(archivo.readlines()) <= lines):
                    return False
                else:
                    return True
        else:
            return False



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
            print(err_template+'en archivo de configuración')
        except Exception as e:
            print(err_template+f"Ocurrio un error al leer el archivo de configuración: {e}")
            return False



    def read_phone_numbers(self, name:str):
        #! ESTA FUNCIÓN NO CONTROLA ACENTOS HASTA AHORA.
        if(self.check_file_integrity('dev\\contacts.txt', 3)):
            # return 'Correcto'
            with open('dev\\contacts.txt', 'r') as archivo:

                # test,num = archivo.readline().strip().replace(' ', '').split(':')
                for line in archivo.readlines():
                    line = line.replace('\n', '')
                    
                    name_in_db,number = line.replace(' ', '').split(':')
                    # name_in_db.replace('á', 'a').replace('é', 'e')

                    if name.lower() == name_in_db:
                        # return {'number':number, 'status':True}
                        # return int(number)
                        return number
                return False
        else:
            # return 'Error en archivo'
            pass
        


if __name__ == '__main__':
    transactions = Transaction()
    # color = Transaction()
    # color.test_colors()
    
    # if(os.path.isfile('dev\\contacts.txt')):
    #     print('en ruta')
    #     with open('dev\\contacts.txt', 'r') as archivo:
    #         if(len(archivo.readlines()) <= 3):
    #             print(False)
    #         else:
    #             print(True)
    # else:
        # print(False)
    
    number = transactions.read_phone_numbers('raylin')
    print(number)

    # print(transactions.read_phone_numbers())