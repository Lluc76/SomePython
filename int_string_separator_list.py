"""
Crea un programa que a partir de un array con ints y strings te separe en 2 arrays segun el tipo de dato
"""

datos = ["hola", 54, 976, "No!!!"]

numeros = []
strings = []

for dato in datos:
    if isinstance(dato, str):
        strings.append(dato)
    elif isinstance(dato, int):
        numeros.append(dato)

print("La lista numeros contiene: {}".format(numeros))
print("La lista strings contiene: {}".format(strings))