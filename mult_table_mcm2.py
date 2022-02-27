"""
Crea un programa que muestre por pantalla la tabla de multiplicar del número introducido por el usuario que sean múltiplos de 2
"""

n_tabla = int(input("Introduce un número: "))

for num in range(1,10):
    if (n_tabla * num % 2) == 0:
        print("{} x {} = {}".format(n_tabla, num, n_tabla * num))