#Ejercicio 6
#Escribir un programa que pida al usuario un número
#entero y muestre por pantalla un triángulo rectángulo
#como el de más abajo, de altura el número introducido.

#   *
#   **
#   ***
#   ****
#   *****

numero_usuario = int(input("Introduce un número entero: "))
triangulo = ""
if numero_usuario >= 1:
    for i in range(0, numero_usuario):
#        triangulo = triangulo + "*"
        triangulo += "*"
        print (triangulo)
else:
    print("Vuelve a intentar")