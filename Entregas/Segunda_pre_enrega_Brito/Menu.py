#importamos clases
from Clase_Cliente import Cliente
from Clase_Producto import Producto

#funcion para mostrar el menu
def mostrar_menu():
    print("1. Crear Cliente")
    print("2. Crear Producto")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

#función para ejecutar la opción seleccionada (con manejo de errores)
def ejecutar_opcion(opcion):
    if opcion == "1":
        try:
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            edad = int(input("Ingrese la edad del cliente: "))
            email = input("Ingrese el email del cliente: ")
        
            # Crear una instancia temporal para verificar el email
            cliente_temp = Cliente(nombre, apellido, edad, email)        
            if cliente_temp.verificar_email(email) == True:
                cliente = Cliente(nombre, apellido, edad, email)
                print("Cliente creado con éxito")
                print(cliente)
            else:
                print("Email inválido. No se pudo crear el cliente.")
                return True
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            return True
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            return
            
    elif opcion == "2":
        try:
            nombre = input("Ingrese el nombre del producto: ")
            precio = int(input("Ingrese el precio del producto: "))
            producto = Producto(nombre, precio)
            print("Producto creado con éxito")
            print(producto)
        except ValueError:
            print("El precio debe ser un número entero, intente nuevamente")
            return True
    elif opcion == "3":
        print("Saliendo del programa")
        return False
    else:
        raise ValueError("Opción inválida")
    return True

#función principal pqra ejecutar el programa
def main():
    while True:
        opcion = mostrar_menu()
        try:
            continuar = ejecutar_opcion(opcion)
            if continuar == False:
                break
        except ValueError as e:
            print(e)
            print("Intente nuevamente")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            print("Intente nuevamente")
            
#llamada a la función principal
if __name__ == "__main__":
    main()
    
