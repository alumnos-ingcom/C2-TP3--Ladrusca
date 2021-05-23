################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero

def prueba():

    num = ingreso_entero()

    print("Es Primo: ", comprobacion_primo(num))


def comprobacion_primo(num):

    if num > 1:

        for dividendo in range(2, num-1):

            if num % dividendo == 0:
                return False

        return True

    return False
        

if __name__ == '__main__':
    prueba()