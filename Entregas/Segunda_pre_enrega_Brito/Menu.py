#función para ejecutar el programa
def main():
    while True:
        print("1. Crear cliente")
        print("2. Mostrar cliente")
        print("3. Cambiar contraseña")
        print("4. Comprar")
        print("5. Crear producto")
        print("6. Mostrar producto")
        print("7. Cambiar precio")
        print("8. Vender")
        print("9. Agregar producto")
        print("10. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombre, apellido, edad, direccion, usuario, password = pedir_datos_cliente()
            cliente = Cliente(nombre, apellido, edad, direccion, usuario, password)
        elif opcion == "2":
            mostrar_datos_cliente(cliente)
        elif opcion == "3":
            nueva_contraseña = input("Ingrese la nueva contraseña: ")
            cliente.cambiar_contraseña(nueva_contraseña)
        elif opcion == "4":
            producto = input("Ingrese el producto que desea comprar: ")
            print(cliente.comprar(producto))
        elif opcion == "5":
            nombre, precio = pedir_datos_producto()
            producto = Producto(nombre, precio)
        elif opcion == "6":
            mostrar_datos_producto(producto)
        elif opcion == "7":
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            producto.cambiar_precio(nuevo_precio)
        elif opcion == "8":
            cantidad = int(input("Ingrese la cantidad de productos vendidos: "))
            print(producto.vender(cantidad))
        elif opcion == "9":
            cantidad = int(input("Ingrese la cantidad de productos agregados: "))
            print(producto.agregar_producto(cantidad))
        elif opcion == "10":
            break
        else:
            print("Opción inválida")