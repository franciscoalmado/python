"""
7 – Un club desea crear un programa para contabilizar los deportes que realiza cada socio. Para ello debemos realizar una 
aplicación de consola la cual debe solicitar el nombre de un socio y la cantidad de deportes que practica. Estos dos valores
deben almacenarse como un diccionario de nombre club (el nombre es la clave y la cantidad
de deportes el valor, este último dato debe ser un número entero).

El menú con las opciones:
1 – Ingresar socio
2 – Ver todos los socios
3 – Ver un socio
4 – Salir

El programa debe hacer uso de 2 funciones, una para verificar ENTEROS, y otra para verificar el ingreso del nombre vacío. 
El programa no debe de terminar de forma imprevista por algún error en tiempo de ejecución.
"""
def verificar(dato):
    while dato == "" or dato == " ":
        print("Error")
        dato = input("Ingrese el dato nuevamente: ")
    return dato
    
def convertir(valor):
    while valor.isdecimal() == False:
        print("Error")
        valor = input("Ingrese valor nuevamente: ")
    return valor

socios = {}

while True:
    print("Menú:")
    print("1 – Ingresar socio.")
    print("2 – Ver todos los socios.")
    print("3 – Ver un socio.")
    print("4 - Salir.")
    opcion = input("Ingrese el número de la operación que desea ejecutar: ")
    if opcion == "1":
        nombre_socio = input("Ingrese el nombre del socio: ")
        nombre_socio = verificar(nombre_socio)
        deportes = input("Ingrese la cantidad de deportes: ")
        deportes = convertir(deportes)
        socios[nombre_socio] = deportes
        print("Se ha ingresado el socio correctamente.")
    elif opcion == "2":
        print("Los socios:")  
        for nombre in socios:
            print(str(socios))
    elif opcion == "3":
        nombre = input("Ingrese el nombre del socio: ")
        if nombre in socios:
            print("Socio:"+ str(socios[nombre]))
        else:
            print("Este socio no está registrado")
    elif opcion == "4":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")