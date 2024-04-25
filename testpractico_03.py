# Suma de los elementos de una tupla.

test_tup = (7, 8, 9, 1, 10, 7)
print("La tupla original es: " + str(test_tup))
res = sum(list(test_tup))
print("La suma de los elementos de la tupla es: " + str(res))

# Realmente la conversion a string en las lineas de print no es
# necesaria en Pyhton, es capaz de concatenar sin hacer la conversion.