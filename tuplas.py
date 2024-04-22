# Una tupla es una lista que una vez creada no se pueden modificar
# los valores. La tuplas van entre () mientras que las lista van entre []

# Definición de una tupla
mi_tupla = (10, 20, 30, 40, 50)

# Accediendo a elementos de la tupla
print("Primer elemento:", mi_tupla[0])  # Imprime el primer elemento de la tupla
print("Segundo elemento:", mi_tupla[1])  # Imprime el segundo elemento de la tupla
print("Quinto elemento:", mi_tupla[4])

# Intentando modificar un elemento de la tupla (esto dará un error)
# mi_tupla[0] = 100  # Esto generaria un error porque las tuplas son inmutables

# Iterando sobre los elementos de la tupla
print("Elementos de la tupla:")
for elemento in mi_tupla:
    print(elemento)

# -----------------------------------------------
# Combinando listas y tuplas
# creo un lista que contiene 3 tuplas
t = [(1, 2), (3, 4), (5, 6)] 

for g, h in t: # g, h hacen referencia a cada elemento de cada tupla
               # dentro de la lista
    print(g+h) # imprime las suma de cada tupla de la lista.

# ---------------------------------------------
