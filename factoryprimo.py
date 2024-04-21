def factor(x):
    lista = list(range(2, x))
    factores = []
    for i in lista:
        if x % i == 0:
            factores.append(i)
            print(i)
    if not factores:
        print("El numero" , x,"es primo")
    else:
        print("El numero" , x,"no es primo") 
factor (1492)

    
