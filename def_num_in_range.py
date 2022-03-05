"""
Crea una función que devuelva true si el número está dentro de un rango
"""

def numero_en_rango(num, range1, range2):
    if num >= range1 and num <= range2:
        return True

    if num < range1 or num > range2:
        return False

print(numero_en_rango(50, 40, 100))