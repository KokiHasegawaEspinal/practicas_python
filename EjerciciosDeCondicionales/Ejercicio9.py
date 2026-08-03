#Ejercicio 9
#Escribir un programa para una empresa que tiene salas de juegos
#para todas las edades y quiere calcular de forma automática el
#precio que debe cobrar a sus clientes por entrar. El programa
#debe preguntar al usuario la edad del cliente y mostrar el precio
# de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
# si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

#| Edad del Cliente  |  Precio  |
#|-------------------|----------|
#|  Menor de 4 años  |  Gratis  |
#| Entre 4 y 18 años |    5€    |
#| Mayor de 18 años  |   10€    |

precio_entrada = {
    "A":0,
    "B":5,
    "C":1
}

edad_cliente = int(input("Que edad tienes? "))

if edad_cliente <4:
    precio = "A"
elif edad_cliente <= 18:
    precio = "B"
else:
    precio = "C"
    
print(f"El precio de la entrada es {precio_entrada[precio]}€ porque tienes {edad_cliente} años de edad") 