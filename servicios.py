
estudiantes=[{"id":1, "nombre":"Robinson","apellido":"Urrego"},
             {"id":2, "nombre":"juan","apellido":"perez"} ] # type: ignore

def readdata(estudiantes):
    for read in estudiantes:
        print (f"ID {read["id"]} NOMBRE {read["nombre"]} APELLIDO {read ["apellido"]}")

readdata(estudiantes)



