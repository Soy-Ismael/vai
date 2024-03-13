nombre_archivo = 'config.txt'

def readfile(int: line):
    try:
        with open('dev\\'+nombre_archivo, 'r') as archivo:
            for line in archivo:
                print(line)

            return True
    except Exception as e:
        print(err_template+f'Ocurrio un error al leer el archivo de configuración: {e}')
        return False