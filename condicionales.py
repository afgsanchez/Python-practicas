print("-------------------------------------")
a = 1
b = 3
if a > b:
    print('se cumple la primera condicion')
elif a == b:
    print('a es igfual a b')
else:
    print('no se cumple la primera condicion')
    
if b > 3:
    print('se cumple la segunda condicion')
else:
    print('no se cunple la segunda condicion')    

print('ya estamos fuera del if')
print("-------------------------------------")
# ----------------------------------
# operador ternario
c = 10
d = 3
e = ("texto" if c > d else "texto2")
print(e)
print("-------------------------------------")
#--------------------------------------
# El siguiente codigo determina si una entrada es un entero, un float
# o un texto
'''
entrada = input("Escribe algo: ")
try:
    entrada = int(entrada)
    print(entrada, " Es un entero")
    exit()
except ValueError:
    pass
try:
    entrada = float(entrada)
    print(entrada," Es un float")
    exit()
except ValueError:
    pass

print(entrada, " Es un string")

print("-------------------------------------")
'''
# -------------------------------------------
# este codigo comprieba la entrada por teclado y si es un numero
# lo añade a la lista que en un principio esta vacia.
l = list () #creo una cadena vacia
texto = input("Escribe un numero: ")
if texto.isnumeric():
    num = int(texto)
    l.append(num)
    print ("Numero " + str(num) + " añadido a la lista")
else:
    print("No es un numero entero")    
texto2 = input("Escribe otro numero: ")
if texto2.isnumeric():
    num = int(texto2)
    l.append(num)
    print("Numero " + str(num) + " añadido tambien")
else:
    print("No es un numero entero")
print(l)
print("-------------------------------------")
# -----------------------------------------------
# este codigo comprueba si el numero de documento introducido
# esta en un diccionario y nos devuelve la edad.
# si no existe nos pide la edad y añade el documento y la edad.
d = {"43102133" : 48, "4235706" : 47}   # este es el diccionario
docu = input("Introduce un documento: ")
if docu in d:   # comprobamos si el documento introducido exsite en el diccionario
    print( "La edad de " + docu + " es " + str(d[docu]))
else:
    edad = input("No existe, vamos a agregarlo. Edad?: ")
    if edad.isnumeric():
        edi = int(edad)
        d[docu] = edi
        print("Añadido al diccionario")
print(d)
print("-------------------------------------")






