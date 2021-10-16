"""
4- Solo utilizando el bucle while borre cada uno de los elementos de la siguiente lista.
nombres = ["Juan","Romina","Tamara","Melanie"]
"""
nombres = ["Juan","Romina","Tamara","Melanie"]

a = -3

while True:
    if a < len(nombres):
        del nombres[a]
        a = a + 1
    else:
        break
print("Lista de nombres: ", nombres)