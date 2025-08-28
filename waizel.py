peso=0
edad=0
ALTURA=0
calorias=0
print("Bienvenido al calculador de gasto calórico basal y macronutrientes.")
print("Por favor, ingrese los siguientes datos para calcular su gasto calórico basal y macronutrientes diarios.")

peso=float(input("Ingrese el peso en kg: "))
if peso < 0:
    print("El peso no puede ser negativo.")
    print("Por favor, ingrese un peso válido.")
    peso=int(input("Ingrese el peso en kg: "))

ALTURA=int(input("Ingrese la altura en cm: "))
if ALTURA < 0:
    print("La altura no puede ser negativa.")
    print("Por favor, ingrese una altura válida.")
    ALTURA=int(input("Ingrese la altura en cm: "))

edad=int(input("Ingrese la edad en años: "))
if edad < 0:
    print("La edad no puede ser negativa.")
    print("Por favor, ingrese una edad válida.")
    edad=int(input("Ingrese la edad en años: "))


calorias=(10 * peso) + (6.25 * ALTURA) - (5 * edad) + 5
print("El gasto calórico basal es de", calorias, "calorías diarias.")

# El código calcula el gasto calórico basal (TMB) de una persona
vago=1.3
ligera=1.55
casimoderada=1.6
moderada=1.78
intensa=2.1
muyintensa=2.4
actividad=input("Ingrese el nivel de actividad física (muyligera, ligera, moderada, intensa, muy intensa): ").lower()
if actividad == "vago":
    calorias *= ligera
elif actividad == "ligera":
    calorias *= ligera
elif actividad=="casimoderada":
    calorias*casimoderada
elif actividad == "moderada":
    calorias *= moderada
elif actividad == "intensa":
    calorias *= intensa
elif actividad == "muy intensa":
    calorias *= muyintensa
else:
    print("Nivel de actividad no reconocido. Se usará el valor base.")
    actividad=input("Ingrese el nivel de actividad física (muy ligera, ligera, moderada, intensa, muy intensa): ").lower()


proteinas=0
proteinas = peso * 2
grasas=0
grasas = peso * 1
carboshidratos=0
carboshidratos = calorias - (proteinas * 4 + grasas * 9)
print("\n=== Resumen de los resultados de los macros: ===")
print("La cantidad de proteínas recomendada es de", proteinas, "gramos diarios.")
print("La cantidad de grasas recomendada es de", grasas, "gramos diarios.")
print("La cantidad de carbohidratos recomendada es de", carboshidratos/4, "gramos diarios.")

print("\n=== Resumen de los resultados pasados en calorias: ===")
print("Gasto calórico basal:", calorias, "calorías")
print("Proteínas:", proteinas*4, "calorias")   
print("Grasas:", grasas*9, "calorias")
print("Carbohidratos:", carboshidratos, "calorias")

print("\n=== Recomendaciones de calorías según objetivos: ===")
print("Para el caso de querer perder peso, se recomienda un déficit de 300 o 500 calorías diarias que serian: ", calorias - 300, "calorías o", calorias - 500, "calorías respectivamente.")
print("Para el caso de querer ganar peso, se recomienda un superávit de 300 o 500 calorías diarias que serian: ", calorias + 500, "calorías.")
print("Para el caso de querer mantener el peso, se recomienda consumir las calorías calculadas: ", calorias, "calorías.")


