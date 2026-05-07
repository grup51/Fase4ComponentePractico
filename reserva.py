class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if self.cantidad <= 0:
                raise ValueError("Cantidad inválida")

            costo = self.servicio.calcular_costo(self.cantidad)
            self.estado = "Confirmada"
            return costo

        except Exception as e:
            raise Exception("Error al confirmar reserva") from e

    def cancelar(self):
        self.estado = "Cancelada"