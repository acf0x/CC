#################################################
# Funciones lambda                              #
#################################################

def saludo(nombre):
    print(f"Hola, me llamo {nombre}")
    
minombre = "Borja"
saludo(minombre)

saludo("Francisco")

# Una funcion lambda equivalente a la funcion saludo()
# lambda parámetro : lógica

demo = lambda nombre : print(f"Hola, me llamo {nombre}")
print(f"Tipo de demo: {type(demo)}")

minombre = "Ana María"
demo(minombre)
demo("Ana")
print()

# Creamos una función Calcular() que recibe como parametros
# una funcion lambda con el calculo que tiene que realizar

def sumar(num):
    return lambda a: a+num
def restar(num):
    return lambda a: a-num
def multiplicar(num):
    return lambda a: a*num
def dividir(num):
    return lambda a: a/num
def calcular(formula):
    for n in range(1, 11, 1):
        print(formula(n))
        
calcular(multiplicar(5))
print()
calcular(lambda a: a * 3)
print()
calcular(lambda x: ((x * 5) - 10) / x)