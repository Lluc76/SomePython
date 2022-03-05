"""
Crea una función que devuelva el número más grande entre 3
"""

def bigger_num(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1

    if (num2 > num1 and num2 > num3):
        return num2

    if (num3 > num1 and num3 > num2):
        return num3

print(bigger_num(2, 82, 45))