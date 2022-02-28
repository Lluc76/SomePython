"""
Crea un programa que compruebe el tipo de dato de un valor y lo meta en un array
"""

lista_datos = [1, 2, 3, "hello", False, [], True, 23, 2.1]

data_type = []

for data in lista_datos:
    data_type.append(type(data))

print(data_type)