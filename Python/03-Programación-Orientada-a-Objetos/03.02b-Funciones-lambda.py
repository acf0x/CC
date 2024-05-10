#################################################
# Funciones lambda                              #
#################################################

from functools import reduce

numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]

# Escribe una funcion que retorne una lista con los numeros mayores de 100
def mayordecien(lista):
    resultado = []
    
    for numero in lista:
        if (numero > 100):
            resultado.append(numero)
    
    return resultado


print(f"Función estándar: {mayordecien(numeros)}")

# Escribe una funcion que return TRUE cuando un numero es mayor de 100,
# si no, retorna FALSE

def nummayorcien(numero):
    if (numero>100):
        return True
    else:
        return False
    
print(f"mayor de 100 con Filter más una función estándar: {list(filter(nummayorcien, numeros))}")


# Extraer número mayores de 100 utilizando FILTER y LAMBDA
print(f"mayor de 100 con Filter más función lambda: {list(filter(lambda x: x>100, numeros))}")

print(f"menor de 50 con Filter más función lambda: {list(filter(lambda x: x<50, numeros))}")
print(f"números pares: {list(filter(lambda x: x%2 == 0, numeros))}")

print(f"Resultado de sumar 10 y dividir entre 2: {list(map(lambda x: (x+10)/2, numeros))}")


# Ejemplo de REDUCE con una suma
# reduce coge los 2 primeros y los suma, resultado lo suma con el 3ro, dsp con el 4to... hasta que queda 1
print(f"Resultado SUM: {sum(numeros)}")
print(f"Resultado: {reduce(lambda x, y: x+y, numeros)}")
print()

print(f"Datos: {numeros}")
print(f"Algún número par?: {any(x%2 == 0 for x in numeros)}")
print(f"Algún número par?: {any((map(lambda x: x%2 == 0, numeros)))}")
print(f"Todos pares?: {all((map(lambda x: x%2 == 0, numeros)))}")
