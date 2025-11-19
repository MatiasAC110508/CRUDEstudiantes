def eliminar_estudiante():
    

    if not estudiantes:
        print("No hay estudiantes por eliminar.")
        return

    try:
        id_buscar = int(input("Ingrese el ID del estudiante a eliminar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    # Buscar estudiante por ID
    indice_encontrado = None

    for i,est in enumerate (estudiantes):
        if est["id"] == id_buscar:
            indice_encontrado = i
            break
            
    if indice_encontrado is not None:
        estudiantes.pop(indice_encontrado)
        print("Estudiante eliminado exitosamente.")
    else:
        print("No se encontró un estudiante con ese ID.")













































































def createstudent():
    nombre=input("Ingrese el nombre--->")
    apellido=input("Ingrese el apellido ")

    dicstudent={"Id":len(student)+1,
                "Nombre":nombre,
                "Apellido":apellido}  
    student.append(dicstudent)

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
