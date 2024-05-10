#################################################
# Clases                                        #
#################################################

from datetime import datetime
class Alumno:
    """Clase demostracion del curso de python"""
    
    # variables de la calse
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None
    
    # función constructora, se ejecuta al crear (instanciar) el objeto
    # self es una variable que contiene el propio objeto
     
    def __init__(self, nombre, apellido1, apellido2="") -> None:    #si ponemos apellido2="" se convierte en un parámetro opcional
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2
    

# funciones del objeto alumno

    def getNombreCompleto(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"
    
    def getEdad(self) -> int:
        try:
#            if (type(self.FechaNacimiento) == datetime.date):
                resultado = datetime.now().date() - self.FechaNacimiento
                return resultado.days // 365
#            else:
#                return -1
        except:
            return -1
        
    
    def setFechaNacimiento(self, fecha) -> bool:
        try:
            if (len(fecha) == 10):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            elif (len(fecha) == 8):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                return False
            
            return True
        except:
            return False
    
    
    
    
    
    
demo = Alumno("Borja", "Cabeza", "Rozas")
print(f"{demo.Nombre} {demo.Apellido1} {demo.Apellido2}")
demo = Alumno("Borja", "Cabeza")
print(f"{demo.Nombre} {demo.Apellido1} {demo.Apellido2}")
print(f"{demo.getNombreCompleto()}")
print(f"{type(demo.FechaNacimiento)}")
if (demo.setFechaNacimiento("12-03-1999")) == True:
    print(f"Edad: {demo.getEdad()} años")
print(f"{type(demo.FechaNacimiento)}")

demo2 = Alumno("Ana", "Sánchez")
print(f"{demo2.getNombreCompleto()}")
if (demo2.setFechaNacimiento("17-10-1965")) == True:
    print(f"Edad: {demo2.getEdad()} años")
    
    
alumnos = [Alumno("Ana", "Sánchez", "Rozas"), Alumno("Roberto", "Sánchez"), Alumno("Borja", "Sanz"), Alumno("Alfonso", "Cabeza")]
for alumno in alumnos:
    print(f"Alumno: {alumno.getNombreCompleto()}")
    
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]
for fruta in frutas:
    print(f">> {fruta.isnumeric()}")