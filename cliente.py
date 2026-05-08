# Clase Cliente (encapsulación + validaciones)
from excepciones import ErrorCliente

class Cliente:
    def __init__(self, nombre, correo):
        if not nombre:
            raise ErrorCliente("Nombre vacío")
        if "@" not in correo:
            raise ErrorCliente("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"{self.__nombre} - {self.__correo}"