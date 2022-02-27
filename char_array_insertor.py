"""
Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario
"""

frase_usuario = input("Introduce tu frase: ")
vocales= []

for char in frase_usuario:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        vocales.append(char)

print("Tu frase contiene estas vocales {}".format(vocales))