a = 'Python' # Ambito (Scope) Global
print('Valor fuera: ', a)

def funcion():
    a = 33
    print('Valor dentro', a) # Scope local a la funcion
funcion()

print('Valor fuera', a)
a = 'Python' # Scope global (al modulo)
