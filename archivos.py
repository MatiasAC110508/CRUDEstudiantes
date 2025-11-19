import os
import json
import csv
from servicios import estudiantes

def guardarJSON(nombreArchivo="estudiantes.json"):
    os.makedirs("Datos", exist_ok=True)
    rutaJson = os.path.join("Datos", nombreArchivo)

    with open(rutaJson, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)

    print("JSON creado en:", rutaJson)


def exportarCSV(nombreArchivo="estudiantes.csv"):
    if not estudiantes:
        print("No hay estudiantes para exportar.")
        return

    os.makedirs("Datos", exist_ok=True)
    rutaCsv = os.path.join("Datos", nombreArchivo)

    with open(rutaCsv, "w", newline='', encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=estudiantes[0].keys())
        writer.writeheader()
        writer.writerows(estudiantes)

    print("CSV creado en:", rutaCsv)
