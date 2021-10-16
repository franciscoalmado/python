"""
Crear una función rango(desde, hasta, intervalo) que retorne una lista de números, tal como la función incorporada range(), aunque según el intervalo especificado.
(No puede usar la función range() para resolver este ejercicio)
Por ejemplo, el siguiente código:
lista = rango(1, 10, 2)
print(lista)
debe imprimir:
[1, 3, 5, 7, 9]
Puesto que se genera una lista desde 1 hasta 10 con un intervalo de 2.
Tomar como base el código de la función rango() que se encuentra en el material del alumno.
"""

def rango(desde, hasta, intervalo):
    numeros = []
    while desde < hasta:
        numeros.append(desde)
        desde = desde + intervalo
    return numeros


lista = rango(1, 10, 2)
print(lista)