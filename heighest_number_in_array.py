"""
Crea un programa que a muestre el número más grande de un array sin usar max()
"""

lista = [2, 80, 321, 12, 94, 3, 56, 445, 76]

biggest_num = 0
for num in lista:
    if num > biggest_num:
        biggest_num = num

print(biggest_num)