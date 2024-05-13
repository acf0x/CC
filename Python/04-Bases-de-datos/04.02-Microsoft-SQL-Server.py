import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb2-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

# Creamos un cursor para ejecutar comando en la base de datos
# Creamos un cursor que retorna Tuplas
cursor = connection.cursor()

# Creamos un cursor que retorna Diccionarios
cursor = connection.cursor(as_dict=True)

######################################################
# SELECT, leer registros de la base de datos
######################################################

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")

# Mostar el contenido del cursor utilizando un WHILE
row = cursor.fetchone()
while (row):
    print(f"      ID: {row["CustomerID"]}")
    print(f" Empresa: {row["CompanyName"]
                       } - {row["City"]} ({row["Country"]})\n")
    row = cursor.fetchone()

# El siguiente ejemplo comentado muestra como tratar los registros cuando se
# entregan como Tuplas en lugar de Diccionarios
"""
row = cursor.fetchone()
while (row):
    print(f"      ID: {row[0]}")
    print(f" Empresa: {row[1]} - {row[5]} ({row[8]})\n")
    row = cursor.fetchone()
"""

cursor.execute("SELECT * FROM dbo.Customers")
for row in cursor.fetchall():
    print(f">      ID: {row["CustomerID"]}")
    print(f"> Empresa: {row["CompanyName"]
                        } - {row["City"]} ({row["Country"]})\n")

# El siguiente ejemplo comentado muestra como tratar los registros cuando se
# entregan como Tuplas en lugar de Diccionarios
"""
for row in cursor.fetchall():
    print(f">      ID: {row[0]}")
    print(f"> Empresa: {row[1]} - {row[5]} ({row[8]})\n") 
"""

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "USA")

pais = input("Nombre del pais: ")
cursor.execute(f"SELECT * FROM dbo.Customers WHERE Country = '{pais}'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", pais)

cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' AND City = 'San Francisco'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany'")

cursor.execute("SELECT CustomerID, CompanyName, City, Country FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country ASC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country DESC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country, City")

for row in cursor.fetchall():
    print(f"     ID: {row["CustomerID"]}")
    print(f"Empresa: {row["CompanyName"]} - {row["City"]} ({row["Country"]})")


######################################################
# SELECT, ejemplos de JOIN
######################################################

# Ejemplo que comienza con una consulta y realiza 830 subconsultas dentro del for
# NO ES UN JOIN, son subconsultas que deben evitarse por rendimiento
cursor.execute("SELECT * FROM dbo.Orders")

for row in cursor.fetchall():
    print(f" -> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")

    cursor2 = connection.cursor(as_dict=True)
    cursor2.execute("SELECT * FROM dbo.Employees WHERE EmployeeID = %d", row["EmployeeID"])
    cursor2.execute(f"SELECT * FROM dbo.Employees WHERE EmployeeID = '{row["EmployeeID"]}'")
    employee = cursor2.fetchone()

    print(f"    Pedido gestionado por el empleado {row["EmployeeID"]}: {employee["FirstName"]} {employee["LastName"]}")


# Ejemplo que ser realiza con una consulta
# query y query2 contienen el mismo JOIN con distinta sintaxis
query = """
    "SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName 
    FROM dbo.Orders AS o, dbo.Employees AS e 
    WHERE o.EmployeeID = e.EmployeeID"
"""
query2 = """
    SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName
    FROM dbo.Orders AS o
    JOIN dbo.Employees AS e
    ON o.EmployeeID = e.EmployeeID
"""
cursor.execute(query)

for row in cursor.fetchall():
    print(f" -> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")
    print(f"    Pedido gestionado por el empleado {
          row["EmployeeID"]}: {row["FirstName"]} {row["LastName"]}")


######################################################
# SELECT, las agrupaciones
######################################################

# Listado de clientes de USA y el número de pedidos de cada cliente
# NO ES UNA AGRUPACIÓN, es una subconsulta dentro del for que debemos evitar por rendimiento
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
for row in cursor.fetchall():
    cursor2 = connection.cursor()
    cursor2.execute(f"SELECT COUNT(*) FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()[0]} pedidos")

"""
    Opcionalmente podemos trabajar con cursores que retornan diccionarios, pero estamos 
    obligados a definir alias para el dato calculado usando AS

    cursor2 = connection.cursor(as_dict=True)
    cursor2.execute(f"SELECT COUNT(*) AS NumPedidos FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()["NumPedidos"]} pedidos")
"""

