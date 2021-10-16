"""
Escriba un programa que permita crear una lista de nombres. Para ello, el programa tiene que pedir un número y luego solicitar esa cantidad de nombres para crear la lista. Por último, el programa tiene que mostrar la lista creada recorriendo la lista con un for.
(Es similar a un ejercicio del módulo 2, pero ahora hay que verificar que la cantidad sea un número, en caso contrario volver a pedir).
"""
cantidad = input("¿Cuantos nombres desea ingresar?: ")

while cantidad.isdecimal() == False:
    print("¡Error. Solo numeros!")
    cantidad = input("Ingrese un numero: ")

cantidad = int(cantidad)
nombres = []
contador = 0

while contador < cantidad:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    contador = contador + 1

print(nombres)