#################################################
# Sentencias de control - try / except          #
#################################################

# Declaración de variables
numero1 = 2
numero2 = 100

print(f"\nInicio del programa: \n")
try:
    numero3 = numero2 / numero1
    print(f"Valor de número 3: {numero3}")
    f = open("miFichero.txt")
except ZeroDivisionError as err:    # err es una variable, da igual el nombre
    print(f"{err}")
    print(f"{type(err)}")
except FileNotFoundError as err:
    print(f"{err}")
    print(f"{type(err)}")
except Exception as err:            # errores genéricos
    print(f"{err}")
    print(f"{type(err)}")
else:
    print(f"Este bloque se ejecuta cuando el TRY finaliza correctamente.")
finally:
    print(f"\nFin del programa \n")

# Ejemplo 2
numero = "32"
print(f"\nInicio del programa 2: \n")
try:
    if(type(numero) is not int):
        raise Exception("La variable NUMERO no es numérica.")
except Exception as e:
    print(f"{e}")
    

# Ejemplo 3

try:

    print("Nivel 1")
    
    # print(100/0) nivel 1
    
    print("Inicio Nivel 2")
    
    try:
        print("Nivel 2")
        print(100/0)
    except Exception as err:
        raise
        print(f"Nivel 2: {err}")
    finally:        #si quitamos el finally, no se ejecutaría el print de abajo ya que el raise eleva la excepcion al nivel 1
        print("Fin Nivel 2")
except Exception as err:
    print(f"Nivel 1: {err}")
