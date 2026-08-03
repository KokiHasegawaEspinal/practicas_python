#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Escribe un numero entero positivo: "))

primero = True

for i in range (1, numero+1):
    if i % 2 != 0:
        if primero:
            print(f"{i}", end="")
            primero = False
        else:    
            print (f", {i}", end="")