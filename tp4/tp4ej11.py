################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

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

def prueba():
    
    texto_crudo = str(input("Ingrese un texto a comprobar: "))

    print(comprobar_palindromo(texto_crudo))

if __name__ == '__main__':
    prueba()