#Ejercicio 8
#Escribir un programa que pregunte por consola el precio de
#un producto en euros con dos decimales y muestre por pantalla
#el número de euros y el número de céntimos del precio introducido.

precio_producto = input("Introduce el precio del producto en euros con dos decimales: ")

buscar_punto = precio_producto.find(".")
print(buscar_punto)

precio_entero = precio_producto[:buscar_punto]
print(f"Euros: {precio_entero}")

precio_decimal = precio_producto[buscar_punto+1:]
print(f"Centimos: {precio_decimal}")
