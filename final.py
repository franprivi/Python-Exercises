
#aqui defino mi funcion para poder calcular el porcentaje de corredores con riesgo de salud
def porcentaje_riesgo_salud(listaRiesgoSalud):
    total_corredores = len(listaRiesgoSalud)
    if total_corredores == 0:
        return 0
    contador_salud = 0
    for i in listaRiesgoSalud:
        if i.lower() == "si":  
            contador_salud += 1
    return (contador_salud / total_corredores) * 100
#aqui defino mi función para determinar el tipo de carrera con más inscriptos
def distancia_mas_repetida(listaTipoCarrera):
    cant_5 = 0
    cant_10 = 0
    cant_21 = 0
    for d in listaTipoCarrera:
        if d == 5:
            cant_5 += 1
        elif d == 10:
            cant_10 += 1
        elif d == 21:
            cant_21 += 1

    if cant_5 >= cant_10 and cant_5 >= cant_21:
        return 5
    elif cant_10 >= cant_5 and cant_10 >= cant_21:
        return 10
    else:
        return 21

# Definición de funciones para calcular la edad máxima y mínima
def edad_maxima(listaEDAD):
    if not listaEDAD:
        return None

    mayor = listaEDAD[0]  
    for edad in listaEDAD:
        if edad > mayor:
            mayor = edad
    return mayor

def edad_minima(listaEDAD):
    if not listaEDAD:
        return None

    menor = listaEDAD[0]  
    for edad in listaEDAD:
        if edad < menor:
            menor = edad
    return menor

# Definición mis listas para guardar la información de los corredores
listaEDAD = []
listaRiesgoSalud = []
listaTipoCarrera = []
listaInformacion = []

id_Corredorr=int(input("Ingrese el numeroro de participante (0000 SIN COMILLAS para finalizar): "))
while id_Corredorr != 0000:

    nombre = input("Ingrese el nombre del corredor: ")
    while nombre =="":
        print("El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")
        nombre = input("Ingrese el nombre del corredor: ")

    listaInformacion.append(nombre)

    apellido = input("Ingrese el apellido del corredor: ")    
    while apellido == "":
        print("El apellido no puede estar vacío. Por favor, ingrese un apellido válido.")
        apellido = input("Ingrese el apellido del corredor: ")
        
    listaInformacion.append(apellido)

    edad = int(input("Ingrese la edad del corredor: "))
    while edad <= 0:
        print("La edad debe ser un número positivo. Por favor, ingrese una edad válida.")
        edad = int(input("Ingrese la edad del corredor: "))
        
    listaEDAD.append(edad)
        
    tipoCarrera = int(input("Ingrese el tipo de carrera (5, 10 ó 21): "))
    while tipoCarrera != 5 and tipoCarrera != 10 and tipoCarrera != 21:
        print("El tipo de carrera debe ser 5, 10 o 21. Por favor, ingrese un valor válido.")
        tipoCarrera = int(input("Ingrese el tipo de carrera (5, 10 ó 21): ")) 

    listaTipoCarrera.append(tipoCarrera)
    
    riesgoSalud = input("¿Tiene riesgo de salud? (si o no): ") 
    while riesgoSalud.upper() != "SI" and riesgoSalud.upper() != "NO":
        print("La respuesta debe ser SI o NO. Por favor, ingrese una respuesta válida.")
        riesgoSalud = input("¿Tiene riesgo de salud? (si o no): ")
    listaRiesgoSalud.append(riesgoSalud.lower())
    
    id_Corredorr=int(input("Ingrese el numeroro de participante (0000 SIN COMILLAS para finalizar): "))



print(f"la informacion ingresada:")
print("Los corredores ingresados son: ", listaInformacion)
print("Los tipos de carrera ingresados son: ", listaTipoCarrera)
print("La cantidad de corredores ingresados es: ", len(listaEDAD))
print("El porcentaje de corredores con riesgo de salud es: ", porcentaje_riesgo_salud(listaRiesgoSalud))
print("El tipo de carrera con más inscriptos es: ", distancia_mas_repetida(listaTipoCarrera))
print("La edad máxima de los corredores es: ", edad_maxima(listaEDAD))
print("La edad mínima de los corredores es: ", edad_minima(listaEDAD)) 