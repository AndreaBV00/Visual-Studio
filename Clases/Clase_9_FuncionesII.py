#Argumentos: son los valores que se pasan a la función
#Parámetros: son las variables que se definen en la función
#Los argumentos se asignan a los parámetros por orden
#Si se asignan por nombre, se pueden poner en cualquier orden
#Si se asignan por nombre, se pueden omitir algunos

def saluda(nombre, apellido):
    return(f"Hola, {nombre} {apellido}")

print(saluda("Juan", "Pérez")) #Hola, Juan Pérez, se pasan los parámetros por orden
print(saluda(apellido="Pérez", nombre="Juan")) #Hola, Juan Pérez, se pasan los parámetros por nombre
print(saluda("Juan", apellido="Pérez")) #Hola, Juan Pérez, se pasan los parámetros por orden y por nombre
print(saluda(apellido="Pérez", nombre="Juan")) #Hola, Juan Pérez, se pasan los parámetros por nombre (No importa el orden)


def resta(a, b):
    return a - b

print(resta(5, 3)) #2
print(resta(3, 5)) #-2
print(resta(b=3, a=5)) #2
print(resta(a=3, b=5)) #-2
#print(resta(5)) #TypeError: resta() missing 1 required positional argument: 'b'. Si tengo un error el programa se para

def resta(a=10, b=5): #Si pongo un valor por defecto, no da error, toma los valores por defecto
    return a - b

print(resta()) #5
print(resta(3)) #-2
print(resta(3, 2)) #1
print(resta(b=3)) #7
print(resta(a=3)) #2

def resta(a=None, b=None): #Si pongo None, no da error, toma los valores por defecto
    if a == None or b == None: #Si no se pasan los dos argumentos, le pido al usuario que los introduzca
        return "Error, faltan argumentos"
    else: #si no pongo el else, el programa sigue ejecutando el código, estaría bien igualmente
        return a - b 
    

#pasar el parámetro por valor o por referencia
#por valor: se crea una copia del valor y se trabaja con esa copia, no se modifica el valor original
#por referencia: se trabaja con la variable original, si se modifica la variable, se modifica el valor original
#en python, los tipos de datos inmutables se pasan por valor y los tipos de datos mutables se pasan por referencia // no lo decide el programador, lo decide el lenguaje
#los tipos de datos inmutables son: int, float, str, tuple
#los tipos de datos mutables son: list, dict, set
#si se pasa un tipo de dato inmutable a una función y se modifica, no se modifica el valor original
#si se pasa un tipo de dato mutable a una función y se modifica, se modifica el valor original

#ejemplo de paso por valor
def modificar_numero(numero):
    numero += 10
    return numero

numero = 5
print(modificar_numero(numero)) #15
print(numero) #5 // no se modifica el valor original

#ejemplo de paso por referencia

def modificar_lista(lista):
    lista.append(4)
    return lista

lista = [1, 2, 3]
print(modificar_lista(lista)) #[1, 2, 3, 4]
print(lista) #[1, 2, 3, 4] // se modifica el valor original

#recibir parametros indeterminados con *args y **kwargs
#*args: se utiliza para recibir un número indeterminado de argumentos posicionales // se pueden pasar tantos argumentos como se quiera por posición // se guarda en una tupla
#**kwargs: se utiliza para recibir un número indeterminado de argumentos por nombre // se pueden pasar tantos argumentos como se quiera por nombre // se guarda en un diccionario
#por valor = por defecto
#por referencia = por nombre

def suma(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

def suma(**args):
    return sum(args)

def resultado(nombre, *args, **kwargs):
    print(f'Hola, {nombre}! estas son tus notas:')
    for nota in args:
        print(f'nota:{nota}')
    print(f'Vamos a enviar una copia a {list(kwargs.values())}')


resultado("Mauricio", 5, 4, 6, 8, 10, padre="Roberto", madre="Mariela")

#recursiòn: una función que se llama a sí misma
#se utiliza cuando una función tiene que hacer una tarea repetitiva
#se utiliza en algoritmos de búsqueda, ordenación, etc
#hay que tener cuidado con la recursión, porque puede consumir muchos recursos
#hay que tener un caso base, que es el que corta la recursión
#hay que tener un caso recursivo, que es el que llama a la función recursiva

def factorial(n):
    if n > 1:   
        return n * factorial(n - 1)
    else:
        return 1
    
print(factorial(5)) #120
#5 * 4 * 3 * 2 * 1 = 120
#consume muchos recursos, no es muy eficiente
#por defecto python tiene un límite de recursión, si se supera, da error, para aumentar el límite, se puede hacer con sys.setrecursionlimit(10000) // no es recomendable, porque puede consumir muchos recursos