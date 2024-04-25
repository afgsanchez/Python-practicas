# Producir la serie Fibonacci
'''
La serie de Fibonacci es una sucesión de números en la
 que cada número es la suma de los dos números anteriores.
 Comienza con 0 y 1, y la secuencia continúa indefinidamente 
 de la siguiente manera:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
'''
n = int(input("Introduce el numero de valores de 'n': "))
first = 0
second = 1
sum = 0
count = 1
print("Secuencia de Fibonacci: ")
while(count<=n):
    print(sum)
    count = count + 1
    first = second
    second = sum
    sum = first + second
