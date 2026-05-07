from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_log

def ejecutar_simulacion():
    print("\n--- SIMULACIÓN ---")

    # 1 válido
    try:
        c1 = Cliente("Ana", "ana@mail.com")
    except Exception as e:
        registrar_log(e)

    # 2 inválido
    try:
        c2 = Cliente("", "mal")
    except Exception as e:
        registrar_log(e)

    # 3 servicio válido
    s1 = ReservaSala("Sala", 50)

    # 4 servicio inválido
    try:
        s2 = AlquilerEquipo("Equipo", -10)
    except Exception as e:
        registrar_log(e)

    # 5 reserva válida
    try:
        r1 = Reserva(c1, s1, 2)
        print("Costo:", r1.confirmar())
    except Exception as e:
        registrar_log(e)

    # 6 reserva inválida
    try:
        r2 = Reserva(c1, s1, -1)
        r2.confirmar()
    except Exception as e:
        registrar_log(e)

    # 7 asesoría válida
    try:
        s3 = Asesoria("Consultoría", 100)
        r3 = Reserva(c1, s3, 3)
        print("Costo asesoría:", r3.confirmar())
    except Exception as e:
        registrar_log(e)

    # 8 cliente inválido correo
    try:
        Cliente("Luis", "correo")
    except Exception as e:
        registrar_log(e)

    # 9 cancelación
    r1.cancelar()
    print("Reserva cancelada")

    # 10 otra válida
    try:
        r4 = Reserva(c1, s1, 1)
        print("Costo:", r4.confirmar())
    except Exception as e:
        registrar_log(e)