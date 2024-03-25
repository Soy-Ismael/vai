import os
from config import create_config_file, initial_config

green_color = "\033[92m"
yellow_color = "\033[93m"
red_color = "\033[91m"
negrita = "\033[1m"
normal_color = "\033[0m"

err_template = f"{red_color}{negrita}ERROR: {normal_color}"
nombre_archivo = 'config.txt'

def check_file_integrity():
    if(os.path.isfile('dev\\'+nombre_archivo)):
        with open('dev\\'+nombre_archivo, 'r') as archivo:
            if(len(archivo.readlines()) <= 3):
                return False
            else:
                return True
    else:
        return False

def readfile():
    try:
        with open('dev\\'+nombre_archivo, 'r') as archivo:
            data = {}

            for line in archivo:
                line = line.replace("\n", '')
                
                key , value  = line.strip().split(': ')
                # try:
                    # key , value  = line.strip().split(': ')
                # except:
                #     print(f"{err_template}archivo de configuración corrupto")
                #     print(f"Creando archivo de configuración nuevamente...")
                #     create_config_file()
                #     initial_config()
                #     readfile()
                # print('Clave:'+key, 'Valor:'+value)

                # data = {f'{key}' : value}
                data[key] = value

            # return data
            if(len(data) <= 0):
                # print(f"{err_template}Archivo de configuración sin datos")
                # print(f"Creando archivo de configuración nuevamente...")
                return False
                # create_config_file()
                # initial_config()
            else:
                return data
    except ValueError:
        print(err_template+'en archivo de configuración')
    except Exception as e:
        print(err_template+f"Ocurrio un error al leer el archivo de configuración: {e}")


        return False
        # print(f"{err_template}archivo de configuración corrupto")
        # print(f"Creando archivo de configuración nuevamente...")
        # create_config_file()
        # initial_config()
        # return readfile()

        # return False

if __name__ == '__main__':
    try:
        
        def print_data(data):
            name, lang, hour_format, voice = data

            print(f"{yellow_color}{negrita}Nombre:{normal_color}{green_color} {name} {normal_color}")
            print(f"{yellow_color}{negrita}Idioma:{normal_color}{green_color} {lang} {normal_color}")
            print(f"{yellow_color}{negrita}Formato de hora:{normal_color}{green_color} {hour_format} {normal_color}")
            print(f"{yellow_color}{negrita}Indice de voz:{normal_color}{green_color} {voice} {normal_color}")


        # print(type(readfile()))
        # print(type(readfile()) != dict)

        data = readfile()
        if type(data) != dict or not check_file_integrity():
            # data = readfile()
            print(err_template+'Archivos de configuración corruptos')
        else:
            data = data.values()
            print_data(data)
    except KeyboardInterrupt:
        print(f'\n{warning_template}Acción cancelada por el usuario.')

    # print(data)

    #* Destructuring - de esta forma necesito pasar tantas variables como lineas en el config.txt y el nombre de la variables es posicional, por lo que no tiene que coincidir con el nombre de la clave del diccionario
    # name, lang, hour_format, voice = data.values() Esta linea ya se ejecuta dentro de la función

    # keys, values = data.keys(), data.values()
    # k_name, k_lang, k_hour_format, k_voice = keys
    # name, lang, hour_format, voice = values

    # print(keys)
    # print(values)

    # print(f"{yellow_color}{negrita} {k_name} {normal_color}{green_color} {name} {normal_color}")
    # print(f"{yellow_color}{negrita} {k_lang} {normal_color}{green_color} {lang} {normal_color}")
    # print(f"{yellow_color}{negrita} {k_hour_format} {normal_color}{green_color} {hour_format} {normal_color}")
    # print(f"{yellow_color}{negrita} {k_voice} {normal_color}{green_color} {voice} {normal_color}")

    # print(name, lang, hour_format, voice)

    #* Destructuring - de esta forma no es necesario pasar variables para cada valor del diccionario y puede tener cualquier orden
    # name = data['name']
    # lang = data['lang']
    # hour_format = data['hour_format']
    # voice = data['voice_number']

    # print(name, lang, hour_format, voice)



#* NOTAS:
# Si la función readfile() retorna retorna el diccionario: "data" entonces se deberia manejar así el resultado de su ejecución:

    # data = readfile()
    # keys, values = data.keys(), data.values()
    # k_name, k_lang, k_hour_format, k_voice = keys
    # name, lang, hour_format, voice = values

    # print(keys)
    # print(values)

    # print(k_name, name)
    # print(k_lang, lang)

# De esta manera obtengo el nombre y el valor exacto que esta en el archivo config.py

#* #################################################################
#* #################################################################

# Si la función readfile() retorna retorna los valores del diccionario: "data.values()" entonces se deberia manejar así el resultado de su ejecución:

    # data = readfile()
    # name, lang, hour_format, voice = data

    # print(data)

    # print('Nombre:', name)
    # print('Idioma', lang)

# De esta manera obtengo el valor exacto que está en el archivo config.py. Es necesario colocar el título o identificador a ese valor obtenido.