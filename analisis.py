import pandas as pd
from ydata_profiling import ProfileReport
import sys

def generar_reporte(archivo_csv, archivo_html):
    """
    Lee un archivo CSV y genera un reporte de perfil de datos en HTML.
    """
    try:
        print(f"Cargando datos desde '{archivo_csv}'...")
        df = pd.read_csv(archivo_csv)
        print("Datos cargados. Generando reporte...")
        
        profile = ProfileReport(df, title=f"Reporte de Datos - {archivo_csv}")
        
        profile.to_file(archivo_html)
        print(f"Reporte generado y guardado como '{archivo_html}'")
        
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Nombre del archivo CSV de entrada y el archivo HTML de salida
    generar_reporte('datos.csv', 'reporte_estadistico.html')
