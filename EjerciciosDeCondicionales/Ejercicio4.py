#Ejercicio 4
#Escribir un programa que pida al usuario un número
#entero y muestre por pantalla si es par o impar.

numero = int(input("Ingresa un numero entero: "))

if numero % 2 == 0:
    print(f"El número que ingresaste es par!")
else:
    print(f"El número que ingresaste es impar!")