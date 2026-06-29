#Ejercicio 5
#Escribir un programa que pida al usuario que introduzca
#una frase en la consola y muestre por pantalla la frase invertida.

palabra = input("Introduce una frase: ")

palabra_invertida = palabra[::-1]

print(f"{palabra_invertida}")