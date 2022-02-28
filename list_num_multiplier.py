"""
Crea un programa que a partir de un array con ints te devuelva el resultado de la multiplicación entre todos ellos
"""

numeros = [2,9,35,75,99]
resultado = 1

for num in numeros:
    resultado *= num

print(resultado)