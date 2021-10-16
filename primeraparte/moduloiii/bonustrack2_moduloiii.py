"""
Escriba un programa que permita crear una lista de nombres (como en el ejercicio anterior). Luego pida un nombre y que diga cuántas veces aparece ese nombre en la lista.
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

dato = input("Ingrese nombre para verificar: ")

veces = 0

for n in nombres:
    if n == dato:
        veces = veces + 1 

print( dato + " aparece " + str(veces) + " veces")