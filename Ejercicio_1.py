
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


    