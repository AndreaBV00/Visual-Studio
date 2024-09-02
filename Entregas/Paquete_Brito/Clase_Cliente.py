#creamos la clase cliente

class Cliente:  
    def __init__(self, nombre, apellido, edad, email): #clase con 4 atributos y 2 métodos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad} Email: {self.email}"
    
    def verificar_email(self, email): #Verifica si el email tiene un formato válido
        if "@" in email and "." in email:
            return True
        else:
            return False