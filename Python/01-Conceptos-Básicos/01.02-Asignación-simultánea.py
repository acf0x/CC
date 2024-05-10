#################################################
# Asignación de variables                       #
#################################################

# Declaración de variables
a = 5
b = 10

# Intercambiar los valores entre a y b. Intento 1

a = b
b = a
print("Intento 1, incorrecto")
print(a)
print(b)
print(f"Variable A: {a}")
print(f"Variable B: {b}")
print()

# Intercambiar los valores entre a y b. Intento 2

a = 5
b = 10

temp = a  # Temp es solo un nombre, igualmente podría ser "c"
a = b
b = temp
print("Intento 2, correcto con una variable temporal")
print(a)
print(b)
print(f"Variable A: {a}")
print(f"Variable B: {b}")
print()

# Intercambiar los valores entre a y b. Intento 3

a = 5
b = 10

a,b = b,a

print("Intento 3, correcto")
print(a)
print(b)
print(f"Variable A: {a}")
print(f"Variable B: {b}")
print()