#Scripts, módulos y paquetes
# En esta clase vamos a ver cómo organizar nuestro código en scripts, módulos y paquetes.
#¿Qué es un script? Un script es un archivo que contiene código fuente de un programa. En Python, los scripts son archivos con extensión .py. Los scripts pueden 
# ser ejecutados directamente por el intérprete de Python. Pueden recibir argumentos desde la línea de comandos y pueden importar módulos y paquetes.

# import sys #importamos el módulo sys
# print(sys.argv) #imprimimos la lista de argumentos que recibe el script desde la línea de comandos
# print(sys.argv[0]) #imprimimos el nombre del script
# print(sys.argv[1]) #imprimimos el primer argumento
# print("Hola", sys.argv[1]) #imprimimos un saludo con el primer argumento
#Para ejecutar el script desde la línea de comandos, escribimos python script.py arg1 arg2 arg3

#¿Qué es un módulo? Un módulo es un archivo que contiene código fuente de un programa. En Python, los módulos son archivos con extensión .py. Los módulos pueden ser
# importados por otros módulos o scripts. Los módulos pueden contener variables, funciones, clases, etc. Los módulos pueden ser reutilizados en diferentes programas.

from func_mate import suma, resta #importamos las funciones suma y resta del módulo func_mate
from personas import persona #importamos la clase persona del módulo personas
