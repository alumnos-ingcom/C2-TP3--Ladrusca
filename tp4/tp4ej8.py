################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def prueba():
    
    lista_desordenada = []

    for i in 3:
        
        lista_desordenada.append(ingreso_entero())

    print("Original: ", lista_desordenada)
    print("De Mayor a Menor: ", ordenar_mayor_a_menor(lista_desordenada))
    print("De Menor a Mayor", ordenar_menor_a_mayor(lista_desordenada))



def ordenar_mayor_a_menor(lista):
    pass
def ordenar_menor_a_mayor(lista):
    pass
if __name__ == '__main__':
    prueba()