#Ejercicio 10
#Escribir un programa que pida al usuario un número
#entero y muestre por pantalla si es un número primo o no.

numero_usuario = int(input("Ingresa un número: "))

numero_primo = True

if numero_usuario <= 1:
    numero_primo = False

for i in range (2, numero_usuario):
    if numero_usuario % i == 0:
        numero_primo = False
        break
if numero_primo:
    print(f" {numero_usuario} es un número primo!")
else:
    print(f"{numero_usuario} no es número primo!")