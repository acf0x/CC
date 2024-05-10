#################################################
# Conversión de variables                       #
#################################################

# Importamos módulos
from datetime import datetime 
import time

# Declaración de variables

# Almacenamos en var dt1 fecha y hora actual del sistema (en el momento ejecutado)
dt1 = datetime.now()

# Mostramos fecha almacenada en dt1
print(f"Fecha 1: {dt1}")

# Mostramos parte de la fecha almacenada en dt1
print(f"Día {dt1.day}")
print(f"Día {str(dt1.day).zfill(2)}") # zfill = hace que salga con n numero de digitos y si no los hay, completa con 0 por la izq hasta completar. Necesario que sea str.
print(f"Mes {dt1.month}")
print(f"Mes {str(dt1.month).zfill(2)}")
print(f"Hora {dt1.hour}")
print(f"Minutos {dt1.minute}")
print(f"Segundos {dt1.second}")
print(f"Milisegundos {dt1.microsecond}")
print()

# Convertir un texto en una fecha utilizando STRPTIME (string parse to time)

fecha = input("Escribe tu fecha de nacimiento (dd-mm-yyyy): ")
dt2 = datetime.strptime(fecha, "%d-%m-%Y").date()   #retorna un date
dt2x = datetime.strptime(fecha, "%d-%m-%Y")          #retorna un datetime

# Mostramos fecha sin formatear
print(f"Fecha 2: {dt2}")

# Mostramos fecha formateada
print(f"Hoy es: {dt2.strftime("%A, %d de %B de %Y")}")

#Calculo entre fechas y mostrar información
dtr = dt1 - dt2x     # dt2 no porque dt1 es datetime (mas preciso, incluye h, min, seg...) y dt2 es date (menos preciso), no pueden restarse
print(dtr)
print(dtr.days)
print(dtr.days/365)
print(dtr.seconds)
print(dtr.total_seconds())

# Creando dt1 pero en date (menos preciso) y ya se podria con dt2. Esta mal hecho xq no concuerdan en tipologia dt1 y dt2 / dt1x y dt2x, pero se entiende
dt1x = datetime.now().date()
dtrx = dt1x - dt2
print()

# Cálculo de edad 1
print()
print(f"Mi edad es: {dtr.days/365} años")
print(f"Mi edad es: {dtr.days//365} años") # // es para obtener sin decimales
print()

# Cálculo de edad 2
print(divmod(dtr.days, 365)) # da (resultadoentero(años), resto(dias))
print()

# Cálculo de edad 3
edad = divmod(dtr.days, 365) # crea una tupla con 2 valores separados por coma, 0 y 1, que serán referenciados abajo
print(f"Tienes {edad[0]} años y {edad[1]} días")
print(f"Mi edad es: {dtr.days//365} años y {dtr.days%365} días") # el % es búsqueda del resto, que dará días
print()

# Otra forma
print(f"Tienes {dt1.year - dt2.year} años") #inexacto


#################################################
#                  TIEMPO                       #
#################################################

# Importamos módulos
from datetime import datetime 
import time
import locale

# Configuración regional
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# TIME retorna la cantidad de segundos transcurridos desde el comienzo
# que por defecto, se fija en el 01-Enero-1970 00:00:00
t1 = time.time()
print(f"Segundos desde el 01-Ene-1970: {t1} \n")

# Transformación de segundos en una fecha
t2 = time.localtime(t1)
print(f"Tupla: {t2}")
print(f"Año: {t2.tm_year} ")
print(f"Mes: {t2.tm_mon} ")
print(f"Mes: {t2.tm_mday} \n")

#Conversión de T2 en una representaciuón de fecha y hora local
print(f"Fecha: {time.asctime(t2)}")
print(f"Hoy es el día {t2.tm_mday} del mes {t2.tm_mon} del año {t2.tm_year} \n")