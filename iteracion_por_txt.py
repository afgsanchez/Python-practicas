# Creamos una variable tipo string para luego grabarla en el archivo.
zen = '''\
Bello es mejor que feo.
Explicito es mejor que implicíto.
Simple es mejor que complejo.
Complejo es mejor que complicado.
'''

# Abrimos/creamos el archivo txt en modo escritura (w)
f = open('short.zen.txt', 'w')
# Grabamos la variable zen en el archivo.
f.writelines(zen)
# Cerramos el archivo txt
f.close()


# Ahora leemos el archivo txt linea a linea
# Abrimos el archivo en modo lectura (r)
f = open('short.zen.txt', 'r')

# Cada vez que ejecutemos la siguiente linea nos devolvera por 
# pantalla una linea del archivo de texto.
# f.readline()

# Tambien podemos recorrer las lineas usando un bucle for:
for i in open('short.zen.txt'):
    print(i.upper(), end=' ')
    