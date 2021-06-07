################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):

    num1 = dividendo
    num2 = divisor
    cociente = 0
    resto = 0

    if dividendo < 0:
        num1 *= -1
    if divisor < 0:
        num2 *= -1

    while num1 >= num2:

        cociente += 1
        num1 -= num2 


    resto = num1 / num2
    
    if dividendo > 0 and divisor > 0:
        pass    
    
    else:
        cociente *= -1
    
    result = (cociente, resto)
    return result


def prueba():

    num1 = ingreso_entero(input("Ingrese un entero: "))
    num2 = ingreso_entero(input("Ingrese un entero: "))

    print(f"La division entre {num1} y",
        f"{num2} da como resultado:"
    )

    resultado = division_lenta(num1, num2)
    print("cociente:",resultado[0],
        "resto:",resultado[1]
    )


if __name__ == '__main__':
    prueba()