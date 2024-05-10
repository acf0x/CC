#################################################
# Colecciones - Listas                          #
#################################################

# Declaración de variables
# Utilizamos [] para la declaracion de variables que son listas

vacia = []
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]

# Mostrar el contenido de una lista
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Mostrar el valor del elemento en la posicion 2 (pomelo)
print(f"Posición 2: {frutas[2]}")
print("==============================\n")

# Mostrar el numero de elementos que contiene la lista
print(f"Número de elementos: {len(frutas)}")
print("==============================\n")

# Mostrar el número de veces que tenemos un valor en la lista
# Sensible a mayúsculas
print(f"Naranja se repite {frutas.count("naranja")} veces")
print("==============================\n")

# Modificar el valor de una posición
frutas[2] = "fresa"
print(f"Posición 2: {frutas[2]}")
print("==============================\n")

# Añadir nuevos valores a la lsita utilizando APPEND
# Se añaden siempre en la siguiente posición
frutas.append("manzana")
frutas.append("melón")
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Añadir un nuevo valor en una posición utilizando INSERT(index, value)
# Añadir sandía en la posicion 1
frutas.insert(1, "sandía")
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Añadir varios elementos utilizando EXTEND(list)lista_edad
nuevasFrutas = ["maracuya", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas)
print(f"Contenido de frutas: {frutas}")
frutas.extend(["platano", "pera"])
print(f"Contenido de frutas: {frutas}")
# también frutas += nuevasFrutas
# o frutas +=["platano", "pera"]
print("==============================\n")

# Añadir un elemento si no existe
print(f"Melocotón existe en FRUTAS: {("melocotón" in frutas)}")
print(f"Melocotón no existe en FRUTAS: {("melocotón" not in frutas)}")
if ("melocotón" not in frutas):
    frutas.append("melocotón")
print("==============================\n")

# Eliminar un elemento indicando su posicion (posicion 5, mandarina)
frutas.pop(5)
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Eliminar un elemento indicando su valor (solo elimina la primera coincidencia, en este caso, la del principio)
frutas.append("naranja")
frutas.remove("naranja")
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Para evitar errores podemos preguntar por la existencia de un valor antes de eleiminar
if ("uva" in frutas):
    frutas.remove("uva")
print("==============================\n")
    
# Invertir el orden utilizando REVERSE
frutas.reverse()
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Ordenar los elementos de la lsita por orden alfabetico
frutas.sort()
print(f"Contenido de frutas: {frutas}")
print()
frutas.sort(reverse=True)
print(f"Contenido de frutas: {frutas}")
print("==============================\n")

# Recorremos las listas mostrando sus valores
for fruta in frutas:
    print(f"{fruta}")
print()
for index in range(len(frutas)):
    print(f"{index}# {frutas[index]}")
print()
for index, value in enumerate(frutas):
    print(f"{index}# {value}")
print("==============================\n")

# Copiar una lista
vacia = frutas.copy()
print(vacia)
print("==============================\n")

# Eliminar todos los elementos de una lsita
frutas.clear()
print(f"Contenido de frutas: {frutas}")
print("==============================\n")
