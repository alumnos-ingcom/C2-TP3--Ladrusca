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
    
    texto_crudo = input("Ingrese un texto a comprobar: ")
    texto_crudo = comprobar_palindromo(texto_crudo)

    print(texto_crudo)

if __name__ == '__main__':
    prueba()