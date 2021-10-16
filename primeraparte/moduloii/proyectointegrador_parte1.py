"""
Una universidad desea crear un programa para contabilizar los cursos que tiene cada alumno. Para ello debemos realizar primero una aplicación de consola la cual debe solicitar el nombre de un alumno y la cantidad de cursos en la que se encuentra inscripto. Estos dos valores deben almacenarse como una lista de dos elementos (el nombre y la cantidad de cursos como un número entero) en una lista de alumnos.

El programa debe solicitar ahora el nombre de un alumno y la cantidad de cursos en la que se encuentra inscripto. Estos dos valores deben almacenarse como una lista de dos elementos (el primero el nombre, el segundo la cantidad de cursos como un número entero) en una lista de alumnos.

Una vez hecho esto, debemos hacer que el programa, al iniciar, pregunte cuál de las siguientes dos operaciones se debe realizar: ingresar un alumno o ver la lista de alumnos ingresados.

Un ejemplo de lo que debe aparecer en consola, en una posible implementación, es lo siguiente:

Ingrese el número de la operación que desea ejecutar:
1 - Añadir un alumno a la lista.
2 - Ver la lista de alumnos.
3 - Salir.

Esto debe preguntarse infinitamente hasta que el usuario escriba “3”. 
"""
alumnos = []

while True:
    print("Menu ")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Salir.")
    opcion = input("Ingrese el número de la operación que desea ejecutar: ")
    if opcion == "1":
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        cursos = input("Ingrese la cantidad de cursos: ")
        cursos = int(cursos)
        if nombre_alumno == "":
            print("Error: no ha ingresado un nombre válido")
        else:
            alumnos.append([nombre_alumno, cursos])
            print("Has ingresado el alumno correctamente")
    elif opcion == "2":
        for alumno in alumnos:
            nombre_alumno = alumno[0]
            cursos = alumno[1]
            print(nombre_alumno + " - " + str(cursos) + " cursos")
    elif opcion == "3":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")