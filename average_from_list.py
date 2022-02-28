"""
Crea un programa que calcule el promedio de los valores de una lista
"""

numeros = [2,7,4,89,4,7,34,6,3,6,3,6,4,6,65,3,6,4,6,4,6,45,7,5,7,898,98,8,7,6,5,3,3]

suma_total = 0
contador = 0

for num in numeros:
    suma_total += num
    contador += 1

promedio = suma_total / contador

print("El promedio es: {}".format(promedio))