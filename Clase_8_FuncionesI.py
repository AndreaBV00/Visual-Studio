#Qué son las funciones??
"""Las funciones son bloques de código que se pueden reutilizar en distintas partes de un programa.
Las funciones pueden recibir parámetros y devolver un valor.
Las funciones se definen con la palabra reservada def.
Las funciones guardan una lógica, un algoritmo que se ejecuta cuando se invoca la función.
Las funciones pueden devolver un valor con la palabra reservada return.
Las funciones pueden no devolver nada, en cuyo caso devuelven None.
Las funciones pueden recibir parámetros, que son los valores que se le pasan a la función para que esta los utilice.
En python existen funciones integradas en el lenguaje, como print, len, etc.
Las funciones se guardan en la memoria y se pueden invocar en cualquier parte del programa.
Para modificar el código de una función, se debe modificar su definición. Es mas sencillo que repetir, porque lo cambiamos en un solo lugar."""

#función para sumar dos números, recibe dos parámetros y devuelve la suma de ambos
"""def calcular_suma(a, b):
    return a + b
print(calcular_suma(5, 3)) #8
print(calcular_suma(2, 2)) #4
"""
#generalizar la función para sumar dos números, para que haga cualquier operación
"""
def calcular(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        return a / b
    else:
        return "Operación no válida"    

print(calcular(5, 3, "suma")) #8
print(calcular(5, 3, "resta")) #2
print(calcular(5, 3, "multiplicacion")) #15
print(calcular(5, 3, "division")) #1.6666666666666667
"""
#para que los resultados salgan por terminal, hay que poner print. Si no se ejecuta y no se ve el resultado
#si no se pone return, la función devuelve None
#el return corta la ejecución de la función, no se ejecuta nada más después de return
#las variables que se crean dentro de una función, solo existen dentro de la función, no se pueden usar fuera de ella
#la función busca la variable dentro de la función, si no la encuentra, busca en el entorno global
#si no la encuentra en el entorno global, da error

#crea una funcion que reiba un numero y una lista e impitam todos los valores son divisibles por numero si son todos divisibles y Hay un vlor que no se puede divideir por número en caso contrario
def divisible_por_numero(numero, lista):
    for i in lista:
        if i % numero != 0:
            return "Hay un valor que no es divisible por el número"
    return "Todos los valores son divisibles por el número"

divisible_por_numero(2, [4, 6, 8, 10]) #Todos los valores son divisibles por el número
divisible_por_numero(2, [4, 6, 8, 11]) #Hay un valor que no es divisible por el número  #si pongo return en vez de print, no sale nada en consola

#crea una función que reciba una lista de números y devuelva la suma de todos los números
def suma_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

#crea una función que reciba una lista y un número y devuelva una lista con todos los números aumentodos en el valor del número pasado como parámetro

def aumentar_lista(lista, numero):
    nueva_lista = []
    for i in lista:
        nueva_lista.append(i + numero)
    return nueva_lista

print(aumentar_lista([1, 2, 3, 4], 5)) #[6, 7, 8, 9]

#crea una función que reciba una tupla de palabras y retorne una frase con las palabras separadas por un espacio

def tupla_a_frase(tupla):
    return " ".join(tupla)  #join es un método de las cadenas de texto que une los elementos de una lista o tupla con un separador
