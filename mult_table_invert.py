"""
Crea un programa que muestre por pantalla la tabla de multiplicar del número introducido por el usuario de forma invertida
"""

n_tabla = int(input("Introduce un número: "))
table = []
for num in range(1,11):
    table.insert(0,num)

for num in table:
    print("{} x {} = {}".format(n_tabla, num, n_tabla * num))

