def aplicar_iva(precio):
    precio_con_iva = precio * 1.21
    return precio_con_iva

precio = input("Introduzca el precio del producto: ")
precio = int(precio)

if aplicar_iva(precio) > 1500:
    print("Tenés descuento")
else:
    print("No tenés descuento")