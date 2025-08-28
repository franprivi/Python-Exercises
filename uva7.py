# uva7.py

def promedio(notaAnual):
    if len(notaAnual) == 0:
        return 0
    return sum(notaAnual) / len(notaAnual)

listainfo= []
listavacia= [] 
legajo=int(input("Ingrese el legajo (0 para salir): "))
while legajo!=0:
    nombre=input("Ingrese el nombre: ")
    while nombre == "":
        nombre=input("El nombre no puede estar vacío. Ingrese el nombre: ")
    listainfo.append(nombre)
    apellido=input("Ingrese el apellido: ")
    while apellido == "":
        apellido=input("El apellido no puede estar vacío. Ingrese el apellido: ")
    listainfo.append(apellido)
    edad=int(input("Ingrese la edad: "))
    while edad <= 0 and edad > 100:
        edad=int(input("La edad debe ser mayor a 0. Ingrese la edad: "))
    listainfo.append(edad)
    notaAnual=int(input("Ingrese la nota anual: "))
    while notaAnual < 0 or notaAnual > 10:
        notaAnual=int(input("La nota anual debe estar entre 0 y 10. Ingrese la nota anual: "))
    listavacia.append(( notaAnual))
    legajo=int(input("Ingrese el legajo (0 para salir): "))

notalta=max(listavacia)
NotaBaja = min(listavacia)

print("el promedio de las notas son: ", promedio(listavacia))
print("la informacion de los alumnos es: ", listainfo)
print("la nota mayor es: ", notalta)
print("la nota menor es: ", NotaBaja)
print("el total de alumnos es: ", len(listavacia))

