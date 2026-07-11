#Ejercicio 3
#Escribir un programa que pida al usuario dos
#números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.

primer_numero = int(input("Ingresa un número (Dividendo): "))
segundo_numero = int(input("Ingresa otro numero (Divisor): "))


if segundo_numero != 0:
    division = (primer_numero / segundo_numero)
    print(f"{primer_numero} / {segundo_numero} = {division:.2f}")
else:
    print(f"Error identificado, el divisor debe ser distinto de cero")