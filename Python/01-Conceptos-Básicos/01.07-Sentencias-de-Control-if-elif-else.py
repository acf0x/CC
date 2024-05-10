#################################################
# Sentencias de control - if / elif / else      #
#################################################

# Declaración de variables
a = 200
b = 200

# Prueba 1 - if/elif/else
print(f"Inicio del programa")
print()
if (b > a):
    print("B es mayor que A")
    print(f"El valor de B es igual a {b}")
elif (a > b):
    print("A es mayor que B")
    print(f"El valor de A es igual a {a}")
else:
    print(f"A es igual a B")
print()
print("Fin del programa")
print()

# Prueba 2 - if/elif/elif
print(f"Inicio del programa")
print()
if (b > a):
    print("B es mayor que A")
    print(f"El valor de B es igual a {b}")
elif (a > b):
    print("A es mayor que B")
    print(f"El valor de A es igual a {a}")
elif (a == b):
    print(f"A es igual a B")
print()
print("Fin del programa")
print()

# Prueba 3 - if/else/if/else
print(f"Inicio del programa")
print()
if (b > a):
    print("B es mayor que A")
    print(f"El valor de B es igual a {b}")
else:
    if (a > b):
        print("A es mayor que B")
        print(f"El valor de A es igual a {a}")
    else:
        print(f"A es igual a B")
print()
print("Fin del programa")
print()


