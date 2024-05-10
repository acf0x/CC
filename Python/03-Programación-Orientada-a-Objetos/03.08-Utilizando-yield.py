#################################################
# Utilizando yield (generadores)                #
#################################################

numeros = [8, 14, 65, 7, 14, 99, 745, 1, -35, 1408]

print(f"Datos: {numeros}")

def func1(lista):
    for i in lista:
        return i * 5
    
def func2(lista):
    resultado = []
    for i in lista:
        resultado.append(i*5)
    return resultado

print(f"Func1: {func1(numeros)}")
print(f"Func2: {func2(numeros)}")
print(f"Lambda: {list(map(lambda x: x*5, numeros))}")

# Hasta aquí, lo que sabíamos hacer
# Ahora con yield

def func3(lista):
    for i in lista:
        yield i * 5

print(f"Func3: {func3(numeros)}") # da el generador
print(f"Func3 To-List: {list(func3(numeros))}") # lo transforma en lista


# Utilización de los generadores

generador = func3(numeros)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

generador = func3(numeros)
for i in generador:
    print(f">> {i}")
    
generador2 = ((i*5) for i in numeros)
print(f">>> {next(generador2)}*")
print(f">>> {next(generador2)}*")
print(f">>> {next(generador2)}*")
for i in generador2:
    print(f">>> {i}")