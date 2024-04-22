# En este ejemplo vamos recorriendo elementos de 
# una lista de strings y vamos imprimiéndolos en pantalla

def letras():  # Definición de la función 'letras'

    for s in ['Me', 'gusta', 'Python']:  # Bucle que recorre la lista de strings
        
        print(s, end=" ")  # Imprime cada elemento de la lista seguido de un espacio
    
    print()  # Imprime una nueva línea para separar los resultados

letras()  # Llamada a la función 'letras'

#-------------------------------------

# otro ejemplo, esta vez sumando números

def numeros():  # Definición de la función 'numeros'

    a = 0  # Inicialización de la variable 'a' en cero

    for i in [1, 2, 3, 4, 5]:  # Bucle que recorre la lista de números
        
        a = a + i  # Suma cada número de la lista a la variable 'a'
        
        print(a, end=" ")  # Imprime el valor acumulado de 'a' en cada iteración
    
    print()  # Imprime una nueva línea para separar los resultados

numeros()  # Llamada a la función 'numeros'

# ------------------------------------------
# otro ejemplo, esta vez con strings, este imprimirá cada letra
# de la cadena de texto con un espacio entre cada letra
# si no ponemos la intruccion end=' ' nos imprimira una letra en cada linea.

for c in 'Me gusta Python!':
    print(c, end= ' ')
print()

# ----------------------------------
# un ejemplo recorriendo un diccionario formado por dos listas.

# Definimos dos listas
keys = ['nombre', 'apellidos', 'edad', 'Profesion']
values = ['Guido', 'van Houtten', '16', 'Python developer']

# Creamos el diccionario con las listas
d = dict(zip(keys, values))

# Iniciamos un bucle for que recorre los elementos de las listas
for k in d:
    # creamos un string con un elemento de cada lista
    info = '{}: {}'.format(k, d[k])

#imprimimos cada string en una linea
    print(info)

