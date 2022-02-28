"""
Crea un programa que pregunte 5 números y determina cual és el más grande de los 5
"""

num_user = []

while len(num_user) < 5:
    num_user.append(input("Introduce un número: "))

bigger_num = max(num_user)

print("The bigger number is: " + bigger_num)