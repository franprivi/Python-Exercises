"""
import random

def crear_matriz_azar(n, m, a, b):
    if n <= 0 or m <= 0 or a > b:
        return []  # sigue retornando lista vacía si es inválido
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            valor = random.randint(a, b)
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def suma_filas(matriz):
    return [sum(fila) for fila in matriz]

def suma_columnas(matriz):
    columnas = len(matriz[0])
    return [sum(fila[j] for fila in matriz) for j in range(columnas)]

# Programa principal
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
a = int(input("Ingrese el valor mínimo aleatorio: "))
b = int(input("Ingrese el valor máximo aleatorio: "))

matriz = crear_matriz_azar(filas, columnas, a, b)

if len(matriz) == 0:
    print("Parámetros inválidos. Matriz vacía.")
else:
    print("\nMatriz resultante:")
    mostrar_matriz(matriz)

    print("\nSuma de cada fila:", suma_filas(matriz))
    print("Suma de cada columna:", suma_columnas(matriz))
"""
import random
def numero_mayor(matriz):
    mayor = matriz[0][0]
    for fila in matriz:
        for valor in fila:
            if valor > mayor:
                mayor = valor
    return mayor
matriz =[]
filas= 4
columnas= 4
numero = 1
for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(100, 1000)
            fila.append(valor)
        matriz.append(fila)
print("Matriz:")
for fila in matriz:
    print(fila)
print("El número mayor de la matriz es:", numero_mayor(matriz))