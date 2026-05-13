from excepciones import ErrorDeNegocio
import logging
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

# definimos una funcion de control para verificar que toda la informacion de la reserva sea valida
    def procesar_confirmacion(self):
        # iniciamos un bloque de prueba para manejar cualquier error
        try:
            # imprimimos un mensaje de seguimiento en consola usando el nombre del cliente
            print(f"[*] Iniciando proceso para {self.cliente.nombre}...")

            # realizamos una validacion de tipo verificamos que el servicio no este vacio
            if not self.servicio or not isinstance(self.servicio, Servicio):
                # si la validacion anterior falla lanzamos una excepcion personalizada para alertar que el servicio es incorrecto
                raise ErrorDeNegocio("Operación denegada: El servicio solicitado no es válido.")
            # verificamos que el parametro de duración cumpla con el requisito obligatorio de ser una cantidad positiva
            if self.duracion <= 0:
                # lanzamos un aviso de error si detectamos que el tiempo ingresado no tiene sentido
                raise ErrorDeNegocio("Reserva incorrecta: La duración debe ser positiva.")
            # llamamos al metodo de calculo para obtener el monto total
            pago_final = self.servicio.calcular_costo(self.duracion)
            # si el calculo anterior funciona actualizamos el estado de la reserva a confirmada
            self.estado = "CONFIRMADA"
            
            # aqui activamos un manejador de excepciones personalizado para atrapar los fallos
        except ErrorDeNegocio as e:
            # guardamos un registro oficial del error
            logging.error(f"Falla de Negocio: {e}")
            # si detectamos una falla de negocio marcamos la reserva como rechazada
            self.estado = "RECHAZADA"
            # le mostramos al usuario un mensaje claro por que su solicitud no pudo completarse
            print(f"   [!] Error Controlado: {e}")
            # revisamos si este error viene encadenado de otro problema
            if e.__cause__:
                # mostramos la falla original que disparo el error
                print(f"   [?] Causa técnica raíz: {e.__cause__}")
        # implementamos un control de fallos general para evitar que el programa se bloquee por completo
        except Exception as e:
            # creamos un registro de auditoria de nivel critico
            logging.critical(f"Falla Crítica de Sistema: {e}")
            # cambiamos el estado para indicar que el problema fue del sistema
            self.estado = "FALLO_TECNICO"
            # emitimos una notificacion de estado estable
            print(f"   [X] Error grave aislado. El programa sigue estable.")
        # este bloque solo se ejecuta si todo salio perfecto y no hubo ninguna falla    
        else:
           # generamos el reporte final de exito mostrando el tipo de servicio el nombre del cliente y el monto total cobrado
            logging.info(f"ÉXITO: {self.servicio.tipo} | Cliente: {self.cliente.nombre} | Pago: ${pago_final}")
            print(f"   [V] {self.estado}: {self.servicio.describir_servicio()}. Total: ${pago_final}")
        
         # finally siempre se ejecuta para asegurar el cierre del proceso    
        finally:
           # imprimimos un mensaje final
            print(f"   [SISTEMA] Registro finalizado. Estado final: {self.estado}\n")


       