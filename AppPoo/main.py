from Negocios import Negocios
from Noticias import Noticias

def main_menu():
    print("Menú Principal")
    print("1. Empleado")
    print("2. Persona")
    print("3. Cliente")
    print("4. Salir")

    while True:
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            empleado = Negocios.registrar_empleado()
            if empleado is not None:
                empleado_menu(empleado)
        elif opcion == "2":
            persona = Negocios.registrar_persona()
            if persona is not None:
                persona_menu(persona)
        elif opcion == "3":
            cliente = Negocios.registrar_cliente()
            if cliente is not None:
                cliente_menu(cliente)
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def empleado_menu(empleado):
    while True:
        print("\nMenú de Empleado")
        print("1. Ver registro")
        print("2. Agendar horario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            empleado.ver_registro()
        elif opcion == "2":
            empleado.agendar_horario_de_trabajo()
        elif opcion == "3":
            print("Saliendo del menú de Empleado")
            break

def persona_menu(persona):
    while True:
        print("\nMenú de Persona")
        print("1. Ver registro")
        print("2. Noticias")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona.ver_registro()
        elif opcion == "2":
            Noticias.mostrar_noticias(persona)
        elif opcion == "3":
            print("Saliendo del menú de Persona")
            break

def cliente_menu(cliente):
    while True:
        print("\nMenú de Cliente")
        print("1. Ver registro")
        print("2. Agendar cita")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente.ver_registro()
        elif opcion == "2":
            cliente.agendar_cita()
        elif opcion == "3":
            print("Saliendo del menú de Cliente")
            break

if __name__ == "__main__":
    main_menu()
