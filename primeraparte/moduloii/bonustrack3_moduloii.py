"""
La figura 1 muestra un diagrama de flujo de como se hace para calcular un año bisiesto. La idea es llevar este algoritmo a código Python. Pedir el año por teclado. (mod significa “módulo” es la división modular %).
"""
anio = input("Introduzca el año: ")
anio = int(anio)

if anio % 400 == 0:
    print("Es bisiesto")
else:
    if anio % 4 == 0 and anio % 100 != 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")
print("Fin")