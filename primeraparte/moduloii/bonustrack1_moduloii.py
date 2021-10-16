"""
1. Realizar un programa que, ingresando la edad de una persona, determine si es menor, mayor con edad laboral o jubilado (contemplando jubilado para ambos sexos a los 65 años).
"""
edad = input("Ingrese su edad: ")
edad = int(edad)

if edad < 18:
    print("Menor de edad")
elif edad >= 18 and edad < 65:
    print("Mayor, con edad laboral")
elif edad >= 65:
    print("Jubilado")