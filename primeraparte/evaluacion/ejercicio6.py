"""
6- Leer el archivo datos.txt y crear un algoritmo para reportar la suma de los renglones. 
Ejemplo: “10,20,30”  La suma del renglón 1 es 60
"""
f = open("datos.txt", "r")
d = f.readlines()
f.close()

for n in d:
    lista = ((n.strip()).split(","))
    suma = 0
    for x in lista:
        suma = suma + int(x)
    print("La suma del renglón es:", suma)