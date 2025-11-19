import servicios


print("<------ESTUDIANTES----->")
print("<-----Ingrese la opción que desea---->\n 1.Leer datos\n 2.Guardar datos\n 3.Crear estudiante\n" \
" 4.Actualizar datos\n 5.Eliminar datos\n 6.Salir ")

student= input("Ingrese la opcion que desea ingresar ").replace(" ","").lower()
check=True

try:
    while check:

        if student=="leerdatos" or student=="1":
            servicios.readdata()
            

        if student=="guardardatos" or student=="2":
            print("guardado")
            

        elif student=="crearestudiante" or student=="3":
            createstudent()
            print("creado")
            

        elif student=="actualizardatos" or student=="4":
            actualizar_estudiante()
            print("actualizar")
            

        elif student=="eliminardatos" or student=="5":
            eliminar_estudiante()
            print("eliminado")
            

        elif student=="salir" or student=="6":       
            print("salir")
            break
            

        else:
            print("No se encontro la información solicitada ")
        student= input("Ingrese la opcion que desea ingresar ").replace(" ","").lower()

            
except SyntaxError:
        print("Fallo el programa ")
