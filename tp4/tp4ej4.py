################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def prueba():
    print("Ingrese el primer numero")
    n1= input()
    
    print("Ingrese el segundo numero")
    n2= input()

    print(comprobaciónNumerica(n1, n2))

def comprobaciónNumerica(num1, num2):

    try:
        num1 = int(num1)
        num2 = int(num2)
    
    except ValueError:
        return "Valores invalidos!"

    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1
        

    

if __name__ == '__main__':
    prueba()