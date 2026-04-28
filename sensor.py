import csv
import random
from datetime import datetime
import os

# Configuración: Nombre del archivo donde se guardarán los datos
FILE_NAME = "dades_temperatura.csv"

def llegir_sensor_simulat():
    # El sensor real DS18B20 tiene un rango de -55 a 125. 
    # Simulamos una temperatura lógica de interior.
    return round(random.uniform(18.0, 26.0), 2)

def desar_dades():
    data_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperatura = llegir_sensor_simulat()
    
    # Comprobar si el archivo existe para escribir la cabecera la primera vez
    file_exists = os.path.isfile(FILE_NAME)
    
    with open(FILE_NAME, mode='a', newline='') as fitxer:
        writer = csv.writer(fitxer)
        if not file_exists:
            writer.writerow(["Data i Hora", "Temperatura (C)"])
        writer.writerow([data_actual, temperatura])
    
    print(f"[{data_actual}] Dada guardada correctament: {temperatura}°C")

if __name__ == "__main__":
    desar_dades()
