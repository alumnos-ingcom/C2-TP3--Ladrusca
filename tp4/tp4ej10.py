################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


from tp4ej1 import ingreso_entero
from tp4ej9 import es_primo

def factores_primos(numero):

    factores = []

    while numero > 1:
        for i in range(2, 10):
            
            if es_primo(i) == True:

                if numero % i == 0:

                    factores.append(i)
                    numero = numero/i


    factores.sort()
    factores.append(1)

    return tuple(factores)
    
def prueba():
        
    num = ingreso_entero(input("Ingrese un entero: "))

    print("Factores Primos:")
    print(factores_primos(num))



if __name__ == '__main__':
    prueba()