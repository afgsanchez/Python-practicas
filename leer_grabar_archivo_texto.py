# -------------------------------------------------
# ejemplo para leer un archivo y 
# guardarlo en un diccionario
# Usaremos las librerias Path y Pickle
import pickle
from pathlib import Path

# Creamos un diccionario vacio
d = dict()

# Solicitamos el nombre del archivo a cargar en el diccionario
file_name = input("Nombre del archivo a cargar: ")

# Comprobamos si existe
path = Path(file_name)
if path.is_file():
    # Abrimos el arcjhivo en modo lectura
    input_file = open(file_name, 'rb')
    # cargamos los datos del archivo en el diccionario
    d = pickle.load(input_file)
    # cerramos el archivo
    input_file.close()
else:
    print("El archivo no existe, no se cargará nada en el diccionario")
# vemos el contenido del diccionario.
print (d)    

# Ahora va a pedir un numero de documento al usuario
# Si existe mostrará la edad asoaciada a ese documento
# Si no existe, pedirá la edad y la agregará al diccionario.
document_number = input("Introduce un numero de documento: ")

# Ahora cimprueba si existe y si existe muestra la edad.
if document_number in d:
    print("La edad de " + document_number + " es " + str(d[document_number]))

# Si no existe pide la edad y lo agrega al diccionario.
else:
    age = input("Introduce la edad: ")
    # verifica que el dato sea numerico.
    if age.isnumeric():
        # Convierte el valor a entero en una variable llamada num
        num = int(age)
        # Lo añade al diccionario
        # d es la variable del diccionario [document_number] es 
        # la variable del numero introducido por el usuario 
        # y num es la variable de la edad
        d[document_number] = num
        print("Añadido al diccionario.")

# Ahora vamos a guardar los datos del diccionario en el archivo
# y cerramos el archivo
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()


