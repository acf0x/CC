import sqlite3, json

# Establecer una conexión con la base de datos, especificando la ruta del fichero
# si el fichero (base de datos) no existe, se crea

# Ruta absoluta
connection = sqlite3.connect("C:\\EOIFormación\\Python\\python-1\\Python\\04-Bases-de-datos\\databases\\demo.db")

# Ruta relativa
#connection = sqlite3.connect(".\\databases\\demo.db")

# Ruta, la misma ubicación del fichero de python
#connection = sqlite3.connect("demo.db")

# Crea una base de datos en memoria ram, es rápida pero los datos
# se eliminan al finalizar la ejecución del programa Python
#connection = sqlite3.connect(":memory:"")

# Creamos un cursor para ejecutar comandos en la base de datos
cursor = connection.cursor()

# Consultar la existencia de tablas en la base de datos
# Si la tabla no existe la creamos
command = """
    SELECT COUNT() FROM sqlite_master WHERE type = 'table' and name = 'Alumnos'
"""
cursor.execute(command)
numTablas = cursor.fetchone()[0]
print(f"Número de tablas con nombre Alumnos: {numTablas}")

if(numTablas == 0):
    command = """
        CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)
    """
    cursor.execute(command)
    
    command = """
        CREATE TABLE Profesores (id integer, nombre text, apellidos text, curso text, salario real, foto blob)
    """
    cursor.execute(command)