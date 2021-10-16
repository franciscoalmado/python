"""
Se tiene la “matriz” (una lista de listas):
m = [ [10,50,5], [20,30,70], [15,45,80]].
Recorrerla con 2 sentencias ‘for’ para mostrar cada uno de los elementos que la componen.
"""
m = [[10,50,5], [20,30,70], [15,45,80]]

for i in m:
    for j in i:
        print(j)