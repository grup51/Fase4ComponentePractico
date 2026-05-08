# Clase abstracta Servicio + herencia
from abc import ABC, abstractmethod
from excepciones import ErrorServicio

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise ErrorServicio("Precio inválido")
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    def descripcion(self):
        return f"Servicio: {self.nombre}"


class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        return self.precio_base * dias


class Asesoria(Servicio):
    def calcular_costo(self, sesiones):
        return self.precio_base * sesiones