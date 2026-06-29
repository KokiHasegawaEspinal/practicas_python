#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca
#una frase en la consola y una vocal, y después muestre por
#pantalla la misma frase pero con la vocal introducida en mayúscula.

palabra = input("Introduce una frase y una vocal: ")

vocal_mayuscula = palabra[-2:]
palabra_sin_vocal = palabra[0:len]

print(vocal_mayuscula)
print(palabra_sin_vocal)