"""Crear una función que reciba dos parámetros, uno de ellos una lista de palabras, mientras que el otro una cadena de texto.
La función debe devolver una colección con las palabras de la lista pasada por parámetro, que puedan ser armadas utilizando algunas de las letras del string.

Ejemplo:
["auto", "flauta", "agua", "laguna"], "ouatg"

El resultado sería ["auto", "agua"]."""

# definición de las variables
lista_palabras = ["auto", "elefente", "palanca", "hadoooken", "electricista", "palangana", "almohada"]
cadena = "el murciélago se atoró en la trompeta de guido higuera"

#solución
def palabras(lista, string):
    lista2 = []
    for palabra in lista:
        if all(palabra.count(letra) <= string.count(letra) for letra in palabra): #se cuenta la cantidad de veces que aparece cada letra de la palabra en el string
            lista2.append(palabra) #si la cantidad de veces que aparece cada letra de la palabra en el string es menor o igual a la cantidad de veces que aparece en la palabra, se agrega la palabra a la lista
    return lista2

print(palabras(lista_palabras, cadena))

#Otra forma de hacerlo
def words_from_string(words, string):
    from collections import Counter #Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
    string_counter = Counter(string)
    return [word for word in words if not Counter(word) - string_counter] # Counter(word) - string_counter returns the difference between the two counters, which is an empty counter if all the elements in word are in string_counter, thats why we use not to return True if the difference is empty

print(words_from_string(lista_palabras, cadena))