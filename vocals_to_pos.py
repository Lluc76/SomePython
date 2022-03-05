"""
Crea un programa que cambie todas las vocales por su numero de aparición
"""

string = input("Escribe tu frase: ")
vocals = ["A","E","I","O","U","a","e","i","o","u"]
vocal_pos = []
counter = 0

for i in string:
    counter += 1
    if i in vocals:
        vocal_pos.append(counter)

counter = 0
for i in vocal_pos:
    string = string.replace(str(i), str(counter))
    counter += 1

print(vocal_pos)
print(string)