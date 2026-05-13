import logging # Importamos la libreria para llevar el registro de lo que pasa en el sistema
#  Registro de errores y eventos 
# en el archivo errores_programa
logging.basicConfig(
    filename='errores_programa.log', # Nombre del archivo donde se guardará todo
    level=logging.INFO, # registra cada movimiento importante
    format='%(asctime)s - %(levelname)s - %(message)s' # la estructura que debe llevar
)