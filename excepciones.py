# Definición de errores propios para que el sistema no se bloquee
class Falla_Sistema(Exception): # definimos errores propios para que el programa no se cierre de golpe
    pass

class ErrorDeNegocio(Falla_Sistema):
    """Excepción para reglas de negocio incumplidas."""
    pass