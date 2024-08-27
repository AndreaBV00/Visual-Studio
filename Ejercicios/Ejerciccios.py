"""
ACTIVIDAD Nº6
Consigna

A partir de una lista realizar las siguientes tareas sin modificar la lista original:

Borrar los elementos duplicados
Ordenar la lista de mayor a menor
Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
Realizar una suma de todos los números que quedan (sum(lista))
Añadir como primer elemento de la lista la suma realizada insert(0, suma)
Devolver la lista modificada
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
Nota: Recuerda que para sumar todos los números de una lista puedes usar sum
"""
"""
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17] #14 elementos

lista2 = lista.copy() #14 elementos

#Borrar los elementos duplicados
lista2 = list(set(lista2)) #11 elementos
print(lista2)
"""
#Ordenar la lista de mayor a menor
"""lista2.sort(reverse=True) #11 elementos
print(lista2)

#Eliminar todos los números impares
for i in lista2:
    if i % 2 == 1:
        lista2.remove(i) #6 elementos
print(lista2)        
        
#Realizar una suma de todos los números que quedan
suma = sum(lista2) #6 elementos
print(suma)

#Añadir como primer elemento de la lista la suma realizada
lista2.insert(0, suma) #7 elementos 

#Devolver la lista modificada   
print(lista2)

#comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
print(lista2[0] == sum(lista2[1:])) #True"""

"""
ACTIVIDAD Nº3
Consigna

Realiza los ejercicios 1, 2, 3, 4, 5 y 6.

Formato


Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.

"""
"""
print('Bienvenido al programa de operaciones matemáticas')
input('Presiona Enter para continuar')
numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))
opcion = 0
print('Menú de opciones')
print('1. Mostrar una suma de los dos números')
print('2. Mostrar una resta de los dos números (el primero menos el segundo)')
print('3. Mostrar una multiplicación de los dos números')
print('4. Salir')
while opcion != 4:
    opcion = int(input('Ingrese la opción deseada: '))
    if opcion == 1:
        print('La suma de los dos números es: ', numero_1 + numero_2)
    elif opcion == 2:
        print('La resta de los dos números es: ', numero_1 - numero_2)
    elif opcion == 3:
        print('La multiplicación de los dos números es: ', numero_1 * numero_2)
    elif opcion == 4:
        print('Gracias por utilizar el programa')
    else:
        print('La opción ingresada no es válida. Intente nuevamente.')
"""

"""
2)  Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

"""
"""print('Bienvenido al programa de números impares')
numero = 0
while numero % 2 == 0:  
    numero = int(input('Ingrese un número impar: '))
    if numero % 2 == 0:
        print('El número ingresado no es impar. Intente nuevamente.')
    else:
        print('El número ingresado es impar. Gracias por utilizar el programa')"""
        
"""
3) Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:

🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números."""

"""lista = list(range(1, 101, 2))
print(lista)
suma = sum(lista)   
print(suma)
"""

"""
4) Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
"""
"""total_numeros = int(input('¿Cuántos números desea introducir? '))
numeros = []
for i in range(total_numeros):
    numero = float(input('Ingrese un número: '))
    numeros.append(numero)  
media = sum(numeros) / total_numeros
print('La media aritmética de los números ingresados es: ', media)"""

"""5) Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).
"""
"""numeros = list(range(10))
numero = -1 
while numero < 0 or numero > 9:
    numero = int(input('Ingrese un número entero del 0 al 9: '))
    if numero < 0 or numero > 9:
        print('El número ingresado no es válido. Intente nuevamente.')
    else:
        if numero in numeros:
            print('El número ingresado se encuentra en la lista de números.')
        break
"""

"""6) Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

"""      

mi_lista = list(range(11))
print(mi_lista)
mi_lista = list(range(-10, 1))
print(mi_lista)
mi_lista = list(range(0, 21, 2))
print(mi_lista)
mi_lista = list(range(-19, 0, 2))
print(mi_lista)
mi_lista = list(range(0, 51, 5))
print(mi_lista)
