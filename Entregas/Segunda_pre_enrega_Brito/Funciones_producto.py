#pedir datos para crear un producto
def pedir_datos_producto():
    nombre = str(input("Ingrese el nombre del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    return nombre, precio

#mostrar datos del producto
def mostrar_datos_producto(producto):
    print(producto)
