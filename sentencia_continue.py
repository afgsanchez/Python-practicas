# La sentencia continue nos permite interrumpir la 
# iteración actual:
a = 100 # Establece el valor inicial de 'a' en 7.
while bool(a):  # Comienza un bucle while que se ejecuta 
                # mientras 'a' sea verdadero (diferente de cero).

    a = a - 1 # Resta 1 del valor de 'a' en cada iteración.

    # if a % 2 == 0:  # Verifica si 'a' es un número par.
    if a % 2 != 0: # Verifica si 'a' es un numero impar    

        continue # Si 'a' es par, se salta el resto del 
                 # bucle actual y pasa a la siguiente iteración.

    print(a, end= " ") # Si 'a' no es par, imprime el valor de 'a' 
                       # seguido de un espacio en blanco.

print('\nFuera del blucle') # Imprime "Fuera del bucle" después de 
                            # que el bucle while haya terminado.
