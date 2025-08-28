"""
def multiplicacion_solosuma(a, b):
    resultado = 0
    for _ in range(abs(b)):
        resultado += abs(a)
    
    if (a < 0) or (b < 0):  
        resultado = -resultado
    return resultado


N = int(input("Ingrese el número de términos de la serie: "))
termino = 1
lista = []
for i in range(1, N + 1):
    lista.append(str(termino))
    termino = multiplicacion_solosuma(termino, i + 1) 
print("", ", ".join(lista))
"""
"""
from random import randint


def multiplicacion_sucesiva(a,b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

n = int(input("Ingrese un número entero positivo: "))
for _ in range(n):
    desde = int(input("Ingrese el valor desde: "))
    hasta = int(input("Ingrese el valor hasta: "))
    a = randint(desde, hasta)
    b = randint(desde, hasta)
    resultado = multiplicacion_sucesiva(a, b)
    print(f"Valores generados: A={a}, B={b} -> A*B={resultado}")

"""
"""
def sumadigitos(numero):
    suma = 0
    while numero > 0:
        suma = suma + numero % 10
        numero=numero// 10
    return suma

def invertir_numero(numero):
    invertido = 0
    while numero > 0:
        invertido = invertido * 10 + numero % 10
        numero = numero // 10
    return invertido

def extraerdigito(numero, digito):
    numero = abs(numero)
    if digito < 0:
        return -1
    for _ in range(digito):
        numero = numero // 10
    if numero == 0:
        return -1
    return numero % 10

from random import randint
while True:
        numero = randint(10000, 99999)
        digito_central = extraerdigito(numero, 2)
        if digito_central == 0:
            print(f"Número generado: {numero}")
            suma1 = sumadigitos(numero)
            suma2 = sum([int(d) for d in str(numero)])
            print(f"Suma de dígitos (usando sumadigitos): {suma1}")
            print(f"Suma de dígitos (usando función interna): {suma2}")
            break
"""
def es_natural(numero):
    if numero > 0 and numero == int(numero):
        return int(numero)
    else:
        return -1
print(es_natural(5.0))  # Debe retornar 5

