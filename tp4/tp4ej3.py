################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################



def prueba():
    ''' FUNCION PARA MOSTRAR POR PANTALLAS LAS OPCIONES Y EL RESULTADO '''

    while True:
        
        print("1) Fahrenheit a Centigrados 2) Centigrados a Fahrenheit")
        opcion = input()

        if opcion == "1":

            print("Ingrese la temperatura en Fahrenheit")            
            valor_crudo = input()

            print("Centigrados: ", convertir_a_centigrados(valor_crudo))

        if opcion == "2":

            print("Ingrese la temperatura en Centigrados")
            valor_crudo = input()
            
            print("Fahrenheits: ", convertir_a_fahrenheit(valor_crudo))

def convertir_a_centigrados(valor):
    ''' FUNCION PARA CONVERTIR A CENTIGRADOS '''

    try:
        valor = float(valor)

    except ValueError:
        return "Ingresaste un valor invalido!"


    result = ((valor - 32) * 5)/9
    return result

def convertir_a_fahrenheit(valor):
    ''' FUNCION PARA CONVERTIR A FAHRENHEIT '''

    try:
        valor = float(valor)

    except ValueError:
        return "Ingresaste un valor invalido!"


    result = ((valor *9)/5) + 32
    return result



if __name__ == '__main__':
    prueba()