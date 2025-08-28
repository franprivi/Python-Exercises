from collections import Counter
from random import randint

def titulo(texto, longitud):
    print('*' * longitud)
    print(texto.center(longitud))
    print('*' * longitud)

# Programa principal
if __name__ == "__main__":
    titulo("Aprendiendo Funciones", 30)

""""
titulo("Meses del Año", 30)
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]
def obtener_mes_texto(mes_numero):
    if 1 <= mes_numero <= 12:
        return meses[mes_numero - 1]
    else:
        return "Número de mes inválido"
intento = int(input("Ingrese un número de mes (1-12): "))
mes_texto = obtener_mes_texto(intento)
print(f"El mes correspondiente al número {intento} es: {mes_texto}")
"""
"""
def descuento(precio, porcentaje):
    if 0 < porcentaje<31:
        return  precio - (precio * porcentaje / 100)
    else:
        print("El porcentaje de descuento debe estar entre 0 y 30.")
        porcentaje = float(input("Ingrese un porcentaje válido (0-30): "))
        return precio - (precio * porcentaje / 100)
def cargo(precio, porcentaje):
    if  0 < porcentaje < 31: 
        return  precio + (precio * porcentaje / 100)
    else:
        print("El porcentaje de descuento debe estar entre 0 y 30.")
        porcentaje = float(input("Ingrese un porcentaje válido (0-30): "))
    return precio + (precio * porcentaje / 100)

# Programa principal para calcular precios con descuento y cargo
precio=float(input("Ingrese el precio del producto (-1 para salir): "))
while precio != -1:
    if precio < 0:
        print("El precio no puede ser negativo. Intente de nuevo.")
        precio = float(input("Ingrese el precio del producto (-1 para salir): "))
    print("Seleccione una opción:")
    print("1. Aplicar descuento")
    print("2. Aplicar cargo")
    opcion = input("Ingrese 1 o 2: ")
    if opcion == '1':
        porcentaje = float(input("Ingrese el porcentaje de descuento (0-30): "))
        precio_final = descuento(precio, porcentaje)
        print(f"El precio final con descuento es: {precio_final:.2f}")
    elif opcion == '2':
        porcentaje = float(input("Ingrese el porcentaje de cargo (0-30): "))
        precio_final = cargo(precio, porcentaje)
        print(f"El precio final con cargo es: {precio_final:.2f}")
    else:
        print("Opción no válida. Intente de nuevo.")
    precio = float(input("Ingrese el precio del producto (-1 para salir): "))
# Fin del programa principal

"""
"""
titulo("metros cuadrados", 30)
def metros_cuadrados(superficie,valor,ambientes):
    if ambientes==1:
        total = superficie * valor * 1.2
    elif ambientes==2 or ambientes==3:
        total = superficie * valor * 1.1
    else:
        total = superficie * valor
    
    return f"El total a pagar por {superficie} metros cuadrados es: {total:.2f} pesos."
# Programa principal para calcular el total a pagar por metros cuadrados
precios_3_ambientes =[]
precio_maximo = 0
for i in range(5):
    print(f"Ingreso de datos para la propiedad {i + 1}:")
    
    superficie = 0
    while superficie <= 0:
        superficie = float(input("Ingrese la superficie en metros cuadrados: "))
        if superficie <= 0:
            print("La superficie debe ser mayor que cero. Intente de nuevo.")

    valor = 0
    while valor <= 0:
        valor = float(input("Ingrese el valor por metro cuadrado: "))
        if valor <= 0:
            print("El valor por metro cuadrado debe ser mayor que cero. Intente de nuevo.")    

    ambientes = 0
    while ambientes<=0:
        ambientes = int(input("Ingrese la cantidad de ambientes: "))
        if ambientes <= 0:
            print("La cantidad de ambientes no puede ser menor a 0. Intente de nuevo.")

    resultado = metros_cuadrados(superficie, valor, ambientes)
    print(resultado)
    if ambientes == 3:
        precios_3_ambientes.append(resultado)
    if precio_maximo < valor:
        precio_maximo = valor

if precios_3_ambientes:
    promedio = sum(precios_3_ambientes) / len(precios_3_ambientes)
    print(f"El promedio de precios de propiedades con 3 ambientes es: {promedio:.2f} pesos.")
else:
    print("No se ingresaron propiedades con 3 ambientes.")

print(f"el precio del depto mas caro es: {precio_maximo:.2f} pesos.")
"""
"""
titulo("Puntaje de Cartas", 30)
def puntaje_cartas(cartas):
    conteo = Counter(cartas)
    if len(conteo) == 1:
        return 10  # Tres números iguales
    elif len(conteo) == 2:
        return 4   # Dos números iguales y uno distinto
    elif len(conteo) == 3:
        return 7   # Tres números distintos
    else:
        return 0
    
cartas = []
puntaje = 0
for i in range(5):
    cartas = [randint(1, 3) for _ in range(3)]
    puntaje = puntaje_cartas(cartas)
    print(f"Jugada {i+1}: Números: {cartas} - Puntaje: {puntaje}")
    total = puntaje if i == 0 else total + puntaje

print(f"Total de puntos acumulados: {total}")
# Fin del programa de puntaje de cartas 
"""
