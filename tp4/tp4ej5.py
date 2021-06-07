################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def signo(numero):

    if numero < 0:
        return "es un numero negativo"
    elif numero == 0:
        return "el numero es 0"
    else:
        return "el numero es positivo"



def prueba():
    
    numero = ingreso_entero(input("Ingrese un numero: "))

    print(signo(numero))
  
if __name__ == '__main__':
    prueba()