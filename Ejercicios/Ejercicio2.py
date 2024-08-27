"""3) El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

In [1]:
numero_1 = 9
numero_2 = 3
numero_3 = 6
​
media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
La nota media es 14.0
"""
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3)/ 3
print("La nota media es", media)


"""4) A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos 
obtener la nota media. Cada nota tiene un valor porcentual:

La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total
Ejemplos:
nota_1 = 10
nota_2 = 7
nota_3 = 4
"""

"""5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado
de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?


Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista
Partirás de: 
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
Debes llegar a: 
matriz = [ 
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]

"""

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

# Asegurar que cada fila tiene el cuarto elemento correcto
for fila in matriz:
    suma_tres_primeros = sum(fila[:3])  # Sumar los tres primeros elementos
    if len(fila) == 3:  # Si la fila tiene solo tres elementos, agregar el cuarto
        fila.append(suma_tres_primeros)
    else:  # Si ya tiene cuatro elementos, corregir el cuarto si es necesario
        fila[3] = suma_tres_primeros

# Imprimir la matriz corregida
for fila in matriz:
    print(fila)