"""
Escriba un programa que permita crear una lista de nombres. Para ello, el programa tiene que pedir un número y luego solicitar esa cantidad de nombres para crear la lista. Por último, el programa tiene que mostrar la lista creada.
(Verificar que la cantidad sea un número, en caso contrario volver a pedir).
"""
cantidad_de_nombres = input("Cantidad de nombres a ingresar: ")
cantidad_de_nombres = int(cantidad_de_nombres)

nombres = []

contador = 0

while contador < cantidad_de_nombres:
    nombre_por_teclado = input("Ingrese un nombre: ")
    nombres.append(nombre_por_teclado)
    contador = contador + 1
print(nombres)