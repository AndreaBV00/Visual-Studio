#Flujo de un algoritmo:
#1. Inicio
#2. Entrada de datos
#3. Procesamiento
#4. Salida de datos
#5. Fin



#Condicionales
#Estructura de un condicional en Python
# if condicion:
#     bloque de código
# else:
#     bloque de código

#Ejemplo de condicional
#numero = 5
#if numero > 0:
#    print('El número es positivo')
#else:  
#    print('El número es negativo')

name = input('Ingrese su nombre: ')
if len(name) > 5:
    print('Tu nombre tiene más de 5 caracteres')
if name[0] == 'A':
    print('Tu nombre empieza con la letra A')
if name == name.capitalize():
    print('Tu nombre está bien escrito')
print('Finalizando la ejecución')

#if condicion:
#    bloque de código
#elif condicion:
#    bloque de código
#else:  
#    bloque de código
