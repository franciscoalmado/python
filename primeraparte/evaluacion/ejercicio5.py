"""
5- Cree un algoritmo para guarda cada una de las personas del diccionario personas en un txt. 
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
El nombre se tiene que guardar en minúsculas. Y cada persona debe quedar renglón en renglón con un guion del medio separando 
el nombre y la edad.
Ejemplo:
juan - 20 
Trabajar el archivo en modo Write
"""
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

archivo = open('diccionario-personas.txt', 'w')

for nombre,valor in personas.items():
    archivo.write(nombre.lower() +' - '+str(valor)+'\n')

archivo.close()