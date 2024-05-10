#################################################
# Formateando cadenas de texto                  #
#################################################

# Declaración de variables
texto = "   hola mundo !!!   "
#posi:   01234567890123456789
print(texto)

# Mostrar determinado caracteres de la cadena 
# indicando su posición o un rango

print(f"Posición 3: {texto[3]}")
print(f"Desde la posición 3 incluida: {texto[3:]}")
print(f"Hasta la posición 6 NO incluida: {texto[:6]}")
print(f"Entre la posición 2 incluida y 6 NO incluida: {texto[2:6]}")
print(f"Los primeros 4 caracteres empezando por derecha {texto[-5]} \n")

# Funciones que podemos utilizar con cadenas de texto

print(f"Número de caracteres: {len(texto)}")
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title()) # mayus la 1ra letra de cada palabra
print(texto.strip()) # eliminar espacios delante y detras
print(texto.count("o")) # cuántas letras o
print(f"Es un dígito: {texto.isdigit()}")
print(f"Es un dígito: {"57".isdigit()} \n")          


# Formatear texto y números

mensaje = "mundo"
print("Hola " + mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))
print(f"Hola {mensaje} !!!")

resultado = 10/3
print("Resultado: " + str(resultado))
print("xResultado:", str(resultado))
print("xResultado:", str(resultado))
print("xResultado:", resultado) # al no concatenar, no es necesario transformarlo a str
print()
print(f"Resultado: {resultado}")
print("Resultado: {}".format(resultado))
print("Resultado: {r}".format(r=resultado))
print() 
print("Resultado: {r:.2f}".format(r=resultado)) #dos decimales
print(f"Resultado: {resultado:.2f}")
