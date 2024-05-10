#################################################
# Fechas y zonas horarias                       #
#################################################

# Importamos
from datetime import datetime
import pytz

# Mostrar las diferentes zonas horarias disponibles
print(pytz.all_timezones)
print()

# Mostrar información sobre la fecha actual, sin zona horaria (local)
dt = datetime.now()
print(f"Fecha: {dt}")
print(f"Zona horaria: {dt.tzinfo}")
print()

# Mostrar información sobre la fecha actual, sin zona horaria
dtTokyo = datetime.now(pytz.timezone("Asia/Tokyo"))
print(f"Fecha de Tokyo: {dtTokyo}")
print(f"Zona horaria: {dtTokyo.tzinfo}")
print()