"""
3 – Se tiene el siguiente diccionario: 
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
Y se tiene una lista de edades vacía. 
edades = []
Cree un algoritmo, que vuelque solo las edades en la lista edades,(código no a mano).
Una vez que este cargada la lista, calcule el promedio utilizando todo lo aprendido, solo lo aprendido. 
"""

personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
edades = []

for edad in personas:
    edades.append(personas[edad])
    
print("La lista de edades del diccionario Personas, es: ", edades)

suma_edades = 0

for edad in edades:
    suma_edades = suma_edades + edad

promedio_edades = 0
promedio_edades = suma_edades / len(edades)

print("El promedio de edades de la lista es: ", promedio_edades)





