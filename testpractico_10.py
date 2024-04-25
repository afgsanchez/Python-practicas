# Verificar si un nuemro es capicua
a = input("Introduce un numero: ")
b = a[::-1]
if a == b:
    print("Es capicua")
else:
    print("No es capicua")
    