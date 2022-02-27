"""
Crea un programa que muestre por pantalla la tabla de multiplicar introducida por el usuario del 5 al 15
"""

n_tabla = int(input("Introduce un número: "))

for num in range(5,16):
    print("{} x {} = {}".format(n_tabla, num,n_tabla * num))
