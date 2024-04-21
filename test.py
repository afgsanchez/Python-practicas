# Creamos una funcion con diferentes sentencias
# a modo de prueba.
import math
import random


def manejo_de_librerias():
    # Importamos la libreria math para hacer operaciones matematicas
    # asignamos a la variable j el cubo de pi (**) (3,1416*3,1416*3,1416)
    j = math.pi ** 3
    # imprimimos j
    # Si solo ponemos un signo multiplicador * en lugar de
    # devolvernos el cubo, nos multiplica pi * 3 = 9.4247
    print(j)
    # ahora con la opcion sqrt sacamos la raiz cuadrada de 25
    k = math.sqrt(25)
    print(k)

    # Ahora vamos a importar el modulo random, para generar
    # numeros aleatorios
    m = random.random()  # esto nos genera un numero aleatorio
    # entre 0 y 0.9999999999
    print(m)

    # Ahora le damos una lista  [1, 2, 3, 4] y elige
    # un numero de la lista al azar
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(lista)
    print(n, " numero al azar de la lista")
    # Ahora para probar multiplicare un numero al azar de la lista por pi
    h = (n * math.pi)
    print(h, " el numero al azar multiplicado por pi")

    # Ahora le pasamos la funcion shuffle a la libreria random
    # la cual nos va a reordenar la lista de forma aleatoria
    random.shuffle(lista)
    # mostramos la lista por el terminal.
    print(lista, " Lista reordenada al azar")

# Aqui termina la funcion manejo_de_librerias
def factorial(x):
    print(x)
    if x>1:
        return x*factorial(x-1)
    else:
        return 1

# -------------------------------------------------
# El codigo realmente empieza a ejecutarse desde aqui.
# -------------------------------------------------
# definimos una variable x con una cadena
x = "El valor de (a+b)*c es "
# Podemos realizar multiples asignaciones
a, b, c = 4, 3, 2
# Realizamos unas operacoiones con a, b, c
d = (a + b) * c
# definimos una variable booleana
imprimir = True
# Si imprimir es True, print(x, d) y llama a la funcion factorial()
if imprimir:
    print(x, d)
    factorial(d)
# Pero si imprimir es False, print("Hello World")
else:
    print("Hello\n World!!")
    print("Como ha impreso Hello World, llamamos a la funcion manejo_de_librerias")
    manejo_de_librerias()

'''
Esto es un 
bloque de
cometarios
'''
