class Persona:
    def __init__(self, id, nombre, apellido, correo, contrasena):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    def registrar(self):
        self._id = input("Ingrese el id: ")
        self._nombre = input("Ingrese el nombre: ")
        self._apellido = input("Ingrese el apellido: ")
        self._correo = input("Ingrese el correo: ")
        self._contrasena = input("Ingrese la contraseña: ")

    def ver_registro(self):
        print(
            f"Id: {self._id} Nombre: {self._nombre} Apellido: {self._apellido} Correo: {self._correo}")
