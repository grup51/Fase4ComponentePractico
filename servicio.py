
# Esta clase es como una regla general nadie puede crear un servicio vacio
# solo sirve de base para los servicios reales
class Servicio(ABC):
    def __init__(self, tipo, precio_base):
        # todos los servicios empiezan con un nombre y un costo inicial
        self.tipo = tipo
        self.precio_base = precio_base
#  es una tarea obligatoria cada servicio debe decirnos como calcula su precio
    @abstractmethod
    def calcular_costo(self, cantidad, **kwargs):
        pass
# Otra tarea obligatoria cada servicio debe saber explicarse a si mismo
    @abstractmethod
    def describir_servicio(self):
        pass
    # aporte jhon jairo cardenas
# creamos el servicio para alquilar salas. Como es hijo de servicio ya sabe que tiene un nombre y un precio base
class ReservaSalas(Servicio):
    def describir_servicio(self): # esta línea sirve para que cuando el programa pregunte que es esto responda sala de juntas
        return f"Sala de Juntas ({self.tipo})" # seguido del tipo de sala
# se define como cobrar
    def calcular_costo(self, horas, descuento=0):
        
        if horas > 12:# pongo un limite si el cliente se pasa de 12 horas el programa se detiene
            raise ErrorDeNegocio("Parámetro excedido: Máximo 12 horas por reserva.") # Lanzo el aviso de error explicando que no se pueden reservar tantas horas
        total = (self.precio_base * horas) - descuento # operación matematica multiplico el precio por el tiempo y le resto el descuento
        return max(total, 0) # entrego el resultado final asegurandome de que si el descuento es mayor al precio el sistema no me de numeros negativos
#esta es la segunda clase también es hija de Servicio aqui alquilamos objetos fisicos
class AlquilerEquipos(Servicio):
    def describir_servicio(self):# identifico el servicio como un equipo tecnologico y lo muestro en pantalla 
        return f"Equipo Tecnológico: {self.tipo}"

    def calcular_costo(self, dias, tiene_seguro=True): # pedimos los días y preguntamos si el cliente tiene seguro
        
        cargo_seguro = 15000 if tiene_seguro else 0 # si tiene seguro le sumamos 15000 pesos si no le sumamos 0
        return (self.precio_base * dias) + cargo_seguro # devuelvo el cobro final sumando el precio por los dias mas lo que haya salido del seguro

class AsesoriaEspecializada(Servicio): # representa el conocimiento experto que vendemos dividido en sesiones 
    def describir_servicio(self): # presento el servicio como una consultoria experta
        return f"Consultoría Experta en {self.tipo}" # le digo al cliente en que tema es experto el asesor que contrato

    def calcular_costo(self, sesiones): # Defino la forma de cobrar
        # multiplicamos el precio base por las sesiones y le sumamos un 10% extra
        return (self.precio_base * sesiones) * 1.10
