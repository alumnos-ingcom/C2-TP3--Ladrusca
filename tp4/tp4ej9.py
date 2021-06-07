################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero


def es_primo(numero):

    if numero > 1:

        for dividendo in range(2, numero-1):

            if numero % dividendo == 0:
                return False

        return True

    return False
        
def prueba():

    num = ingreso_entero(input("Ingrese un entero: "))

    print("Es Primo: ", es_primo(num))


if __name__ == '__main__':
    prueba()