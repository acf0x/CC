#################################################
# Conversión de variables                       #
#################################################

# Declaración de variables

a = 5.3
b = "25"
c = "25.7"
d = "a 8.4"
x = 1.7

# Conversiones de números a texto con STR

# Este print("El valor de A es: " + a) dará ERROR porque solo se pueden concatenar (+) dos variables string y "a" es float
print("El valor de B es: " + b)

print(type(a))
print(type(b))

print("El valor de A es: " + str(a)) # Lo convertimos a string

temp = str(a) # También podemos hacer una nueva variable que sea "a" pero str, aunque no debe hacerse porque es 1 variable de más
print("El valor de A es: " + temp)

# Conversiones de texto a número con INT y FLOAT

# Este print("Valor de B: " + int(b)) dará ERROR porque concatena un str con un int, si le añadimos el formateador dejará printearlo, aunque el tipo interno no cambiará realmente
print(f"Valor de B: {int(b)}")
print(type(int(b)))
print()

print(f"Suma: {b + c}") # esto está sumando TEXTO, el resultado será la suma del TEXTO
# este print(f"Suma: {int(b) + int(c)} ") dará error porque no puede convertir C en int porque tiene decimales, tendría que ser float
print(f"Suma: {int(b) + float(c)} ") # esto sí deja y el resultado será un float

print(a + x)
print(type(a + x)) # la suma de dos floats que da X.0, será también tomada como float aunque el .0 no aporte valor