#Ejercicio 11
#Escribir un programa que pregunte el nombre el un producto,
#su precio y un número de unidades y muestre por pantalla una
#cadena con el nombre del producto seguido de su precio unitario
#con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre_producto = input("Ingresa el nombre del producto: ")
precio_producto = input("Ingresa su precio: ")
unidades_producto = input("Ingresa el numero de unidades que deseas adquirir: ")

precio_producto = float(precio_producto)
unidades_producto = int(unidades_producto)

###########################################
#print(f"{precio_producto:09.2f}")

#La parte :09.2f significa:

#.2f → mostrar siempre 2 decimales.
#9 → ocupar un ancho total de 9 caracteres.
#0 → rellenar con ceros a la izquierda.
############################################

print(f"El nombre del producto es {nombre_producto}")
print(f"El precio del producto es S/{precio_producto:09.2f}")
print(f"Números de unidades adquiridas: {unidades_producto:03d}")

costo_total = precio_producto*unidades_producto

print(f"El costo total es: S/{costo_total:011.2f}")

print(f"{nombre_producto} {precio_producto:09.2f} {unidades_producto:03d} {costo_total:011.2f}")