#################################################
# Sentencias de repetición - For                #
#################################################

# Declaración de variables
cítricos = ["naranja", "limón", "pomelo", "lima", "mandarina"]

# Utilizamos FOR para recorrer colecciones con IN
# No tenemos la posición de los elementos
print("======================================")

for fruta in cítricos:        # Fruta es una variable donde se guardan los valores de la colección a medida que se recorre
    if (fruta == "limón"):    
        fruta = "no nos quedan limones :("
    print(f"-> {fruta}")
    
print("======================================")

# Utilizamos FOR para crear contadores con RANGE

# Contador de 0 a 10 
for numero in range(11):
    print(f"-> {numero}")
print("======================================")

# Contador de 10 a 20 de 2 en 2 (start, end, step)
for numero in range(10, 22, 2):
    print(f"-> {numero}")
print("======================================")

# Contador de 20 a 5 de -3 en -3 (start, end, step)
for numero in range(20, 4, -3):
    print(f"-> {numero}")
print("======================================")

# La combinación de RANGE con LEN nos permite también recorrer colecciones
# Tenemos la posición de cada elemento en la colección

for index in range(len(cítricos)):
    print(f"-> {index}# {cítricos[index]}")
    
print("======================================")
 
 # El uso de ENUMERATE nos permite recorrer colecciones
 # conociendo tanto el índice como el valor
for index, fruta in enumerate(cítricos):
     print(f"-> {index}| {cítricos[index]}")
     print(f"-> {index}| {fruta}")              #ambos valdrían
     
print("======================================")
     

# Utilización de CONTINUE y BREAK con las sentencias FOR

# BREAK finaliza la ejecución de bloque de sentencias y el FOR

for fruta in cítricos:        # Fruta es una variable donde se guardan los valores de la colección a medida que se recorre
    if (fruta == "limón"):
        print(f"B R E A K")    
        break
    print(f"-> {fruta}")
    
print("======================================")

# CONTINUE finaliza la ejecución de bloque de sentencias (pero no del FOR)

for fruta in cítricos:        # Fruta es una variable donde se guardan los valores de la colección a medida que se recorre
    if (fruta == "limón"):
        print(f"C O N T I N U E (salta el limón)")    
        continue
    print(f"-> {fruta}")
    
print("======================================")