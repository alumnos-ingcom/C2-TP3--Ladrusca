################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def compara(num1, num2):

    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1
        

    
def prueba():

    numero = ingreso_entero(input("Ingrese el primer numero: "))
    
    otro_numero = ingreso_entero(input("Ingrese el segundo numero: "))

    print(compara(numero, otro_numero))


if __name__ == '__main__':
    prueba()