from servicios import (
   readdata, createstudent, actualizar_estudiante, eliminar_estudiante
)
from archivos import guardarJSON, exportarCSV
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=" * 50)
    print("        SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 50)

    print("""
    1. Leer estudiantes
    2. Guardar datos en JSON
    3. Crear estudiante
    4. Actualizar estudiante
    5. Eliminar estudiante
    6. Exportar CSV
    7. Salir
    """)

    print("-" * 50)


# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------
limpiar()
while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ").strip().lower()

    limpiar()

    if opcion in ["1", "leer", "leerdatos"]:
        print("===== LISTA DE ESTUDIANTES =====")
        readdata()

    elif opcion in ["2", "guardar", "json", "guardardatos"]:
        print("Guardando datos...")
        guardarJSON()

    elif opcion in ["3", "crear", "crearestudiante"]:
        print("===== CREAR ESTUDIANTE =====")
        createstudent()

    elif opcion in ["4", "actualizar", "actualizardatos"]:
        print("===== ACTUALIZAR ESTUDIANTE =====")
        actualizar_estudiante()

    elif opcion in ["5", "eliminar", "eliminardatos"]:
        print("===== ELIMINAR ESTUDIANTE =====")
        eliminar_estudiante()

    elif opcion in ["6", "csv", "exportarcsv"]:
        print("Exportando CSV...")
        exportarCSV()

    elif opcion in ["7", "salir"]:
        print("Saliendo del sistema... ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intente nuevamente.")

    input("\nPresione ENTER para continuar...")
    limpiar()
