class Nomina:

    def __init__(self):
        self.empleados = {}
        self.salario_minimo = 1000000  # 2 SMLV
        self.auxilio_transporte = 106454  # Valor del auxilio de transporte

    def registrar_empleado(self, id, nombre, apellido, cargo, area, salario):
        self.empleados[id] = {
            "nombre": nombre,
            "apellido": apellido,
            "cargo": cargo,
            "area": area,
            "salario": salario
        }
        print("Empleado registrado exitosamente.")

    def listar_empleados(self):
        return self.empleados

    def calcular_salario_neto(self, empleado_id):
        empleado = self.empleados.get(empleado_id)
        if not empleado:
            return "Empleado no encontrado."

        salario = empleado["salario"]
        salario_neto = salario + (self.auxilio_transporte if salario < 2 * self.salario_minimo else 0)
        return salario_neto

    def imprimir_colilla(self, empleado_id):
        empleado = self.empleados.get(empleado_id)
        if empleado:
            salario_neto = self.calcular_salario_neto(empleado_id)

            print("Colilla de pago para el empleado:")
            print(f"ID: {empleado_id}")
            print(f"Nombre: {empleado['nombre']} {empleado['apellido']}")
            print(f"Cargo: {empleado['cargo']}")
            print(f"Área: {empleado['area']}")
            print(f"Salario Bruto: {empleado['salario']}")
            print(f"Salario Neto: {salario_neto}")
        else:
            print("Empleado no encontrado.")

    def sumar_nomina(self):
        total_nomina = sum(self.calcular_salario_neto(empleado_id) for empleado_id in self.empleados)
        return total_nomina

if __name__ == "__main__":
    nomina = Nomina()

    while True:
        print("\nMENU INICIAL:")
        print("1. Analista en Recursos Humanos")
        print("2. Empleado")
        print("3. Sumar Total de la Nómina")
        print("4. Salir")

        opcion_menu_inicial = input("Seleccione una opción: ")

        if opcion_menu_inicial == "1":
            while True:
                print("\nMENU DE ANALISTA EN RECURSOS HUMANOS:")
                print("1. Registrar Empleado")
                print("2. Listar Empleados")
                print("3. Buscar Colilla")
                print("4. Buscar Empleado")
                print("5. Salir")

                opcion_menu_analista = input("Seleccione una opción: ")

                if opcion_menu_analista == "1":
                    id = int(input("ID del empleado: "))
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    cargo = input("Cargo: ")
                    area = input("Área: ")
                    salario = float(input("Salario: "))
                    nomina.registrar_empleado(id, nombre, apellido, cargo, area, salario)

                elif opcion_menu_analista == "2":
                    empleados = nomina.listar_empleados()
                    for empleado_id, empleado_info in empleados.items():
                        print(f"ID: {empleado_id}, Nombre: {empleado_info['nombre']} {empleado_info['apellido']}")

                elif opcion_menu_analista == "3":
                    empleado_id = int(input("ID del empleado: "))
                    nomina.imprimir_colilla(empleado_id)

                elif opcion_menu_analista == "4":
                    empleado_id = int(input("ID del empleado: "))
                    if empleado_id in nomina.empleados:
                        print(f"Empleado encontrado: {nomina.empleados[empleado_id]['nombre']} {nomina.empleados[empleado_id]['apellido']}")
                    else:
                        print("Empleado no encontrado.")

                elif opcion_menu_analista == "5":
                    break

        elif opcion_menu_inicial == "2":
            while True:
                print("\nMENU DE EMPLEADO:")
                print("1. Buscar e Imprimir Colilla")
                print("2. Salir")

                opcion_menu_empleado = input("Seleccione una opción: ")

                if opcion_menu_empleado == "1":
                    empleado_id = int(input("ID del empleado: "))
                    nomina.imprimir_colilla(empleado_id)

                elif opcion_menu_empleado == "2":
                    break

        elif opcion_menu_inicial == "3":
            total_nomina = nomina.sumar_nomina()
            print(f"Total de la nómina: {total_nomina}")

        elif opcion_menu_inicial == "4":
            break
