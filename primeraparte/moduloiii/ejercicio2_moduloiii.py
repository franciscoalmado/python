"""
Forzar el ingreso de solo números. Crear un programa que pida una edad, verificar que el ingreso por input sea un número entero. En caso contrario volver a pedir el ingreso.
Después decidir si por la edad la persona es mayor o menor de edad.
(Ayuda utilizar un bucle while y el método isdecimal() sobre el str en cuestión)
"""
edad = input("Ingrese edad: ")

while edad.isdecimal() == False:
	print("Error de ingreso")
	edad = input("Ingrese edad nuevamente: ")

edad = int(edad)

if edad < 18:
	print("Menor de edad")
else:
	print("Mayor de edad")