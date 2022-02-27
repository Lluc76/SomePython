"""
Crea un programa que pregunte 10 números y determina cual és el más grande de los 10
"""

num_user = []

while len(num_user) < 10:
    num_user.append(input("Introduce un número: "))

bigger_num = max(num_user)

print(bigger_num)