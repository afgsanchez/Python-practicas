# creamos una lista con las letras del abecedario
letras = list('abcdefghijklmnopqrstuvwxyz')
for i in letras:
    print(i, end=' - ')

print() # este es solo para hacer un salto de linea

for e in letras:
    print(e)

# ----------------------------------
# Ahora creamos una lista de numeros que esten en un rango 
# de entre -5 y 5
lista2 = list(range(-5, 5))
print(lista2)
#-----------------------------------
# Ahora el mismo tip de lista pero nos devolvera los valores 
# en saltos de 2 en 2
lista3 = list(range(-5, 5, 2))
print(lista3)
#---------------------------------
# Ahora vamos a crear un lista de 10 numeros al azar comprendidos entre
# 0 y 25.
# Uasermos la libreria random patra generar los nuemros aleatorios
import random

# Creamos un conjunto para almacenar los números aleatorios únicos.
numeros_unicos = set() # set() no permite elementos duplicados

# Mientras la longitud del conjunto sea menor que 10, seguimos generando números aleatorios únicos.
while len(numeros_unicos) < 10:
    # Generamos un número aleatorio entre 0 y 25 y lo agregamos al conjunto.
    numeros_unicos.add(random.randint(0, 25))

# Convertimos el conjunto en una lista y la imprimimos.
lista4 = list(numeros_unicos)
print(lista4)
# --------------------------------
# Enumerar elementos de una lista
# para este ejemplo usaremos la lista anterior "letras"
# Nos devolvera cada valor de la lista letras en 
# una "sublista enumerada"
lista5 = list(enumerate(letras))
print(lista5) # esto nos lo devuelve en una fila tipo tupla
#
# Podemos recorrer la lista5 con un bucle for y parar cuando
# encuentre una letra en concreto, en el ejempño la w

for index, l in lista5: # usamos index  que es el indice de la para decirle
                        # lista original letras para encontrar la w
                        # ya que lista5 ahora será una lista enumerada.
    
    print(l) # imprimimos el valor de l en cada iteracion del bucle

    if l  == "w": # si enuentra la w entonces      
        break     # sale del bucle for      
    
    # --------------------------------





