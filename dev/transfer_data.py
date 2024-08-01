from socket import gethostbyname, create_connection, error
import json

# Este fichero contendra una clase con todos los métodos y propiedades necesarios para la transferencia de informaciónes entre disitntos archivos, esto con el fin de tener un código más modularizado y limpio.

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

    #* Leer archivo .json de configuración
    def read_config_file(self):
        try:
            with open('dev/web/assets/config.json', 'r', encoding='utf-8') as file:
                config = json.load(file)
                return config
                # El tipo de dato de config es diccionario.

                # Imprimir el contenido de forma legible
                # print(json.dumps(config['assistant'], indent=4, ensure_ascii=False))
        except FileNotFoundError:
            print("No se encontró el archivo de configuración.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")


    #* Leer archivo de configuración y devolver diccionario con los resultados obtenidos readfile()

    #* Función para revisar si el usuario tiene conección a internet
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

    def letras_a_numero(self, texto:str):
        mapeo = {
            'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5,
            'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9, 'diez': 10,
            'once': 11, 'doce': 12, 'trece': 13, 'catorce': 14, 'quince': 15, 
            'dieciséis': 16, 'diecisiete': 17, 'dieciocho': 18, 'diecinueve': 19, 
            'veinte': 20, 'veintiuno': 21, 'veintidós': 22, 'veintitrés': 23, 
            'veinticuatro': 24, 'veinticinco': 25, 'veintiséis': 26, 'veintisiete': 27, 
            'veintiocho': 28, 'veintinueve': 29, 'treinta': 30, 'treinta y uno': 31, 'treinta y dos': 32
        }

        # Método 1
        # for text_number in mapeo:
        #     if texto == text_number:
        #         return mapeo.get(text_number)
        # return False

        # Método 2
        # if texto in mapeo.keys():
        #     return mapeo.get(texto)
        # else:
        #     return False
        
        # Método 3
        # return mapeo.get(texto) if texto in mapeo.keys() else False

        # Método 4
        return mapeo.get(texto, False)
        # Este es el método más eficiente, con una unica comprobación obtenemos lo que queremos
            


if __name__ == '__main__':
    transactions = Transaction()
    print(transactions.read_config_file())
    # transactions.initial_config()
    # print(transactions.letras_a_numero('cien'))
    # color = Transaction()
    # color.test_colors()
    # transactions.initial_config()
    # data = transactions.read_config_file_line('language')
    # print(data)
    # print(transactions.check_internet_connection())
    # transactions.write_on_config_file('Dato1', 'Jarvis')
    # transactions.write_on_config_file('Dato2', True)
    # transactions.write_on_config_file('Dato3', 12.25)
    # transactions.initial_config()
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