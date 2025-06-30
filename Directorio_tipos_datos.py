# Programa para gestionar información básica de 5 socios de una urbanización
# Registro de nombres, apellidos, cédula, edad y peso de los socios

def main():
    # Lista para almacenar los datos de los socios
    lista_socios = []

    # Datos predefinidos de 5 socios
    datos_socios = [
        {"nombres": "Juan Carlos", "apellidos": "Pérez González", "cedula": "0-12345678", "edad": 35, "peso": 72.5},
        {"nombres": "María Alejandra", "apellidos": "Gómez Rodríguez", "cedula": "2-87654321", "edad": 28,
         "peso": 58.3},
        {"nombres": "Luis Enrique", "apellidos": "Martínez Blanco", "cedula": "3-56781234", "edad": 42, "peso": 81.7},
        {"nombres": "Ana Isabel", "apellidos": "López Sánchez", "cedula": "4-43218765", "edad": 31, "peso": 63.2},
        {"nombres": "Carlos Andrés", "apellidos": "Hernández Castro", "cedula": "5-98765432", "edad": 39, "peso": 75.0}
    ]

    # Agregar socios a la lista principal usando for
    for socio in datos_socios:
        lista_socios.append(socio)

    # Mostrar información de todos los socios
    print("\n=== REGISTRO DE SOCIOS ===")
    for i, socio in enumerate(lista_socios, 1):
        print(f"\nSocio #{i}:")
        print(f"Nombre completo: {socio['nombres']} {socio['apellidos']}")
        print(f"Cédula: {socio['cedula']}")
        print(f"Edad: {socio['edad']} años")
        print(f"Peso: {socio['peso']} kg")

    # Buscar socio por cédula usando while y if-else
    print("\n=== BUSCAR SOCIO POR CÉDULA ===")
    while True:
        cedula_buscar = input("Ingrese la cédula a buscar (o 'salir' para terminar): ")

        if cedula_buscar.lower() == 'salir':
            break

        socio_encontrado = None
        # Buscar en la lista de socios
        for socio in lista_socios:
            if socio["cedula"] == cedula_buscar:
                socio_encontrado = socio
                break

        if socio_encontrado:
            print("\nSocio encontrado:")
            print(f"Nombre: {socio_encontrado['nombres']} {socio_encontrado['apellidos']}")
            print(f"Edad: {socio_encontrado['edad']} años")
            print(f"Peso: {socio_encontrado['peso']} kg")
        else:
            print("No se encontró ningún socio con esa cédula.")

    # Clasificar socios por edad usando if-else
    print("\n=== CLASIFICACIÓN POR EDAD ===")
    for socio in lista_socios:
        if socio['edad'] < 30:
            categoria = "Joven"
        elif 30 <= socio['edad'] < 50:
            categoria = "Adulto"
        else:
            categoria = "Mayor"

        print(f"{socio['nombres']} {socio['apellidos']} ({socio['edad']} años) - Categoría: {categoria}")

    # Calcular promedio de peso
    total_peso = sum(socio['peso'] for socio in lista_socios)
    promedio_peso = total_peso / len(lista_socios)
    print(f"\nEl peso promedio de los socios es: {promedio_peso:.2f} kg")


if __name__ == "__main__":
    main()