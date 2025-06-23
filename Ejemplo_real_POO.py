# Definición de la clase Contacto
class Contacto:
    # Método constructor (inicializa el objeto)
    def __init__(self, nombre, telefono, email):
        # Asigna atributos al contacto
        self.nombre = nombre  # Guarda el nombre
        self.telefono = telefono  # Guarda el teléfono
        self.email = email  # Guarda el email

    # Método para mostrar información del contacto
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")  # Muestra nombre
        print(f"Teléfono: {self.telefono}")  # Muestra teléfono
        print(f"Email: {self.email}")  # Muestra email


# Definición de la clase Agenda
class Agenda:
    # Método constructor (inicializa la agenda)
    def __init__(self):
        self.contactos = []  # Crea lista vacía para contactos

    # Método para agregar contacto a la agenda
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)  # Añade contacto a la lista

    # Método para buscar contacto por nombre
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:  # Recorre todos los contactos
            if contacto.nombre.lower() == nombre.lower():  # Compara nombres (sin importar mayúsculas)
                contacto.mostrar_info()  # Muestra info si encuentra
                return  # Termina la función
        print("Contacto no encontrado")  # Mensaje si no encuentra


# Ejemplo de uso del programa
agenda_personal = Agenda()  # Crea una nueva agenda

# Creación de contactos de ejemplo
contacto1 = Contacto("Jensy", "0985061138", "jensyordonez650@email.com")  # Primer contacto
contacto2 = Contacto("Samuel", "0985061138", "jessyp99_6a66@email.com")  # Segundo contacto

# Agregar contactos a la agenda
agenda_personal.agregar_contacto(contacto1)  # Añade primer contacto
agenda_personal.agregar_contacto(contacto2)  # Añade segundo contacto

# Buscar un contacto específico
agenda_personal.buscar_contacto("Jensy")  # Busca contacto por nombre