
student=[]

def readdata():
    for read in student:
        print (f"ID {read["id"]} NOMBRE {read["nombre"]} APELLIDO {read ["apellido"]}")


def createstudent():
    nombre=input("Ingrese el nombre--->")
    apellido=input("Ingrese el apellido ")

    dicstudent={"Id":len(student)+1,
                "Nombre":nombre,
                "Apellido":apellido}  
    student.append(dicstudent)


createstudent()
print(student)





