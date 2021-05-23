################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def prueba():

    num1 = ingreso_entero()
    num2 = ingreso_entero()

    print(f"La division entre {num1} y {num2} da como resultado:")
    print(division_lenta(num1, num2))


def division_lenta(n1, n2):

    num1 = n1
    num2 = n2
    cociente = 0
    resto = 0

    if n1 < 0:
        num1 *= -1
    if n2 < 0:
        num2 *= -1

    while num1 >= num2:

        cociente += 1
        num1 -= num2 

    resto = num1 / num2
    
    if n1 > 0 and n2 > 0:
        pass    
    
    else:
        cociente *= -1
    
    return f"cociente: {cociente} Resto: {resto}"

if __name__ == '__main__':
    prueba()