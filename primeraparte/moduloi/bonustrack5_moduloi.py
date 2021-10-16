"""
Un empleado cobro 300 dólares por mes desde enero a junio, 500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre. Hace un programa que calcule el sueldo promedio. Y que diga si este “empleado” esta cobrando un sueldo bajo, normal o mejor de lo normal.
a. Sueldo Bajo: por debajo de 300 dólares
b. Sueldo Normal: entre 300 a 900
c. Sueldo mejor de lo normal: más de 900 dólares
"""
sueldo_enero_a_junio = 300
sueldo_julio_a_octubre = 500
sueldo_noviembre_a_diciembre = 700

sueldo_promedio = (sueldo_enero_a_junio + sueldo_julio_a_octubre + sueldo_noviembre_a_diciembre) / 3

if sueldo_promedio < 300:
    print("El empleado tiene un sueldo bajo")
elif sueldo_promedio >= 300 and sueldo_promedio <= 900:
    print("El empleado tiene sueldo normal")
elif sueldo_promedio > 900:
    print("El empleado tiene un sueldo mejor de lo normal")