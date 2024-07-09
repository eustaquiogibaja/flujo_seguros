import pandas as pd

# Ruta del archivo TXT
archivo_txt = 'Claro_Peru_Asegurados_20022021234238.txt'
data_BD_ORACLE_tabla_asegurados = 'ruta BD'

try:
    # Leer el archivo TXT
    data = pd.read_csv(archivo_txt, delimiter='|')
    data = pd.read_csv(data_BD_ORACLE_tabla_asegurados, delimiter='|')
    
    # Guardar los datos en un archivo CSV temporal
    archivo_csv = 'clientes.csv'
    data.to_csv(archivo_csv, index=False)
    
    print(f"Datos leídos y guardados en {archivo_csv}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
