"""
Programa de gestión de granja de animales domésticos
Demuestra los conceptos de POO: Clases, Objetos, Herencia, Encapsulación y Polimorfismo
"""


class Animal:
    """
    Clase base que representa un animal genérico en la granja.
    Demuestra encapsulación mediante atributos privados.
    """

    def __init__(self, nombre, edad, peso):
        self.__nombre = nombre  # Atributo privado (encapsulado)
        self.__edad = edad  # Atributo privado
        self.__peso = peso  # Atributo privado
        self.__alimentado = False

    # Métodos getter y setter para demostrar encapsulación
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.__nombre = nombre
        else:
            print("Error: Nombre no válido")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("Error: Edad no puede ser negativa")

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        if peso > 0:
            self.__peso = peso
        else:
            print("Error: Peso debe ser positivo")

    def alimentar(self):
        """Método para alimentar al animal"""
        if not self.__alimentado:
            print(f"{self.__nombre} ha sido alimentado.")
            self.__alimentado = True
        else:
            print(f"{self.__nombre} ya estaba alimentado.")

    def hacer_sonido(self):
        """Método genérico que será sobrescrito por clases derivadas (polimorfismo)"""
        print("Este animal hace un sonido genérico")

    def __str__(self):
        """Método especial para representación como string"""
        return f"Animal: {self.__nombre}, Edad: {self.__edad} años, Peso: {self.__peso} kg"


class Perro(Animal):
    """
    Clase derivada que representa un perro en la granja.
    Demuestra herencia y polimorfismo.
    """

    def __init__(self, nombre, edad, peso, raza, entrenado=False):
        super().__init__(nombre, edad, peso)  # Llamada al constructor de la clase base
        self.raza = raza
        self.entrenado = entrenado

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Guau guau!")

    def entrenar(self):
        """Método específico de la clase Perro"""
        if not self.entrenado:
            print(f"{self.get_nombre()} está siendo entrenado.")
            self.entrenado = True
        else:
            print(f"{self.get_nombre()} ya está entrenado.")

    def __str__(self):
        """Extiende el método __str__ de la clase base"""
        base_info = super().__str__()
        return f"{base_info}, Raza: {self.raza}, Entrenado: {'Sí' if self.entrenado else 'No'}"


class Gato(Animal):
    """
    Otra clase derivada que representa un gato en la granja.
    Demuestra herencia y polimorfismo.
    """

    def __init__(self, nombre, edad, peso, color, caza_ratones=False):
        super().__init__(nombre, edad, peso)
        self.color = color
        self.caza_ratones = caza_ratones

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Miau miau!")

    def cazar(self):
        """Método específico de la clase Gato"""
        if self.caza_ratones:
            print(f"{self.get_nombre()} ha cazado un ratón.")
        else:
            print(f"{self.get_nombre()} no está interesado en cazar ratones ahora.")

    def __str__(self):
        """Extiende el método __str__ de la clase base"""
        base_info = super().__str__()
        return f"{base_info}, Color: {self.color}, Caza ratones: {'Sí' if self.caza_ratones else 'No'}"


# Función para demostrar polimorfismo con diferentes tipos de animales
def presentar_animal(animal):
    """
    Función que acepta cualquier objeto Animal y muestra su información y sonido.
    Demuestra polimorfismo al trabajar con diferentes tipos de animales.
    """
    print("\n--- Presentando animal ---")
    print(animal)
    animal.hacer_sonido()


# Programa principal
if __name__ == "__main__":
    print("=== Sistema de Gestión de Granja ===")

    # Creación de instancias (objetos)
    animal_generico = Animal("Genérico", 3, 10)
    perro1 = Perro("Rex", 5, 15, "Labrador", False)
    gato1 = Gato("Mishi", 2, 4, "Negro", True)

    # Demostración de encapsulación
    print("\n--- Demostración de Encapsulación ---")
    print(f"Nombre del perro (usando getter): {perro1.get_nombre()}")
    perro1.set_nombre("Rex Modificado")
    print(f"Nombre modificado: {perro1.get_nombre()}")

    # Intentando acceder directamente al atributo privado (generaría error)
    # print(perro1.__nombre)  # AttributeError

    # Demostración de métodos
    print("\n--- Alimentando animales ---")
    animal_generico.alimentar()
    perro1.alimentar()
    gato1.alimentar()

    print("\n--- Entrenando al perro ---")
    perro1.entrenar()
    perro1.entrenar()  # Segunda llamada para mostrar diferencia

    print("\n--- Acción del gato ---")
    gato1.cazar()

    # Demostración de polimorfismo
    print("\n--- Demostración de Polimorfismo ---")
    presentar_animal(animal_generico)
    presentar_animal(perro1)
    presentar_animal(gato1)

    # Mostrando información completa de los animales
    print("\n--- Información completa de los animales ---")
    print(animal_generico)
    print(perro1)
    print(gato1)