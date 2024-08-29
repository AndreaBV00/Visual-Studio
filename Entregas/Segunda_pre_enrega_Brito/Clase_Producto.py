class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

    def vender(self, cantidad):
        return f"Se han vendido {cantidad} unidades de {self.nombre}"

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        return f"Precio cambiado con éxito"
    
    def agregar_producto(self, cantidad):
        return f"Se han agregado {cantidad} unidades de {self.nombre}"
