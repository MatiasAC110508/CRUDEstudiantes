import json

# Archivo JSON
DATA_FILE = 'data.json'

def actualizar_estudiante(estudiantes, id_input, nuevo_nombre, nuevo_apellido):
    # Cargar datos
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        estudiantes = json.load(file)

    # Pedir ID del estudiante
    id_input = int(input("Ingresa el ID del estudiante a actualizar: "))

    # Buscar estudiante
    estudiante = next((e for e in estudiantes if e['id'] == id_input), None)

    if estudiante is None:
        print("Estudiante no encontrado.")
    else:
        print(f"Estudiante actual: {estudiante['nombre']} {estudiante['apellido']}")

        # Pedir nuevos datos
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")

        # Actualizar datos
        estudiante['nombre'] = nuevo_nombre
        estudiante['apellido'] = nuevo_apellido

        # Guardar cambios
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(estudiantes, file, indent=2, ensure_ascii=False)

        print("Estudiante actualizado exitosamente!")