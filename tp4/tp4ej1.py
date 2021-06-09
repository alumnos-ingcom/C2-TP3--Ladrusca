################
# Tomas Grossi - @ladrusca
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """

    try:
        ingreso = input(mensaje + " #")

        entero = int(ingreso)

    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero


def ingreso_entero_reintento(valor_ingresado, cantidad_reintentos=5):
    ''' FUNCION QUE PERMITE EQUIVOCARSE UNA CANTIDAD DE VECES DEFINIDA '''

    while cantidad_reintentos >= 0:

        try:
            return int(valor_ingresado)
            
        except:
            
            if cantidad_reintentos > 0:

                print(f"El valor no es valido, debe ser un entero. Le quedan {cantidad_reintentos} intentos")
                mensaje = input("Vuelva a intentar: ")

            cantidad_reintentos -= 1

    raise IngresoIncorrecto("Valor No entero! y te quedaste sin intentos!")


def ingreso_entero_restringido(valor_ingresado, valor_minimo=0, valor_maximo=10):
    ''' FUNCION QUE VERIFICA UN NUMERO EN UN RANGO DEFINIDO '''

    try:

        valor = ingreso_entero(valor_ingresado)

        if valor >=0 and valor <=10:

            return valor
        else:
            raise IngresoIncorrecto("Numero fuera de rango!")
            
    except ValueError as error:
        raise IngresoIncorrecto('Valor invalido, no es un entero!') from error
    
    except IngresoIncorrecto as error:
        raise IngresoIncorrecto(error)


class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass


def prueba():
    
    bucle = True

    while bucle:

        print("1)ingrese un entero"
            "2)ingrese un entero en un rago especifico", 
            "3)ingrese un entero default",
            "4)salir"
        )

        opcion =  input("Elija una opción(1, 2, 3, 4):")
        
        if opcion == "1":

            print(ingreso_entero("ingrese un valor entero!:"))
            
        elif opcion == "2":

            valor = input("ingrese un valor entero en el rango de 0 a 10!:")

            print("Valido:")
            print(ingreso_entero_restringido(valor))
            
        
        elif opcion == "3":
            
            valor = input("ingrese un valor entero!(5 chances!):")

            print("Valido:")
            print(ingreso_entero_reintento(valor))
            

        elif opcion == "4":
            bucle = False
        
        else:
            print("Opción no valida!")


if __name__ == "__main__":
    prueba()