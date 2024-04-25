# Contar las palabras en mayusculas de un archivo.
archivo = "short.zen.txt"
with open(archivo) as fh:
    count = 0
    text = fh.read()
    for character in text:
        if character.isupper():
            count += 1
print(count)