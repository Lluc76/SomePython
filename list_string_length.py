"""
Crea un programa que a partir de un array con strings te devuelva una lista con el largo de cada string
"""

array = ["buenos dias", "pepinillos con aguacate", "Jesús te bendiga"]
string_length = []

for string in array:
    string_length.append(len(string))

print(string_length)