primos = [1, 2, 3, 5, 7, 11, 13]

for numero in primos:
    if numero == 5:
        continue
    print(numero)

for numero in primos:
    if numero != 5:
        print(numero)

for numero in primos:
    if numero == 5:
        break
    print(numero)
print("Fin de programa")