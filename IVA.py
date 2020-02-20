#Cristhian Alejandro Frias Portillo

PORCENTAJE_IVA = 16

conteo_productos = 1
precio_total = 0  

while conteo_productos <= 5:
    mensaje = "Ingresa el precio del producto número {}: ".format(
        conteo_productos)
    precio_como_cadena = input(mensaje)
 
    precio = float(precio_como_cadena)

    precio_total = precio_total + precio
 
    conteo_productos = conteo_productos + 1

aumento = precio_total * (PORCENTAJE_IVA / 100)  

precio_con_iva = precio_total + aumento

print("Total: ${}".format(precio_total))
print("IVA: ${}".format(aumento))
print("Total con IVA: ${}".format(precio_con_iva))
