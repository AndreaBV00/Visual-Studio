print('Bienvenido al programa de cálculo de notas finales')
print('Por favor, ingrese las notas de los alumnos del 1 al 10')
while True:
    try:
        nota_1 = float(input('Ingrese la nota 1 (entre 1 y 10): '))
        if 1 <= nota_1 <= 10:
            break  # Si la nota está dentro del rango, salimos del bucle
        else:
            print('La nota debe estar entre 1 y 10. Intente nuevamente.')
    except ValueError:
        print('Por favor, ingrese un número válido.')
        nota_1 = float(input('Ingrese la nota 1 (entre 1 y 10): '))
        if 1 <= nota_1 <= 10:
            break  # Si la nota está dentro del rango, salimos del bucle
        else:
            print('La nota debe estar entre 1 y 10. Intente nuevamente.')
while True:
    try:
        nota_2 = float(input('Ingrese la nota 2 (entre 1 y 10): '))
        if 1 <= nota_2 <= 10:
            break  # Si la nota está dentro del rango, salimos del bucle
        else:
            print('La nota debe estar entre 1 y 10. Intente nuevamente.')
    except ValueError:
        print('Por favor, ingrese un número válido.')
        nota_2 = float(input('Ingrese la nota 2 (entre 1 y 10): '))
        if 1 <= nota_2 <= 10:
            break  # Si la nota está dentro del rango, salimos del bucle
        else:
            print('La nota debe estar entre 1 y 10. Intente nuevamente.')

while True:
    try:
        nota_3 = float(input('Ingrese la nota 3 (entre 1 y 10): '))
        if 1 <= nota_3 <= 10:
            break  # Si la nota está dentro del rango, salimos del bucle
        else:
            print('La nota debe estar entre 1 y 10. Intente nuevamente.')
    except ValueError:
        print('Por favor, ingrese un número válido.')
        nota_3 = float(input('Ingrese la nota 3 (entre 1 y 10): '))
        if 1 <= nota_3 <= 10:
            break  # Si la nota está dentro del rango, salimos del bucle
        else:
            print('La nota debe estar entre 1 y 10. Intente nuevamente.')

                                  
# Calculamos la nota final
nota_final = (nota_1 * 0.2 + nota_2 * 0.3 + nota_3 * 0.5) #no divido porque la suma de los pesos es 1

print('La nota final del alumno es: ', nota_final)

#lo subí a github ahora