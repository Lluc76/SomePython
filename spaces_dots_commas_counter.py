"""
Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario
"""

frase_usuario = input("Introduce tu frase: ")
n_space = 0
n_dot = 0
n_comma = 0

for char in frase_usuario:
    if char == " ":
        n_space += 1
    if char == ".":
        n_dot += 1
    if char == ",":
        n_comma += 1

print("Tu frase contiene {} espacios, {} puntos y {} comas".format(n_space,n_dot,n_comma))