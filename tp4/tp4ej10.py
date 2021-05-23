################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


from tp4ej1 import ingreso_entero
from tp4ej9 import comprobacion_primo
from tp4ej8 import ordenar_menor_a_mayor
def prueba():
        
    num = ingreso_entero()
    print("Factores Primos: ", factores_primos(num))



def factores_primos(numero):

    factores = []

    while numero > 1:
        for i in range(2, 10):
            
            if comprobacion_primo(i) == True:

                if numero % i == 0:

                    factores.append(i)
                    numero = numero/i


    factores = ordenar_menor_a_mayor(factores)
    factores.append(1)

    return tuple(factores)


if __name__ == '__main__':
    prueba()