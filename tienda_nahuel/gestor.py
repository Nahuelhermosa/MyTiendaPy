import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data")

def cargar_json(nombre_archivo):
    ruta = os.path.join(DATA_PATH, nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_json(nombre_archivo, data):
    ruta = os.path.join(DATA_PATH, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
