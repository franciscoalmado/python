"""
Pedir por teclado el nombre de usuario, si está vacío, volver a pedirlo hasta que se ingrese un nombre.
Luego, saludar al usuario.
"""
nombre = input("Introduzca su nombre: ")
saludo = "Buenos dias, "
frase = ". Bienvenido (a) al sistema!"

while nombre == "":
    print("Error")
    nombre = input("Introduzca su nombre: ")
print(saludo+nombre+frase)