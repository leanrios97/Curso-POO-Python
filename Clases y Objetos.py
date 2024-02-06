class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")
    
celular1 = Celular("Samsung", "S23", "48mp")
celular2 = Celular("Apple", "Iphone 15 Pro", "98mp")

print(celular1.marca)
print(celular2.marca)

celular2.llamar()

# Ejercicio

"""
Crear una clase que se llame estudiante: 
Atributos: 
    - Nombre
    - Edad
    - Grado 
    
Metodos: 
    - estudiar()
    (el estudiante {nombre} esta estudiando)
"""

class Estudiante: 
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando!!")
        

nombre = str(input("Nombre del estudiante: "))
edad = int(input("Edad del estudiante: "))
grado = str(input("Grado del estudiante: "))

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""
      Datos del estudiante: \\n
      Nombre: {estudiante1.nombre} \n
      Edad: {estudiante1.edad} \n
      Grado: {estudiante1.grado} \n
      """)

estudiar = input("Que accion va a hacer? ")

while True:
    if (estudiar.lower() == 'estudiar'):
        estudiante1.estudiar()