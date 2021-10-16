"""
1. Crear un programa que solicite una fila y una columna e imprima en pantalla el número en esa posición según la siguiente matriz:
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

Un ejemplo de entrada (lo que escribe el usuario) y salida (lo que se imprime en pantalla) es el siguiente (los caracteres en rojo son ingresados por el usuario):
Fila: 1
Columna: 2
6.4

El resultado es 6.4 puesto que es el valor ubicado en
matriz[1][2].

2. El programa debe chequear que la fila y la columna tengan valores válidos. En este caso, las únicas filas válidas son 0 y 1; las columnas, 0, 1 y 2. Si alguno de los dos valores es inválido, debe mostrar un mensaje de error.
"""
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
print(matriz)

fila = input("Introduzca el número de la fila: ")
fila = int(fila) 
columna = input("Introduzca el número de la columna: ")
columna = int(columna)

if fila < len(matriz):
    if columna < len(matriz[fila]):
        print(matriz[fila][columna])
    else:
        print("Error en las columnas")
else: print("Error en las filas")