################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def prueba():
    print("Ingrese un numero")
    n1= input()

    print(comprobaciónNumerica(n1))

def comprobaciónNumerica(num1):

    try:
        num1 = int(num1)
    
    except ValueError:
        return "Valor invalido!"

    if num1 < 0:
        return "es un numero negativo"
    elif num1 == 0:
        return "el numero es 0"
    else:
        return "el numero es positivo"
        
if __name__ == '__main__':
    prueba()