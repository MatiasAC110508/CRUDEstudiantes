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



