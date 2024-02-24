import os

green_color = "\033[92m"
yellow_color = "\033[93m"
red_color = "\033[91m"
negrita = "\033[1m"
normal_color = "\033[0m"

warning_template = f"{yellow_color}{negrita}ADVERTENCIA: {normal_color}"
err_template = f"{red_color}{negrita}ERROR: {normal_color}"
nombre_archivo = 'config.txt'

def check_config():
    if(os.path.isfile('dev\\'+nombre_archivo)):
        # print('Archivo de configuración existente')
        return True
    else:
        # print(warning_template+'Archivo de configuración inexistente')
        # talk('Archivo de configuración inexistente, ¿Te gustaria crearlo ahora?')
        # text = va.listen()
        return False
        # if('si' in text):
        #     create_config_file()
        #     initial_config()

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
    text_plain_enter = '\n'
    # name = input('Nombre del asistente')
    # language = input('Lenguaje preferido')
    # hour_format = input('Formato de hora')
    # print(name)
    # print(language)
    # print(hour_format)

    # data_config = {
    #     'Nombre'        : str(name),
    #     'Idioma'        : str(language),
    #     'Formato de hora': str(hour_format),
    # }

    name = f"name: {input('Nombre del asistente: ')}"
    language = f"language: {input('Idioma preferido (es-ES / en-US): ')}"
    hour_format = f"hour_format: {input('Formato de hora (12 / 24): ')}"

    print(f"{yellow_color} {negrita} {name} {normal_color}")
    print(f"{yellow_color} {negrita} {language} {normal_color}")
    print(f"{yellow_color} {negrita} {hour_format} {normal_color}")

    data_dictionary = [name+text_plain_enter, language+text_plain_enter, hour_format+text_plain_enterb]

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

# check_config()
initial_config()