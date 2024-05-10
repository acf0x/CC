#################################################
# Funciones                                     #
#################################################

from datetime import datetime

# Ejemplo de función que NO recibe datos (NO tiene parámetros) y NO retorna datos
def Func1():
    """Func1, no tiene parámetros y no retorna datos""" # esto hace que lo entrecomillado aparezca al poner ratón sobre Func1
    print(f"Hola mundo !!")

# Ejemplo de función que SÍ recibe datos (SÍ tiene parámetros) y NO retorna datos
def Func2(nombre, número):
    print(f"Me llamo {nombre} y mi número de la suerte es {número}")

# Ejemplo de función que SÍ recibe datos (SÍ tiene parámetros) y SÍ retorna datos
def Func3(frase):
    cantidad = len(frase)
    return cantidad

# Ejemplo de función que SÍ recibe datos (NO tiene parámetros) y SÍ retorna datos
def Func4():
    return datetime.now().date().strftime("%A")


print(f"Función 1:\n")
Func1()
Func1()
Func1()

print(f"\nFunción 2:\n")
Func2("Álvaro", 6)

print(f"\nFunción 3:\n")
u = Func3("En un lugar de la mancha de cuyo nombre...")
print(u)
print(Func3("En un lugar de la mancha de cuyo nombre..."))

print(f"\nFunción 4:\n")
print(f"{Func4()}")

print()
print()

#################################################################################

# Asignación de valores a los parámetros 

def Resta(a,b):                             # todos los parámetros son obligatorios
    return a - b

print(f"1) 85 - 10 = {Resta(85,10)}")       # por posición
print(f"1) 85 - 10 = {Resta(a=85,b=10)}")   # por nombre
print(f"1) 85 - 10 = {Resta(b=10,a=85)}")   # por nombre

print()

def Resta1(a,b=10):                         # solo el parámetro A es obligatorio
    return a - b

print(f"2) 85 - 10 = {Resta1(85,10)}")      # por posición
print(f"2) 85 - 10 = {Resta1(a=85,b=10)}")  # por nombre
print(f"2) 85 - 10 = {Resta1(b=10,a=85)}")  # por nombre
print(f"2) 85 - 10 = {Resta1(85)}")         # por posición, valor para A
print(f"2) 85 - 10 = {Resta1(a=85)}")       # por posición, valor para A

print()

def Resta3(a=85,b=10):                         # todos los aprametros son opcionales
    return a - b

print(f"2) 85 - 10 = {Resta3()}")           # sin valores para los parametros
print(f"3) 85 - 10 = {Resta3(85,10)}")      # por posición
print(f"3) 85 - 10 = {Resta3(a=85,b=10)}")  # por nombre
print(f"3) 85 - 10 = {Resta3(b=10,a=85)}")  # por nombre
print(f"3) 85 - 10 = {Resta3(85)}")         # por posición, valor para A
print(f"3) 85 - 10 = {Resta3(a=85)}")       # por posición, valor para A
print(f"3) 85 - 10 = {Resta3(b=10)}")       # por posición, valor para A

