# Como las tuplas son inmutables, si queremos añadir algo a una tupla
# primero debemos convertirla a lista, luego le añadimos lo que 
# queremos y la volvemos a convertir a tupla.

# Creamos la tupla
tup = (2, 3, 4, 5, 6)
# Imprimimos en pantalla la tu`la inicial para verificar:
print("Tupla inicial: ", tup)

# Ahora cogemos los datos de la tupla y la pasamos a lista.
lista = list(tup)

# Le agregamos un nuevo elemento entero (int) solicitandoselo al usuario.
lista.append(int(input("Introduce un nuevo entero para añadir a la tupla: ")))
# El elemento ya se ha añadido con el codigo de la linea anterior.

# Convertimos la lista de nuevo a tupla.
tup = tuple(lista)

# Imprimimos otra vez la tupla para ver los cambios.
print("Tupla final: ", tup)
