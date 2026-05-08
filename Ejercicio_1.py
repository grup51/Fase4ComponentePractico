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