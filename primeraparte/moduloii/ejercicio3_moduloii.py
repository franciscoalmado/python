"""
Pedir la edad por teclado y comparar si, es mayor o menor de edad. No olvidar de que para poder comparar el ingreso debe ser convertido a int, ya que el usuario ingresaría un número entero.
"""
edad = input("Ingrese la edad: ")
edad = int(edad)

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
