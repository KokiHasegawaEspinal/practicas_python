#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad
#y muestre por pantalla si es mayor de edad o no.

edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario >= 18:
    print(f"Es mayor de edad")
    
else:
    print(f"Es menor de edad")