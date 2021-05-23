################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def prueba():
    
    print("Ingrese un texto a comprobar:")
    texto_crudo = str(input())

    print("El texto es Palindromo? ", comprobar_palindromo(texto_crudo))

def comprobar_palindromo(cadena):

    cadenaLimpia = ""            
    indice = 0

    for c in cadena:
        if c != " ":
            cadenaLimpia += c

    for i in cadenaLimpia:
        indice -= 1
        if i != cadenaLimpia[indice]:
            return False

    return True

if __name__ == '__main__':
    prueba()