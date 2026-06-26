#Ejercicio 12
#Una panadería vende barras de pan a 3.49€ cada una.
#El pan que no es del día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número
#de barras vendidas que no son del día.
#Después el programa debe mostrar el precio habitual de una barra de pan,
#el descuento que se le hace por no ser fresca y el coste final total.

precio_pan = 3.49

descuento = 0.6

pan_descuento = precio_pan * descuento

barra_pan_pasado = int(input("Ingresa la cantidad de barras de pan que no son del dia: "))

costo_total = round(barra_pan_pasado * pan_descuento,2)

print (f"El precio habitual del pan es {precio_pan}€ ")

descuento = int(descuento*100)

print (f"El descuento del pan por no ser fresco es {descuento}%")

print (f"El costo final total de los panes es {costo_total}€")