"""
Escribir un programa que cree un diccionario vacío y lo vaya llenando con personas. Donde el nombre(str) será la clave(el key) y el valor(value) la edad(int).

El programa debe estar acompañado de un menú:
Menú:
A) Agregar.
B) Mostrar el más chico.
C) Mostrar el más grande.
D) Salir.

La opción de agregar inserta a una persona. Mostrar el más chico, nos debería mostrar el nombre de la persona más chica, y viceversa el de mostrar el más grande. Con la opción 4 deberíamos salir del programa. 
"""
def agregar_persona():
    nombre = input("Ingrese el nombre: ")
    nombre = ingresar_nombre(nombre)
    edad = input("Ingrese la edad: ")
    edad = convertir_edad(edad)
    personas[nombre] = edad

def ingresar_nombre(nombre):
    while nombre == "" or nombre == " " or nombre == "*":
        print("Error")
        nombre = input("Ingrese el nombre nuevamente: ")
    return nombre

def convertir_edad(edad):
    while edad.isdecimal() == False:
        print("¡Error!")
        edad = input("Ingrese la edad nuevamente: ")
    return int(edad)

def mostrar_persona_chica():
    edad_limite_superior = 100 
    nombre = ""
    for n in personas:
        if personas[n] < edad_limite_superior:
            edad_limite_superior = personas[n]
            nombre = n
    return nombre

def mostrar_persona_grande():
    edad_limite_inferior = 0 
    nombre = ""
    for n in personas:
        if personas[n] > edad_limite_inferior:
            edad_limite_inferior = personas[n]
            nombre = n
    return nombre

personas = {}

while True:
    print("Diccionario de Personas:")
    print("1 - Agregar")
    print("2 - Mostrar el más chico")
    print("3 - Mostrar el más grande")
    print("4 - Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agregar_persona()
        print("¡La persona se agregó exitosamente!")
    elif opcion == "2":
        print(mostrar_persona_chica() +" es la persona más chica")
    elif opcion == "3":
        print(mostrar_persona_grande() +" es la persona más grande")
    elif opcion == "4":
        print("¡Gracias, hasta la próxima!")
        break
    else:
        print("¡Error de opción! Elija nuevamente")