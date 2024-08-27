#calse 7, métdos de colecciones
name = "Sergio"
print(name.upper()) #metodo de la clase string, devuelve el string en mayusculas
print(name.lower()) #metodo de la clase string, devuelve el string en minusculas
print(name.capitalize()) #metodo de la clase string, devuelve el string con la primera letra en mayuscula
print(name.title()) #metodo de la clase string, devuelve el string con la primera letra de cada palabra en mayuscula
print(name.swapcase()) #metodo de la clase string, devuelve el string con las mayusculas en minusculas y viceversa
print(name.center(50)) #metodo de la clase string, devuelve el string centrado en 50 caracteres
print(name.ljust(50)) #metodo de la clase string, devuelve el string justificado a la izquierda en 50 caracteres
print(name.rjust(50)) #metodo de la clase string, devuelve el string justificado a la derecha en 50 caracteres
print(name.zfill(50)) #metodo de la clase string, devuelve el string rellenado con ceros a la izquierda en 50 caracteres
print(name.count("e")) #metodo de la clase string, devuelve la cantidad de veces que aparece la letra "e" en el string
print(name.find("e")) #metodo de la clase string, devuelve la posicion de la primera aparicion de la letra "e" en el string
print(name.rfind("e")) #metodo de la clase string, devuelve la posicion de la ultima aparicion de la letra "e" en el string
print(name.index("e")) #metodo de la clase string, devuelve la posicion de la primera aparicion de la letra "e" en el string
print(name.rindex("e")) #metodo de la clase string, devuelve la posicion de la ultima aparicion de la letra "e" en el string
print(name.startswith("S")) #metodo de la clase string, devuelve True si el string empieza con la letra "S"
print(name.endswith("o")) #metodo de la clase string, devuelve True si el string termina con la letra "o"
print(name.count("e")) #metodo de la clase string, devuelve la cantidad de veces que aparece la letra "e" en el string
print(name.replace("e", "a")) #metodo de la clase string, reemplaza la letra "e" por la letra "a"
print(name.split("r")) #metodo de la clase string, divide el string en una lista de strings, separando por la letra "r"
print(name.insert(3, "a")) #metodo de la clase string, inserta la letra "a" en la posicion 3 del string

lista = [5-3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
lista.sort() #metodo de la clase list, ordena la lista de menor a mayor
print(lista)
lista.sort(reverse=True) #metodo de la clase list, ordena la lista de mayor a menor
print(lista)
lista.reverse() #metodo de la clase list, invierte el orden de la lista
print(lista)    
lista.append(11) #metodo de la clase list, agrega el numero 11 al final de la lista
print(lista)    
lista.insert(3, 3) #metodo de la clase list, inserta el numero 3 en la posicion 3 de la lista
print(lista)
lista.pop() #metodo de la clase list, elimina el ultimo elemento de la lista
print(lista)    
lista.remove(3) #metodo de la clase list, elimina el primer elemento que coincida con el numero 3
print(lista)
lista.clear() #metodo de la clase list, elimina todos los elementos de la lista
print(lista)

set1 = {1, 2, 3, 4, 5}
set2 = set1.copy() #metodo de la clase set, devuelve una copia del set, otro espacio en memoria
set1.isdisjoint(set2) #metodo de la clase set, devuelve True si los sets no tienen elementos en comun
set1.issubset(set2) #metodo de la clase set, devuelve True si el set1 es un subconjunto de set2
set1.issuperset(set2) #metodo de la clase set, devuelve True si el set1 es un superconjunto de set2
set1.union(set2) #metodo de la clase set, devuelve la union de los sets
set1.intersection(set2) #metodo de la clase set, devuelve la interseccion de los sets   

cadena = "Hola Mundo"
cadena2 = "Hola Mundo"

mi_lista = [1, 2, 3, 4, 5]
mi_lista.pop(1)
print(mi_lista) 