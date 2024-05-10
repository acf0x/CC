#################################################
# Sentencias de control - while                 #
#################################################

# Declaración de variables
valor = 0

print(f"Inicio del WHILE")
print()

while (valor < 5):
    valor += 1
    if (valor == 3):
        continue
    print(f"Valor actual: {valor}")


print()    
print(f"Fin del WHILE")

while (valor < 5):
    valor += 2
    print(f"Valor actual: {valor}") #va a pintar hasta 6, porque si el valor es 4(+2) = 6
    #print(f"Valor actual: {valor}" if valor <5 else "") <- esto para que no pinte más allá de 5 teniendo en cuenta la suma

print()    
print(f"Fin del WHILE")

# Declaración de más variables
cítricos = ["naranja", "limón", "pomelo", "lima", "mandarina"]
index = 0

# Utilizamos el WHILE para recorrer colecciones

while (index < len(cítricos)):
    print(f"-> {index}# {cítricos[index]}")
    index += 1      # equivalente a index = index + 1
    
# Implementar la funcionalidad que otros lenguajes ofrecen mediante el uso de DO/WHILE
# consiguiendo que el bloque de sentencias se ejecute al menos una vez

valor = 0

while(True == True):
    valor += 1
    print(f"Valor actual es {valor}")
    
    if(valor > 4):
        break
else:
    print(f"No se inicia el WHILE") # Si ponemos en el WHILE (TRUE == FALSE) o un valor raro, printearía
