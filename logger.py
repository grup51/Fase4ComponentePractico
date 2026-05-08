# Función para registrar errores y eventos
# en el archivo logs.txt
from datetime import datetime

def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {mensaje}\n")