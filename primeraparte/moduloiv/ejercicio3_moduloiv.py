"""
Hacer un script contador de 0 hasta 10, que vaya mostrando los números segundo a segundo.
"""
import time

i = 0

while i < 10:
    print(i)
    time.sleep(1)
    i = i + 1