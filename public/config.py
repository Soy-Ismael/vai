import os
import pyttsx3

green_color = "\033[92m"
yellow_color = "\033[93m"
red_color = "\033[91m"
cian_color = "\033[96m"
negrita = "\033[1m"
normal_color = "\033[0m"


warning_template = f"{yellow_color}{negrita}ADVERTENCIA: {normal_color}"
err_template = f"{red_color}{negrita}ERROR: {normal_color}"

nombre_archivo = 'config.txt'

def check_config():
    if(os.path.isfile('dev\\'+nombre_archivo)):
        return True
    else:
        return False


def create_config_file():
    try:
        with open('dev\\'+nombre_archivo, 'w') as archivo:
            # Retorna verdadero si el archivo de configuración se crea con exito
            return True
    except Exception as e:
        print(err_template+f'Ocurrio un error al crear el archivo de configuración: {e}')
        # Retorna false si el archivo de configuración no se crea, ya sea por ausencia de permisos de escritura para el usuario que ejecuta el software o por cualquier otro motivo
        return False
    

# initial_config()
def initial_config():
    try:
        text_plain_enter = '\n'

        name = input('Nombre del asistente: ')
        while(len(name) < 1):
            print(f"{err_template} {red_color} {negrita}DATO INVALIDO. {normal_color}")
            print(f"{err_template} {red_color} {negrita}El nombre debe tener algún carácter.{normal_color}")
            name = input('Nombre del asistente: ')
            
        name = f"name: {name}"
        lang = input('Idioma preferido (es-ES / en-US): ')

        while lang != 'es-ES':
            if lang == 'en-US':
                break
            print(warning_template+'Entrada invalida, intentalo nuevamente')
            lang = input('Idioma preferido (es-ES / en-US): ')

        lang = f"language: {lang}"

        hour_format = int(input('Formato de hora (12 / 24): '))
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
            # engine.setProperty('voice', voices[voice_id].id)
            # print(f"No existe la voz con el ID {voice_id}, asegurese de tener ingles, español de españa y español de mexico instalado en su windows")
            # print(f"{err_template}en configuración de idiomas")

            # print(f"{yellow_color} ={negrita} = Escoge una voz escribiendo su ID = = = {normal_color}")
            print(f"{yellow_color}Las voces disponibles son proporcionales a la cantidad de idiomas instalados{normal_color} {text_plain_enter}")

            index = 0
            for voice in voices:
                # print(f'{yellow_color} - - - - - - - - - - - - {normal_color}')
                # print(f'INDICE:{cian_color} {index} {normal_color}')
                # print(f'ID:{cian_color} {voice.id} {normal_color}')
                voice_name = voice.name

                # try:
                #     voice_name = voice_name.replace('Microsoft', '')
                #     voice_name = voice_name.replace('Desktop', '')
                # except:
                #     pass

                voice_name = voice_name.replace('Microsoft', '')
                voice_name = voice_name.replace('Desktop', '')

                # print(f'ID:{red_color}{negrita} {index} || {normal_color}Name:{cian_color} {voice_name} {normal_color}')

                # ϟ ↦ ↯ ↪ ⇆ ⇢ ⇉ ⇨ ➜ ➠ ➸ ➵ ⤨ ⟼ ☠ ✘ ッ ヅ ツ 
                print(f'{red_color} {negrita} ID: {green_color} {index}  {red_color} ヅ {normal_color}{cian_color} {voice_name} {normal_color}')
                print(f'{yellow_color} - - - - - - - - - - - - {normal_color}')
                index = index + 1

            # print(voices.__len__())
            print(f"{yellow_color}{negrita}= = Escoge una voz escribiendo su ID = = {normal_color} {text_plain_enter}")

            voice_number = int(input('Voz preferida (0, 1, 2...)(int): '))
            
            while(voice_number < 0 or voice_number > len(voices)):
                voice_number = 0
                print(f"{err_template} {red_color} {negrita}DATO INVALIDO. {normal_color}")
                # print(f"{err_template}No existe la voz con el ID {voice_number}, intentalo nuevamnete")
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

        try:
            with open('dev\\'+nombre_archivo, 'w') as archivo:
                archivo.writelines(data_dictionary)
                # Retorna verdadero si se insertaron con exito los datos en el archivo de configuración
                return True
        except Exception as e:
            print(err_template+f'Ocurrio un problema al insertar datos en archivo de configuración ')
            print(e)
            # Retorna falso si no se insertaron los datos en el archivo config.txt
            return False
    except KeyboardInterrupt:
        print(f'\n{warning_template}Acción cancelada por el usuario.')

if __name__ == "__main__":
    # check_config()
    initial_config()

    # try:
    #     initial_config()
    # except KeyboardInterrupt:
    #     print(f'\n{warning_template}Acción cancelada por el usuario.')