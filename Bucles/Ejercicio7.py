#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1,13):
    print(f"Tabla del {i}")
    for j in range(1,13):
        print(f"{i} * {j} = {i*j}")
    print(" ")