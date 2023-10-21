from Empleado import Empleado
from Persona import Persona
from Cliente import Cliente
import random

class Negocios:
    @staticmethod
    def registrar_persona():
        print("Registro de Persona:")
        tipo = input("Seleccione el tipo (Empleado/Cliente): ").lower()
        if tipo == "empleado":
            return Negocios.registrar_empleado()
        elif tipo == "cliente":
            return Negocios.registrar_cliente()
        else:
            print("Tipo no válido.")
            return None

    @staticmethod
    def registrar_empleado():
        empleado = Empleado(None, None, None, None, None, None, None)
        empleado.registrar()
        return empleado

    @staticmethod
    def registrar_cliente():
        cliente = Cliente(None, None, None, None, None, None)
        cliente.registrar()
        return cliente

    @staticmethod
    def agendar_cita():
        print("Agendar Cita:")
        fechas_disponibles = Negocios.generar_fechas_disponibles()
        for i, fecha in enumerate(fechas_disponibles):
            print(f"{i + 1}. {fecha}")
        seleccion = int(input("Seleccione una fecha (1-5): "))
        if 1 <= seleccion <= 5:
            fecha_seleccionada = fechas_disponibles[seleccion - 1]
            print(f"Ha agendado una cita para el {fecha_seleccionada}.")
            fechas_disponibles.remove(fecha_seleccionada)
        else:
            print("Selección no válida.")

    @staticmethod
    def generar_fechas_disponibles():
        fechas_disponibles = []
        for _ in range(5):
            dia = random.randint(1, 31)
            mes = random.randint(1, 12)
            fecha = f"{dia:02}/{mes:02}"
            fechas_disponibles.append(fecha)
        return fechas_disponibles
