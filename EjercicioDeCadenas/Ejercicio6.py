#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca
#una frase en la consola y una vocal, y después muestre por
#pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

vocal_mayuscula = vocal.upper()

frase_vocal_mayuscula  = frase.replace(vocal,vocal_mayuscula)
print(frase_vocal_mayuscula)