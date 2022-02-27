"""
Crea un programa que sea capaz de contar la cantidad de letras mayúsculas en una string introducida por el usuario
"""

frase_usuario = input("Introduce tu frase: ")
n_mayus = 0
for char in frase_usuario:
    if char.isupper():
        n_mayus += 1

print("Tu frase contiene {} letras mayúsculas".format(n_mayus))