lista1 = ["club", "grande"]
lista2 = ["El", "mas", "es", "River", "Plate"]
listaFinal = []


if len(lista1) >= len(lista2):
    primera = lista1
    segunda = lista2
else:
    primera = lista2
    segunda = lista1

min_len = min(len(primera), len(segunda))


for i in range(min_len):
    listaFinal.append(primera[i])
    listaFinal.append(segunda[i])

for i in range(min_len, len(primera)):
    listaFinal.append(primera[i])
for i in range(min_len, len(segunda)):
    listaFinal.append(segunda[i])

print("Lista que queda:", listaFinal)