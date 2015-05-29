#Text to speech example
# Speech synthetizer: eSpeak

'''Para empezar hay que forzar a que se use la salida de Headphones de
Raspberry, o yendo a pyhtonGames y forzando headphones o
escribiendo: amixer cset numid=3 1
'''
#Importamos los módulos apropiados que tienen funciones que nos serán útiles luego
import os, time

#Creamos una función.
''' Una función es un pedazo de código que se va a usar muchas veces.
En vez de escribirlo como los anteriores, lo escribimos en la forma
de función que tendrá un nombre apropiado. Cada vez que llamemos a
esa función por su nombre se ejecutara el pedazo de código que contiene.
Además permite aceptar parámetros y devolver un resultado.
Ejemplo: función suma. ¿Cómo se escribiría en nuestro lenguaje?
'''
#1) Primero definimos la función con "def" + nombreFuncion + (parametros...):
def suma(num1, num2):
    return num1 + num2

#2) Luego la usamos desde nuestro código:
resultado = suma (3, 5)
print(resultado)


#Para nuesto conversor de texto a voz, primero definimos una función
#que acepta una variable (texto = string = "bla bla" = 'bla bla') como parámetro:
def robot(text):
    os.system("espeak ' " + text + " ' ")

robot("Hola soy un texto hablado por un sintetizador con acentazo inglés")
