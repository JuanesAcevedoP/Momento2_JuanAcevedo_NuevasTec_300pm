from Empleado import Empleado
from Cliente import Cliente


class Noticias:
    @staticmethod
    def mostrar_noticias(persona):
        if isinstance(persona, Empleado):
            print("Noticias para Empleados:")
            print("1. Bienvenido a nuestro equipo.")
            print("2. Reunión de empleados esta semana.")
        elif isinstance(persona, Cliente):
            print("Noticias para Clientes:")
            print("1. Descuento especial para clientes frecuentes.")
            print("2. Nuevos servicios disponibles para ti.")

        opcion = input("Seleccione una noticia (1/2): ")
        if opcion == "1":
            print("¡Gracias por elegirnos!")
        elif opcion == "2":
            print("No te pierdas la reunión importante esta semana.")
        else:
            print("Opción no válida.")
