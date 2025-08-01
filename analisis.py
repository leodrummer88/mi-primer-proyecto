import pandas as pd
import dtale
import dtale.app as dtale_app

dtale_app.USE_COLAB = True

# Leemos los datos desde el archivo CSV
try:
    df = pd.read_csv('datos.csv')
    print("Archivo datos.csv cargado correctamente.")
    # Mostramos el DataFrame con D-Tale
    dtale.show(df)
except FileNotFoundError:
    print("Error: El archivo datos.csv no se encontró.")
