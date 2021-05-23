################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def prueba():
    
    lista_desordenada = []

    for i in range(3):
        
        lista_desordenada.append(ingreso_entero())

    print("Original: ", lista_desordenada)
    print("De Mayor a Menor: ", ordenar_mayor_a_menor(lista_desordenada))
    print("De Menor a Mayor", ordenar_menor_a_mayor(lista_desordenada))


def ordenar_mayor_a_menor(lista):
    
    ordenada = []

    lista_interna = []
    lista_interna.extend(lista)

    while len(lista_interna) > 0:

        mayor = lista_interna[0]
            
        for i in lista_interna:

            if mayor < i:
                mayor = i


        ordenada.append(mayor)
        lista_interna.remove(mayor)

    return ordenada

def ordenar_menor_a_mayor(lista):

    ordenada = []

    lista_interna = []
    lista_interna.extend(lista)

    while len(lista_interna) > 0:

        menor = lista_interna[0]
            
        for i in lista_interna:

            if menor > i:
                menor = i


        ordenada.append(menor)
        lista_interna.remove(menor)

    return ordenada


    
if __name__ == '__main__':
    prueba()