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
