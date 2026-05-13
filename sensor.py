import os
import csv
from datetime import datetime

# CONFIGURACIÓ: Posa aquí el TEU ID de sensor que has trobat abans
SENSOR_ID = "28-xxxxxxx" 
SENSOR_PATH = f"/sys/bus/w1/devices/{SENSOR_ID}/w1_slave"
FILE_NAME = "dades_temperatura.csv"

def llegir_temp_real():
    try:
        with open(SENSOR_PATH, "r") as f:
            lines = f.readlines()
            # Busquem la temperatura al final de la segona línia
            temp_line = lines[1].find("t=")
            if temp_line != -1:
                temp_string = lines[1][temp_line+2:]
                return float(temp_string) / 1000.0
    except Exception as e:
        print(f"Error llegint el sensor: {e}")
        return None

def desar_dades():
    temp = llegir_temp_real()
    if temp is not None:
        ara = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        existeix = os.path.isfile(FILE_NAME)
        
        with open(FILE_NAME, mode='a', newline='') as f:
            writer = csv.writer(f)
            if not existeix:
                writer.writerow(["Data i Hora", "Temperatura (C)"])
            writer.writerow([ara, round(temp, 2)])
        print(f"Dada real guardada: {temp}ºC a les {ara}")

if __name__ == "__main__":
    desar_dades()
