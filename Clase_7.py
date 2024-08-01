
#Un bucle es realizar repeticiones, se puede hacer con for o while, se le dice iteraciones
#Iterar es realizar repeticiones

"""n = int(input('Ingrese un número: '))
for i in range(n):
    print(i)
print('Finalizando la ejecución')"""
#En este caso, el bucle for se ejecutará n veces, es decir, el valor que el usuario ingrese.

#Ejemplo de bucle while
"""n = int(input('Ingrese un número: '))   
i = 0   
while i < n:
    print(i)
    i += 1
print('Finalizando la ejecución')"""
#En este caso, el bucle while se ejecutará mientras i sea menor que n, es decir, el valor que el usuario ingrese.
#Hay dos tipos de bucles, los definidos y los indefinidos
#Los bucles definidos son aquellos que se sabe cuántas veces se van a repetir
#Los bucles indefinidos son aquellos que no se sabe cuántas veces se van a repetir

#bucle while infinito

"""contrasena = 'Homero123'
valor_ingresado = input('Ingrese la contraseña: ')
while valor_ingresado != contrasena:
    print('Contraseña incorrecta')
    valor_ingresado = input('Ingrese la contraseña: ')  
print('Contraseña correcta')
print('Finalizando la ejecución')"""
#En este caso, el bucle while se ejecutará hasta que el valor ingresado sea igual a la contraseña.

"""numero = int(input('Ingrese un número: '))
i = 1
while i <= numero:
    if i > 10:
        break
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
print('Finalizando la ejecución')"""
#En este caso, el bucle while se ejecutará hasta que i sea mayor que el número ingresado o hasta que i sea mayor que 10.
#El break se utiliza para salir de un bucle.
#El continue se utiliza para saltar a la siguiente iteración de un bucle. No sigue con el código de abajo, sino que vuelve al inicio del bucle.

"""numero = int(input('Ingrese un número: '))
i = 1
while i <= numero:
    if i > 10:
        break
    print(i)
    i += 1
else:
    print('El bucle ha terminado')
    
print('Finalizando la ejecución')
"""
    
#se puede poner un else asociado a un bucla while, que se ejecuta cuando el bucle termina de ejecutarse 
#sin haber sido interrumpido por un break
#En este caso, el bucle while se ejecutará hasta que i sea mayor que el número ingresado o hasta que i sea mayor que 10.
#Si el bucle termina sin haber sido interrumpido por un break, se imprimirá 'El bucle ha terminado'.

#pass no sirve para nada, es como un comentario, pero no se puede dejar un bloque de código vacío, por lo que se pone pass
"""numero = int(input('Ingrese un número: '))
i = 1
while i <= numero:
    if i == 2:
        pass #No hace nada, si no lo pongo el código da error
    if i > 10:
        break
    print(i)
    i += 1
else:
    print('El bucle ha terminado')
    
print('Finalizando la ejecución')"""

#pido al usuario que ingrese un número, si el usuario ingresa mas de 4 veces y no lo logra adivinar, se termina el juego
#si el usuario adivina el número, se termina el juego

"""numero = int(input('Ingrese un número: '))
numero_secreto = 5
intentos = 4

while numero != numero_secreto:
    if intentos == 4:
        print('Has perdido')
        break
    else:
        print('Número incorrecto')
        intentos += 1
        numero = int(input('Ingrese un número: '))  
else:
    print('Has ganado')"""

#cargar la suma de numeros enteros ingresados por el usuario hasta que el usuario ingrese exit

"""suma = 0
while True: #Bucle infinito, se ejecutará hasta que se rompa
    valor = input('Ingrese un número: ')
    if valor == 'exit':
        break
    suma += int(valor)
print(f'La suma de los números ingresados es: {suma}')
print('Finalizando la ejecución')"""

#Ejemplo de bucle for

"""lista =[10, 20, 30, 40, 50]
lista_dobles = []
for i in lista:
    lista_dobles.append(i*2)
print(lista_dobles)"""
#En este caso, se crea una lista con los dobles de los elementos de la lista original.

"""personas = [('Juan', 25), ('María', 30), ('Pedro', 35)]
for persona in personas:
    print(f'{persona[0]} tiene {persona[1]} años')"""
#En este caso, se recorre la lista de tuplas personas y se imprime el nombre y la edad de cada persona.
"""for nombre, edad in personas:
    print(f'{nombre} tiene {edad} años')    """
#En este caso, se recorre la lista de tuplas personas y se desempaquetan los elementos de cada tupla en las variables nombre y edad.

"""paises = ['Argentina', 'Brasil', 'Chile', 'Uruguay', 'Paraguay', 'Bolivia', 'Corea del Sur'] 
#uso la estrategia del candidato para recorrer la lista de paises y ver la posicion del pais que tiene mas caracteres

candidato = paises [0]
pos_candidato = 0
for i, pais in enumerate(paises): #enumerate devuelve el indice y el valor de la lista
    if len(pais) > len(candidato):
        candidato = pais
        pos_candidato = i
print(f'El país con más caracteres es {candidato} y se encuentra en la posición {pos_candidato}')"""

#recorrer un string, coleccion de caracteres

"""nombre = 'Juan'
for letra in nombre:
    print(letra)"""
#En este caso, se recorre el string nombre y se imprime cada letra.

#range es una función que devuelve un rango de números
#range(inicio, fin, paso)
#inicio: número inicial del rango
#fin: número final del rango
#paso: incremento del rango
#Si no se especifica el inicio, se asume que es 0
#Si no se especifica el paso, se asume que es 1

"""for i in range(2, 10, 2):
    print(i)    """

mi_lista = [5, 9, 13, -4, 22, 0, 1]

for i in mi_lista:
    if i == -4:
        continue #Si encuentra un -4, se salta a la siguiente iteración
    if i == 11:
        break #Si encuentra un 11, se interrumpe el bucle
    print(i)
else:
    print('No había ningún 11 en la lista') #No se ejecuta porque el bucle fue interrumpido por el break, si no se interrumpe, se ejecuta
print('Finalizando la ejecución')

#En este caso, se recorre la lista mi_lista y se imprimen los elementos que no son -4. Si se encuentra un 11, se interrumpe el bucle y se imprime 'No había ningún 11 en la lista'. Si no se encuentra un 11, se imprime 'Finalizando la ejecución'. 

#como regla general para recorrer una colección uso un bucle for
#si no se cuantas veces se va a repetir uso un bucle while
#si tengo que recorrer una colección y necesito el indice uso enumerate
#si tengo que recorrer una colección y necesito el valor y el indice uso enumerate

 