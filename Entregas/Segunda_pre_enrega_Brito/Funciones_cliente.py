#pedir datos para crear un cliente
def pedir_datos_cliente():
    nombre = str(input("Ingrese el nombre del cliente: "))
    apellido = str(input("Ingrese el apellido del cliente: "))
    edad = int(input("Ingrese la edad del cliente: "))
    direccion = str(input("Ingrese la dirección del cliente: "))
    usuario = nombre + apellido
    password = nombre + "123" 
    return nombre, apellido, edad, direccion, usuario, password

#mostrar datos del cliente
def mostrar_datos_cliente(cliente):
    print(cliente)