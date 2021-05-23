################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def prueba():
    
    while True:

        print("1)ingrese un entero 2)ingrese un entero en un rago especifico 3)ingrese un entero default")
        print("Elija una opción(1, 2, 3):")
        
        opcion =  input()
        
        if opcion == "1":
            print("---Valor Valido, ", ingreso_entero_reintento())
            
        elif opcion == "2":
            print("---Valor Valido, ", ingreso_entero_restringido())
        
        elif opcion == "3":
            print("---Valor Valido, ", ingreso_entero())
        
        else:
            print("Opción no valida!")



def ingreso_entero():
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """

    print("ingrese un valor entero!:")
    valor_interno = input()

    try:
        entero = int(valor_interno)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero


def ingreso_entero_reintento():
    ''' FUNCION QUE PERMITE EQUIVOCARSE UNA CANTIDAD DE VECES DEFINIDA '''

    cantidad_reintentos = 5

    while cantidad_reintentos >= 0:

        print("ingrese un valor entero!:")
        valor_interno = input()

        try:
            return int(valor_interno)
            

        except:
            
            if cantidad_reintentos > 0:
                print(f"El valor no es valido, debe ser un entero. Le quedan {cantidad_reintentos} Vuelva a intentar.")
            
            cantidad_reintentos -= 1

    raise IngresoIncorrecto("Valor No entero! y te quedaste sin intentos!")


def ingreso_entero_restringido():
    ''' FUNCION QUE VERIFICA UN NUMERO EN UN RANGO DEFINIDO '''

    print("ingrese un valor entero en el rango de 0 a 10!:")

    valor_interno = input()

    try:

        valor_interno = int(valor_interno)

        if valor_interno >=0 and valor_interno <=10:

            return valor_interno
        else:
            raise IngresoIncorrecto("Numero fuera de rango!")
            
    except ValueError as error:
        raise IngresoIncorrecto('Valor invalido, no es un entero!') from error
    
    except IngresoIncorrecto as error:
        raise IngresoIncorrecto(error)


class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass


if __name__ == "__main__":
    prueba()