################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def signo(numero):

    if numero < 0:
        return "-"
    elif numero == 0:
        return "0"
    else:
        return "+"



def prueba():
    
    numero = ingreso_entero(input("Ingrese un numero: "))
    resultado = signo(numero)
    
    print(resultado)
  
if __name__ == '__main__':
    prueba()