"""
Generar un programa de consola que tenga un menú y permita generar números aleatorios entre 1 y 6, como si fuera un dado.
Menú:
1. Tirar dado.
2. Salir
"""
import random

while True:
    print("Menú")
    print("1 - Tirar dado")
    print("2 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        valor = random.randint(1,6)
        print("El valor del dado es:", valor)
    elif opcion == "2":
        print(" ¡Gracias por usar nuestro programa! ")
        break
    else:
        print("¡No existe esa opción!")