#ACTIVIDAD 1: Escribe un programa que solicite al usuario dos números enteros. Luego, muestra por pantalla la suma, resta, multiplicación y división de esos dos números.
"""print('Bienvenido al programa de operaciones matemáticas')
input('Presiona Enter para continuar')
numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))
print('La suma de los dos números es: ', numero_1 + numero_2)
print('La resta de los dos números es: ', numero_1 - numero_2)
print('La multiplicación de los dos números es: ', numero_1 * numero_2)
print('La división de los dos números es: ', numero_1 / numero_2)
"""

#ACTIVIDAD 2: Crea un programa que tome una cadena de texto como entrada del usuario. Luego, muestra por pantalla los primeros tres caracteres de la cadena, 
#seguidos por los tres últimos caracteres. Además, concatena ambos subconjuntos y muestra el resultado.

"""print('Bienvenido al programa de cadenas de texto')
input('Presiona Enter para continuar')
cadena = input('Ingrese una cadena de texto: ')
print('Los primeros tres caracteres de la cadena son: ', cadena[:3])
print('Los tres últimos caracteres de la cadena son: ', cadena[-3:])
print('La concatenación de ambos subconjuntos es: ', cadena[:3] + cadena[-3:])"""

#ACTIIDAD 3: Crea un programa que inicie con una lista de números enteros. Luego, solicita al usuario un número entero y 
# un índice para reemplazar un elemento en la lista por el nuevo número ingresado en el índice ingresado. 
# Imprime la lista resultante.

"""lista = [1, 2, 3, 4, 5]
print('Lista original: ', lista)
numero = int(input('Ingrese un número entero: '))
indice = int(input('Ingrese un índice para reemplazar un elemento en la lista: '))
if indice >= len(lista):
    print('El índice ingresado es mayor al tamaño de la lista. Intente nuevamente.')
else:
    lista[indice] = numero
    print('Lista resultante: ', lista)"""


#ACTIVIDAD 4: Crea un programa que, teniendo en cuenta la siguiente tupla, muestre el valor del segundo elemento de la misma. 
# Además, debe mostrar cuántas veces se repite este valor y cuál es el índice del valor repetido.
"""
palabras_tupla = ("manzana", "pera", "uva", "naranja", "sandía", "manzana", "plátano", "kiwi", "pera", "fresa", "mango", "uva", "cereza", "manzana", "durazno")
segundo_elemento = palabras_tupla[1]
repeticiones = palabras_tupla.count(segundo_elemento)
indice = palabras_tupla.index(segundo_elemento)
print('El segundo elemento de la tupla es: ', segundo_elemento)
print('El valor se repite ', repeticiones, ' veces')
print('El índice del valor repetido es: ', indice)
"""

#CONUNTOS, DICCIONARIOS Y MÉTODOS DE COLECCIONES
#ACTIVIDAD 1: Crea un programa que solicite al usuario ingresar nombres separados por comas. 
# Luego, crea un conjunto con los nombres ingresados y muestra por pantalla la cantidad de nombres únicos en el conjunto.

"""print('Bienvenido al programa de nombres')
input('Presiona Enter para continuar')
nombres = input('Ingrese nombres separados por comas: ')
nombres_lista = nombres.split(',')
nombres_conjunto = set(nombres_lista)
print('La cantidad de nombres únicos en el conjunto es: ', len(nombres_conjunto))"""

#ACTIVIDAD 2: Crea un programa que simule un inventario de productos en una tienda. Inicia con un diccionario 
# que contenga algunos productos y sus cantidades. Luego, permite al usuario agregar un nuevo producto con su cantidad y actualizar la cantidad de un producto existente. 
# Muestra el inventario actualizado.
"""
Manzanas >= 50
Bananas => 30
Peras => 40
"""

"""inventario = {'Manzanas': 50, 'Bananas': 30, 'Peras': 40}
print('Inventario actual: ', inventario)
producto = input('Ingrese el nombre del producto: ')
cantidad = int(input('Ingrese la cantidad del producto: '))
if producto in inventario:
    inventario[producto] += cantidad
else:
    inventario[producto] = cantidad
print('Inventario actualizado: ', inventario)
"""

#ACTIVIDAD 3: Crea un programa que tome una oración ingresada por el usuario y realice las siguientes operaciones: convierte la oración a mayúsculas, 
# cuenta cuántas veces aparece la palabra "python", y muestra la oración sin espacios en blanco al inicio y al final.

"""print('Bienvenido al programa de oraciones')
input('Presiona Enter para continuar')
oracion = input('Ingrese una oración: ')
oracion_mayusculas = oracion.upper()
contador_python = oracion.count('python')
oracion_sin_espacios = oracion.strip()
print('Oración en mayúsculas: ', oracion_mayusculas)
print('La palabra "python" aparece ', contador_python, ' veces')
print('Oración sin espacios en blanco al inicio y al final: ', oracion_sin_espacios)"""

#ACTIVIDAD 4: Crea dos conjuntos con números ingresados por el usuario y separados por coma. 
#Luego, muestra cuáles elementos tienen en común los conjuntos y crea un nuevo conjunto que contenga la unión de ambos.

conjunto_1 = set(input('Ingrese números separados por coma para el primer conjunto: ').split(','))
conjunto_2 = set(input('Ingrese números separados por coma para el segundo conjunto: ').split(','))
elementos_comunes = conjunto_1.intersection(conjunto_2)
union_conjuntos = conjunto_1.union(conjunto_2)  
print('Elementos en común: ', elementos_comunes)
print('Unión de conjuntos: ', union_conjuntos)



