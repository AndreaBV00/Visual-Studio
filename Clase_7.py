
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
