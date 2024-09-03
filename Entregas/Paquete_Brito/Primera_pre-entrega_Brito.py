#Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. 
# Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.
#El formato de registro es: Nombre de usuario y Contraseña.
#Utilizar una función para almacenar la información y otra función para mostrar la información.
#Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
#Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
#guarde la información en un archivo de texto

# definición de las variables
usuarios = {}

#función para registrar un usuario
def registrar_usuario(usuario, contraseña):
    usuarios[usuario] = contraseña
    print("Usuario registrado con éxito")
    return usuarios

#función para mostrar los usuarios registrados
def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario, contraseña in usuarios.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

#función para hacer login
def login(usuario, contraseña):
    if usuario in usuarios:
        if usuarios[usuario] == contraseña:
            print("Login exitoso")
        else:
            print("Contraseña incorrecta")
    else:
        print("Usuario no registrado")

#función para guardar los usuarios en un archivo de texto
def guardar_usuarios():
    with open("usuarios.txt", "w") as archivo:
        for usuario, contraseña in usuarios.items():
            archivo.write(f"{usuario},{contraseña}\n") #se guarda en el archivo de texto el usuario y la contraseña separados por una coma en cada línea
        print("Usuarios guardados con éxito")

#función para ejecutar el programa
def main():
    while True:
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Login")
        print("4. Guardar usuarios")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            usuario = input("Ingrese el nombre de usuario: ")
            contraseña = input("Ingrese la contraseña: ")
            registrar_usuario(usuario, contraseña)
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            usuario = input("Ingrese el nombre de usuario: ")
            contraseña = input("Ingrese la contraseña: ")
            login(usuario, contraseña)
        elif opcion == "4":
            guardar_usuarios()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")
            

#llamada a la función principal
#main()

