import random

# Diccionario para almacenar tickets
tickets = {}

def generar_ticket():
    nombre = input("Ingrese su Nombre: ")
    sector = input("Ingrese su Sector: ")
    asunto = input("Ingrese el Asunto: ")
    mensaje = input("Ingrese el Mensaje: ")

    numero = random.randint(1000, 9999)
    tickets[numero] = {
        "nombre": nombre,
        "sector": sector,
        "asunto": asunto,
        "mensaje": mensaje
    }

    print("\nSe generó el siguiente Ticket:")
    print(f"Su nombre: {nombre}")
    print(f"Nº Ticket: {numero}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
    print("== Recordar su número de Ticket ==\n")

def leer_ticket():
    try:
        numero = int(input("Ingrese el número de Ticket: "))
        ticket = tickets[numero]
        print("\nTicket encontrado:")
        print(f"Nombre: {ticket['nombre']}")
        print(f"Sector: {ticket['sector']}")
        print(f"Asunto: {ticket['asunto']}")
        print(f"Mensaje: {ticket['mensaje']}\n")
    except:
        print("--- Ticket no encontrado ---\n")

def menu():
    while True:
        print("Hola, bienvenido al sistema de Tickets")
        print("1 - Generar un Nuevo Ticket")
        print("2 - Leer un Ticket")
        print("3 - Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            generar_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            salir = input("¿Seguro que desea salir? (s/n): ")
            if salir.lower() == "s":
                print("Programa finalizado.")
                break
        else:
            print("Opción inválida.\n")

menu()
