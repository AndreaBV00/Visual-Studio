conjunto = {'Inglaterra', 'USA','Mexico'}
print(conjunto)
conjunto.update(['Islandia', 'Italia', 'Argentina', 'Portugal', 'USA'])
print(conjunto)
conjunto.discard('Chile')
conjunto.discard('Italia')
print(conjunto)
"""
Consigna Dicts

Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:
utilizando un diccionario.

Ejemplo del output solicitado: 
Juan tiene 25 años, y vive en Carrera 7 - Bogotá
"""

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
direccion = input('Ingrese su dirección: ')
usuario = {
    'nombre': nombre, #Juan 
    'edad': edad, #25
    'direccion': direccion #Carrera 7 - Bogotá
}
print(f'{usuario["nombre"]} tiene {usuario["edad"]} años, y vive en {usuario["direccion"]}') #Juan tiene 25 años, y vive en Carrera 7 - Bogotá


#esto es una prueba

andrea = 'Andrea'

