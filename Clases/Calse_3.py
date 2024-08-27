#conjuntos
conjunto = {1,2,3,4,5}
print(conjunto)
print(type(conjunto)) #<class 'set'>
#no se pueden acceder a los elementos de un conjunto con slicing
#no se pueden modificar los elementos de un conjunto
#no se pueden concatenar conjuntos
#no se pueden repetir elementos en un conjunto
#se pueden agregar elementos a un conjunto
conjunto.add(6)
#para declarar un conjunto vacío se debe hacer de la siguiente manera
conjunto_vacio = set()
print(conjunto_vacio)   #set()  //conjunto vacío
#para eliminar un elemento de un conjunto
conjunto.remove(6)
print(conjunto) #{1, 2, 3, 4, 5}
#para eliminar todos los elementos de un conjunto
conjunto.clear()
print(conjunto) #set()  //conjunto vacío

name = 'Ariel'
conjunto_a = set(name)
print(conjunto_a)  #{'A', 'r', 'i', 'e', 'l'} //conjunto de letras de la palabra Ariel
conjunto_a.update('Python') 
print(conjunto_a)  #{'A', 'r', 'i', 'e', 'l', 'P', 'o', 'n', 't', 'h', 'y'} //conjunto de letras de la palabra Ariel y Python
conjunto_a.discard('P')
print(conjunto_a)  #{'A', 'r', 'i', 'e', 'l', 'o', 'n', 't', 'h', 'y'} //conjunto de letras de la palabra Ariel y Python sin la letra P
conjunto_a.remove('H')  #si el elemento no está en el conjunto, arroja un error

vvv = {1,2,3,4,5}
