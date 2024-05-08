# Modulo para calcular que dia fue hace x dias atras
import os
from datetime import datetime, date, timedelta
from transfer_data import Transaction

transaction = Transaction()

def crear_carpeta_oculta(nombre_carpeta:str, crear_carpeta:bool = True, ocultar:bool = True):
    try:
        # Obtiene la ruta del directorio actual
        directorio_actual = os.getcwd()

        # Crea la ruta de la carpeta con el nombre proporcionado
        ruta_carpeta = os.path.join(directorio_actual, f".{nombre_carpeta}")

        if crear_carpeta:
            os.mkdir(ruta_carpeta)

        if ocultar:
            # Oculta la carpeta estableciendo el atributo "oculto"
            if os.name == 'nt':  # Windows
                os.system(f"attrib +h {ruta_carpeta}")
            else:  # Linux o macOS
                os.system(f"chflags hidden {ruta_carpeta}")
            # print(f"Carpeta oculta '{nombre_carpeta}' creada exitosamente en {ruta_carpeta}")
        else:
             # Oculta la carpeta estableciendo el atributo "oculto"
            if os.name == 'nt':  # Windows
                os.system(f"attrib -h {ruta_carpeta}")
            else:  # Linux o macOS
                os.system(f"chflags nohidden {ruta_carpeta}")
            # print(f"Carpeta '{nombre_carpeta}' mostrada exitosamente en {ruta_carpeta}")
            
    except FileExistsError:
        print(f"La carpeta '{nombre_carpeta}' ya existe en {ruta_carpeta}")


day_es = [line.rstrip('\n') for line in open('dev/txt/days_es.txt')]
day_en = [line.rstrip('\n') for line in open('dev/txt/days_en.txt')]

# Now es este momento, un ejemplo de lo que recibe como parametro es: "Monday, 15 de April del 2024", esta función remplaza la fecha en ingles por una fecha en español, de modo que no sera Lunes en lugar de Monday
def iterateDays(now):
    for i in range(len(day_en)):
        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

# getDay obtiene el dia de hoy en español
def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterateDays(now)

# Recibe el texto resultado de la peticion del usuario para evaluar lo dicho
# Esta es la funcion principal
def getDaysAgo(rec):
    value =""
    if 'ayer' in rec:
        days = 1
        value = 'ayer'
    elif 'antier' in rec:
        days = 2
        value = 'antier'
    else:
        rec = rec.replace(",","")
        rec = rec.split()
        days = 0

        for i in range(len(rec)):
            try:
                days = float(rec[i])
                # days = int(rec[i])
                break
            except:
                pass
    
    if days != 0:
        try:
            now = date.today() - timedelta(days=days)
            now = now.strftime("%A, %d de %B del %Y").lower()

            if value != "":
                return f"{value} fue {now}" if transaction.read_config_file_line('language') != 'es-ES' else f"{value} fue {iterateDays(now)}"
                # return f"{value} fue {now}"
            else:
                return f"Hace {int(days)} días fue {now}" if transaction.read_config_file_line('language') != 'es-ES' else f"Hace {int(days)} días fue {iterateDays(now)}"
                # return f"Hace {int(days)} días fue {now}"
        except Exception as e:
            return "Aún no existíamos"
    else:
        # return "No entendí"
        return ''

def getDaysAhead(rec):
    value =""
    if 'mañana' in rec:
        days = 1
        value = 'mañana'
    elif 'pasado' in rec or 'pasado mañana' in rec:
        days = 2
        value = 'pasado mañana'
    else:
        rec = rec.replace(",","")
        rec = rec.split()
        days = 0

        for i in range(len(rec)):
            try:
                days = float(rec[i])
                # days = int(rec[i])
                break
            except:
                pass
    
    if days != 0:
            now = date.today() + timedelta(days=days)
            now = now.strftime("%A, %d de %B del %Y").lower()
            return iterateDays(now)
    else:
        # return "No entendí"
        return ''




if __name__ == "__main__":
    # crear_carpeta_oculta('txt',False,True)
    # print(getDaysAgo('que dia fue hace 5 dias'))
    print(getDaysAhead('recuerdame comprar el pavo en 5 dias'))
    # print(getDay())
    # print(getDaysAgo('que dia fue ayer'))