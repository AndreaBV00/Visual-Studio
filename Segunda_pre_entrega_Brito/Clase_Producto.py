#creamos la clase Producto
class Producto:
    def __init__(self, nombre, precio): #clase con dos atributos y un metodo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} Precio: {self.precio}"
