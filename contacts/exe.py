class transfer_data:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    

def importar_contactos(contacts):
    contactos = []

    with open(contacts, 'r') as contacts:
        lineas = contacts.readlines()
        for linea in lineas:
            datos_contacto = linea.strip().split(',')
            if len(datos_contacto) == True:
                nombre, telefono = datos_contacto
                contactos.append(transfer_data(nombre, telefono, ))
            else:
                print("Error: El formato de la línea es incorrecto:", linea)

    return contactos

def importar_contactos():
    contactos = 'contacts.txt'
    contactos = importar_contactos(contactos)

    print("Contactos importados:")
    for contacto in contactos:
        print("Nombre:", contacto.nombre)
        print("Teléfono:", contacto.telefono)
       #  print("Email:", contacto.email)
       # print()

if __name__ == "__importar_contactosq__":
   importar_contactos()
