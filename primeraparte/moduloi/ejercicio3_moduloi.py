"""
Tomas rindió 3 exámenes, se desea saber su promedio sabiendo que:
nota_uno = 10
nota_dos = 6
nota_tres = 8

Mostrar el promedio por pantalla. Además, hacer que el programa indique si aprobó o no. (Se aprueba con 6).
"""
nota_uno = 10
nota_dos = 6
nota_tres = 8
promedio_notas = (nota_uno + nota_dos + nota_tres) / 3

print(promedio_notas)

if promedio_notas >= 6:
    print("Aprobó")
else:
    print("Desaprobó")