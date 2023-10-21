from Persona import Persona
import random

class Cliente(Persona):
    def __init__(self, id, nombre, apellido, correo, contrasena, fecha_ingreso):
        super().__init__(id, nombre, apellido, correo, contrasena)
        self._fecha_ingreso = fecha_ingreso

    @property
    def fecha_ingreso(self):
        return self._fecha_ingreso

    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    def registrar(self):
        super().registrar()
        self.fecha_ingreso = input("Ingrese la fecha de ingreso: ")

    def ver_registro(self):
        super().ver_registro()
        print(f"Fecha de Ingreso: {self.fecha_ingreso}")

    def agendar_cita(self):
        print("Agendar Cita:")
        fechas_disponibles = Cliente.generar_fechas_disponibles()
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
