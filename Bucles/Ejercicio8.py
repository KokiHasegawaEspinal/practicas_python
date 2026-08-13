#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y
#muestre por pantalla un triángulo rectángulo como el de más abajo.

#   1
#   3 1
#   5 3 1
#   7 5 3 1
#   9 7 5 3 1

numero_usuario = int(input("Ingresa un número entero: "))

if numero_usuario >= 1:
    for i in range(1, numero_usuario + 1):
        # Genera los valores impares desde el valor actual (2*i - 1) hasta 1 bajando de 2 en 2
        for j in range(2 * i - 1, 0, -2):
            print(j, end=" ")
        print()  # Salto de línea al terminar cada fila
else:
    print("Valor no válido, ingresa un número entero!")