from Persona import Persona
import random

class Empleado(Persona):
    def __init__(self, id, nombre, apellido, correo, contrasena, salario, cargo):
        super().__init__(id, nombre, apellido, correo, contrasena)
        self._cargo = cargo
        self._salario = salario
        self._horario_trabajo = {}

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def registrar(self):
        super().registrar()
        self.cargo = input("Ingrese el Cargo: ")
        self.salario = float(input("Ingrese el Salario: "))

    def ver_registro(self):
        super().ver_registro()
        print(f"Cargo: {self.cargo} Salario: {self.salario}")

    def iniciar_sesion(self):
        correo_reg = input("Ingrese el correo registrado: ")
        contras_reg = input("Ingrese la contraseña registrada: ")

        if correo_reg == self.correo and contras_reg == self.contrasena:
            print(f"Bienvenido {self._nombre}")
            return True
        else:
            print("Valida tus credenciales")
            return False

    def agendar_horario_de_trabajo(self):
        print("Agendando horario de trabajo...")

        # Días de la semana
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        for dia in dias_semana:
            # Generar una hora aleatoria para el día
            hora_inicio = random.randint(8, 12)  # Ejemplo: De 8 AM a 12 PM
            hora_fin = hora_inicio + random.randint(1, 4)  # Ejemplo: Duración de 1 a 4 horas

            # Agregar el horario al diccionario
            self._horario_trabajo[dia] = f"{hora_inicio}:00 AM - {hora_fin}:00 PM"

        print("Horario de trabajo agendado:")
        for dia, horario in self._horario_trabajo.items():
            print(f"{dia}: {horario}")

    def iniciar_negocio_empleado(self, iniciar_sesion, ver_registro):
        init = iniciar_sesion()

        while init:
            print("1: Ver datos de usuario 2: Agendar horario de trabajo 3: Salir")
            opc = int(input("Seleccione una opción: "))

            if opc == 1:
                print("Ver Datos de usuario")
                ver_registro()
            elif opc == 2:
                self.agendar_horario_de_trabajo()
            elif opc == 3:
                print("Salir")
                init = False
            else:
                print("Seleccione una opción correcta")
