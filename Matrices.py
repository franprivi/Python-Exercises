
from random import randint

def crearTablero(n):
    tablero = []
    for f in range(n):
        fila_lista = []
        for c in range(n):
            fila_lista.append(' ')
        tablero.append(fila_lista)
    return tablero

def colocarTesoro(tablero, tesoro):
    n = len(tablero)
    fila_aleatoria = randint(0, n-1)
    columna_aleatoria = randint(0, n-1)
    tablero[fila_aleatoria][columna_aleatoria] = tesoro


print("------------------------------------")
print("--  Juego de Búsqueda del Tesoro  --")
print("------------------------------------")


n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
while n <= 0:
    print("El tamaño de la matriz debe ser un número positivo.")
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

tablero = crearTablero(n)
colocarTesoro(tablero, "tesoro")


fila = int(input(f"Ingrese la fila donde buscar el tesoro (0 a {n-1}): "))
columna = int(input(f"Ingrese la columna donde buscar el tesoro (0 a {n-1}): "))
intentos = 0

while tablero[fila][columna] != 'tesoro':
    print(f"No encontraste el tesoro en la posición ({fila}, {columna}). Intenta de nuevo.")
    fila = int(input(f"Ingrese la fila donde buscar el tesoro (0 a {n-1}): "))
    columna = int(input(f"Ingrese la columna donde buscar el tesoro (0 a {n-1}): "))
    intentos += 1

print(f" ¡Felicitaciones! Has encontrado el tesoro. ({fila}, {columna}).")
print(f"Total de intentos: {intentos + 1}")

