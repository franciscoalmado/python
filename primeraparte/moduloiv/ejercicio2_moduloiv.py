"""
El ejercicio de alumnos que habíamos creado en la versión anterior del proyecto que lo resolvimos con un diccionario, ahora debemos agregarle funciones para que verifique los datos y tratar de organizar mejor para poder aprovechar la reutilización de código.
"""
def verificar(dato):
    while dato == "":
        print("Error")
        dato = input("Ingrese nuevamente: ")
    return dato

def convertir(dato):
    while dato.isdecimal() == False:
        print("Error")
        dato = input("Ingrese nuevamente: ")
    dato = int(dato)
    return dato

def mostrar(estudiantes):
    for n in estudiantes:
        print(n,"-",estudiantes[n],"cursos")

alumnos ={}

while True:
    print("Menú")
    print("1 - Mostrar alumnos y cursos")
    print("2 - Ingreso de alumno")
    print("3 - Mostrar un alumno")
    print("4 - Salir")
    opcion = input(">>> ")
    if opcion == "1": 
        mostrar(alumnos)
    elif opcion == "2":
        nombre = input("Ingrese nombre: ")
        nombre = verificar(nombre)
        cursos = input("Ingrese cursos del alumno: ")
        cursos =  convertir(cursos)
        alumnos[nombre] = cursos
        print("¡Alumno ingresado!")
    elif opcion == "3":
        nombre = input("Ingrese alumno para mostrar cursos: ")
        nombre = verificar(nombre)
        if nombre in alumnos:
            print("Los cursos de",nombre,"son",alumnos[nombre])
        else:
            print(nombre + " no tiene cursos asignados")
    elif opcion == "4":
        print("¡Gracias por utilizar nuestro programa!")
        break
    else:
        print("¡Error de opción!")