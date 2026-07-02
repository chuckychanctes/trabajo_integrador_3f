import random
import string

def generar_contrasena(opcion, longitud=8):
    if opcion == "1":
        caracteres = string.ascii_letters
    elif opcion == "2":
        caracteres = string.digits
    elif opcion == "3":
        caracteres = string.ascii_letters + string.digits
    elif opcion == "4":
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    return ''.join(random.choice(caracteres) for _ in range(longitud))

def menu_password():
    while True:
        print("\n--- Generador de Contraseñas ---")
        print("1. Solo letras")
        print("2. Solo números")
        print("3. Letras y números")
        print("4. Letras, números y caracteres especiales")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            break
        else:
            pwd = generar_contrasena(opcion)
            if pwd:
                print(f"Contraseña generada: {pwd}\n")
            else:
                print("Opción inválida.\n")

menu_password()
