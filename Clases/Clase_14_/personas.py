class persona ():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    def mostrar(self):
        print ("Nombre: ", self.nombre)
        print ("Edad: ", self.edad)
        print ("Sexo: ", self.sexo)
    def mayor_edad(self):   
        if self.edad >= 18:
            print ("Es mayor de edad")
        else:
            print ("Es menor de edad")
