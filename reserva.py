# Clase Reserva para gestionar las reservas de servicios
from excepciones import ErrorReserva

class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if self.cantidad <= 0:
                raise ErrorReserva("Cantidad inválida")

            costo = self.servicio.calcular_costo(self.cantidad)
            self.estado = "Confirmada"
            return costo

        except Exception as e:
            raise ErrorReserva("Error al confirmar reserva") from e

    def cancelar(self):
        self.estado = "Cancelada"