"""
Se quiere buscar los múltiplos de 3 y de 5 en un rango que ingrese el usuario. Guardar los múltiplos en una lista. La única limitación al resolver este ejercicio, es que estamos obligados a usar un “for” asociado a un range como vimos en la teoría.
"""
inicio = input("Ingrese el numero de incio del rango: ")
inicio = int(inicio)

final = input("Ingrese el numero del final del rango: ")
final = int(final)

multiplos = []

for n in range(inicio,final+1,1):
	if n%3 == 0 and n%5 == 0:
		multiplos.append(n)

print("Los multiplos de 3 y de 5 en ese rango son: ")
print(multiplos)