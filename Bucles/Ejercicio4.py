#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre
#por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero_usuario = int(input("Ingresa un número entero positivo: "))

primero = True

if numero_usuario >= 1:
    for i in range(9, -1, -1):
        if primero:
            print(f"{i}", end = "" )
            primero = False
        else:
            print(",", i, end="")