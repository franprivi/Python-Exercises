def doble(lista):
    lista_por_dos = []
    for num in lista:
        lista_por_dos.append(num * 2)
    return lista_por_dos
print(doble([1, 2, 3, 4, 5]))

def cantidadEntre(lista, desde,hasta):
    contador = 0
    for num in lista:
        if desde <= num <= hasta:
            contador = contador + 1
    return contador

print(cantidadEntre([1, 2, 3, 4, 5], 2, 4))
def cantNegativos(lista):
    contador = 0
    for num in lista:
        if num < 0:
            contador = contador + 1
    return contador
print(cantNegativos([0, 5, 3, 4, -10]))

def promedio(lista):
    if len(lista) == 0:
        print("Lista vacía")
        return 

    suma = 0
    contador = 0

    for i in range(len(lista)):
        print(f"{i} → {lista[i]}")
        suma = suma +lista[i]
        contador = contador + 1

    print("El promedio es :", suma / contador)
    
print(promedio([5, 7, 8, 9, 4]))
