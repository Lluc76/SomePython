"""
Crea un programa que compruebe la longitud de una lista
"""

numeros = [2,3,6,4,46,4,9,4,8,7,6,5,6,4,7,6,5,4,7,6,5,8,4,8,5,78,5,87,5,7,45]

contador = 0

for num in numeros:
    contador += 1

print("En la lista hay {} número/s".format(contador))

