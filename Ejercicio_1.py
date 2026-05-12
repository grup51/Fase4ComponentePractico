
import logging # Importamos la libreria para llevar el registro de lo que pasa en el sistema
from abc import ABC, abstractmethod # Importamos la base para las clases abstractas

#  Registro de errores y eventos 
logging.basicConfig(
    filename='errores_programa.log', # Nombre del archivo donde se guardará todo
    level=logging.INFO, # registra cada movimiento importante
    format='%(asctime)s - %(levelname)s - %(message)s' # la estructura que debe llevar
)


# Definición de errores propios para que el sistema no se bloquee
class Falla_Sistema(Exception): # definimos errores propios para que el programa no se cierre de golpe
    pass

class ErrorDeNegocio(Falla_Sistema):
    """Excepción para reglas de negocio incumplidas."""
    pass

# Definición de la estructura base para los objetos del sistema
# Aquí aplicamos la abstracción para que los datos sean seguros
class EntidadGeneral(ABC): # aplicando clases abstractas entidadGeneral no se puede usar sola
    @abstractmethod
    def obtener_identificacion(self): # obligamos a que todos tengan un metodo para mostrar su ID
        pass
# --- APORTE DE BREITNER EDUARDO RODRIGUEZ FRANCO ---
# Aqui definimos al cliente, que hereda las cosas de EntidadGeneral
class Cliente(EntidadGeneral):
    def __init__(self, nombre, id_personal):
        # Revisamos que el nombre sea válido
        if not nombre or len(nombre) < 3:
            # Si el nombre esta vacio o es muy cortito frenamos todo
            raise ErrorDeNegocio("Validación Fallida: Nombre inexistente o muy corto.")
        # ahora guardamos los datos en el objeto
        self.__nombre = nombre 
        try:
            # Primero nos aseguramos de que la ID no tenga caracteres especiales
            if not str(id_personal).isalnum():
            # Si detectamos algo extraño generamos una alerta de valor invalido
                raise ValueError("Formato de identificación no alfanumérico.")
            # Superada la prueba procedemos a asignar el valor al campo privado del objeto
            self.__id_personal = id_personal
        # Si la prueba de arriba falla este bloque captura el error
        except ValueError as e:
            # El from e sirve para guardar el rastro del error original
            raise ErrorDeNegocio(f"Error al procesar identidad de {nombre}") from e
# Esta es la forma segura de dejar que otros vean el nombre del cliente
    @property
    def nombre(self):
        return self.__nombre
# Con esto entregamos la cedula etiquetada con la palabra ID
    def obtener_identificacion(self):
        return f"ID: {self.__id_personal}"

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

#definimos la clase reserva que funciona como el molde principal para generar cada registro de alquiler en nuestro sistema
class Reserva:
    #creamos el metodo de inicio que es el encargado de recibir los datos basicos cuando nace una nueva reserva
    def __init__(self, cliente, servicio, duracion):
        # tomamos el dato del cliente y lo guardamos como un atributo propio
        self.cliente = cliente
        # vinculamos el servicio solicitado a esta reserva especifica
        self.servicio = servicio
        # almacenamos la cantidad de tiempo que el cliente planea usar el servicio
        self.duracion = duracion
        # le asignamos por defecto un estado inicial pendiente
        self.estado = "PENDIENTE"
    