#HERENCIAS
#POLIMORFISMO
#HERENCIA MULTIPLE
#La herencia es un concepto transversal en la programación orientada a objetos.

#Herencia
#La herencia es un concepto fundamental en la programación orientada a objetos.
#Permite definir una clase en función de otra clase ya existente.
#La herencia se utiliza para reutilizar código y para crear una jerarquía de clases. Si una clase es una generalización de otra clase, 
# entonces se puede decir que la primera clase es una subclase de la segunda clase.
#Capacidad de una clase, de recibir (heredar) atributos y métodos de otra clase.

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def saluda_persona(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)
        
class Empleado(Persona):
    def __init__(self, nombre, apellido, salario, ingreso, horario):
        super().__init__(nombre, apellido)#llama al constructor de la clase padre
        self.salario = salario
        self.ingreso = ingreso
        self.horario = horario
        
    def fichar(self):
        if self.ingreso < self.horario:
            print("Fichado")  
    def saluda_empleado(self):
        print("Hola, mi nombre es", self.nombre, self.apellido, "y mi salario es", self.salario)

class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono, email):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.email = email
        
    def saluda_cliente(self):
        print("Hola, mi nombre es", self.nombre, self.apellido, "y mi teléfono es", self.telefono)  

class Guardia(Empleado, Persona):
    def __init__(self, nombre, apellido, salario, ingreso, horario, turno):
        Empleado.__init__(self, nombre, apellido, salario, ingreso, horario)#Hereda de empleado que a su vez hereda de persona
        self.turno = turno
        
    def saluda_guardia(self):
        print("Hola, mi nombre es", self.nombre, self.apellido, "y mi turno es", self.turno)    
        
    def llama_policia(self):
        print("Llamando a la policía")          

#polimorfismo, significa que un objeto puede tener diferentes formas, es decir, que un objeto puede ser de diferentes clases.
#En Python, el polimorfismo se refiere a la capacidad de una clase para tener métodos con el mismo nombre pero con diferentes comportamientos.
#en python todas las clases heredan de la clase object
#ejemplo de polimorfismo
class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")   


class Humano():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        print("Hola")

garfield = Gato("Garfield")
Pluto = Perro("Pluto")
Juan = Humano("Juan")
Lista_sonidos = [garfield, Pluto, Juan]
for animal in Lista_sonidos:
    animal.sonido() #se llama al método sonido de cada clase, aunque Juan sea un humano, emite sonido humano. Esto es polimorfismo en python, en otros lenguajes no se puede hacer esto
    
    
#Herencia múltiple: significa que una clase puede heredar de más de una clase. Una clase puede tener más de una clase padre.

#ejemplo de herencia múltiple
class A:
    def __init__
    def metodo(self):
        print("Soy de la clase A")
        
class B:
    def metodo(self):
        print("Soy de la clase B")
        
class C(A, B): #hereda de A y B
    pass        