def aplicar_iva(precio):
    if precio < 1000:
        precio_con_iva = precio
    else:
        precio_con_iva = precio * 1.21
    return precio_con_iva

print(aplicar_iva(800))
print(aplicar_iva(1500))

resultado = aplicar_iva(1000)
print(resultado)