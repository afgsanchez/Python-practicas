# comprobar si un numero es primo
def isPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True
        
def app():
    num = int(input('Escribe un numero: '))
    result = isPrimo(num)

    if result is True:
        print('El numero', num, 'es primo')
    else:
        print('El numero', num, 'no es primo')

if __name__ == '__main__':
    app()