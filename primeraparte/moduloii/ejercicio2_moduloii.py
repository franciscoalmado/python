"""
Crear un programa que solicite el nombre de un alumno a través de la consola, y luego chequee que no esté vacío. En caso de estarlo, debe imprimir un mensaje de error; en caso contrario, imprimir un mensaje indicando que se ingresó correctamente.
"""
nombre_alumno = input("Introduzca el nombre del alumno: ")

if nombre_alumno == "":
    print("Error. El nombre ingresado no es válido.")
else:
    print("El nombre se ingresó correctamente")