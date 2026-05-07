def registrar_log(mensaje):
    with open("logs.txt", "a") as f:
        f.write(mensaje + "\n")