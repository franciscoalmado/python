"""
Crea una función que reciba un dato ingresado por teclado(str), que verifique que sea un número entero posible de convertir (a int), y si no lo es vuelva a pedir ese dato, hasta que sea posible de convertirlo. Luego que retorne el entero convertido.
"""
def convertir(dato):
    while dato.isdecimal() == False:
        print("¡Error!")
        dato = input("Ingrese nuevamente: ")
    return int(dato)

dato = input("Ingrese su edad: ")

if convertir(dato) < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")