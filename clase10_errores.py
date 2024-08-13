#los errores detienen la ejecución del programa
#para evitar que se detenga la ejecución del programa se puede usar try y except
#try: se intenta ejecutar el código
#except: si hay un error se ejecuta el código dentro de except
#finally: se ejecuta siempre, haya o no error
#raise: se puede lanzar un error
#assert: se puede lanzar un error si no se cumple una condición
#assert condición, mensaje de error
#ejemplo de try y except

"""
try:
    print(2/0)  #se intenta dividir por cero
except ZeroDivisionError:
    print("No se puede dividir por cero")
#ejemplo de finally
try:
    print(2/0)  #se intenta dividir por cero
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto se ejecuta siempre")
    
#ejemplo de raise   
def mi_funcion(x):
    if x < 0:
        raise ValueError("El número no puede ser negativo")
    return x
print(mi_funcion(2))
print(mi_funcion(-2))

#ejemplo de assert
def mi_funcion(x):
    assert x >= 0, "El número no puede ser negativo"
    return x
print(mi_funcion(2))
print(mi_funcion(-2))

try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
except ValueError:
    print("Los valores ingresados no son correctos")
    peso = 1
    altura = 1
    exit()
imc = peso / altura**2
print("Su índice de masa corporal es:", imc)
assert imc >= 0, "El índice de masa corporal no puede ser negativo"
assert imc <= 100, "El índice de masa corporal no puede ser mayor a 100
"""



#diferentes tipos de error:
#ZeroDivisionError
#ValueError: cuando el tipo de dato es correcto pero el valor no es apropiado
#TypeError: cuando el tipo de dato no es el correcto
#NameError; cuando se usa una variable que no está definida
#IndexError: cuando se intenta acceder a un índice que no existe
#KeyError: cuando se intenta acceder a una clave que no existe
#FileNotFoundError: cuando se intenta abrir un archivo que no existe
#SyntaxError: cuando hay un error de sintaxis
#IndentationError: cuando hay un error de indentación
#AssertionError: cuando una expresión es falsa
#AttributeError: cuando se intenta acceder a un atributo que no existe
#ImportError: cuando hay un error al importar un módulo
#ModuleNotFoundError: cuando no se encuentra un módulo
#OSError: cuando hay un error del sistema operativo
#RecursionError: cuando hay un error de recursión
#MemoryError: cuando no hay suficiente memoria
#KeyboardInterrupt: cuando se interrumpe el programa con Ctrl+C
#SystemExit: cuando se llama a sys.exit()
#StopIteration: cuando se intenta acceder a un elemento que no existe

#ejemplo completo de manejo de errores, programa que calcula el índice de masa corporal
while True: 
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        imc = peso / altura**2
        print("Su índice de masa corporal es:", imc)
    except:  #si se ingresa un valor inºvalido se ejecuta el except
        print("Los valores ingresados no son correctos")
    else:
        print("No hay errores")
        break
    finally:
        print("Esto se ejecuta siempre") #sirve para limpiar recursos, cerrar conexiones con bases de datos, etc        
print("Fin del programa")  #se ejecuta siempre

        




