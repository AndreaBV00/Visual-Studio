"""print (10/3) #division
print (10//3) #division entera
print (10%3) #modulo (el resto de la division entera)
"""
#Python primero resuelve las terminos entre paréntesis, luego potencias y multiplicaciones, luego las sumas y restas
"""
print (10**3) #potencia
"""
#función input
"""
name = input("What is your name? ")
edad = input("How old are you? ")
print("Hello " + name + "!")
print("You are " + edad + " years old")
"""
#String son un tipo de dato compuesto, es decir, una secuencia de caracteres. Tiene un orden y una posición dentro de la secuencia

#SLICING

"""frase = "Hola Mundo"
"""
"""
print(frase[0]) #H // la posición arranca a contar desde 0
print(frase[1]) #o
print(frase[2]) #l
print(frase[3]) #a
print(frase[4]) #" "
print(frase[5]) #M
print(frase[6]) #u
print(frase[7]) #n
print(frase[8]) #d
print(frase[9]) #o
"""
""""
print(frase[0:5]) #Hola // el primer número es inclusivo y el segundo es exclusivo
print(frase[5:11]) #Mundo

print(frase[1:7:2]) #oaM // el tercer número es el salto que se da entre los caracteres
print(frase[2:]) #por defecto si no pongo el final se escribe hasta el final de la frase

print(frase[::-1]) #odnuM aloH // invierte la frase
"""

#listas
#en las listas se pueden guardar diferentes tipos de datos
#si accedo con caracteres negativos, empieza a contar desde el final
#las listas son mutables, es decir, puedo modificarlas

datos = ['Ariel', 23, 1.75, True,[1,2,3]]
print(datos) 
print(type(datos)) #<class 'list'>
print(type(datos[0])) #<class 'str'>
print(type(datos[1])) #<class 'int'>
print(type(datos[2])) #<class 'float'>
print(type(datos[3])) #<class 'bool'>
print(type(datos[4])) #<class 'list'>

print(datos[-1][0]) #1
print(datos[-1][-1]) #3
print(datos[0:3]) #['Ariel', 23, 1.75]
print(datos[0:3:2]) #['Ariel', 1.75]


datos2 =[1,2,3,4,5,6,7,8,9,10]
print(datos + datos2) #['Ariel', 23, 1.75, True, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

datos[0] = 'Ari'    #modifico el primer elemento de la lista
print(datos) #['Ari', 23, 1.75, True, [1, 2, 3]]

datos.append('Python') #agrego un elemento al final de la lista
print(datos) #['Ari', 23, 1.75, True, [1, 2, 3], 'Python']


#las tuplas son inmutables, es decir, no se pueden modificar
#se pueden acceder a los elementos de la tupla con slicing
#se pueden concatenar tuplas
#se pueden multiplicar tuplas
#se pueden convertir listas en tuplas y viceversa
#se pueden desempaquetar tuplas

tupla = (1,2,3,4,5)


