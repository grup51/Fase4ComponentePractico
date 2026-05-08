# Menu interactivo para gestionar clientes, servicios y reservas
from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva
from simulacion import ejecutar_simulacion
from logger import registrar_log

# Listas para almacenar información de clientes, servicios y reservas
clientes = []
servicios = []
reservas = []

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear cliente")
        print("2. Crear servicio")
        print("3. Crear reserva")
        print("4. Ejecutar simulación")
        print("5. Salir")

        opcion = input("Seleccione: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                cliente = Cliente(nombre, correo)
                clientes.append(cliente)
                print("Cliente creado")

            elif opcion == "2":
                nombre = input("Servicio: ")
                precio = float(input("Precio: "))
                servicio = ReservaSala(nombre, precio)
                servicios.append(servicio)
                print("Servicio creado")

            elif opcion == "3":
                if not clientes or not servicios:
                    raise Exception("Debe crear cliente y servicio primero")

                reserva = Reserva(clientes[0], servicios[0], 2)
                print("Costo:", reserva.confirmar())
                reservas.append(reserva)

            elif opcion == "4":
                ejecutar_simulacion()

            elif opcion == "5":
                break

        except Exception as e:
            registrar_log(str(e))
            print("Error:", e)

if __name__ == "__main__":
    menu()