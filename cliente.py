from excepciones import ErrorDeNegocio
from abc import ABC, abstractmethod
class EntidadGeneral(ABC):
    @abstractmethod
    def obtener_identificacion(self):
        pass

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
