# ejemplo donde evaluamos si un número es 
# primo o no dentro de un bucle while.

# En este caso realizamos la busqueda de factores del numero 13 y, al no 
# encontrar ninguno, no ejecutamos break. Por ello el bucle finaliza
# limpiamente y por ello se ejecuta el bloque else al final del while.

# Solicita al usuario que introduzca un número
entrada = input("Introduce un numero: ")

# Verifica si la entrada consiste solo en caracteres numéricos
if entrada.isnumeric():

# Convierte la entrada en un entero y la asigna a la variable 'a'
    a = int(entrada)

# Inicializa 'b' con la mitad de 'a'. Ningún factor de 'a' puede ser
#  mayor que la mitad de 'a'.
b = a // 2 # Esto es una division entera. Por ej: 13 // 2 == 6

# Inicia un bucle while que se ejecutará mientras 'b' sea mayor que 1.
while b > 1:

# Verifica si 'b' es un factor de 'a'. Si el residuo de 'a' dividido 
# por 'b' es cero, 'b' es un factor de 'a'.
    if a % b == 0:

# Imprime un mensaje indicando que 'b' es un factor de 'a'.
        print('{} es factor de {}'.format(b,a))

# Sale del bucle while si se encuentra un factor.        
        break

# Reduce el valor de 'b' en cada iteración para continuar 
# la búsqueda de factores.    
    b = b - 1

else:

# Si el bucle while termina limpiamente (sin encontrar factores), 
# imprime un mensaje indicando que 'a' es primo.    
    print('{} es primo'.format(a))

# Imprime un mensaje fuera del bucle. Este mensaje se imprimirá 
# independientemente de si 'a' es primo o no.
print('Fuera del bucle.')
