"""
Crea un programa que pregunte 5 números y determina cual és el más pequeño de los 5
"""

num_user = []

while len(num_user) < 5:
    num_user.append(input("Introduce un número: "))

print(num_user)

print("El número más pequeño es: " + min(num_user))