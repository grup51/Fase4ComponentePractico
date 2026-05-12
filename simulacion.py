# simulacion de las 10 operaciones
# aqui defino la funcion principal que sirve como el punto de entrada para ejecutar todo nuestro sistema de gestion
def iniciar_software():
    # imprimimos el encabezado para darle una bienvenida visual al usuario
    print("   SOFTWARE FJ - SISTEMA DE GESTIÓN INTEGRAL         ")
    

    # Creamos un diccionario de servicios
    servicios_fj = {
        "SALA": ReservaSalas("Sala Executive", 60000),
        "PC": AlquilerEquipos("Workstation Dell", 20000),
        "DEV": AsesoriaEspecializada("Arquitectura Software", 150000)
    }
# inicializamos una lista vacia para guardar a los clientes que pasen las reglas de registro
    clientes_validados = []
    
    try: # implementamos una estructura de control de excepciones
        # creamos un nuevo objeto de la clase Cliente y lo agregamos a nuestra lista
        clientes_validados.append(Cliente("Carlos Ruiz", "CR8899")) 
        clientes_validados.append(Cliente("Ana Maria", "AM7744"))
        # si al crear los clientes ocurre un fallo de validacion atrapamos esa excepcion
    except ErrorDeNegocio as e:
        # generamos una notificacion de error en la configuracion utilizando el mensaje guardado en la variable {e}
        print(f"Error en configuración inicial: {e}")

    # Preparamos una lista de tareas pendientes donde organizamos todas las pruebas que queremos que el software ejecute
    operaciones = [
        # reserva de sala primera prueba caso de exito donde todo deberia salir bien
        lambda: Reserva(clientes_validados[0], servicios_fj["SALA"], 4).procesar_confirmacion(),
        
        # aqui forzamos una excepcion controlada enviando una duracion negativa
        lambda: Reserva(clientes_validados[0], servicios_fj["PC"], -1).procesar_confirmacion(),
        
        # en esta prueba ejecutamos un caso de exito polimorfico
        lambda: Reserva(clientes_validados[1], servicios_fj["PC"], 3).procesar_confirmacion(),
        
        # ponemos a prueba el modulo de restricciones al intentar reservar 15 horas
        lambda: Reserva(clientes_validados[1], servicios_fj["SALA"], 15).procesar_confirmacion(),
        
        # el sistema identifica que el objeto es una asesoria y aplica un recargo del 10%
        lambda: Reserva(clientes_validados[0], servicios_fj["DEV"], 2).procesar_confirmacion(),
        
        # error de cliente nombre invalido muy corto
        lambda: Cliente("Ed", "0000"),
        
        # error de encadenamiento id con caracteres prohibidos
        lambda: Cliente("Roberto", "ID_#$_ERROR"),
        
        # simulacion de calculo inconsistente division por cero
        lambda: 10 / 0,
        
        # servicio no disponible o nulo envia un valor None en lugar de un servicio real
        lambda: Reserva(clientes_validados[0], None, 5).procesar_confirmacion(),
        
        # demostracion de estabilidad tras error grave
        lambda: Reserva(clientes_validados[1], servicios_fj["SALA"], 2).procesar_confirmacion()
    ]