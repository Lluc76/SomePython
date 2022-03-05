"""
Crea un programa que cambie todas las vocales por i
"""

string = input("Escribe tu frase: ")

vocals = ["A","E","I","O","U","a","e","i","o","u"]

for voc in vocals:
    string = string.replace(voc, "i")

print(string)