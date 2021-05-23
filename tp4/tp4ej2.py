################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero

def prueba():
    
    print('num1:')
    num1 = ingreso_entero()
    print('num2:')
    num2 = ingreso_entero()

    print('El resultado es: ', sumaLenta(num1, num2))


def sumaLenta(n1, n2):

    result = n1
    for i in range(abs(n2)):
        
        if n2 < 0:
            result -=1
        else:    
            result += 1

    return result

if __name__ == "__main__":
    prueba()