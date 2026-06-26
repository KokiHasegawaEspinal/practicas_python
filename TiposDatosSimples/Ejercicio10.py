#Ejercicio 10
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de
#cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
#en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último
#pedido y calcule el peso total del paquete que será enviado.

# Peso del payaso en gramos
peso_payaso = 112

# peso de la muñeca en gramos
peso_muneca = 75

numero_payasos = int(input("Introduce el numero de payasos a enviar: "))

numero_de_munecas = int(input("Introduce el numero de muñecas a enviar: "))

print (f"El numero de payasos vendidos en el último pedido es {numero_payasos}")

print (f"El numero de muñecas vendidas en el último pedido es {numero_de_munecas}")

peso_paquete = (peso_payaso*numero_payasos) + (peso_muneca*numero_de_munecas)

print (f"El peso total del paquete a ser enviado es {peso_paquete}")