################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def ordenar_mayor_a_menor(n1, n2, n3):
    
    ordenada = []

    lista_interna = [n1, n2, n3]

    while len(lista_interna) > 0:

        mayor = lista_interna[0]
            
        for i in lista_interna:

            if mayor < i:
                mayor = i


        ordenada.append(mayor)
        lista_interna.remove(mayor)

    return tuple(ordenada)

def ordenar_menor_a_mayor(n1, n2, n3):

    ordenada = []

    lista_interna = [n1, n2, n3]

    while len(lista_interna) > 0:

        menor = lista_interna[0]
            
        for i in lista_interna:

            if menor > i:
                menor = i


        ordenada.append(menor)
        lista_interna.remove(menor)

    return tuple(ordenada)


def prueba():
    
    n1 = ingreso_entero(input("Ingrese un entero: "))
    n2 = ingreso_entero(input("Ingrese un entero: "))
    n3 = ingreso_entero(input("Ingrese un entero: "))

    print("De Mayor a Menor: ",
        ordenar_mayor_a_menor(n1,n2,n3)
    )
    print("De Menor a Mayor",
        ordenar_menor_a_mayor(n1,n2,n3)
    )
   
   
if __name__ == '__main__':
    prueba()