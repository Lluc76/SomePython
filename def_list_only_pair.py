"""
Crea una función que reciba una lista de números y devuelva sólo los pares
"""

def devolver_pares(array):
    final_array = []
    for num in array:
        if num % 2 == 0:
            final_array.append(num)

    return final_array

print(devolver_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))