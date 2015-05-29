#La siguiente frase me permite poner tildes y spanish caracteres  (si no usa solo ASCII)
# -*- coding: utf-8 -*-

#Hay que poner almohadilla para escribir un comentario de una sola línea
''' Hay que poner 3 comillas simples para varias lineas de comentario:
 ¿Qué es un comentario?
# Una anotación que haces para que te resulte fácil entender lo
# que hace el código de debajo.
# Se usan porque CUALQUIER CODIGO SE LEE MAS VECES DE LO QUE SE ESCRIBE
# (no pondre tildes en ningun sitio por ahora)
'''

#Ejemplo de primera orden. print: saca en pantalla un mensaje
print("Hola, aquí habra varios comandos simples")

#Ejemplo de variable y operaciones matemáticas
print("")
print("EJEMPLO DE SUMA")
valor = 1
resultado = valor + 2
print(resultado)

# Ejemplo de como importar un módulo
print("")
print("EJEMPLO DE MODULOS")
import sys
# Ejemplo de como crear una varia
versionPython = sys.version
print("Trabajo con la version de Python:", versionPython)

#Ejemplo de donde estamos
import os
directorioActual = os.getcwd()
print("Estoy en directorioActual")



print("CONTAINERS: LISTAS Y DICCIONARIOS")
#Ejemplo de lista
print("")
print("EJEMPLO DE LISTA")
listaArchivos = os.listdir(directorioActual)
print("En este directorio hay estos archivos:", listaArchivos)
print("Número total de archivos: ", len(listaArchivos))
print("El primer archivo tiene indice 0 y se accede poniendo listaArchivos[0]:", listaArchivos[0])

#Ejemplo de condiciones:
# Si pasa la condición X, entonces haz la acción Y. Si no pasa, haz la condición Z.
# Si en la lista de archivos está el archivo simpleCommands.py, entonces dilo, si no di que no se encuentra.
print("")
print("EJEMPLO DE CONDICION IF/ELSE")
nombreArchivo = "simpleCommands.py"
if nombreArchivo in listaArchivos:
	print("Sí esta el archivo "+ nombreArchivo)
else:
	print("No he encontrado el archivo " + nombreArchivo)

#Ejemplo de bucles (se usan para hacer determinada acción sobre varios elementos - de una lista, por ejemplo -
print("EJEMPLO DE BUCLE FOR")
for elemento in listaArchivos:
	print("Elemento encontrado: " + elemento )

#Ejemplo de FOR para hacer la suma de los 10 primeros números:
print("")
print("EJEMPLO DE BUCLE FOR PARA HACER SUMA DE 10 NUMEROS")
lista10PrimerosNumeros = range(1,11)
print("Lista de numeros: ", end="") #Imprime sin salto de línea
print(*lista10PrimerosNumeros, sep=",") # Con el * se indica que imprima cada elementos de la lista, y el "sep" indica el separador entre cada elemento de la lista
resultadoSuma = 0
for i in lista10PrimerosNumeros:
    resultadoSuma = resultadoSuma + i
    print("Sumo " + str(i) + " a la suma y me queda: " + str(resultadoSuma))
print("Resultado total suma: " + str(resultadoSuma))


#Ejemplo de diccionarios:
#Un diccionario es un conjunto de datos que puedes buscar por un nombre especial llamado key (clave).
#La forma que tienen es la siguiente:
# {"key_name":"dato"}
print("")
print("EJEMPLO DICCIONARIO")
ejemploDiccionario ={"juan": "cinturon negro", "miguel":"cinturon blanco", "damian":"cinturon verde"}
for elemento in ejemploDiccionario:
    print("Clave: " + elemento[0] + ", dato: "  + elemento[1])