# Listado de clientes de USA y el número de pedidos de cada cliente
# Solo los cliente con más de 10 pedidos
query = """
    SELECT c.CustomerID, c.CompanyName, COUNT(o.OrderID) AS NumPedidos
    FROM dbo.Customers c
    JOIN dbo.Orders o
    ON c.CustomerID = o.CustomerID
    WHERE c.Country = 'USA'
    GROUP BY c.CustomerID, c.CompanyName
    HAVING COUNT(o.OrderID) > 10
"""
cursor.execute(query)
for row in cursor.fetchall():
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {row["NumPedidos"]} pedidos")
    
    
######################################################
# INSERT, insertar nuevo registros
######################################################

# Definición de un objeto que representa el registro CUSTOMER 
class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None

# Instaciamos el objeto CUSTOMER
cliente = Customer()
cliente.CustomerID = "DEMO1"
cliente.CompanyName = "Empresa Uno, SL"
cliente.ContactName = "Borja"
cliente.ContactTitle = "Gerente"
cliente.Address = "Calle Uno, S/N"
cliente.City = "Madrid"
cliente.Region = "Madrid"
cliente.PostalCode = "28016"
cliente.Country = "España"
cliente.Phone = "900100100"
cliente.Fax = "900100200"

# cliente2 es un diccionario que también representa el registro CUSTOMER
cliente2 = {"CustomerID": "DEMO2",
            "CompanyName": "Empresa Dos, SL",
            "ContactName": "Borja Cabeza",
            "ContactTitle": "Gerente",
            "Address": "Calle Dos S/N",
            "City": "Madrid",
            "Region": "Madrid",
            "PostalCode": "28019",
            "Country": "España",
            "Phone": "910 101 102",
            "Fax": "910 101 103"}

# INSERT comando de inserción
# Ejemplo que indica las columnas o campos y los valores
command = """
    INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactTitle, City, Country)
    VALUES('ACF01', 'Company SL', 'Álvaro Cascajosa', 'Osuna', 'España')
"""

# Ejemplo que indica las columnas o campos y comodines para los valores
command = """
    INSERT INTO dbo.Customers VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Al ejecutar el comando con comodines, pasamos como segundo parámetro los valroes en una lista
command2 = """ # Hay que dar los valores después
    INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, ContactTitle, City, Country)
    VALUES(%s, %s, %s, %s, %s, %s)

cursor.execute(command2, ["ACF1", "Company DEMO, SL", "Álvaro Cascajosa", "CEO", "Osuna", "España"])
cursor.execute(command2, ("ACF2", "Company DEMO, SL", "Álvaro Cascajosa", "CEO", "Osuna", "España"))

connection.commit()
"""

# Se pueden poner comodines en todas las posiciones
# Hay que poner tantos %s como valores tiene en total, al no haber delimitado como arriba despues de dbo.Customers
command = """ 
    INSERT INTO dbo.Customers VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# Insertamos nuevos registros ejecutando el comando INSERT
cursor.execute(command)

# Utilizamos la función commit() de la conexión para CONFIRMAR la transacción
# tanto para operaciones de insercción, actualización y borrado
connection.commit()

# Utilizamos la función rollback() de la conexión para ANULAR la transacción
# tanto para operaciones de insercción, actualización y borrado
connection.rollback()


# Para insertar varios registros, creamos una lista que contiene en cada
# posición una tupla con los valores de cada registro a insertar
"""
data = []
data.append("ACF3", "Company DEMO, SL", "Álvaro Cascajosa", "CEO", "Osuna", "España")
data.append("ACF4", "Company DEMO, SL", "Álvaro Cascajosa", "CEO", "Osuna", "España")
data.append("ACF5", "Company DEMO, SL", "Álvaro Cascajosa", "CEO", "Osuna", "España")
"""

# Utilizamos .executemany() para insertar varios registros y pasamos como
# segundo parámetro la lista de tuplas con los valores de los diferentes registros
"""
cursor.executemany(command2, data)
connection.commit()
"""

# .rowcount devuelve el num de registros insertados, actualizados o borrados
"""
print(f"{cursor.rowcount} registros insertados.")
"""

# Cierre de la conexión
connection.close()