#################################################
# Colecciones - Diccionarios                    #
#################################################

# Declaración de variables
# Utilizamos [] para la declaracion de variables que son diccionarios

vacio = {}
frutas = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LM":"lima", "MA":"mandarina"}

# Mostrar el contenido de un diccionario
print()
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Mostrar el valor de un elemento en con la clave PO (pomelo)
print(f"Clave PO: {frutas["PO"]}")
print("==============================\n")

# Mostrar el valor de un elemento con la función GET
print(f"Clave PO: {frutas.get("PO")}")

# Mostrar el numero de elementos que contiene el diccionario
print(f"Número de elementos: {len(frutas)}")
print("==============================\n")

# Mostrar las claves que contienen el diccionario
print(f"Claves: {list(frutas.keys())}")
print("-----------")

print(f"Claves: {frutas.keys()}")
print("==============================\n")

# Modificar valores del diccionario
frutas["NA"] = "sandía"
print(f"Contenido de frutas: {frutas}")
frutas.update({"NA":"ciruela"})
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Añadir nuevos valores al diccionario
frutas["ML"] = "melón"
print(f"Contenido de frutas: {frutas}")
frutas.update({"MZ":"manzana"})
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Eliminar valores del diccionario
frutas.pop("NA")
del frutas["MZ"]
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Recorremos el diccionario mostrando los diferentes valores
for key in frutas:
    print(f"{key}# {frutas[key]}")
print("==============================\n")

# Copiar un diccionario
vacio = frutas.copy()
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Eliminar todos los elementos de un diccionario
frutas.clear()
print(f"Contenido de frutas: {frutas}")
print(f"Contenido de frutas: {vacio}")
print("==============================\n")