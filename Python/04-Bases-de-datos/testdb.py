import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb2-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

cursor = connection.cursor(as_dict=True)

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