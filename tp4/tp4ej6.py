################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero

def minimo(lista):

    valor_minimo = lista[0]

    for i in lista:
        if i < valor_minimo:
            valor_minimo = i

    return valor_minimo


    
def maximo(lista):

    valor_maximo = lista[0]

    for i in lista:
        if i > valor_maximo:
            valor_maximo = i

    return valor_maximo       

def prueba():
    
    lista_de_numeros = []
    bucle = True

    while bucle:

        numero = input("Ingrese un entero: ")

        lista_de_numeros.append(ingreso_entero(numero))

        while bucle:
            print("Quiere ingresar otro numero? (s/n)")

            res = input()
            if res == "n":
                bucle = False
            
            elif res == "s":
                break
        
    
    print("La lista es: ", 
        lista_de_numeros
    )

    print("El valor minimo de la lista es: ",
        minimo(lista_de_numeros)
    )
    print("El valor maximo de la lista es: ",
        maximo(lista_de_numeros)
    )

if __name__ == '__main__':
    prueba()