# servicios.py
estudiantes = []

def readdata():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for est in estudiantes:
        print(f"ID: {est['id']}  NOMBRE: {est['nombre']}  APELLIDO: {est['apellido']}")

def createstudent():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    dicstudent = {
        "id": len(estudiantes) + 1,
        "nombre": nombre,
        "apellido": apellido
    }

    estudiantes.append(dicstudent)
    print("Estudiante creado exitosamente.")
    return dicstudent

def eliminar_estudiante():
    if not estudiantes:
        print("No hay estudiantes por eliminar.")
        return

    try:
        id_buscar = int(input("Ingrese el ID del estudiante a eliminar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    for i, est in enumerate(estudiantes):
        if est["id"] == id_buscar:
            estudiantes.pop(i)
            print("Estudiante eliminado exitosamente.")
            return

    print("No se encontró un estudiante con ese ID.")

def actualizar_estudiante():
    if not estudiantes:
        print("No hay estudiantes para actualizar.")
        return

    try:
        id_input = int(input("Ingresa el ID del estudiante a actualizar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    estudiante = next((e for e in estudiantes if e['id'] == id_input), None)

    if estudiante is None:
        print("Estudiante no encontrado.")
        return

    print(f"Estudiante actual: {estudiante['nombre']} {estudiante['apellido']}")

    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_apellido = input("Nuevo apellido: ")

    estudiante['nombre'] = nuevo_nombre
    estudiante['apellido'] = nuevo_apellido

    print("Estudiante actualizado exitosamente!")
