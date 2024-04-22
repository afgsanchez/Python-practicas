a = 10
while a: # usamos la misma variable como condicion
    print(a, end=' ')
    if a == 3:
        break
    a -= 1
print ('\nFuera del Bucle.')
print('Valor de "a": {}'.format(a))
