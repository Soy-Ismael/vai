# Suponiendo que se tiene este json:
# {
#     "database": {
#         "host": "localhost",
#         "port": 3306,
#         "user": "root",
#         "password": "password"
#     },
#     "logging": {
#         "level": "DEBUG",
#         "file": "app.log"
#     }
# }

#? Para leerlo:
import json

# Leer el archivo JSON
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

# Acceder a los valores
db_host = config['database']['host']
db_port = config['database']['port']
log_level = config['logging']['level']

# Imprimir los valores
print(f"Database Host: {db_host}")
print(f"Database Port: {db_port}")
print(f"Logging Level: {log_level}")


#? Para escribir:
import json

# Leer el archivo JSON
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

# Modificar un valor
config['database']['password'] = 'new_password'

# Guardar los cambios en el archivo JSON
with open('config.json', 'w', encoding='utf-8') as file:
    json.dump(config, file, indent=4, ensure_ascii=False)

print("Configuración actualizada y guardada.")


# Lectura del Archivo:
# Usamos with open('config.json', 'r', encoding='utf-8') as file: para abrir el archivo en modo lectura.
# json.load(file) carga el contenido del archivo JSON en un diccionario de Python.
# Acceso a los Valores:
# Puedes acceder a los valores del diccionario utilizando las claves, como config['database']['host'].
# Modificación y Escritura:
# Para modificar un valor, simplemente asignas un nuevo valor a la clave correspondiente.
# Para guardar los cambios, abrimos el archivo en modo escritura ('w') y usamos json.dump() para escribir el diccionario de vuelta al archivo.
# indent=4 formatea el JSON para que sea más legible, y ensure_ascii=False permite que los caracteres no ASCII se escriban tal como están (por ejemplo, caracteres acentuados).


#* Manejo de errores
try:
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
except FileNotFoundError:
    print("El archivo de configuración no se encontró.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")