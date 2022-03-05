"""
Crea un programa que cambie todas las "A" o "a" por la string "VACA" de una string introducida por el usuario
"""

string = input("Introduce una frase: ")

string = string.replace("A", "VACA")

string = string.replace("a", "VACA")

print(string)