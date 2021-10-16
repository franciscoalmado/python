a = 1
b = 1
c = -6

discriminante = b**2 - 4*a*c
print("Discriminante:", discriminante)

resultado_raiz = discriminante ** (1/2)
print("Resultado de la raiz:", resultado_raiz)

x1 = (-b + resultado_raiz) / 2*a
x2 = (-b - resultado_raiz) / 2*a

print("Raiz 1:", x1)
print("Raiz 2:", x2)