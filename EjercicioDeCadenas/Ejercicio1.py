#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola
#y un número entero e imprima por pantalla en líneas distintas
#el nombre del usuario tantas veces como el número introducido.

nombre_usuario =input ("Cuál es tu nombre? ")
numero_entero = input ("Escribe un número entero: ")

numero_entero = int(numero_entero)

for i in range(numero_entero):
    print (f"{i+1}. {nombre_usuario}")