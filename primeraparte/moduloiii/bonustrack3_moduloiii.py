"""
Crea una función que calcule el factorial de un número pasado por parámetro(argumento). Y
‘muestre’ el resultado.
Aclaración: En matemática el factorial se representa con un signo de exclamación “!” detrás de un número. Esta exclamación quiere decir que hay que multiplicar todos los números enteros positivos que hay entre ese número y el 1.
Por ejemplo, el 6 factorial ( 6! ):

6! = 1 x 2 x 3 x 4 x 5 x 6 = 720
"""

def factorial(numero):
    num = 1
    for n in range(1,numero+1,1):
        num = num * n
    print(num)

factorial(6)
